from __future__ import annotations

import locale
import os
import os.path
import shutil
import subprocess
import sys
import zipfile

from typing import cast

from ._common import translate_path
from ._env import bg3_modding_env

locale.setlocale(locale.LC_ALL, '')
LOCALE_CONVERSION_NEEDED = locale.localeconv()["decimal_point"] == ','

def initialize_dot_net() -> bool:
    try:
        # Set environment to help find .NET
        __program_files_path = os.getenv('ProgramFiles')
        __system_drive = os.getenv('SystemDrive')
        if __program_files_path is None:
            if __system_drive is not None:
                __program_files_path = __system_drive + "\\Program Files"
            else:
                __program_files_path = "C:\\Program Files"
        os.environ["DOTNET_ROOT"] = os.path.join(__program_files_path, 'dotnet')

        from pythonnet import set_runtime
        from clr_loader import get_coreclr

        # This should find the latest .NET runtime automatically
        set_runtime(get_coreclr())

        import clr
        global LSLIB_INITIALIZED
        LSLIB_INITIALIZED = False
    except:
        return False
    return True


DOTNET_INITIALIZED: bool = initialize_dot_net()
LSLIB_INITIALIZED: bool = False
PAK_KEYS = dict[str, str]()
PAK_CACHE = dict[str, dict[str, object]]()

class bg3_modding_tool:
    __env: bg3_modding_env
    __work_dir: str
    __toolkit_present: bool

    def __init__(self, env: bg3_modding_env) -> None:
        self.__env = env
        self.__work_dir = os.path.join(env.env_root_path, "build")
        self.__toolkit_present = env.bg3_toolkit_path and os.path.isdir(env.bg3_toolkit_path)
        if os.path.isdir(self.__work_dir):
            shutil.rmtree(self.__work_dir)
        os.makedirs(self.__work_dir)
        global LSLIB_INITIALIZED
        if not LSLIB_INITIALIZED:
            lib_path = os.path.join(env.lslib_path, 'Packed', 'Tools')

            sys.path.append(lib_path)
            if self.__toolkit_present:
                sys.path.append(env.bg3_toolkit_path)

            import clr
            clr.AddReference("System.IO") # type: ignore
            clr.AddReference("LSLib") # type: ignore
            if self.__toolkit_present:
                clr.AddReference("Modio") # type: ignore
            LSLIB_INITIALIZED = True

    def __get_package(self, pak_path: str) -> dict[str, object]:
        if not os.path.isfile(pak_path):
            raise FileNotFoundError('Pak file does not exist: ' + pak_path)
        key = pak_path + '|' + str(os.stat(pak_path).st_mtime)
        if key not in PAK_CACHE:
            if pak_path in PAK_KEYS:
                old_pak_key = PAK_KEYS[pak_path]
                del PAK_CACHE[old_pak_key]
                del PAK_KEYS[pak_path]
            pak_files = dict[str, object]()
            try:
                from LSLib.LS import PackageReader # type: ignore

                pak_reader = PackageReader() # type: ignore
                package = cast(object, pak_reader.Read(pak_path)) # type: ignore

                for file_info in package.Files: # type:ignore
                    file_name = str(file_info.Name) # type:ignore
                    pak_files[file_name] = file_info
                PAK_KEYS[pak_path] = key
                PAK_CACHE[key] = pak_files
                PAK_CACHE[key]['$package$'] = package
            except BaseException as exc:
                raise RuntimeError(f'Failed to read pak {pak_path}') from exc
        else:
            pak_files = PAK_CACHE[key]
        return pak_files

    def __convert(self, src_path: str, dest_path: str) -> None:
        try:
            from LSLib.LS import ResourceConversionParameters, ResourceLoadParameters, ResourceUtils # type: ignore
            from LSLib.LS.Enums import Game # type: ignore

            res_fmt = ResourceUtils.ExtensionToResourceFormat(dest_path) # type: ignore
            conv_params = ResourceConversionParameters.FromGameVersion(Game.BaldursGate3) # type: ignore
            load_params = ResourceLoadParameters.FromGameVersion(Game.BaldursGate3) # type: ignore
            resource = ResourceUtils.LoadResource(src_path, load_params) # type: ignore
            ResourceUtils.SaveResource(resource, dest_path, res_fmt, conv_params) # type: ignore
        except BaseException as exc:
            raise RuntimeError(f'Conversion of "{src_path}" to "{dest_path}" failed.') from exc

    def __convert_loca(self, src_path: str, dest_path: str) -> None:
        try:
            from LSLib.LS import LocaUtils # type: ignore

            loca = LocaUtils.Load(src_path) # type: ignore
            LocaUtils.Save(loca, dest_path) # type: ignore
        except BaseException as exc:
            raise RuntimeError(f'Conversion of "{src_path}" to "{dest_path}" failed.') from exc

    @property
    def work_dir(self) -> str:
        return self.__work_dir

    @property
    def env(self) -> bg3_modding_env:
        return self.__env

    @property
    def toolkit_present(self) -> bool:
        return self.__toolkit_present

    def get_file_path(self, relative_file_path: str) -> str:
        return os.path.join(self.__work_dir, "unpacked", translate_path(relative_file_path))

    def list(self, pak_name: str) -> list[str]:
        if not pak_name.endswith(".pak"):
            pak_name += ".pak"
        if os.path.isfile(pak_name):
            src_path = pak_name
        else:
            src_path = os.path.join(self.__env.bg3_data_path, translate_path(pak_name))
        if not os.path.isfile(src_path):
            raise FileNotFoundError("Pak not found: " + src_path)
        try:
            package = self.__get_package(src_path)
            return [fn for fn in package.keys() if fn != '$package$']
        except BaseException as exc:
            raise RuntimeError(f'Failed to list files in pak {src_path}') from exc

    def unpack(self, pak_name: str, target: str) -> str:
        if not pak_name.endswith(".pak"):
            pak_name += ".pak"
        if os.path.isfile(pak_name):
            src_path = pak_name
        else:
            src_path = os.path.join(self.__env.bg3_data_path, translate_path(pak_name))
        package = self.__get_package(src_path)
        if target not in package:
            raise FileNotFoundError(f'File "{target}" is not found in pak "{src_path}".')

        dest_path = os.path.join(self.__work_dir, "unpacked", *target.split('/'))
        os.makedirs(os.path.dirname(dest_path), exist_ok=True)
        if os.path.isfile(dest_path):
            os.unlink(dest_path)

        source_stream = None
        destination_stream = None
        try:
            from System.IO import FileAccess, FileMode, FileStream # type: ignore

            file_info = package[target]
            source_stream = file_info.CreateContentReader() # type: ignore
            destination_stream = FileStream(dest_path, FileMode.Create, FileAccess.Write) # type: ignore
            source_stream.CopyTo(destination_stream) # type: ignore
        except BaseException as exc:
            raise RuntimeError(f'Writing to "{dest_path}" failed. File "{target}" was not unpacked from "{src_path}".') from exc
        finally:
            if source_stream is not None:
                source_stream.Close() # type: ignore
            if destination_stream is not None:
                destination_stream.Close() # type: ignore

        if os.path.isfile(dest_path):
            ext_pos = dest_path.rfind('.')
            if ext_pos == -1:
                raise RuntimeError(f'file {dest_path} has no extension')
            ext = dest_path[ext_pos:].lower()
            return dest_path[:-len(ext)] + ext
        raise RuntimeError(f"Failed to unpack {target} from {pak_name}.")

    def pack(self, mod_dir_path: str, dest_pak_file_path: str) -> str:
        if not os.path.isdir(mod_dir_path):
            raise FileNotFoundError("Mod directory not found: " + mod_dir_path)
        os.makedirs(os.path.dirname(dest_pak_file_path), exist_ok=True)
        if os.path.isfile(dest_pak_file_path):
            os.unlink(dest_pak_file_path)

        try:
            from LSLib.LS import CompressionMethod, LSCompressionLevel, PackageBuildData, Packager # type: ignore
            from LSLib.LS.Enums import PackageVersion # type: ignore

            pak_build_data = cast(object, PackageBuildData()) # type: ignore
            pak_build_data.Version = PackageVersion.V18 # type: ignore
            pak_build_data.Priority = 30  # type: ignore
            pak_build_data.Compression = CompressionMethod.LZ4 # type: ignore
            pak_build_data.CompressionLevel = LSCompressionLevel.Default # type: ignore

            packager = cast(object, Packager()) # type: ignore
            packager.CreatePackage(dest_pak_file_path, mod_dir_path, pak_build_data) # type: ignore
        except BaseException as exc:
            raise RuntimeError(f"Failed to pack {mod_dir_path}") from exc

        return dest_pak_file_path

    def upload(
            self,
            mod_name: str,
            mod_uuid: str,
            mod_version: tuple[int, int, int, int],
            pak_file_path: str,
            mod_publish_handle: int
    ) -> str:
        if not self.__toolkit_present:
            raise RuntimeError(f'cannot upload {pak_file_path} because BG3 modding toolkit is not present')
        pak_name = f'{mod_name}_{mod_uuid}.pak'
        mod_zip_file_path = pak_file_path + '.zip'
        with zipfile.ZipFile(mod_zip_file_path, 'w', compression = zipfile.ZIP_DEFLATED) as zipf:
            zipf.write(pak_file_path, arcname = pak_name)
        try:
            from System import Uri # type: ignore
            from System.IO import FileInfo # type: ignore
            from Modio import Client, Credentials, EditFile, NewFile # type: ignore
            modio_uri = Uri(self.__env.modio_endpoint) # type: ignore
            modio_credentials = Credentials(self.__env.modio_api_key, self.__env.modio_api_token) # type: ignore
            modio_client = Client(modio_uri, modio_credentials) # type: ignore
            modio_game_client = modio_client.Games[6715] # type: ignore
            modio_mod_client = modio_game_client.Mods[mod_publish_handle] # type: ignore
            modio_files_client = modio_mod_client.Files # type: ignore
            file_info = FileInfo(mod_zip_file_path) # type: ignore
            modio_new_file = NewFile(file_info) # type: ignore
            modio_file = modio_files_client.Add(modio_new_file).Result # type: ignore
            modio_edit_file = EditFile() # type: ignore
            modio_edit_file.Version = f'{mod_version[0]}.{mod_version[1]}.{mod_version[2]}.{mod_version[3]}' # type: ignore
            modio_files_client.Edit(modio_file.Id, modio_edit_file).Result # type: ignore
            return modio_file.Download.BinaryUrl.AbsoluteUri # type: ignore
        except BaseException as exc:
            raise RuntimeError(f"Failed to upload {pak_file_path}") from exc

    def convert_lsf_to_lsx(self, target: str) -> str:
        if target.endswith(".lsx.lsf"):
            dest_path = target[:-4]
        elif target.endswith(".lsf"):
            dest_path = target + ".lsx"
        else:
            raise ValueError(f"Unexpected input file: {target}; expected an .lsx.lsf or an .lsf file.")
        if os.path.isfile(dest_path):
            os.unlink(dest_path)

        self.__convert(target, dest_path)

        if os.path.isfile(dest_path) and os.stat(dest_path).st_size > 0:
            os.unlink(target)
            return dest_path
        raise RuntimeError(f"Failed to convert {target} to .lsx")

    def convert_lsx_to_lsf(self, target: str) -> str:
        if target.endswith(".lsf.lsx"):
            dest_path = target[:-4]
        elif target.endswith(".lsx"):
            dest_path = target + ".lsf"
        else:
            raise ValueError(f"Unexpected input file: {target}; expected an .lsf.lsx or an .lsx file.")
        if os.path.isfile(dest_path):
            os.unlink(dest_path)

        self.__convert(target, dest_path)

        if os.path.isfile(dest_path) and os.stat(dest_path).st_size > 0:
            os.unlink(target)
            return dest_path
        raise RuntimeError(f"Failed to convert {target} to .lsf")

    def convert_lsj_to_lsx(self, target: str) -> str:
        if target.endswith(".lsx.lsj"):
            dest_path = target[:-4]
        elif target.endswith(".lsj"):
            dest_path = target + ".lsx"
        else:
            raise ValueError(f"Unexpected input file: {target}; expected an .lsx.lsj or an .lsj file.")
        if os.path.isfile(dest_path):
            os.unlink(dest_path)

        self.__convert(target, dest_path)

        if os.path.isfile(dest_path) and os.stat(dest_path).st_size > 0:
            os.unlink(target)
            return dest_path
        raise RuntimeError(f"Failed to convert {target} to .lsf")

    def convert_loca_to_xml(self, target: str) -> str:
        if not target.endswith(".loca"):
            raise ValueError(f"Unexpected input file: {target}; expected an .loca file.")
        dest_path = target + ".xml"
        if os.path.isfile(dest_path):
            os.unlink(dest_path)

        self.__convert_loca(target, dest_path)

        if os.path.isfile(dest_path) and os.stat(dest_path).st_size > 0:
            os.unlink(target)
            return dest_path
        raise RuntimeError(f"Failed to convert {target} to .xml")

    def convert_xml_to_loca(self, target: str) -> str:
        if not target.endswith(".loca.xml"):
            raise ValueError(f"Unexpected input file: {target}; expected an .loca.xml file.")
        dest_path = target[:-4]
        if os.path.isfile(dest_path):
            os.unlink(dest_path)

        self.__convert_loca(target, dest_path)

        if os.path.isfile(dest_path) and os.stat(dest_path).st_size > 0:
            os.unlink(target)
            return dest_path
        raise RuntimeError(f"Failed to convert {target} to .loca")

    def unpack_pak(self, pak_name: str, destination_path: str | None = None) -> str:
        if not pak_name.endswith(".pak"):
            pak_name += ".pak"
        if os.path.isfile(pak_name):
            src_path = pak_name
            pak_file_name = pak_name
        else:
            src_path = os.path.join(self.__env.bg3_data_path, translate_path(pak_name))
            pak_file_name = os.path.basename(src_path)
        if not os.path.isfile(src_path):
            raise FileNotFoundError("Pak not found: " + src_path)
        if destination_path is None:
            dest_path = os.path.join(self.__work_dir, "unpacked", pak_file_name)
        else:
            dest_path = destination_path
        os.makedirs(dest_path, exist_ok=True)

        try:
            from LSLib.LS import Packager # type: ignore
            packager = cast(object, Packager()) # type: ignore
            packager.UncompressPackage(src_path, dest_path) # type: ignore
        except BaseException as exc:
            raise RuntimeError(f"Failed to unpack {pak_name}") from exc
        return dest_path

    def unpack_and_convert(self, pak_path: str, dest_dir_path: str | None = None) -> str:
        if not os.path.isfile(pak_path):
            raise RuntimeError(f'Source path is not a pak file: {pak_path}')
        if dest_dir_path is None:
            dest_dir_path = os.path.splitext(pak_path)[0] + '_unpacked'
            if os.path.exists(dest_dir_path):
                shutil.rmtree(dest_dir_path)
            os.makedirs(dest_dir_path, exist_ok = True)
        elif os.path.isfile(dest_dir_path):
            raise RuntimeError(f'destination path is a file {dest_dir_path}')
        os.makedirs(dest_dir_path, exist_ok = True)

        dest_path = self.unpack_pak(pak_path, dest_dir_path)

        def recurse_convert(path: str) -> None:
            dirs = list[str]()
            for p in os.listdir(path):
                p = os.path.join(path, p)
                if os.path.isfile(p):
                    if len(p) > 5 and p[-5:] == '.loca':
                        self.convert_loca_to_xml(p)
                    elif len(p) > 4 and p[-4:] == '.lsf':
                        self.convert_lsf_to_lsx(p)
                    elif len(p) > 4 and p[-4:] == '.lsj':
                        self.convert_lsj_to_lsx(p)
                else:
                    dirs.append(p)
            for p in dirs:
                recurse_convert(p)

        recurse_convert(dest_path)
        return dest_path

    #
    # Deprecated implementation
    #

    def sanity_check_deprecated(self) -> bool:
        proc = subprocess.run(
            [
                self.__env.divine_exe,
            ],
            capture_output=True)
        if proc.returncode == 0:
            return True
        return False

    def list_deprecated(self, pak_name: str) -> list[str]:
        if not pak_name.endswith(".pak"):
            pak_name += ".pak"
        if os.path.isfile(pak_name):
            src_path = pak_name
        else:
            src_path = os.path.join(self.__env.bg3_data_path, translate_path(pak_name))
        if not os.path.isfile(src_path):
            raise FileNotFoundError("Pak not found: " + src_path)
        proc = subprocess.run(
            [
                self.__env.divine_exe,
                '-g', 'bg3',
                '-s', f'{src_path}',
                '-a', 'list-package'
            ],
            capture_output=True)
        if proc.returncode == 0:
            s = proc.stdout.decode()
            n = 0
            result = list[str]()
            while n < len(s):
                pos = s.find("\t", n)
                if pos == -1:
                    break
                result.append(s[n : pos])
                n = s.find("\n", pos)
                if n == -1:
                    break
                n += 1
            return result
        raise RuntimeError(f"Failed to list {pak_name}\nstdout: {proc.stdout}\nstderr: {proc.stderr}")

    def unpack_deprecated(self, pak_name: str, target: str) -> str:
        if not pak_name.endswith(".pak"):
            pak_name += ".pak"
        if os.path.isfile(pak_name):
            src_path = pak_name
        else:
            src_path = os.path.join(self.__env.bg3_data_path, translate_path(pak_name))
        if not os.path.isfile(src_path):
            raise FileNotFoundError("Pak not found: " + src_path)
        dest_path = os.path.join(self.__work_dir, "unpacked", *target.split('/'))
        os.makedirs(os.path.dirname(dest_path), exist_ok=True)
        if os.path.isfile(dest_path):
            os.unlink(dest_path)
        proc = subprocess.run(
            [
                self.__env.divine_exe,
                '-g', 'bg3',
                '-s', f'{src_path}',
                '-d', f'{dest_path}',
                '-f', target,
                '-a', 'extract-single-file'
            ],
            capture_output=True)
        if proc.returncode == 0 and os.path.isfile(dest_path):
                ext_pos = dest_path.rfind('.')
                if ext_pos == -1:
                    raise RuntimeError(f'file {dest_path} has no extension')
                ext = dest_path[ext_pos:].lower()
                return dest_path[:-len(ext)] + ext
        raise RuntimeError(f"Failed to unpack {target} from {pak_name}\nerror code {proc.returncode}\nstdout: {proc.stdout}\nstderr: {proc.stderr}")

    def unpack_pak_deprecated(self, pak_name: str, destination_path: str | None = None) -> str:
        if not pak_name.endswith(".pak"):
            pak_name += ".pak"
        if os.path.isfile(pak_name):
            src_path = pak_name
            pak_file_name = pak_name
        else:
            src_path = os.path.join(self.__env.bg3_data_path, translate_path(pak_name))
            pak_file_name = os.path.basename(src_path)
        if not os.path.isfile(src_path):
            raise FileNotFoundError("Pak not found: " + src_path)
        if destination_path is None:
            dest_path = os.path.join(self.__work_dir, "unpacked", pak_file_name)
        else:
            dest_path = destination_path
        os.makedirs(dest_path, exist_ok=True)
        proc = subprocess.run(
            [
                self.__env.divine_exe,
                '-g', 'bg3',
                '-s', f'{src_path}',
                '-d', f'{dest_path}',
                '-a', 'extract-package'
            ],
            capture_output=True)
        if proc.returncode != 0:
            raise RuntimeError(f"Failed to unpack {pak_name}\nerror code {proc.returncode}\nstdout: {proc.stdout}\nstderr: {proc.stderr}")
        return dest_path

    def unpack_and_convert_deprecated(self, pak_path: str, dest_dir_path: str | None = None) -> str:
        if not os.path.isfile(pak_path):
            raise RuntimeError(f'source path is not a pak file: {pak_path}')
        if dest_dir_path is None:
            dest_dir_path = os.path.splitext(pak_path)[0] + '_unpacked'
            if os.path.exists(dest_dir_path):
                shutil.rmtree(dest_dir_path)
            os.makedirs(dest_dir_path, exist_ok = True)
        elif os.path.isfile(dest_dir_path):
            raise RuntimeError(f'destination path is a file {dest_dir_path}')
        os.makedirs(dest_dir_path, exist_ok = True)
        proc = subprocess.run(
            [
                self.__env.divine_exe,
                '-g', 'bg3',
                '-s', f'{pak_path}',
                '-d', f'{dest_dir_path}',
                '-a', 'extract-package'
            ],
            capture_output=True)
        if proc.returncode != 0:
            raise RuntimeError(f"Failed to unpack {pak_path}\nerror code {proc.returncode}\nstdout: {proc.stdout}\nstderr: {proc.stderr}")
        
        def recurse_convert(path: str) -> None:
            dirs = list[str]()
            for p in os.listdir(path):
                p = os.path.join(path, p)
                if os.path.isfile(p):
                    proc = None
                    if len(p) > 5 and p[-5:] == '.loca':
                        proc = subprocess.run(
                            [
                                self.__env.divine_exe,
                                '-g', 'bg3',
                                '-s', f'{p}',
                                '-d', f'{p}.xml',
                                '-a', 'convert-loca'
                            ],
                            capture_output=True)
                    elif len(p) > 4 and p[-4:] == '.lsf':
                        proc = subprocess.run(
                            [
                                self.__env.divine_exe,
                                '-g', 'bg3',
                                '-s', f'{p}',
                                '-d', f'{p}.lsx',
                                '-a', 'convert-resource'
                            ],
                            capture_output=True)
                    if proc is not None and proc.returncode != 0:
                        raise RuntimeError(f'failed to convert {p}\nerror code {proc.returncode}\nstdout: {proc.stdout}\nstderr: {proc.stderr}')
                else:
                    dirs.append(p)
            for p in dirs:
                recurse_convert(p)

        recurse_convert(dest_dir_path)
        return dest_dir_path

    def pack_deprecated(self, mod_dir_path: str, dest_pak_file_path: str) -> str:
        if not os.path.isdir(mod_dir_path):
            raise FileNotFoundError("Mod directory not found: " + mod_dir_path)
        os.makedirs(os.path.dirname(dest_pak_file_path), exist_ok=True)
        if os.path.isfile(dest_pak_file_path):
            os.unlink(dest_pak_file_path)
        proc = subprocess.run(
            [
                self.__env.divine_exe,
                '-g', 'bg3',
                '-s', f'{mod_dir_path}',
                '-d', f'{dest_pak_file_path}',
                '-a', 'create-package',
                '--package-priority', '30'
            ],
            capture_output=True)
        if proc.returncode == 0 and os.path.isfile(dest_pak_file_path):
            return dest_pak_file_path
        raise RuntimeError(f"Failed to pack {mod_dir_path}\nerror code {proc.returncode}\nstdout: {proc.stdout}\nstderr: {proc.stderr}")

    def convert_lsf_to_lsx_deprecated(self, target: str) -> str:
        if target.endswith(".lsx.lsf"):
            dest_path = target[:-4]
        elif target.endswith(".lsf"):
            dest_path = target + ".lsx"
        else:
            raise ValueError(f"Unexpected input file: {target}; expected an .lsx.lsf or an .lsf file.")
        if os.path.isfile(dest_path):
            os.unlink(dest_path)
        proc = subprocess.run(
            [
                self.__env.divine_exe,
                '-g', 'bg3',
                '-s', f'{target}',
                '-d', f'{dest_path}',
                '-a', 'convert-resource'
            ],
            capture_output=True)
        if proc.returncode == 0 and os.path.isfile(dest_path):
            os.unlink(target)
            return dest_path
        raise RuntimeError(f"Failed to convert {target} to .lsx\nerror code {proc.returncode}\nstdout: {proc.stdout}\nstderr: {proc.stderr}")

    def convert_lsx_to_lsf_deprecated(self, target: str) -> str:
        if target.endswith(".lsf.lsx"):
            dest_path = target[:-4]
        elif target.endswith(".lsx"):
            dest_path = target + ".lsf"
        else:
            raise ValueError(f"Unexpected input file: {target}; expected an .lsf.lsx or an .lsx file.")
        if os.path.isfile(dest_path):
            os.unlink(dest_path)
        proc = subprocess.run(
            [
                self.__env.divine_exe,
                '-g', 'bg3',
                '-s', f'{target}',
                '-d', f'{dest_path}',
                '-a', 'convert-resource',
                '-l', 'all'
            ],
            capture_output=True)
        if proc.returncode == 0 and os.path.isfile(dest_path) and os.stat(dest_path).st_size > 0:
            os.unlink(target)
            return dest_path
        raise RuntimeError(f"Failed to convert {target} to .lsf\nerror code {proc.returncode}\nstdout: {proc.stdout}\nstderr: {proc.stderr}")

    def convert_lsj_to_lsx_deprecated(self, target: str) -> str:
        if target.endswith(".lsx.lsj"):
            dest_path = target[:-4]
        elif target.endswith(".lsj"):
            dest_path = target + ".lsx"
        else:
            raise ValueError(f"Unexpected input file: {target}; expected an .lsx.lsj or an .lsj file.")
        if os.path.isfile(dest_path):
            os.unlink(dest_path)
        proc = subprocess.run(
            [
                self.__env.divine_exe,
                '-g', 'bg3',
                '-s', f'{target}',
                '-d', f'{dest_path}',
                '-a', 'convert-resource',
                '-l', 'all'
            ],
            capture_output=True)
        if proc.returncode == 0 and os.path.isfile(dest_path) and os.stat(dest_path).st_size > 0:
            os.unlink(target)
            return dest_path
        raise RuntimeError(f"Failed to convert {target} to .lsf\nerror code {proc.returncode}\nstdout: {proc.stdout}\nstderr: {proc.stderr}")

    def convert_loca_to_xml_deprecated(self, target: str) -> str:
        if not target.endswith(".loca"):
            raise ValueError(f"Unexpected input file: {target}; expected an .loca file.")
        dest_path = target + ".xml"
        if os.path.isfile(dest_path):
            os.unlink(dest_path)
        proc = subprocess.run(
            [
                self.__env.divine_exe,
                '-g', 'bg3',
                '-s', f'{target}',
                '-d', f'{dest_path}',
                '-a', 'convert-loca'
            ],
            capture_output=True)
        if proc.returncode == 0 and os.path.isfile(dest_path):
            os.unlink(target)
            return dest_path
        raise RuntimeError(f"Failed to convert {target} to .xml\nerror code {proc.returncode}\nstdout: {proc.stdout}\nstderr: {proc.stderr}")

    def convert_xml_to_loca_deprecated(self, target: str) -> str:
        if not target.endswith(".loca.xml"):
            raise ValueError(f"Unexpected input file: {target}; expected an .loca.xml file.")
        dest_path = target[:-4]
        if os.path.isfile(dest_path):
            os.unlink(dest_path)
        proc = subprocess.run(
            [
                self.__env.divine_exe,
                '-g', 'bg3',
                '-s', f'{target}',
                '-d', f'{dest_path}',
                '-a', 'convert-loca'
            ],
            capture_output=True)
        if proc.returncode == 0 and os.path.isfile(dest_path):
            os.unlink(target)
            return dest_path
        raise RuntimeError(f"Failed to convert {target} to .loca\nerror code {proc.returncode}\nstdout: {proc.stdout}\nstderr: {proc.stderr}")

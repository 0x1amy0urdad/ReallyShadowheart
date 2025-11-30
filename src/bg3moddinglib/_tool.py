from __future__ import annotations

import os.path
import shutil
import subprocess

from ._common import translate_path
from ._env import bg3_modding_env

class bg3_modding_tool:
    __work_dir: str
    __env: bg3_modding_env

    def __init__(self, env: bg3_modding_env) -> None:
        self.__env = env
        self.__work_dir = os.path.join(env.env_root_path, "build")
        if os.path.isdir(self.__work_dir):
            shutil.rmtree(self.__work_dir)
        os.makedirs(self.__work_dir)

    @property
    def work_dir(self) -> str:
        return self.__work_dir

    @property
    def env(self) -> bg3_modding_env:
        return self.__env

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

    def unpack(self, pak_name: str, target: str) -> str:
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
        if os.path.isfile(dest_path):
            ext_pos = dest_path.rfind('.')
            if ext_pos == -1:
                raise RuntimeError(f'file {dest_path} has no extension')
            ext = dest_path[ext_pos:].lower()
            return dest_path[:-len(ext)] + ext
        raise RuntimeError(f"Failed to unpack {target} from {pak_name}\nerror code {proc.returncode}\nstdout: {proc.stdout}\nstderr: {proc.stderr}")

    def unpack_and_convert(self, pak_path: str, dest_dir_path: str | None = None) -> str:
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
        return dest_dir_path
        
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

    def pack(self, mod_dir_path: str, dest_pak_file_path: str) -> str:
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

    def convert_lsf_to_lsx(self, target: str) -> str:
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

    def convert_lsx_to_lsf(self, target: str) -> str:
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

    def convert_lsj_to_lsx(self, target: str) -> str:
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

    def convert_loca_to_xml(self, target: str) -> str:
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

    def convert_xml_to_loca(self, target: str) -> str:
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

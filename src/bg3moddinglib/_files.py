from __future__ import annotations

import datetime
import hashlib
import json
import os
import os.path
import shutil
import sys
import xml.etree.ElementTree as et

from ._common import get_required_bg3_attribute, translate_path
from ._meta_lsx import create_meta_lsx
from ._tool import bg3_modding_tool

type ElementTree = et.ElementTree[et.Element[str]]

class game_file:
    __tool: bg3_modding_tool
    __source_pak: str
    __relative_file_path: str
    __unpacked_file_path: str
    __converted_file_path: str | None
    __file_format: str
    __mod_specific: bool
    __rename_to: str
    __xml: ElementTree | None

    def __init__(
            self,
            tool: bg3_modding_tool,
            file_path: str,
            /,
            pak_name: str | None = None,
            source_file_path: str | None = None,
            new_file: bool = False,
            mod_specific: bool = False,
            rename_to: str = ""
    ) -> None:
        self.__tool = tool
        self.__source_pak = ''
        self.__relative_file_path = ''
        self.__unpacked_file_path = ''
        self.__converted_file_path = None
        self.__file_format = ''
        self.__mod_specific = mod_specific
        self.__rename_to = rename_to
        self.__xml = None
        if pak_name is not None:
            self.__source_pak = pak_name
            self.__relative_file_path = file_path
            self.__unpacked_file_path = tool.unpack(pak_name, file_path)
            if self.__unpacked_file_path.endswith(".lsf"):
                self.__converted_file_path = tool.convert_lsf_to_lsx(self.__unpacked_file_path)
                self.__file_format = "lsf"
            elif self.__unpacked_file_path.endswith(".loca"):
                self.__converted_file_path = tool.convert_loca_to_xml(self.__unpacked_file_path)
                self.__file_format = "loca"
            elif self.__unpacked_file_path.endswith(".lsx"):
                self.__converted_file_path = self.__unpacked_file_path
                self.__file_format = "lsx"
            elif self.__unpacked_file_path.endswith(".xml"):
                self.__converted_file_path = self.__unpacked_file_path
                self.__file_format = "xml"
            elif self.__unpacked_file_path.endswith(".lsj"):
                self.__converted_file_path = tool.convert_lsj_to_lsx(self.__unpacked_file_path)
                self.__file_format = "lsj"
            else:
                self.__converted_file_path = None
                self.__file_format = "other"
            if self.__converted_file_path is not None:
                self.__xml = et.parse(self.__converted_file_path)
        else:
            if source_file_path is not None:
                self.__unpacked_file_path = source_file_path
                self.__relative_file_path = file_path
                if self.__unpacked_file_path.endswith(".lsf.lsx"):
                    self.__converted_file_path = self.__unpacked_file_path
                    self.__unpacked_file_path = self.__unpacked_file_path[:-4]
                    self.__file_format = "lsf"
                elif self.__unpacked_file_path.endswith(".loca.xml"):
                    self.__converted_file_path = self.__unpacked_file_path
                    self.__unpacked_file_path = self.__unpacked_file_path[:-4]
                    self.__file_format = "loca"
                elif self.__unpacked_file_path.endswith(".lsx"):
                    self.__converted_file_path = self.__unpacked_file_path
                    self.__unpacked_file_path = self.__unpacked_file_path
                    self.__file_format = "lsx"
                elif self.__unpacked_file_path.endswith(".xml"):
                    self.__converted_file_path = self.__unpacked_file_path
                    self.__unpacked_file_path = self.__unpacked_file_path
                    self.__file_format = "xml"
                else:
                    self.__converted_file_path = None
                    self.__file_format = "other"
                if self.__converted_file_path is not None:
                    self.__xml = et.parse(self.__converted_file_path)
            elif new_file:
                self.__relative_file_path = file_path
                self.__unpacked_file_path = tool.get_file_path(file_path)
                os.makedirs(os.path.dirname(self.__unpacked_file_path), exist_ok=True)
                if self.__unpacked_file_path.endswith(".lsf"):
                    self.__file_format = "lsf"
                    self.__converted_file_path = None
                    self.__xml = et.ElementTree(et.fromstring('<?xml version="1.0" encoding="utf-8"?>\n<save>\n</save>\n'))
                elif self.__unpacked_file_path.endswith(".lsx"):
                    self.__file_format = "lsx"
                    self.__converted_file_path = None
                    self.__xml = et.ElementTree(et.fromstring('<?xml version="1.0" encoding="utf-8"?>\n<save>\n</save>\n'))
                elif self.__unpacked_file_path.endswith(".loca"):
                    self.__file_format = "loca"
                    self.__converted_file_path = None
                    self.__xml = et.ElementTree(et.fromstring('<?xml version="1.0" encoding="utf-8"?>\n<contentList>\n</contentList>\n'))
                else:
                    raise RuntimeError(f"unsupported file type: {file_path}")
            elif len(file_path) == 0:
                return
            else:
                raise ValueError("pak_name should be provided")

    @property
    def is_empty(self) -> bool:
        return self.__xml is None

    @property
    def tool(self) -> bg3_modding_tool:
        return self.__tool

    @property
    def source_pak(self) -> str:
        return self.__source_pak

    @property
    def relative_file_path(self) -> str:
        return self.__relative_file_path

    @property
    def unpacked_file_path(self) -> str:
        return self.__unpacked_file_path

    @property
    def file_format(self) -> str:
        return self.__file_format

    @property
    def xml(self) -> ElementTree:
        if self.__xml is None:
            raise RuntimeError(f'Element tree is absent; file: {self.__relative_file_path}')
        return self.__xml

    @property
    def root_node(self) -> et.Element:
        root = self.xml.getroot()
        if root is None:
            raise RuntimeError(f'root is None, file {self.__relative_file_path}')
        return root

    @property
    def is_mod_specific(self) -> bool:
        return self.__mod_specific

    @property
    def rename_to(self) -> str:
        return self.__rename_to

    def get_output_relative_path(self, mod_name: str) -> str:
        parts = self.__relative_file_path.replace("\\", "/").split("/")
        n = len(parts)
        if self.__rename_to:
            s = parts[n - 1]
            pos = s.rfind(".")
            if pos == -1:
                raise RuntimeError(f'Failed to rename {self.__relative_file_path} to {self.__rename_to}')
            ext = s[pos:]
            parts[n - 1] = self.__rename_to + ext
        if self.__mod_specific:
            parts[1] = mod_name
        return "/".join(parts)

    def replace_xml(self, new_content: ElementTree) -> None:
        self.__xml = new_content


class game_files:
    __tool: bg3_modding_tool
    __mod_pretty_name: str
    __mod_name: str
    __mod_uuid: str
    __mod_version: int | None
    __files: dict[str, game_file]
    __empty_game_file: game_file


    def __init__(self, tool: bg3_modding_tool, mod_name: str = 'UnnamedMod', mod_uuid: str = '17d21eca-4b0d-45e8-826f-38f82489f36c') -> None:
        self.__tool = tool
        self.__mod_pretty_name = mod_name
        self.__mod_name = mod_name + "_" + mod_uuid
        self.__mod_uuid = mod_uuid
        self.__mod_version = None
        self.__files = dict[str, game_file]()
        self.__empty_game_file = game_file(tool, '')

    @property
    def mod_name(self) -> str:
        return self.__mod_pretty_name

    @mod_name.setter
    def mod_name(self, mod_name: str) -> None:
        self.__mod_pretty_name = mod_name
        self.__mod_name = mod_name + "_" + self.__mod_uuid

    @property
    def mod_uuid(self) -> str:
        return self.__mod_uuid

    @mod_uuid.setter
    def mod_uuid(self, mod_uuid: str) -> None:
        self.__mod_uuid = mod_uuid
        self.__mod_name = self.__mod_pretty_name + "_" + self.__mod_uuid

    @property
    def mod_name_uuid(self) -> str:
        return self.__mod_name

    @property
    def output_dir_path(self) -> str:
        return os.path.join(self.__tool.env.output_path, self.__mod_pretty_name)

    @property
    def preview_dir_path(self) -> str:
        return os.path.join(self.__tool.env.output_path, self.__mod_pretty_name + '_preview')

    @property
    def pak_path(self) -> str:
        return self.__tool.env.output_path

    @property
    def tool(self) -> bg3_modding_tool:
        return self.__tool

    @property
    def empty_game_file(self) -> game_file:
        return self.__empty_game_file

    def mod_destination_dir_path(self, original_relative_path: str) -> str:
        parts = original_relative_path.replace('\\', '/').split('/')
        parts[1] = self.__mod_name
        return os.path.join(self.output_dir_path, *parts)
    
    def mod_destination_dir_path_preview(self, original_relative_path: str) -> str:
        parts = original_relative_path.replace('\\', '/').split('/')
        parts[1] = self.__mod_name
        return os.path.join(self.output_dir_path, *parts)

    def get_loca_relative_path(self) -> str:
        result = f"Localization/English/{self.__mod_name}.loca"
        os.makedirs(os.path.join(self.output_dir_path, os.path.dirname(result)), exist_ok=True)
        return result

    def get_text_bank_file(self) -> game_file:
        try:
            return game_file(self.__tool, 'Localization/English/english.loca', pak_name = 'Localization/English.pak')
        except:
            pass
        return game_file(self.__tool, 'Localization/English/english.xml', pak_name = 'Localization/English.pak')

    def get_soundbank_file(self, speaker_uuid: str) -> game_file:
        soundbank_id = speaker_uuid.replace('-', '')
        try:
            return game_file(self.__tool, f'Mods/Gustav/Localization/English/Soundbanks/{soundbank_id}.lsf', pak_name = 'Localization/VoiceMeta.pak')
        except:
            pass
        try:
            return game_file(self.__tool, f'Localization/English/Soundbanks/{soundbank_id}.lsf', pak_name = 'Localization/Voice.pak')
        except:
            pass
        return game_file(self.__tool, f'Mods/Gustav/Localization/English/Soundbanks/{soundbank_id}.lsf', pak_name = 'Localization/Voice.pak')

    def get_file(
            self,
            pak_name: str | None,
            file_path: str,
            /,
            mod_specific: bool = False,
            rename_to: str = "",
            exclude_from_build: bool = False
    ) -> game_file:
        if file_path in self.__files:
            return self.__files[file_path]
        gf = game_file(self.__tool, file_path, pak_name = pak_name, mod_specific = mod_specific, rename_to = rename_to)
        if not exclude_from_build:
            self.__files[file_path] = gf
        return gf

    def add_new_file(self, relative_path: str, is_mod_specific = False) -> game_file:
        if relative_path in self.__files:
            return self.__files[relative_path]
        gf = game_file(self.__tool, relative_path, new_file = True, mod_specific = is_mod_specific)
        self.__files[relative_path] = gf
        return gf

    def add_new_root_template(self, root_template_uuid: str, root_template: et.Element[str]) -> game_file:
        gf = self.add_new_file(f'Public/ModNameHere/RootTemplates/{root_template_uuid}.lsf', is_mod_specific = True)
        if gf.xml is None:
            raise RuntimeError('Failed to create a new root template')
        gf.xml.getroot().append(et.fromstring('<version major="4" minor="8" revision="0" build="10" lslib_meta="v1,bswap_guids,lsf_keys_adjacency" />'))
        gf.xml.getroot().append(et.fromstring(f"""
<region id="Templates">
    <node id="Templates">
        <children>
        </children>
    </node>
</region>
"""))
        c = gf.xml.getroot().find('./region/node/children')
        if c is None:
            raise RuntimeError('Failed to create a new root template')
        c.append(root_template)
        return gf

    def add_external_file(self, source_file_path: str, relative_path: str, is_mod_specific = False) -> game_file:
        gf = game_file(self.__tool, relative_path, source_file_path = source_file_path, mod_specific = is_mod_specific)
        self.__files[relative_path] = gf
        return gf

    def copy_external_files(self, source_dir_path: str, relative_path: str) -> None:
        os.makedirs(self.output_dir_path, exist_ok = True)
        dest_path = os.path.join(self.output_dir_path, translate_path(relative_path))
        os.makedirs(dest_path, exist_ok=True)
        for dir_entry in os.scandir(source_dir_path):
            if dir_entry.is_dir():
                shutil.copytree(dir_entry.path, os.path.join(dest_path, dir_entry.name), dirs_exist_ok=True)

    def copy_osiris_goals(self, source_path: str) -> None:
        os.makedirs(self.output_dir_path, exist_ok = True)
        if not os.path.isdir(source_path):
            raise ValueError("not a directory path: " + source_path)
        if os.path.isdir(os.path.join(source_path, "Story")):
            osi_dir_path = os.path.join(self.output_dir_path, "Mods", self.__mod_name, "Story")
            os.makedirs(osi_dir_path, exist_ok=True)
            shutil.copytree(os.path.join(source_path, "Story"), osi_dir_path, dirs_exist_ok=True)

    def copy_script_extender_lua_files(self, source_path: str) -> None:
        os.makedirs(self.output_dir_path, exist_ok = True)
        if not os.path.isdir(source_path):
            raise ValueError("not a directory path: " + source_path)
        if os.path.isdir(os.path.join(source_path, "ScriptExtender")):
            scripts_dir_path = os.path.join(self.output_dir_path, "Mods", self.__mod_name, "ScriptExtender")
            os.makedirs(scripts_dir_path, exist_ok=True)
            shutil.copytree(os.path.join(source_path, "ScriptExtender"), scripts_dir_path, dirs_exist_ok=True)

    def copy_mod_logo(self, source_path: str, mod_file_name: str) -> None:
        os.makedirs(self.output_dir_path, exist_ok = True)
        mod_dir_path = os.path.join(self.output_dir_path, "Mods", self.__mod_name)
        if os.path.isdir(source_path):
            file_path = os.path.join(source_path, mod_file_name)
            if os.path.isfile(file_path):
                shutil.copy(file_path, os.path.join(mod_dir_path, "mod_publish_logo.png"))
            else:
                raise FileNotFoundError(f"{file_path} is not found in provided path {source_path}")
        elif os.path.isfile(source_path):
            shutil.copy(source_path, os.path.join(mod_dir_path, "mod_publish_logo.png"))
        else:
            raise FileNotFoundError(f"mod_publish_logo.png is not found in provided path {source_path}")

    def copy_memento_file(self, source_path: str, file_name: str) -> None:
        os.makedirs(self.output_dir_path, exist_ok = True)
        mod_dir_path = os.path.join(self.output_dir_path, "Mods", self.__mod_name)
        if os.path.isdir(source_path):
            file_path = os.path.join(source_path, file_name)
            if os.path.isfile(file_path):
                shutil.copy(file_path, os.path.join(mod_dir_path, file_name))
            else:
                raise FileNotFoundError(f"{file_path} is not found in provided path {source_path}")
        elif os.path.isfile(source_path):
            shutil.copy(source_path, os.path.join(mod_dir_path, file_name))
        else:
            raise FileNotFoundError(f"mod_publish_logo.png is not found in provided path {source_path}")

    def create_meta_lsx(
            self,
            mod_name: str,
            mod_display_name: str,
            description: str,
            mod_uuid: str,
            author: str,
            publish_handle: int,
            mod_version: tuple[int, int, int, int],
            pak_size: int,
            mod_hash: str
    ) -> None:
        os.makedirs(self.output_dir_path, exist_ok = True)
        self.__mod_version = mod_version[3] + (mod_version[2] << 31) + (mod_version[1] << 47) + (mod_version[0] << 55)
        meta_lsx = create_meta_lsx(mod_name, mod_display_name, description, mod_uuid, author, publish_handle, mod_version, pak_size, mod_hash)
        meta_lsx_path = os.path.join(self.output_dir_path, "Mods", self.__mod_name, "meta.lsx")
        os.makedirs(os.path.dirname(meta_lsx_path), exist_ok = True)
        if os.path.isfile(meta_lsx_path):
            os.unlink(meta_lsx_path)
        with open(meta_lsx_path, "wt") as f:
            f.write(meta_lsx)

    def create_info_json(self, md5_hash: str) -> None:
        info_json = {
            "Mods": [
                {
                    "Author": "iamy0urdad",
                    "Name": self.__mod_pretty_name,
                    "Folder": self.__mod_name,
                    "Version": str(self.__mod_version),
                    "Description": self.__mod_pretty_name,
                    "UUID": self.__mod_uuid,
                    "Created": datetime.datetime.now(tz=datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%S+00:00"),
                    "Dependencies": [],
                    "Group": "9ea70f48-daab-4f0a-8ed8-c6b910ee9c4c"
                }
            ],
            "MD5": md5_hash
        }
        info_json_path = os.path.join(self.pak_path, "info.json")
        with open(info_json_path, "wt") as f:
            json.dump(info_json, f)

    def build(self, /, preview: bool = True, verbose: bool = False) -> None:
        output_dir_path = self.output_dir_path
        preview_dir_path = self.preview_dir_path
        os.makedirs(output_dir_path, exist_ok = True)
        os.makedirs(preview_dir_path, exist_ok = True)
        for gf in self.__files.values():
            relative_file_path = translate_path(gf.relative_file_path)
            output_relative_path = translate_path(gf.get_output_relative_path(self.__mod_name))
            if verbose:
                sys.stdout.write(f"Writing {output_relative_path} ")
            match gf.file_format:
                case "lsj":
                    raise RuntimeError(".lsj files are not supported")
                case "lsf":
                    if verbose:
                        sys.stdout.write(" as lsf file .")
                    et.indent(gf.xml.getroot())
                    if preview:
                        preview_file_path = os.path.join(preview_dir_path, output_relative_path) + '.lsx'
                        os.makedirs(os.path.dirname(preview_file_path), exist_ok=True)
                        if verbose:
                            sys.stdout.write('.')
                        gf.xml.write(preview_file_path, encoding="utf-8", xml_declaration=True)
                        if verbose:
                            sys.stdout.write('.')
                    lsx_file_path = os.path.join(output_dir_path, output_relative_path) + '.lsx'
                    os.makedirs(os.path.dirname(lsx_file_path), exist_ok=True)
                    gf.xml.write(lsx_file_path, encoding="utf-8", xml_declaration=True)
                    if verbose:
                        sys.stdout.write('.')
                    self.__tool.convert_lsx_to_lsf(lsx_file_path)
                    if verbose:
                        sys.stdout.write('. done\n')
                case "lsx":
                    if verbose:
                        sys.stdout.write(" as lsx file .")
                    et.indent(gf.xml.getroot())
                    if preview:
                        preview_file_path = os.path.join(preview_dir_path, output_relative_path)
                        os.makedirs(os.path.dirname(preview_file_path), exist_ok=True)
                        if verbose:
                            sys.stdout.write('.')
                        gf.xml.write(preview_file_path, encoding="utf-8", xml_declaration=True)
                        if verbose:
                            sys.stdout.write('.')
                    lsx_file_path = os.path.join(output_dir_path, output_relative_path)
                    os.makedirs(os.path.dirname(lsx_file_path), exist_ok=True)
                    if verbose:
                        sys.stdout.write('.')
                    gf.xml.write(lsx_file_path, encoding="utf-8", xml_declaration=True)
                    if verbose:
                        sys.stdout.write('. done\n')
                case "xml":
                    if verbose:
                        sys.stdout.write(" as xml file .")
                    et.indent(gf.xml.getroot())
                    if preview:
                        preview_file_path = os.path.join(preview_dir_path, output_relative_path)
                        os.makedirs(os.path.dirname(preview_file_path), exist_ok=True)
                        if verbose:
                            sys.stdout.write('.')
                        gf.xml.write(preview_file_path, encoding="utf-8", xml_declaration=True)
                        if verbose:
                            sys.stdout.write('.')
                    xml_file_path = os.path.join(output_dir_path, output_relative_path)
                    os.makedirs(os.path.dirname(xml_file_path), exist_ok=True)
                    if verbose:
                        sys.stdout.write('.')
                    gf.xml.write(xml_file_path, encoding="utf-8", xml_declaration=True)
                    if verbose:
                        sys.stdout.write('. done\n')
                case "loca":
                    if verbose:
                        sys.stdout.write(" as loca file .")
                    et.indent(gf.xml.getroot())
                    if preview:
                        preview_file_path = os.path.join(preview_dir_path, relative_file_path) + '.xml'
                        os.makedirs(os.path.dirname(preview_file_path), exist_ok=True)
                        gf.xml.write(preview_file_path, encoding="utf-8", xml_declaration=True)
                        if verbose:
                            sys.stdout.write('.')
                    xml_file_path = os.path.join(output_dir_path, relative_file_path) + '.xml'
                    os.makedirs(os.path.dirname(xml_file_path), exist_ok=True)
                    gf.xml.write(xml_file_path, encoding="utf-8", xml_declaration=True)
                    if verbose:
                        sys.stdout.write('.')
                    self.__tool.convert_xml_to_loca(xml_file_path)
                    if verbose:
                        sys.stdout.write('. done\n')
                case "other":
                    if verbose:
                        sys.stdout.write(" as other file .")
                    preview_file_path = os.path.join(preview_dir_path, relative_file_path)
                    if preview:
                        os.makedirs(os.path.dirname(preview_file_path), exist_ok=True)
                    file_path = os.path.join(output_dir_path, relative_file_path)
                    os.makedirs(os.path.dirname(file_path), exist_ok=True)
                    src_ext = os.path.splitext(gf.unpacked_file_path)[1]
                    dest_ext = os.path.splitext(file_path)[1]
                    if src_ext == '.lsx' and dest_ext == '.lsf':
                        if preview:
                            shutil.copy(gf.unpacked_file_path, preview_file_path)
                        shutil.copy(gf.unpacked_file_path, file_path + '.lsx')
                        if verbose:
                            sys.stdout.write('.')
                        self.__tool.convert_lsx_to_lsf(file_path + '.lsx')
                    elif src_ext == '.xml' and dest_ext == '.loca':
                        if preview:
                            shutil.copy(gf.unpacked_file_path, preview_file_path)
                        shutil.copy(gf.unpacked_file_path, file_path + '.xml')
                        if verbose:
                            sys.stdout.write('.')
                        self.__tool.convert_xml_to_loca(file_path + '.xml')
                    elif src_ext == dest_ext:
                        if preview:
                            shutil.copy(gf.unpacked_file_path, preview_file_path)
                        shutil.copy(gf.unpacked_file_path, file_path)
                    else:
                        raise RuntimeError(f"failed to process an external file {gf.unpacked_file_path} with target relative path {gf.relative_file_path}")
                    if verbose:
                        sys.stdout.write('. done\n')
                case unknown_format:
                    raise ValueError(F"Unknown file format: {unknown_format}")
        if verbose:
            sys.stdout.write('Generating the .pak file .')
        pak_file = self.__tool.pack(self.output_dir_path, os.path.join(self.pak_path, self.__mod_name + ".pak"))
        if verbose:
            sys.stdout.write('.')
        md5 = hashlib.new('md5')
        with open(pak_file, 'rb') as f:
            buf = f.read(1024 * 1024)
            while buf:
                md5.update(buf)
                buf = f.read(1024 * 1024)
        md5_hash = md5.hexdigest()
        with open(pak_file + '.md5', 'wt') as f:
            f.write(md5_hash)
        if verbose:
            sys.stdout.write('. done\n')
        self.create_info_json(md5_hash)


    def build_mod_io_pak(self) -> str:
        output_pak_path = os.path.join(self.pak_path, self.__mod_name + "_mod.io.pak")
        if os.path.isfile(output_pak_path):
            os.unlink(output_pak_path)
        return self.__tool.pack(self.output_dir_path, output_pak_path)

    def get_mod_hash_and_version(self, pak_path: str) -> tuple[str, tuple[int, int, int, int]]:
        meta_lsx_path = self.__tool.unpack(pak_path, f'Mods/{self.__mod_name}/meta.lsx')
        with open(meta_lsx_path, "rt") as f:
            xml = et.parse(f)
        module_info = xml.getroot().find('./region[@id="Config"]/node[@id="root"]/children/node[@id="ModuleInfo"]')
        if module_info is None:
            raise ValueError(f'ModuleInfo is not found in meta.lsx of {pak_path}')
        version = int(get_required_bg3_attribute(module_info, 'Version64'))
        v4 = version & 0x7ffffff
        v3 = (version >> 31) & 0xffff
        v2 = (version >> 47) & 0xff
        v1 = version >> 55
        return (get_required_bg3_attribute(module_info, 'MD5'), (v1, v2, v3, v4))


    @staticmethod
    def generate_lua_io_overrides(lua_overrides_file_path: str, lua_overrides_lines: list[str]) -> None:
        if not os.path.isfile(lua_overrides_file_path):
            raise FileNotFoundError(f"Lua overrides file not found at {lua_overrides_file_path}")
        with open(lua_overrides_file_path, "rt") as f:
            lines = f.readlines()
        with open(lua_overrides_file_path, "wt") as f:
            for line in lines:
                if '-- Autogenerated IO path overrides' in line:
                    f.write(line)
                    for override_line in lua_overrides_lines:
                        f.write('    ')
                        f.write(override_line.replace('\\', '/'))
                        f.write("\n")
                else:
                    f.write(line)

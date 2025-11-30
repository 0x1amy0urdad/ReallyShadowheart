from __future__ import annotations

from dataclasses import dataclass, field

from ._assets import bg3_assets
from ._dialog import dialog_object
from ._common import get_bg3_attribute, get_required_bg3_attribute, new_random_uuid
from ._files import game_files
from ._env import bg3_modding_env
from ._pak_content import pak_content
from ._timeline import timeline_object
from ._tool import bg3_modding_tool
from ._types import XmlElement

import os
import traceback
import xml.etree.ElementTree as et

from typing import Callable

@dataclass
class mod_info:
    mod_name: str
    mod_uuid: str
    mod_version: tuple[int, int, int, int]
    pak_path: str = ""
    mod_files: list[str] = field(default_factory = list)
    content: pak_content | None = None
    meta_lsx: XmlElement | None = None
    mod_folder: str = ""
    enabled_in_load_order: bool = True

    def get_mod_attribute(self, attribute_name: str) -> str | None:
        if self.meta_lsx is None:
            return None
        module_info = self.meta_lsx.find('./region[@id="Config"]/node[@id="root"]/children/node[@id="ModuleInfo"]')
        if module_info is None:
            return None
        return get_bg3_attribute(module_info, attribute_name)


@dataclass
class mod_conflict:
    mods: tuple[mod_info, ...]
    dialogs: tuple[str, ...]

    def get_conflict_name(self) -> str:
        return '/'.join([mod.mod_name for mod in self.mods])


@dataclass
class conflict_resolution_settings:
    result_mod_name: str
    result_mod_uuid: str
    method: str
    mod_priorities: dict[int, tuple[str, ...]]


class mod_manager:
    __env: bg3_modding_env
    __tool: bg3_modding_tool
    __assets: bg3_assets
    __mods_dir_path: str
    __modsettings_path: str
    __mods: list[mod_info]
    __mods_imm: tuple[mod_info, ...]
    __mods_index: dict[str, mod_info]
    __conflicts: list[mod_conflict]
    __conflicts_imm: tuple[mod_conflict, ...]

    def __init__(self, f: game_files, bg3_appdata_path: str) -> None:
        self.__env = f.tool.env
        self.__tool = f.tool
        self.__assets = bg3_assets(f)
        self.__mods_dir_path = os.path.join(bg3_appdata_path, 'Mods')
        self.__modsettings_path = os.path.join(bg3_appdata_path, 'PlayerProfiles', 'Public', 'modsettings.lsx')
        self.__mods = list[mod_info]()
        self.__mods_imm = ()
        self.__mods_index = dict[str, mod_info]()
        self.__conflicts = list[mod_conflict]()
        self.__conflicts_imm = ()
        
    def get_mod_info(self, mod_uuid: str) -> mod_info:
        if mod_uuid in self.__mods_index:
            return self.__mods_index[mod_uuid]
        raise KeyError(f'Unknown mod {mod_uuid}')

    def reload_mods(self, progress_callback: Callable[[int, int, str], None] | None = None) -> None:
        self.__mods = list[mod_info]()
        self.__mods_imm = ()
        self.__mods_index = dict[str, mod_info]()
        self.__conflicts = list[mod_conflict]()
        self.__conflicts_imm = ()
        self.__load_modsettings()
        for f in os.listdir(self.__mods_dir_path):
            pak_path = os.path.join(self.__mods_dir_path, f)
            if os.path.isfile(pak_path) and pak_path.endswith('.pak'):
                self.__add_mod(pak_path)
        self.__mods_imm = tuple(self.__mods)

    def detect_conflicts(self, progress_callback: Callable[[int, int, str], None] | None = None) -> bool:
        conflicts = dict[str, list[str]]()
        for mod in self.__mods:
            if mod.content is None:
                continue
            modded_dialogs = mod.content.content_index
            for dialog_uuid in modded_dialogs:
                if dialog_uuid in conflicts:
                    conflicts[dialog_uuid].append(mod.mod_uuid)
                else:
                    conflicts[dialog_uuid] = [mod.mod_uuid]
        no_conflicts = list[str]()
        for dialog_uuid, mods in conflicts.items():
            if len(mods) == 1:
                no_conflicts.append(dialog_uuid)
        for no_conflict in no_conflicts:
            del conflicts[no_conflict]

        conflicts_grouped = dict[tuple[str, ...], list[str]]()
        for dialog_uuid, mod_uuids in conflicts.items():
            mod_uuids.sort()
            conflict_key = tuple(mod_uuids)
            if conflict_key in conflicts_grouped:
                conflicts_grouped[conflict_key].append(dialog_uuid)
            else:
                conflicts_grouped[conflict_key] = [dialog_uuid]
        self.__conflicts = list[mod_conflict]()
        for conflicted_mods, conflicted_dialogs in conflicts_grouped.items():
            mods = [self.get_mod_info(mod_uuid) for mod_uuid in conflicted_mods]
            self.__conflicts.append(mod_conflict(tuple(mods), tuple(conflicted_dialogs)))
        self.__conflicts_imm = tuple(self.__conflicts)
        return len(self.__conflicts_imm) > 0

    @property
    def mod_list(self) -> tuple[mod_info, ...]:
        return self.__mods_imm

    @property
    def conflicts(self) -> tuple[mod_conflict, ...]:
        return self.__conflicts_imm

    @staticmethod
    def __get_mod_version(node: XmlElement) -> tuple[int, int, int, int]:
        version = int(get_required_bg3_attribute(node, 'Version64'))
        v4 = version & 0x7ffffff
        v3 = (version >> 31) & 0xffff
        v2 = (version >> 47) & 0xff
        v1 = version >> 55
        return (v1, v2, v3, v4)

    def __load_modsettings(self) -> None:
        modsettings = et.parse(self.__modsettings_path).getroot()
        mods = modsettings.findall('./region[@id="ModuleSettings"]/node[@id="root"]/children/node[@id="Mods"]/children/node[@id="ModuleShortDesc"]')
        for mod in mods:
            mod_name = get_required_bg3_attribute(mod, 'Name')
            mod_uuid = get_required_bg3_attribute(mod, 'UUID')
            mod_version = mod_manager.__get_mod_version(mod)
            mi = mod_info(mod_name, mod_uuid, mod_version)
            self.__mods.append(mi)
            self.__mods_index[mod_uuid] = mi

    def __add_mod(self, pak_path: str) -> None:
        mod_files = self.__tool.list(pak_path)
        content = pak_content(self.__assets, pak_path)
        for f in mod_files:
            if f.endswith('meta.lsx'):
                meta_lsx = self.__tool.unpack(pak_path, f)
                meta_lsx_xml = et.parse(meta_lsx).getroot()
                module_info = meta_lsx_xml.find('./region[@id="Config"]/node[@id="root"]/children/node[@id="ModuleInfo"]')
                if module_info is None:
                    continue
                try:
                    mod_uuid = get_required_bg3_attribute(module_info, 'UUID')
                    mod_folder = get_required_bg3_attribute(module_info, 'Folder')
                    if mod_uuid in self.__mods_index:
                        modinfo = self.__mods_index[mod_uuid]
                        modinfo.pak_path = pak_path
                        modinfo.mod_files = mod_files
                        modinfo.content = content
                        modinfo.meta_lsx = meta_lsx_xml
                        modinfo.mod_folder = mod_folder
                    else:
                        mod_name = get_required_bg3_attribute(module_info, 'Name')
                        mod_version = mod_manager.__get_mod_version(module_info)
                        modinfo = mod_info(mod_name, mod_uuid, mod_version, pak_path, mod_files, content, meta_lsx_xml, mod_folder, False)
                        self.__mods_index[mod_uuid] = modinfo
                        self.__mods.append(modinfo)
                except BaseException as exc:
                    for l in traceback.format_exception(exc):
                        print(l)

    def resolve_conflicts(
            self,
            settings: conflict_resolution_settings,
            progress_callback: Callable[[int, int, str], None] | None = None
    ) -> tuple[bool, str]:
        if settings.method == 'merge':
            return (False, 'Merging mods is not supported.')
        elif settings.method != 'patch':
            return (False, f'Unsupported resolution strategy: {settings.method}.')

        # prepare the tools
        self.__env.cleanup_output()
        mod_name = settings.result_mod_name
        if settings.result_mod_uuid:
            mod_uuid = settings.result_mod_uuid
        else:
            mod_uuid = new_random_uuid()
        bt = bg3_modding_tool(self.__env)
        bf = game_files(bt, mod_name, mod_uuid)
        ba = bg3_assets(bf)
    
        for conflict_index, mod_priorities in settings.mod_priorities.items():
            conflict = self.conflicts[conflict_index]
            mods = tuple([(self.get_mod_info(m), pak_content(self.__assets, self.get_mod_info(m).pak_path)) for m in mod_priorities])
            for dialog_uuid in conflict.dialogs:
                if not mod_manager.resolve_dialog_conflict(ba, dialog_uuid, mods):
                    return (False, f'Failed to resolve conflicts for dialog {self.__assets.index.get_dialog_name(dialog_uuid)}')

        return (True, 'Success')

    @staticmethod
    def resolve_dialog_conflict(ba: bg3_assets, dialog_uuid: str, mods: tuple[tuple[mod_info, pak_content], ...]) -> bool:
        print(f'resolve_dialog_conflict for {dialog_uuid}')
        # Copy the dialog from the vanilla game
        # dialog_name = ba.index.get_dialog_name(dialog_uuid)
        # ab = ba.copy_dialog_to_mod(dialog_name)

        # 
        d: dialog_object | None = None
        t: timeline_object | None = None
        for mi, pc in mods:
            cb = pc.get_content_bundle(dialog_uuid)
            print(f'content bundle from {mi.mod_name}: {cb}')
            # if cb.dialog_file:
            #     d = pc.get_dialog_object(dialog_uuid)
            # if cb.timeline_file:
            #     t = pc.get_timeline_object(dialog_uuid)
            

        return True


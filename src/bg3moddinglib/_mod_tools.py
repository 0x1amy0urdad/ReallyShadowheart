from __future__ import annotations

from dataclasses import dataclass, field

from ._assets import bg3_assets
from ._common import (
    get_bg3_attribute,
    get_required_bg3_attribute,
    find_bg3_appdata_path,
    new_random_uuid,
    set_bg3_attribute
)
from ._dialog import dialog_object
from ._dialog_differ import dialog_differ
from ._env import bg3_modding_env
from ._files import game_file, game_files
from ._loca import loca_object
from ._logger import get_logger
from ._pak_content import pak_content
from ._soundbank import soundbank_object
from ._timeline import timeline_object
from ._timeline_differ import timeline_differ
from ._tool import bg3_modding_tool
from ._types import XmlElement

import copy
import shutil
import os
import time
import traceback
import xml.etree.ElementTree as et

from datetime import datetime, timezone
from enum import StrEnum
from typing import Callable


PROGRESS_MSG_LEN = 72


class conflict_resolution_method(StrEnum):
    MERGE = "merge"
    PATCH = "patch"


@dataclass
class mod_info:
    mod_name: str
    mod_uuid: str
    mod_version: tuple[int, int, int, int]
    pak_path: str = ""
    mod_files: tuple[str, ...] = field(default_factory = tuple)
    content: pak_content | None = None
    meta_lsx: XmlElement | None = None
    mod_description: str = ""
    mod_author: str = ""
    mod_folder: str = ""
    mod_short_name: str = ""
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
    selected: bool = False

    @property
    def is_conflict(self) -> bool:
        return len(self.mods) > 1

    def get_conflict_name(self) -> str:
        if len(self.mods) > 1:
            return 'CONFLICT: ' + '/'.join([mod.mod_short_name for mod in self.mods])
        if len(self.mods) == 1:
            return 'MOD: ' + self.mods[0].mod_name
        return ''


@dataclass
class mod_metadata:
    mod_name: str
    mod_display_name: str
    mod_description: str
    mod_uuid: str
    mod_author: str
    mod_version: tuple[int, int, int, int]


@dataclass
class conflict_resolution_settings:
    chosen_conflicts: tuple[int, ...]
    priority_order: tuple[str, ...]
    metadata: mod_metadata | None = None
    install_when_done: bool = False


class mod_manager:
    __env: bg3_modding_env
    __assets: bg3_assets
    __mods_dir_path: str
    __modsettings_path: str
    __mods: list[mod_info]
    __mods_imm: tuple[mod_info, ...]
    __mods_index: dict[str, mod_info]
    __conflicts: list[mod_conflict]
    __conflicts_imm: tuple[mod_conflict, ...]
    __conflicting_files: dict[str, list[str]]
    __loca: loca_object | None
    __report: list[str]

    def __init__(self, f: game_files, bg3_appdata_path: str | None = None) -> None:
        if bg3_appdata_path is None:
            bg3_appdata_path = find_bg3_appdata_path()
        if bg3_appdata_path is None:
            raise ValueError('failed to determine bg3_appdata_path')
        self.__env = f.tool.env
        self.__assets = bg3_assets(f)
        self.__mods_dir_path = os.path.join(bg3_appdata_path, 'Mods')
        self.__modsettings_path = os.path.join(bg3_appdata_path, 'PlayerProfiles', 'Public', 'modsettings.lsx')
        self.__mods = list[mod_info]()
        self.__mods_imm = ()
        self.__mods_index = dict[str, mod_info]()
        self.__conflicts = list[mod_conflict]()
        self.__conflicts_imm = ()
        self.__conflicting_files = dict[str, list[str]]()
        self.__loca = None
        self.__report = list[str]()

    def add_to_report(self, message: str) -> None:
        log_msg = f'{datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")}: {message}'
        self.__report.append(log_msg)
        get_logger().info(message)

    def get_mod_info(self, mod_uuid: str) -> mod_info:
        if mod_uuid in self.__mods_index:
            return self.__mods_index[mod_uuid]
        raise KeyError(f'Unknown mod {mod_uuid}')

    def uninstall_mod(self, mod_uuid: str) -> bool:
        try:
            modsettings = et.parse(self.__modsettings_path)
            container = modsettings.getroot().find('./region[@id="ModuleSettings"]/node[@id="root"]/children/node[@id="Mods"]/children')
            if container is not None:
                mods = container.findall('./node[@id="ModuleShortDesc"]')
                for_removal: XmlElement | None = None
                for mod in mods:
                    current_uuid = get_required_bg3_attribute(mod, 'UUID')
                    if current_uuid == mod_uuid:
                        for_removal = mod
                        break
                if for_removal is not None:
                    container.remove(for_removal)
                os.unlink(self.__modsettings_path)
                et.indent(modsettings)
                modsettings.write(self.__modsettings_path, encoding = "utf-8", xml_declaration = True)
            mi = self.get_mod_info(mod_uuid)
            os.unlink(mi.pak_path)
            del self.__mods_index[mod_uuid]
            return True
        except:
            return False

    def install_mod(self, pak_path: str) -> bool:
        try:
            print('install_mod')
            appdata_path = find_bg3_appdata_path()
            if appdata_path is None:
                get_logger().info(f'install_mod for {pak_path} failed: unable to determine local appdata path')
                return False
            mods_folder_path = os.path.join(appdata_path, 'Mods')
            shutil.copy2(pak_path, mods_folder_path)
            
            files = self.__assets.tool.list(pak_path)
            meta_lsx: XmlElement | None = None
            for f in files:
                if f.endswith('/meta.lsx'):
                    meta_lsx_path = self.__assets.tool.unpack(pak_path, f)
                    meta_lsx = et.parse(meta_lsx_path).getroot()
                    break
            if meta_lsx is None:
                get_logger().info(f'install_mod for {pak_path} failed: unable to locate meta.lsx in the mod')
                return False

            module_info = meta_lsx.find('./region[@id="Config"]/node[@id="root"]/children/node[@id="ModuleInfo"]')
            if module_info is None:
                get_logger().info(f'install_mod for {pak_path} failed: meta.lsx does not contain ModuleInfo')
                return False
            mod_folder = get_required_bg3_attribute(module_info, 'Folder')
            mod_md5 = get_bg3_attribute(module_info, 'MD5')
            if mod_md5 is None:
                mod_md5 = ''
            mod_name = get_required_bg3_attribute(module_info, 'Name')
            mod_publish_handle = get_bg3_attribute(module_info, 'PublishHandle')
            if mod_publish_handle is None:
                mod_publish_handle = '0'
            mod_uuid = get_required_bg3_attribute(module_info, 'UUID')
            mod_version= get_bg3_attribute(module_info, 'Version64')
            if mod_version is None:
                mod_version = '36028797018963968'

            modsettings = et.parse(self.__modsettings_path)
            container = modsettings.getroot().find('./region[@id="ModuleSettings"]/node[@id="root"]/children/node[@id="Mods"]/children')
            if container is None:
                get_logger().info(f'install_mod for {pak_path} failed: unexpected content in modsettings.lsx')
                return False
            module_short_desc = et.fromstring(
                '<node id="ModuleShortDesc">'
                + f'<attribute id="Folder" type="LSString" value="{mod_folder}"/>'
                + f'<attribute id="MD5" type="LSString" value="{mod_md5}"/>'
                + f'<attribute id="Name" type="LSString" value="{mod_name}"/>'
                + f'<attribute id="PublishHandle" type="uint64" value="{mod_publish_handle}"/>'
                + f'<attribute id="UUID" type="guid" value="{mod_uuid}"/>'
                + f'<attribute id="Version64" type="int64" value="{mod_version}"/>'
                + '</node>')
            container.append(module_short_desc)
            os.unlink(self.__modsettings_path)
            et.indent(modsettings)
            modsettings.write(self.__modsettings_path, encoding = "utf-8", xml_declaration = True)
            return True
        except:
            print('exception')
            return False

    def reload_mods(self, progress_callback: Callable[[int, int, str], None] | None = None) -> None:
        if progress_callback is not None:
            progress_callback(0, 0, 'Reading: modsettings.lsx')
        self.__mods = list[mod_info]()
        self.__mods_imm = ()
        self.__mods_index = dict[str, mod_info]()
        self.__conflicts = list[mod_conflict]()
        self.__conflicts_imm = ()
        self.__load_modsettings()

        all_files = os.listdir(self.__mods_dir_path)
        total_count = len([f for f in all_files if f.endswith('.pak')])
        count = 0
        for f in all_files:
            pak_path = os.path.join(self.__mods_dir_path, f)
            if os.path.isfile(pak_path) and pak_path.endswith('.pak'):
                count += 1
                if progress_callback is not None:
                    progress_callback(count, total_count, f'[{count:3}/{total_count:3}] Reading pak file: {os.path.basename(pak_path)}')
                self.__add_mod(pak_path)
        self.__filter_out_mods()
        self.__mods_imm = tuple(self.__mods)

    def detect_conflicts(self, progress_callback: Callable[[int, int, str], None] | None = None) -> bool:
        if progress_callback is not None:
            progress_callback(0, 0, 'Conflict detection is in progress...')
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
        mods_with_conflicts = set[str]()
        for conflicted_mods, conflicted_dialogs in conflicts_grouped.items():

            # # TODO: replace this stub with correct handling of unknown dialogs
            unknown_dialogs = False
            for dialog_uuid in conflicted_dialogs:
                try:
                    self.__assets.index.get_dialog_name(dialog_uuid)
                except:
                    self.add_to_report(f'unknown dialog: {dialog_uuid}')
                    unknown_dialogs = True
            # For now, if conflicts are in unknown dialogs, skip them
            if unknown_dialogs:
                self.add_to_report(f'the following mods have conflicts in unknown dialogs: {', '.join(conflicted_mods)}')
                continue

            for mod_uuid in conflicted_mods:
                mods_with_conflicts.add(mod_uuid)
            mods = [self.get_mod_info(mod_uuid) for mod_uuid in conflicted_mods]
            self.__conflicts.append(mod_conflict(tuple(mods), tuple(conflicted_dialogs)))

        for mod in self.__mods:
            if mod.content is None or mod.mod_uuid in mods_with_conflicts:
                continue
            self.__conflicts.append(mod_conflict((mod,), ()))

        self.__conflicts_imm = tuple(self.__conflicts)

        n = 0
        self.add_to_report('=== detect_conflicts results ===')
        for c in self.__conflicts_imm:
            if not c.is_conflict:
                continue
            n += 1
            conflict_name = c.get_conflict_name()
            self.add_to_report(f'conflict detected: {conflict_name}')
            for dialog_uuid in c.dialogs:
                dialog_name = self.__assets.index.get_dialog_name(dialog_uuid)
                self.add_to_report(f'{dialog_uuid} {dialog_name}')
        self.add_to_report('=== === ===')

        return n > 0

    @property
    def mod_list(self) -> tuple[mod_info, ...]:
        return self.__mods_imm

    @property
    def conflicts(self) -> tuple[mod_conflict, ...]:
        return self.__conflicts_imm

    @property
    def report(self) -> tuple[str, ...]:
        return tuple(self.__report)

    @staticmethod
    def __get_mod_version(node: XmlElement) -> tuple[int, int, int, int]:
        version64 = get_bg3_attribute(node, 'Version64')
        if version64 is None:
            return (0, 0, 0, 0)
        version = int(version64)
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
            mod_short_name = mod_manager.make_mod_short_name(mod_name)
            mi = mod_info(mod_name, mod_uuid, mod_version, mod_short_name = mod_short_name)
            self.__mods.append(mi)
            self.__mods_index[mod_uuid] = mi

    def __add_mod(self, pak_path: str) -> None:
        try:
            content = pak_content(self.__assets, pak_path)
            if content.meta_lsx is None:
                self.add_to_report(f'Failed to process mod {pak_path}: meta.lsx is not found')
                return
            module_info = content.meta_lsx.find('./region[@id="Config"]/node[@id="root"]/children/node[@id="ModuleInfo"]')
            if module_info is None:
                self.add_to_report(f'Failed to process mod {pak_path}: ModuleInfo is not present in meta.lsx')
                return
            mod_uuid = get_required_bg3_attribute(module_info, 'UUID')
            mod_folder = get_required_bg3_attribute(module_info, 'Folder')
            mod_name = get_required_bg3_attribute(module_info, 'Name')
            mod_short_name = mod_manager.make_mod_short_name(mod_name)
            mod_description = get_bg3_attribute(module_info, 'Description')
            if mod_description is None:
                mod_description = ''
            mod_author = get_bg3_attribute(module_info, 'Author')
            if mod_author is None:
                mod_author = 'Anonymous'

            if mod_uuid in self.__mods_index:
                modinfo = self.__mods_index[mod_uuid]
                modinfo.pak_path = pak_path
                modinfo.mod_files = content.files
                modinfo.content = content
                modinfo.meta_lsx = content.meta_lsx
                modinfo.mod_folder = mod_folder
                modinfo.mod_short_name = mod_short_name
                modinfo.mod_description = mod_description
                modinfo.mod_author = mod_author
            else:
                mod_name = get_required_bg3_attribute(module_info, 'Name')
                mod_version = mod_manager.__get_mod_version(module_info)
                modinfo = mod_info(mod_name, mod_uuid, mod_version, pak_path, content.files, content, content.meta_lsx, mod_description, mod_author, mod_folder, mod_short_name, False)
                self.__mods_index[mod_uuid] = modinfo
                self.__mods.append(modinfo)
        except:
            self.add_to_report(f'Failed to process mod {pak_path}: {traceback.format_exc()}')

    def __filter_out_mods(self) -> None:
        mods_for_removal = list[mod_info]()
        for mod in self.__mods:
            if mod.content is None:
                self.add_to_report(f'Skipped mod {mod.mod_name} {mod.mod_uuid} {mod.mod_version} because it has failed to load or it is a part of the vanilla game')
                mods_for_removal.append(mod)
                continue
            guidance_lsx_path = f'Mods/{mod.mod_folder}/guidance.lsx'
            if guidance_lsx_path in mod.mod_files:
                self.add_to_report(f'Skipped mod {mod.mod_name} {mod.mod_uuid} {mod.mod_version} because Guidance created it')
                mods_for_removal.append(mod)
        for mod in mods_for_removal:
            del self.__mods_index[mod.mod_uuid]
            self.__mods.remove(mod)

    def __create_guidance_node(self, settings: conflict_resolution_settings, method: conflict_resolution_method) -> None:
        gf = self.__assets.files.add_new_file('Mods/ModName/guidance.lsx', is_mod_specific = True)
        guidance_node = et.fromstring('<node id="Guidance"></node>')
        set_bg3_attribute(guidance_node, 'Guidance', 'True', attribute_type = 'bool')
        set_bg3_attribute(guidance_node, 'Type', method, attribute_type = 'LSString')
        children_node = et.fromstring('<children></children>')
        for mod_uuid in settings.priority_order:
            mod_node = et.fromstring('<node id="ModReference"></node>')
            set_bg3_attribute(mod_node, 'UUID', mod_uuid, attribute_type = 'guid')
            children_node.append(mod_node)
        guidance_node.append(children_node)
        gf.xml.getroot().append(guidance_node)


    def resolve_conflicts(
            self,
            settings: conflict_resolution_settings,
            method: conflict_resolution_method,
            progress_callback: Callable[[int, int, str], None] | None = None
    ) -> tuple[bool, str]:
        self.__report.clear()
        success = False
        try:
            self.add_to_report('*** merge_mods ***')

            if progress_callback:
                progress_callback(0, 0, 'Getting ready...')

            self.__env.cleanup_output()
            if settings.metadata is None:
                mod_uuid = settings.priority_order[0]
                mod_name = self.__mods_index[mod_uuid].mod_short_name
                mod_folder = self.__mods_index[mod_uuid].mod_folder
            else:
                mod_uuid = settings.metadata.mod_uuid
                mod_name = mod_manager.make_mod_short_name(settings.metadata.mod_name)
                mod_folder = mod_name + '_' + settings.metadata.mod_uuid
            t = bg3_modding_tool(self.__env)

            f = game_files(t, mod_name, mod_uuid)

            if settings.metadata is not None:
                self.append_to_exclusion_list(settings.priority_order[0], '\\meta.lsx')
                f.create_meta_lsx(
                    settings.metadata.mod_name,
                    settings.metadata.mod_display_name,
                    settings.metadata.mod_description,
                    settings.metadata.mod_uuid,
                    f'{settings.metadata.mod_author} with Guidance',
                    0,
                    settings.metadata.mod_version,
                    20000000,
                    '15f1afd547fbd0ac70a98c2432c10868')

            self.add_to_report(f'result mod name = {mod_name}, mod uuid = {mod_uuid}, mod folder = {f.mod_name}')

            self.__assets = bg3_assets(f)
            self.__conflicting_files.clear()

            mod_priority_order_list = list[mod_info]()
            self.add_to_report('mod priority order:')
            for mod_uuid in settings.priority_order:
                mi = self.get_mod_info(mod_uuid)
                mod_priority_order_list.append(mi)
                self.add_to_report(f'{mi.mod_name} [{mod_uuid}]')

            total_count = 0
            for mod_conflict_index in settings.chosen_conflicts:
                total_count += len(self.conflicts[mod_conflict_index].dialogs)

            count = 0
            mod_priority_order = tuple(mod_priority_order_list)
            for mod_conflict_index in settings.chosen_conflicts:
                conflict = self.conflicts[mod_conflict_index]
                for dialog_uuid in conflict.dialogs:
                    count += 1
                    if progress_callback is not None:
                        dialog_name = self.__assets.index.get_dialog_name(dialog_uuid)
                        s = f'Resolving conflicts in {dialog_name}'
                        if len(s) > PROGRESS_MSG_LEN:
                            s = s[:PROGRESS_MSG_LEN - 2] + '...'
                        progress_callback(count, total_count, s)
                    self.merge_conflicting_dialogs(dialog_uuid, mod_priority_order)

            if method == conflict_resolution_method.MERGE:
                # Skip all unnecessary osiris clutter
                for mod in mod_priority_order:
                    self.append_to_exclusion_list(mod.mod_uuid, '\\Story\\story_ac.dat')
                    self.append_to_exclusion_list(mod.mod_uuid, '\\Story\\story.div')
                    self.append_to_exclusion_list(mod.mod_uuid, '\\Story\\story.div.osi')
                    self.append_to_exclusion_list(mod.mod_uuid, '\\Story\\goals.raw')
                    self.append_to_exclusion_list(mod.mod_uuid, '\\Story\\log.txt')
                    self.append_to_exclusion_list(mod.mod_uuid, '\\Story\\story_orphanqueries_found.txt')
                    self.append_to_exclusion_list(mod.mod_uuid, '\\Story\\story_orphanqueries_ignore.txt')
                    self.append_to_exclusion_list(mod.mod_uuid, '\\Story\\RawFiles\\story_definitions.div')
                    self.append_to_exclusion_list(mod.mod_uuid, '\\Story\\RawFiles\\story_header.div')

                for i in range(1, len(mod_priority_order)):
                    self.append_to_exclusion_list(mod_priority_order[i].mod_uuid, '\\meta.lsx')
                    self.append_to_exclusion_list(mod_priority_order[i].mod_uuid, '\\mod_publish_logo.png')

                self.merge_resource_banks(mod_priority_order, progress_callback = progress_callback)
                self.merge_overlapping_files(mod_priority_order, progress_callback = progress_callback)

                for mi in mod_priority_order:
                    if progress_callback is not None:
                        s = f'Unpacking {mi.mod_name}'
                        if len(s) > PROGRESS_MSG_LEN:
                            s = s[:PROGRESS_MSG_LEN - 2] + '...'
                        progress_callback(0, 0, s)
                    src_path = self.unpack_mod(mi)
                    self.copy_mod_files(src_path, self.__assets.files.output_dir_path, mod_folder, mi.mod_uuid, progress_callback = progress_callback)

            self.__create_guidance_node(settings, method)
            pak_path = self.__assets.files.build(verbose = False, preview = True, progress_callback = progress_callback)

            if settings.install_when_done:
                if method == conflict_resolution_method.PATCH:
                    self.install_mod(pak_path)
                else:
                    for mod_uuid in settings.priority_order:
                        self.uninstall_mod(mod_uuid)
                    self.install_mod(pak_path)

            success = True
            return (True, 'Success')
        except BaseException as exc:
            self.add_to_report('An exception has been raised, see below.')
            for line in traceback.format_exception(exc):
                self.add_to_report(line)
            raise RuntimeError('Conflict resolution failure') from exc
        finally:
            now = datetime.now()
            suffix = 'success' if success else 'failure'
            file_path = os.path.join(self.__env.env_root_path, f'worklog-{suffix}-{now.year:04}{now.month:02}{now.day:02}-{now.hour:02}{now.minute:02}{now.second:02}.txt')
            with open(file_path, 'w') as f:
                for line in self.__report:
                    f.write(line)
                    f.write('\n')


    def merge_resource_banks(
            self,
            mod_priority_order: tuple[mod_info, ...],
            progress_callback: Callable[[int, int, str], None] | None = None
    ) -> None:
        total_count = 0
        for mi in mod_priority_order:
            total_count += len(mi.mod_files)
        count = 0
        
        t = time.time()
        for mi in mod_priority_order:
            for f in mi.mod_files:
                count += 1
                if progress_callback is not None and time.time() - t >= 1.0:
                    t = time.time()
                    s = f'Processing resource banks: {f}'
                    if len(s) > PROGRESS_MSG_LEN:
                        n = len(s) - PROGRESS_MSG_LEN
                        s = f'Processing resource banks: ...{f[n + 2:]}'
                    progress_callback(count, total_count, s)

                f_dirs = f.split('/')
                # Dialog and Timeline banks
                if len(f_dirs) > 2 and f_dirs[0] == 'Public' and f_dirs[2] == 'Content' and f.endswith('.lsf'):
                    gf = game_file(self.__assets.tool, f, pak_name = mi.pak_path)
                    root_node = gf.xml.getroot()
                    # Dialog bank
                    dialog_resources = root_node.findall('./region[@id="DialogBank"]/node[@id="DialogBank"]/children/node[@id="Resource"]')
                    if len(dialog_resources) > 0:
                        self.add_to_report(f'found dialog bank {f} with {len(dialog_resources)} resources')
                        self.append_to_exclusion_list(mi.mod_uuid, f)
                        # add all dialogs that are not in the exclusion list to the resulting dialog bank
                        for dialog_resource in dialog_resources:
                            source_file = get_required_bg3_attribute(dialog_resource, 'SourceFile')
                            if '/Story/Dialogs/' in source_file:
                                source_file = source_file.replace('/Story/Dialogs/', '/Story/DialogsBinary/').replace('.lsj', '.lsf')
                            if not self.is_in_exclusion_list(mi.mod_uuid, source_file.replace('/', '\\')):
                                self.add_to_report(f'added to the dialog bank: {source_file}')
                                self.__assets.add_to_dialog_bank(dialog_resource)
                            else:
                                self.add_to_report(f'not added to the dialog bank because this file is in exclusion list: {source_file}')
                    # Timeline bank
                    timeline_resources = root_node.findall('./region[@id="TimelineBank"]/node[@id="TimelineBank"]/children/node[@id="Resource"]')
                    if len(timeline_resources) > 0:
                        self.add_to_report(f'found timeline bank {f} with {len(timeline_resources)} resources')
                        self.append_to_exclusion_list(mi.mod_uuid, f)
                        # add all timelines that are not in the exclusion list to the resulting dialog bank
                        for timeline_resource in timeline_resources:
                            source_file = get_required_bg3_attribute(timeline_resource, 'SourceFile')
                            if not self.is_in_exclusion_list(mi.mod_uuid, source_file.replace('/', '\\')):
                                self.add_to_report(f'added to the timeline bank: {source_file}')
                                self.__assets.add_to_timeline_bank(timeline_resource)
                            else:
                                self.add_to_report(f'not added to the timeline bank because this file is in exclusion list: {source_file}')
                # Soundbank
                if len(f_dirs) > 4 and f_dirs[0] == 'Mods' and f_dirs[2] == 'Localization' and f_dirs[4] == 'Soundbanks' and f.endswith('.lsf'):
                    gf = game_file(self.__assets.tool, f, pak_name = mi.pak_path)
                    root_node = gf.xml.getroot()
                    speaker_metadata = root_node.find('./region[@id="VoiceMetaData"]/node[@id="VoiceMetaData"]/children/node[@id="VoiceSpeakerMetaData"]')
                    if speaker_metadata is None:
                        continue
                    speaker_uuid = get_required_bg3_attribute(speaker_metadata, 'MapKey')
                    voice_text_meta_datas = speaker_metadata.findall('./children/node[@id="MapValue"]/children/node[@id="VoiceTextMetaData"]')
                    if len(voice_text_meta_datas) > 0:
                        self.add_to_report(f'found sound (voice text) bank {f} with {len(voice_text_meta_datas)} resources')
                        self.append_to_exclusion_list(mi.mod_uuid, f)
                        sounbank = soundbank_object.create_new(self.__assets.files, speaker_uuid)
                        for voice_text_meta_data in voice_text_meta_datas:
                            handle = get_required_bg3_attribute(voice_text_meta_data, 'MapKey')
                            map_val = voice_text_meta_data.find('./children/node[@id="MapValue"]')
                            if map_val is not None:
                                length = get_required_bg3_attribute(map_val, 'Length')
                                priority = get_required_bg3_attribute(map_val, 'Priority')
                                source = get_required_bg3_attribute(map_val, 'Source')
                                sounbank.add_voice_metadata(handle, length, priority = priority, audio_file_name = source)
                                self.add_to_report(f'added to the sound bank {speaker_uuid}: {source} {priority} {length}')

                # Translated Strings bank
                if f.startswith('Localization\\') and (f.endswith('.loca') or f.endswith('.xml')):
                    self.append_to_exclusion_list(mi.mod_uuid, f)
                    self.append_text_content(game_file(self.__assets.tool, f, pak_name = mi.pak_path))
                    self.add_to_report(f'merged the text bank: {f}')
                # Legacy/EA Translated Strings bank
                if f_dirs[0] == 'Mods' and f_dirs[2] == 'Localization' and (f.endswith('.loca') or f.endswith('.xml')):
                    self.append_to_exclusion_list(mi.mod_uuid, f)
                    self.append_text_content(game_file(self.__assets.tool, f, pak_name = mi.pak_path))
                    self.add_to_report(f'merged the text bank: {f}')


    def __merge_xml(self, dest_node: XmlElement, src_node: XmlElement, selector: str, dedup_attribute: str) -> None:
        existing_nodes_ids = set()
        existing_nodes = dest_node.findall(selector)
        for n in existing_nodes:
            existing_nodes_ids.add(get_required_bg3_attribute(n, dedup_attribute))
        nodes = src_node.findall(selector)
        for node in nodes:
            if get_required_bg3_attribute(node, dedup_attribute) in existing_nodes_ids:
                continue
            dest_node.append(node)


    def __merge_overlapping_files(self, base_file: game_file, overlapping_file: game_file) -> None:
        # Gossips
        self.add_to_report(f'merging files: {base_file.relative_file_path} <- {overlapping_file.relative_file_path}')
        base_node_root = base_file.xml.find('./region[@id="Gossips"]/node[@id="root"]/children')
        if base_node_root is not None:
            overlap_node_root = overlapping_file.xml.find('./region[@id="Gossips"]/node[@id="root"]/children')
            if overlap_node_root is not None:
                self.add_to_report(f'merging gossips: {base_file.relative_file_path} <- {overlapping_file.relative_file_path}')
                self.__merge_xml(base_node_root, overlap_node_root, './node[@id="Gossip"]', 'DialogUUID')
                return

        # Game Objects and Root Templates
        base_node_root = base_file.xml.find('./region[@id="Templates"]/node[@id="Templates"]/children')
        if base_node_root is not None:
            overlap_node_root = overlapping_file.xml.find('./region[@id="Templates"]/node[@id="Templates"]/children')
            if overlap_node_root is not None:
                self.add_to_report(f'merging game objects: {base_file.relative_file_path} <- {overlapping_file.relative_file_path}')
                self.__merge_xml(base_node_root, overlap_node_root, './node[@id="GameObjects"]', 'MapKey')
                return

        # Translated String Keys
        base_node_root = base_file.xml.find('./region[@id="TranslatedStringKeys"]/node[@id="TranslatedStringKeys"]/children')
        if base_node_root is not None:
            overlap_node_root = overlapping_file.xml.find('./region[@id="TranslatedStringKeys"]/node[@id="TranslatedStringKeys"]/children')
            if overlap_node_root is not None:
                self.add_to_report(f'merging translated string keys: {base_file.relative_file_path} <- {overlapping_file.relative_file_path}')
                self.__merge_xml(base_node_root, overlap_node_root, './node[@id="TranslatedStringKey"]', 'UUID')
                return

        # Character Visuals
        base_node_root = base_file.xml.find('./region[@id="CharacterVisualBank"]/node[@id="CharacterVisualBank"]/children')
        if base_node_root is not None:
            overlap_node_root = overlapping_file.xml.find('./region[@id="CharacterVisualBank"]/node[@id="CharacterVisualBank"]/children')
            if overlap_node_root is not None:
                self.add_to_report(f'merging character visuals: {base_file.relative_file_path} <- {overlapping_file.relative_file_path}')
                self.__merge_xml(base_node_root, overlap_node_root, './node[@id="Resource"]', 'ID')
                return


    def __is_mergeable(self, file_name: str) -> bool:
        # Do not attempt to merge dialogs and timelines, this is already done
        if file_name.startswith('Mods/') and '/Story/DialogsBinary/' in file_name:
            return False
        if file_name.startswith('Public/') and '/Timeline/Generated/' in file_name:
            return False
        if file_name.endswith('.lsf'):
            return True
        if '/Gossips/' in file_name:
            return True
        return False


    def merge_overlapping_files(
            self,
            mod_priority_order: tuple[mod_info, ...],
            progress_callback: Callable[[int, int, str], None] | None = None
    ) -> None:
        if progress_callback is not None:
            progress_callback(0, 0, 'Merging overlapping files...')

        overlapping_files_dict = dict[str, tuple[int, list[tuple[int, str]]]]()
        mod_index = 0
        for mod in mod_priority_order:
            if mod.content is None:
                continue
            for f in mod.content.files:
                if not self.__is_mergeable(f):
                    continue
                ps = f.split('/')
                if len(ps) > 2 and (ps[0] == 'Mods' or ps[0] == 'Public'):
                    ps[1] = '$ModName$'
                if len(ps) > 3 and ps[0] == 'Generated' and ps[1] == 'Public':
                    ps[2] = '$ModName$'
                f = '/'.join(ps)
                if f in overlapping_files_dict:
                    overlapping_files_dict[f][1].append((mod_index, f))
                else:
                    overlapping_files_dict[f] = (mod_index, [])
            mod_index += 1

        total_count = len(overlapping_files_dict)
        count = 0
        t = time.time()
        for base_file_name, v in overlapping_files_dict.items():
            count += 1

            base_mod_index, overlapping = v
            if len(overlapping) == 0:
                continue

            base_file_name = base_file_name.replace('$ModName$', mod_priority_order[base_mod_index].mod_folder)

            if progress_callback is not None and time.time() - t >= 1.0:
                t = time.time()
                s = f'Merging overlapping files: {base_file_name}'
                if len(s) > PROGRESS_MSG_LEN:
                    n = len(s) - PROGRESS_MSG_LEN
                    s = f'Merging overlapping files: ...{base_file_name[n + 2:]}'
                progress_callback(count, total_count, s)

            bf = game_file(self.__assets.tool, base_file_name, pak_name = mod_priority_order[base_mod_index].pak_path, mod_specific = True)
            for mod_idx, file_name in overlapping:
                file_name = file_name.replace('$ModName$', mod_priority_order[mod_idx].mod_folder)
                of = game_file(self.__assets.tool, file_name, pak_name = mod_priority_order[mod_idx].pak_path, mod_specific = True)
                self.__merge_overlapping_files(bf, of)
                self.append_to_exclusion_list(mod_priority_order[mod_idx].mod_uuid, file_name)
            self.__assets.files.add(bf)
            self.append_to_exclusion_list(mod_priority_order[base_mod_index].mod_uuid, base_file_name)


    def append_text_content(self, gf: game_file) -> None:
        if self.__loca is None:
            self.__loca = loca_object(self.__assets.files.add_new_file(self.__assets.files.get_loca_relative_path()))
        content_elements = gf.xml.getroot().findall('./content')
        for content_element in content_elements:
            text_handle = content_element.attrib['contentuid']
            text_version = int(content_element.attrib['version'])
            text_line = content_element.text
            if text_line is not None:
                self.__loca.add_line(text_handle, text_version, text_line)


    @staticmethod
    def make_mod_short_name(name: str) -> str:
        valid_chars = 'QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm0123456789.-_'
        result = ''
        for c in name:
            if c in valid_chars:
                result += c
        if len(result) > 48:
            return result[:48]
        return result


    def merge_text_files(self, dest_path: str, src_path: str) -> None:
        with open(dest_path, 'a') as dest:
            with open(src_path, 'r') as src:
                dest.write('\n')
                dest.writelines(src.readlines())


    # this procedure should copy files from source mods to the destination mod
    # it should skip conflicting files
    # it should skip meta.lsx and mod_publish_logo.png for all except the very first mod
    # it should correctly handle override and non-override mods
    # it should merge .loca or .xml localization files 
    # it should merge overlapping soundbanks, dialog banks, timeline banks, etc
    def copy_mod_files(
            self,
            src_mod_root_path: str,
            dest_dir_path: str,
            mod_folder: str,
            mod_uuid: str,
            progress_callback: Callable[[int, int, str], None] | None = None
    ) -> None:
        total_count = 0
        for _, _, files in os.walk(src_mod_root_path):
            total_count += len(files)
        count = 0
        
        t = time.time()
        self.add_to_report(f'copying files from mod {mod_uuid}, source root path {src_mod_root_path}, destination root path {dest_dir_path}')
        for dir, _, files in os.walk(src_mod_root_path):
            for file in files:
                full_src_path = os.path.join(dir, file)

                count += 1
                if progress_callback is not None and time.time() - t >= 1.0:
                    t = time.time()
                    s = f'Copying files: {full_src_path}'
                    if len(s) > PROGRESS_MSG_LEN:
                        n = len(s) - PROGRESS_MSG_LEN
                        s = f'Copying files: ...{full_src_path[n + 2:]}'
                    progress_callback(count, total_count, s)

                rel_dirs = os.path.dirname(os.path.relpath(full_src_path, src_mod_root_path)).split('\\')
                if len(rel_dirs) >= 2:
                    if rel_dirs[0] == 'Mods' or rel_dirs[0] == 'Public':
                        rel_dirs[1] = mod_folder
                if len(rel_dirs) >= 3:
                    if rel_dirs[0] == 'Generated' and rel_dirs[1] == 'Public':
                        rel_dirs[2] = mod_folder
                dest_path = os.path.join(os.path.join(dest_dir_path, *rel_dirs), file)
                if not self.is_in_exclusion_list(mod_uuid, full_src_path):
                    if os.path.isfile(dest_path):
                        if '\\Stats\\' in dest_path:
                            self.merge_text_files(dest_path, full_src_path)
                            self.add_to_report(f'a file already exists at destination {dest_path}, merged text from {full_src_path}')
                        elif '\\Story\\RawFiles\\Goals\\' in dest_path and dest_path.endswith('.txt'):
                            new_dest_path = dest_path.replace('.txt', new_random_uuid()[:8] + '.txt')
                            self.add_to_report(f'copying {full_src_path} to {new_dest_path}')
                            os.makedirs(os.path.dirname(new_dest_path), exist_ok = True)
                            shutil.copy(full_src_path, new_dest_path)
                        else:
                            self.add_to_report(f'a file already exists at destination {dest_path}, skipped copying {full_src_path}')
                    else:
                        self.add_to_report(f'copying {full_src_path} to {dest_path}')
                        os.makedirs(os.path.dirname(dest_path), exist_ok = True)
                        shutil.copy(full_src_path, dest_path)
                else:
                    self.add_to_report(f'skipped {full_src_path} because it is in exclusion list of [{mod_uuid}]')
        self.add_to_report(f'finished copying files from mod {mod_uuid}')


    def unpack_mod(self, mi: mod_info) -> str:
        dest_path = os.path.join(self.__assets.tool.env.output_path, 'build', mi.mod_uuid)
        os.makedirs(dest_path)
        self.__assets.tool.unpack_pak(mi.pak_path, dest_path)
        return dest_path


    def merge_conflicting_dialogs(self, dialog_uuid: str, mods: tuple[mod_info, ...]) -> None:
        # Dialog conflict resolution
        # dialog_uuid contains the conflicting dialog resource UUID
        # mods are sorted by priority
        # algorithm:
        # find the dialog in the mods, starting from the head of the list
        # find the diff between this dialog and 
        # initialize the result with that dialog
        # use differ to find all nodes that are changed in the dialog
        # look for the next variant of the dialog in remaining mods
        # for each 'remaining' dialog, run the differ and determine changed nodes that are not overwritten yet
        # copy those nodes into the result
        # continue until all mods are processed

        name = self.__assets.index.get_dialog_name(dialog_uuid)
        dialog_name = f'{name}_{dialog_uuid}'
        timeline_name = f'{name}_{self.__assets.index.get_timeline_uuid_by_dialog_uuid(dialog_uuid)}'
        self.add_to_report(f'resolving conflicts in dialog {dialog_name} and timeline {timeline_name}')

        result_dialog : dialog_object | None = None
        result_dialog_resource: XmlElement | None = None
        dialog_nodes_diff = dict[str, str]()
        root_nodes_diff = dict[str, str]()

        result_timeline: timeline_object | None = None
        result_timeline_resource: XmlElement | None = None
        changed_phases = set[str]()

        result_scene_file_lsf: game_file | None = None
        result_scene_file_lsx: game_file | None = None

        d_differ = dialog_differ(self.__assets)
        t_differ = timeline_differ(self.__assets)
        for modinfo in mods:
            modcontent = modinfo.content
            if modcontent is None:
                continue
            mod_uuid = modinfo.mod_uuid
            if modcontent.has_content_bundle(dialog_uuid):
                cb = modcontent.get_content_bundle(dialog_uuid)

                if result_dialog is None:
                    # the top priority dialog object
                    if cb.dialog_file:
                        self.add_to_report(f'baseline dialog {dialog_name} is taken from mod {modinfo.mod_short_name} [{mod_uuid}]')
                        self.append_to_exclusion_list(mod_uuid, cb.dialog_file)
                        result_dialog = dialog_object(game_file(self.__assets.tool, cb.dialog_file, pak_name = modinfo.pak_path, mod_specific = True))
                        result_dialog_resource = self.get_dialog_resource(dialog_uuid, modcontent)
                        dialog_nodes_diff = d_differ.get_modified_dialog_nodes(result_dialog, dialog_uuid)
                        root_nodes_diff = d_differ.get_modified_dialog_root_nodes(result_dialog, dialog_uuid)
                else:
                    # the next conflicting dialog object
                    if cb.dialog_file:
                        self.add_to_report(f'merging dialog {dialog_name} from mod {modinfo.mod_short_name} [{mod_uuid}]')
                        self.append_to_exclusion_list(mod_uuid, cb.dialog_file)
                        modded_dialog = dialog_object(game_file(self.__assets.tool, cb.dialog_file, pak_name = modinfo.pak_path))
                        diff = d_differ.get_modified_dialog_nodes(modded_dialog, dialog_uuid)
                        root_diff = d_differ.get_modified_dialog_root_nodes(modded_dialog, dialog_uuid)
                        self.merge_dialog_nodes(dialog_uuid, result_dialog, dialog_nodes_diff, root_nodes_diff, modded_dialog, diff, root_diff)

                if result_timeline is None:
                    # the top priority timeline object
                    if cb.timeline_file:
                        self.add_to_report(f'baseline timeline {timeline_name} is taken from mod {modinfo.mod_short_name} [{mod_uuid}]')
                        self.append_to_exclusion_list(mod_uuid, cb.timeline_file)
                        gf = game_file(self.__assets.tool, cb.timeline_file, pak_name = modinfo.pak_path)
                        if result_dialog:
                            d = result_dialog
                        else:
                            d = self.__assets.get_dialog_object(dialog_uuid)
                        result_timeline = timeline_object(gf, d)
                        result_timeline_resource = self.get_timeline_resource(cb.timeline_uuid, modcontent)
                        timeline_nodes_diff = t_differ.get_modified_timeline_nodes(result_timeline, dialog_uuid)
                        for diff_state in timeline_nodes_diff.values():
                            phase_uuid = diff_state.split('|')[1]
                            changed_phases.add(phase_uuid)
                else:
                    # the next conflicting timeline object
                    if cb.timeline_file:
                        self.add_to_report(f'merging timeline {timeline_name} from mod {modinfo.mod_short_name} [{mod_uuid}]')
                        self.append_to_exclusion_list(mod_uuid, cb.timeline_file)
                        gf = game_file(self.__assets.tool, cb.timeline_file, pak_name=modinfo.pak_path)
                        if result_dialog:
                            d = result_dialog
                        else:
                            d = self.__assets.get_dialog_object(dialog_uuid)
                        modded_timeline = timeline_object(gf, d)
                        timeline_nodes_diff = t_differ.get_modified_timeline_nodes(modded_timeline, dialog_uuid)
                        self.merge_timeline_nodes(dialog_uuid, result_timeline, changed_phases, modded_timeline, timeline_nodes_diff)

                # Take the scene file from the top priority mod
                # Resolution of scene conflicts is not supported yet
                if result_scene_file_lsf is None and cb.scene_lsf_file:
                    result_scene_file_lsf = game_file(self.__assets.tool, cb.scene_lsf_file, pak_name = modinfo.pak_path, mod_specific = True)
                    self.append_to_exclusion_list(mod_uuid, cb.scene_lsf_file)
                if result_scene_file_lsx is None and cb.scene_lsx_file:
                    result_scene_file_lsx = game_file(self.__assets.tool, cb.scene_lsx_file, pak_name = modinfo.pak_path, mod_specific = True)
                    self.append_to_exclusion_list(mod_uuid, cb.scene_lsx_file)


        if result_dialog is None and result_timeline is None:
            self.add_to_report(f'unexpected: both dialog and timeline are None after resolution for dialog uuid {dialog_uuid}')
            self.add_to_report(f'mods: {','.join([m.mod_short_name + m.mod_uuid for m in mods])}')
            return

        vanilla_name = None
        if self.__assets.index.has_entry(dialog_uuid):
            vanilla_relative_path = self.__assets.index.get_entry(dialog_uuid)['lsf_path']
            n1 = vanilla_relative_path.rfind('/')
            n2 = vanilla_relative_path.rfind('.')
            if n1 == -1 or n2 == -1:
                raise ValueError(f'Bad lsf_path {vanilla_relative_path}, dialog uuid = {dialog_uuid}')
            vanilla_name = vanilla_relative_path[n1 + 1 : n2]

        # Make sure the names match
        if result_dialog is not None and result_timeline is not None:
            if vanilla_name:
                new_name = '_'.join([self.__assets.files.mod_name, vanilla_name])
            else:
                n1 = result_dialog.dialog_file.relative_file_path.rfind('/')
                n2 = result_dialog.dialog_file.relative_file_path.rfind('.')
                if n1 == -1 or n2 == -1:
                    raise ValueError(f'Bad lsf_path {result_dialog.dialog_file.relative_file_path}, dialog uuid = {dialog_uuid}')
                file_name = result_dialog.dialog_file.relative_file_path[n1 + 1 : n2]
                new_name = '_'.join([self.__assets.files.mod_name, file_name])
            result_dialog.dialog_file.rename_to = new_name
            result_timeline.timeline_file.rename_to = new_name
            # Rename scene files to match timeline and dialog names
            if result_scene_file_lsf is not None:
                result_scene_file_lsf.rename_to = new_name + '_Scene'
            if result_scene_file_lsx is not None:
                result_scene_file_lsx.rename_to = new_name + '_Scene'
        elif vanilla_name:
            if result_dialog is not None and result_timeline is None:
                result_dialog.dialog_file.rename_to = vanilla_name
            elif result_dialog is None and result_timeline is not None:
                result_timeline.timeline_file.rename_to = vanilla_name
                # Rename scene files to match timeline and dialog names
                if result_scene_file_lsf is not None:
                    result_scene_file_lsf.rename_to = vanilla_name + '_Scene'
                if result_scene_file_lsx is not None:
                    result_scene_file_lsx.rename_to = vanilla_name + '_Scene'

        if result_dialog is not None:
            result_dialog.dialog_file.is_mod_specific = True
            self.__assets.files.add(result_dialog.dialog_file)
            self.add_to_report(f'added dialog {dialog_name} to the build, file name {result_dialog.dialog_file.relative_file_path}, output file name {result_dialog.dialog_file.get_output_relative_path(self.__assets.files)}')
            if result_dialog_resource is not None:
                self.__assets.add_to_dialog_bank(result_dialog_resource, result_dialog.dialog_file)
                self.add_to_report(f'added dialog {dialog_name} to the dialog bank, dialog uuid = {dialog_uuid}')
            else:
                self.add_to_report(f'unexpected: dialog resource for {dialog_name} is None, dialog uuid = {dialog_uuid}')

        if result_timeline is not None:
            result_timeline.timeline_file.is_mod_specific = True
            self.__assets.files.add(result_timeline.timeline_file)
            self.add_to_report(f'added timeline {timeline_name} to the build, file name {result_timeline.timeline_file.relative_file_path}, output file name {result_timeline.timeline_file.get_output_relative_path(self.__assets.files)}')
            if result_timeline_resource is not None:
                self.__assets.add_to_timeline_bank(result_timeline_resource, result_timeline.timeline_file)
                self.add_to_report(f'added timeline {timeline_name} to the timeline bank')
            else:
                self.add_to_report(f'unexpected: timeline resource for {timeline_name} is None, dialog uuid = {dialog_uuid}')

        if result_scene_file_lsf is not None:
            self.__assets.files.add(result_scene_file_lsf)
            self.add_to_report(f'added scene file for {timeline_name} to the build, file name {result_scene_file_lsf.relative_file_path}, output file name {result_scene_file_lsf.get_output_relative_path(self.__assets.files)}')

        if result_scene_file_lsx is not None:
            self.__assets.files.add(result_scene_file_lsx)
            self.add_to_report(f'added scene file for {timeline_name} to the build, file name {result_scene_file_lsx.relative_file_path}, output file name {result_scene_file_lsx.get_output_relative_path(self.__assets.files)}')

        self.add_to_report(f'finished resolving conflicts in dialog {dialog_name} and timeline {timeline_name}, dialog uuid = {dialog_uuid}')


    def get_dialog_resource(self, dialog_uuid: str, content: pak_content) -> XmlElement:
        try:
            return content.get_dialog_resource(dialog_uuid)
        except:
            pass
        self.add_to_report(f'failed to retrieve dialog resource for dialog uuid {dialog_uuid}, falling back to vanilla game resource')
        return self.__assets.get_dialog_resource(dialog_uuid)


    def get_timeline_resource(self, timeline_uuid: str, content: pak_content) -> XmlElement:
        try:
            return content.get_timeline_resource(timeline_uuid)
        except:
            pass
        self.add_to_report(f'failed to retrieve timeline resource for timeline uuid {timeline_uuid}, falling back to vanilla game resource')
        return self.__assets.get_timeline_resource(timeline_uuid)


    def append_to_exclusion_list(self, mod_uuid: str, file: str) -> None:
        if mod_uuid not in self.__conflicting_files:
            conflicting_files = list[str]()
            self.__conflicting_files[mod_uuid] = conflicting_files
        else:
            conflicting_files = self.__conflicting_files[mod_uuid]
        conflicting_files.append(file.replace('/', '\\'))
        self.add_to_report(f'added to exclusion list of mod [{mod_uuid}]: {file}')


    def is_in_exclusion_list(self, mod_uuid: str, file: str) -> bool:
        if mod_uuid not in self.__conflicting_files:
            return False
        conflicting_files = self.__conflicting_files[mod_uuid]
        for conflicting_file in conflicting_files:
            if file.endswith(conflicting_file):
                return True
        return False


    def merge_dialog_nodes(
            self,
            dialog_uuid: str,
            destination_dialog: dialog_object,
            destination_diff: dict[str, str],
            destination_root_diff: dict[str, str],
            source_dialog: dialog_object,
            source_diff: dict[str, str],
            source_root_diff: dict[str, str]
    ) -> None:
        try:
            self.add_to_report(f'merging dialog nodes for {dialog_uuid}')
            for node_uuid, node_state in source_diff.items():
                self.add_to_report(f'dialog node {node_uuid}, diff {node_state}')
                if node_uuid in destination_diff:
                    self.add_to_report(f'dialog node {node_uuid} is already changed in higher priority mod, skipped')
                    continue
                if node_state == dialog_differ.DELETED:
                    self.add_to_report(f'dialog node {node_uuid} is deleted, no action')
                    continue
                elif node_state == dialog_differ.MODIFIED or node_state == dialog_differ.ADDED:
                    if destination_dialog.has_dialog_node(node_uuid):
                        destination_dialog.delete_dialog_node(node_uuid)
                        self.add_to_report(f'dialog node {node_uuid}, found and removed existing node')
                    node = copy.deepcopy(source_dialog.find_dialog_node(node_uuid))
                    destination_dialog.add_dialog_node(node)
                    destination_diff[node_uuid] = node_state
                    self.add_to_report(f'copied dialog node {node_uuid} into the result')
                else:
                    raise RuntimeError(f'unexpected diff node state for node {node_uuid}: {node_state}')
            destination_root_nodes = set(destination_dialog.get_root_nodes())
            for root_node_uuid, root_node_state in source_root_diff.items():
                self.add_to_report(f'root dialog node {root_node_uuid}, diff {root_node_state}')
                if root_node_uuid in destination_root_diff:
                    self.add_to_report(f'root dialog node {root_node_uuid} is already changed in higher priority mod, skipped')
                    continue
                if root_node_state == dialog_differ.DELETED:
                    self.add_to_report(f'root dialog node {root_node_uuid} is deleted, removing it from the result')
                    destination_dialog.remove_root_node(root_node_uuid)
                elif root_node_state == dialog_differ.ADDED or root_node_state == dialog_differ.MODIFIED:
                    source_root_nodes = source_dialog.get_root_nodes()
                    source_root_nodes_order = source_dialog.get_root_nodes_order()
                    # find the 'next' root in the source node that is after the 'modified' node
                    mod_node_idx = source_root_nodes_order[root_node_uuid] + 1
                    next_node_uuid = ''
                    while mod_node_idx < len(source_root_nodes):
                        if source_root_nodes[mod_node_idx] in destination_root_nodes:
                            next_node_uuid = source_root_nodes[mod_node_idx]
                            break
                        mod_node_idx += 1
                    self.add_to_report(f'root dialog node {root_node_uuid}, found the next root node "{next_node_uuid}" in source')
                    # remove this node if it already exists
                    if root_node_uuid in destination_root_nodes:
                        self.add_to_report(f'root dialog node {root_node_uuid}, removed existing entry from the result')
                        destination_dialog.remove_root_node(root_node_uuid)
                    if next_node_uuid == '':
                        # add to the tail if node is not found
                        destination_dialog.add_root_node(root_node_uuid)
                        self.add_to_report(f'root dialog node {root_node_uuid}, added to the tail of the result')
                    else:
                        # add before the 'next' node
                        destination_dialog.add_root_node_before(next_node_uuid, root_node_uuid)
                        self.add_to_report(f'root dialog node {root_node_uuid}, added to the result before {next_node_uuid}')
                else:
                    raise RuntimeError(f'unexpected dialog diff root node state for node {root_node_uuid}: {root_node_state}')
        except BaseException as exc:
            raise RuntimeError(f'merge_dialog_nodes() failed for dialog {dialog_uuid}') from exc
        finally:
            self.add_to_report(f'finished merging dialog nodes for {dialog_uuid}')


    def __print_node_interval(self, node: XmlElement, what: str) -> None:
        node_uuid = get_required_bg3_attribute(node, 'ID')
        start = get_bg3_attribute(node, 'StartTime')
        if start is None:
            start = '0.0'
        end = get_required_bg3_attribute(node, 'EndTime')
        self.add_to_report(f'{what} node interval [{node_uuid}]: {start} to {end}')


    def merge_timeline_nodes(
            self,
            dialog_uuid: str,
            destination_timeline: timeline_object,
            already_changed_phases: set[str],
            source_timeline: timeline_object,
            source_timeline_diff: dict[str, str]
    ) -> None:
        try:
            self.add_to_report(f'merging timeline nodes for {dialog_uuid}')
            self.add_to_report(f'destination timeline duration: {destination_timeline.duration}')
            for node_uuid, node_state in source_timeline_diff.items():
                self.add_to_report(f'timeline node {node_uuid}, diff {node_state}')
                p = node_state.split('|')
                node_state = p[0]
                phase_uuid = p[1]
                if phase_uuid in already_changed_phases:
                    self.add_to_report(f'timeline phase {phase_uuid} is already changed in higher priority mod, skipped timeline node {node_uuid}')
                    continue
                if node_state == timeline_differ.DELETED:
                    self.add_to_report(f'timeline node {node_uuid} is deleted in the source, removing it from the result')
                    destination_timeline.remove_effect_component(node_uuid)
                elif node_state == timeline_differ.ADDED or node_state == timeline_differ.MODIFIED:
                    if destination_timeline.has_phase(phase_uuid):
                        destionation_phase = destination_timeline.use_existing_phase(phase_uuid)
                        self.add_to_report(f'timeline phase {phase_uuid} exists in the result, phase index {destionation_phase.index}')
                    else:
                        self.add_to_report(f'timeline phase {phase_uuid} does not exists in the result')
                        source_phase = source_timeline.get_timeline_phase(phase_uuid)
                        self.add_to_report(f'source phase {phase_uuid} starts at {source_phase.start}, ends at {source_phase.end}')
                        destination_timeline.create_new_phase(source_phase.dialog_node_uuid, source_phase.duration, additional_nodes=source_phase.group_nodes_uuids)
                        destionation_phase = destination_timeline.use_existing_phase(phase_uuid)
                        self.add_to_report(f'timeline phase {phase_uuid} was created in the result, phase index {destionation_phase.index}, source phase index {source_phase.index}')
                        self.add_to_report(f'destination phase {phase_uuid} starts at {destionation_phase.start}, ends at {destionation_phase.end}')
                        self.add_to_report(f'destination timeline duration: {destination_timeline.duration}')
                    
                    if destination_timeline.has_effect_component(node_uuid):
                        self.add_to_report(f'timeline phase {phase_uuid} in the result contains existing node {node_uuid}, removing it')
                        destination_timeline.remove_effect_component(node_uuid)
                    
                    effect_component = source_timeline.find_effect_component(node_uuid)
                    self.__print_node_interval(effect_component, 'source effect_component')
                    source_phase = source_timeline.get_timeline_phase(phase_uuid)
                    normalized_node = timeline_differ.normalize_tl_node(effect_component, source_phase.start, source_phase.duration)
                    self.__print_node_interval(normalized_node, 'source normalized_node')
                    destination_node = timeline_differ.normalize_tl_node(normalized_node, destionation_phase.start.copy_negate())
                    self.__print_node_interval(destination_node, 'destination_node')
                    set_bg3_attribute(destination_node, 'PhaseIndex', destionation_phase.index, attribute_type = 'int64')


                    self.add_to_report(f'normalized node {node_uuid}, source start {source_phase.start}, start in the result {destionation_phase.start}')
                    destination_timeline.insert_new_tl_node(destination_node)
                    self.add_to_report(f'timeline phase {phase_uuid}, added node {node_uuid} to the result')
                else:
                    raise RuntimeError(f'unexpected timeline diff root node state for node {node_uuid}: {node_state}')
        except BaseException as exc:
            raise RuntimeError(f'merge_timeline_nodes() failed for dialog {dialog_uuid}') from exc
        finally:
            self.add_to_report(f'finished merging timeline nodes for {dialog_uuid}')

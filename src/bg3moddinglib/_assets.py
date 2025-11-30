from __future__ import annotations

import gzip
import json
import os.path
import sys
import xml.etree.ElementTree as et

from base64 import b64encode, b64decode
from typing import cast

from ._dialog import dialog_object
from ._common import new_random_uuid, set_bg3_attribute, get_bg3_attribute, get_required_bg3_attribute, has_bg3_attribute, remove_all_nodes
from ._constants import *
from ._files import game_file, game_files
from ._loca import loca_object
from ._scene import scene_object
from ._timeline import timeline_object
from ._tool import bg3_modding_tool

class dialog_asset_bundle:
    __original_dialog_uuid: str
    __modded_dialog_uuid: str
    __original_timeline_uuid: str
    __modded_timeline_uuid: str
    __dialog: game_file
    __timeline: game_file
    __scene_lsf: game_file
    __scene_lsx: game_file

    def __init__(
            self,
            original_dialog_uuid: str,
            modded_dialog_uuid: str,
            original_timeline_uuid: str,
            modded_timeline_uuid: str,
            dialog: game_file,
            timeline: game_file,
            scene_lsf: game_file,
            scene_lsx: game_file
    ) -> None:
        self.__original_dialog_uuid = original_dialog_uuid
        self.__modded_dialog_uuid = modded_dialog_uuid
        self.__original_timeline_uuid = original_timeline_uuid
        self.__modded_timeline_uuid = modded_timeline_uuid
        self.__dialog = dialog
        self.__timeline = timeline
        self.__scene_lsf = scene_lsf
        self.__scene_lsx = scene_lsx

    @property
    def original_dialog_uuid(self) -> str:
        return self.__original_dialog_uuid

    @property
    def modded_dialog_uuid(self) -> str:
        return self.__modded_dialog_uuid

    @property
    def original_timeline_uuid(self) -> str:
        return self.__original_timeline_uuid

    @property
    def modded_timeline_uuid(self) -> str:
        return self.__modded_timeline_uuid

    @property
    def dialog(self) -> game_file:
        return self.__dialog
    
    @property
    def timeline(self) -> game_file:
        return self.__timeline

    @property
    def scene_lsf(self) -> game_file:
        return self.__scene_lsf

    @property
    def scene_lsx(self) -> game_file:
        return self.__scene_lsx


class dialog_index:
    __paks: tuple[str, ...]
    __files: game_files
    __index: dict[str, dict]

    INDEX_VERSION = '2025-10-16'

    def __init__(self, files: game_files) -> None:
        self.__paks = ()
        self.__files = files
        file_path = self.index_path
        self.__index = {}
        if os.path.isfile(file_path):
            with gzip.open(file_path, 'rt') as f:
                self.__index = cast(dict[str, dict], json.load(f))
            try:
                if self.__index['version']['index_version'] != dialog_index.INDEX_VERSION:
                    self.__index = {}
            except KeyError:
                self.__index = {}
                os.unlink(file_path)
        if not self.__index:
            self.__index = self.create()
            os.makedirs(os.path.dirname(file_path), exist_ok = True)
            with gzip.open(file_path, 'wt') as f:
                json.dump(self.__index, f)

    @property
    def index_path(self) -> str:
        return os.path.join(self.__files.tool.env.index_path, 'dialog_index.json.gz')

    def get_pak_by_file(self, file_path_or_name: str) -> str:
        files_to_paks = self.__index['files_to_paks']
        fp = file_path_or_name.lower()
        if fp in files_to_paks:
            return files_to_paks[fp]
        raise RuntimeError(f'Cannot find file path {file_path_or_name}')

    def get_dialog_name(self, path_or_uuid: str) -> str:
        dialog_name_index = self.__index['dialog_name_index']
        if path_or_uuid in dialog_name_index:
            return dialog_name_index[path_or_uuid]
        raise RuntimeError(f'Cannot find dialog by {path_or_uuid}')

    def get_timeline_resource(self, timeline_uuid: str) -> et.Element:
        timeline_index = self.__index['timeline_index']
        if timeline_uuid in timeline_index:
            return et.fromstring(b64decode(timeline_index[timeline_uuid]))
        raise RuntimeError(f'Timeline {timeline_uuid} is not found')

    def get_timeline_file_path(self, timeline_uuid: str) -> str:
        timeline_index = self.__index['timeline_index']
        if timeline_uuid in timeline_index:
            timeline_res = et.fromstring(b64decode(timeline_index[timeline_uuid]))
            return get_required_bg3_attribute(timeline_res, 'SourceFile')
        raise RuntimeError(f'Timeline {timeline_uuid} is not found')

    def get_timeline_uuid_by_dialog_uuid(self, dialog_uuid: str) -> str:
        timeline_by_dialog_index = self.__index['timeline_by_dialog_index']
        if dialog_uuid in timeline_by_dialog_index:
            return timeline_by_dialog_index[dialog_uuid]
        raise RuntimeError(f'Timeline for dialog {dialog_uuid} is not found')

    def discover_paks(self) -> tuple[str, ...]:
        if self.__paks:
            return self.__paks
        result = list[str]()
        patches = list[str]()
        bg3_data_path = self.__files.tool.env.bg3_data_path
        for d in os.scandir(bg3_data_path):
            if not d.is_file():
                continue
            name = d.name.lower()
            if name.startswith('gustav_'):
                continue
            if 'sound' in name:
                continue
            if name.startswith('gustav') or name.startswith('shared'):
                result.append(d.name)
            elif name.startswith('patch') and 'hotfix' in name:
                patches.append(d.name)
        result.sort()
        patches.sort()
        result += patches
        self.__paks = tuple(result)
        return self.__paks

    def create(self) -> dict[str, dict]:
        t = self.__files.tool
        index = dict[str, dict]()
        index['version'] = { 'index_version': dialog_index.INDEX_VERSION }

        paks = self.discover_paks()
        files_to_paks = dict[str, str]()
        all_files = list[tuple[str, str]]()
        for pak in paks:
            listing = self.__files.tool.list(pak)
            for file_path in listing:
                file_name = os.path.basename(file_path)
                if not file_name.startswith('_'):
                    files_to_paks[file_name.lower()] = pak
                files_to_paks[file_path.lower()] = pak
                all_files.append((file_path, pak))
        index['files_to_paks'] = files_to_paks

        timeline_index = dict[str, str]()
        timeline_by_dialog_index = dict[str, str]()
        for file_path, pak_name in all_files:
            if '/Content/Generated/[PAK]_GeneratedDialogTimelines/' in file_path:
                merged_lsf = game_file(self.__files.tool, file_path, pak_name = pak_name)
                timelines = merged_lsf.root_node.findall('./region[@id="TimelineBank"]/node[@id="TimelineBank"]/children/node[@id="Resource"]')
                for timeline in timelines:
                    timeline_uuid = get_required_bg3_attribute(timeline, 'ID')
                    dialog_uuid = get_required_bg3_attribute(timeline, 'DialogResourceId')
                    timeline_index[timeline_uuid] = b64encode(et.tostring(timeline)).decode()
                    timeline_by_dialog_index[dialog_uuid] = timeline_uuid
        index['timeline_index'] = timeline_index
        index['timeline_by_dialog_index'] = timeline_by_dialog_index

        text_bank = loca_object(self.__files.get_text_bank_file())

        dialog_idx = dict[str, dict]()
        dialog_name_idx = dict[str, str]()
        character_idx = dict[str, str]()
        for file_path, pak_name in all_files:
            if '/Content/Assets/Dialogs/' in file_path:
                merged_lsf = game_file(t, file_path, pak_name = pak_name)
                dialogs = merged_lsf.root_node.findall('./region[@id="DialogBank"]/node[@id="DialogBank"]/children/node[@id="Resource"]')
                for dialog in dialogs:
                    name = get_required_bg3_attribute(dialog, 'Name')
                    lsj_path = get_required_bg3_attribute(dialog, 'SourceFile')
                    if len(name) == 0 or len(lsj_path) == 0:
                        continue
                    name_key = name.lower()
                    dialog_uuid = get_required_bg3_attribute(dialog, 'ID')
                    timeline_uuid = timeline_by_dialog_index[dialog_uuid] if dialog_uuid in timeline_by_dialog_index else ''
                    lsf_path = lsj_path.replace('/Story/Dialogs/', '/Story/DialogsBinary/')[:-4] + '.lsf'
                    index_entry = {
                        'dialog_uuid': dialog_uuid,
                        'timeline_uuid': timeline_uuid,
                        'lsf_path': lsf_path,
                        'lsj_path': lsj_path,
                        'dialog_bank_path': file_path,
                        'dialog_bank_pak': pak_name,
                    }
                    file_name, _ = os.path.splitext(os.path.basename(lsf_path))
                    file_name = file_name.lower()
                    dialog_idx[name_key] = index_entry
                    if file_name != name_key:
                        dialog_idx[file_name] = index_entry
                    dialog_name_idx[lsf_path.lower()] = name_key
                    dialog_name_idx[lsj_path.lower()] = name_key
                    dialog_name_idx[dialog_uuid] = name_key
            elif file_path.endswith('/Characters/_merged.lsf'):
                merged_lsf = game_file(t, file_path, pak_name = pak_name)
                characters = merged_lsf.root_node.findall('./region[@id="Templates"]/node[@id="Templates"]/children/node[@id="GameObjects"]')
                for character in characters:
                    if get_bg3_attribute(character, 'Type') != 'character':
                        continue
                    key = get_required_bg3_attribute(character, 'MapKey')
                    display_name = ""
                    try:
                        if has_bg3_attribute(character, 'DisplayName'):
                            handle = get_required_bg3_attribute(character, 'DisplayName', value_name = 'handle')
                            display_name = text_bank.get_line(handle)
                    except:
                        pass
                    if not display_name:
                        if has_bg3_attribute(character, 'Name'):
                            display_name = get_required_bg3_attribute(character, 'Name')
                        elif has_bg3_attribute(character, 'AnubisConfigName'):
                            display_name = get_required_bg3_attribute(character, 'AnubisConfigName')
                        else:
                            display_name = f'Character_{key}'
                    character_idx[key] = display_name
            elif file_path.endswith('/Voice/SpeakerGroups.lsf'):
                speaker_groups_lsf = game_file(t, file_path, pak_name = pak_name)
                speaker_groups = speaker_groups_lsf.root_node.findall('./region[@id="SpeakerGroups"]/node[@id="SpeakerGroups"]/children/node[@id="SpeakerGroup"]')
                for speaker_group in speaker_groups:
                    key = get_required_bg3_attribute(speaker_group, 'UUID')
                    if key == 'e0d1ff71-04a8-4340-ae64-9684d846eb83':
                        name_key = 'Player'
                    elif key == 'e6b3c2c4-e88d-e9e6-ffa1-d49cdfadd411':
                        name_key = 'Dark Urge'
                    else:
                        name_key = get_required_bg3_attribute(speaker_group, 'Name')
                    character_idx[key] = name_key
            for k,v in SPEAKER_NAME.items():
                character_idx[k] = v

        index['dialog_index'] = dialog_idx
        index['dialog_name_index'] = dialog_name_idx
        index['character_index'] = character_idx
        return index

    def refresh(self) -> None:
        file_path = self.index_path
        if os.path.exists(file_path):
            os.unlink(file_path)
        self.__index = self.create()
        os.makedirs(os.path.dirname(file_path), exist_ok = True)
        with gzip.open(file_path, 'wt') as f:
            json.dump(self.__index, f)

    def has_entry(self, dialog_name: str) -> bool:
        dialog_name = dialog_name.lower()
        dialog_index = self.__index['dialog_index']
        return  dialog_name in dialog_index

    def get_entry(self, dialog_name: str) -> dict[str, str]:
        dialog_name = dialog_name.lower()
        dialog_index = self.__index['dialog_index']
        if dialog_name in dialog_index:
            return dialog_index[dialog_name]
        raise KeyError(f"Dialog {dialog_name} doesn't exist")

    def get_all_entries(self) -> tuple[dict[str, str], ...]:
        dialog_index = cast(dict[str, dict[str, str]], self.__index['dialog_index'])
        return tuple(dialog_index.values())

    def get_all_dialog_names(self) -> tuple[str, ...]:
        dialog_index = cast(dict[str, str], self.__index['dialog_index'])
        return tuple(dialog_index.keys())

    def get_character_name(self, character_uuid: str) -> str | None:
        if 'character_index' not in self.__index:
            raise RuntimeError('character name index is not initialized')
        if character_uuid not in self.__index['character_index']:
            return None
        return self.__index['character_index'][character_uuid]

    def get_dialogs_paths(self) -> tuple[tuple[str, str], ...]:
        r = list[tuple[str, str]]()
        for val in self.__index['dialog_index'].values():
            lsf_path = val['lsf_path']
            if not isinstance(lsf_path, str):
                raise TypeError(f"'lsf_path' value should be str, got {type(lsf_path)}")
            k = lsf_path.lower()
            if k in self.__index['files_to_paks']:
                r.append((self.__index['files_to_paks'][k], lsf_path))
            else:
                lsj_path = val['lsj_path']
                if not isinstance(lsj_path, str):
                    raise TypeError(f"'lsj_path' value should be str, got {type(lsj_path)}")
                k = lsj_path.lower()
                if k in self.__index['files_to_paks']:
                    r.append((self.__index['files_to_paks'][k], lsj_path))
        return tuple(r)


class bg3_assets:
    __files: game_files
    __index: dialog_index
    __dialog_bank: game_file | None
    __dialog_bank_parent_node: et.Element[str] | None
    __timeline_bank: game_file | None
    __timeline_bank_parent_node: et.Element[str] | None
    __asset_bundles: dict[str, dialog_asset_bundle]

    def __init__(self, files: game_files) -> None:
        self.__files = files
        self.__index = dialog_index(files)
        self.__asset_bundles = dict[str, dialog_asset_bundle]()
        self.__dialog_bank = None
        self.__dialog_bank_parent_node = None
        self.__timeline_bank = None
        self.__timeline_bank_parent_node = None


    @property
    def index(self) -> dialog_index:
        return self.__index


    @property
    def files(self) -> game_files:
        return self.__files


    @property
    def tool(self) -> bg3_modding_tool:
        return self.__files.tool


    def __get_dialog_bank_parent_node(self) -> et.Element[str]:
        if self.__dialog_bank_parent_node is None:
            #self.__dialog_bank = self.__files.add_new_file(f'Public/ModNameHere/Content/Assets/Dialogs/[PAK]_{files.mod_name_uuid}/_merged.lsf', is_mod_specific = True)
            self.__dialog_bank = self.__files.add_new_file(f'Public/ModNameHere/Content/[PAK]_{self.files.mod_name_uuid}/{self.files.mod_name_uuid}.lsf', is_mod_specific = True)
            dialog_bank_root_node = self.__dialog_bank.root_node
            dialog_bank_root_node.append(et.fromstring('<version major="4" minor="0" revision="9" build="0" lslib_meta="v1,bswap_guids,lsf_adjacency" />'))
            dialog_bank_root_node.append(et.fromstring(''.join((
                '<region id="DialogBank">',
                '<node id="DialogBank">',
                '<children>',
                '</children>',
                '</node>',
                '</region>'))))
            dialog_bank_parent_node = dialog_bank_root_node.find('./region[@id="DialogBank"]/node[@id="DialogBank"]/children')
            if dialog_bank_parent_node is None:
                raise RuntimeError('Corrupt dialog bank')
            self.__dialog_bank_parent_node = dialog_bank_parent_node
        return self.__dialog_bank_parent_node


    def __get_timeline_bank_parent_node(self) -> et.Element[str]:
        if self.__timeline_bank_parent_node is None:
            self.__timeline_bank = self.__files.add_new_file(f'Public/ModNameHere/Content/Generated/[PAK]_GeneratedDialogTimelines/{self.files.mod_name_uuid}.lsf', is_mod_specific = True)
            timeline_bank_root_node = self.__timeline_bank.root_node
            timeline_bank_root_node.append(et.fromstring('<version major="4" minor="0" revision="9" build="0" lslib_meta="v1,bswap_guids,lsf_adjacency" />'))
            timeline_bank_root_node.append(et.fromstring(''.join((
                '<region id="TimelineBank">',
                '<node id="TimelineBank">',
                '<children>',
                '</children>',
                '</node>',
                '</region>'))))
            timeline_bank_parent_node = timeline_bank_root_node.find('./region[@id="TimelineBank"]/node[@id="TimelineBank"]/children')
            if timeline_bank_parent_node is None:
                raise RuntimeError('Corrupt dialog bank')
            self.__timeline_bank_parent_node = timeline_bank_parent_node
        return self.__timeline_bank_parent_node


    def get_modded_dialog_asset_bundle(self, dialog_name: str) -> dialog_asset_bundle:
        dialog_name = dialog_name.lower()
        if dialog_name in self.__asset_bundles:
            return self.__asset_bundles[dialog_name]
        raise KeyError(f'Cannot find an asset bundle for dialog name {dialog_name}')


    def get_dialog_object(self, dialog_name: str, /, with_editor_context: bool = False) -> dialog_object:
        index_entry = self.__index.get_entry(dialog_name)
        if not with_editor_context:
            try:
                source_dialog_path = index_entry['lsf_path']
                pak_name = self.__index.get_pak_by_file(source_dialog_path)
                return dialog_object(self.__files.get_file(pak_name, source_dialog_path, exclude_from_build = True))
            except:
                pass
        source_dialog_path = index_entry['lsj_path']
        pak_name = self.__index.get_pak_by_file(source_dialog_path)
        return dialog_object(self.__files.get_file(pak_name, source_dialog_path, exclude_from_build = True))


    def get_timeline_object(self, dialog_name: str) -> timeline_object:
        d = None
        index_entry = self.__index.get_entry(dialog_name)
        try:
            source_dialog_path = index_entry['lsf_path']
            pak_name = self.__index.get_pak_by_file(source_dialog_path)
            d = dialog_object(self.__files.get_file(pak_name, source_dialog_path, exclude_from_build = True))
        except:
            pass
        if d is None:
            source_dialog_path = index_entry['lsj_path']
            pak_name = self.__index.get_pak_by_file(source_dialog_path)
            d = dialog_object(self.__files.get_file(pak_name, source_dialog_path, exclude_from_build = True))
        tr = self.index.get_timeline_resource(index_entry['timeline_uuid'])
        timeline_path = get_required_bg3_attribute(tr, 'SourceFile')
        pak_name = self.__index.get_pak_by_file(timeline_path)
        return timeline_object(self.__files.get_file(pak_name, timeline_path, exclude_from_build = True), d)


    def get_scene_object(self, dialog_name: str) -> scene_object:
        index_entry = self.__index.get_entry(dialog_name)
        tr = self.index.get_timeline_resource(index_entry['timeline_uuid'])
        timeline_path = get_required_bg3_attribute(tr, 'SourceFile')
        pak_name = self.__index.get_pak_by_file(timeline_path)
        scene_lsf_path = timeline_path[:-4] + '_Scene.lsf'
        scene_lsf = self.__files.get_file(pak_name, scene_lsf_path, exclude_from_build = True)
        scene_lsx_path = timeline_path[:-4] + '_Scene.lsx'
        scene_lsx = self.__files.get_file(pak_name, scene_lsx_path, exclude_from_build = True)
        return scene_object(scene_lsf, scene_lsx)


    def copy_dialog_to_mod(self, dialog_name: str, new_dialog_uuid: str | None = None, new_timeline_uuid: str | None = None) -> dialog_asset_bundle:
        dialog_name = dialog_name.lower()
        if dialog_name in self.__asset_bundles:
            raise RuntimeError(f'Dialog {dialog_name} is already present in modded assets')

        index_entry = self.__index.get_entry(dialog_name)
        original_dialog_uuid = index_entry['dialog_uuid']
        original_timeline_uuid = index_entry['timeline_uuid']
        source_dialog_path = index_entry['lsf_path']

        has_timeline = len(original_timeline_uuid) > 0

        if new_dialog_uuid is None:
            new_dialog_uuid = original_dialog_uuid
        if has_timeline and new_timeline_uuid is None:
            new_timeline_uuid = original_timeline_uuid

        pos = source_dialog_path.rfind('/')
        if pos == -1 or not source_dialog_path.endswith('.lsf'):
            raise RuntimeError(f'Incorrect dialog path: {source_dialog_path}')
        dialog_file_name = source_dialog_path[pos + 1: -4]

        source_mod_name = source_dialog_path.split('/')[1]
        new_file_name = f'{self.__files.mod_name}_{dialog_file_name}'
        new_file_name_scene = new_file_name + '_Scene'
        dialog_file = self.__files.get_file(
            self.__index.get_pak_by_file(source_dialog_path), source_dialog_path, mod_specific = True, rename_to = new_file_name)
        source_timeline_path = f'Public/{source_mod_name}/Timeline/Generated/{dialog_file_name}.lsf'

        if has_timeline:
            timeline_file = self.__files.get_file(
                self.__index.get_pak_by_file(source_timeline_path), source_timeline_path, mod_specific = True, rename_to = new_file_name)
            if new_timeline_uuid != original_timeline_uuid:
                self.update_timeline_actor(timeline_file, new_timeline_uuid)
            source_scene_lsf_path = f'Public/{source_mod_name}/Timeline/Generated/{dialog_file_name}_Scene.lsf'
            scene_lsf_file = self.__files.get_file(
                self.__index.get_pak_by_file(source_scene_lsf_path), source_scene_lsf_path, mod_specific = True, rename_to = new_file_name_scene)
            source_scene_lsx_path = f'Public/{source_mod_name}/Timeline/Generated/{dialog_file_name}_Scene.lsx'
            scene_lsx_file = self.__files.get_file(
                self.__index.get_pak_by_file(source_scene_lsx_path), source_scene_lsx_path, mod_specific = True, rename_to = new_file_name_scene)
        else:
            timeline_file = self.__files.empty_game_file
            scene_lsf_file = self.__files.empty_game_file
            scene_lsx_file = self.__files.empty_game_file

        internal_dialog_uuid = new_random_uuid()
        internal_scene_uuid = new_random_uuid()
    
        dialog_node = dialog_file.root_node.find('./region[@id="dialog"]/node[@id="dialog"]')
        if dialog_node is None:
            raise RuntimeError(f'Failed to find a dialog node in {dialog_file.relative_file_path}')
        set_bg3_attribute(dialog_node, 'UUID', internal_dialog_uuid, attribute_type = 'FixedString')

        if has_timeline:
            if original_timeline_uuid != get_required_bg3_attribute(dialog_node, 'TimelineId'):
                raise RuntimeError(f'Corrupted dialog {original_dialog_uuid}, found references to 2 timelines')
            set_bg3_attribute(dialog_node, 'TimelineId', new_timeline_uuid, attribute_type = 'FixedString')

            scene_lsf_node = scene_lsf_file.root_node.find('./region[@id="TLScene"]/node[@id="TLScene"]')
            if scene_lsf_node is None:
                raise RuntimeError(f'Failed to find a TLScene node in {scene_lsf_file.relative_file_path}')
            set_bg3_attribute(scene_lsf_node, 'Identifier', internal_scene_uuid, attribute_type = 'guid')

            scene_lsx_node = scene_lsx_file.root_node.find('./region[@id="TLScene"]/node[@id="root"]')
            if scene_lsx_node is None:
                raise RuntimeError(f'Failed to find a root node in {scene_lsx_file.relative_file_path}')
            set_bg3_attribute(scene_lsx_node, 'Identifier', internal_scene_uuid, attribute_type = 'guid')

        dialog_resource = self.load_dialog_resource(index_entry['dialog_bank_pak'], index_entry['dialog_bank_path'], original_dialog_uuid)
        lsf_path = dialog_file.get_output_relative_path(self.__files.mod_name_uuid)
        lsj_path = lsf_path.replace('/Story/DialogsBinary/', '/Story/Dialogs/')[:-4] + '.lsj'
        dialog_version = int(get_required_bg3_attribute(dialog_resource, '_OriginalFileVersion_')) + 2147483648 + 1
        set_bg3_attribute(dialog_resource, 'ID', new_dialog_uuid, attribute_type = 'FixedString')
        set_bg3_attribute(dialog_resource, 'SourceFile', lsj_path, attribute_type = 'LSString')
        set_bg3_attribute(dialog_resource, 'Name', new_file_name, attribute_type = 'LSString')
        set_bg3_attribute(dialog_resource, '_OriginalFileVersion_', str(dialog_version), attribute_type = 'int64')

        if has_timeline:
            timeline_resource = self.__index.get_timeline_resource(original_timeline_uuid)
            timeline_file_path = timeline_file.get_output_relative_path(self.__files.mod_name_uuid)
            timeline_version = int(get_required_bg3_attribute(timeline_resource, '_OriginalFileVersion_')) + 2147483648 + 1
            set_bg3_attribute(timeline_resource, 'DialogResourceId', new_dialog_uuid, attribute_type = 'guid')
            set_bg3_attribute(timeline_resource, 'ID', new_timeline_uuid, attribute_type = 'FixedString')
            set_bg3_attribute(timeline_resource, 'Name', new_file_name, attribute_type = 'LSString')
            set_bg3_attribute(timeline_resource, 'SourceFile', timeline_file_path, attribute_type = 'LSString')
            set_bg3_attribute(timeline_resource, '_OriginalFileVersion_', str(timeline_version), attribute_type = 'int64')

            # update timeline dependency list
            # replace UUID of the original dialog with the new dialog UUID
            dependencies = timeline_resource.findall('./children/node[@id="DependencyCache"]')
            for dependency in dependencies:
                dependency_uuid = get_required_bg3_attribute(dependency, 'Object')
                if dependency_uuid == original_dialog_uuid:
                    set_bg3_attribute(dependency, 'Object', new_dialog_uuid, attribute_type = 'guid')
                    break

        ab = dialog_asset_bundle(original_dialog_uuid, new_dialog_uuid, original_timeline_uuid, new_timeline_uuid, dialog_file, timeline_file, scene_lsf_file, scene_lsx_file)
        self.__asset_bundles[dialog_name] = ab
        self.__get_dialog_bank_parent_node().append(dialog_resource)

        if has_timeline:
            self.__get_timeline_bank_parent_node().append(timeline_resource)

        return ab


    def update_timeline_actor(self, timeline_file: game_file, new_timeline_uuid: str) -> None:
        timeline_actors = timeline_file.xml.getroot().findall('./region[@id="TimelineContent"]/node[@id="TimelineContent"]/children/node[@id="TimelineActorData"]/children/node[@id="TimelineActorData"]/children/node[@id="Object"]')
        for timeline_actor in timeline_actors:
            value = timeline_actor.find('./children/node[@id="Value"]')
            if value:
                actor_type_id = get_bg3_attribute(value, 'ActorTypeId')
                if actor_type_id == 'timeline':
                    set_bg3_attribute(timeline_actor, 'MapKey', new_timeline_uuid)
                    return


    def prepare_assets(self, assets: dict[str, dict[str, str]], /, verbose: bool = False) -> None:
        count = len(assets)
        n = 1
        for dialog_name in assets:
            if verbose:
                sys.stdout.write(f'\nPreparing asset ({n}/{count}): {dialog_name}')
            asset = assets[dialog_name]
            dialog_uuid = asset['dialog_uuid'] if 'dialog_uuid' in asset else None
            timeline_uuid = asset['timeline_uuid'] if 'timeline_uuid' in asset else None
            self.copy_dialog_to_mod(dialog_name, dialog_uuid, timeline_uuid)
            if verbose:
                sys.stdout.write(' done')
                n += 1


    def load_dialog_resource(self, pak_name: str, dialog_bank_path: str, dialog_uuid: str) -> et.Element[str]:
        dialog_bank = self.__files.get_file(pak_name, dialog_bank_path, exclude_from_build = True)
        resources = dialog_bank.root_node.findall('./region[@id="DialogBank"]/node[@id="DialogBank"]/children/node[@id="Resource"]')
        for resource in resources:
            if get_required_bg3_attribute(resource, 'ID') == dialog_uuid:
                return resource
        raise RuntimeError(f'Cannot find dialog resource {dialog_uuid} in {pak_name} {dialog_bank_path}')


    def post_process_assets(self) -> None:
        for ab in self.__asset_bundles.values():
            d = dialog_object(ab.dialog)
            if not ab.timeline.is_empty:
                timeline_object(ab.timeline, d).post_process()


    # asset_id could be dialog UUID, or asset name
    def get_dialog_resource(self, asset_id: str) -> et.Element[str]:
        resources = self.__get_dialog_bank_parent_node().findall('./node[@id="Resource"]')
        asset_id = asset_id.lower()
        for resource in resources:
            identifier = get_bg3_attribute(resource, 'Name')
            if identifier is not None and identifier.lower() == asset_id:
                return resource
            identifier = get_bg3_attribute(resource, 'ID')
            if identifier is not None and identifier.lower() == asset_id:
                return resource
        raise RuntimeError(f'Cannot find dialog resource with id {asset_id}')


    # asset_id could be timeline UUID, dialog UUID, or asset name
    def get_timeline_resource(self, asset_id: str) -> et.Element[str]:
        resources = self.__get_timeline_bank_parent_node().findall('./node[@id="Resource"]')
        asset_id = asset_id.lower()
        for resource in resources:
            identifier = get_bg3_attribute(resource, 'Name')
            if identifier is not None and identifier.lower() == asset_id:
                return resource
            identifier = get_bg3_attribute(resource, 'ID')
            if identifier is not None and identifier.lower() == asset_id:
                return resource
            identifier = get_bg3_attribute(resource, 'DialogResourceId')
            if identifier is not None and identifier.lower() == asset_id:
                return resource
        raise RuntimeError(f'Cannot find timeline resource with id {asset_id}')


    def append_dependency_to_timeline(self, asset_id: str, dependency_uuid: str) -> None:
        resource = self.get_timeline_resource(asset_id)
        children = resource.find('./children')
        if children is None:
            children = et.fromstring('<children></children>')
            resource.append(children)
        children.append(et.fromstring(f'<node id="DependencyCache"><attribute id="Object" type="guid" value="{dependency_uuid}" /></node>'))
        return


    def copy_timeline_dependencies(self, source_id: str, destination_id: str) -> None:
        resource = self.get_timeline_resource(destination_id)
        deps = resource.findall('./children/node[@id="DependencyCache"]')
        dest_deps = set[str]()
        for dep in deps:
            dep_uuid = get_required_bg3_attribute(dep, 'Object')
            dest_deps.add(dep_uuid)

        dest_deps_node = resource.find('./children')
        if dest_deps_node is None:
            dest_deps_node = et.fromstring('<children></children>')
            resource.append(dest_deps_node)

        resource = self.get_timeline_resource(source_id)
        deps = resource.findall('./children/node[@id="DependencyCache"]')
        src_dialog_uuid = get_required_bg3_attribute(resource, 'DialogResourceId')
        for dep in deps:
            dep_uuid = get_required_bg3_attribute(dep, 'Object')
            if dep_uuid != src_dialog_uuid and dep_uuid not in dest_deps:
                dest_deps_node.append(et.fromstring(f'<node id="DependencyCache"><attribute id="Object" type="guid" value="{dep_uuid}" /></node>'))


    def create_new_empty_dialog_from_another(
            self,
            source_dialog_name: str,
            new_dialog_name: str,
            new_dialog_uuid: str,
            new_timeline_uuid: str
    ) -> dialog_asset_bundle:
        source_dialog_name = source_dialog_name.lower()

        index_entry = self.__index.get_entry(source_dialog_name)
        source_dialog_path = index_entry['lsf_path']
        original_dialog_uuid = index_entry['dialog_uuid']
        original_timeline_uuid = index_entry['timeline_uuid']

        pos = source_dialog_path.rfind('/')
        if pos == -1 or not source_dialog_path.endswith('.lsf'):
            raise RuntimeError(f'Incorrect dialog path: {source_dialog_path}')
        dialog_file_name = source_dialog_path[pos + 1: -4]

        source_mod_name = source_dialog_path.split('/')[1]
        new_file_name = f'{self.__files.mod_name}_{new_dialog_name}'
        new_file_name_scene = new_file_name + '_Scene'
        dialog_file = self.__files.get_file(
            self.__index.get_pak_by_file(source_dialog_path), source_dialog_path, mod_specific = True, rename_to = new_file_name)
        source_timeline_path = f'Public/{source_mod_name}/Timeline/Generated/{dialog_file_name}.lsf'
        timeline_file = self.__files.get_file(
            self.__index.get_pak_by_file(source_timeline_path), source_timeline_path, mod_specific = True, rename_to = new_file_name)
        source_scene_lsf_path = f'Public/{source_mod_name}/Timeline/Generated/{dialog_file_name}_Scene.lsf'
        scene_lsf_file = self.__files.get_file(
            self.__index.get_pak_by_file(source_scene_lsf_path), source_scene_lsf_path, mod_specific = True, rename_to = new_file_name_scene)
        source_scene_lsx_path = f'Public/{source_mod_name}/Timeline/Generated/{dialog_file_name}_Scene.lsx'
        scene_lsx_file = self.__files.get_file(
            self.__index.get_pak_by_file(source_scene_lsx_path), source_scene_lsx_path, mod_specific = True, rename_to = new_file_name_scene)

        internal_dialog_uuid = new_random_uuid()
        internal_scene_uuid = new_random_uuid()

        dialog_node = dialog_file.root_node.find('./region[@id="dialog"]/node[@id="dialog"]')
        if dialog_node is None:
            raise RuntimeError(f'Failed to find a dialog node in {dialog_file.relative_file_path}')
        set_bg3_attribute(dialog_node, 'UUID', internal_dialog_uuid, attribute_type = 'FixedString')
        set_bg3_attribute(dialog_node, 'TimelineId', new_timeline_uuid, attribute_type = 'FixedString')

        # remove all existing nodes from the dialog
        nodes = dialog_node.find('./children/node[@id="nodes"]')
        if nodes is None:
            raise RuntimeError(f'Failed to parse a dialog from {dialog_file.relative_file_path}')
        remove_all_nodes(nodes)

        # remove all existing phases, timeline phases, and effects from the timeline
        phases = timeline_file.root_node.find('./region[@id="TimelineContent"]/node[@id="TimelineContent"]/children/node[@id="Effect"]/children/node[@id="Phases"]')
        if phases is None:
            raise RuntimeError(f'Failed to parse a dialog from {timeline_file.relative_file_path}')
        remove_all_nodes(phases)

        effect_components = timeline_file.root_node.find('./region[@id="TimelineContent"]/node[@id="TimelineContent"]/children/node[@id="Effect"]/children/node[@id="EffectComponents"]')
        if effect_components is None:
            raise RuntimeError(f'Failed to parse a dialog from {timeline_file.relative_file_path}')
        remove_all_nodes(effect_components)

        timeline_phases = timeline_file.root_node.find('./region[@id="TimelineContent"]/node[@id="TimelineContent"]/children/node[@id="TimelinePhases"]')
        if timeline_phases is None:
            raise RuntimeError(f'Failed to parse a dialog from {timeline_file.relative_file_path}')
        remove_all_nodes(timeline_phases)

        scene_lsf_node = scene_lsf_file.root_node.find('./region[@id="TLScene"]/node[@id="TLScene"]')
        if scene_lsf_node is None:
            raise RuntimeError(f'Failed to find a TLScene node in {scene_lsf_file.relative_file_path}')
        set_bg3_attribute(scene_lsf_node, 'Identifier', internal_scene_uuid, attribute_type = 'guid')

        scene_lsx_node = scene_lsx_file.root_node.find('./region[@id="TLScene"]/node[@id="root"]')
        if scene_lsx_node is None:
            raise RuntimeError(f'Failed to find a root node in {scene_lsx_file.relative_file_path}')
        set_bg3_attribute(scene_lsx_node, 'Identifier', internal_scene_uuid, attribute_type = 'guid')

        dialog_resource = self.load_dialog_resource(index_entry['dialog_bank_pak'], index_entry['dialog_bank_path'], original_dialog_uuid)
        lsf_path = dialog_file.get_output_relative_path(self.__files.mod_name_uuid)
        lsj_path = lsf_path.replace('/Story/DialogsBinary/', '/Story/Dialogs/')[:-4] + '.lsj'
        dialog_version = int(get_required_bg3_attribute(dialog_resource, '_OriginalFileVersion_')) + 2147483648 + 1
        set_bg3_attribute(dialog_resource, 'ID', new_dialog_uuid, attribute_type = 'FixedString')
        set_bg3_attribute(dialog_resource, 'SourceFile', lsj_path, attribute_type = 'LSString')
        set_bg3_attribute(dialog_resource, 'Name', new_file_name, attribute_type = 'LSString')
        set_bg3_attribute(dialog_resource, '_OriginalFileVersion_', str(dialog_version), attribute_type = 'int64')

        timeline_resource = self.__index.get_timeline_resource(original_timeline_uuid)
        timeline_file_path = timeline_file.get_output_relative_path(self.__files.mod_name_uuid)
        timeline_version = int(get_required_bg3_attribute(timeline_resource, '_OriginalFileVersion_')) + 2147483648 + 1
        set_bg3_attribute(timeline_resource, 'DialogResourceId', new_dialog_uuid, attribute_type = 'guid')
        set_bg3_attribute(timeline_resource, 'ID', new_timeline_uuid, attribute_type = 'FixedString')
        set_bg3_attribute(timeline_resource, 'Name', new_file_name, attribute_type = 'LSString')
        set_bg3_attribute(timeline_resource, 'SourceFile', timeline_file_path, attribute_type = 'LSString')
        set_bg3_attribute(timeline_resource, '_OriginalFileVersion_', str(timeline_version), attribute_type = 'int64')

        dependencies = timeline_resource.findall('./children/node[@id="DependencyCache"]')
        for dependency in dependencies:
            dependency_uuid = get_required_bg3_attribute(dependency, 'Object')
            if dependency_uuid == original_dialog_uuid:
                set_bg3_attribute(dependency, 'Object', new_dialog_uuid, attribute_type = 'guid')
                break

        ab = dialog_asset_bundle(
            new_dialog_uuid,
            new_dialog_uuid,
            new_timeline_uuid,
            new_timeline_uuid,
            dialog_file,
            timeline_file,
            scene_lsf_file,
            scene_lsx_file)
        self.__asset_bundles[new_dialog_name.lower()] = ab
        self.__get_dialog_bank_parent_node().append(dialog_resource)
        self.__get_timeline_bank_parent_node().append(timeline_resource)

        return ab


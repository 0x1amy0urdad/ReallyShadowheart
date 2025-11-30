from __future__ import annotations

import os
import os.path
import xml.etree.ElementTree as et

from ._common import (
    get_bg3_attribute,
    get_required_bg3_attribute,
)
from ._assets import bg3_assets, dialog_index
from ._dialog import dialog_object
from ._files import game_file
from ._timeline import timeline_object, timeline_phase
from ._tool import bg3_modding_tool
from ._types import XmlElement

from dataclasses import dataclass


class dialog_timeline_phase:
    __tl_phase: timeline_phase | None
    __dialog_nodes: dict[str, XmlElement]
    __timeline_nodes: dict[str, XmlElement]

    def __init__(self, tl_phase: timeline_phase | None, dialog_nodes: list[XmlElement], timeline_nodes: list[XmlElement]) -> None:
        self.__tl_phase = tl_phase
        self.__dialog_nodes = { get_required_bg3_attribute(node, 'UUID') : node for node in dialog_nodes }
        self.__timeline_nodes = { get_required_bg3_attribute(node, 'ID') : node for node in timeline_nodes }

    @property
    def tl_phase(self) -> timeline_phase | None:
        return self.__tl_phase

    @property
    def dialog_nodes(self) -> dict[str, XmlElement]:
        return self.__dialog_nodes

    @property
    def timeline_nodes(self) -> dict[str, XmlElement]:
        return self.__timeline_nodes


class dialog_timeline_nodes:
    __phases: dict[str, dialog_timeline_phase]

    def __init__(self, d: dialog_object, t: timeline_object) -> None:
        dialog_to_phase_index = dict[str, int]()
        timeline_phases = t.xml.findall('./region[@id="TimelineContent"]/node[@id="TimelineContent"]/children/node[@id="TimelinePhases"]/children/node[@id="Object"]/children/node[@id="Object"]')
        for timeline_phase in timeline_phases:
            dialog_uuid = get_required_bg3_attribute(timeline_phase, 'MapKey')
            phase_index = get_required_bg3_attribute(timeline_phase, 'MapValue')
            dialog_to_phase_index[dialog_uuid] = int(phase_index)

        plain_dialog_nodes = list[XmlElement]()
        dialog_nodes_by_phase_idx = dict[int, list[XmlElement]]()
        for dialog_node in d.get_dialog_nodes():
            dialog_uuid = get_required_bg3_attribute(dialog_node, 'UUID')
            if dialog_uuid in dialog_to_phase_index:
                phase_idx = dialog_to_phase_index[dialog_uuid]
                if phase_idx in dialog_nodes_by_phase_idx:
                    dialog_nodes_by_phase_idx[phase_idx].append(dialog_node)
                else:
                    dialog_nodes_by_phase_idx[phase_idx] = [dialog_node]
            else:
                plain_dialog_nodes.append(dialog_node)
        
        timeline_nodes_by_phase_idx = dict[int, list[XmlElement]]()
        for timeline_node in t.all_effect_components:
            idx = get_bg3_attribute(timeline_node, 'PhaseIndex')
            if idx is None:
                phase_index = 0
            else:
                phase_index = int(idx)
            if phase_index in timeline_nodes_by_phase_idx:
                timeline_nodes_by_phase_idx[phase_index].append(timeline_node)
            else:
                timeline_nodes_by_phase_idx[phase_index] = [timeline_node]

        indexes = list[int](dialog_nodes_by_phase_idx.keys())
        indexes.sort()
        self.__phases = dict[str, dialog_timeline_phase]()
        for idx in indexes:
            tl_phase = t.get_timeline_phase(idx)
            dtp = dialog_timeline_phase(tl_phase, dialog_nodes_by_phase_idx[idx], timeline_nodes_by_phase_idx[idx])
            for dialog_node in dialog_nodes_by_phase_idx[idx]:
                dialog_uuid = get_required_bg3_attribute(dialog_node, 'UUID')
                self.__phases[dialog_uuid] = dtp

        for plain_dialog_node in plain_dialog_nodes:
            dialog_uuid = get_required_bg3_attribute(plain_dialog_node, 'UUID')
            dtp = dialog_timeline_phase(None, [plain_dialog_node], [])
            self.__phases[dialog_uuid] = dtp

    def get_dialog_timeline_phase(self, dialog_uuid: str) -> dialog_timeline_phase:
        if dialog_uuid not in self.__phases:
            raise RuntimeError(f"Dialog not found: {dialog_uuid}")
        return self.__phases[dialog_uuid]


@dataclass
class content_bundle:
    content: pak_content
    dialog_uuid: str = ""
    timeline_uuid: str = ""
    dialog_file: str = ""
    timeline_file: str = ""
    scene_lsf_file: str = ""
    scene_lsx_file: str = ""


class pak_content:
    __assets: bg3_assets
    __index: dialog_index
    __tool: bg3_modding_tool
    __file_path: str
    __pak_files: tuple[str, ...]
    __content_bundles: dict[str, content_bundle]
    __dialog_bank: dict[str, XmlElement]
    __timeline_bank: dict[str, XmlElement]

    def __init__(self, a: bg3_assets, file_path: str) -> None:
        self.__assets = a
        self.__index = a.index
        self.__tool = a.files.tool
        self.__file_path = file_path
        self.__pak_files = ()
        self.__content_bundles = dict[str, content_bundle]()
        self.__dialog_bank = dict[str, XmlElement]()
        self.__timeline_bank = dict[str, XmlElement]()
        self.initialize()


    def initialize(self) -> None:
        self.__pak_files = tuple(self.__tool.list(self.__file_path))
        cb : content_bundle
        content_bundles = dict[str, content_bundle]()
        for file_path in self.__pak_files:
            if file_path.startswith('Public/'):
                if '/Content/' in file_path and file_path.endswith('.lsf'):
                    if '/Generated/' in file_path:
                        self.__read_timeline_bank_lsf(file_path)
                    else:
                        self.__read_dialog_bank_lsf(file_path)
                elif '/Timeline/Generated/' in file_path:
                    if file_path.endswith('_Scene.lsx'):
                        filename = os.path.basename(file_path)[:-10].lower()
                        if filename not in content_bundles:
                            cb = content_bundle(self)
                            content_bundles[filename] = cb
                        else:
                            cb = content_bundles[filename]
                        cb.scene_lsx_file = file_path
                    elif file_path.endswith('_Scene.lsf'):
                        filename = os.path.basename(file_path)[:-10].lower()
                        if filename not in content_bundles:
                            cb = content_bundle(self)
                            content_bundles[filename] = cb
                        else:
                            cb = content_bundles[filename]
                        cb.scene_lsf_file = file_path
                    elif file_path.endswith('.lsf'):
                        filename = os.path.basename(file_path)[:-4].lower()
                        if filename not in content_bundles:
                            cb = content_bundle(self)
                            content_bundles[filename] = cb
                        else:
                            cb = content_bundles[filename]
                        cb.timeline_file = file_path
            elif file_path.startswith('Mods/') and '/Story/DialogsBinary/' in file_path and file_path.endswith('.lsf'):
                filename = os.path.basename(file_path)[:-4].lower()
                if filename not in content_bundles:
                    cb = content_bundle(self)
                    content_bundles[filename] = cb
                else:
                    cb = content_bundles[filename]
                cb.dialog_file = file_path
        for fn, cb in content_bundles.items():
            if fn in self.__dialog_bank:
                dialog_res = self.__dialog_bank[fn]
                cb.dialog_uuid = get_required_bg3_attribute(dialog_res, 'ID')
            elif self.__index.has_entry(fn):
                entry = self.__index.get_entry(fn)
                cb.dialog_uuid = entry['dialog_uuid']
            if fn in self.__timeline_bank:
                timeline_res = self.__timeline_bank[fn]
                cb.timeline_uuid = get_required_bg3_attribute(timeline_res, 'ID')
            elif self.__index.has_entry(fn):
                # there could be a renamed dialog in the dialog bank that doesn't have a timeline
                entry = self.__index.get_entry(fn)
                cb.timeline_uuid = entry['timeline_uuid']
        self.__content_bundles = dict[str, content_bundle]()
        for fn, cb in content_bundles.items():
            self.__content_bundles[cb.dialog_uuid] = cb

    @property
    def tool(self) -> bg3_modding_tool:
        return self.__tool

    @property
    def file_path(self) -> str:
        return self.__file_path

    @property
    def files(self) -> tuple[str, ...]:
        return self.__pak_files

    @property
    def content_index(self) -> tuple[str, ...]:
        return tuple(self.__content_bundles.keys())

    def get_content_bundle(self, dialog_uuid: str) -> content_bundle:
        dialog_uuid = dialog_uuid.lower()
        if dialog_uuid in self.__content_bundles:
            return self.__content_bundles[dialog_uuid]
        raise KeyError(f'content_bundle not found for dialog uuid: {dialog_uuid}')

    def get_dialog_resource(self, dialog_id: str) -> XmlElement:
        dialog_id = dialog_id.lower()
        if dialog_id in self.__dialog_bank:
            return self.__dialog_bank[dialog_id]
        raise KeyError(f'dialog not found in the bank: {dialog_id}')

    def get_timeline_resource(self, timeline_id: str) -> XmlElement:
        timeline_id = timeline_id.lower()
        if timeline_id in self.__timeline_bank:
            return self.__timeline_bank[timeline_id]
        raise KeyError(f'dialog not found in the bank: {timeline_id}')

    def get_dialog_object(self, dialog_uuid: str) -> dialog_object:
        cb = self.get_content_bundle(dialog_uuid)
        if cb.dialog_file:
            gf = self.__assets.files.get_file(self.__file_path, cb.dialog_file, exclude_from_build = True)
        else:
            dialog_name = self.__assets.index.get_dialog_name(dialog_uuid)
            e = self.__assets.index.get_entry(dialog_name)
            ori_dialog_lsf_path = e['lsf_path']
            ori_pak = self.__assets.index.get_pak_by_file(ori_dialog_lsf_path)
            gf = self.__assets.files.get_file(ori_pak, ori_dialog_lsf_path, exclude_from_build = True)
        return dialog_object(gf)

    def get_timeline_object(self, dialog_uuid: str) -> timeline_object:
        cb = self.get_content_bundle(dialog_uuid)
        if cb.timeline_file:
            gf = self.__assets.files.get_file(self.__file_path, cb.timeline_file, exclude_from_build = True)
        else:
            dialog_name = self.__assets.index.get_dialog_name(dialog_uuid)
            e = self.__assets.index.get_entry(dialog_name)
            timeline_uuid = e['timeline_uuid']
            ori_timeline_lsf_path = self.__assets.index.get_timeline_file_path(timeline_uuid)
            ori_pak = self.__assets.index.get_pak_by_file(ori_timeline_lsf_path)
            gf = self.__assets.files.get_file(ori_pak, ori_timeline_lsf_path, exclude_from_build = True)
        return timeline_object(gf, self.get_dialog_object(dialog_uuid))

    def __read_dialog_bank_lsf(self, lsf_path: str) -> None:
        gf = game_file(self.__tool, lsf_path, pak_name = self.__file_path)
        resources = gf.xml.getroot().findall('./region[@id="DialogBank"]/node[@id="DialogBank"]/children/node[@id="Resource"]')
        for resource in resources:
            dialog_file_uuid = get_required_bg3_attribute(resource, 'ID').lower()
            self.__dialog_bank[dialog_file_uuid] = resource
            source_file = get_required_bg3_attribute(resource, 'SourceFile')
            filename = os.path.basename(source_file)[:-4]
            self.__dialog_bank[filename.lower()] = resource
        
    def __read_timeline_bank_lsf(self, lsf_path: str) -> None:
        gf = game_file(self.__tool, lsf_path, pak_name = self.__file_path)
        resources = gf.xml.getroot().findall('./region[@id="TimelineBank"]/node[@id="TimelineBank"]/children/node[@id="Resource"]')
        for resource in resources:
            timeline_file_uuid = get_required_bg3_attribute(resource, 'ID').lower()
            self.__timeline_bank[timeline_file_uuid] = resource
            source_file = get_required_bg3_attribute(resource, 'SourceFile')
            filename = os.path.basename(source_file)[:-4]
            self.__timeline_bank[filename.lower()] = resource



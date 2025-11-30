from __future__ import annotations

import xml.etree.ElementTree as et

from ._assets import bg3_assets, dialog_index
from ._common import attrs_to_str, delete_bg3_attribute, get_bg3_attribute, get_required_bg3_attribute, decimal_from_str, DECIMAL_ZERO, set_bg3_attribute
from ._timeline import timeline_object

from ._types import XmlElement

from dataclasses import dataclass, field

import os.path
import decimal as dc


@dataclass
class normalized_tl_phase:
    phase_start: dc.Decimal = DECIMAL_ZERO
    phase_duration: dc.Decimal = DECIMAL_ZERO
    phase_index: int = 0
    effects: list[XmlElement] = field(default_factory = list)
    effects_by_uuid: dict[str, int] = field(default_factory = dict)

    def add_node(self, node: XmlElement) -> None:
        n = len(self.effects)
        self.effects.append(node)
        effect_uuid = get_required_bg3_attribute(node, 'ID')
        self.effects_by_uuid[effect_uuid] = n


@dataclass
class normalized_tl_phases:
    phases_by_dialog: dict[str, normalized_tl_phase] = field(default_factory = dict)
    phases: list[normalized_tl_phase] = field(default_factory = list)


class timeline_differ:
    __assets: bg3_assets
    __index: dialog_index

    def __init__(self, a: bg3_assets) -> None:
        self.__assets = a
        self.__index = a.index


    @property
    def assets(self) -> bg3_assets:
        return self.__assets


    @property
    def index(self) -> dialog_index:
        return self.__index


    def get_modified_timeline_nodes(self, modded_timeline: timeline_object, dialog_name: str | None = None) -> dict[str, str]:
        result = dict[str, str]()
        if dialog_name is None:
            dialog_name, _ = os.path.splitext(os.path.basename(modded_timeline.filename))
        original_timeline = self.__assets.get_timeline_object(dialog_name.lower())

        modded_phases = timeline_differ.convert_to_phases(modded_timeline)
        original_phases = timeline_differ.convert_to_phases(original_timeline)

        modded_phases_uuids = set(modded_phases.phases_by_dialog.keys())
        original_phases_uuids = set(original_phases.phases_by_dialog.keys())
        common_uuids = original_phases_uuids.intersection(modded_phases_uuids)
        only_in_modded_uuids = modded_phases_uuids.difference(original_phases_uuids)
        only_in_original_uuids = original_phases_uuids.difference(modded_phases_uuids)
        for dialog_uuid in only_in_original_uuids:
            phase = original_phases.phases_by_dialog[dialog_uuid]
            for effect_uuid in phase.effects_by_uuid.keys():
                result[effect_uuid] = f'removed|{dialog_uuid}'
        for dialog_uuid in only_in_modded_uuids:
            phase = modded_phases.phases_by_dialog[dialog_uuid]
            for effect_uuid in phase.effects_by_uuid.keys():
                result[effect_uuid] = f'added|{dialog_uuid}'
        for dialog_uuid in common_uuids:
            modded_phase = modded_phases.phases_by_dialog[dialog_uuid]
            original_phase = original_phases.phases_by_dialog[dialog_uuid]
            modded_phase_uuids = set(modded_phase.effects_by_uuid.keys())
            original_phase_uuids = set(original_phase.effects_by_uuid.keys())
            common_uuids = original_phase_uuids.intersection(modded_phase_uuids)
            only_in_modded_uuids = modded_phase_uuids.difference(original_phase_uuids)
            only_in_original_uuids = original_phase_uuids.difference(modded_phase_uuids)
            for effect_uuid in only_in_original_uuids:
                result[effect_uuid] = f'removed|{dialog_uuid}'
            for effect_uuid in only_in_modded_uuids:
                result[effect_uuid] = f'added|{dialog_uuid}'
            for effect_uuid in common_uuids:
                modded_effect = modded_phase.effects[modded_phase.effects_by_uuid[effect_uuid]]
                original_effect = original_phase.effects[original_phase.effects_by_uuid[effect_uuid]]
                if not timeline_differ.compare_timeline_nodes(original_effect, modded_effect):
                    result[effect_uuid] = f'modified|{dialog_uuid}'
        return result


    @staticmethod
    def convert_to_phases(t: timeline_object) -> normalized_tl_phases:
        result = normalized_tl_phases()
        effect_node = t.xml.find('./region[@id="TimelineContent"]/node[@id="TimelineContent"]/children/node[@id="Effect"]')
        if effect_node is None:
            raise RuntimeError('bad timeline format, "Effect" node is not found')
        timeline_phases = t.xml.findall('./region[@id="TimelineContent"]/node[@id="TimelineContent"]/children/node[@id="TimelinePhases"]/children/node[@id="Object"]/children/node[@id="Object"]')
        if len(timeline_phases) == 0:
            raise RuntimeError('bad timeline format, "TimelinePhases" node is not found')
        phases = effect_node.findall('./children/node[@id="Phases"]/children/node[@id="Phase"]')
        if len(phases) == 0:
            raise RuntimeError('bad timeline format, "Phases" node is not found')
        effect_comps = effect_node.findall('./children/node[@id="EffectComponents"]/children/node[@id="EffectComponent"]')
        if len(effect_comps) == 0:
            raise RuntimeError('bad timeline format, "EffectComponents" node is not found')
        for phase in phases:
            duration = get_required_bg3_attribute(phase, 'Duration')
            dialog_uuid = get_required_bg3_attribute(phase, 'DialogNodeId')
            ntp = normalized_tl_phase(phase_duration = decimal_from_str(duration), phase_index = len(result.phases))
            result.phases.append(ntp)
            result.phases_by_dialog[dialog_uuid] = ntp
        for effect_comp in effect_comps:
            phase_index = get_bg3_attribute(effect_comp, 'PhaseIndex')
            if phase_index is None:
                phase_index = 0
            else:
                phase_index = int(phase_index)
            start_time, _ = timeline_differ.get_start_end_times(effect_comp)
            ntp = result.phases[phase_index]
            if ntp.phase_start > start_time:
                ntp.phase_start = start_time            
            node_uuid = get_required_bg3_attribute(effect_comp, 'ID')
            ntp.effects_by_uuid[node_uuid] = len(ntp.effects)
            ntp.effects.append(effect_comp)

        for ntp in result.phases:
            for tl_node in ntp.effects:
                start_time, end_time = timeline_differ.get_start_end_times(tl_node)
                if start_time > DECIMAL_ZERO:
                    delete_bg3_attribute(tl_node, 'StartTime')
                start_time -= ntp.phase_start
                end_time -= ntp.phase_start
                if start_time > DECIMAL_ZERO:
                    set_bg3_attribute(tl_node, 'StartTime', str(start_time))
                set_bg3_attribute(tl_node, 'EndTime', str(end_time))
                keys = timeline_differ.find_keys(tl_node)
                for key in keys:
                    time_attr = get_bg3_attribute(key, 'Time')
                    if time_attr is not None:
                        time_val = decimal_from_str(time_attr)
                        time_val -= ntp.phase_start
                        set_bg3_attribute(key, 'Time', str(time_val))

        return result


    @staticmethod
    def compare_timeline_nodes(a: XmlElement, b: XmlElement) -> bool:
        return timeline_differ.tl_node_to_str(a) == timeline_differ.tl_node_to_str(b)


    @staticmethod
    def tl_node_to_str(node: XmlElement) -> str:
        result = [attrs_to_str(node)]
        for key in timeline_differ.find_keys(node):
            result.append(attrs_to_str(key))
        return ";".join(result)


    @staticmethod
    def get_start_end_times(node: XmlElement) -> tuple[dc.Decimal, dc.Decimal]:
        start_time = get_bg3_attribute(node, 'StartTime')
        if start_time is None:
            start_time = DECIMAL_ZERO
        else:
            start_time = decimal_from_str(start_time)
        end_time = decimal_from_str(get_required_bg3_attribute(node, 'EndTime'))
        return (start_time, end_time)


    @staticmethod
    def find_keys(node: XmlElement) -> tuple[XmlElement, ...]:
        keys = node.findall('./children/node[@id="Keys"]/children/node[@id="Key"]')
        if len(keys) == 0:
            keys = node.findall('./children/node[@id="TransformChannels"]/children/node[@id="TransformChannel"]/children/node[@id="Keys"]/children/node[@id="Key"]')
            if len(keys) == 0:
                keys = node.findall('./children/node[@id="Channels"]/children/node/children/node[@id="Keys"]/children/node[@id="Key"]')
        return tuple(keys)

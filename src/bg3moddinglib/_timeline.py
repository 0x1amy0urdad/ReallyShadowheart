from __future__ import annotations

import decimal as dc
import xml.etree.ElementTree as et

from ._attitudes import *
from ._common import (
    DECIMAL_ZERO,
    TIMELINE_DECIMAL_PRECISION,
    get_bg3_attribute,
    get_len,
    get_required_bg3_attribute,
    decimal_from,
    decimal_from_str,
    delete_bg3_attribute,
    new_random_uuid,
    set_bg3_attribute,
    to_compact_string
)
from ._constants import (
    PEANUT_SLOT_0,
    PEANUT_SLOT_1,
    PEANUT_SLOT_2,
    PEANUTS,
    SPEAKER_NARRATOR,
    SPEAKER_PLAYER
)
from ._dialog import dialog_object
from ._files import game_file
from ._types import XmlElement

from typing import Iterable

class timeline_phase:
    __index: int
    __dialog_node_uuid: str
    __reference_id: str
    __start: dc.Decimal
    __end: dc.Decimal

    def __init__(self, index: int, dialog_node_uuid: str, reference_id: str, start: str | dc.Decimal, end: str | dc.Decimal) -> None:
        self.__index = index
        self.__dialog_node_uuid = dialog_node_uuid
        self.__reference_id = reference_id
        self.__start = decimal_from_str(start)
        self.__end = decimal_from_str(end)

    @property
    def index(self) -> int:
        return self.__index

    @property
    def dialog_node_uuid(self) -> str:
        return self.__dialog_node_uuid

    @property
    def reference_id(self) -> str:
        return self.__reference_id

    @property
    def start(self) -> dc.Decimal:
        return self.__start

    @property
    def end(self) -> dc.Decimal:
        return self.__end

    @property
    def duration(self) -> dc.Decimal:
        return self.__end - self.__start

class timeline_object:

    ACTOR_CHARACTER = 'character'
    ACTOR_PEANUT = 'peanut'
    ACTOR_NARRATOR = 'narrator'
    ACTOR_CAMERA = 'scenecam'
    ACTOR_LIGHT = 'scenelight'
    ACTOR_EFFECT = 'effect'

    ATTITUDE = 'TLAttitudeEvent'
    EMOTION = 'TLEmotionEvent'
    LOOK_AT = 'TLLookAtEvent'
    SOUND = 'TLSoundEvent'
    SHOW_VISUAL = 'TLShowVisual'
    SHOW_WEAPON = 'TLShowWeapon'
    HANDS_IK = 'TLHandsIK'
    PHYSICS = 'TLPhysics'
    SPRINGS = 'TLSprings'
    PLAY_EFFECT = 'TLPlayEffectEvent'
    PLAY_EFFECT_PHASE = 'TLEffectPhaseEvent'

    VALID_ACTOR_NODES = frozenset([ATTITUDE, EMOTION, LOOK_AT, SOUND, SHOW_VISUAL, SHOW_WEAPON, HANDS_IK, PHYSICS, SPRINGS, PLAY_EFFECT, PLAY_EFFECT_PHASE])

    SWITCH_STAGE = 'TLSwitchStageEvent'
    SWITCH_LOCATION = 'TLSwitchLocationEvent'
    SHOW_PEANUTS = 'TLShowPeanuts'

    VALID_NON_ACTOR_NODES = frozenset([SWITCH_STAGE, SWITCH_LOCATION, SHOW_PEANUTS])

    SHOW_ARMOR = 'TLShowArmor'

    __file: game_file
    __dialog: dialog_object
    __effect_components_parent_node: et.Element
    __duration: dc.Decimal
    __original_duration: dc.Decimal
    __phases_start_times: list[dc.Decimal]
    __phases_end_times: list[dc.Decimal]
    __phases_durations: list[dc.Decimal]
    __current_phase_start_time: dc.Decimal | None
    __current_phase_index: int | None
    __node_insertion_index: int | None
    __peanuts_uuids: list[str]
    __cameras_uuids: list[str]

    def __init__(self, gamefile: game_file, dialog: dialog_object) -> None:
        self.__file = gamefile
        self.__dialog = dialog
        node = gamefile.root_node.find('./region[@id="TimelineContent"]/node[@id="TimelineContent"]/children/node[@id="Effect"]/children/node[@id="EffectComponents"]/children')
        if node is None:
            raise RuntimeError(f"file {gamefile.relative_file_path} doesn't contain a timeline object")
        self.__effect_components_parent_node = node
        self.__phases_start_times = list[dc.Decimal]()
        self.__phases_end_times = list[dc.Decimal]()
        self.__phases_durations = list[dc.Decimal]()
        self.__original_duration = self.scan_timeline()
        self.__current_phase_start_time = None
        self.__current_phase_index = None
        self.__node_insertion_index = None
        self.__peanuts_uuids = list[str]()
        peanuts = gamefile.root_node.findall('./region[@id="TimelineContent"]/node[@id="TimelineContent"]/children/node[@id="PeanutSlotIdMap"]/children/node[@id="Object"]/children/node[@id="Object"][@key="MapKey"]')
        for peanut in peanuts:
            peanut_uuid = get_required_bg3_attribute(peanut, 'MapKey')
            self.__peanuts_uuids.append(peanut_uuid)
        self.__cameras_uuids = list[str]()

    @property
    def timeline_file(self) -> game_file:
        return self.__file

    @property
    def filename(self) -> str:
        return self.__file.relative_file_path

    @property
    def duration(self) -> float:
        return float(self.__duration)

    @property
    def original_duration(self) -> float:
        return float(self.__original_duration)

    @property
    def all_effect_components(self) -> tuple[et.Element, ...]:
        return tuple(self.__effect_components_parent_node.findall('./node[@id="EffectComponent"]'))

    @property
    def xml(self) -> et.Element:
        return self.__file.root_node

    @staticmethod
    def __recurse_update_node_times(current_node: et.Element, time_delta: dc.Decimal) -> None:
        time_value = get_bg3_attribute(current_node, 'Time')
        if time_value is not None:
            effective_time_value = decimal_from_str(time_value) + time_delta
            set_bg3_attribute(current_node, 'Time', str(effective_time_value))
        children = current_node.findall("./children/node")
        for child in children:
            timeline_object.__recurse_update_node_times(child, time_delta)

    def __update_phase_duration(self) -> None:
        effect_node = self.__file.root_node.find('./region[@id="TimelineContent"]/node[@id="TimelineContent"]/children/node[@id="Effect"]')
        if effect_node is None:
            raise RuntimeError(f"cannot find the 'Effect' node in {self.__file.relative_file_path}")
        set_bg3_attribute(effect_node, "Duration", str(self.__duration))

    def __find_node_insertion_index(self) -> None:
        if self.__current_phase_index == 0:
            self.__node_insertion_index = 0
        else:
            self.__node_insertion_index = len(self.__effect_components_parent_node)
            for n in range(0, len(self.__effect_components_parent_node)):
                node = self.__effect_components_parent_node[n]
                node_phase_idx = get_bg3_attribute(node, 'PhaseIndex')
                if node_phase_idx is None:
                    node_phase_idx = 0
                else:
                    node_phase_idx = int(node_phase_idx)
                if self.__current_phase_index == node_phase_idx:
                    self.__node_insertion_index = n
                    break

    def __get_tl_node_start_time(self, tl_node: et.Element) -> dc.Decimal:
        start_time = get_bg3_attribute(tl_node, 'StartTime')
        if start_time is None:
            return DECIMAL_ZERO
        return decimal_from_str(start_time)

    def insert_new_tl_node(self, tl_node: et.Element) -> None:
        start_time = self.__get_tl_node_start_time(tl_node)
        n = len(self.__effect_components_parent_node)
        if n > 0:
            tail_node_start_time = self.__get_tl_node_start_time(self.__effect_components_parent_node[n - 1])
        else:
            tail_node_start_time = DECIMAL_ZERO
        if start_time >= tail_node_start_time:
            self.__effect_components_parent_node.append(tl_node)
        else:
            if self.__node_insertion_index is None:
                raise ValueError("self.__node_insertion_index is None")
            insert_pos = self.__node_insertion_index
            while insert_pos < n:
                t = self.__get_tl_node_start_time(self.__effect_components_parent_node[insert_pos])
                if t > start_time:
                    break
                insert_pos += 1
            if insert_pos > 0:
                insert_pos -= 1
            self.__effect_components_parent_node.insert(insert_pos, tl_node)

    def scan_timeline(self) -> dc.Decimal:
        self.__duration = DECIMAL_ZERO
        effect_node = self.__file.root_node.find('./region[@id="TimelineContent"]/node[@id="TimelineContent"]/children/node[@id="Effect"]')
        if effect_node is None:
            raise RuntimeError(f"cannot determine duration of timeline {self.__file.relative_file_path}")
        phases = effect_node.findall('./children/node[@id="Phases"]/children/node[@id="Phase"]')
        self.__phases_start_times = list[dc.Decimal]()
        for phase in phases:
            phase_duration = decimal_from_str(get_required_bg3_attribute(phase, 'Duration'))
            self.__phases_durations.append(phase_duration)
        effect_components = effect_node.findall('./children/node[@id="EffectComponents"]/children/node[@id="EffectComponent"]')

        timeline_duration = DECIMAL_ZERO        
        for effect_component in effect_components:
            phase_index = get_bg3_attribute(effect_component, 'PhaseIndex')
            if phase_index is None:
                effective_phase_index = 0
            else:
                effective_phase_index = int(phase_index)
            start_time = get_bg3_attribute(effect_component, 'StartTime')
            if start_time is None:
                effective_start_time = DECIMAL_ZERO
            else:
                effective_start_time = decimal_from_str(start_time)
            end_time = decimal_from_str(get_required_bg3_attribute(effect_component, 'EndTime'))
            if len(self.__phases_start_times) <= effective_phase_index:
                self.__phases_start_times.append(effective_start_time)
                self.__phases_end_times.append(end_time)
            else:
                existing_start_time = self.__phases_start_times[effective_phase_index]
                existing_end_time = self.__phases_end_times[effective_phase_index]
                if existing_start_time > effective_start_time:
                    self.__phases_start_times[effective_phase_index] = effective_start_time
                if existing_end_time < end_time:
                    self.__phases_end_times[effective_phase_index] = end_time
            if timeline_duration < end_time:
                timeline_duration = end_time
        self.__duration = timeline_duration
        set_bg3_attribute(effect_node, "Duration", str(self.__duration))
        return self.__duration

    def get_timeline_actors(self, actor_type_id: str | Iterable[str] | None = None) -> dict[str, et.Element]:
        result = dict[str, et.Element]()
        actors = self.__file.root_node.findall('./region[@id="TimelineContent"]/node[@id="TimelineContent"]/children/node[@id="TimelineActorData"]/children/node[@id="TimelineActorData"]/children/node[@id="Object"][@key="MapKey"]')
        if isinstance(actor_type_id, str):
            actor_type_ids = frozenset([actor_type_id])
        elif isinstance(actor_type_id, Iterable):
            actor_type_ids = frozenset(actor_type_id)
        else:
            actor_type_ids = None
        for actor in actors:
            actor_uuid = get_required_bg3_attribute(actor, 'MapKey')
            value = actor.find('./children/node[@id="Value"]')
            if value is None:
                raise RuntimeError('Failed to get timeline actors')
            type_id = get_bg3_attribute(value, 'ActorTypeId')
            if actor_type_ids is None or type_id in actor_type_ids:
                result[actor_uuid] = value
        return result

    def get_tl_node_actor_uuid(self, node: XmlElement) -> str | None:
        actor = node.find('./children/node[@id="Actor"]')
        if actor is not None:
            return get_bg3_attribute(actor, 'UUID')

    def get_timeline_actors_uuids(self, actor_type_id: str | Iterable[str] | None = None) -> tuple[str, ...]:
        return tuple(self.get_timeline_actors(actor_type_id).keys())

    def get_timeline_peanuts_uuids(self) -> tuple[str, ...]:
        return tuple(self.__peanuts_uuids)

    def get_phase_start_time(self, phase_index: int) -> dc.Decimal:
        if phase_index >= len(self.__phases_start_times):
            raise KeyError(f"phase index {phase_index} is out of bounds [0; {len(self.__phases_start_times)})")
        return self.__phases_start_times[phase_index]

    def get_phase_duration(self, phase_index: int) -> dc.Decimal:
        if phase_index >= len(self.__phases_durations):
            raise KeyError(f"phase index {phase_index} is out of bounds [0; {len(self.__phases_durations)})")
        return self.__phases_durations[phase_index]


    def create_narrator_timeline_actor_data(self) -> None:
        timeline_actor_data_children = self.__file.root_node.find('./region[@id="TimelineContent"]/node[@id="TimelineContent"]/children/node[@id="TimelineActorData"]/children/node[@id="TimelineActorData"]/children')
        if timeline_actor_data_children is None:
            raise RuntimeError(f'TimelineActorData is not found in timeline {self.__file.relative_file_path}')
        timeline_actor_data_nodes = timeline_actor_data_children.findall('node[@id="Object"]')
        for timeline_actor_data_node in timeline_actor_data_nodes:
            actor_uuid = get_required_bg3_attribute(timeline_actor_data_node, 'MapKey')
            if actor_uuid == SPEAKER_NARRATOR:
                return
        narrator_node = et.fromstring(''.join([
            '<node id="Object" key="MapKey"><attribute id="MapKey" type="guid" value="a346318f-15b3-49ad-ab97-ddf8283dc339" />',
            '<children><node id="Value">',
            '<attribute id="Speaker" type="int32" value="-666" />',
            '<attribute id="ActorTypeId" type="FixedString" value="narrator" />',
            '<attribute id="ActorType" type="uint8" value="0" />',
            '<attribute id="DefaultStepOutDelay" type="float" value="0.06311228" />',
            '<attribute id="AudienceSlot" type="uint8" value="16" />',
            '<attribute id="SceneActorIndex" type="int32" value="0" />',
            '<children><node id="CompiledNodeSnapshots"><children><node id="ComponentMap"></node></children></node></children>',
            '</node></children></node>'
        ]))
        timeline_actor_data_children.append(narrator_node)


    def create_new_phase(
            self,
            dialog_node_uuid: str,
            phase_duration: str | dc.Decimal,
            /,
            line_index: int | None = None,
            additional_nodes: Iterable[str] | None = None
    ) -> int:
        phases_children = self.__file.root_node.find('./region[@id="TimelineContent"]/node[@id="TimelineContent"]/children/node[@id="Effect"]/children/node[@id="Phases"]/children')
        if phases_children is None:
            raise RuntimeError(f"cannot find 'Phases' in timeline {self.__file.relative_file_path}")
        phase_index = len(phases_children)
        effective_phase_duration = decimal_from_str(phase_duration)
        timeline_phases_children = self.__file.root_node.find('./region[@id="TimelineContent"]/node[@id="TimelineContent"]/children/node[@id="TimelinePhases"]/children/node[@id="Object"]/children')
        if timeline_phases_children is None:
            raise RuntimeError(f"cannot find 'TimelinePhases' in timeline {self.__file.relative_file_path}")
        phase_xml = '<node id="Phase">' + \
                f'<attribute id="Duration" type="float" value="{effective_phase_duration}" />' + \
                '<attribute id="PlayCount" type="int32" value="1" />' + \
                f'<attribute id="DialogNodeId" type="guid" value="{dialog_node_uuid}" />' + \
				'<children><node id="QuestionHoldAutomation" /></children></node>'
        if line_index is None:
            reference_id = dialog_node_uuid
        else:
            tag_texts = self.__dialog.get_tagged_texts(dialog_node_uuid)
            if line_index >= len(tag_texts) or line_index < 0:
                raise IndexError(f"line index {line_index} is out of bounds [0; {len(tag_texts)})")
            reference_id = get_required_bg3_attribute(tag_texts[line_index], "CustomSequenceId")
        timeline_phase_xml = f'<node id="Object" key="MapKey"><attribute id="MapKey" type="guid" value="{reference_id}" /><attribute id="MapValue" type="uint64" value="{phase_index}" /></node>'
        phases_children.append(et.fromstring(phase_xml))
        timeline_phases_children.append(et.fromstring(timeline_phase_xml))
        if additional_nodes:
            for additional_node in additional_nodes:
                timeline_phase_xml = f'<node id="Object" key="MapKey"><attribute id="MapKey" type="guid" value="{additional_node}" /><attribute id="MapValue" type="uint64" value="{phase_index}" /></node>'
                timeline_phases_children.append(et.fromstring(timeline_phase_xml))

        self.__current_phase_index = phase_index
        self.__current_phase_start_time = self.__duration
        self.__duration = self.__duration + effective_phase_duration
        self.__phases_start_times.append(self.__current_phase_start_time)
        self.__phases_durations.append(effective_phase_duration)
        self.__phases_end_times.append(self.__duration)
        self.__find_node_insertion_index()
        self.__update_phase_duration()
        return self.__current_phase_index

    def use_existing_phase(self, phase_id: str | int) -> timeline_phase:
        phase = self.get_timeline_phase(phase_id)
        self.__current_phase_index = phase.index
        self.__current_phase_start_time = phase.start
        self.__find_node_insertion_index()
        return phase

    def find_tl_node(self, node_uuid: str) -> et.Element:
        for node in self.all_effect_components:
            if get_bg3_attribute(node, 'ID') == node_uuid:
                return node
        raise KeyError(f"node {node_uuid} doesn't exist in timeline {self.__file.relative_file_path}")

    def get_phase_by_tl_node(self, tl_node: et.Element | str) -> timeline_phase:
        if isinstance(tl_node, str):
            tl_node = self.find_effect_component(tl_node)
        node_phase_idx = get_bg3_attribute(tl_node, 'PhaseIndex')
        if node_phase_idx is None:
            node_phase_idx = 0
        else:
            node_phase_idx = int(node_phase_idx)
        return self.get_timeline_phase(node_phase_idx)

    def find_tl_nodes_of_a_phase(self, phase_id: int | str) -> Iterable[et.Element]:
        result = list[et.Element]()
        phase = self.get_timeline_phase(phase_id)
        for node in self.all_effect_components:
            node_phase_idx = get_bg3_attribute(node, 'PhaseIndex')
            if node_phase_idx is None:
                node_phase_idx = 0
            else:
                node_phase_idx = int(node_phase_idx)
            if node_phase_idx == phase.index:
                result.append(node)
            elif node_phase_idx > phase.index:
                return result
        return result

    def get_effective_actor(self, actor_uuid: str) -> tuple[str, bool]:
        if actor_uuid == SPEAKER_NARRATOR:
            return SPEAKER_NARRATOR, False
        if actor_uuid in PEANUTS:
            peanut_override = False
            if actor_uuid == PEANUT_SLOT_0:
                effective_actor = self.__peanuts_uuids[0]
            elif actor_uuid == PEANUT_SLOT_1:
                effective_actor = self.__peanuts_uuids[1]
            elif actor_uuid == PEANUT_SLOT_2:
                effective_actor = self.__peanuts_uuids[2]
            else:
                raise RuntimeError(f'unexpected peanut: {actor_uuid}')
        else:
            try:
                effective_actor = self.__dialog.get_speaker_actor_uuid(actor_uuid)
                peanut_override = self.__dialog.is_peanut_speaker(actor_uuid)
            except:
                effective_actor = actor_uuid
                peanut_override = False
        return effective_actor, peanut_override

    def get_tl_node_speaker_uuid(self, tl_node: et.Element) -> str | None:
        actor_node = tl_node.find('./children/node[@id="Actor"]')
        if actor_node is None:
            raise RuntimeError("cannot determine actor: actor node doesn't exist")
        actor_uuid = get_required_bg3_attribute(actor_node, 'UUID')
        speakers = self.__file.xml.findall('./region[@id="TimelineContent"]/node[@id="TimelineContent"]/children/node[@id="TimelineSpeakers"]/children/node[@id="TimelineSpeaker"]/children/node[@id="Object"][@key="MapKey"]')
        for speaker in speakers:
            map_val = get_required_bg3_attribute(speaker, 'MapValue')
            if map_val == actor_uuid:
                speaker_index = get_required_bg3_attribute(speaker, 'MapKey')
                return self.__dialog.get_speaker_by_index(int(speaker_index))
        return None

    def clone_tl_node(
            self,
            source_node: str | et.Element,
            /,
            new_node_uuid: str | None = None,
            entire_phase_node_duration: bool = False,
            new_node_duration: str | dc.Decimal | None = None,
            new_actor: str | None = None
    ) -> et.Element:
        if self.__current_phase_index is None or self.__current_phase_start_time is None:
            raise RuntimeError("cannot clone a node without creating a new phase first")
        if isinstance(source_node, str):
            source_node = self.find_tl_node(source_node)
        elif not isinstance(source_node, et.Element):
            raise TypeError(f"unexpected type of 'source_node' argument: {type(source_node)}")
        new_node = et.fromstring(et.tostring(source_node))
        phase_index = get_bg3_attribute(source_node, 'PhaseIndex')
        val = get_bg3_attribute(source_node, 'StartTime')
        source_node_start = DECIMAL_ZERO if val is None else decimal_from_str(val)
        source_node_end = decimal_from_str(get_required_bg3_attribute(source_node, 'EndTime'))
        if phase_index is None:
            phase_index = 0
        else:
            phase_index = int(phase_index)
        source_phase_start = self.__phases_start_times[phase_index]
        current_phase_duration = self.__phases_durations[self.__current_phase_index]
        current_phase_end_time = self.__current_phase_start_time + current_phase_duration

        if entire_phase_node_duration:
            effective_new_node_duration = current_phase_duration
        elif new_node_duration is None:
            effective_new_node_duration = source_node_end - source_node_start
        else:
            effective_new_node_duration = decimal_from_str(new_node_duration)

        if effective_new_node_duration < TIMELINE_DECIMAL_PRECISION:
            raise ValueError(f"timeline node duration is too short: {effective_new_node_duration}")

        if new_node_uuid is None:
            new_node_uuid = new_random_uuid()
        time_delta = source_node_start - source_phase_start
        if time_delta <= TIMELINE_DECIMAL_PRECISION:
            time_delta = DECIMAL_ZERO
        new_node_start = self.__current_phase_start_time + time_delta
        new_node_end = new_node_start + effective_new_node_duration
        if new_node_end > current_phase_end_time:
            new_node_end = current_phase_end_time
        set_bg3_attribute(new_node, 'ID', new_node_uuid, attribute_type = 'guid')
        set_bg3_attribute(new_node, 'PhaseIndex', str(self.__current_phase_index), attribute_type = 'int64')
        set_bg3_attribute(new_node, 'StartTime', str(new_node_start), attribute_type = 'float')
        set_bg3_attribute(new_node, 'EndTime', str(new_node_end), attribute_type = 'float')
        timeline_object.__recurse_update_node_times(new_node, new_node_start - source_node_start)
        if new_actor is not None:
            actor_node = new_node.find('./children/node[@id="Actor"]')
            if actor_node is None:
                raise RuntimeError(f'effect component cloning failed: the source node has no actor node')
            peanut_override = False
            try:
                effective_actor, peanut_override = self.get_effective_actor(new_actor)
            except:
                effective_actor = new_actor
            set_bg3_attribute(actor_node, 'UUID', effective_actor, attribute_type = 'guid')
            if peanut_override:
                set_bg3_attribute(actor_node, 'PeanutOverride', 'False', attribute_type = 'bool')
        return new_node

    def create_new_voice_phase_from_another(
            self,
            template_dialog_node_uuid: str,
            speaker: str,
            voice_duration: str | dc.Decimal,
            dialog_node_uuid: str,
            /,
            skip_tl_nodes: Iterable[str] | None = None,
            phase_duration: str | dc.Decimal | None = None,
            line_index: int | None = None,
            emotions: dict[str, Iterable[tuple[str | float, int, int | None]]] | None = None,
            attitudes: dict[str, Iterable[tuple[str | float, str, str, int | None]]] | None = None
    ) -> None:
        tl_phase = self.get_timeline_phase(template_dialog_node_uuid)
        phase_components = list[et.Element]()
        for effect_component in self.all_effect_components:
            phase_index = get_bg3_attribute(effect_component, 'PhaseIndex')
            phase_index = 0 if phase_index is None else int(phase_index)
            if phase_index == tl_phase.index:
                phase_components.append(effect_component)
        if phase_duration is None:
            effective_phase_duration = decimal_from_str(voice_duration)
        else:
            effective_phase_duration = decimal_from_str(phase_duration)
        self.create_new_phase(dialog_node_uuid, effective_phase_duration, line_index=line_index)
        skip_set = frozenset(skip_tl_nodes) if skip_tl_nodes is not None else frozenset()
        tl_voice_cloned = False
        emotions_added = list[str]()
        attitudes_added = list[str]()
        for effect_component in phase_components:
            tl_node_type = get_required_bg3_attribute(effect_component, 'Type')
            if tl_node_type in skip_set:
                continue
            if tl_node_type == 'TLVoice':
                if tl_voice_cloned:
                    #raise RuntimeError(f'cloning of voice phases with multiple TLVoice nodes is not supported')
                    continue
                tl_voice_cloned = True
                new_effect_component = self.clone_tl_node(effect_component, new_node_duration = voice_duration, new_actor = speaker)
                if line_index is None:
                    reference_id = dialog_node_uuid
                else:
                    tag_texts = self.__dialog.get_tagged_texts(dialog_node_uuid)
                    if line_index >= len(tag_texts) or line_index < 0:
                        raise IndexError(f"line index {line_index} is out of bounds [0; {len(tag_texts)})")
                    reference_id = get_required_bg3_attribute(tag_texts[line_index], "CustomSequenceId")
                set_bg3_attribute(new_effect_component, 'DialogNodeId', dialog_node_uuid, attribute_type='guid')
                set_bg3_attribute(new_effect_component, 'ReferenceId', reference_id, attribute_type='guid')
            elif tl_node_type == 'TLEmotionEvent':
                new_effect_component = self.clone_tl_node(effect_component, entire_phase_node_duration = True)
                speaker_uuid = self.get_tl_node_speaker_uuid(effect_component)
                if emotions is not None and speaker_uuid is not None and speaker_uuid in emotions:
                    children = new_effect_component.find('./children')
                    if children is None:
                        new_effect_component.append(et.fromstring('<children><node id="Keys"><children></children></node></children>'))
                    else:
                        emotion_keys = children.find('./node[@id="Keys"]')
                        if emotion_keys is not None:
                            children.remove(emotion_keys)
                        children.append(et.fromstring('<node id="Keys"><children></children></node>'))
                    children = new_effect_component.find('./children/node[@id="Keys"]/children')
                    if children is None:
                        raise RuntimeError("this should never happen: children node doesn't exist")
                    for emotion in emotions[speaker_uuid]:
                        children.append(self.create_emotion_key(emotion[0], emotion[1], variation = emotion[2]))
                    emotions_added.append(speaker_uuid)
            elif tl_node_type == 'TLAttitudeEvent':
                new_effect_component = self.clone_tl_node(effect_component, entire_phase_node_duration = True)
                speaker_uuid = self.get_tl_node_speaker_uuid(effect_component)
                if attitudes is not None and speaker_uuid is not None and speaker_uuid in attitudes:
                    children = new_effect_component.find('./children')
                    if children is None:
                        new_effect_component.append(et.fromstring('<children><node id="Keys"><children></children></node></children>'))
                    else:
                        emotion_keys = children.find('./node[@id="Keys"]')
                        if emotion_keys is not None:
                            children.remove(emotion_keys)
                        children.append(et.fromstring('<node id="Keys"><children></children></node>'))                            
                    children = new_effect_component.find('./children/node[@id="Keys"]/children')
                    if children is None:
                        raise RuntimeError(f"this should never happen: children node doesn't exist: {to_compact_string(new_effect_component)}")
                    for attitude in attitudes[speaker_uuid]:
                        interpolation_type = 3 if attitude[3] is None else attitude[3]
                        children.append(self.create_attitude_key(attitude[0], attitude[1], attitude[2], interpolation_type = interpolation_type))
                    attitudes_added.append(speaker_uuid)
            else:
                new_effect_component = self.clone_tl_node(effect_component, entire_phase_node_duration = True)
            #self.__effect_components_parent_node.append(new_effect_component)
            self.insert_new_tl_node(new_effect_component)
        if emotions is not None:
            for speaker_uuid in emotions:
                if speaker_uuid not in emotions_added:
                    emotion_keys = list[et.Element]()
                    for emotion in emotions[speaker_uuid]:
                        emotion_keys.append(self.create_emotion_key(emotion[0], emotion[1], variation = emotion[2]))
                    self.create_tl_actor_node(timeline_object.EMOTION, speaker_uuid, '0.0', effective_phase_duration, emotion_keys)
        if attitudes is not None:
            for speaker_uuid in attitudes:
                if speaker_uuid not in attitudes_added:
                    attitude_keys = list[et.Element]()
                    for attitude in attitudes[speaker_uuid]:
                        attitude_keys.append(self.create_attitude_key(attitude[0], attitude[1], attitude[2]))
                    self.create_tl_actor_node(timeline_object.ATTITUDE, speaker_uuid, '0.0', effective_phase_duration, attitude_keys)

    def create_new_cinematic_phase_from_another(
            self,
            template_dialog_node_uuid: str,
            dialog_node_uuid: str,
            /,
            skip_tl_nodes: Iterable[str] | None = None,
            phase_duration: str | dc.Decimal | None = None,
            line_index: int | None = None,
            emotions: dict[str, Iterable[tuple[str, int, int | None]]] | None = None,
            attitudes: dict[str, Iterable[tuple[str, str, str, int | None]]] | None = None
    ) -> dc.Decimal:
        if self.__current_phase_index is None:
            raise RuntimeError('current phase index is None')
        tl_phase = self.get_timeline_phase(template_dialog_node_uuid)
        phase_components = list[et.Element]()
        for effect_component in self.all_effect_components:
            phase_index = get_bg3_attribute(effect_component, 'PhaseIndex')
            phase_index = 0 if phase_index is None else int(phase_index)
            if phase_index == tl_phase.index:
                phase_components.append(effect_component)
        if phase_duration is None:
            phase_duration = tl_phase.duration
        self.create_new_phase(dialog_node_uuid, phase_duration, line_index=line_index)
        skip_set = frozenset(skip_tl_nodes) if skip_tl_nodes is not None else frozenset()
        emotions_added = list[str]()
        attitudes_added = list[str]()
        for effect_component in phase_components:
            tl_node_type = get_required_bg3_attribute(effect_component, 'Type')
            if tl_node_type in skip_set:
                continue
            if tl_node_type == 'TLEmotionEvent':
                new_effect_component = self.clone_tl_node(effect_component)
                speaker_uuid = self.get_tl_node_speaker_uuid(effect_component)
                if emotions is not None and speaker_uuid is not None and speaker_uuid in emotions:
                    children = new_effect_component.find('./children')
                    if children is None:
                        new_effect_component.append(et.fromstring('<children><node id="Keys"><children></children></node></children>'))
                    else:
                        emotion_keys = children.find('./node[@id="Keys"]')
                        if emotion_keys is not None:
                            children.remove(emotion_keys)
                        children.append(et.fromstring('<node id="Keys"><children></children></node>'))
                    children = new_effect_component.find('./children/node[@id="Keys"]/children')
                    if children is None:
                        raise RuntimeError("this should never happen: children node doesn't exist")
                    for emotion in emotions[speaker_uuid]:
                        children.append(self.create_emotion_key(emotion[0], emotion[1], variation = emotion[2]))
                    emotions_added.append(speaker_uuid)
            elif tl_node_type == 'TLAttitudeEvent':
                new_effect_component = self.clone_tl_node(effect_component)
                speaker_uuid = self.get_tl_node_speaker_uuid(effect_component)
                if attitudes is not None and speaker_uuid is not None and speaker_uuid in attitudes:
                    children = new_effect_component.find('./children')
                    if children is None:
                        new_effect_component.append(et.fromstring('<children><node id="Keys"><children></children></node></children>'))
                    else:
                        emotion_keys = children.find('./node[@id="Keys"]')
                        if emotion_keys is not None:
                            children.remove(emotion_keys)
                        children.append(et.fromstring('<node id="Keys"><children></children></node>'))                            
                    children = new_effect_component.find('./children/node[@id="Keys"]/children')
                    if children is None:
                        raise RuntimeError(f"this should never happen: children node doesn't exist: {to_compact_string(new_effect_component)}")
                    for attitude in attitudes[speaker_uuid]:
                        children.append(self.create_attitude_key(attitude[0], attitude[1], attitude[2]))
                    attitudes_added.append(speaker_uuid)
            else:
                new_effect_component = self.clone_tl_node(effect_component)
            #self.__effect_components_parent_node.append(new_effect_component)
            self.insert_new_tl_node(new_effect_component)
        phase_duration = self.__phases_durations[self.__current_phase_index]
        if emotions is not None:
            for speaker_uuid in emotions:
                if speaker_uuid not in emotions_added:
                    emotion_keys = list[et.Element]()
                    for emotion in emotions[speaker_uuid]:
                        emotion_keys.append(self.create_emotion_key(emotion[0], emotion[1], variation = emotion[2]))
                    self.create_tl_actor_node(timeline_object.EMOTION, speaker_uuid, DECIMAL_ZERO, phase_duration, emotion_keys)
        if attitudes is not None:
            for speaker_uuid in attitudes:
                if speaker_uuid not in attitudes_added:
                    attitude_keys = list[et.Element]()
                    for attitude in attitudes[speaker_uuid]:
                        attitude_keys.append(self.create_attitude_key(attitude[0], attitude[1], attitude[2]))
                    self.create_tl_actor_node(timeline_object.ATTITUDE, speaker_uuid, DECIMAL_ZERO, phase_duration, attitude_keys)
        return phase_duration

    def copy_tl_nodes_to_current_phase(
            self,
            source_phase_id: int | str,
            /,
            node_id_map: dict[str, str] | None = None
    ) -> None:
        tl_nodes = self.find_tl_nodes_of_a_phase(source_phase_id)
        for tl_node in tl_nodes:
            tl_node_id = get_required_bg3_attribute(tl_node, 'ID')
            if node_id_map is not None and tl_node_id in node_id_map:
                new_tl_node_id = node_id_map[tl_node_id]
            else:
                new_tl_node_id = new_random_uuid()
            new_tl_node = self.clone_tl_node(tl_node, new_node_uuid = new_tl_node_id)
            self.insert_new_tl_node(new_tl_node)

    def create_tl_actor_node(
            self,
            node_type: str,
            speaker_actor: str,
            start: str | dc.Decimal,
            end: str | dc.Decimal,
            keys: Iterable[et.Element],
            /,
            node_uuid: str | None = None,
            is_snapped_to_end: bool = False,
            is_mimicry: bool = False,
            peanut_override: bool | None = None
    ) -> et.Element:
        if self.__current_phase_index is None or self.__current_phase_start_time is None:
            raise RuntimeError("a new phase hasn't been created")
        if node_uuid is None:
            node_uuid = new_random_uuid()
        
        effective_actor, effective_peanut = self.get_effective_actor(speaker_actor)
        if peanut_override is None:
            peanut_override = effective_peanut

        if node_type in timeline_object.VALID_ACTOR_NODES:
            xml = [f'<node id="EffectComponent"><attribute id="Type" type="LSString" value="{node_type}" />']
        else:
            raise ValueError(f"unsupported timeline event {node_type}")
        xml.append(f'<attribute id="ID" type="guid" value="{node_uuid}" />')
        start_time = self.__current_phase_start_time + decimal_from_str(start)
        end_time = self.__current_phase_start_time + decimal_from_str(end)
        xml.append(f'<attribute id="StartTime" type="float" value="{start_time}" />')
        xml.append(f'<attribute id="EndTime" type="float" value="{end_time}" />')
        if self.__current_phase_index > 0:
            xml.append(f'<attribute id="PhaseIndex" type="int64" value="{self.__current_phase_index}" />')
        if is_snapped_to_end:
            xml.append('<attribute id="IsSnappedToEnd" type="bool" value="True" />')
        if is_mimicry:
            xml.append('<attribute id="IsMimicry" type="bool" value="True" />')
        if peanut_override:
            xml.append(f'<children><node id="Actor"><attribute id="UUID" type="guid" value="{effective_actor}" /><attribute id="PeanutOverride" type="bool" value="True" /></node>')
        else:
            xml.append(f'<children><node id="Actor"><attribute id="UUID" type="guid" value="{effective_actor}" /></node>')
        if get_len(keys) > 0:
            xml.append('<node id="Keys"><children></children></node>')
        xml.append('</children>')
        xml.append('</node>')
        tl_node = et.fromstring("".join(xml))
        if get_len(keys) > 0:
            keys_children = tl_node.find('./children/node[@id="Keys"]/children')
            if keys_children is None:
                raise RuntimeError(f'cannot add keys to the node: {to_compact_string(tl_node)}')
            for key in keys:
                keys_children.append(key)
        #self.__effect_components_parent_node.append(tl_node)
        self.insert_new_tl_node(tl_node)
        return tl_node

    def create_tl_actor_nodes(
            self,
            node_type: str,
            actors: list[str],
            start: str | dc.Decimal,
            end: str | dc.Decimal,
            keys: Iterable[et.Element],
            /,
            is_snapped_to_end: bool = False,
            is_mimicry: bool = False,
            peanut_override: bool | None = None
    ) -> list[et.Element]:
        return [self.create_tl_actor_node(
            node_type,
            actor,
            start,
            end,
            keys,
            is_snapped_to_end=is_snapped_to_end,
            is_mimicry=is_mimicry,
            peanut_override=peanut_override) for actor in actors]

    def create_tl_non_actor_node(
            self,
            node_type: str,
            start: str | dc.Decimal,
            end: str | dc.Decimal,
            keys: Iterable[et.Element],
            /,
            node_uuid: str | None = None,
            is_snapped_to_end: bool = False,
    ) -> et.Element:
        if self.__current_phase_index is None or self.__current_phase_start_time is None:
            raise RuntimeError("a new phase hasn't been created")
        if node_uuid is None:
            node_uuid = new_random_uuid()
        if node_type in timeline_object.VALID_NON_ACTOR_NODES:
            xml = [f'<node id="EffectComponent"><attribute id="Type" type="LSString" value="{node_type}" />']
        else:
            raise ValueError(f"unsupported timeline event {node_type}")
        xml.append(f'<attribute id="ID" type="guid" value="{node_uuid}" />')
        start_time = self.__current_phase_start_time + decimal_from_str(start)
        end_time = self.__current_phase_start_time + decimal_from_str(end)
        xml.append(f'<attribute id="StartTime" type="float" value="{start_time}" />')
        xml.append(f'<attribute id="EndTime" type="float" value="{end_time}" />')
        if self.__current_phase_index > 0:
            xml.append(f'<attribute id="PhaseIndex" type="int64" value="{self.__current_phase_index}" />')
        if is_snapped_to_end:
            xml.append('<attribute id="IsSnappedToEnd" type="bool" value="True" />')
        if get_len(keys) > 0:
            xml.append('<children><node id="Keys"><children></children></node></children>')
        xml.append('</node>')
        tl_node = et.fromstring("".join(xml))
        if keys:
            keys_children = tl_node.find('./children/node[@id="Keys"]/children')
            if keys_children is None:
                raise RuntimeError(f'cannot add keys to the node: {to_compact_string(tl_node)}')
            for key in keys:
                keys_children.append(key)
        #self.__effect_components_parent_node.append(tl_node)
        self.insert_new_tl_node(tl_node)
        return tl_node

    def create_tl_voice(
            self,
            speaker: str,
            start: str | dc.Decimal,
            end: str | dc.Decimal,
            dialog_node_uuid: str,
            /,
            line_index: int | None = None,
            node_uuid: str | None = None,
            performance_fade: float | None = None,
            fade_in: float | None = None,
            fade_out: float | None = None,
            performance_drift_type: int | None = None,
            head_pitch_correction: float | None = None,
            head_roll_correction: float | None = None,
            head_yaw_correction: float | None = None,
            hold_mocap: bool = True,
            disable_mocap: bool = False,
            is_snapped_to_end: bool = False,
            peanut_override: bool | None = None,
            is_mirrored: bool = False
    ) -> et.Element:
        if self.__current_phase_index is None or self.__current_phase_start_time is None:
            raise RuntimeError("a new phase hasn't been created")
        if node_uuid is None:
            node_uuid = new_random_uuid()

        xml = ['<node id="EffectComponent"><attribute id="Type" type="LSString" value="TLVoice" />']
        xml.append(f'<attribute id="ID" type="guid" value="{node_uuid}" />')
        start_time = self.__current_phase_start_time + decimal_from_str(start)
        end_time = self.__current_phase_start_time + decimal_from_str(end)
        xml.append(f'<attribute id="StartTime" type="float" value="{start_time}" />')
        xml.append(f'<attribute id="EndTime" type="float" value="{end_time}" />')
        xml.append(f'<attribute id="DialogNodeId" type="guid" value="{dialog_node_uuid}" />')
        if self.__current_phase_index > 0:
            xml.append(f'<attribute id="PhaseIndex" type="int64" value="{self.__current_phase_index}" />')
        if line_index is None:
            reference_id = dialog_node_uuid
        else:
            tag_texts = self.__dialog.get_tagged_texts(dialog_node_uuid)
            if line_index >= len(tag_texts) or line_index < 0:
                raise IndexError(f"line index {line_index} is out of bounds [0; {len(tag_texts)})")
            reference_id = get_required_bg3_attribute(tag_texts[line_index], "CustomSequenceId")
        xml.append(f'<attribute id="ReferenceId" type="guid" value="{reference_id}" />')        
        if performance_fade is not None:
            xml.append(f'<attribute id="PerformanceFade" type="double" value="{performance_fade}" />')
        if fade_in is not None:
            xml.append(f'<attribute id="FadeIn" type="double" value="{fade_in}" />')
        if fade_out is not None:
            xml.append(f'<attribute id="FadeOut" type="double" value="{fade_out}" />')
        if performance_drift_type is not None:
            xml.append(f'<attribute id="PerformanceDriftType" type="uint8" value="{performance_drift_type}" />')
        if head_pitch_correction is not None:
            xml.append(f'<attribute id="HeadPitchCorrection" type="double" value="{head_pitch_correction}" />')
        if head_roll_correction is not None:
            xml.append(f'<attribute id="HeadRollCorrection" type="double" value="{head_roll_correction}" />')
        if head_yaw_correction is not None:
            xml.append(f'<attribute id="HeadYawCorrection" type="double" value="{head_yaw_correction}" />')
        if not hold_mocap:
            xml.append('<attribute id="HoldMocap" type="bool" value="False" />')
        if disable_mocap:
            xml.append('<attribute id="DisableMocap" type="bool" value="True" />')
        if is_snapped_to_end:
            xml.append('<attribute id="IsSnappedToEnd" type="bool" value="True" />')
        if is_mirrored:
            xml.append('<attribute id="IsMirrored" type="bool" value="True" />')

        effective_actor, effective_peanut_override = self.get_effective_actor(speaker)
        if peanut_override is None:
            peanut_override = effective_peanut_override
        if peanut_override:
            xml.append(f'<children><node id="Actor"><attribute id="UUID" type="guid" value="{effective_actor}" /><attribute id="PeanutOverride" type="bool" value="True" /></node></children>')
        else:
            xml.append(f'<children><node id="Actor"><attribute id="UUID" type="guid" value="{effective_actor}" /></node></children>')
        xml.append('</node>')
        tl_node = et.fromstring("".join(xml))
        #self.__effect_components_parent_node.append(tl_node)
        self.insert_new_tl_node(tl_node)
        return tl_node

    def create_tl_show_armor(
            self,
            target_speaker: str,
            start: str | dc.Decimal,
            end: str | dc.Decimal,
            channels: Iterable[Iterable[et.Element]],
            /,
            node_uuid: str | None = None,
            is_snapped_to_end: bool = False,
            peanut_override: bool | None = None
    ) -> et.Element:
        if self.__current_phase_index is None or self.__current_phase_start_time is None:
            raise RuntimeError("a new phase hasn't been created")           
        if node_uuid is None:
            node_uuid = new_random_uuid()
        xml = [f'<node id="EffectComponent"><attribute id="Type" type="LSString" value="TLShowArmor" />']
        xml.append(f'<attribute id="ID" type="guid" value="{node_uuid}" />')
        start_time = self.__current_phase_start_time + decimal_from_str(start)
        end_time = self.__current_phase_start_time + decimal_from_str(end)
        xml.append(f'<attribute id="StartTime" type="float" value="{start_time}" />')
        xml.append(f'<attribute id="EndTime" type="float" value="{end_time}" />')
        if self.__current_phase_index > 0:
            xml.append(f'<attribute id="PhaseIndex" type="int64" value="{self.__current_phase_index}" />')
        if is_snapped_to_end:
            xml.append('<attribute id="IsSnappedToEnd" type="bool" value="True" />')
        
        effective_actor, effective_peanut_override = self.get_effective_actor(target_speaker)
        if peanut_override is None:
            peanut_override = effective_peanut_override
        xml.append('<children>')
        if peanut_override:
            xml.append(f'<node id="Actor"><attribute id="UUID" type="guid" value="{effective_actor}" />' +
                       '<attribute id="PeanutOverride" type="bool" value="True" /></node>')
        else:
            xml.append(f'<node id="Actor"><attribute id="UUID" type="guid" value="{effective_actor}" /></node>')
        if get_len(channels) == 11:
            xml.append('<node id="Channels"><children></children></node>')
        elif get_len(channels) != 0:
            raise ValueError(f"TLShowArmor requires 11 channels, {get_len(channels)} were provided")
        xml.append('</children></node>')
        tl_node = et.fromstring("".join(xml))
        if get_len(channels) == 11:
            channels_children = tl_node.find('./children/node[@id="Channels"]/children')
            if channels_children is None:
                raise RuntimeError(f'cannot add channels to the node: {to_compact_string(tl_node)}')
            for channel in channels:
                if get_len(channel) == 0:
                    channels_children.append(et.fromstring('<node id="" />'))
                else:
                    channel_node = et.fromstring('<node id=""><children><node id="Keys"><children></children></node></children></node>')
                    keys_children = channel_node.find('./children/node[@id="Keys"]/children')
                    if keys_children is None:
                        raise RuntimeError('keys_children is None')
                    for key in channel:
                        keys_children.append(key)
                    channels_children.append(channel_node)
        #self.__effect_components_parent_node.append(tl_node)
        self.insert_new_tl_node(tl_node)
        return tl_node

    def create_tl_transform(
            self,
            actor: str,
            start: str | dc.Decimal,
            end: str | dc.Decimal,
            channels: Iterable[Iterable[et.Element]],
            /,
            node_uuid: str | None = None,
            continuous: bool = False,
            is_snapped_to_end: bool = False
    ) -> et.Element:
        if self.__current_phase_index is None or self.__current_phase_start_time is None:
            raise RuntimeError("a new phase hasn't been created")
        if get_len(channels) > 0 and get_len(channels) != 6:
            raise ValueError(f"expected 6 channels, got {get_len(channels)}")
        effective_actor, _ = self.get_effective_actor(actor)
        if node_uuid is None:
            node_uuid = new_random_uuid()
        xml = [f'<node id="EffectComponent"><attribute id="Type" type="LSString" value="TLTransform" />']
        xml.append(f'<attribute id="ID" type="guid" value="{node_uuid}" />')
        start_time = self.__current_phase_start_time + decimal_from_str(start)
        end_time = self.__current_phase_start_time + decimal_from_str(end)
        xml.append(f'<attribute id="StartTime" type="float" value="{start_time}" />')
        xml.append(f'<attribute id="EndTime" type="float" value="{end_time}" />')
        if self.__current_phase_index > 0:
            xml.append(f'<attribute id="PhaseIndex" type="int64" value="{self.__current_phase_index}" />')
        if continuous:
            xml.append('<attribute id="Continuous" type="bool" value="True" />')
        if is_snapped_to_end:
            xml.append('<attribute id="IsSnappedToEnd" type="bool" value="True" />')
        if get_len(channels) == 0:
            xml.append(f'<children><node id="Actor"><attribute id="UUID" type="guid" value="{effective_actor}" /></node></children></node>')
        else:
            xml.append(f'<children><node id="Actor"><attribute id="UUID" type="guid" value="{effective_actor}" /></node>' +
                       '<node id="TransformChannels"><children></children></node></children></node>')
        tl_node = et.fromstring("".join(xml))
        if get_len(channels) == 6:
            transform_channels_children = tl_node.find('./children/node[@id="TransformChannels"]/children')
            if transform_channels_children is None:
                raise RuntimeError('transform_channels_children is None')
            for channel in channels:
                if get_len(channel) == 0:
                    transform_channels_children.append(et.fromstring('<node id="TransformChannel" />'))
                else:
                    channel_node = et.fromstring('<node id="TransformChannel"><children><node id="Keys"><children></children></node></children></node>')
                    channel_node_keys_children = channel_node.find('./children/node[@id="Keys"]/children')
                    if channel_node_keys_children is None:
                        raise RuntimeError('channel_node_keys_children is None')
                    for key in channel:
                        channel_node_keys_children.append(key)
                    transform_channels_children.append(channel_node)
        #self.__effect_components_parent_node.append(tl_node)
        self.insert_new_tl_node(tl_node)
        return tl_node

    def create_tl_shot(
            self,
            camera: int | str | None,
            start: str | dc.Decimal,
            end: str | dc.Decimal,
            /,
            node_uuid: str | None = None,
            is_snapped_to_end: bool | None = None,
            is_looping: bool | None = None,
            is_logic_enabled: bool | None = None,
            disable_conditional_staging: bool | None = None,
            is_jcut_enabled: bool | None = None,
            j_cut_length: float | None = None,
            automated_camera: bool | None = None,
            automated_lighting: bool | None = None,
            companion_cameras: tuple[object, object, object] | None = None
    ) -> et.Element:
        if self.__current_phase_index is None or self.__current_phase_start_time is None:
            raise RuntimeError("a new phase hasn't been created")
        if isinstance(camera, int):
            if camera < 0 or camera >= len(self.__cameras_uuids):
                raise ValueError(f"camera index is out of bounds [0, {len(self.__cameras_uuids)})")
            effective_camera_uuid = self.__cameras_uuids[camera]
        elif isinstance(camera, str):
            effective_camera_uuid = camera
        else:
            effective_camera_uuid = ''
        if node_uuid is None:
            node_uuid = new_random_uuid()
        xml = [f'<node id="EffectComponent"><attribute id="Type" type="LSString" value="TLShot" />']
        xml.append(f'<attribute id="ID" type="guid" value="{node_uuid}" />')
        start_time = self.__current_phase_start_time + decimal_from_str(start)
        end_time = self.__current_phase_start_time + decimal_from_str(end)
        xml.append(f'<attribute id="StartTime" type="float" value="{start_time}" />')
        xml.append(f'<attribute id="EndTime" type="float" value="{end_time}" />')
        if self.__current_phase_index > 0:
            xml.append(f'<attribute id="PhaseIndex" type="int64" value="{self.__current_phase_index}" />')
        if is_snapped_to_end is not None:
            xml.append(f'<attribute id="IsSnappedToEnd" type="bool" value="{is_snapped_to_end}" />')
        if is_looping is not None:
            xml.append(f'<attribute id="IsLooping" type="bool" value="{is_looping}" />')
        if is_logic_enabled is not None:
            xml.append(f'<attribute id="IsLogicEnabled" type="bool" value="{is_logic_enabled}" />')
        if disable_conditional_staging is not None:
            xml.append(f'<attribute id="DisableConditionalStaging" type="bool" value="{disable_conditional_staging}" />')
        if is_jcut_enabled is not None:
            xml.append(f'<attribute id="IsJCutEnabled" type="bool" value="{is_jcut_enabled}" />')
        if automated_camera is not None:
            xml.append(f'<attribute id="AutomatedCamera" type="bool" value="{automated_camera}" />')
        if automated_lighting is not None:
            xml.append(f'<attribute id="AutomatedLighting" type="bool" value="{automated_lighting}" />')

        if companion_cameras is not None:
            for i in range(0, 3):
                c = "ABC"[i]
                companion_camera = companion_cameras[i]
                if isinstance(companion_camera, int):
                    camera_uuid = self.__cameras_uuids[companion_camera]
                elif isinstance(companion_camera, str):
                    camera_uuid = companion_camera
                else:
                    raise TypeError(f'companion camera should be either int or str, got {type(companion_cameras[i])}')
                xml.append(f'<attribute id="CompanionCamera{c}" type="guid" value="{camera_uuid}" />')
        if j_cut_length is not None:
            xml.append(f'<attribute id="JCutLength" type="float" value="{j_cut_length}" />')
        if effective_camera_uuid:
            xml.append(f'<children><node id="CameraContainer"><attribute id="Object" type="guid" value="{effective_camera_uuid}" /></node></children>')
        xml.append('</node>')
        tl_node = et.fromstring("".join(xml))
        #self.__effect_components_parent_node.append(tl_node)
        self.insert_new_tl_node(tl_node)
        return tl_node

    def create_tl_camera_dof(
            self,
            camera: int | str,
            start: str | dc.Decimal,
            end: str | dc.Decimal,
            channels: Iterable[Iterable[et.Element]],
            /,
            node_uuid: str | None = None,
            is_snapped_to_end: bool = False
    ) -> et.Element:
        if self.__current_phase_index is None or self.__current_phase_start_time is None:
            raise RuntimeError("a new phase hasn't been created")
        if get_len(channels) > 0 and get_len(channels) != 7:
            raise ValueError(f"expected 7 channels, got {get_len(channels)}")
        if isinstance(camera, str):
            effective_camera_uuid = camera
        elif isinstance(camera, int):
            if camera < 0 or camera >= len(self.__cameras_uuids):
                raise ValueError(f"camera index is out of bounds [0, {len(self.__cameras_uuids)})")
            effective_camera_uuid = self.__cameras_uuids[camera]
        else:
            raise TypeError(f"camera could be either an integer index or a string uuid, got {type(camera)}")
        if node_uuid is None:
            node_uuid = new_random_uuid()
        xml = [f'<node id="EffectComponent"><attribute id="Type" type="LSString" value="TLCameraDoF" />']
        xml.append(f'<attribute id="ID" type="guid" value="{node_uuid}" />')
        start_time = self.__current_phase_start_time + decimal_from_str(start)
        end_time = self.__current_phase_start_time + decimal_from_str(end)
        xml.append(f'<attribute id="StartTime" type="float" value="{start_time}" />')
        xml.append(f'<attribute id="EndTime" type="float" value="{end_time}" />')
        if self.__current_phase_index > 0:
            xml.append(f'<attribute id="PhaseIndex" type="int64" value="{self.__current_phase_index}" />')
        if is_snapped_to_end:
            xml.append('<attribute id="IsSnappedToEnd" type="bool" value="True" />')
        if get_len(channels) == 0:
            xml.append(f'<children><node id="Actor"><attribute id="UUID" type="guid" value="{effective_camera_uuid}" /></node></children>')
        else:
            xml.append(f'<children><node id="Actor"><attribute id="UUID" type="guid" value="{effective_camera_uuid}" /></node>' +
                       '<node id="Channels"><children></children></node></children>')
        xml.append('</node>')
        tl_node = et.fromstring("".join(xml))
        if get_len(channels) == 7:
            channels_children = tl_node.find('./children/node[@id="Channels"]/children')
            if channels_children is None:
                raise RuntimeError('channels_children is None')
            for channel in channels:
                if get_len(channel) == 0:
                    channels_children.append(et.fromstring('<node id="Channel" />'))
                else:
                    channel_node = et.fromstring('<node id="Channel"><children><node id="Keys"><children></children></node></children></node>')
                    channel_node_keys_children = channel_node.find('./children/node[@id="Keys"]/children')
                    if channel_node_keys_children is None:
                        raise RuntimeError('channel_node_keys_children is None')
                    for key in channel:
                        channel_node_keys_children.append(key)
                    channels_children.append(channel_node)
        #self.__effect_components_parent_node.append(tl_node)
        self.insert_new_tl_node(tl_node)
        return tl_node

    def create_tl_material(
            self,
            actor: str,
            start: str | dc.Decimal,
            end: str | dc.Decimal,
            group_id: str,
            material_parameters: Iterable[et.Element],
            visibility_channel_keys: Iterable[et.Element],
            /,
            node_uuid: str | None = None,
            is_continuous: bool = False,
            is_snapped_to_end: bool = False,
            is_overlay: bool = False,
            overlay_priority: int | None = None
    ) -> et.Element:
        if self.__current_phase_index is None or self.__current_phase_start_time is None:
            raise RuntimeError("a new phase hasn't been created")
        if node_uuid is None:
            node_uuid = new_random_uuid()
        xml = [f'<node id="EffectComponent"><attribute id="Type" type="LSString" value="TLMaterial" />']
        xml.append(f'<attribute id="ID" type="guid" value="{node_uuid}" />')
        start_time = self.__current_phase_start_time + decimal_from_str(start)
        end_time = self.__current_phase_start_time + decimal_from_str(end)
        xml.append(f'<attribute id="StartTime" type="float" value="{start_time}" />')
        xml.append(f'<attribute id="EndTime" type="float" value="{end_time}" />')
        if self.__current_phase_index > 0:
            xml.append(f'<attribute id="PhaseIndex" type="int64" value="{self.__current_phase_index}" />')
        if is_snapped_to_end:
            xml.append('<attribute id="IsSnappedToEnd" type="bool" value="True" />')
        if is_continuous:
            xml.append('<attribute id="IsContinuous" type="bool" value="True" />')
        if is_overlay:
            xml.append('<attribute id="IsOverlay" type="bool" value="True" />')
        if overlay_priority is not None:
            xml.append(f'<attribute id="OverlayPriority" type="float" value="{overlay_priority}" />')
        xml.append(f'<attribute id="GroupId" type="guid" value="{group_id}" />')
        effective_actor, _ = self.get_effective_actor(actor)
        xml.append(f'<children><node id="Actor"><attribute id="UUID" type="guid" value="{effective_actor}" /></node>')
        if get_len(material_parameters) > 0:
            xml.append(f'<node id="MaterialParameter"><children></children></node>')
        else:
            xml.append(f'<node id="MaterialParameter" />')
        if get_len(visibility_channel_keys) > 0:
            xml.append(f'<node id="VisibilityChannel"><children><node id="Keys"><children></children></node></children></node>')
        else:
            xml.append(f'<node id="VisibilityChannel" />')
        xml.append('</children></node>')
        tl_node = et.fromstring("".join(xml))
        if get_len(material_parameters) > 0:
            material_parameters_children = tl_node.find('./children/node[@id="MaterialParameter"]/children')
            if material_parameters_children is None:
                raise RuntimeError(f"bad TLMaterial node: {to_compact_string(tl_node)}")
            for material_parameter in material_parameters:
                material_parameters_children.append(material_parameter)
        if get_len(visibility_channel_keys) > 0:
            visibility_channel_keys_children = tl_node.find('./children/node[@id="VisibilityChannel"]/children/node[@id="Keys"]/children')
            if visibility_channel_keys_children is None:
                raise RuntimeError(f"bad TLMaterial node: {to_compact_string(tl_node)}")
            for key in visibility_channel_keys:
                visibility_channel_keys_children.append(key)
        #self.__effect_components_parent_node.append(tl_node)
        self.insert_new_tl_node(tl_node)
        return tl_node

    def create_tl_animation(
            self,
            actor: str,
            start: str | dc.Decimal,
            end: str | dc.Decimal,
            animation_id: str,
            animation_group: str,
            /,
            node_uuid: str | None = None,
            animation_slot: int | None = None,
            animation_play_rate: float | None = None,
            animation_play_start_offset: float | None = None,
            offset_type: int | None = None,
            fade_in: float | None = None,
            fade_out: float | None = None,
            continuous: bool = False,
            is_mirrored: bool = False,
            is_snapped_to_end: bool = False,
            enable_root_motion: bool = False,
            hold_animation: bool = False,
            target_transform: et.Element | None = None
    ) -> et.Element:
        if self.__current_phase_index is None or self.__current_phase_start_time is None:
            raise RuntimeError("a new phase hasn't been created")
        if node_uuid is None:
            node_uuid = new_random_uuid()
        xml = [f'<node id="EffectComponent"><attribute id="Type" type="LSString" value="TLAnimation" />']
        xml.append(f'<attribute id="ID" type="guid" value="{node_uuid}" />')
        start_time = self.__current_phase_start_time + decimal_from_str(start)
        end_time = self.__current_phase_start_time + decimal_from_str(end)
        xml.append(f'<attribute id="StartTime" type="float" value="{start_time}" />')
        xml.append(f'<attribute id="EndTime" type="float" value="{end_time}" />')
        if self.__current_phase_index > 0:
            xml.append(f'<attribute id="PhaseIndex" type="int64" value="{self.__current_phase_index}" />')
        xml.append(f'<attribute id="AnimationSourceId" type="guid" value="{animation_id}" />')
        xml.append(f'<attribute id="AnimationGroup" type="guid" value="{animation_group}" />')
        if animation_slot is not None:
            xml.append(f'<attribute id="AnimationSlot" type="FixedString" value="{animation_slot}" />')
        if animation_play_rate is not None:
            xml.append(f'<attribute id="AnimationPlayRate" type="double" value="{animation_play_rate}" />')
        if animation_play_start_offset is not None:
            xml.append(f'<attribute id="AnimationPlayStartOffset" type="double" value="{animation_play_start_offset}" />')
        if offset_type is not None:
            xml.append(f'<attribute id="OffsetType" type="uint8" value="{offset_type}" />')
        if fade_in is not None:
            xml.append(f'<attribute id="FadeIn" type="double" value="{fade_in}" />')
        if fade_out is not None:
            xml.append(f'<attribute id="FadeOut" type="double" value="{fade_out}" />')
        if continuous:
            xml.append('<attribute id="Continuous" type="bool" value="True" />')
        if is_mirrored:
            xml.append('<attribute id="IsMirrored" type="bool" value="True" />')
        if is_snapped_to_end:
            xml.append('<attribute id="IsSnappedToEnd" type="bool" value="True" />')
        if enable_root_motion:
            xml.append('<attribute id="EnableRootMotion" type="bool" value="True" />')
        if hold_animation:
            xml.append('<attribute id="HoldAnimation" type="bool" value="True" />')
        effective_actor, _ = self.get_effective_actor(actor)
        xml.append(f'<children><node id="Actor"><attribute id="UUID" type="guid" value="{effective_actor}" /></node></children>')
        xml.append('</node>')
        tl_node = et.fromstring("".join(xml))
        if target_transform is not None:
            children = tl_node.find('./children')
            if children is None:
                raise RuntimeError(f'bad TLAnimation node: {to_compact_string(tl_node)}')
            children.append(target_transform)
        #self.__effect_components_parent_node.append(tl_node)
        self.insert_new_tl_node(tl_node)
        return tl_node


    def create_animation_target_transform(
            self,
            scale: float,
            position: tuple[float, float, float],
            rotation: tuple[float, float, float, float]
    ) -> et.Element:
        return et.fromstring(f'<node id="TargetTransform"><attribute id="Scale" type="float" value="{scale}" />' +
                             f'<attribute id="Position" type="fvec3" value="{position[0]} {position[1]} {position[2]}" />' +
                             f'<attribute id="RotationQuat" type="fvec4" value="{rotation[0]} {rotation[1]} {rotation[2]} {rotation[3]}" /></node>')


    def create_tl_camera_fov(
            self,
            camera_uuid: str,
            start: str | dc.Decimal,
            end: str | dc.Decimal,
            keys: Iterable[et.Element],
            /,
            node_uuid: str | None = None,
            is_snapped_to_end: bool = False,
    ) -> et.Element:
        if self.__current_phase_index is None or self.__current_phase_start_time is None:
            raise RuntimeError("a new phase hasn't been created")
        if node_uuid is None:
            node_uuid = new_random_uuid()
        xml = [f'<node id="EffectComponent"><attribute id="Type" type="LSString" value="TLCameraFoV" />']
        xml.append(f'<attribute id="ID" type="guid" value="{node_uuid}" />')
        start_time = self.__current_phase_start_time + decimal_from_str(start)
        end_time = self.__current_phase_start_time + decimal_from_str(end)
        xml.append(f'<attribute id="StartTime" type="float" value="{start_time}" />')
        xml.append(f'<attribute id="EndTime" type="float" value="{end_time}" />')
        if self.__current_phase_index > 0:
            xml.append(f'<attribute id="PhaseIndex" type="int64" value="{self.__current_phase_index}" />')
        if is_snapped_to_end:
            xml.append('<attribute id="IsSnappedToEnd" type="bool" value="True" />')
        xml.append('<children>')
        xml.append(f'<node id="Actor"><attribute id="UUID" type="guid" value="{camera_uuid}" /></node>')
        if get_len(keys) > 0:
            xml.append('<node id="Keys"><children></children></node>')
        xml.append('</children>')
        xml.append('</node>')
        tl_node = et.fromstring("".join(xml))
        if get_len(keys) > 0:
            keys_children = tl_node.find('./children/node[@id="Keys"]/children')
            if not isinstance(keys_children, et.Element):
                raise RuntimeError(f'bad TLCameraFoV node: {to_compact_string(tl_node)}')
            for key in keys:
                keys_children.append(key)
        #self.__effect_components_parent_node.append(tl_node)
        self.insert_new_tl_node(tl_node)
        return tl_node


    def create_tl_camera_look_at(
            self,
            camera_uuid: str,
            start: str | dc.Decimal,
            end: str | dc.Decimal,
            keys: Iterable[et.Element],
            /,
            node_uuid: str | None = None,
            is_snapped_to_end: bool = False
    ) -> et.Element:
        if self.__current_phase_index is None or self.__current_phase_start_time is None:
            raise RuntimeError("a new phase hasn't been created")
        if node_uuid is None:
            node_uuid = new_random_uuid()
        xml = [f'<node id="EffectComponent"><attribute id="Type" type="LSString" value="TLCameraLookAt" />']
        xml.append(f'<attribute id="ID" type="guid" value="{node_uuid}" />')
        start_time = self.__current_phase_start_time + decimal_from_str(start)
        end_time = self.__current_phase_start_time + decimal_from_str(end)
        xml.append(f'<attribute id="StartTime" type="float" value="{start_time}" />')
        xml.append(f'<attribute id="EndTime" type="float" value="{end_time}" />')
        if self.__current_phase_index > 0:
            xml.append(f'<attribute id="PhaseIndex" type="int64" value="{self.__current_phase_index}" />')
        if is_snapped_to_end:
            xml.append('<attribute id="IsSnappedToEnd" type="bool" value="True" />')
        xml.append('<children>')
        xml.append(f'<node id="Actor"><attribute id="UUID" type="guid" value="{camera_uuid}" /></node>')
        if get_len(keys) > 0:
            xml.append('<node id="Keys"><children></children></node>')
        xml.append('</children>')
        xml.append('</node>')
        tl_node = et.fromstring("".join(xml))
        if get_len(keys) > 0:
            keys_children = tl_node.find('./children/node[@id="Keys"]/children')
            if not isinstance(keys_children, et.Element):
                raise RuntimeError(f'bad TLCameraLookAt node: {to_compact_string(tl_node)}')
            for key in keys:
                keys_children.append(key)
        #self.__effect_components_parent_node.append(tl_node)
        self.insert_new_tl_node(tl_node)
        return tl_node


    def create_tl_camera_look_at_key(
            self,
            time: str | dc.Decimal | float,
            target: str,
            bone: str,
            framing: tuple[float, float],
            /,
            interpolation_type: int = 0,
            damping_strength: float | None = None
    ) -> et.Element:
        if self.__current_phase_start_time is None:
            raise RuntimeError("new phase should be created before effect components")
        abs_time = self.__current_phase_start_time + decimal_from(time)
        effective_target, _ = self.get_effective_actor(target)
        xml = [
            f'<node id="Key"><attribute id="Time" type="float" value="{abs_time}" />',
            f'<attribute id="InterpolationType" type="uint8" value="{interpolation_type}" />',
            f'<attribute id="Target" type="guid" value="{effective_target}" />',
            f'<attribute id="Bone" type="FixedString" value="{bone}" />',
            f'<attribute id="Framing" type="fvec2" value="{framing[0]} {framing[1]}" />']
        if damping_strength is not None:
            xml.append(f'<attribute id="DampingStrength" type="float" value="{damping_strength}" />')
        xml.append('</node>')
        return et.fromstring(''.join(xml))


    def create_tl_splatter(
            self,
            actor: str,
            start: str | dc.Decimal,
            end: str | dc.Decimal,
            channels: Iterable[et.Element],
            /,
            node_uuid: str | None = None,
            is_snapped_to_end: bool = False,
    ) -> et.Element:
        if self.__current_phase_index is None or self.__current_phase_start_time is None:
            raise RuntimeError("a new phase hasn't been created")
        if node_uuid is None:
            node_uuid = new_random_uuid()
        xml = [f'<node id="EffectComponent"><attribute id="Type" type="LSString" value="TLSplatter" />']
        xml.append(f'<attribute id="ID" type="guid" value="{node_uuid}" />')
        start_time = self.__current_phase_start_time + decimal_from_str(start)
        end_time = self.__current_phase_start_time + decimal_from_str(end)
        xml.append(f'<attribute id="StartTime" type="float" value="{start_time}" />')
        xml.append(f'<attribute id="EndTime" type="float" value="{end_time}" />')
        if self.__current_phase_index > 0:
            xml.append(f'<attribute id="PhaseIndex" type="int64" value="{self.__current_phase_index}" />')
        if is_snapped_to_end:
            xml.append('<attribute id="IsSnappedToEnd" type="bool" value="True" />')
        xml.append('<children>')
        effective_actor, _ = self.get_effective_actor(actor)
        xml.append(f'<node id="Actor"><attribute id="UUID" type="guid" value="{effective_actor}" /></node>')
        xml.append('<node id="Channels"><children></children></node></children></node>')
        tl_node = et.fromstring(''.join(xml))
        channles_node = tl_node.find('./children/node[@id="Channels"]/children')
        if not isinstance(channles_node, et.Element):
            raise RuntimeError(f'bad TLCameraFoV node: {to_compact_string(tl_node)}')
        for channel in channels:
            channles_node.append(channel)
        self.insert_new_tl_node(tl_node)
        return tl_node

    def create_splatter_channel(
            self,
            splatter_type: int,
            /,
            time: str | dc.Decimal | float | None = None,
            value: float | None = None,
            interpolation_type: int | None = None,
    ) -> et.Element:
        xml = [f'<node id="Channel"><attribute id="SplatterType" type="uint8" value="{splatter_type}" />']
        if time is not None or value is not None:
            xml.append('<children><node id="Keys"><children><node id="Key">')
            if interpolation_type is None:
                interpolation_type = 2
            if time is not None:
                xml.append(f'<attribute id="Time" type="float" value="{decimal_from(time)}" />')
            if value is not None:
                xml.append(f'<attribute id="Value" type="float" value="{value}" />')
            xml.append(f'<attribute id="InterpolationType" type="uint8" value="{interpolation_type}" />')
            xml.append('</node></children></node></children>')
        xml.append('</node>')
        return et.fromstring(''.join(xml))


    def create_attitude_key(
            self,
            time: str | dc.Decimal | float,
            pose: str,
            transition: str,
            /,
            interpolation_type: int = 3
    ) -> et.Element:
        if self.__current_phase_start_time is None:
            raise RuntimeError("new phase should be created before effect components")
        abs_time = self.__current_phase_start_time + decimal_from(time)
        return et.fromstring(f'<node id="Key"><attribute id="Time" type="float" value="{abs_time}" />' +
                                f'<attribute id="InterpolationType" type="uint8" value="{interpolation_type}" />' +
                                f'<attribute id="Pose" type="FixedString" value="{pose}" />' +
                                f'<attribute id="Transition" type="FixedString" value="{transition}" /></node>')

    def create_emotion_key(
            self,
            time: str | dc.Decimal | float,
            emotion: int,
            /,
            variation: int | None = None,
            interpolation_type: int = 3,
            is_sustained: bool = True
    ) -> et.Element:
        if self.__current_phase_start_time is None:
            raise RuntimeError("new phase should be created before effect components")
        abs_time = self.__current_phase_start_time + decimal_from(time)
        strings = [
            f'<node id="Key"><attribute id="Time" type="float" value="{abs_time}" />',
            f'<attribute id="InterpolationType" type="uint8" value="{interpolation_type}" />'
        ]
        if emotion != 0:
            strings.append(f'<attribute id="Emotion" type="int32" value="{emotion}" />')
        if variation is not None and variation > 0:
            strings.append(f'<attribute id="Variation" type="int32" value="{variation}" />')
        if is_sustained == False:
            strings.append('<attribute id="IsSustainedEmotion" type="bool" value="False" />')
        strings.append('</node>')
        return et.fromstring(''.join(strings))

    def create_look_at_key(
            self,
            time: str | dc.Decimal | float,
            /,
            target: str | None = None,
            bone: str | None = None,
            turn_mode: int | None = None,
            tracking_mode: int | None = None,
            turn_speed_multiplier: float | None = None,
            torso_turn_speed_multiplier: float | None = None,
            head_turn_speed_multiplier: float | None = None,
            weight: float | None = None,
            look_at_mode: int | None = None,
            look_at_interp_mode: int | None = None,
            eye_look_at_bone: str | None = None,
            eye_look_at_offset: tuple[float, float, float] | None = None,
            offset: tuple[float, float, float] | None = None,
            safe_zone_angle: float | None = None,
            head_safe_zone_angle: float | None = None,
            reset: bool = False,
            is_eye_look_at_enabled: bool = False,
            eye_look_at_target_id: str | None = None,
            interpolation_type: int = 3
    ) -> et.Element:
        if self.__current_phase_start_time is None:
            raise RuntimeError("new phase should be created before effect components")
        xml = ['<node id="Key">']
        abs_time = self.__current_phase_start_time + decimal_from(time)
        xml.append(f'<attribute id="Time" type="float" value="{abs_time}" />')
        xml.append(f'<attribute id="InterpolationType" type="uint8" value="{interpolation_type}" />')
        if target is not None:
            effective_target, _ = self.get_effective_actor(target)
            xml.append(f'<attribute id="Target" type="guid" value="{effective_target}" />')
        if bone is not None:
            xml.append(f'<attribute id="Bone" type="FixedString" value="{bone}" />')
        if turn_mode is not None:
            xml.append(f'<attribute id="TurnMode" type="uint8" value="{turn_mode}" />')
        if tracking_mode is not None:
            xml.append(f'<attribute id="TrackingMode" type="uint8" value="{tracking_mode}" />')
        if turn_speed_multiplier is not None:
            xml.append(f'<attribute id="TurnSpeedMultiplier" type="float" value="{turn_speed_multiplier}" />')
        if torso_turn_speed_multiplier is not None:
            xml.append(f'<attribute id="TorsoTurnSpeedMultiplier" type="float" value="{torso_turn_speed_multiplier}" />')
        if head_turn_speed_multiplier is not None:
            xml.append(f'<attribute id="HeadTurnSpeedMultiplier" type="float" value="{head_turn_speed_multiplier}" />')
        if weight is not None:
            xml.append(f'<attribute id="Weight" type="double" value="{weight}" />')
        if look_at_mode is not None:
            xml.append(f'<attribute id="LookAtMode" type="uint8" value="{look_at_mode}" />')
        if look_at_interp_mode is not None:
            xml.append(f'<attribute id="LookAtInterpMode" type="uint8" value="{look_at_interp_mode}" />')
        if eye_look_at_bone is not None:
            xml.append(f'<attribute id="EyeLookAtBone" type="FixedString" value="{eye_look_at_bone}" />')
        if eye_look_at_offset is not None:
            xml.append(f'<attribute id="EyeLookAtOffset" type="fvec3" value="{eye_look_at_offset[0]} {eye_look_at_offset[1]} {eye_look_at_offset[2]}" />')
        if offset is not None:
            xml.append(f'<attribute id="Offset" type="fvec3" value="{offset[0]} {offset[1]} {offset[2]}" />')
        if safe_zone_angle is not None:
            xml.append(f'<attribute id="SafeZoneAngle" type="double" value="{safe_zone_angle}" />')
        if head_safe_zone_angle is not None:
            xml.append(f'<attribute id="HeadSafeZoneAngle" type="double" value="{head_safe_zone_angle}" />')
        if reset:
            xml.append(f'<attribute id="Reset" type="bool" value="True" />')
        if is_eye_look_at_enabled:
            xml.append(f'<attribute id="IsEyeLookAtEnabled" type="bool" value="True" />')
        if eye_look_at_target_id is not None:
            effective_target, _ = self.get_effective_actor(eye_look_at_target_id)
            xml.append(f'<attribute id="EyeLookAtTargetId" type="guid" value="{effective_target}" />')
        xml.append("</node>")
        return et.fromstring("".join(xml))

    def create_sound_event_key(
            self,
            time: str | dc.Decimal | float,
            /,
            sound_event_id: str | None = None,
            sound_object_index: int | None = None,
            sound_type: int | None = None,
            vocal_type: int | None = None,
            foley_type: int | None = None,
            foley_intensity: int | None = None,
            interpolation_type: int = 3
    ) -> et.Element:
        if self.__current_phase_start_time is None:
            raise RuntimeError("new phase should be created before effect components")        
        strings = [
            f'<node id="Key"><attribute id="Time" type="float" value="{self.__current_phase_start_time + decimal_from(time)}" />',
            f'<attribute id="InterpolationType" type="uint8" value="{interpolation_type}" />'
        ]
        if sound_event_id is not None:
            strings.append(f'<attribute id="SoundEventID" type="guid" value="{sound_event_id}" />')
        if sound_object_index is not None:
            strings.append(f'<attribute id="SoundObjectIndex" type="uint8" value="{sound_object_index}" />')
        if sound_type is not None:
            strings.append(f'<attribute id="SoundType" type="uint8" value="{sound_type}" />')
        if vocal_type is not None:
            strings.append(f'<attribute id="VocalType" type="uint8" value="{vocal_type}" />')
        if foley_type is not None:
            strings.append(f'<attribute id="FoleyType" type="uint8" value="{foley_type}" />')
        if foley_intensity is not None:
            strings.append(f'<attribute id="FoleyIntensity" type="uint8" value="{foley_intensity}" />')
            
        strings.append('</node>')
        return et.fromstring(''.join(strings))

    def create_value_key(
            self,
            /,
            value: bool | float | dc.Decimal | int | Iterable | str | None = None,
            value_name: str | None = None,
            value_type: str | None = None,
            time: str | dc.Decimal | float | None = None,
            interpolation_type: int | None = None
    ) -> et.Element:
        if self.__current_phase_start_time is None:
            raise RuntimeError("new phase should be created before effect components")
        xml = ['<node id="Key">']
        if value_name is None:
            value_name = "Value"
        if isinstance(value_type, str):
            xml.append(f'<attribute id="{value_name}" type="{value_type}" value="{value}" />')
        elif isinstance(value, bool):
            xml.append(f'<attribute id="{value_name}" type="bool" value="{value}" />')
        elif isinstance(value, float) or isinstance(value, int) or isinstance(value, dc.Decimal):
            xml.append(f'<attribute id="{value_name}" type="float" value="{value}" />')
        elif isinstance(value, tuple | list) and get_len(value) == 3:
            xml.append(f'<attribute id="{value_name}" type="fvec3" value="{value[0]} {value[1]} {value[2]}" />')
        elif isinstance(value, tuple | list) and get_len(value) == 4:
            xml.append(f'<attribute id="{value_name}" type="fvec4" value="{value[0]} {value[1]} {value[2]} {value[3]}" />')
        elif value is None:
            pass
        else:
            raise RuntimeError(f"unexpected type of 'value' argument: {type(value)}")
        if time is not None:
            abs_time = self.__current_phase_start_time + decimal_from(time)
            xml.append(f'<attribute id="Time" type="float" value="{abs_time}" />')
        if interpolation_type is not None:
            xml.append(f'<attribute id="InterpolationType" type="uint8" value="{interpolation_type}" />')
        xml.append('</node>')
        return et.fromstring("".join(xml))

    def create_frame_of_reference_key(
            self,
            time: str | dc.Decimal | float,
            interpolation_type: int,
            target_uuid: str,
            target_bone: str,
            one_frame_only: bool,
            keep_scale: bool
    ) -> et.Element:
        if self.__current_phase_start_time is None:
            raise RuntimeError("new phase should be created before effect components")
        abs_time = self.__current_phase_start_time + decimal_from(time)
        effective_actor, _ = self.get_effective_actor(target_uuid)
        return et.fromstring(f'<node id="Key"><attribute id="Time" type="float" value="{abs_time}" />' +
                             f'<attribute id="InterpolationType" type="uint8" value="{interpolation_type}" />' +
                             '<children><node id="Value"><children><node id="frameOfReference">' +
                             f'<attribute id="targetId" type="guid" value="{effective_actor}" />' +
                             f'<attribute id="targetBone" type="FixedString" value="{target_bone}" />' +
                             f'<attribute id="OneFrameOnly" type="bool" value="{one_frame_only}" />' +
                             f'<attribute id="KeepScale" type="bool" value="{keep_scale}" />' +
                             '</node></children></node></children></node>')

    def create_switch_stage_event_key(
            self,
            time: str | dc.Decimal | float,
            /,
            interpolation_type: int = 3,
            event_uuid: str | None = None,
            force_transform_update: bool | None = None
    ) -> et.Element:
        if self.__current_phase_start_time is None:
            raise RuntimeError("new phase should be created before effect components")
        abs_time = self.__current_phase_start_time + decimal_from(time)
        xml = ['<node id="Key">',
               f'<attribute id="Time" type="float" value="{abs_time}" />',
               f'<attribute id="InterpolationType" type="uint8" value="{interpolation_type}" />']
        if event_uuid is not None:
            xml.append(f'<attribute id="SwitchStageEventID" type="guid" value="{event_uuid}" />')
        if force_transform_update is not None:
            xml.append(f'<attribute id="ForceTransformUpdate" type="bool" value="{force_transform_update}" />')
        xml.append('</node>')
        return et.fromstring(''.join(xml))
        
    def create_switch_location_event_key(
            self,
            time: str | dc.Decimal | float,
            interpolation_type: int,
            event_uuid: str | None
    ) -> et.Element:
        if self.__current_phase_start_time is None:
            raise RuntimeError("new phase should be created before effect components")
        abs_time = self.__current_phase_start_time + decimal_from(time)
        if event_uuid is None:
            return et.fromstring(f'<node id="Key"><attribute id="Time" type="float" value="{abs_time}" />' +
                                 f'<attribute id="InterpolationType" type="uint8" value="{interpolation_type}" /></node>')
        else:
            return et.fromstring(f'<node id="Key"><attribute id="Time" type="float" value="{abs_time}" />' +
                                 f'<attribute id="InterpolationType" type="uint8" value="{interpolation_type}" />' +
                                 f'<attribute id="SwitchLocationEventID" type="guid" value="{event_uuid}" /></node>')

    def create_material_parameter(
            self,
            parameter_name: str,
            keys: Iterable[et.Element]
    ) -> et.Element:
        if self.__current_phase_start_time is None:
            raise RuntimeError("new phase should be created before effect components")
        elt = et.fromstring(f'<node id="Node"><attribute id="MaterialParameterName" type="FixedString" value="{parameter_name}" /><children>' +
                            '<node id="MaterialParameter"><children><node id="Keys"><children></children></node></children></node></children></node>')
        keys_children = elt.find('./children/node[@id="MaterialParameter"]/children/node[@id="Keys"]/children')
        if keys_children is None:
            raise RuntimeError(f'bad material parameter: {to_compact_string(elt)}')
        for key in keys:
            keys_children.append(key)
        return elt

    def create_simple_dialog_answer_phase(
            self,
            speaker: str,
            voice_duration: str | dc.Decimal,
            dialog_node_uuid: str,
            shots: Iterable[tuple[str | dc.Decimal | None, int | str]],
            /,
            voice_delay: str | dc.Decimal | None = None,
            phase_duration: str | dc.Decimal | None = None,
            line_index: int | None = None,
            emotions: dict[str, Iterable[tuple[float | str, int, int | None]]] | None = None,
            attitudes: dict[str, Iterable[tuple[float | str, str, str, int | None]]] | None = None,
            speaker_player: str = SPEAKER_PLAYER,
            look_at_player: str | None = None,
            peanut_override: bool = False,
            disable_mocap: bool = False,
            fade_in: float = 0.0,
            fade_out: float = 0.0,
            performance_fade: float = 0.0
    ) -> None:
        if phase_duration is None:
            phase_duration = voice_duration
        if look_at_player is None:
            look_at_player = speaker
        start = DECIMAL_ZERO
        voice_start = start if voice_delay is None else decimal_from_str(voice_delay)
        end = decimal_from_str(phase_duration)
        self.create_new_phase(dialog_node_uuid, phase_duration, line_index=line_index)
        self.create_tl_voice(
            speaker,
            voice_start,
            voice_start + decimal_from_str(voice_duration),
            dialog_node_uuid,
            line_index = line_index,
            is_snapped_to_end = True,
            peanut_override = peanut_override,
            fade_in = fade_in,
            fade_out = fade_out,
            performance_fade = performance_fade,
            disable_mocap = disable_mocap)

        self.create_tl_actor_node(timeline_object.LOOK_AT, speaker_player, DECIMAL_ZERO, phase_duration, (
            self.create_look_at_key(
                DECIMAL_ZERO,
                target = look_at_player,
                bone = 'Head_M',
                turn_mode = 3,
                turn_speed_multiplier = 0.3,
                head_turn_speed_multiplier = 0.3,
                weight = 0.3,
                reset = True,
                is_eye_look_at_enabled = True,
                eye_look_at_target_id = speaker,
                eye_look_at_bone = 'Head_M'
            ),
        ), is_snapped_to_end = True)
        self.create_tl_actor_node(timeline_object.LOOK_AT, speaker, DECIMAL_ZERO, phase_duration, (
            self.create_look_at_key(
                DECIMAL_ZERO,
                target = speaker_player,
                bone = 'Head_M',
                turn_mode = 3,
                turn_speed_multiplier = 0.3,
                head_turn_speed_multiplier = 0.3,
                weight = 0.3,
                reset = True,
                is_eye_look_at_enabled = True,
                eye_look_at_target_id = speaker_player,
                eye_look_at_bone = 'Head_M'
            ),
        ), is_snapped_to_end = True)

        if emotions is not None:
            for target, emotion_records in emotions.items():
                emotion_keys = list[et.Element]()
                for emotion_record in emotion_records:
                    emotion_keys.append(self.create_emotion_key(str(emotion_record[0]), emotion_record[1], variation = emotion_record[2]))
                self.create_tl_actor_node(timeline_object.EMOTION, target, start, end, emotion_keys, is_snapped_to_end=True)
        if attitudes is not None:
            for target, attitude_records in attitudes.items():
                attitude_keys = list[et.Element]()
                for attitude_record in attitude_records:
                    interpolation_type = 3 if attitude_record[3] is None else attitude_record[3]
                    attitude_keys.append(
                        self.create_attitude_key(
                            str(attitude_record[0]),
                            attitude_record[1],
                            attitude_record[2],
                            interpolation_type = interpolation_type))
                self.create_tl_actor_node(timeline_object.ATTITUDE, target, start, end, attitude_keys, is_snapped_to_end = True)
        else:
            self.create_tl_actor_node(timeline_object.ATTITUDE, speaker, start, end, (
                self.create_attitude_key(start, ATTITUDE_DIAG_Pose_Stand_R_Forward_01, ATTITUDE_DIAG_T_Pose),
            ), is_snapped_to_end = True)
            self.create_tl_actor_node(timeline_object.ATTITUDE, speaker_player, start, end, (
                self.create_attitude_key(start, ATTITUDE_DIAG_Pose_Stand_L_Forward_01, ATTITUDE_DIAG_T_Pose),
            ), is_snapped_to_end = True)
        shot_start = start
        for shot in shots:
            if shot_start >= end:
                raise RuntimeError(f"duration of TLShot exceeds phase duration: {shot_start} >= {phase_duration}")
            shot_end = shot[0]
            camera = shot[1]
            if shot_end is None:
                self.create_tl_shot(camera, shot_start, phase_duration, is_snapped_to_end=True)
                shot_start = end
            else:
                shot_end = decimal_from_str(shot_end)
                self.create_tl_shot(camera, shot_start, shot_end)
                shot_start = shot_end

    def remove_effect_component(self, effect_component: str | et.Element[str]) -> None:
        if isinstance(effect_component, str):
            self.__effect_components_parent_node.remove(self.find_effect_component(effect_component))
        else:
            self.__effect_components_parent_node.remove(effect_component)

    def get_timeline_phase_index(self, dialog_node_uuid: str) -> int | None:
        tl_voice_nodes = self.find_effect_components(effect_component_types = 'TLVoice')
        for tl_voice in tl_voice_nodes:
            phase_index = get_bg3_attribute(tl_voice, 'PhaseIndex')
            if phase_index is None:
                phase_index = 0
            else:
                phase_index = int(phase_index)
            if dialog_node_uuid == get_required_bg3_attribute(tl_voice, 'DialogNodeId') or dialog_node_uuid == get_required_bg3_attribute(tl_voice, 'ReferenceId'):
                return phase_index
        timeline_phases = self.__file.root_node.findall('./region[@id="TimelineContent"]/node[@id="TimelineContent"]/children/node[@id="TimelinePhases"]/children/node[@id="Object"]/children/node[@id="Object"]')
        for timeline_phase in timeline_phases:
            if dialog_node_uuid == get_required_bg3_attribute(timeline_phase, 'MapKey'):
                return int(get_required_bg3_attribute(timeline_phase, 'MapValue'))
        return None

    def get_number_of_phases(self) -> int:
        return len(self.__phases_durations)

    def get_timeline_phase(self, phase_id: str | int) -> timeline_phase:
        phases = self.__file.root_node.findall('./region[@id="TimelineContent"]/node[@id="TimelineContent"]/children/node[@id="Effect"]/children/node[@id="Phases"]/children/node[@id="Phase"]')
        timeline_phases = self.__file.root_node.findall('./region[@id="TimelineContent"]/node[@id="TimelineContent"]/children/node[@id="TimelinePhases"]/children/node[@id="Object"]/children/node[@id="Object"]')
        for tl_phase in timeline_phases:
            map_key = get_required_bg3_attribute(tl_phase, "MapKey")
            map_value = int(get_required_bg3_attribute(tl_phase, "MapValue"))
            if (isinstance(phase_id, str) and phase_id == map_key) or (isinstance(phase_id, int) and phase_id == map_value):
                dialog_uuid = get_required_bg3_attribute(phases[map_value], "DialogNodeId")
                return timeline_phase(map_value, dialog_uuid, map_key, self.__phases_start_times[map_value], self.__phases_end_times[map_value])
        raise KeyError(f"failed to find a phase with id {phase_id} in timeline {self.__file.relative_file_path}")

    def find_effect_component(self, effect_component_uuid: str) -> et.Element[str]:
        effect_components = self.__effect_components_parent_node.findall('./node[@id="EffectComponent"]')
        for effect_component in effect_components:
            if get_required_bg3_attribute(effect_component, "ID") == effect_component_uuid:
                return effect_component
        raise KeyError(f"effect component {effect_component_uuid} is not found in {self.__file.relative_file_path}")

    def find_effect_components(
            self,
            /,
            effect_component_types: str | set[str] | None = None,
            actor: str | None = None,
            phase_index: int | None = None
    ) -> list[et.Element[str]]:
        result = []
        effect_components = self.__effect_components_parent_node.findall('./node[@id="EffectComponent"]')
        if actor is not None:
            effective_actor, _ = self.get_effective_actor(actor)
        else:
            effective_actor = None
        for effect_component in effect_components:
            if effect_component_types is not None:
                ct = get_required_bg3_attribute(effect_component, "Type")
                if isinstance(effect_component_types, str) and ct != effect_component_types:
                    continue
                if isinstance(effect_component_types, set) and ct not in effect_component_types:
                    continue
            if effective_actor is not None:
                actor_node = effect_component.find('./children/node[@id="Actor"]')
                if actor_node is None or get_bg3_attribute(actor_node, "UUID") != effective_actor:
                    continue
            if phase_index is not None:
                comp_phase_idx = get_bg3_attribute(effect_component, 'PhaseIndex')
                if comp_phase_idx is None:
                    comp_phase_idx = 0
                else:
                    comp_phase_idx = int(comp_phase_idx)
                if phase_index != comp_phase_idx:
                    continue
            result.append(effect_component)
        return result

    def get_tl_node_start_end(self, node_uuid: str) -> tuple[str, str]:
        tl_node = self.find_effect_component(node_uuid)
        start_time = get_bg3_attribute(tl_node, 'StartTime')
        if start_time is None:
            start_time = '0.0'
        end_time = get_required_bg3_attribute(tl_node, 'EndTime')
        return start_time, end_time

    def get_tl_animation_target_transform_position(self, node: XmlElement | str) -> tuple[str, str, str]:
        if isinstance(node, str):
            node = self.find_effect_component(node)
        target_transform = node.find('./children/node[@id="TargetTransform"]')
        if target_transform is None:
            return ('', '', '')
        position = get_bg3_attribute(target_transform, 'Position')
        if position is None:
            return ('', '', '')
        coords = position.split(' ')
        if len(coords) != 3:
            return ('', '', '')
        return (coords[0], coords[1], coords[2])

    def set_tl_animation_target_transform_position(self, node: XmlElement | str, pos: tuple[str | float, str | float, str | float]) -> None:
        if isinstance(node, str):
            node = self.find_effect_component(node)
        target_transform = node.find('./children/node[@id="TargetTransform"]')
        if target_transform is None:
            id = get_required_bg3_attribute(node, 'ID')
            raise RuntimeError(f'TLAnimation node {id} does not have TargetTransform')
        set_bg3_attribute(target_transform, 'Position', f'{pos[0]} {pos[1]} {pos[2]}', attribute_type = 'fvec3')

    def get_tl_animation_target_transform_rotation(self, node: XmlElement | str) -> tuple[str, str, str, str]:
        if isinstance(node, str):
            node = self.find_effect_component(node)
        target_transform = node.find('./children/node[@id="TargetTransform"]')
        if target_transform is None:
            return ('', '', '', '')
        quaternion = get_bg3_attribute(target_transform, 'RotationQuat')
        if quaternion is None:
            return ('', '', '', '')
        quat_comps = quaternion.split(' ')
        if len(quat_comps) != 4:
            return ('', '', '', '')
        return (quat_comps[0], quat_comps[1], quat_comps[2], quat_comps[3])

    def set_tl_animation_target_transform_rotation(self, node: XmlElement | str, rot: tuple[str | float, str | float, str | float, str | float]) -> None:
        if isinstance(node, str):
            node = self.find_effect_component(node)
        target_transform = node.find('./children/node[@id="TargetTransform"]')
        if target_transform is None:
            id = get_required_bg3_attribute(node, 'ID')
            raise RuntimeError(f'TLAnimation node {id} does not have TargetTransform')
        set_bg3_attribute(target_transform, 'RotationQuat', f'{rot[0]} {rot[1]} {rot[2]} {rot[3]}', attribute_type = 'fvec4')

    def set_tl_animation_target_transform(
            self,
            node: XmlElement | str,
            position: tuple[str | float, str | float, str | float],
            rotation: tuple[str | float, str | float, str | float, str | float],
            scale: str | float
    ) -> None:
        if isinstance(node, str):
            node = self.find_effect_component(node)
        children = node.find('./children')
        if children is None:
            id = get_required_bg3_attribute(node, 'ID')
            raise RuntimeError(f'TLAnimation node {id} does not have children')
        target_transform = children.find('./node[@id="TargetTransform"]')
        pos = f'{position[0]} {position[1]} {position[2]}'
        rot = f'{rotation[0]} {rotation[1]} {rotation[2]} {rotation[3]}'
        if target_transform is None:
            children.append(et.fromstring(
                '<node id="TargetTransform">' +
                f'<attribute id="Scale" type="float" value="{scale}" />' +
                f'<attribute id="Position" type="fvec3" value="{pos}" />' +
                f'<attribute id="RotationQuat" type="fvec4" value="{rot}" />' +
                '</node>'))
        else:
            set_bg3_attribute(target_transform, 'Scale', scale, attribute_type = 'float')
            set_bg3_attribute(target_transform, 'Position', pos, attribute_type = 'fvec3')
            set_bg3_attribute(target_transform, 'RotationQuat', rot, attribute_type = 'fvec4')

    def remove_tl_animation_target_transform(self, node: XmlElement | str) -> None:
        if isinstance(node, str):
            node = self.find_effect_component(node)
        children = node.find('./children')
        if children:
            target_transform = children.find('./node[@id="TargetTransform"]')
            if target_transform:
                children.remove(target_transform)


    def edit_tl_animation(
            self,
            node_uuid: str,
            /,
            target_transform_scale: str | dc.Decimal | None = None,
            target_transform_position: tuple[str | dc.Decimal | float, str | dc.Decimal | float, str | dc.Decimal | float] | None = None,
            target_transform_rotation: tuple[str | dc.Decimal | float, str | dc.Decimal | float, str | dc.Decimal | float, str | dc.Decimal| float] | None = None,
    ) -> et.Element:
        tl_node = self.find_effect_component(node_uuid)
        target_transform = tl_node.find('./children/node[@id="TargetTransform"]')
        if target_transform is None:
            raise RuntimeError(f'animation node {node_uuid} does not have a target transform')
        if target_transform_scale is not None:
            set_bg3_attribute(target_transform, 'Scale', str(target_transform_scale), attribute_type = 'float')
        if target_transform_position is not None:
            val = f'{target_transform_position[0]} {target_transform_position[1]} {target_transform_position[2]}'
            set_bg3_attribute(target_transform, 'Position', val, attribute_type = 'fvec3')
        if target_transform_rotation is not None:
            val = f'{target_transform_rotation[0]} {target_transform_rotation[1]} {target_transform_rotation[2]} {target_transform_rotation[3]}'
            set_bg3_attribute(target_transform, 'RotationQuat', val, attribute_type = 'fvec4')
        return tl_node

    def get_tl_transform_position(self, node: XmlElement | str, index: int = 0) -> tuple[str, str, str]:
        if isinstance(node, str):
            node = self.find_effect_component(node)
        channels = node.findall('./children/node[@id="TransformChannels"]/children/node[@id="TransformChannel"]')
        if len(channels) == 0:
            return ('', '', '')
        if len(channels) != 6:
            id = get_required_bg3_attribute(node, 'ID')
            raise RuntimeError(f'Malformed TLTransform node: {id}')
        x_nodes = channels[0].findall('./children/node[@id="Keys"]/children/node[@id="Key"]')
        y_nodes = channels[1].findall('./children/node[@id="Keys"]/children/node[@id="Key"]')
        z_nodes = channels[2].findall('./children/node[@id="Keys"]/children/node[@id="Key"]')
        if len(x_nodes) <= index or len(y_nodes) <= index or len(z_nodes) <= index:
            return ('', '', '')
        return (
            get_required_bg3_attribute(x_nodes[index], 'Value'),
            get_required_bg3_attribute(y_nodes[index], 'Value'),
            get_required_bg3_attribute(z_nodes[index], 'Value'))

    def set_tl_transform_position(self, node: XmlElement | str, pos: tuple[str | float, str | float, str | float], index: int = 0) -> None:
        if isinstance(node, str):
            node = self.find_effect_component(node)
        channels = node.findall('./children/node[@id="TransformChannels"]/children/node[@id="TransformChannel"]')
        if len(channels) != 6:
            id = get_required_bg3_attribute(node, 'ID')
            raise RuntimeError(f'Malformed TLTransform node: {id}')
        x_nodes = channels[0].findall('./children/node[@id="Keys"]/children/node[@id="Key"]')
        y_nodes = channels[1].findall('./children/node[@id="Keys"]/children/node[@id="Key"]')
        z_nodes = channels[2].findall('./children/node[@id="Keys"]/children/node[@id="Key"]')
        if len(x_nodes) <= index or len(y_nodes) <= index or len(z_nodes) <= index:
            id = get_required_bg3_attribute(node, 'ID')
            raise RuntimeError(f'No position is defined in TLTransform node {id} for index {index}')
        set_bg3_attribute(x_nodes[index], 'Value', pos[0], attribute_type = 'float')
        set_bg3_attribute(y_nodes[index], 'Value', pos[1], attribute_type = 'float')
        set_bg3_attribute(z_nodes[index], 'Value', pos[2], attribute_type = 'float')

    def get_tl_transform_coordinate(self, node: XmlElement | str, channel_index: int, index: int = 0) -> str:
        if isinstance(node, str):
            node = self.find_effect_component(node)
        channels = node.findall('./children/node[@id="TransformChannels"]/children/node[@id="TransformChannel"]')
        if len(channels) == 0:
            return ''
        if len(channels) != 6:
            id = get_required_bg3_attribute(node, 'ID')
            raise RuntimeError(f'Malformed TLTransform node: {id}')
        nodes = channels[channel_index].findall('./children/node[@id="Keys"]/children/node[@id="Key"]')
        if len(nodes) <= index:
            return ''
        return get_required_bg3_attribute(nodes[index], 'Value')

    def set_tl_transform_coordinate(self, node: XmlElement | str, channel_index: int, val: str, index: int = 0, val_type : str = 'float') -> None:
        if isinstance(node, str):
            node = self.find_effect_component(node)
        channels = node.findall('./children/node[@id="TransformChannels"]/children/node[@id="TransformChannel"]')
        if len(channels) == 0:
            return
        if len(channels) != 6:
            id = get_required_bg3_attribute(node, 'ID')
            raise RuntimeError(f'Malformed TLTransform node: {id}')
        nodes = channels[channel_index].findall('./children/node[@id="Keys"]/children/node[@id="Key"]')
        if len(nodes) <= index:
            id = get_required_bg3_attribute(node, 'ID')
            raise RuntimeError(f'No position is defined in TLTransform node {id} for channel {channel_index} and index {index}')
        set_bg3_attribute(nodes[index], 'Value', val, attribute_type = val_type)

    def edit_tl_transform(
            self,
            node_uuid: str,
            /,
            actor: str | None = None,
            start: str | dc.Decimal | None = None,
            end: str | dc.Decimal | None = None,
            channels: Iterable[Iterable[et.Element]] | None = None,
            continuous: bool = False,
            is_snapped_to_end: bool = False
    ) -> et.Element:
        if self.__current_phase_start_time is None:
            raise RuntimeError("new phase should be created before effect components")
        tl_node = self.find_effect_component(node_uuid)
        tl_phase = self.get_phase_by_tl_node(tl_node)
        phase_start_time = tl_phase.start
        if actor is not None:
            actor_node = tl_node.find('./children/node[@id="Actor"]')
            if actor_node is None:
                raise RuntimeError(f"bad timeline object {node_uuid}, cannot find the Actor node")
            effective_actor, _ = self.get_effective_actor(actor)
            set_bg3_attribute(actor_node, "UUID", effective_actor)
        if start is not None:
            start_time = phase_start_time + decimal_from_str(start)
            set_bg3_attribute(tl_node, "StartTime", str(start_time), attribute_type="float")
        if end is not None:
            end_time = phase_start_time + decimal_from_str(end)
            set_bg3_attribute(tl_node, "EndTime", str(end_time), attribute_type="float")
        if continuous:
            set_bg3_attribute(tl_node, "Continuous", "True", attribute_type="bool")
        if is_snapped_to_end:
            set_bg3_attribute(tl_node, "IsSnappedToEnd", "True", attribute_type="bool")
        if channels is not None:
            transform_channels = et.fromstring('<node id="TransformChannels"><children></children></node>')
            transform_channels_children = transform_channels.find('./children')
            if transform_channels_children is None:
                raise RuntimeError('impossible: children node not found')
            for channel in channels:
                if get_len(channel) == 0:
                    transform_channels_children.append(et.fromstring('<node id="TransformChannel" />'))
                else:
                    channel_node = et.fromstring('<node id="TransformChannel"><children><node id="Keys"><children></children></node></children></node>')
                    channel_node_keys_children = channel_node.find('./children/node[@id="Keys"]/children')
                    if channel_node_keys_children is None:
                        raise RuntimeError('channel_node_keys_children is None')
                    for key in channel:
                        time = get_bg3_attribute(key, 'Time')
                        if time is not None:
                            time_val = decimal_from_str(time) + self.__current_phase_start_time
                            set_bg3_attribute(key, 'Time', str(time_val), attribute_type = 'float')
                        channel_node_keys_children.append(key)
                    transform_channels_children.append(channel_node)
            tl_node_children = tl_node.find('./children')
            if tl_node_children is None:
                raise RuntimeError('unexpected: children node not found')
            old_transform_channels = tl_node_children.find('./node[@id="TransformChannels"]')
            if old_transform_channels is not None:
                tl_node_children.remove(old_transform_channels)
            tl_node_children.append(transform_channels)
        return tl_node

    def edit_tl_camera_fov(
            self,
            node_uuid: str,
            /,
            start: str | dc.Decimal | None = None,
            end: str | dc.Decimal | None = None,
            camera_uuid: str | None = None,
            keys: Iterable[et.Element] | None = None
    ) -> None:
        tl_node = self.find_effect_component(node_uuid)
        tl_phase = self.get_phase_by_tl_node(tl_node)
        phase_start_time = tl_phase.start
        tl_node = self.find_effect_component(node_uuid)
        if camera_uuid is not None:
            camera_node = tl_node.find('./children/node[@id="Actor"]')
            if camera_node is None:
                raise RuntimeError(f"bad timeline object {node_uuid}, cannot find the Actor node")
            set_bg3_attribute(camera_node, "UUID", camera_uuid)
        if start is not None:
            start_time = phase_start_time + decimal_from_str(start)
            set_bg3_attribute(tl_node, "StartTime", str(start_time), attribute_type="float")
        if end is not None:
            end_time = phase_start_time + decimal_from_str(end)
            set_bg3_attribute(tl_node, "EndTime", str(end_time), attribute_type="float")
        if keys is not None:
            children_node = tl_node.find('./children')
            if children_node is None:
                raise RuntimeError(f"bad TLCameraFoV object {node_uuid}, cannot find the children node")
            keys_node = children_node.find('./node[@id="Keys"]')
            if keys_node:
                children_node.remove(keys_node)
            keys_node = et.fromstring('<node id="Keys"><children></children></node>')
            children_node.append(keys_node)
            children_node = keys_node.find('./children')
            if children_node is None:
                raise RuntimeError(f"bad TLCameraFoV object {node_uuid}, cannot find the children node")
            for key in keys:
                children_node.append(key)

    def edit_tl_shot(
            self,
            node_uuid: str,
            /,
            start: str | dc.Decimal | None = None,
            end: str | dc.Decimal | None = None,
            camera_uuid: str | None = None,
            is_snapped_to_end: bool | None = None
    ) -> None:
        tl_node = self.find_effect_component(node_uuid)
        tl_phase = self.get_phase_by_tl_node(tl_node)
        phase_start_time = tl_phase.start
        tl_node = self.find_effect_component(node_uuid)
        if camera_uuid is not None:
            camera_node = tl_node.find('./children/node[@id="CameraContainer"]')
            if camera_node is None:
                raise RuntimeError(f"bad timeline object {node_uuid}, cannot find the Actor node")
            set_bg3_attribute(camera_node, "Object", camera_uuid)
        if start is not None:
            start_time = phase_start_time + decimal_from_str(start)
            set_bg3_attribute(tl_node, 'StartTime', str(start_time), attribute_type="float")
        if end is not None:
            end_time = phase_start_time + decimal_from_str(end)
            set_bg3_attribute(tl_node, 'EndTime', str(end_time), attribute_type="float")
        if is_snapped_to_end is not None:
            if is_snapped_to_end:
                set_bg3_attribute(tl_node, "IsSnappedToEnd", "True", attribute_type="bool")
            elif get_bg3_attribute(tl_node, "IsSnappedToEnd") is not None:
                delete_bg3_attribute(tl_node, "IsSnappedToEnd")

    def edit_tl_node_append_keys(self, node_uuid: str, keys: Iterable[XmlElement]) -> None:
        tl_node = self.find_effect_component(node_uuid)
        children = tl_node.find('./children')
        if children is None:
            raise RuntimeError(f'timeline node {node_uuid} has no children')
        keys_node = children.find('./node[@id="Keys"]')
        if keys_node is None:
            keys_node = et.fromstring('<node id="Keys"><children></children></node>')
            children.append(keys_node)
        keys_children = keys_node.find('./node/children')
        if keys_children is None:
            raise RuntimeError()
        for key in keys:
            keys_children.append(key)
        
    def edit_tl_node_set_keys(self, node_uuid: str, keys: Iterable[XmlElement]) -> None:
        tl_node = self.find_effect_component(node_uuid)
        children = tl_node.find('./children')
        if children is None:
            raise RuntimeError(f'timeline node {node_uuid} has no children')
        keys_node = children.find('./node[@id="Keys"]')
        if keys_node is not None:
            children.remove(keys_node)
        keys_node = et.fromstring('<node id="Keys"><children></children></node>')
        keys_children = keys_node.find('./children')
        if keys_children is None:
            raise RuntimeError()
        for key in keys:
            keys_children.append(key)
        children.append(keys_node)

    def edit_tl_node(
            self,
            node_uuid: str,
            /,
            start: str | dc.Decimal | None = None,
            end: str | dc.Decimal | None = None,
            fade_in: str | dc.Decimal | None = None,
            fade_out: str | dc.Decimal | None = None,
            is_snapped_to_end: bool | None = None
    ) -> None:
        tl_node = self.find_effect_component(node_uuid)
        tl_phase = self.get_phase_by_tl_node(tl_node)
        phase_start_time = tl_phase.start
        phase_end_time = tl_phase.end
        if start is not None:
            start_time = phase_start_time + decimal_from_str(start)
            set_bg3_attribute(tl_node, 'StartTime', str(start_time), attribute_type = "float")
        if end is not None:
            end_time = phase_start_time + decimal_from_str(end)
            set_bg3_attribute(tl_node, 'EndTime', str(end_time), attribute_type = "float")
        if fade_in is not None:
            set_bg3_attribute(tl_node, 'FadeIn', str(fade_in), attribute_type = 'double')
        if fade_out is not None:
            set_bg3_attribute(tl_node, 'FadeOut', str(fade_out), attribute_type = 'double')
        if is_snapped_to_end is not None:
            if is_snapped_to_end:
                set_bg3_attribute(tl_node, "IsSnappedToEnd", "True", attribute_type = "bool")
            elif get_bg3_attribute(tl_node, "IsSnappedToEnd") is not None:
                delete_bg3_attribute(tl_node, "IsSnappedToEnd")


    def get_emotions(self, speaker: str, target_text_handle: str) -> list[tuple[str, int, int]]:
        custom_seq_id = None
        dialog_node_uuid = None
        for dialog_node in self.__dialog.get_dialog_nodes():
            texts = dialog_node.findall('./children/node[@id="TaggedTexts"]/children/node[@id="TaggedText"]/children/node[@id="TagTexts"]/children/node[@id="TagText"]')
            for text in texts:
                text_handle = get_required_bg3_attribute(text, 'TagText', value_name = 'handle')
                if target_text_handle == text_handle:
                    custom_seq_id = get_bg3_attribute(text, 'CustomSequenceId')
                    dialog_node_uuid = get_required_bg3_attribute(dialog_node, 'UUID')
                    break
            if dialog_node_uuid is not None:
                break
        tp = None
        if custom_seq_id:
            tp = self.get_timeline_phase(custom_seq_id)
        if tp is None and dialog_node_uuid is not None:
            tp = self.get_timeline_phase(dialog_node_uuid)
        if tp is None:
            raise RuntimeError(f'cannot find phase that contains text handle {target_text_handle}')
        voice_comps = self.find_effect_components(effect_component_types = 'TLVoice', phase_index = tp.index)
        emo_comps = self.find_effect_components(effect_component_types = 'TLEmotionEvent', phase_index = tp.index)

        tl_voice = None
        tl_emo = None

        if len(voice_comps) > 1:
            if custom_seq_id is not None:
                for voice_comp in voice_comps:
                    reference_id = get_required_bg3_attribute(voice_comp, 'ReferenceId')
                    if custom_seq_id == reference_id:
                        tl_voice = voice_comp
                        break
            if tl_voice is None:
                for voice_comp in voice_comps:
                    dialog_node_id = get_bg3_attribute(voice_comp, 'DialogNodeId')
                    if dialog_node_id == dialog_node_uuid:
                        tl_voice = voice_comp
                        break
        else:
            tl_voice = voice_comps[0]
        if tl_voice is None:
            raise RuntimeError(f'cannot find dialog for text handle {target_text_handle}')

        effective_speaker, _ = self.get_effective_actor(speaker)
        for emo_comp in emo_comps:
            actor_node = emo_comp.find('./children/node[@id="Actor"]')
            if actor_node is not None:
                emo_comp_actor = get_required_bg3_attribute(actor_node, 'UUID')
                if emo_comp_actor == effective_speaker or emo_comp_actor == speaker:
                    tl_emo = emo_comp
                    break
        if tl_emo is None:
            raise RuntimeError(f'cannot find emoton node for speaker {speaker}')

        start_time = get_bg3_attribute(tl_voice, 'StartTime')
        t0 = DECIMAL_ZERO
        if start_time is not None:
            t0 = decimal_from_str(start_time)
        t1 = decimal_from_str(get_required_bg3_attribute(tl_voice, 'EndTime'))

        result = list[tuple[str, int, int]]()
        emo_keys = tl_emo.findall('./children/node[@id="Keys"]/children/node[@id="Key"]')
        for emo_key in emo_keys:
            emo_time = get_bg3_attribute(emo_key, 'Time')
            if emo_time is None:
                t = DECIMAL_ZERO
            else:
                t = decimal_from_str(emo_time)
            if t < t0 or t > t1:
                continue
            t = t - tp.start
            emotion = get_bg3_attribute(emo_key, 'Emotion')
            if emotion is None:
                emotion = '0'
            variation = get_bg3_attribute(emo_key, 'Variation')
            if variation is None:
                variation = '0'
            result.append((str(t), int(emotion), int(variation)))
        return result

    def get_node_duration(self, node_uuid: str) -> dc.Decimal:
        tl_node = self.find_effect_component(node_uuid)
        start_time = get_bg3_attribute(tl_node, 'StartTime')
        if start_time is None:
            start_time = DECIMAL_ZERO
        end_time = get_required_bg3_attribute(tl_node, 'EndTime')
        return decimal_from_str(end_time) - decimal_from_str(start_time)

    def get_node_relative_start_time(self, node_uuid: str) -> dc.Decimal:
        tl_node = self.find_effect_component(node_uuid)
        start_time = get_bg3_attribute(tl_node, 'StartTime')
        phase_index = get_bg3_attribute(tl_node, 'PhaseIndex')
        if phase_index is None:
            phase_index = 0
        else:
            phase_index = int(phase_index)
        if start_time is None:
            start_time = DECIMAL_ZERO
        else:
            start_time = decimal_from_str(start_time) - self.get_timeline_phase(phase_index).start
        return start_time

    def get_node_relative_end_time(self, node_uuid: str) -> dc.Decimal:
        tl_node = self.find_effect_component(node_uuid)
        end_time = get_required_bg3_attribute(tl_node, 'EndTime')
        phase_index = get_bg3_attribute(tl_node, 'PhaseIndex')
        if phase_index is None:
            phase_index = 0
        else:
            phase_index = int(phase_index)
        end_time = decimal_from_str(end_time) - self.get_timeline_phase(phase_index).start
        return end_time

    def post_process(self) -> None:
        pass

    def create_scene_actor(
            self,
            actor_uuid: str,
            actor_params: dict[str, str],
            /,
            scale: float | None = None,
            position: tuple[float, float, float] | None = None,
            rotation: tuple[float, float, float, float] | None = None
    ) -> None:
        actors_root = self.xml.find('./region[@id="TimelineContent"]/node[@id="TimelineContent"]/children/node[@id="TimelineActorData"]/children/node[@id="TimelineActorData"]/children')
        if actors_root is None:
            raise RuntimeError(f'cannot add actor {actor_uuid} to {self.__file.relative_file_path}')
        actor_node = et.fromstring(f'<node id="Object" key="MapKey"><attribute id="MapKey" type="guid" value="{actor_uuid}" />'
                                   + '<children><node id="Value"><children><node id="CompiledNodeSnapshots">'
                                   + '<children><node id="ComponentMap" /></children></node></children></node></children></node>')
        attrs_node = actor_node.find('./children/node[@id="Value"]')
        if attrs_node is None:
            raise RuntimeError()
        for k, v in actor_params.items():
            name_type = k.split(':')
            set_bg3_attribute(attrs_node, name_type[0], v, attribute_type = name_type[1])
        actors_root.append(actor_node)
        if scale is not None or position is not None or rotation is not None:
            n = attrs_node.find('./children')
            if n is None:
                raise RuntimeError()
            if position is None:
                raise RuntimeError('position cannot be None')
            if scale is None:
                scale = 1.0
            if rotation is None:
                rotation = (0.0, 0.0, 0.0, 1.0)
            n.append(et.fromstringlist([
                '<node id="InitialTransform">',
                f'<attribute id="Scale" type="float" value="{scale}" />',
                f'<attribute id="Position" type="fvec3" value="{position[0]} {position[1]} {position[2]}" />',
                f'<attribute id="RotationQuat" type="fvec4" value="{rotation[0]} {rotation[1]} {rotation[2]} {rotation[3]}" />',
                '</node>',
            ]))

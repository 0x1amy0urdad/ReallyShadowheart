from __future__ import annotations

import os
import os.path
import xml.etree.ElementTree as et

from ._common import (
    delete_bg3_attribute,
    get_bg3_attribute,
    get_len,
    get_required_bg3_attribute,
    new_random_uuid,
    set_bg3_attribute,
    to_compact_string
)
from ._constants import REALLY_TAGS, SPEAKER_NARRATOR
from ._files import game_file
from ._flags import flag, flag_group
from ._types import XmlElement

from typing import Iterable

class speaker_flag:
    __speaker: str
    __uuid: str
    __value: bool

    def __init__(self, speaker: str, flag_uuid: str, value: bool) -> None:
        self.__speaker = speaker
        self.__uuid = flag_uuid
        self.__value = value

    @property
    def speaker(self) -> str:
        return self.__speaker

    @property
    def uuid(self) -> str:
        return self.__uuid

    @property
    def value(self) -> bool:
        return self.__value


class dialog_flag:
    __type: str
    __uuid: str
    __condition: bool
    __speaker_slot: int | None

    def __init__(self, type: str, uuid: str, condition: bool, /, speaker_slot: int | None = None) -> None:
        self.__type = type
        self.__uuid = uuid
        self.__condition = condition
        self.__speaker_slot = speaker_slot

    @property
    def flag_type(self) -> str:
        return self.__type

    @property
    def flag_uuid(self) -> str:
        return self.__uuid

    @property
    def condition(self) -> bool:
        return self.__condition

    @property
    def speaker_slot(self) -> int | None:
        return self.__speaker_slot


class text_content:
    __handle: str
    __version: int
    __line_id: str
    __custom_sequence_id: str | None

    def __init__(
            self,
            handle: str,
            version: int,
            line_id: str = '',
            /,
            custom_sequence_id: str | None = None,
    ) -> None:
        self.__handle = handle
        self.__version = version
        self.__line_id = line_id if len(line_id) > 0 else new_random_uuid()
        self.__custom_sequence_id = custom_sequence_id

    @property
    def handle(self) -> str:
        return self.__handle

    @property
    def version(self) -> int:
        return self.__version

    @property
    def line_id(self) -> str:
        return self.__line_id

    @property
    def custom_sequence_id(self) -> str | None:
        return self.__custom_sequence_id

    def to_xml(self) -> XmlElement:
        if self.__custom_sequence_id is None:
            return et.fromstring(f"""<node id="TagText">
                <attribute id="TagText" type="TranslatedString" handle="{self.__handle}" version="{self.__version}" />
                <attribute id="LineId" type="guid" value="{self.__line_id}" />
                <attribute id="stub" type="bool" value="True" /></node>\n""")
        else:
            return et.fromstring(f"""<node id="TagText">
                <attribute id="TagText" type="TranslatedString" handle="{self.__handle}" version="{self.__version}" />
                <attribute id="LineId" type="guid" value="{self.__line_id}" />
                <attribute id="CustomSequenceId" type="guid" value="{self.__custom_sequence_id}" />
                <attribute id="stub" type="bool" value="True" /></node>\n""")


class tagged_text_content:
    pass

class dialog_object:
    GREETING = 'TagGreeting'
    QUESTION = 'TagQuestion'
    ANSWER = 'TagAnswer'
    JUMP = 'Jump'
    ALIAS = 'Alias'

    ROLL_SKILL_CHECK = 'SkillCheck'
    ROLL_RAW_ABILITY = 'RawAbility'
    ROLL_ACTIVE = 'ActiveRoll'
    ROLL_PASSIVE = 'PassiveRoll'
    ABILITY_STRENGTH = 'Strength'
    ABILITY_DEXTERITY = 'Dexterity'
    ABILITY_CONSTITUTION = 'Constitution'
    ABILITY_INTELLIGENCE = 'Intelligence'
    ABILITY_WISDOM = 'Wisdom'
    ABILITY_CHARISMA = 'Charisma'
    SKILL_ATHLETICS = 'Athletics'
    SKILL_ACROBATICS = 'Acrobatics'
    SKILL_SLEIGHTOFHAND = 'SleightOfHand'
    SKILL_STEALTH = 'Stealth'
    SKILL_ARCANA = 'Arcana'
    SKILL_HISTORY = 'History'
    SKILL_INVESTIGATION = 'Investigation'
    SKILL_NATURE = 'Nature'
    SKILL_RELIGION = 'Religion'
    SKILL_ANIMALHANDLING = 'AnimalHandling'
    SKILL_INSIGHT = 'Insight'
    SKILL_MEDICINE = 'Medicine'
    SKILL_PERCEPTION = 'Perception'
    SKILL_SURVIVAL = 'Survival'
    SKILL_DECEPTION = 'Deception'
    SKILL_INTIMIDATION = 'Intimidation'
    SKILL_PERFORMANCE = 'Performance'
    SKILL_PERSUASION = 'Persuasion'

    __file: game_file
    __dialog_nodes_parent: XmlElement
    __dialog_nodes: dict[str, XmlElement]
    __speakers_slots: dict[str, tuple[int, str, bool]]

    def __init__(self, gamefile: game_file) -> None:
        self.__file = gamefile
        self.__speakers_slots = dict[str, tuple[int, str, bool]]()
        n = self.__file.root_node.find('./region[@id="dialog"]/node[@id="dialog"]/children/node[@id="nodes"]/children')
        if n is None:
            raise RuntimeError(f"file {gamefile.relative_file_path} doesn't contain a dialog")
        self.__dialog_nodes_parent = n
        self.__dialog_nodes = { get_required_bg3_attribute(n, "UUID") : n for n in self.get_dialog_nodes() }

    @property
    def dialog_file(self) -> game_file:
        return self.__file

    @property
    def filename(self) -> str:
        return self.__file.relative_file_path

    @property
    def xml(self) -> et.ElementTree[XmlElement]:
        return self.__file.xml

    @property
    def name(self) -> str:
        result = os.path.basename(self.__file.relative_file_path)
        return result[:result.find('.')]

    def get_dialog_nodes(self) -> list[XmlElement]:
        return self.__file.root_node.findall('./region[@id="dialog"]/node[@id="dialog"]/children/node[@id="nodes"]/children/node[@id="node"]')

    def get_speaker_slot_index(self, speaker_uuid: str) -> int:
        if speaker_uuid == SPEAKER_NARRATOR:
            return -666
        return self.get_speaker_slot(speaker_uuid)[0]

    def get_speaker_actor_uuid(self, speaker_uuid: str) -> str:
        if speaker_uuid == SPEAKER_NARRATOR:
            return SPEAKER_NARRATOR
        return self.get_speaker_slot(speaker_uuid)[1]

    def is_peanut_speaker(self, speaker_uuid: str) -> bool:
        return self.get_speaker_slot(speaker_uuid)[2]

    def has_speaker(self, speaker_uuid: str) -> bool:
        try:
            self.get_speaker_slot(speaker_uuid)
            return True
        except:
            pass
        return False

    def get_speakers(self) -> tuple[str, ...]:
        root_node = self.__file.root_node
        speaker_nodes = root_node.findall('./region[@id="dialog"]/node[@id="dialog"]/children/node[@id="speakerlist"]/children/node[@id="speaker"]')
        result = list[str]()
        for speaker_node in speaker_nodes:
            speaker_uuid = get_bg3_attribute(speaker_node, "list")
            if speaker_uuid:
                result.append(speaker_uuid)
            else:
                result.append('00000000-0000-0000-0000-000000000000')
        return tuple(result)

    def get_speaker_slot(self, speaker_uuid: str) -> tuple[int, str, bool]:
        if speaker_uuid in self.__speakers_slots:
            return self.__speakers_slots[speaker_uuid]
        root_node = self.__file.root_node
        speaker_nodes = root_node.findall('./region[@id="dialog"]/node[@id="dialog"]/children/node[@id="speakerlist"]/children/node[@id="speaker"]')
        for speaker_node in speaker_nodes:
            if get_bg3_attribute(speaker_node, "list") == speaker_uuid:
                index = int(get_required_bg3_attribute(speaker_node, "index"))
                actor_uuid = get_required_bg3_attribute(speaker_node, "SpeakerMappingId")
                is_peanut_speaker = get_bg3_attribute(speaker_node, 'IsPeanutSpeaker') == 'True'
                slot = (index, actor_uuid, is_peanut_speaker)
                self.__speakers_slots[speaker_uuid] = slot
                return slot
        raise ValueError(f"speaker {speaker_uuid} is not found in dialog {self.__file.relative_file_path}")

    def get_speaker_by_index(self, speaker_index: int) -> str:
        root_node = self.__file.root_node
        speaker_nodes = root_node.findall('./region[@id="dialog"]/node[@id="dialog"]/children/node[@id="speakerlist"]/children/node[@id="speaker"]')
        for speaker_node in speaker_nodes:
            if int(get_required_bg3_attribute(speaker_node, "index")) == speaker_index:
                return get_required_bg3_attribute(speaker_node, 'list')
        raise ValueError(f"speaker index {speaker_index} is not found in dialog {self.__file.relative_file_path}")

    def create_speaker_flag_group(self, speaker_flags: Iterable[speaker_flag]) -> flag_group:
        return flag_group(
            flag_group.OBJECT,
            [flag(sf.uuid, sf.value, speaker_index=self.get_speaker_slot_index(sf.speaker)) for sf in speaker_flags])

    def get_child_dialog_node_index(self, parent_node_uuid: str, child_node_uuid: str) -> int:
        node = self.find_dialog_node(parent_node_uuid)
        if node is None:
            raise RuntimeError(f"node {parent_node_uuid} doesn't exist in dialog {self.__file.relative_file_path}")
        node_children = node.find('./children/node[@id="children"]/children')
        if node_children is None:
            raise ValueError(f"children node {child_node_uuid} doesn't exist in node {parent_node_uuid} in dialog {self.__file.relative_file_path}")
        children_nodes = node_children.findall('./node[@id="child"]')
        index = 0
        for child_node in children_nodes:
            if get_required_bg3_attribute(child_node, "UUID") == child_node_uuid:
                return index
            index += 1
        raise ValueError(f"children node {child_node_uuid} doesn't exist in node {parent_node_uuid} in dialog {self.__file.relative_file_path}")

    def add_child_dialog_node(self, parent_node_uuid: str, child_node_uuid: str, index: int = -1) -> None:
        node = self.find_dialog_node(parent_node_uuid)
        if node is None:
            raise RuntimeError(f"node {parent_node_uuid} doesn't exist in dialog {self.__file.relative_file_path}")
        node_children = node.find('./children/node[@id="children"]/children')
        if node_children is None:
            node_children = node.find('./children/node[@id="children"]')
            if node_children is None:
                raise ValueError(f"inconsistent dialog node {parent_node_uuid} in dialog {self.__file.relative_file_path}")
            node_children.append(et.fromstring(f'<children><node id="child"><attribute id="UUID" type="FixedString" value="{child_node_uuid}" /></node></children>'))
            return
        children_nodes = node_children.findall('./node[@id="child"]')
        element = et.fromstring(f'<node id="child"><attribute id="UUID" type="FixedString" value="{child_node_uuid}" /></node>')
        if index == -1 or index >= len(children_nodes):
            node_children.append(element)
        else:
            node_children.insert(index, element)

    def add_child_dialog_node_before(self, parent_node_uuid: str, child_node_uuid: str, existing_node_uuid: str) -> None:
        idx = self.get_child_dialog_node_index(parent_node_uuid, existing_node_uuid)
        self.add_child_dialog_node(parent_node_uuid, child_node_uuid, idx)

    def add_child_dialog_node_after(self, parent_node_uuid: str, child_node_uuid: str, existing_node_uuid: str) -> None:
        idx = self.get_child_dialog_node_index(parent_node_uuid, existing_node_uuid)
        self.add_child_dialog_node(parent_node_uuid, child_node_uuid, idx + 1)

    def delete_child_dialog_node(self, parent_node_uuid: str, child_node_uuid: str) -> None:
        node = self.find_dialog_node(parent_node_uuid)
        if node is None:
            raise RuntimeError(f"node {parent_node_uuid} doesn't exist in dialog {self.__file.relative_file_path}")
        node_children = node.find('./children/node[@id="children"]/children')
        if node_children is None:
            raise ValueError(f"children node {child_node_uuid} doesn't exist in node {parent_node_uuid} in dialog {self.__file.relative_file_path}")
        children_nodes = node_children.findall('./node[@id="child"]')
        for child_node in children_nodes:
            if get_required_bg3_attribute(child_node, "UUID") == child_node_uuid:
                node_children.remove(child_node)
                return
        raise ValueError(f"children node {child_node_uuid} doesn't exist in node {parent_node_uuid} in dialog {self.__file.relative_file_path}")

    def delete_all_children_dialog_nodes(self, parent_node_uuid: str) -> None:
        node = self.find_dialog_node(parent_node_uuid)
        if node is None:
            raise RuntimeError(f"node {parent_node_uuid} doesn't exist in dialog {self.__file.relative_file_path}")
        node_children = node.find('./children/node[@id="children"]/children')
        if node_children is None:
            raise ValueError(f"children nodes don't exist in node {parent_node_uuid} in dialog {self.__file.relative_file_path}")
        children_nodes = node_children.findall('./node[@id="child"]')
        for child_node in children_nodes:
            node_children.remove(child_node)

    def set_dialog_flags(self, node_uuid: str, setflags: Iterable[flag_group] | None = None, checkflags: Iterable[flag_group] | None = None) -> None:
        node = self.find_dialog_node(node_uuid)
        if setflags is not None:
            setflags_node = node.find('./children/node[@id="setflags"]')
            if setflags_node is None:
                raise ValueError(f"bad dialog node {node_uuid}: 'setflags' node doesn't exist")
            setflags_children_node = setflags_node.find('children')
            if setflags_children_node is not None:
                setflags_node.remove(setflags_children_node)
            setflags_children_node = et.fromstring('<children></children>')
            setflags_node.append(setflags_children_node)
            for fg in setflags:
                setflags_children_node.append(fg.to_xml())
        if checkflags is not None:
            checkflags_node = node.find('./children/node[@id="checkflags"]')
            if checkflags_node is None:
                raise ValueError(f"bad dialog node {node_uuid}: 'checkflags' node doesn't exist")
            checkflags_children_node = checkflags_node.find('children')
            if checkflags_children_node is not None:
                checkflags_node.remove(checkflags_children_node)
            checkflags_children_node = et.fromstring('<children></children>')
            checkflags_node.append(checkflags_children_node)
            for fg in checkflags:
                checkflags_children_node.append(fg.to_xml())

    def add_dialog_flags(self, node_uuid: str, setflags: Iterable[flag_group] = [], checkflags: Iterable[flag_group] = []) -> None:
        node = self.find_dialog_node(node_uuid)
        if setflags:
            setflags_node = node.find('./children/node[@id="setflags"]')
            if setflags_node is None:
                raise ValueError(f"bad dialog node {node_uuid}: 'setflags' node doesn't exist")
            setflags_children_node = setflags_node.find('children')
            if setflags_children_node is None:
                setflags_children_node = et.fromstring('<children></children>')
                setflags_node.append(setflags_children_node)
            for fg in setflags:
                setflags_children_node.append(fg.to_xml())
        if checkflags:
            checkflags_node = node.find('./children/node[@id="checkflags"]')
            if checkflags_node is None:
                raise ValueError(f"bad dialog node {node_uuid}: 'checkflags' node doesn't exist")
            checkflags_children_node = checkflags_node.find('children')
            if checkflags_children_node is None:                
                checkflags_children_node = et.fromstring('<children></children>')
                checkflags_node.append(checkflags_children_node)
            for fg in checkflags:
                checkflags_children_node.append(fg.to_xml())

    def replace_dialog_flag(self, node_uuid: str, set_or_get: str, flag_type: str, flag_uuid: str, new_flag_uuid: str, new_flag_value: bool, new_flag_param: int | None) -> None:
        if set_or_get != 'setflags' and set_or_get != 'checkflags':
            raise ValueError('expected either setflags of checkflags')
        node = self.find_dialog_node(node_uuid)
        flags_node = node.find(f'./children/node[@id="{set_or_get}"]')
        if flags_node is None:
            raise RuntimeError(f'flags not found in node {node_uuid}')
        flag_groups = flags_node.findall('./children/node[@id="flaggroup"]')
        for flag_group in flag_groups:
            flag_group_type = get_required_bg3_attribute(flag_group, 'type')
            if flag_group_type != flag_type:
                continue
            flags = flag_group.findall('./children/node[@id="flag"]')
            for flag in flags:
                if get_required_bg3_attribute(flag, 'UUID') == flag_uuid:
                    set_bg3_attribute(flag, 'UUID', new_flag_uuid)
                    set_bg3_attribute(flag, 'value', str(new_flag_value))
                    if new_flag_param is None:
                        delete_bg3_attribute(flag, 'paramval')
                    else:
                        set_bg3_attribute(flag, 'paramval', str(new_flag_param))
                    return
        raise RuntimeError(f'failed to replace flag {flag_uuid}')


    def remove_dialog_attribute(self, node_uuid: str, attribute_name: str) -> None:
        node = self.find_dialog_node(node_uuid)
        attribute = node.find(f'./attribute[@id="{attribute_name}"]')
        if attribute is None:
            raise RuntimeError(f"dialog node {node_uuid} doesn't have attribute {attribute_name}")
        node.remove(attribute)

    def set_dialog_attribute(self, node_uuid: str, attribute_name: str, attribute_value: str, /, attribute_type: str | None = None) -> None:
        node = self.find_dialog_node(node_uuid)
        attribute = node.find(f'./attribute[@id="{attribute_name}"]')
        if attribute is None:
            if attribute_type is None:
                raise ValueError(f"cannot set an attribute without a type, attribute name {attribute_name}, node uuid {node_uuid}")
            set_bg3_attribute(node, attribute_name, attribute_value, attribute_type=attribute_type)
        else:
            if attribute_type is None:
                attribute_type = ''
            set_bg3_attribute(node, attribute_name, attribute_value, attribute_type=attribute_type)

    def find_dialog_node(self, node_uuid: str) -> XmlElement:
        if node_uuid in self.__dialog_nodes:
            return self.__dialog_nodes[node_uuid]
        raise RuntimeError(f"node {node_uuid} doesn't exist in dialog {self.__file.relative_file_path}")

    def get_children_nodes_uuids(self, node_uuid: str) -> list[str]:
        result = list[str]()
        node = self.find_dialog_node(node_uuid)
        children = node.findall('./children/node[@id="children"]/children/node[@id="child"]')
        for child in children:
            result.append(get_required_bg3_attribute(child, 'UUID'))
        return result

    def get_child_node_index(self, node_uuid: str, child_node_uuid: str) -> int | None:
        children = self.get_children_nodes_uuids(node_uuid)
        result = 0
        for node_uuid in children:
            if child_node_uuid == node_uuid:
                return result
            result += 1
        return None

    def get_dialog_node_text(self, dialog_node_uuid: str) -> str:
        dialog_node = self.find_dialog_node(dialog_node_uuid)
        if dialog_node is None:
            raise RuntimeError(f"dialog node {dialog_node_uuid} doesn't exist in {self.__file.relative_file_path}")
        tag_text = dialog_node.find('./children/node[@id="TaggedTexts"]/children/node[@id="TaggedText"]/children/node[@id="TagTexts"]/children/node[@id="TagText"]')
        if tag_text is None:
            return f'No voice line in the dialog node {dialog_node_uuid}'
        return get_required_bg3_attribute(tag_text, 'TagText', value_name = 'handle')

    def get_tagged_texts(self, dialog_node_uuid: str) -> list[XmlElement]:
        dialog_node = self.find_dialog_node(dialog_node_uuid)
        if dialog_node is None:
            raise RuntimeError(f"dialog node {dialog_node_uuid} doesn't exist in {self.__file.relative_file_path}")
        return dialog_node.findall('./children/node[@id="TaggedTexts"]/children/node[@id="TaggedText"]/children/node[@id="TagTexts"]/children/node[@id="TagText"]')

    def get_tagged_texts_with_rules(self, dialog_node_uuid: str) -> list[XmlElement]:
        dialog_node = self.find_dialog_node(dialog_node_uuid)
        if dialog_node is None:
            raise RuntimeError(f"dialog node {dialog_node_uuid} doesn't exist in {self.__file.relative_file_path}")
        return dialog_node.findall('./children/node[@id="TaggedTexts"]/children/node[@id="TaggedText"]')

    def get_all_tagged_texts(self) -> dict[str, int]:
        nodes = self.__file.root_node.find("region[@id='dialog']/node[@id='dialog']/children/node[@id='nodes']/children")
        if nodes is None:
            return {}
        tag_texts = nodes.findall('./node[@id="node"]/children/node[@id="TaggedTexts"]/children/node[@id="TaggedText"]/children/node[@id="TagTexts"]/children/node[@id="TagText"]')
        result = dict[str, int]()
        for tag_text in tag_texts:
            text_handle = get_required_bg3_attribute(tag_text, 'TagText', value_name = 'handle')
            maybe_version = get_bg3_attribute(tag_text, 'TagText', value_name = 'version')
            if maybe_version is not None:
                version = int(maybe_version)
            else:
                version = 0
            result[text_handle] = version
        return result

    def set_tagged_text(self, dialog_node_uuid: str, text: text_content | Iterable[text_content]) -> None:
        dialog_node = self.find_dialog_node(dialog_node_uuid)
        if dialog_node is None:
            raise RuntimeError(f"dialog node {dialog_node_uuid} doesn't exist in {self.__file.relative_file_path}")
        tag_texts = dialog_node.find('./children/node[@id="TaggedTexts"]/children/node[@id="TaggedText"]/children/node[@id="TagTexts"]')
        if tag_texts is None:
            raise RuntimeError(f"dialog node {dialog_node_uuid} doesn't contain tagged texts")
        tag_texts_children = tag_texts.find('./children')
        if tag_texts_children is not None:
            tag_texts.remove(tag_texts_children)
        tag_texts_children = et.fromstring('<children></children>')
        tag_texts.append(tag_texts_children)
        if isinstance(text, text_content):
            tag_texts_children.append(text.to_xml())
        elif isinstance(text, Iterable):
            for t in text:
                tag_texts_children.append(t.to_xml())
        else:
            raise TypeError(f'expected text_content or Iterable[text_content]; got {type(text)}')

    def replace_text_tag(self, old_tag_uuid: str, new_tag_uuid: str, speaker_override: int | None = None) -> None:
        nodes = self.get_dialog_nodes()
        for node in nodes:
            rules = node.findall('./children/node[@id="TaggedTexts"]/children/node[@id="TaggedText"]/children/node[@id="RuleGroup"]/children/node[@id="Rules"]/children/node[@id="Rule"]')
            for rule in rules:
                tags = rule.findall('./children/node[@id="Tags"]/children/node[@id="Tag"]')
                tag_replaced = False
                has_really_tag = False
                for tag in tags:
                    tag_uuid = get_bg3_attribute(tag, 'Object')
                    if isinstance(tag_uuid, str):
                        if tag_uuid in REALLY_TAGS:
                            has_really_tag = True
                        if tag_uuid == old_tag_uuid:
                            set_bg3_attribute(tag, 'Object', new_tag_uuid, attribute_type = 'guid')
                            tag_replaced = True
                if tag_replaced and not has_really_tag and speaker_override is not None:
                    speaker_index = get_bg3_attribute(rule, 'speaker')
                    if speaker_override != speaker_index:
                        node_uuid = get_bg3_attribute(node, 'UUID')
                        print(f'speaker mismatch in node {node_uuid}')
                        set_bg3_attribute(rule, 'speaker', speaker_override, attribute_type = 'int32')

    def replace_flags(self, group_type: str, old_flag_uuid: str, new_flag_uuid: str, /, setflags: bool = False, speaker_override: int | None = None) -> None:
        is_global_flag = group_type == 'Global' or group_type == 'Script'
        if setflags:
            flags_node_id = 'setflags'
        else:
            flags_node_id = 'checkflags'
        for node in self.get_dialog_nodes():
            flag_groups = node.findall(f'./children/node[@id="{flags_node_id}"]/children/node[@id="flaggroup"]')
            for fg in flag_groups:
                if group_type == get_required_bg3_attribute(fg, 'type'):
                    flags = fg.findall('./children/node[@id="flag"]')
                    for f in flags:
                        flag_uuid = get_required_bg3_attribute(f, 'UUID')
                        if old_flag_uuid == flag_uuid:
                            set_bg3_attribute(f, 'UUID', new_flag_uuid)
                            if not is_global_flag and speaker_override is not None:
                                set_bg3_attribute(f, 'paramval', speaker_override)

    def delete_dialog_node(self, dialog_node_uuid: str) -> None:
        dialog_node = self.find_dialog_node(dialog_node_uuid)
        if dialog_node is None:
            raise RuntimeError(f"dialog node {dialog_node_uuid} doesn't exist in {self.__file.relative_file_path}")
        self.__dialog_nodes_parent.remove(dialog_node)
        del self.__dialog_nodes[dialog_node_uuid]

    def create_standard_dialog_node(
            self,
            node_uuid: str,
            speaker: str,
            children: Iterable[str],
            text: text_content | Iterable[text_content] | None,
            /,
            constructor: str = ANSWER,
            text_tags: Iterable[str] | None = None,
            tags: Iterable[XmlElement] = [],
            setflags: Iterable[flag_group] = [],
            checkflags: Iterable[flag_group] = [],
            transition_mode: bool = False,
            show_once: bool = False,
            root: bool = False,
            end_node: bool = False,
            group_id: str = "",
            group_index: int = 0,
            approval_rating_uuid: str | None = None,
            validated_has_value: bool | None = None
    ) -> XmlElement:
        speaker_index = self.get_speaker_slot_index(speaker)
        result = list[str]()
        result.append('<node id="node" key="UUID">')
        result.append(f'<attribute id="constructor" type="FixedString" value="{constructor}" />')
        result.append(f'<attribute id="UUID" type="FixedString" value="{node_uuid}" />')
        result.append(f'<attribute id="speaker" type="int32" value="{speaker_index}" />')
        if transition_mode:
            result.append('<attribute id="transitionmode" type="uint8" value="2" />')
        if show_once:
            result.append('<attribute id="ShowOnce" type="bool" value="True" />')
        if root:
            result.append('<attribute id="Root" type="bool" value="True" />')
        if end_node:
            result.append('<attribute id="endnode" type="bool" value="True" />')
        if group_id:
            result.append(f'<attribute id="GroupID" type="FixedString" value="{group_id}" />')
            result.append(f'<attribute id="GroupIndex" type="int32" value="{group_index}" />')
        if approval_rating_uuid:
            result.append(f'<attribute id="ApprovalRatingID" type="guid" value="{approval_rating_uuid}" />')
        result.append('<children>')
        if not children:
            result.append('<node id="children" />')
        else:
            result.append('<node id="children"><children>')
            for child in children:
                result.append(f'<node id="child"><attribute id="UUID" type="FixedString" value="{child}" /></node>')
            result.append('</children></node>')
        result.append('<node id="GameData"><children><node id="AiPersonalities" key="AiPersonality" /><node id="MusicInstrumentSounds" /><node id="OriginSound" /></children></node>')
        if get_len(tags) == 0:
            result.append('<node id="Tags" />')
        else:
            result.append('<node id="Tags"><children>')
            for t in tags:
                result.append(to_compact_string(t))
            result.append('</children></node>')
        if get_len(setflags) == 0:
            result.append('<node id="setflags" />')
        else:
            result.append('<node id="setflags"><children>')
            for f in setflags:
                result.append(to_compact_string(f.to_xml()))
            result.append('</children></node>')
        if get_len(checkflags) == 0:
            result.append('<node id="checkflags" />')
        else:
            result.append('<node id="checkflags"><children>')
            for f in checkflags:
                result.append(to_compact_string(f.to_xml()))
            result.append('</children></node>')
        if text is None:
            result.append('<node id="TaggedTexts" />')
        else:
            result.append('<node id="TaggedTexts"><children><node id="TaggedText"><attribute id="HasTagRule" type="bool" value="True" /><children><node id="TagTexts"><children>')
            if isinstance(text, Iterable):
                for t in text:
                    result.append(to_compact_string(t.to_xml()))
            elif isinstance(text, text_content):
                result.append(to_compact_string(text.to_xml()))
            else:
                raise TypeError(f'expected text_content, Iterable[text_content], or None; got {type(text)}')
            result.append('</children></node>')

            if text_tags is None or get_len(text_tags) == 0:
                result.append('<node id="RuleGroup"><attribute id="TagCombineOp" type="uint8" value="0" /><children><node id="Rules" /></children></node>')
            else:
                result.append('<node id="RuleGroup"><attribute id="TagCombineOp" type="uint8" value="0" /><children><node id="Rules">')
                result.append('<children><node id="Rule"><attribute id="HasChildRules" type="bool" value="False" />')
                result.append(f'<attribute id="speaker" type="int32" value="{speaker_index}" /><attribute id="TagCombineOp" type="uint8" value="1" />')
                result.append('<children><node id="Tags"><children>')
                for tag in text_tags:
                    result.append(f'<node id="Tag"><attribute id="Object" type="guid" value="{tag}" /></node>')
                result.append('</children></node></children></node></children></node></children></node>')
            result.append('</children></node></children></node>')
        if validated_has_value is not None:
            result.append(f'<node id="ValidatedFlags"><attribute id="ValidatedHasValue" type="bool" value="{validated_has_value}" /></node>')
        result.append('</children></node>')
        dialog = et.fromstring("\n".join(result))
        self.__dialog_nodes_parent.append(dialog)
        self.__dialog_nodes[node_uuid] = dialog
        return dialog

    def create_cinematic_dialog_node(
            self,
            node_uuid: str,
            children: Iterable[str],
            /,
            visual_state: bool = False,
            speaker: str | None = None,
            tags: Iterable[XmlElement] = [],
            setflags: Iterable[flag_group] = [],
            checkflags: Iterable[flag_group] = [],
            transition_mode: bool = False,
            root: bool = False,
            show_once: bool = False,
            end_node: bool = False,
            group_id: str = "",
            group_index: int = 0,
            approval_rating_uuid: str | None = None,
    ) -> XmlElement:
        result = list[str]()
        result.append('<node id="node" key="UUID">')
        if visual_state:
            result.append('<attribute id="constructor" type="FixedString" value="Visual State" />')
        else:
            result.append('<attribute id="constructor" type="FixedString" value="TagCinematic" />')
        result.append(f'<attribute id="UUID" type="FixedString" value="{node_uuid}" />')
        if speaker is None:
            result.append('<attribute id="speaker" type="int32" value="-1" />')
        else:
            speaker_index = self.get_speaker_slot_index(speaker)
            result.append(f'<attribute id="speaker" type="int32" value="{speaker_index}" />')        
        if transition_mode:
            result.append('<attribute id="transitionmode" type="uint8" value="2" />')
        if show_once:
            result.append('<attribute id="ShowOnce" type="bool" value="True" />')
        if root:
            result.append('<attribute id="Root" type="bool" value="True" />')
        if end_node:
            result.append('<attribute id="endnode" type="bool" value="True" />')
        if group_id:
            result.append(f'<attribute id="GroupID" type="FixedString" value="{group_id}" />')
            result.append(f'<attribute id="GroupIndex" type="int32" value="{group_index}" />')
        if approval_rating_uuid:
            result.append(f'<attribute id="ApprovalRatingID" type="guid" value="{approval_rating_uuid}" />')
        result.append('<children>')
        if not children:
            result.append('<node id="children" />')
        else:
            result.append('<node id="children"><children>')
            for child in children:
                result.append(f'<node id="child"><attribute id="UUID" type="FixedString" value="{child}" /></node>')
            result.append('</children></node>')
        result.append('<node id="GameData"><children><node id="AiPersonalities" key="AiPersonality" /><node id="MusicInstrumentSounds" /><node id="OriginSound" /></children></node>')
        if get_len(tags) == 0:
            result.append('<node id="Tags" />')
        else:
            result.append('<node id="Tags"><children>')
            for t in tags:
                result.append(to_compact_string(t))
            result.append('</children></node>')
        if get_len(setflags) == 0:
            result.append('<node id="setflags" />')
        else:
            result.append('<node id="setflags"><children>')
            for f in setflags:
                result.append(to_compact_string(f.to_xml()))
            result.append('</children></node>')
        if get_len(checkflags) == 0:
            result.append('<node id="checkflags" />')
        else:
            result.append('<node id="checkflags"><children>')
            for f in checkflags:
                result.append(to_compact_string(f.to_xml()))
            result.append('</children></node>')
        result.append('</children></node>')
        dialog = et.fromstring("\n".join(result))
        self.__dialog_nodes_parent.append(dialog)
        self.__dialog_nodes[node_uuid] = dialog
        return dialog

    def create_jump_dialog_node(
            self,
            node_uuid: str,
            jump_target_node_uuid: str,
            jump_target_point: int
    ) -> XmlElement:
        result = list[str]()
        result.append('<node id="node" key="UUID">')
        result.append('<attribute id="constructor" type="FixedString" value="Jump" />')
        result.append(f'<attribute id="UUID" type="FixedString" value="{node_uuid}" />')
        result.append(f'<attribute id="jumptarget" type="FixedString" value="{jump_target_node_uuid}" />')
        result.append(f'<attribute id="jumptargetpoint" type="uint8" value="{jump_target_point}" />')
        result.append('<children><node id="children" /><node id="Tags" /><node id="setflags" /><node id="checkflags" /></children></node>')
        dialog = et.fromstring("\n".join(result))
        self.__dialog_nodes_parent.append(dialog)
        self.__dialog_nodes[node_uuid] = dialog
        return dialog

    def create_alias_dialog_node(
            self,
            node_uuid: str,
            source_node_uuid: str,
            children: Iterable[str],
            /,
            tags: Iterable[XmlElement] = [],
            setflags: Iterable[flag_group] = [],
            checkflags: Iterable[flag_group] = [],
            show_once: bool = False,
            root: bool = False,
            end_node: bool = False,
            approval_rating_uuid: str | None = None,
    ) -> XmlElement:
        result = list[str]()
        result.append('<node id="node" key="UUID">')
        result.append(f'<attribute id="constructor" type="FixedString" value="Alias" />')
        result.append(f'<attribute id="UUID" type="FixedString" value="{node_uuid}" />')
        if show_once:
            result.append('<attribute id="ShowOnce" type="bool" value="True" />')
        if root:
            result.append('<attribute id="Root" type="bool" value="True" />')
            result.append('<attribute id="Greeting" type="bool" value="True" />')
        if end_node:
            result.append('<attribute id="endnode" type="bool" value="True" />')
        if approval_rating_uuid:
            result.append(f'<attribute id="ApprovalRatingID" type="guid" value="{approval_rating_uuid}" />')
        result.append('<attribute id="speaker" type="int32" value="-1" />')
        result.append(f'<attribute id="SourceNode" type="FixedString" value="{source_node_uuid}" />')
        result.append('<children>')
        if not children:
            result.append('<node id="children" />')
        else:
            result.append('<node id="children"><children>')
            for child in children:
                result.append(f'<node id="child"><attribute id="UUID" type="FixedString" value="{child}" /></node>')
            result.append('</children></node>')
        result.append('<node id="GameData"><children><node id="AiPersonalities" key="AiPersonality" /><node id="MusicInstrumentSounds" /><node id="OriginSound" /></children></node>')
        if get_len(tags) == 0:
            result.append('<node id="Tags" />')
        else:
            result.append('<node id="Tags"><children>')
            for t in tags:
                result.append(to_compact_string(t))
            result.append('</children></node>')
        if not setflags:
            result.append('<node id="setflags" />')
        else:
            result.append('<node id="setflags"><children>')
            for f in setflags:
                result.append(to_compact_string(f.to_xml()))
            result.append('</children></node>')
        if not checkflags:
            result.append('<node id="checkflags" />')
        else:
            result.append('<node id="checkflags"><children>')
            for f in checkflags:
                result.append(to_compact_string(f.to_xml()))
            result.append('</children></node>')
        result.append('</children></node>')
        dialog = et.fromstring("\n".join(result))
        self.__dialog_nodes_parent.append(dialog)
        self.__dialog_nodes[node_uuid] = dialog
        return dialog

    def create_roll_result_dialog_node(
            self,
            node_uuid: str,
            success: bool,
            children: Iterable[str]
    ) -> XmlElement:
        result = list[str]()
        result.append('<node id="node" key="UUID">')
        result.append(f'<attribute id="constructor" type="FixedString" value="RollResult" />')
        result.append(f'<attribute id="UUID" type="FixedString" value="{node_uuid}" />')
        result.append(f'<attribute id="Success" type="bool" value="{success}" />')
        result.append('<children>')
        if not children:
            result.append('<node id="children" />')
        else:
            result.append('<node id="children"><children>')
            for child in children:
                result.append(f'<node id="child"><attribute id="UUID" type="FixedString" value="{child}" /></node>')
            result.append('</children></node>')
        result.append('<node id="Tags" /><node id="setflags" /><node id="checkflags" /></children></node>')
        dialog = et.fromstring("\n".join(result))
        self.__dialog_nodes_parent.append(dialog)
        self.__dialog_nodes[node_uuid] = dialog
        return dialog

    def create_roll_dialog_node(
            self,
            node_uuid: str,
            speaker: str,
            roll_target_speaker: str,
            ability: str,
            skill: str,
            dc: str,
            success_node_uuid: str,
            failure_node_uuid: str,
            text: text_content | Iterable[text_content] | None,
            tags: Iterable[XmlElement] = [],
            setflags: Iterable[flag_group] = [],
            checkflags: Iterable[flag_group] = [],
            transition_mode: bool = False,
            show_once: bool = False,
            passive: bool = False,
            roll_type: str = ROLL_SKILL_CHECK,
            advantage: int = 0,
            advantage_reason: tuple[str, int] | str | None = None,
            exclude_speaker_bonus: bool = False,
            exclude_companion_bonus: bool = False,
            validated_has_value: bool | None = None
    ) -> XmlElement:
        speaker_index = self.get_speaker_slot_index(speaker)
        roll_target_speaker_index = self.get_speaker_slot_index(roll_target_speaker)
        constructor = dialog_object.ROLL_ACTIVE if passive == False else dialog_object.ROLL_PASSIVE
        roll_success_node_uuid = new_random_uuid()
        roll_failure_node_uuid = new_random_uuid()
        self.create_roll_result_dialog_node(roll_success_node_uuid, True, [success_node_uuid])
        self.create_roll_result_dialog_node(roll_failure_node_uuid, False, [failure_node_uuid])
        result = list[str]()
        result.append('<node id="node" key="UUID">')
        result.append(f'<attribute id="constructor" type="FixedString" value="{constructor}" />')
        result.append(f'<attribute id="UUID" type="FixedString" value="{node_uuid}" />')
        if transition_mode:
            result.append('<attribute id="transitionmode" type="uint8" value="2" />')
        if show_once:
            result.append('<attribute id="ShowOnce" type="bool" value="True" />')
        result.append(f'<attribute id="speaker" type="int32" value="{speaker_index}" />')
        result.append(f'<attribute id="RollType" type="string" value="{roll_type}" />')
        result.append(f'<attribute id="Ability" type="string" value="{ability}" />')
        result.append(f'<attribute id="Skill" type="string" value="{skill}" />')
        result.append(f'<attribute id="RollTargetSpeaker" type="int32" value="{roll_target_speaker_index}" />')
        result.append(f'<attribute id="Advantage" type="uint8" value="{advantage}" />')
        if isinstance(advantage_reason, str):
            result.append(f'<attribute id="AdvantageReason" type="TranslatedString" handle="{advantage_reason}" version="1" />')
        elif isinstance(advantage_reason, tuple):
            if len(advantage_reason) == 2 and isinstance(advantage_reason[0], str) and isinstance(advantage_reason[1], int):
                result.append(f'<attribute id="AdvantageReason" type="TranslatedString" handle="{advantage_reason[0]}" version="{advantage_reason[1]}" />')
            else:
                raise ValueError('advantage_reason should be a tuple of str and int: string handle and version')
        result.append(f'<attribute id="ExcludeCompanionsOptionalBonuses" type="bool" value="{exclude_companion_bonus}" />')
        result.append(f'<attribute id="ExcludeSpeakerOptionalBonuses" type="bool" value="{exclude_speaker_bonus}" />')
        result.append(f'<attribute id="DifficultyClassID" type="guid" value="{dc}" />')
        result.append('<children>')
        result.append('<node id="children"><children>')
        result.append(f'<node id="child"><attribute id="UUID" type="FixedString" value="{roll_success_node_uuid}" /></node>')
        result.append(f'<node id="child"><attribute id="UUID" type="FixedString" value="{roll_failure_node_uuid}" /></node>')
        result.append('</children></node>')
        result.append('<node id="GameData"><children><node id="AiPersonalities" key="AiPersonality" /><node id="MusicInstrumentSounds" /><node id="OriginSound" /></children></node>')
        if get_len(tags) == 0:
            result.append('<node id="Tags" />')
        else:
            result.append('<node id="Tags"><children>')
            for t in tags:
                result.append(to_compact_string(t))
            result.append('</children></node>')
        if get_len(setflags) == 0:
            result.append('<node id="setflags" />')
        else:
            result.append('<node id="setflags"><children>')
            for f in setflags:
                result.append(to_compact_string(f.to_xml()))
            result.append('</children></node>')
        if get_len(checkflags) == 0:
            result.append('<node id="checkflags" />')
        else:
            result.append('<node id="checkflags"><children>')
            for f in checkflags:
                result.append(to_compact_string(f.to_xml()))
            result.append('</children></node>')
        if not passive:
            if text is None:
                result.append('<node id="TaggedTexts" />')
            else:
                result.append('<node id="TaggedTexts"><children><node id="TaggedText"><attribute id="HasTagRule" type="bool" value="True" /><children><node id="TagTexts"><children>')
                if isinstance(text, Iterable):
                    for t in text:
                        result.append(to_compact_string(t.to_xml()))
                elif isinstance(text, text_content):
                    result.append(to_compact_string(text.to_xml()))
                else:
                    raise TypeError(f'expected text_content, Iterable[text_content], or None; got {type(text)}')
                result.append('</children></node>')
                result.append('<node id="RuleGroup"><attribute id="TagCombineOp" type="uint8" value="0" /><children><node id="Rules" /></children></node>')
                result.append('</children></node></children></node>')
        if validated_has_value is not None:
            result.append(f'<node id="ValidatedFlags"><attribute id="ValidatedHasValue" type="bool" value="{validated_has_value}" /></node>')
        result.append('</children></node>')
        dialog = et.fromstring("\n".join(result))
        self.__dialog_nodes_parent.append(dialog)
        self.__dialog_nodes[node_uuid] = dialog
        return dialog

    def create_nested_dialog_node(
            self,
            node_uuid: str,
            nested_dialog_node_uuid: str,
            children: Iterable[str],
            /,
            speaker_linking: Iterable[tuple[int, int]] = [],
            speaker_count: int | None = None,
            root: bool = False,
            tags: Iterable[XmlElement] = [],
            setflags: Iterable[flag_group] = [],
            checkflags: Iterable[flag_group] = [],
    ) -> XmlElement:
        result = list[str]()
        result.append('<node id="node" key="UUID">')
        result.append(f'<attribute id="constructor" type="FixedString" value="Nested Dialog" />')
        result.append(f'<attribute id="UUID" type="FixedString" value="{node_uuid}" />')
        result.append(f'<attribute id="NestedDialogNodeUUID" type="guid" value="{nested_dialog_node_uuid}" />')
        if root:
            result.append('<attribute id="Root" type="bool" value="True" />')
        result.append('<children>')
        if get_len(speaker_linking) == 0 and isinstance(speaker_count, int):
            result.append('<node id="SpeakerLinking"><children>')
            for n in range(0, speaker_count):
                result.append(f'<node id="SpeakerLinkingEntry"><attribute id="Key" type="int32" value="{n}" /><attribute id="Value" type="int32" value="{n}" /></node>')
            result.append('</children></node>')
        elif get_len(speaker_linking) > 0:
            result.append('<node id="SpeakerLinking"><children>')
            for a, b in speaker_linking:
                result.append(f'<node id="SpeakerLinkingEntry"><attribute id="Key" type="int32" value="{a}" /><attribute id="Value" type="int32" value="{b}" /></node>')
            result.append('</children></node>')
        else:
            raise ValueError('either speaker_linking or speaker_count should be provided')
        if not children:
            result.append('<node id="children" />')
        else:
            result.append('<node id="children"><children>')
            for child in children:
                result.append(f'<node id="child"><attribute id="UUID" type="FixedString" value="{child}" /></node>')
            result.append('</children></node>')
        if get_len(tags) == 0:
            result.append('<node id="Tags" />')
        else:
            result.append('<node id="Tags"><children>')
            for t in tags:
                result.append(to_compact_string(t))
            result.append('</children></node>')
        if not setflags:
            result.append('<node id="setflags" />')
        else:
            result.append('<node id="setflags"><children>')
            for f in setflags:
                result.append(to_compact_string(f.to_xml()))
            result.append('</children></node>')
        if not checkflags:
            result.append('<node id="checkflags" />')
        else:
            result.append('<node id="checkflags"><children>')
            for f in setflags:
                result.append(to_compact_string(f.to_xml()))
            result.append('</children></node>')
        result.append('</children></node>')
        dialog = et.fromstring("\n".join(result))
        self.__dialog_nodes_parent.append(dialog)
        self.__dialog_nodes[node_uuid] = dialog
        return dialog

    def add_root_node(self, node_uuid: str, index: int = -1) -> None:
        nodes = self.__file.root_node.find("region[@id='dialog']/node[@id='dialog']/children/node[@id='nodes']/children")
        if nodes is None:
            raise RuntimeError("Dialog has no nodes")
        new_root_node = et.fromstring(f'<node id="RootNodes"><attribute id="RootNodes" type="FixedString" value="{node_uuid}" /></node>')
        if index == -1:
            nodes.append(new_root_node)
            return
        n = len(nodes)
        if index >= 0:
            idx = index
            for i in range(0, n):
                if nodes[i].get("id") == 'RootNodes':
                    if idx == 0:
                        nodes.insert(i, new_root_node)
                        return
                    else:
                        idx -= 1
        else:
            nodes.append(new_root_node)
        raise RuntimeError(f"Cannot add root node '{node_uuid}' at index {index}")

    def add_root_node_before(self, existing_node_uuid: str, new_root_node_uuid: str) -> None:
        idx = self.get_root_node_index(existing_node_uuid)
        self.add_root_node(new_root_node_uuid, idx)

    def add_root_node_after(self, existing_node_uuid: str, new_root_node_uuid: str) -> None:
        idx = self.get_root_node_index(existing_node_uuid)
        self.add_root_node(new_root_node_uuid, idx + 1)

    def remove_root_node(self, node_uuid: str) -> None:
        children = self.__file.root_node.find("./region[@id='dialog']/node[@id='dialog']/children/node[@id='nodes']/children")
        if children is not None:
            root_nodes = children.findall("./node[@id='RootNodes']")
            for root_node in root_nodes:
                if get_required_bg3_attribute(root_node, 'RootNodes') == node_uuid:
                    children.remove(root_node)
                    return
        raise RuntimeError(f"Cannot remove root node '{node_uuid}'")

    def get_root_nodes(self) -> list[str]:
        root_nodes = self.__file.root_node.findall("./region[@id='dialog']/node[@id='dialog']/children/node[@id='nodes']/children/node[@id='RootNodes']")
        return [get_required_bg3_attribute(root_node, 'RootNodes') for root_node in root_nodes]

    def get_root_node_index(self, node_uuid: str) -> int:
        root_nodes = self.__file.root_node.findall("./region[@id='dialog']/node[@id='dialog']/children/node[@id='nodes']/children/node[@id='RootNodes']")
        for index in range(0, len(root_nodes)):
            root_node = root_nodes[index]
            current_node_uuid = get_required_bg3_attribute(root_node, 'RootNodes')
            if current_node_uuid == node_uuid:
                return index
        raise KeyError(f"root node {node_uuid} doesn't exist in {self.__file.relative_file_path}")

    def get_dialog_flags(self, node_uuid: str, /, setflags: bool = False, checkflags: bool = False) -> dict[str, dialog_flag]:
        result = dict[str, dialog_flag]()
        d = self.find_dialog_node(node_uuid)
        if setflags and not checkflags:
            flag_groups = d.findall('./children/node[@id="setflags"]/children/node[@id="flaggroup"]')
        elif checkflags and not setflags:
            flag_groups = d.findall('./children/node[@id="checkflags"]/children/node[@id="flaggroup"]')
        else:
            raise ValueError('one should be set: either setflags or checkflags')
        for flag_group in flag_groups:
            flag_type = get_required_bg3_attribute(flag_group, 'type')
            flags = flag_group.findall('children/node[@id="flag"]')
            for flag in flags:
                flag_uuid = get_required_bg3_attribute(flag, 'UUID')
                flag_value = get_required_bg3_attribute(flag, 'value') == 'True'
                flag_paramval = get_bg3_attribute(flag, 'paramval')
                if flag_paramval is None:
                    result[flag_uuid] = dialog_flag(flag_type, flag_uuid, flag_value, None)
                else:
                    result[flag_uuid] = dialog_flag(flag_type, flag_uuid, flag_value, int(flag_paramval))
        return result

    def has_tags(self, tag_uuids: set[str]) -> bool:
        for dialog_node in self.__dialog_nodes.values():
            # Replace tags in tagged texts
            texts = dialog_node.findall('./children/node[@id="TaggedTexts"]/children/node[@id="TaggedText"]')
            for text in texts:
                tag = text.find('./children/node[@id="RuleGroup"]/children/node[@id="Rules"]/children/node[@id="Rule"]/children/node[@id="Tags"]/children/node[@id="Tag"]')
                if tag is not None:
                    tag_uuid = get_bg3_attribute(tag, 'Object')
                    if tag_uuid in tag_uuids:
                        return True
    
            # Replace tags in flags
            for tag_name in ('checkflags', 'setflags'):
                flag_groups = dialog_node.findall(f'./children/node[@id="{tag_name}"]/children/node[@id="flaggroup"]')
                for flag_group in flag_groups:
                    if get_bg3_attribute(flag_group, 'type') == 'Tag':
                        flags = flag_group.findall('./children/node[@id="flag"]')
                        for flag in flags:
                            tag_uuid = get_bg3_attribute(flag, 'UUID')
                            if tag_uuid in tag_uuids:
                                return True
        return False

    def replace_tags(self, tags: dict[str, str]) -> None:
        original_tags_uuids = frozenset(tags.keys())
        for dialog_node in self.__dialog_nodes.values():
            # Replace tags in tagged texts
            texts = dialog_node.findall('./children/node[@id="TaggedTexts"]/children/node[@id="TaggedText"]')
            for text in texts:
                tag = text.find('./children/node[@id="RuleGroup"]/children/node[@id="Rules"]/children/node[@id="Rule"]/children/node[@id="Tags"]/children/node[@id="Tag"]')
                if tag is not None:
                    tag_uuid = get_bg3_attribute(tag, 'Object')
                    if tag_uuid is not None and tag_uuid in original_tags_uuids:
                        new_tag_uuid = tags[tag_uuid]
                        set_bg3_attribute(tag, 'Object', new_tag_uuid)
    
            # Replace tags in flags
            for tag_name in ('checkflags', 'setflags'):
                flag_groups = dialog_node.findall(f'./children/node[@id="{tag_name}"]/children/node[@id="flaggroup"]')
                for flag_group in flag_groups:
                    if get_bg3_attribute(flag_group, 'type') == 'Tag':
                        flags = flag_group.findall('./children/node[@id="flag"]')
                        for flag in flags:
                            tag_uuid = get_bg3_attribute(flag, 'UUID')
                            if tag_uuid in original_tags_uuids:
                                new_tag_uuid = tags[tag_uuid]
                                set_bg3_attribute(flag, 'UUID', new_tag_uuid)

    def set_approval_rating(self, dialog_node_uuid: str, approval_rating_uuid: str) -> None:
        node = self.find_dialog_node(dialog_node_uuid)
        set_bg3_attribute(node, 'ApprovalRatingID', approval_rating_uuid, attribute_type = 'guid')

    def remove_approval_rating(self, dialog_node_uuid: str) -> None:
        node = self.find_dialog_node(dialog_node_uuid)
        delete_bg3_attribute(node, 'ApprovalRatingID')


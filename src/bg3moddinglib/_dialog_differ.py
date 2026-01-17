from __future__ import annotations

import xml.etree.ElementTree as et

from ._assets import bg3_assets, dialog_index
from ._common import attrs_to_str, get_bg3_attribute, get_required_bg3_attribute
from ._dialog import dialog_object

from ._types import XmlElement

import os.path

class dialog_differ:
    ADDED = 'added'
    DELETED = 'deleted'
    MODIFIED = 'modified'

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


    def get_modified_dialog_nodes(self, modded_dialog: dialog_object, dialog_name: str | None = None) -> dict[str, str]:
        result = dict[str, str]()
        if dialog_name is None:
            dialog_name, _ = os.path.splitext(os.path.basename(modded_dialog.filename))
        original_dialog = self.__assets.get_dialog_object(dialog_name)
        original_nodes = { get_required_bg3_attribute(node, 'UUID') : node for node in original_dialog.get_dialog_nodes() }
        modded_nodes = { get_required_bg3_attribute(node, 'UUID') : node for node in modded_dialog.get_dialog_nodes() }
        original_nodes_uuids = set(original_nodes.keys())
        modded_nodes_uuids = set(modded_nodes.keys())
        common_nodes_uuids = original_nodes_uuids.intersection(modded_nodes_uuids)
        only_in_modded_uuids = modded_nodes_uuids.difference(original_nodes_uuids)
        only_in_original_uuids = original_nodes_uuids.difference(modded_nodes_uuids)
        for node_uuid in only_in_original_uuids:
            result[node_uuid] = dialog_differ.DELETED
        for node_uuid in only_in_modded_uuids:
            result[node_uuid] = dialog_differ.ADDED
        for node_uuid in common_nodes_uuids:
            original_node = original_nodes[node_uuid]
            modded_node = modded_nodes[node_uuid]
            if not dialog_differ.compare_dialog_nodes(original_node, modded_node):
                result[node_uuid] = dialog_differ.MODIFIED
        return result


    def get_modified_dialog_root_nodes(self, modded_dialog: dialog_object, dialog_name: str | None = None) -> dict[str, str]:
        result = dict[str, str]()
        if dialog_name is None:
            dialog_name, _ = os.path.splitext(os.path.basename(modded_dialog.filename))
        original_dialog = self.__assets.get_dialog_object(dialog_name.lower())
        original_roots = original_dialog.get_root_nodes_order()
        original_roots_len = len(original_roots)
        modded_roots = modded_dialog.get_root_nodes_order()
        modded_roots_len = len(modded_roots)
        original_roots_uuids = set(original_roots.keys())
        modded_roots_uuids = set(modded_roots.keys())
        common_nodes_uuids = original_roots_uuids.intersection(modded_roots_uuids)
        only_in_modded_uuids = modded_roots_uuids.difference(original_roots_uuids)
        only_in_original_uuids = original_roots_uuids.difference(modded_roots_uuids)
        for node_uuid in only_in_original_uuids:
            result[node_uuid] = dialog_differ.DELETED
        for node_uuid in only_in_modded_uuids:
            result[node_uuid] = dialog_differ.ADDED

        original_roots_uuids_list = original_dialog.get_root_nodes()
        modded_roots_uuids_list = modded_dialog.get_root_nodes()

        # If a root node is the first or the last in both original and modded, it is considerded as not modified
        # If a root node precedes the same node in both original and modded (ignoring new added nodes), it is considerded as not modified
        for node_uuid in common_nodes_uuids:
            ori_idx = original_roots[node_uuid]
            mod_idx = modded_roots[node_uuid]
            if ori_idx == 0 and mod_idx == 0:
                continue
            if ori_idx == (original_roots_len - 1) and mod_idx == (modded_roots_len - 1):
                continue
            if ori_idx == 0 and mod_idx != 0:
                result[node_uuid] = dialog_differ.MODIFIED
            elif ori_idx == (original_roots_len - 1) and mod_idx != (modded_roots_len - 1):
                result[node_uuid] = dialog_differ.MODIFIED
            elif ori_idx != 0 and mod_idx == 0:
                result[node_uuid] = dialog_differ.MODIFIED
            elif ori_idx != (original_roots_len - 1) and mod_idx == (modded_roots_len - 1):
                result[node_uuid] = dialog_differ.MODIFIED
            else:
                ori_next_node_uuid = original_roots_uuids_list[ori_idx + 1]
                mod_idx += 1
                mod_next_node_uuid = ''
                while mod_idx < modded_roots_len:
                    mod_next_node_uuid = modded_roots_uuids_list[mod_idx]
                    if mod_next_node_uuid not in only_in_modded_uuids:
                        break
                    mod_idx += 1
                if ori_next_node_uuid != mod_next_node_uuid:
                    result[node_uuid] = dialog_differ.MODIFIED
        return result


    @staticmethod
    def get_dialog_attributes(node: XmlElement) -> str:
        result = list[str]()
        attrs = node.findall('./attribute')
        for attr in attrs:
            result.append(f"{attr.attrib['id']}={attr.attrib['value']}")
        return '|'.join(result)


    @staticmethod
    def get_dialog_children(d: XmlElement) -> str:
        return '|'.join([e.attrib['value'] for e in d.findall('./children/node[@id="children"]/children/node[@id="child"]/attribute')])


    @staticmethod
    def get_dialog_flags(d: XmlElement) -> str:
        result = list[str]()
        for name in ('checkflags', 'setflags'):
            action = name[:-5]
            flags_groups = d.findall(f'./children/node[@id="{name}"]/children/node[@id="flaggroup"]')
            for flag_group in flags_groups:
                flag_type = get_required_bg3_attribute(flag_group, 'type')
                flags = flag_group.findall('./children/node[@id="flag"]')
                for flag in flags:
                    flag_uuid = get_bg3_attribute(flag, 'UUID')
                    flag_value = get_bg3_attribute(flag, 'value')
                    flag_paramval = get_bg3_attribute(flag, 'paramval')
                    result.append(f'{action} {flag_uuid}:{flag_type}:{flag_paramval}={flag_value}')
        return '|'.join(result)


    @staticmethod
    def get_dialog_texts(d: XmlElement) -> str:
        result = list[str]()
        tagged_texts = d.findall('./children/node[@id="TaggedTexts"]/children/node[@id="TaggedText"]')
        for tagged_text in tagged_texts:        
            tags = [f'[{get_required_bg3_attribute(e, 'Object')}]' for e in tagged_text.findall('./children/node[@id="RuleGroup"]/children/node[@id="Rules"]/children/node[@id="Rule"]/children/node[@id="Tags"]/children/node[@id="Tag"]')]
            tags.sort()
            tag_texts = [get_required_bg3_attribute(e, 'TagText', value_name='handle') for e in tagged_text.findall('./children/node[@id="TagTexts"]/children/node[@id="TagText"]')]
            tag_texts.sort()
            result.append(''.join(tags) + ','.join(tag_texts))
        return '|'.join(result)


    @staticmethod
    def compare_dialog_nodes(a: XmlElement, b: XmlElement) -> bool:
        return attrs_to_str(a) == attrs_to_str(b) \
            and dialog_differ.get_dialog_children(a) == dialog_differ.get_dialog_children(b) \
            and dialog_differ.get_dialog_flags(a) == dialog_differ.get_dialog_flags(b) \
            and dialog_differ.get_dialog_texts(a) == dialog_differ.get_dialog_texts(b)



from __future__ import annotations

import os
import uuid
import xml.etree.ElementTree as et

from ._files import game_file
from ._common import get_bg3_attribute


class gossips_object:
    __file: game_file
    __gossips: et.Element

    __gossips_by_name: dict[str, et.Element]
    __gossips_by_uuid: dict[str, et.Element]
    __gossips_by_dialog_uuid: dict[str, et.Element]

    def __init__(self, gamefile: game_file) -> None:
        self.__file = gamefile
        g = self.__file.root_node.findall("./region[@id='Gossips']/node[@id='root']/children")
        if len(g) == 0 or len(g[0]) == 0:
            raise RuntimeError(f"No gossips found in {self.__file.relative_file_path}")
        self.__gossips = g[0]
        self.__gossips_by_name = dict[str, et.Element]()
        self.__gossips_by_uuid = dict[str, et.Element]()
        self.__gossips_by_dialog_uuid = dict[str, et.Element]()
        for gossip in self.__gossips:
            name = get_bg3_attribute(gossip, "Name")
            if name:
                self.__gossips_by_name[name] = gossip
            uuid = get_bg3_attribute(gossip, "UUID")
            if uuid:
                self.__gossips_by_uuid[uuid] = gossip
            uuid = get_bg3_attribute(gossip, "DialogUUID")
            if uuid:
                self.__gossips_by_dialog_uuid[uuid] = gossip

    def __contains__(self, gossip_id: str) -> bool:
        return gossip_id in self.__gossips_by_dialog_uuid or gossip_id in self.__gossips_by_uuid or gossip_id in self.__gossips_by_name

    def get_gossip_by_name(self, name: str) -> et.Element:
        if name not in self.__gossips_by_name:
            raise KeyError(f"Gossip with name {name} doesn't exist in {self.__file.relative_file_path}")
        return self.__gossips_by_name[name]

    def get_gossip_by_uuid(self, gossip_uuid: str) -> et.Element:
        if gossip_uuid in self.__gossips_by_uuid:
            return self.__gossips_by_uuid[gossip_uuid]
        if gossip_uuid in self.__gossips_by_dialog_uuid:
            return self.__gossips_by_dialog_uuid[gossip_uuid]
        raise KeyError(f"Gossip with uuid {gossip_uuid} doesn't exist in {self.__file.relative_file_path}")

    def add_new_gossip(self, gossip_dialog_uuid: str, gossip_name: str, priority: int, conditions: tuple[tuple[str, str], ...] = ()) -> None:
        new_uuid = str(uuid.uuid4())
        if len(conditions) > 0:
            xml_conditions = list[str]()
            xml_conditions.append("""<children><node id="ConditionFlags"><children>""")
            for condition in conditions:
                xml_conditions.append(f"""<node id="{condition[0]}"><attribute id="UUID" type="guid" value="{condition[1]}"/></node>""")
            xml_conditions.append("""</children></node></children>""")
            all_conditions = "".join(xml_conditions)
        else:
            all_conditions = ""
        gossip = et.fromstring(f"""
            <node id="Gossip">
                <attribute id="DialogUUID" type="guid" value="{gossip_dialog_uuid}"/>
                <attribute id="Name" type="FixedString" value="{gossip_name}"/>
                <attribute id="Priority" type="int32" value="{priority}"/>
                <attribute id="Type" type="FixedString" value="PartyBanter"/>
                <attribute id="UUID" type="guid" value="{new_uuid}"/>
                {all_conditions}
            </node>""")
        self.__gossips_by_name[gossip_name] = gossip
        self.__gossips_by_dialog_uuid[gossip_dialog_uuid] = gossip
        self.__gossips.append(gossip)

    def remove_gossip(self, gossip_uuid: str) -> None:
        g = self.get_gossip_by_uuid(gossip_uuid)
        self.__gossips.remove(g)

    def remove_condition_flag(self, gossip_uuid: str, condition: str, condition_uuid: str) -> None:
        g = self.get_gossip_by_uuid(gossip_uuid)
        conditions_node = g.find(f"./children/node[@id='ConditionFlags']/children")
        if conditions_node:
            conditions = conditions_node.findall(f"./node[@id='{condition}']")
            for c in conditions:
                c_uuid = get_bg3_attribute(c, "UUID")
                if condition_uuid == c_uuid:
                    conditions_node.remove(c)
                    return
        raise RuntimeError(f"Failed to remove condition {condition} {condition_uuid} from gossip {gossip_uuid}, file {self.__file.relative_file_path}")

    def add_condition_flag(self, gossip_uuid: str, condition: str, condition_uuid: str) -> None:
        g = self.get_gossip_by_uuid(gossip_uuid)
        conditions_node = g.find(f'./children/node[@id="ConditionFlags"]/children')
        if conditions_node is None:
            children_node = g.find('./children')
            if children_node is None:
                g.append(et.fromstring('<children><children>'))
                children_node = g.find('./children')
                if children_node is None:
                    raise RuntimeError()
            children_node.append(et.fromstring(f'<node id=""><children></children></node>'))
            conditions_node = children_node.find('./node[@id="ConditionFlags"]/children')
            if conditions_node is None:
                raise RuntimeError()
        conditions_node.append(et.fromstring(f"""<node id="{condition}"><attribute id="UUID" type="guid" value="{condition_uuid}"/></node>"""))

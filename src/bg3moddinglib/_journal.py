from __future__ import annotations

import os
import xml.etree.ElementTree as et

from ._common import get_bg3_attribute, get_required_bg3_attribute
from ._files import game_file, game_files, ElementTree
from ._tool import bg3_modding_tool

class quest_step:
    __flag_uuid: str
    __description: str
    __devcomment: str
    __objective: str
    __quest_id: str
    __quest_title: str

    def __init__(self, flag_uuid: str, description: str, devcomment: str, objective: str, quest_id: str, quest_title: str) -> None:
        self.__flag_uuid = flag_uuid
        self.__description = description
        self.__devcomment = devcomment
        self.__objective = objective
        self.__quest_id = quest_id
        self.__quest_title = quest_title

    @property
    def flag_uuid(self) -> str:
        return self.__flag_uuid

    @property
    def description(self) -> str:
        return self.__description

    @property
    def devcomment(self) -> str:
        return self.__devcomment

    @property
    def objective(self) -> str:
        return self.__objective

    @property
    def quest_id(self) -> str:
        return self.__quest_id

    @property
    def quest_title(self) -> str:
        return self.__quest_title


class journal:
    __flags: dict[str, quest_step]

    def __init__(self, tool: bg3_modding_tool) -> None:
        self.__flags = dict[str, quest_step]()
        pak_name = 'Gustav'
        quest_files = [f for f in tool.list(pak_name) if f.endswith('quest_prototypes.lsx')]
        for quest_file in quest_files:
            gf = game_file(tool, quest_file, pak_name = pak_name)
            quests = gf.root_node.findall('./region[@id="Quests"]/node[@id="root"]/children/node[@id="Quest"]')
            for quest in quests:
                quest_id = get_required_bg3_attribute(quest, 'QuestID')
                quest_title = get_bg3_attribute(quest, 'QuestTitle', value_name = 'handle')
                if quest_title is None:
                    quest_title = ''
                quest_steps = quest.findall('./children/node[@id="QuestStep"]')
                for step in quest_steps:
                    flag_uuid = get_required_bg3_attribute(step, 'DialogFlagGUID')
                    description = get_bg3_attribute(step, 'Description', value_name = 'handle')
                    if description is None:
                        description = ''
                    devcomment = get_bg3_attribute(step, 'DevComment')
                    if devcomment is None:
                        devcomment = ''
                    objective = get_bg3_attribute(step, 'Objective')
                    if objective is None:
                        objective = 'NamelessObjective'
                    self.__flags[flag_uuid] = quest_step(flag_uuid, description, devcomment, objective, quest_id, quest_title)

    def get_quest_step(self, flag_uuid: str) -> quest_step:
        if flag_uuid in self.__flags:
            return self.__flags[flag_uuid]
        raise RuntimeError(f'Quest flag {flag_uuid} is not found')

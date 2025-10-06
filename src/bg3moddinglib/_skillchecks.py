from __future__ import annotations

import os
import xml.etree.ElementTree as et

from ._common import get_bg3_handle_attribute, get_required_bg3_attribute, new_random_uuid, set_bg3_attribute
from ._files import game_file, game_files, ElementTree
from ._tool import bg3_modding_tool

class difficulty_class:
    __name: str
    __difficulty: int
    __uuid: str

    def __init__(self, name: str, difficulty: int, uuid: str) -> None:
        self.__name = name
        self.__difficulty = difficulty
        self.__uuid = uuid

    @property
    def name(self) -> str:
        return self.__name

    @property
    def difficulty(self) -> int:
        return self.__difficulty

    @property
    def uuid(self) -> str:
        return self.__uuid

class difficulty_classes:
    __registry: dict[str, difficulty_class]
    __dcs: tuple[difficulty_class, ...]

    def __init__(self, t: bg3_modding_tool) -> None:
        self.__registry = dict[str, difficulty_class]()
        for pak_name in ('Gustav', 'Shared'):
            dc_files = [f for f in t.list(pak_name) if f.endswith('DifficultyClasses.lsx')]
            for dc_file in dc_files:
                gf = game_file(t, dc_file, pak_name=pak_name)
                dcs = gf.root_node.findall('./region[@id="DifficultyClasses"]/node[@id="root"]/children/node[@id="DifficultyClass"]')
                for dc in dcs:
                    dc_uuid = get_required_bg3_attribute(dc, 'UUID')
                    dc_name = get_required_bg3_attribute(dc, 'Name')
                    dc_value = int(get_required_bg3_attribute(dc, 'Difficulties'))
                    self.__registry[dc_uuid] = difficulty_class(dc_name, dc_value, dc_uuid)
        self.__dcs = tuple(self.__registry.values())

    @property
    def values(self) -> tuple[difficulty_class, ...]:
        return self.__dcs

    def get_dc(self, dc_uuid: str) -> difficulty_class:
        if dc_uuid not in self.__registry:
            raise KeyError(f"difficulty class {dc_uuid} doesn't exist")
        return self.__registry[dc_uuid]

from __future__ import annotations

import xml.etree.ElementTree as et

from ._common import get_required_bg3_attribute, get_bg3_attribute
from ._files import game_file, game_files

from typing import Iterable

class string_key:
    __text_handle: str
    __text_version: int
    __identifier: str
    __speaker: str
    __extra_data: str
    __stub: bool

    def __init__(
            self,
            text_handle: str,
            identifier: str,
            /,
            text_version: int = 1,
            speaker: str = "",
            extra_data: str = "",
            stub: bool = True
    ) -> None:
        self.__text_handle = text_handle
        self.__text_version = text_version
        self.__identifier = identifier
        self.__speaker = speaker
        self.__extra_data = extra_data
        self.__stub = stub

    @property
    def text_handle(self) -> str:
        return self.__text_handle

    @property
    def text_version(self) -> int:
        return self.__text_version

    @property
    def identifier(self) -> str:
        return self.__identifier

    @property
    def speaker(self) -> str:
        return self.__speaker

    @property
    def extra_data(self) -> str:
        return self.__extra_data

    @property
    def stub(self) -> bool:
        return self.__stub

    def to_xml(self) -> et.Element:
        return et.fromstring(''.join([
            '<node id="TranslatedStringKey">',
			f'<attribute id="Content" type="TranslatedString" handle="{self.__text_handle}" version="{self.__text_version}" />',
			f'<attribute id="UUID" type="FixedString" value="{self.__identifier}" />',
			f'<attribute id="Speaker" type="FixedString" value="{self.__speaker}" />',
			f'<attribute id="ExtraData" type="LSString" value="{self.__extra_data}" />',
			f'<attribute id="Stub" type="bool" value="{self.__stub}" />',
			'</node>']))

class string_keys:
    __file: game_file
    __string_keys_node: et.Element
    __string_keys: list[string_key]
    __index_by_id: dict[str, string_key]
    __index_by_handle: dict[str, string_key]


    def __init__(self, gf: game_file) -> None:
        self.__file = gf
        root = gf.xml.getroot()
        if root is None:
            raise RuntimeError(f'Corrupt translated string keys file: {gf.relative_file_path}')
        string_keys_node = root.find('./region[@id="TranslatedStringKeys"]/node[@id="TranslatedStringKeys"]/children')
        if string_keys_node is None:
            raise RuntimeError(f'Corrupt translated string keys file: {gf.relative_file_path}')
        self.__string_keys_node = string_keys_node
        self.__string_keys = list[string_key]()
        self.__index_by_id = dict[str, string_key]()
        self.__index_by_handle = dict[str, string_key]()
        nodes = self.__string_keys_node.findall('./node[@id="TranslatedStringKey"]')
        for node in nodes:
            text_handle = get_required_bg3_attribute(node, 'Content', value_name = 'handle')
            text_version = get_required_bg3_attribute(node, 'Content', value_name = 'version')
            identifier = get_required_bg3_attribute(node, 'UUID')
            speaker = get_bg3_attribute(node, 'Speaker')
            extra_data = get_bg3_attribute(node, 'ExtraData')
            stub = get_bg3_attribute(node, 'Stub')
            text_version = 1 if text_version is None else int(text_version)
            speaker = "" if speaker is None else speaker
            extra_data = "" if extra_data is None else extra_data
            stub = True if stub is None else bool(stub)
            sk = string_key(text_handle, identifier, text_version = text_version, speaker = speaker, extra_data = extra_data, stub = stub)
            self.__string_keys.append(sk)
            self.__index_by_id[sk.identifier] = sk
            self.__index_by_handle[sk.text_handle] = sk

    @property
    def file(self) -> game_file:
        return self.__file

    @property
    def string_keys(self) -> Iterable[string_key]:
        return tuple(self.__string_keys)

    def get_string_key(self, id: str) -> string_key | None:
        if id in self.__index_by_id:
            return self.__index_by_id[id]
        if id in self.__index_by_handle:
            return self.__index_by_handle[id]
        return None

    def add_string_key(self, text_handle: str, identifier: str, /, text_version: int = 1) -> None:
        if text_handle in self.__index_by_handle:
            raise KeyError(f'Duplicate handle {text_handle} in {self.__file.relative_file_path}')
        if identifier in self.__index_by_id:
            raise KeyError(f'Duplicate identifier {identifier} in {self.__file.relative_file_path}')
        sk = string_key(text_handle, identifier, text_version = text_version)
        self.__string_keys_node.append(sk.to_xml())
        self.__string_keys.append(sk)
        self.__index_by_handle[sk.text_handle] = sk
        self.__index_by_id[sk.identifier] = sk

    def delete_string_key(self, identifier: str) -> None:
        if identifier not in self.__index_by_id:
            if identifier not in self.__index_by_handle:
                raise KeyError(f'A translated string key with identifier f{identifier} does not exist')
            else:
                sk = self.__index_by_handle[identifier]
        else:
            sk = self.__index_by_id[identifier]
        for node in self.__string_keys_node.findall('./node[@id="TranslatedStringKey"]'):
            if get_required_bg3_attribute(node, 'UUID') == sk.identifier:
                self.__string_keys_node.remove(node)
                self.__string_keys.remove(sk)
                del self.__index_by_handle[sk.text_handle]
                del self.__index_by_id[sk.identifier]
                return
        raise RuntimeError(f'An xml node was not found for translated string key {sk.text_handle} {sk.identifier}')

    @staticmethod
    def create_new(gfs: game_files, name: str) -> string_keys:
        f = gfs.add_new_file(f'Mods/ModNameHere/Localization/{name}.lsf', is_mod_specific = True)
        root_node = f.xml.getroot()
        if root_node.find('./region[@id="TranslatedStringKeys"]') is None:
            root_node.append(et.fromstring('<version major="4" minor="8" revision="0" build="10" lslib_meta="v1,bswap_guids,lsf_keys_adjacency" />'))
            root_node.append(et.fromstring('<region id="TranslatedStringKeys"><node id="TranslatedStringKeys"><children></children></node></region>'))
        return string_keys(f)

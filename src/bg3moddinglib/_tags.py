from __future__ import annotations

import os
import xml.etree.ElementTree as et

from ._common import get_bg3_handle_attribute, get_required_bg3_attribute, new_random_uuid, set_bg3_attribute
from ._files import game_file, game_files, ElementTree
from ._tool import bg3_modding_tool

from typing import Iterable

LOCAL_FLAG = 1
OBJECT_FLAG = 4
GLOBAL_FLAG = 5

class tag_object:
    __file: game_file
    __description: str
    __display_description: tuple[str, int]
    __display_name: tuple[str, int]
    __icon: str
    __name: str
    __uuid: str
    __categories: list[str]

    def __init__(
            self,
            f: game_files | game_file | None,
            /,
            description: str | None = None,
            display_description: tuple[str, int] | None = None,
            display_name: tuple[str, int] | None = None,
            icon: str | None = None,
            name: str | None = None,
            tag_uuid: str | None = None,
            categories: list[str] | None = None,
    ) -> None:
        if isinstance(f, game_files):
            if tag_uuid is None:
                raise RuntimeError("tag_uuid cannot be None")
            if description is None:
                raise RuntimeError("description cannot be None")
            if display_description is None:
                raise RuntimeError("display_description cannot be None")
            if display_name is None:
                raise RuntimeError("display_name cannot be None")
            if name is None:
                raise RuntimeError("name cannot be None")
            if categories is None or len(categories) == 0:
                raise RuntimeError("categories cannot be None or empty")
            self.__description = description
            self.__display_description = display_description
            self.__display_name = display_name
            self.__icon = icon if icon is not None else ""
            self.__name = name
            self.__categories = categories
            self.__file = f.add_new_file(f'Public/Shared/Tags/{tag_uuid}.lsf')
            root_node = self.__file.root_node
            root_node.append(et.fromstring('<version major="4" minor="0" revision="0" build="58" lslib_meta="v1,bswap_guids,lsf_keys_adjacency" />'))
            root_node.append(et.fromstring('<region id="Tags"><node id="Tags"><children><node id="Categories"><children></children></node></children></node></region>'))
            tag_node = root_node.find('./region[@id="Tags"]/node[@id="Tags"]')
            if tag_node is None:
                raise RuntimeError("bad xml object")
            set_bg3_attribute(tag_node, "Description", self.__description, attribute_type = "LSString")
            set_bg3_attribute(tag_node, "DisplayDescription", self.__display_description[0], attribute_type = "TranslatedString", version = self.__display_description[1])
            set_bg3_attribute(tag_node, "DisplayName", self.__display_name[0], attribute_type = "TranslatedString", version = self.__display_name[1])
            set_bg3_attribute(tag_node, "Icon", self.__icon, attribute_type = "FixedString")
            set_bg3_attribute(tag_node, "Name", self.__name, attribute_type = "FixedString")
            set_bg3_attribute(tag_node, "UUID", self.__uuid, attribute_type = "guid")
            categories_node = root_node.find('./region[@id="Tags"]/node[@id="Tags"]/children/node[@id="Categories"]/children')
            if categories_node is None:
                raise RuntimeError("bad xml object")
            for category in categories:
                categories_node.append(et.fromstring(f'<node id="Category"><attribute id="Name" type="LSString" value="{category}" /></node>'))
        elif isinstance(f, game_file):
            self.__file = f
            root_node = f.xml.getroot()
            if isinstance(root_node, et.Element):
                node = root_node.find('./region[@id="Tags"]/node[@id="Tags"]')
                if node is None:
                    node = root_node.find('./region[@id="Tags"]/node[@id="root"]')
                    if node is None:
                        raise RuntimeError(f"bad xml object in file {f.relative_file_path}")
                self.__description = get_required_bg3_attribute(node, "Description")
                self.__display_description = get_bg3_handle_attribute(node, "DisplayDescription")
                self.__display_name = get_bg3_handle_attribute(node, "DisplayName")
                self.__icon = get_required_bg3_attribute(node, "Icon")
                self.__name = get_required_bg3_attribute(node, "Name")
                self.__uuid = get_required_bg3_attribute(node, "UUID")
                categories_nodes = root_node.findall('./region[@id="Tags"]/node[@id="Tags"]/children/node[@id="Categories"]/children/node[@id="Category"]')
                self.__categories = list[str]()
                for category_node in categories_nodes:
                    self.__categories.append(get_required_bg3_attribute(category_node, "Name"))

    @staticmethod
    def create_new(
        files: game_files,
        tag_uuid: str,
        tag_name: str,
        description: str,
        display_description_handle: tuple[str, int],
        display_name_handle: tuple[str, int],
        categories: Iterable[str],
        /,
        icon: str = ""
    ) -> tag_object:
        gf = files.add_new_file(f'Public/ModNameHere/Tags/{tag_uuid}.lsf', is_mod_specific = True)
        gf.root_node.append(et.fromstring('<version major="4" minor="0" revision="0" build="58" lslib_meta="v1,bswap_guids,lsf_keys_adjacency" />'))
        xml_categories = ''.join([f'<node id="Category"><attribute id="Name" type="LSString" value="{category}" /></node>' for category in categories])
        gf.root_node.append(et.fromstring(''.join((
            '<region id="Tags"><node id="Tags">',
            f'<attribute id="Description" type="LSString" value="{description}" />',
			f'<attribute id="DisplayDescription" type="TranslatedString" handle="{display_description_handle[0]}" version="{display_description_handle[1]}" />',
			f'<attribute id="DisplayName" type="TranslatedString" handle="{display_name_handle[0]}" version="{display_name_handle[1]}" />',
			f'<attribute id="Icon" type="FixedString" value="{icon}" />',
			f'<attribute id="Name" type="FixedString" value="{tag_name}" />',
			f'<attribute id="UUID" type="guid" value="{tag_uuid}" />',
            f'<children><node id="Categories"><children>{xml_categories}</children></node></children></node></region>'
        ))))
        return tag_object(gf)

    @property
    def xml(self) -> ElementTree:
        return self.__file.xml

    @property
    def root_node(self) -> et.Element[str]:
        return self.__file.xml.getroot()

    @property
    def description(self) -> str:
        return self.__description

    @property
    def display_description(self) -> str:
        return self.__display_description[0]

    @property
    def display_description_version(self) -> int:
        return self.__display_description[1]

    @property
    def display_name(self) -> str:
        return self.__display_name[0]

    @property
    def display_name_version(self) -> int:
        return self.__display_name[1]

    @property
    def icon(self) -> str:
        return self.__icon

    @property
    def name(self) -> str:
        return self.__name

    @property
    def tag_uuid(self) -> str:
        return self.__uuid

    @property
    def categories(self) -> tuple[str, ...]:
        return tuple(self.__categories)

class tag_registry:
    __tool: bg3_modding_tool
    __registry: dict[str, tuple[str, str]]
    __cache: dict[str, tag_object]

    def __init__(self, tool: bg3_modding_tool) -> None:
        self.__tool = tool
        self.__registry = dict[str, tuple[str, str]]()
        self.__cache = dict[str, tag_object]()
        try:
            for pak_name in ('Gustav', 'Shared', 'GustavX'):
                tag_files = [f for f in self.__tool.list(pak_name) if '/Tags/' in f]
                for tag_file in tag_files:
                    flag_uuid = os.path.basename(tag_file)[:-4]
                    self.__registry[flag_uuid] = pak_name, tag_file
        except:
            pass

    def add_tags_to_registry(self, pak_name: str) -> None:
        tag_files = [f for f in self.__tool.list(pak_name) if '/Tags/' in f]
        for tag_file in tag_files:
            tag_uuid = os.path.basename(tag_file)[:-4]
            self.__registry[tag_uuid] = pak_name, tag_file


    def get_tag(self, tag_uuid: str) -> tag_object:
        if tag_uuid in self.__cache:
            return self.__cache[tag_uuid]
        if tag_uuid not in self.__registry:
            raise KeyError(f'tag {tag_uuid} is not found')
        pak_name, tag_file = self.__registry[tag_uuid]
        result = tag_object(game_file(self.__tool, tag_file, pak_name = pak_name))
        self.__cache[tag_uuid] = result
        return result

from __future__ import annotations

import bg3moddinglib as bg3

from .context import files
from .flags import *


############################################################################
# Create a root template for the mod's author note to the player
############################################################################


def create_new_book_root_template(
        root_template_uuid: str,
        parent_template_uuid: str,
        name: str,
        stats: str,
        display_name: tuple[str, int],
        on_use_description: tuple[str, int],
        book_id: str,
        text_handle: tuple[str, int],
        /,
        is_story_item: bool = False
) -> None:
    gf = files.add_new_file(f'Public/ModNameHere/RootTemplates/{root_template_uuid}.lsf', is_mod_specific = True)
    if gf.xml is None:
        raise RuntimeError('Failed to create a new root template')
    gf.xml.getroot().append(bg3.et.fromstring('<version major="4" minor="8" revision="0" build="10" lslib_meta="v1,bswap_guids,lsf_keys_adjacency" />'))
    gf.xml.getroot().append(bg3.et.fromstring(f"""
        <region id="Templates">
            <node id="Templates">
                <children>
                    <node id="GameObjects">
                        <attribute id="MapKey" type="FixedString" value="{root_template_uuid}" />
                        <attribute id="Name" type="LSString" value="{name}" />
                        <attribute id="LevelName" type="FixedString" value="" />
                        <attribute id="Type" type="FixedString" value="item" />
                        <attribute id="ParentTemplateId" type="FixedString" value="{parent_template_uuid}" />
                        <attribute id="DisplayName" type="TranslatedString" handle="{display_name[0]}" version="{display_name[1]}" />
                        <attribute id="Stats" type="FixedString" value="{stats}" />
                        <attribute id="StoryItem" type="bool" value="{is_story_item}" />
                        <attribute id="OnUseDescription" type="TranslatedString" handle="{on_use_description[0]}" version="{on_use_description[1]}" />
                        <children>
                            <node id="OnUsePeaceActions">
                                <children>
                                    <node id="Action">
                                        <attribute id="ActionType" type="int32" value="11" />
                                        <children>
                                            <node id="Attributes">
                                                <attribute id="Animation" type="FixedString" value="" />
                                                <attribute id="Conditions" type="LSString" value="" />
                                                <attribute id="BookId" type="FixedString" value="{book_id}" />
                                            </node>
                                        </children>
                                    </node>
                                </children>
                            </node>
                        </children>
                    </node>
                </children>
            </node>
        </region>
        """))
    books = bg3.string_keys.create_new(files, 'Misc')
    books.add_string_key(text_handle[0], book_id, text_version = text_handle[1])


def create_mod_author_note() -> None:
    compat_template_uuid = '28921aea-3ee6-458f-9760-b6e35deb609c'
    create_new_book_root_template(
        compat_template_uuid,
        'c0de891b-f804-4d89-953d-97c5dcd54946',
        'BOOK_ReallyShadowheart_A_Note_From_Stan_Compat',
        'OBJ_Scroll',
        ('h4b4ff284g5083g5e63g9adfg8de423d3d883', 1),
        ('hb090a2aegd0dfg4f7eg9296g7e57c3f940d8', 1),
        'GLO_A_Note_From_Stan_Compat',
        ('h82afae29g158bg47c3g84d1g61088c55493a', 1),
        is_story_item = True)

    legacy_template_uuid = 'ff8a16ab-ad4c-43d3-b832-b9105a4eec94'
    create_new_book_root_template(
        legacy_template_uuid,
        'c0de891b-f804-4d89-953d-97c5dcd54946',
        'BOOK_ReallyShadowheart_A_Note_From_Stan',
        'OBJ_Scroll',
        ('h4b4ff284g5083g5e63g9adfg8de423d3d883', 1),
        ('hb090a2aegd0dfg4f7eg9296g7e57c3f940d8', 1),
        'GLO_A_Note_From_Stan',
        ('h3f959d1cg8596g3b45g5b51gb0b61a33b9e1', 1),
        is_story_item = True)


def patch_druid_notebook() -> None:
    gf = files.get_file('Gustav', 'Mods/Gustav/Levels/WLD_Main_A/Items/_merged.lsf', mod_specific = True)
    children = gf.xml.find('./region[@id="Templates"]/node[@id="Templates"]/children')
    if children is None:
        raise RuntimeError("failed to patch Creep's diary in the grove")
    game_objects = children.findall('./node[@id="GameObjects"]')
    creepy_diary = None
    for game_object in game_objects:
        if bg3.get_required_bg3_attribute(game_object, 'Name') != 'S_DEN_DruidDiary':
            children.remove(game_object)
        else:
            creepy_diary = game_object
    if creepy_diary is None:
        raise RuntimeError("failed to find Creep's diary in the grove")

    book_id = 'DEN_DruidLair_CreepyDiary'
    attrs = creepy_diary.find('./children/node[@id="OnUsePeaceActions"]/children/node[@id="Action"]/children/node[@id="Attributes"]')
    if attrs is None:
        raise RuntimeError("failed to read attributes of Creep's diary in the grove")
    bg3.set_bg3_attribute(attrs, 'BookId', book_id)


bg3.add_build_procedure('create_mod_author_note', create_mod_author_note)
bg3.add_build_procedure('patch_druid_notebook', patch_druid_notebook)

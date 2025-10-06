from __future__ import annotations

import bg3moddinglib as bg3

from .context import game_assets
from .flags import *

def customize_shadowheart_character_template() -> None:
    gf = game_assets.files.get_file('Gustav', 'Mods/Gustav/Globals/WLD_Main_A/Characters/_merged.lsf', mod_specific = True)
    children = gf.root_node.find('./region[@id="Templates"]/node[@id="Templates"]/children')
    if children is None:
        raise RuntimeError('Corrupt file: Mods/Gustav/Globals/WLD_Main_A/Characters/_merged.lsf')
    game_objects = children.findall('./node[@id="GameObjects"]')
    shadowheart = None
    for game_object in game_objects:
        if bg3.get_bg3_attribute(game_object, "MapKey") == bg3.SPEAKER_SHADOWHEART:
            shadowheart = game_object
        else:
            children.remove(game_object)
    if shadowheart is None:
        raise RuntimeError('Cannot find root template for Shadowheart')
    #bg3.set_bg3_attribute(shadowheart, 'Title', 'h96c9a6d2gc5bfg4584g8badg883f003abf73', attribute_type = 'TranslatedString', version = 1)
    bg3.set_bg3_attribute(shadowheart, 'Title', 'h744690e1g4055g49b9gba6cgf175c791781f', attribute_type = 'TranslatedString', version = 1)


def customize_shadowheart_origin() -> None:
    gf = game_assets.files.get_file('Gustav', 'Public/GustavDev/Origins/Origins.lsx', mod_specific = True)
    children = gf.root_node.find('./region[@id="Origins"]/node[@id="root"]/children')
    if children is None:
        raise RuntimeError('Corrupt file: Public/GustavDev/Origins/Origins.lsx')
    origins = children.findall('./node[@id="Origin"]')
    shadowheart = None
    for origin in origins:
        if bg3.get_bg3_attribute(origin, "GlobalTemplate") == bg3.SPEAKER_SHADOWHEART:
            shadowheart = origin
        else:
            children.remove(origin)
    if shadowheart is None:
        raise RuntimeError('Cannot find root template for Shadowheart')
    # Urchin 'ac38525a-222b-4280-9c8e-60d5533b675c'
    bg3.set_bg3_attribute(shadowheart, 'BackgroundUUID', 'ac38525a-222b-4280-9c8e-60d5533b675c', attribute_type = 'guid')


def create_inspirations() -> None:
    gf = game_assets.files.add_new_file('Public/ModNameHere/Backgrounds/BackgroundGoals.lsx', is_mod_specific = True)
    gf.root_node.append(bg3.et.fromstring('<version major="4" minor="0" revision="10" build="400"/>'))
    gf.root_node.append(bg3.et.fromstring('<region id="BackgroundGoals"><node id="root"><children></children></node></region>'))
    children = gf.root_node.find('./region[@id="BackgroundGoals"]/node[@id="root"]/children')
    if children is None:
        raise RuntimeError()
    acolyte_stick_to_your_morals = bg3.et.fromstring(''.join([
        '<node id="BackgroundGoal">',
        '<attribute id="BackgroundUUID" type="guid" value="633aa4be-365f-4358-ba56-e2b85f9a88ec"/>',
        '<attribute id="Description" type="TranslatedString" handle="hb5305b06g1ed5g4512gb17egcb10f5094603" version="1"/>',
        '<attribute id="ExperienceReward" type="guid" value="90f636c0-2d85-46d8-9760-30b57c664f4b"/>',
        '<attribute id="InspirationPoints" type="uint32" value="1"/>',
        '<attribute id="RewardLevel" type="uint32" value="9"/>',
        '<attribute id="Title" type="TranslatedString" handle="h68335c1dgfb26g4371ga60bg9f3a875df9d4" version="1"/>',
        '<attribute id="UUID" type="guid" value="9f83d20a-f717-4c3c-891a-6d427ea61062"/>',
        '</node>',
    ]))
    urchin_when_less_is_more = bg3.et.fromstring(''.join([
        '<node id="BackgroundGoal">',
        '<attribute id="BackgroundUUID" type="guid" value="ac38525a-222b-4280-9c8e-60d5533b675c"/>',
        '<attribute id="Description" type="TranslatedString" handle="h4f1100e2g4f18g41bagb467g64e8b4857895" version="1"/>',
        '<attribute id="ExperienceReward" type="guid" value="90f636c0-2d85-46d8-9760-30b57c664f4b"/>',
        '<attribute id="InspirationPoints" type="uint32" value="1"/>',
        '<attribute id="RewardLevel" type="uint32" value="9"/>',
        '<attribute id="Title" type="TranslatedString" handle="he238353eg5b96g4969ga2cage6967553ee2f" version="1"/>',
        '<attribute id="UUID" type="guid" value="ede620ed-a17d-434a-b8a8-fa4538120cd6"/>',
        '</node>',
    ]))
    children.append(acolyte_stick_to_your_morals)
    children.append(urchin_when_less_is_more)


def create_chatty_stool() -> bg3.et.Element[str]:
    # <attribute id="Position" type="fvec3" value="-1.6595 0.0 -1.416" />
    return bg3.et.fromstring("""
<node id="GameObjects">
    <attribute id="Flag" type="uint8" value="1" />
    <attribute id="LevelName" type="FixedString" value="CMP_Bed_Shadowheart_A" />
    <attribute id="MapKey" type="FixedString" value="6296c936-c3eb-486d-bcd3-e6411044bbcd" />
    <attribute id="Name" type="LSString" value="FUR_GEN_Stool_Wood_Poor_Elfsong" />
    <attribute id="TemplateName" type="FixedString" value="2544b579-1b07-4240-9d9e-7cf6e9a6f550" />
    <attribute id="Type" type="FixedString" value="item" />
    <attribute id="_OriginalFileVersion_" type="int64" value="144818875517633112" />
    <children>
        <node id="LayerList">
            <children>
                <node id="Layers">
                    <children>
                        <node id="Object">
                            <attribute id="MapKey" type="FixedString" value="CMP_Bed_Shadowheart_A" />
                        </node>
                    </children>
                </node>
            </children>
        </node>
        <node id="Tags">
            <children>
                <node id="Tag">
                    <attribute id="Object" type="guid" value="87572f4a-8462-4042-a06a-caba1e0eb2cb" />
                </node>
                <node id="Tag">
                    <attribute id="Object" type="guid" value="f1d35c14-6f7c-4a25-9d8f-69a895b173ae" />
                </node>
            </children>
        </node>
        <node id="Transform">
            <attribute id="Position" type="fvec3" value="-1.4 0.0 -1.9" />
            <attribute id="RotationQuat" type="fvec4" value="0 -0.382683 0 0.923880" />
            <attribute id="Scale" type="float" value="1" />
        </node>
    </children>
</node>""")


def initialize_templates_merged_lsf(gf: bg3.game_file) -> bg3.et.Element[str]:
    gf.xml.getroot().append(bg3.et.fromstring('<version major="4" minor="0" revision="9" build="0" lslib_meta="v1,bswap_guids,lsf_adjacency" />'))
    gf.xml.getroot().append(bg3.et.fromstring('<region id="Templates"><node id="Templates"><children></children></node></region>'))
    result = gf.xml.getroot().find('./region[@id="Templates"]/node[@id="Templates"]/children')
    if result is None:
        raise ValueError("this should never happen")
    return result


def modify_act3_elfsong_camp() -> None:
    gf = game_assets.files.get_file('Gustav', 'Mods/GustavDev/Levels/CMP_Bed_Shadowheart_A/Scenery/_merged.lsf', mod_specific = True)

    children = gf.xml.find('./region[@id="Templates"]/node[@id="Templates"]/children')
    if children is None:
        raise RuntimeError("failed to patch Shadowheart's corner in elfsong camp")
    game_objects = children.findall('./node[@id="GameObjects"]')
    shar_banner = None
    for game_object in game_objects:
        if bg3.get_required_bg3_attribute(game_object, 'Name') != 'DEC_BAN_Banner_Shar_Standing_A_000':
            children.remove(game_object)
        else:
            shar_banner = game_object
    if shar_banner is None:
        raise RuntimeError("failed to find Shar banner in Shadowheart's corner in elfsong camp")
    transform = shar_banner.find('./children/node[@id="Transform"]')
    if transform is None:
        raise RuntimeError("failed to find Shar banner's transform in Shadowheart's corner in elfsong camp")
    bg3.set_bg3_attribute(transform, 'Position', '-2.3675537 -15.0 -0.51501465')

    gf = game_assets.files.add_new_file('Mods/ModNameHere/Levels/CMP_Bed_Shadowheart_A/Items/_merged.lsf', is_mod_specific = True)
    initialize_templates_merged_lsf(gf).append(create_chatty_stool())

    gf = game_assets.files.get_file('Gustav', 'Mods/GustavDev/Levels/CMP_BGO_Elfsong_B/Triggers/_merged.lsf', mod_specific = True)
    children = gf.xml.find('./region[@id="Templates"]/node[@id="Templates"]/children')
    if children is None:
        raise RuntimeError("failed to patch Shadowheart's father location in elfsong camp")
    game_objects = children.findall('./node[@id="GameObjects"]')
    arnell_location = None
    emmeline_location = None
    for game_object in game_objects:
        if bg3.get_required_bg3_attribute(game_object, 'Name') == 'S_CAMP_ELFSONG_ShadowheartDad':
            arnell_location = game_object
        elif bg3.get_required_bg3_attribute(game_object, 'Name') == 'S_CAMP_ELFSONG_ShadowheartMom':
            emmeline_location = game_object
        else:
            children.remove(game_object)
            
    if arnell_location is None:
        raise RuntimeError("failed to find Arnell in elfsong camp")
    if emmeline_location is None:
        raise RuntimeError("failed to find Emmeline in elfsong camp")

    bg3.set_bg3_attribute(arnell_location, 'MapKey', '32c982ea-6879-4fdb-b485-1b5020f28e5f')
    bg3.set_bg3_attribute(arnell_location, 'Name', 'S_CAMP_ELFSONG_ReallyShadowheartDad')

    bg3.set_bg3_attribute(emmeline_location, 'MapKey', 'f826b7e7-51ac-41b6-bd1f-69fe2c43320d')
    bg3.set_bg3_attribute(emmeline_location, 'Name', 'S_CAMP_ELFSONG_ReallyShadowheartMom')

    arnell_transform = arnell_location.find('./children/node[@id="Transform"]')
    if arnell_transform is None:
        raise RuntimeError("failed to find Arnell's transform in elfsong camp")
    bg3.set_bg3_attribute(arnell_transform, 'Position', '13.7 3.7 14.2')
    bg3.set_bg3_attribute(arnell_transform, 'RotationQuat', '0.0 0.9998476951563913 0.0 0.0174524064372836')

    emmeline_transform = emmeline_location.find('./children/node[@id="Transform"]')
    if emmeline_transform is None:
        raise RuntimeError("failed to find Emmeline's transform in elfsong camp")
    bg3.set_bg3_attribute(emmeline_transform, 'Position', '14.6 3.7 14.2')
    bg3.set_bg3_attribute(emmeline_transform, 'RotationQuat', '0.0 0.8932144919853736 0.0 0.4496308166788738')


def modify_act3_slums_camp() -> None:
    gf = game_assets.files.get_file('Gustav', 'Mods/GustavDev/Levels/CMP_CTY_Slums_A/Triggers/_merged.lsf', mod_specific = True)

    children = gf.xml.find('./region[@id="Templates"]/node[@id="Templates"]/children')
    if children is None:
        raise RuntimeError("failed to patch Shadowheart's father location in the slums camp")
    game_objects = children.findall('./node[@id="GameObjects"]')
    arnell_location = None
    emmeline_location = None
    for game_object in game_objects:
        if bg3.get_required_bg3_attribute(game_object, 'Name') == 'S_CAMP_SLUMS_Shadowdad':
            arnell_location = game_object
        elif bg3.get_required_bg3_attribute(game_object, 'Name') == 'S_CAMP_SLUMS_Shadowmom':
            emmeline_location = game_object
        else:
            children.remove(game_object)
            
    if arnell_location is None:
        raise RuntimeError("failed to find Arnell in the slums camp")
    if emmeline_location is None:
        raise RuntimeError("failed to find Emmeline in the slums camp")

    bg3.set_bg3_attribute(arnell_location, 'MapKey', 'b5892250-a964-4fe2-8966-9fbc8ea5a45f')
    bg3.set_bg3_attribute(arnell_location, 'Name', 'S_CAMP_FARM_ReallyShadowheartDad')

    bg3.set_bg3_attribute(emmeline_location, 'MapKey', 'b5abe3b2-a606-4377-b92e-9dca272353fc')
    bg3.set_bg3_attribute(emmeline_location, 'Name', 'S_CAMP_FARM_ReallyShadowheartMom')

    arnell_transform = arnell_location.find('./children/node[@id="Transform"]')
    if arnell_transform is None:
        raise RuntimeError("failed to find Arnell's transform in the slums camp")
    bg3.set_bg3_attribute(arnell_transform, 'Position', '-34.5 4.5 -29.0')
    bg3.set_bg3_attribute(arnell_transform, 'RotationQuat', '0.0 0.9222009716704518 0.0 0.3867109616368206')
    #bg3.set_bg3_attribute(arnell_transform, 'Position', '-36.092 4.5 -26.72')
    #bg3.set_bg3_attribute(arnell_transform, 'RotationQuat', '0 -0.98473793 0 0.17404416')

    emmeline_transform = emmeline_location.find('./children/node[@id="Transform"]')
    if emmeline_transform is None:
        raise RuntimeError("failed to find Emmeline's transform in the slums camp")
    bg3.set_bg3_attribute(emmeline_transform, 'Position', '-35.25 4.5 -29.0')
    bg3.set_bg3_attribute(emmeline_transform, 'RotationQuat', '0.0 0.9850342141597025 0.0 0.17235891893017108')
    #bg3.set_bg3_attribute(emmeline_transform, 'Position', '-37.292 4.5 -26.72')
    #bg3.set_bg3_attribute(emmeline_transform, 'RotationQuat', '0 -0.9085717 0 0.41772893')


bg3.add_build_procedure('create_inspirations', create_inspirations)
bg3.add_build_procedure('modify_act3_slums_camp', modify_act3_slums_camp)
bg3.add_build_procedure('modify_act3_elfsong_camp', modify_act3_elfsong_camp)
#bg3.add_build_procedure('customize_shadowheart_character_template', customize_shadowheart_character_template)
#bg3.add_build_procedure('customize_shadowheart_origin', customize_shadowheart_origin)

from __future__ import annotations

import bg3moddinglib as bg3

from .assets import ASSETS_OVERRIDES
from .context import game_assets
from .flags import *

OVERRIDES_LOOKUP_MAP: dict[str, str]

def create_overrides_lookup_map() -> dict[str, str]:
    result = dict[str, str]()
    index = game_assets.index
    for dialog_name, new_uuids in ASSETS_OVERRIDES.items():
        if 'dialog_uuid' in new_uuids:
            entry = index.get_entry(dialog_name)
            result[entry['dialog_uuid']] = new_uuids['dialog_uuid']
    return result


def get_dialog_uuid(dialog_name: str) -> str:
    dialog_uuid = game_assets.index.get_entry(dialog_name)['dialog_uuid']
    if bg3.feature_enabled('override', True, False):
        if dialog_uuid in OVERRIDES_LOOKUP_MAP:
            return OVERRIDES_LOOKUP_MAP[dialog_uuid]
    return dialog_uuid


def add_dialog_dependency(ab: bg3.dialog_asset_bundle, dependency_uuid: str) -> None:
    dialog_res = game_assets.get_dialog_resource(ab.modded_dialog_uuid)
    child_resources = dialog_res.findall('./children/node[@id="childResources"]')
    for child_resource in child_resources:
        resource_uuid = bg3.get_bg3_attribute(child_resource, 'Object')
        if resource_uuid == dependency_uuid:
            return
    children = dialog_res.find('./children')
    if children is not None:
        children.append(bg3.et.fromstring(f'<node id="childResources"><attribute id="Object" type="guid" value="{dependency_uuid}" /></node>'))


def override_nested_dialogs_in_dialog(dialog_name: str) -> None:
    ab = game_assets.get_modded_dialog_asset_bundle(dialog_name)
    d = bg3.dialog_object(ab.dialog)
    nested_overides = False
    for node in d.get_dialog_nodes():
        nested_uuid = bg3.get_bg3_attribute(node, 'NestedDialogNodeUUID')
        if nested_uuid is not None and nested_uuid in OVERRIDES_LOOKUP_MAP:
            new_nested_uuid = OVERRIDES_LOOKUP_MAP[nested_uuid]
            bg3.set_bg3_attribute(node, 'NestedDialogNodeUUID', new_nested_uuid)
            nested_overides = True
    if nested_overides:
        dialog_uuid = game_assets.index.get_entry(dialog_name)['dialog_uuid']
        if dialog_uuid in OVERRIDES_LOOKUP_MAP:
            dialog_res = game_assets.get_dialog_resource(OVERRIDES_LOOKUP_MAP[dialog_uuid])
            child_resources = dialog_res.findall('./children/node[@id="childResources"]')
            for child_resource in child_resources:
                resource_uuid = bg3.get_bg3_attribute(child_resource, 'Object')
                if resource_uuid is not None and resource_uuid in OVERRIDES_LOOKUP_MAP:
                    new_resource_uuid = OVERRIDES_LOOKUP_MAP[resource_uuid]
                    bg3.set_bg3_attribute(child_resource, 'Object', new_resource_uuid)


def override_nested_dialogs() -> None:
    dialog_names = (
        'Shadowheart_InParty',
        'ShadowHeart_InPartyEND',
        'ShadowHeart_InParty2_Nested_BackgroundChapter',
        'ShadowHeart_InParty2_Nested_CityChapter',
        'ShadowHeart_InParty2_Nested_DefaultChapter',
        'ShadowHeart_InParty2_Nested_OriginChapter',
        'ShadowHeart_InParty2_Nested_Romance',
        'ShadowHeart_InParty2_Nested_ShadowCurseChapter',
        'ShadowHeart_InParty2_Nested_ShadowheartHug',
        'ShadowHeart_InParty2_Nested_ShadowheartKiss',
        'ShadowHeart_InParty2_Nested_SharranChapter',
        'Shadowheart_InParty_Nested_TopicalGreetings',
    )
    for dialog_name in dialog_names:
        override_nested_dialogs_in_dialog(dialog_name)


OVERRIDES_LOOKUP_MAP = create_overrides_lookup_map()

bg3.add_build_procedure('override_nested_dialogs', override_nested_dialogs, 'override')

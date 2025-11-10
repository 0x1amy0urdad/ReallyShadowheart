from __future__ import annotations

import bg3moddinglib as bg3

from .context import game_assets
from .dialog_overrides import add_dialog_dependency, get_dialog_uuid
from .flags import *


def create_low_hp_tav_dialog() -> None:
    ab = game_assets.get_modded_dialog_asset_bundle('ShadowHeart_InParty')
    d = bg3.dialog_object(ab.dialog)

    speaker_idx_shadowheart = d.get_speaker_slot_index(bg3.SPEAKER_SHADOWHEART)
    

bg3.add_build_procedure('create_low_hp_tav_dialog', create_low_hp_tav_dialog)

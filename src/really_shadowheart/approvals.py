from __future__ import annotations

import bg3moddinglib as bg3

from .context import get_context
from .flags import *

def new_hairstyle_approval() -> None:
    game_assets = get_context().assets

    ########################################################################################
    # ShadowHeart_InParty2_Nested_ShadowCurseChapter.lsf
    # Wyll and Shadowheart nodes are mixed up, this fixes that
    ########################################################################################

    ab = game_assets.get_modded_dialog_asset_bundle('ShadowHeart_InParty2_Nested_ShadowCurseChapter')
    d = bg3.dialog_object(ab.dialog)

    love_it_reaction = bg3.reaction_object.create_new(game_assets.files, { bg3.SPEAKER_SHADOWHEART: +3 })

    # Shadowheart: Be honest... what do you think of the new look?
    # Tav:         I love it.
    d.set_approval_rating('23f65c40-f744-4261-92db-b5fbaf368bdf', love_it_reaction.uuid)

bg3.add_build_procedure('new_hairstyle_approval', new_hairstyle_approval)
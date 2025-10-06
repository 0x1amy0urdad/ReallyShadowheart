from __future__ import annotations

import bg3moddinglib as bg3

from .context import game_assets
from .flags import *

##################################################
# Changes from Wyll's Good Manners
# Wyll_InParty2.lsf
##################################################

def patch_wyll_greetings() -> None:
    # try:
    #     # Patch 7
    #     d = bg3.dialog_object(files.get_file('Patch7_Hotfix3', 'Mods/GustavDev/Story/DialogsBinary/Companions/Wyll_InParty2.lsf'))
    # except:
    #     # Patch 8
    #     d = bg3.dialog_object(files.get_file('Gustav', 'Mods/GustavDev/Story/DialogsBinary/Companions/Wyll_InParty2.lsf'))

    ab = game_assets.get_modded_dialog_asset_bundle('Wyll_InParty')
    d = bg3.dialog_object(ab.dialog)

    slot_idx_tav = d.get_speaker_slot_index(bg3.SPEAKER_PLAYER)
    slot_idx_wyll = d.get_speaker_slot_index(bg3.SPEAKER_WYLL)

    d.remove_root_node('4abc86e9-690c-49a5-af34-bf5982af3e65')
    d.remove_root_node('fb849cf5-880d-779a-46b1-7339c3a8b4d6')
    d.remove_root_node('b3fa6380-daa9-27a5-63ed-115c4876bf7d')
    d.remove_root_node('0710c3cd-737a-b234-f9a8-f977fe2142ed')
    d.remove_root_node('aaee1f12-3ae0-e770-d4a9-46662038aa61')
    d.remove_root_node('bbf0bcb4-15d0-fd9a-b8f0-17030f09f8ab')

    # Always good to talk, my friend.
    d.set_dialog_flags(
        'fb849cf5-880d-779a-46b1-7339c3a8b4d6',
        checkflags=(
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_Approval_AtLeast_60_For_Sp2, True, slot_idx_wyll),
            )),
        ))

    # The Blade of Frontiers, at your calling.
    d.set_dialog_flags(
        '4abc86e9-690c-49a5-af34-bf5982af3e65',
        checkflags=(
            bg3.flag_group('Global', (
                bg3.flag(bg3.FLAG_VISITEDREGION_INT_Main_A_ACT_3, False, None),
            )),
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_Approval_AtLeast_60_For_Sp2, True, slot_idx_wyll),
            )),
        ),
        setflags=(
            bg3.flag_group('Object', (
                bg3.flag('d4fd622a-dc87-40ce-7d8f-eab9f2a76fa0', True, slot_idx_tav),
            )),
        ))

    # Well met.
    d.set_dialog_flags(
        'b3fa6380-daa9-27a5-63ed-115c4876bf7d',
        checkflags=(
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_Approval_AtLeast_40_For_Sp2, True, slot_idx_wyll),
            )),
        ))

    # Let's talk.
    d.set_dialog_flags(
        '0710c3cd-737a-b234-f9a8-f977fe2142ed',
        checkflags=(
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_Approval_AtLeast_10_For_Sp2, True, slot_idx_wyll),
            )),
        ))

    # Go ahead.
    d.set_dialog_flags(
        'bbf0bcb4-15d0-fd9a-b8f0-17030f09f8ab',
        checkflags=(
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_Approval_AtLeast_N20_For_Sp2, True, slot_idx_wyll),
            )),        
        ))

    # You've got something to say?
    d.set_dialog_flags('aaee1f12-3ae0-e770-d4a9-46662038aa61', checkflags=())


    d.add_root_node('aaee1f12-3ae0-e770-d4a9-46662038aa61', index=39)
    d.add_root_node('bbf0bcb4-15d0-fd9a-b8f0-17030f09f8ab', index=39) 
    d.add_root_node('0710c3cd-737a-b234-f9a8-f977fe2142ed', index=39)
    d.add_root_node('b3fa6380-daa9-27a5-63ed-115c4876bf7d', index=39)
    d.add_root_node('fb849cf5-880d-779a-46b1-7339c3a8b4d6', index=39)
    d.add_root_node('4abc86e9-690c-49a5-af34-bf5982af3e65', index=39)

bg3.add_build_procedure('patch_wyll_greetings', patch_wyll_greetings)

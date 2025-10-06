from __future__ import annotations

import bg3moddinglib as bg3

from .context import game_assets
from .flags import *

########################################################################################
# When Shadowheart breaks up with Tav/Durge because of Mizora, Halsin, or drow twins,
# there is no specific line for any of those;
# this is a replacement that works for all non-origin break-ups.
########################################################################################

def create_breakup_line() -> None:
    ########################################################################################
    # Dialog: ShadowHeart_InParty2.lsf
    ########################################################################################

    # d = bg3.dialog_object(files.get_file('Gustav', 'Mods/GustavDev/Story/DialogsBinary/Companions/ShadowHeart_InParty2.lsf'))
    # t = bg3.timeline_object(files.get_file('Gustav', 'Public/GustavDev/Timeline/Generated/ShadowHeart_InParty2.lsf'), d)

    ab = game_assets.get_modded_dialog_asset_bundle('ShadowHeart_InParty')
    d = bg3.dialog_object(ab.dialog)
    t = bg3.timeline_object(ab.timeline, d)

    slot_idx_shadowheart = d.get_speaker_slot_index(bg3.SPEAKER_SHADOWHEART)
    slot_idx_tav = d.get_speaker_slot_index(bg3.SPEAKER_PLAYER)

    your_affections_have_drifted_node_uuid = '8e227955-8a68-42da-98b6-3fcff2c2af5f'
    maybe_you_and_i_are_not_meant_to_be_node_uuid = '5f23932d-fe2c-4ea6-8a84-8483f63259dc'
    dialog_continuation_node_uuid = '0251a191-20a0-4ca5-b8c1-d4c1dd386190'

    # Maybe you and I are not meant to be, I don't know. I sense I'll have little time for distractions, moving forward. Especially ones that don't bear fruit.
    d.create_standard_dialog_node(
        maybe_you_and_i_are_not_meant_to_be_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [dialog_continuation_node_uuid],
        bg3.text_content('h03a13c89ge885g4ebcgbc71gb2d502c80f3a', 1),
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(Shadowheart_BreakUp_Notification_Finish.uuid, True, slot_idx_tav),
            )),
            bg3.flag_group('Global', (
                bg3.flag(bg3.FLAG_NIGHT_Shadowheart_Skinnydipping, False, None),
            ))
        ))
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '11.2',
        maybe_you_and_i_are_not_meant_to_be_node_uuid,
        (('11.2', '0e8837db-4344-48d0-9175-12262c73806b'),),
        emotions={
            bg3.SPEAKER_SHADOWHEART: ((0.0, 32, None), (4.76, 16, None), (9.05, 2048, None))
        })

    d.add_child_dialog_node(your_affections_have_drifted_node_uuid, maybe_you_and_i_are_not_meant_to_be_node_uuid)


bg3.add_build_procedure('create_breakup_line', create_breakup_line)

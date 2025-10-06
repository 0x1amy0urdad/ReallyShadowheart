from __future__ import annotations

import bg3moddinglib as bg3

from .context import game_assets
from .flags import *


def patch_minsc_conversations() -> None:
    ########################################################################################
    # Minsc_InParty_Nested_PersonalQuestions.lsf
    ########################################################################################

    ab = game_assets.get_modded_dialog_asset_bundle('Minsc_InParty_Nested_PersonalQuestions')
    d = bg3.dialog_object(ab.dialog)

    speaker_idx_tav = d.get_speaker_slot_index(bg3.SPEAKER_PLAYER)

    # Re-arrange some nodes such that all questions are under the same top level question bank node
    top_level_node_uuid = '9f5fbfe9-5c8e-57ba-f614-b26226380685'
    minsc_queston_bank_node_uuid = 'e49781e1-e65a-4fc8-bcd5-5ceca135acb3'
    nydeshka_node_uuid = '5635d5db-abfd-41ba-b049-f2231b605ba1'
    dumb_node_uuid = '94cf6fd3-6957-4b82-bcc1-6c8ca1ac084d'

    d.delete_child_dialog_node(top_level_node_uuid, nydeshka_node_uuid)
    d.delete_child_dialog_node(top_level_node_uuid, dumb_node_uuid)

    d.add_child_dialog_node(minsc_queston_bank_node_uuid, dumb_node_uuid, 0)
    d.add_child_dialog_node(minsc_queston_bank_node_uuid, nydeshka_node_uuid, 0)

    # Minsc about companions

    shadowheart_node_uuid = '0329ee92-39cb-492e-aa04-62a7b76b9411'
    she_is_a_sharran_no_more_uuid = '6f9a25cc-3ed1-4c89-acdc-8fca42c7ec5d'
    astarion_node_uuid = '23c42e26-f628-411e-ae0a-c55bdce06fd7'
    wyll_node_uuid = '4ca9507c-2d25-4360-96e6-cda3930ad601'
    karlach_node_uuid = '5c6ec9ce-fc67-4c7f-a03f-63549560153b'
    gale_node_uuid = '12f69829-fdd6-4eb4-ad30-05b4638e3419'
    creep_node_uuid = '887ea33a-f860-4ce6-83e0-2b623dd633eb'
    minthara_node_uuid = '6bd998d4-a2de-4f63-a9b4-05a978c02b5f'
    laezel_node_uuid  = '58128ecd-3e81-4033-bd52-6cb6a648a51f'

    # Shadowheart
    d.set_dialog_flags(shadowheart_node_uuid, checkflags = (
        bg3.flag_group('Global', (
            bg3.flag(bg3.FLAG_GLO_Origin_PartOfTheTeam_Shadowheart, True, None),
        )),
        bg3.flag_group('Tag', (
            bg3.flag(bg3.TAG_REALLY_SHADOWHEART, False, speaker_idx_tav),
        )),
    ))
    d.set_dialog_flags(she_is_a_sharran_no_more_uuid, checkflags = (
        bg3.flag_group('Global', (
            bg3.flag(Shadowheart_Turned_Away_From_Shar.uuid, True, None),
        )),
    ))
    # Minsc will comment on Shadowheart even after the conclusion of her questline
    d.delete_child_dialog_node(shadowheart_node_uuid, 'ac598f77-4589-4552-ac56-61f0aa929a8b')


    # Astarion
    d.set_dialog_flags(astarion_node_uuid, checkflags = (
        bg3.flag_group('Global', (
            bg3.flag(bg3.FLAG_GLO_Origin_PartOfTheTeam_Astarion, True, None),
        )),
        bg3.flag_group('Tag', (
            bg3.flag(bg3.TAG_REALLY_ASTARION, False, speaker_idx_tav),
        )),
    ))
    # Minsc will comment on Astarion even after the conclusion of his questline
    d.delete_child_dialog_node(astarion_node_uuid, 'd01acc83-a6fd-4aaa-a3f8-0c68d811ceb6')

    # Wyll
    d.set_dialog_flags(wyll_node_uuid, checkflags = (
        bg3.flag_group('Global', (
            bg3.flag(bg3.FLAG_GLO_Origin_PartOfTheTeam_Wyll, True, None),
        )),
        bg3.flag_group('Tag', (
            bg3.flag(bg3.TAG_REALLY_WYLL, False, speaker_idx_tav),
        )),
    ))

    # Karlach
    d.set_dialog_flags(karlach_node_uuid, checkflags = (
        bg3.flag_group('Global', (
            bg3.flag(bg3.FLAG_GLO_Origin_PartOfTheTeam_Karlach, True, None),
        )),
        bg3.flag_group('Tag', (
            bg3.flag(bg3.TAG_REALLY_KARLACH, False, speaker_idx_tav),
        )),
    ))

    # Gale
    d.set_dialog_flags(gale_node_uuid, checkflags = (
        bg3.flag_group('Global', (
            bg3.flag(bg3.FLAG_GLO_Origin_PartOfTheTeam_Gale, True, None),
        )),
        bg3.flag_group('Tag', (
            bg3.flag(bg3.TAG_REALLY_GALE, False, speaker_idx_tav),
        )),
    ))

    # Creepy guy
    d.set_dialog_flags(creep_node_uuid, checkflags = (
        bg3.flag_group('Global', (
            bg3.flag(bg3.FLAG_GLO_Origin_PartOfTheTeam_Halsin, True, None),
        )),
        bg3.flag_group('Tag', (
            bg3.flag(bg3.TAG_REALLY_HALSIN, False, speaker_idx_tav),
        )),
    ))

    # Minthara
    d.set_dialog_flags(minthara_node_uuid, checkflags = (
        bg3.flag_group('Global', (
            bg3.flag(bg3.FLAG_GLO_Origin_PartOfTheTeam_Minthara, True, None),
        )),
        bg3.flag_group('Tag', (
            bg3.flag(bg3.TAG_REALLY_MINTHARA, False, speaker_idx_tav),
        )),
    ))

    # Lae'zel
    d.set_dialog_flags(laezel_node_uuid, checkflags = (
        bg3.flag_group('Global', (
            bg3.flag(bg3.FLAG_GLO_Origin_PartOfTheTeam_Laezel, True, None),
        )),
        bg3.flag_group('Tag', (
            bg3.flag(bg3.TAG_REALLY_LAEZEL, False, speaker_idx_tav),
        )),
    ))

bg3.add_build_procedure('patch_minsc_conversations', patch_minsc_conversations)

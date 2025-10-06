from __future__ import annotations

import bg3moddinglib as bg3

from .common import create_approval_fork
from .context import game_assets
from .flags import *

################################################################################################
# Various story improvements
################################################################################################

def grove_squirell_encounter_wound_flare() -> None:
    # When Shadowheart succeeds 2x animal handling checks, she'll got the wound flare.

    # d = bg3.dialog_object(files.get_file('Gustav', 'Mods/Gustav/Story/DialogsBinary/Act1/DEN/DEN_General_Squirrel.lsf'))

    ab = game_assets.get_modded_dialog_asset_bundle('DEN_General_Squirrel')
    d = bg3.dialog_object(ab.dialog)

    speaker_idx_player = d.get_speaker_slot_index(bg3.SPEAKER_PLAYER)
    speaker_idx_shadowheart = d.get_speaker_slot_index(bg3.SPEAKER_SHADOWHEART)

    squirell_made_friends_node_uuid = '3ed6ebf3-a4a1-1baf-84d0-938722d5a502'
    squirell_the_trees_are_mine_node_uuid = 'b00f07a6-fb3d-2097-fdeb-ad287d1e07e6'
    #ngh_it_hurts_node_uuid = 'd462597a-8a9e-4884-81dd-fd9b2d65a439'
    ngh_it_hurts_node_uuid = '2ff98782-e74f-487e-a881-32cf830fa960' # existing node
    alias_ngh_it_hurts_node_uuid = 'fa1e16c2-1ae3-493b-a438-62e1ca3d71a8'
    fallback_node_uuid = '87ee6311-043a-428d-86c2-a4d44d8a38f1'
    

    d.create_alias_dialog_node(
        alias_ngh_it_hurts_node_uuid,
        ngh_it_hurts_node_uuid,
        [],
        end_node = True,
        checkflags = (
            bg3.flag_group('Global', (
                bg3.flag(bg3.FLAG_ORI_Shadowheart_State_IncurableWound_Unavailable, False, None),
                bg3.flag(bg3.FLAG_ORI_Shadowheart_State_SavedAnimal, False, None)
            )),
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_REALLY_SHADOWHEART, True, speaker_idx_player),
                bg3.flag(bg3.TAG_AVATAR, False, speaker_idx_player),
            ))
        ),
        setflags = (
            bg3.flag_group('Global', (
                bg3.flag(bg3.FLAG_ORI_Shadowheart_State_SavedAnimal, True, None),
                bg3.flag(bg3.FLAG_ORI_Shadowheart_Event_IncurableWoundFlared, True, None)
            )),
        ))

    d.create_standard_dialog_node(
        fallback_node_uuid,
        bg3.SPEAKER_PLAYER,
        [],
        None,
        end_node = True)

    d.remove_dialog_attribute(squirell_made_friends_node_uuid, 'endnode')
    d.add_child_dialog_node(squirell_made_friends_node_uuid, alias_ngh_it_hurts_node_uuid)
    d.add_child_dialog_node(squirell_made_friends_node_uuid, fallback_node_uuid)

    d.remove_dialog_attribute(squirell_the_trees_are_mine_node_uuid, 'endnode')
    d.add_child_dialog_node(squirell_the_trees_are_mine_node_uuid, alias_ngh_it_hurts_node_uuid)
    d.add_child_dialog_node(squirell_the_trees_are_mine_node_uuid, fallback_node_uuid)


def mean_greetings() -> None:

    ################################################################################################
    # Dialog: ShadowHeart_InParty2.lsf
    ################################################################################################

    ab = game_assets.get_modded_dialog_asset_bundle('ShadowHeart_InParty')
    d = bg3.dialog_object(ab.dialog)

    speaker_idx_shadowheart = d.get_speaker_slot_index(bg3.SPEAKER_SHADOWHEART)

    low_approval_greetings_node_uuid = '35e88436-e6ac-4812-90e4-98dfcd504eb8' # existing node
    alias_low_approval_greetings_node_uuid = '8c3dce88-b540-4669-9ee4-6c8905b5919e'

    d.add_dialog_flags(low_approval_greetings_node_uuid, checkflags = (
        bg3.flag_group('Global', (
            bg3.flag(Really_Shadowheart_Softened_Version.uuid, True, None),
        )),
    ))

    d.create_alias_dialog_node(
        alias_low_approval_greetings_node_uuid,
        low_approval_greetings_node_uuid,
        d.get_children_nodes_uuids(low_approval_greetings_node_uuid),
        checkflags = (
            bg3.flag_group('Global', (
                bg3.flag(Really_Shadowheart_Softened_Version.uuid, False, None),
            )),
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_Approval_AtLeast_10_For_Sp2, False, speaker_idx_shadowheart),
            )
        )),
        root = True
    )
    d.add_root_node_before(low_approval_greetings_node_uuid, alias_low_approval_greetings_node_uuid)


def rejecting_half_illithid() -> None:
    #
    # Tav won't ask that again after picking 'Very well. If your mind is set, I won't try to change it.'
    #

    # d = bg3.dialog_object(files.get_file('Gustav', 'Mods/GustavDev/Story/DialogsBinary/Companions/ShadowHeart_InParty2.lsf'))

    ab = game_assets.get_modded_dialog_asset_bundle('ShadowHeart_InParty')
    d = bg3.dialog_object(ab.dialog)

    speaker_idx_tav = d.get_speaker_slot_index(bg3.SPEAKER_PLAYER)
    speaker_idx_shadowheart = d.get_speaker_slot_index(bg3.SPEAKER_SHADOWHEART)

    tadpole_question_node_uuid = 'e7bd3ce7-2d3d-2e6f-2508-3c61c6d2fe98'
    d.set_dialog_flags(tadpole_question_node_uuid, checkflags = (
        bg3.flag_group('Object', (
            bg3.flag('9c5367df-18c8-4450-9156-b818b9b94975', False, speaker_idx_shadowheart),
            bg3.flag(Tav_Stopped_Asking_Half_Illithid.uuid, False, speaker_idx_tav)
        )),
        bg3.flag_group('Global', (
            bg3.flag('390b8985-7256-42c0-a205-62e5f275d55d', True, None),
            bg3.flag('7c43d181-2bb0-ed4d-5fed-c19752617955', False, None)
        )),
    ))

    #
    # Changes to roll dificulties and flags in the nested dialog.
    #
    # d = bg3.dialog_object(files.get_file('Gustav', 'Mods/GustavDev/Story/DialogsBinary/Companions/ShadowHeart_InParty2_Nested_DefaultChapter.lsf'))

    ab = game_assets.get_modded_dialog_asset_bundle('ShadowHeart_InParty2_Nested_DefaultChapter')
    d = bg3.dialog_object(ab.dialog)

    speaker_idx_tav = d.get_speaker_slot_index(bg3.SPEAKER_PLAYER)
    speaker_idx_shadowheart = d.get_speaker_slot_index(bg3.SPEAKER_SHADOWHEART)

    i_gave_you_my_answer_node_uuid = '753c1025-4f2f-481f-8006-e86641955de4'
    d.set_dialog_flags(i_gave_you_my_answer_node_uuid, setflags = (
        bg3.flag_group('Object', (
            bg3.flag(bg3.FLAG_Shadowheart_InParty_State_EndDialog, True, speaker_idx_tav),
            bg3.flag(bg3.FLAG_GLO_Tadpole_Event_BlockedTadpoleConvinceFailRepeatableApprovalDrain, True, speaker_idx_shadowheart),
            bg3.flag(Shadowheart_Refused_Half_Illithid.uuid, True, speaker_idx_shadowheart)
        )),
    ))

    roll_low_approval_disadv_node_uuid = '393b1628-5ec4-4fec-a6a3-33f122c2f079'
    roll_medium_approval_node_uuid = '84e6bdc4-5163-4448-adb1-01096c25941a'
    roll_high_approval_adv_node_uuid = '9f0a60bb-d7e0-4140-8400-8fa380acf6e7'

    d.set_dialog_attribute(roll_low_approval_disadv_node_uuid, 'DifficultyClassID', bg3.DC_Act3_Hard)
    d.set_dialog_attribute(roll_medium_approval_node_uuid, 'DifficultyClassID', bg3.DC_Act3_Hard)
    d.set_dialog_attribute(roll_high_approval_adv_node_uuid, 'DifficultyClassID', bg3.DC_Act3_Hard)

    consider_the_matter_closed_then_node_uuid = '1e8a616f-87f8-cf3c-274b-8653c9b5a447' # existing node
    alias_consider_the_matter_closed_then_node_uuid = '8c16629d-bd51-46ac-82f6-f72f4390d8c6'
    if_your_mind_is_set_node_uuid = '2a9d6297-5749-484b-8de9-ea589b60495e'
    # d.set_dialog_flags(if_your_mind_is_set_node_uuid, setflags = (
    #     bg3.flag_group('Object', (
    #         bg3.flag(Tav_Stopped_Asking_Half_Illithid.uuid, True, speaker_idx_tav),
    #     )),
    # ))
    d.remove_dialog_attribute(if_your_mind_is_set_node_uuid, 'endnode')
    d.remove_dialog_attribute(if_your_mind_is_set_node_uuid, 'ShowOnce')
    d.add_child_dialog_node(if_your_mind_is_set_node_uuid, alias_consider_the_matter_closed_then_node_uuid)

    d.create_alias_dialog_node(
        alias_consider_the_matter_closed_then_node_uuid,
        consider_the_matter_closed_then_node_uuid,
        [],
        end_node = True,
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_Shadowheart_InParty_State_EndDialog, True, speaker_idx_tav),
                bg3.flag(Tav_Stopped_Asking_Half_Illithid.uuid, True, speaker_idx_tav)
            )),
        ))

    #
    # A new dialog that hits the player with -10 disapproval if they attempt it again
    #
    minus_10_approval = bg3.reaction_object.create_new(files, {bg3.SPEAKER_SHADOWHEART: -10})
    another_attempt_node_uuid = '355b87ab-4775-4cfb-8ba7-adba6c670d49'
    reaction_node_uuid = '335b8123-99a8-4435-a8fd-b6bc4bf30b2e'
    d.create_standard_dialog_node(
        another_attempt_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [reaction_node_uuid],
        None,
        approval_rating_uuid = minus_10_approval.uuid,
        constructor = bg3.dialog_object.GREETING,
        root = True,
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_Shadowheart_InParty_Event_AstralTadpoleStart, True, speaker_idx_tav),
                bg3.flag(Shadowheart_Refused_Half_Illithid.uuid, True, speaker_idx_shadowheart),
            )),
        ),
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(Tav_Stopped_Asking_Half_Illithid.uuid, True, speaker_idx_tav),
                bg3.flag(bg3.FLAG_Shadowheart_InParty_Event_AstralTadpoleStart, False, speaker_idx_tav),
            )),
        ))
    d.create_alias_dialog_node(
        reaction_node_uuid,
        i_gave_you_my_answer_node_uuid,
        [],
        end_node = True,
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_Shadowheart_InParty_State_EndDialog, True, speaker_idx_tav),
                bg3.flag(Tav_Stopped_Asking_Half_Illithid.uuid, True, speaker_idx_tav)
            )),
        ))
    d.add_root_node(another_attempt_node_uuid, index = 0)


def shadowheart_recruitment() -> None:
    reaction_thankful_for_freeing_her = bg3.reaction_object.create_new(files, { bg3.SPEAKER_SHADOWHEART : 3 }, uuid = 'cfbfcb19-0881-438d-8f60-5258b910920f')

    ################################################################################################
    # Shadowheart_Recruitment_Beach
    ################################################################################################
    ab = game_assets.get_modded_dialog_asset_bundle('Shadowheart_Recruitment_Beach')
    d = bg3.dialog_object(ab.dialog)

    speaker_idx_shadowheart = d.get_speaker_slot_index(bg3.SPEAKER_SHADOWHEART)

    all_right_fine_lets_stay_together_node_uuid = 'f4fa187e-18f7-ffec-c52d-7b4507b68b97'
    thank_you_again_for_freeing_me_node_uuid = '942b33b7-e7fc-1680-6c25-e29b01003df3'
    thank_you_again_for_freeing_me_even_if_you_knock_me_node_uuid = 'e53c987f-ce5a-3993-0cc1-3825406ee631'
    lead_the_way_node_uuid = '30e22497-284d-3f6a-c9bb-b779b088c451'
    alias_lead_the_way_node_uuid = '0b212bc1-b15e-4127-b6f7-ed071ed23733'

    d.create_alias_dialog_node(
        alias_lead_the_way_node_uuid,
        lead_the_way_node_uuid,
        [],
        end_node = True,
        checkflags = (
            bg3.flag_group('Global', (
                bg3.flag(Really_Shadowheart_Softened_Version.uuid, False, None),
            )),
        ),
        setflags = (
            bg3.flag_group('Global', (
                bg3.flag(bg3.FLAG_ORI_ShadowHeart_State_IsInParty, True, None),
            )),
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_OriginAddToParty, True, speaker_idx_shadowheart),
                bg3.flag(Shadowheart_Did_Not_Thank_Tav_For_Freeing_Her.uuid, True, speaker_idx_shadowheart),
            )),
        ))

    d.add_child_dialog_node(all_right_fine_lets_stay_together_node_uuid, alias_lead_the_way_node_uuid, 3)

    d.add_dialog_flags(thank_you_again_for_freeing_me_node_uuid, setflags = (
        bg3.flag_group('Object', (
            bg3.flag(Shadowheart_Thanked_For_Freeing_Her.uuid, True, speaker_idx_shadowheart),
        )),
    ))
    d.add_dialog_flags(thank_you_again_for_freeing_me_even_if_you_knock_me_node_uuid, setflags = (
        bg3.flag_group('Object', (
            bg3.flag(Shadowheart_Thanked_For_Freeing_Her.uuid, True, speaker_idx_shadowheart),
        )),
    ))


    # d.delete_child_dialog_node(all_right_fine_lets_stay_together_node_uuid, thank_you_again_for_freeing_me_node_uuid)
    # d.delete_child_dialog_node(all_right_fine_lets_stay_together_node_uuid, thank_you_again_for_freeing_me_even_if_you_knock_me_node_uuid)
    # d.add_child_dialog_node(all_right_fine_lets_stay_together_node_uuid, lead_the_way_node_uuid)

    # d.set_dialog_flags(lead_the_way_node_uuid, checkflags = (), setflags = (
    #     bg3.flag_group('Global', (
    #         bg3.flag(bg3.FLAG_ORI_ShadowHeart_State_IsInParty, True, None),
    #     )),
    #     bg3.flag_group('Object', (
    #         bg3.flag(bg3.FLAG_OriginAddToParty, True, speaker_idx_shadowheart),
    #         bg3.flag(Shadowheart_Did_Not_Thank_Tav_For_Freeing_Her.uuid, True, speaker_idx_shadowheart),
    #     )),
    # ))

    # ill_remember_that_node_uuid = 'b24c2a6c-9a76-30c2-8a78-5263283b7ff9'
    # d.set_dialog_attribute(ill_remember_that_node_uuid, 'ApprovalRatingID', reaction_plus_3.uuid)


    ################################################################################################
    # Shadowheart_Recruitment_Den
    ################################################################################################
    ab = game_assets.get_modded_dialog_asset_bundle('Shadowheart_Recruitment_Den')
    d = bg3.dialog_object(ab.dialog)

    speaker_idx_shadowheart = d.get_speaker_slot_index(bg3.SPEAKER_SHADOWHEART)

    # existing nodes
    time_we_got_moving_node_uuid = '41936517-d657-10da-5d6c-6ab1c4eeb311'
    before_we_go_i_wanted_to_thank_you_node_uuid = 'f1f1916d-f1a3-8ee1-1ee0-62a0891a044a'
    lead_the_way_node_uuid = '85a77590-4032-9e52-4dc4-4c50fcda5aa8'
    alias_lead_the_way_node_uuid = '87eb8566-9a71-4eee-9567-5c5a1ed3a965'

    d.create_alias_dialog_node(
        alias_lead_the_way_node_uuid,
        lead_the_way_node_uuid,
        [],
        end_node = True,
        checkflags = (
            bg3.flag_group('Global', (
                bg3.flag(Really_Shadowheart_Softened_Version.uuid, False, None),
            )),
        ),
        setflags = (
            bg3.flag_group('Global', (
                bg3.flag(bg3.FLAG_ORI_ShadowHeart_State_IsInParty, True, None),
            )),
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_OriginAddToParty, True, speaker_idx_shadowheart),
                bg3.flag(Shadowheart_Did_Not_Thank_Tav_For_Freeing_Her.uuid, True, speaker_idx_shadowheart),
            )),
        ))

    d.add_child_dialog_node(time_we_got_moving_node_uuid, alias_lead_the_way_node_uuid, 4)

    d.add_dialog_flags(before_we_go_i_wanted_to_thank_you_node_uuid, setflags = (
        bg3.flag_group('Object', (
            bg3.flag(Shadowheart_Thanked_For_Freeing_Her.uuid, True, speaker_idx_shadowheart),
        )),
    ))

    # d.delete_child_dialog_node(time_we_got_moving_node_uuid, before_we_go_i_wanted_to_thank_you_node_uuid)
    # d.set_dialog_flags(lead_the_way_node_uuid, checkflags = (), setflags = (
    #     bg3.flag_group('Global', (
    #         bg3.flag(bg3.FLAG_ORI_ShadowHeart_State_IsInParty, True, None),
    #     )),
    #     bg3.flag_group('Object', (
    #         bg3.flag(bg3.FLAG_OriginAddToParty, True, speaker_idx_shadowheart),
    #         bg3.flag(Shadowheart_Did_Not_Thank_Tav_For_Freeing_Her.uuid, True, speaker_idx_shadowheart),
    #     )),
    # ))


    ################################################################################################
    # Shadowheart_InParty
    ################################################################################################
    ab = game_assets.get_modded_dialog_asset_bundle('Shadowheart_InParty')
    d = bg3.dialog_object(ab.dialog)
    t = bg3.timeline_object(ab.timeline, d)

    speaker_idx_shadowheart = d.get_speaker_slot_index(bg3.SPEAKER_SHADOWHEART)
    speaker_idx_tav = d.get_speaker_slot_index(bg3.SPEAKER_PLAYER)

    # existing nodes
    leave_node_uuid = 'd1ce2ce6-36b7-4e36-8b41-4eae545fe827'

    # new nodes
    fork_node_uuid = 'a16042fc-370f-481d-8ad6-838c081b1f08'
    shadowheart_thankful_knocked_node_uuid = '3e0516ed-317d-4f1d-8dae-a623525366e8'
    shadowheart_thankful_den_node_uuid = '8319c8fe-19d1-40fc-bfa3-4adbe9587a76'
    shadowheart_thankful_node_uuid = 'e782ac78-a4d2-4c1b-a9fc-9df029293c90'
    ill_remember_that_node_uuid = '71eabb84-f1f7-4bb3-9207-0430c7aeadf8'
    end_dialog_node_uuid = 'fa89e3bd-9195-45d0-8076-f083afe91d85'

    d.remove_dialog_attribute(leave_node_uuid, 'endnode')
    d.add_child_dialog_node(leave_node_uuid, fork_node_uuid)

    d.create_standard_dialog_node(
        fork_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [
            shadowheart_thankful_knocked_node_uuid,
            shadowheart_thankful_den_node_uuid,
            shadowheart_thankful_node_uuid,
            end_dialog_node_uuid,
        ],
        None)

    # One thing, just before we go. I wanted to thank you again, for freeing me... even if you did knock me unconscious afterwards.
    d.create_standard_dialog_node(
        shadowheart_thankful_knocked_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [ill_remember_that_node_uuid],
        bg3.text_content('h43c2f583ge45ag4804g905cg2a2430f77849', 1),
        checkflags = (
            bg3.flag_group('Global', (
                bg3.flag(bg3.FLAG_ORI_ShadowheartRecruitment_State_ShadowheartKnockedOut, True, None),
            )),
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_TUT_TransformChamber_State_FreedShadowheart, True, speaker_idx_tav),
                bg3.flag(Shadowheart_Thanked_For_Freeing_Her.uuid, False, speaker_idx_shadowheart),
                bg3.flag(bg3.FLAG_Approval_AtLeast_10_For_Sp2, True, speaker_idx_shadowheart),
                bg3.flag(Shadowheart_Did_Not_Thank_Tav_For_Freeing_Her.uuid, True, speaker_idx_shadowheart),
            )),
        ),
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(Shadowheart_Thanked_For_Freeing_Her.uuid, True, speaker_idx_shadowheart),
                bg3.flag(Shadowheart_Did_Not_Thank_Tav_For_Freeing_Her.uuid, False, speaker_idx_shadowheart),
            )),
        ),
        approval_rating_uuid = reaction_thankful_for_freeing_her.uuid)
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '10.05',
        shadowheart_thankful_knocked_node_uuid,
        ((None, '8942c483-83c9-4974-9f47-87cd1dd10828'),),
        emotions = {
            bg3.SPEAKER_SHADOWHEART: (('0.2', 64, 2), ('3.23', 4, None), ('4.5', 16, None), ('7.35', 4, None)),
        },
        phase_duration = '10.5'
    )

    # Before we go, I wanted to thank you, for freeing me aboard the nautiloid.
    d.create_standard_dialog_node(
        shadowheart_thankful_den_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [ill_remember_that_node_uuid],
        bg3.text_content('h0f9733e5g3ca9g417cg9336g11673e3bffdc', 1),
        checkflags = (
            bg3.flag_group('Global', (
                bg3.flag(bg3.FLAG_DEN_PartyProgress_EnteredGrove, True, None),
            )),
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_TUT_TransformChamber_State_FreedShadowheart, True, speaker_idx_tav),
                bg3.flag(Shadowheart_Thanked_For_Freeing_Her.uuid, False, speaker_idx_shadowheart),
                bg3.flag(bg3.FLAG_Approval_AtLeast_10_For_Sp2, True, speaker_idx_shadowheart),
                bg3.flag(Shadowheart_Did_Not_Thank_Tav_For_Freeing_Her.uuid, True, speaker_idx_shadowheart),
            )),
        ),
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(Shadowheart_Thanked_For_Freeing_Her.uuid, True, speaker_idx_shadowheart),
                bg3.flag(Shadowheart_Did_Not_Thank_Tav_For_Freeing_Her.uuid, False, speaker_idx_shadowheart),
            )),
        ),
        approval_rating_uuid = reaction_thankful_for_freeing_her.uuid)
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '6.01',
        shadowheart_thankful_den_node_uuid,
        ((None, '8942c483-83c9-4974-9f47-87cd1dd10828'),),
        emotions = {
            bg3.SPEAKER_SHADOWHEART: (('0.2', 32, 2), ('1.76', 64, 2), ('4.19', 2048, None)),
        },
        phase_duration = '6.5'
    )

    # One thing, just before we go. I wanted to thank you again, for freeing me.
    d.create_standard_dialog_node(
        shadowheart_thankful_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [ill_remember_that_node_uuid],
        bg3.text_content('h8fffc8cagc979g4154g8633gb7771491c819', 1),
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_TUT_TransformChamber_State_FreedShadowheart, True, speaker_idx_tav),
                bg3.flag(Shadowheart_Thanked_For_Freeing_Her.uuid, False, speaker_idx_shadowheart),
                bg3.flag(bg3.FLAG_Approval_AtLeast_10_For_Sp2, True, speaker_idx_shadowheart),
                bg3.flag(Shadowheart_Did_Not_Thank_Tav_For_Freeing_Her.uuid, True, speaker_idx_shadowheart),
            )),
        ),
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(Shadowheart_Thanked_For_Freeing_Her.uuid, True, speaker_idx_shadowheart),
                bg3.flag(Shadowheart_Did_Not_Thank_Tav_For_Freeing_Her.uuid, False, speaker_idx_shadowheart),
            )),
        ),
        approval_rating_uuid = reaction_thankful_for_freeing_her.uuid)
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '7.39',
        shadowheart_thankful_node_uuid,
        ((None, '8942c483-83c9-4974-9f47-87cd1dd10828'),),
        emotions = {
            bg3.SPEAKER_SHADOWHEART: (('0.2', 16, None), ('1.96', 4, None), ('3.94', 64, 2), ('6.41', 16, None)),
        },
        phase_duration = '7.9'
    )

    # It would've been all too easy for you to run right past my pod, but you didn't. I'll remember that.
    d.create_standard_dialog_node(
        ill_remember_that_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [end_dialog_node_uuid],
        bg3.text_content('h62a47aa0g30cfg443bga478g031445fe530c', 1))
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '7.45',
        ill_remember_that_node_uuid,
        ((None, '0e8837db-4344-48d0-9175-12262c73806b'),),
        emotions = {
            bg3.SPEAKER_SHADOWHEART: (('0.2', 2048, None), ('2.13', 64, 2), ('4.53', 4, None)),
        },
        phase_duration = '7.9'
    )

    d.create_standard_dialog_node(
        end_dialog_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [],
        None,
        end_node = True)


def shadowheart_how_am_i_holding_up() -> None:
    ################################################################################################
    # ShadowHeart_InParty2_Nested_DefaultChapter
    ################################################################################################
    ab = game_assets.get_modded_dialog_asset_bundle('ShadowHeart_InParty2_Nested_DefaultChapter')
    d = bg3.dialog_object(ab.dialog)
    t = bg3.timeline_object(ab.timeline, d)

    speaker_idx_shadowheart = d.get_speaker_slot_index(bg3.SPEAKER_SHADOWHEART)
    speaker_idx_tav = d.get_speaker_slot_index(bg3.SPEAKER_PLAYER)

    # existing nodes
    how_am_i_holding_up_node_uuid = '1bf8f704-3f8b-40db-afcf-1d33249114dc'

    no_notes_node_uuid = '476ccb28-b8cb-4e9f-ad7d-1281511c5b24' # No notes. You've exceeded my every expectation.
    quite_splendidly_to_give_credit_where_its_due_node_uuid = 'b8999bec-364f-49b7-8437-73b5dea63a88' # Quite splendidly to give credit where it's due. You and I have shared some good times together, and it seems we have plenty in common...
    youre_a_better_catch_than_id_expected_node_uuid = '40314a62-ab4f-4ea4-b7f4-8cb009db4e45' # You're a better catch than I'd expected to find while fighting for survival in the wilderness.
    youre_doing_just_fine_node_uuid = 'd551f66e-a6cc-4a1a-9aa9-23bf1dcf6f45' # You're doing just fine. After all, I'd scarcely anticipated being courted while fighting for survival in the wilderness.
    dont_be_so_modest_node_uuid = 'c5a5e3d2-27ee-44c3-b8ef-3f5b62939a7a' # How are you holding up? Don't be so modest - I can't remember the last time I met someone like you. Perhaps I never did, and never will again.
    does_it_even_need_to_be_asked_node_uuid = 'ea90260a-2869-44fa-b415-823ddff7d272' # Does it even need to be asked? We're beyond me merely liking you - I think I'm a different person, owing to you.
    had_a_confidante_quite_like_you_node_uuid = '9954ac9c-5a33-4317-b13b-8da2ff2d1a83' # I don't think I've ever had a confidante quite like you - and if I have, I can't remember them.
    its_been_downhill_from_there_node_uuid = 'e1938b71-f1ae-4a18-989f-7ede2d0f1986' # I opened up to you like I have with no one before. We bonded... but it's been downhill from there. Perhaps we can rekindle things, or perhaps not...
    perhaps_we_can_rekindle_things_node_uuid = '3b687214-c692-4c05-971e-dc84f50313eb' # I don't know what to say. You and I shared good times together... but it's been downhill from there. Perhaps we can rekindle things, or perhaps not...
    youve_been_a_surprise_and_not_an_unpleasant_one_node_uuid = '827e28d1-b246-483a-98e4-f35e40e0bf27' # I must admit, you've been a surprise, and not an unpleasant one. Kindred spirits are few and far between for me.
    all_things_considered_youll_do_node_uuid = 'fab5c057-6723-4f2b-8d22-af37c53326fe' # You're not the kind of company I'd keep willingly, but all things considered... you'll do.
    you_can_at_least_soak_up_any_arrows_node_uuid = '36a58ee2-d39a-49c7-b053-06038fab617a' # If nothing else, you can at least soak up any arrows that are loosed at us.

    id_never_have_expected_that_from_a_gith_node_uuid = '10f77221-72ba-4947-ab0d-48cf49cd4a8f' # You saved my life aboard the nautiloid. I'd never have expected that from a gith.
    my_estimations_started_at_a_low_point_gith_node_uuid = '8b80e54e-5131-42e9-807b-cf8a1e8cf966' # My estimations started at a low point as far as you're concerned, gith.

    i_dont_think_id_have_wanted_to_node_uuid = '30bc6851-486e-4eb8-ab18-a4824f05a575' # Even if I could have made it this far without you, I don't think I'd have wanted to.
    and_attractive_company_too_no_less_node_uuid = '11dce6f8-f35c-4d86-a432-9557436705a5' # Considering all we've been through, I think I was very lucky to find such favourable company. And attractive company too, no less.
    and_think_of_how_far_weve_come_together_node_uuid = '97dc9105-f62d-4776-bd4f-1dfea11a846c' # And think of how far we've come together - all the ways from the Hells, back to civilisation.
    weve_already_made_great_strides_node_uuid = '558aff95-f067-4bbb-9157-71c56307fbff' # We've already made great strides - both in distance travelled, and in more personal matters...
    youre_someone_i_can_actually_turn_to_node_uuid = '2a48fa44-256e-4b3d-bb36-b2bb326e3631' # You're someone I can actually turn to, when I don't know what to do.
    trust_isnt_something_that_comes_easily_node_uuid = '05270f98-a894-4d66-84f5-af216e585d26' # Trust isn't something that comes easily to me. But with you... I think I can make an exception.
    what_i_shared_with_you_about_my_past_node_uuid = 'f4865f1f-e164-44f9-9365-8d44d011cd3f' # After all, what I shared with you about my past, about being saved from the wolf... that is not something I would normally even dream of sharing.
    concentrate_on_whats_truly_important_to_me_node_uuid = '079934f5-c4dd-4720-a5b5-2eab18b53620' # Besides, we've come so far now - the end isn't so distant. I may need to concentrate on what's truly important to me.
    # maybe_you_and_i_are_not_meant_to_be_node_uuid = '3e0155b7-bb2f-4f04-b6ff-1beccb0c553e' # Maybe you and I are not meant to be, I don't know. I sense I'll have little time for distractions, moving forward. Especially ones that don't bear fruit.
    how_can_i_do_anything_but_sing_your_praises_node_uuid = '9b2108a2-0313-4230-8259-384a73092ca3' # Besides, you saved my life aboard the nautiloid. How can I do anything but sing your praises?
    i_havent_forgotten_that_you_saved_my_life_node_uuid = '247733ea-7527-438c-b8cd-d5c862d19253' # And I haven't forgotten that you saved my life aboard the nautiloid. Perhaps I'll be able to return the favour at some point.
    pity_youd_started_off_so_well_node_uuid = '38cafe73-5a67-4f86-af7b-c7ccf8e89396' # Pity. You'd started off so well, saving my life aboard the nautiloid. I suppose now I'm seeing the real you.
    
    youve_seemed_reliable_node_uuid = 'dfa07b50-fe30-4f4a-a9e0-941f405327db' # And since then, you've seemed reliable. Maybe I'll have to reevaluate what I think I know about your kind.
    my_suspicions_have_been_confirmed_node_uuid = 'a13eea50-dba1-40fa-820c-7faae7dfc23b' # But since then, well... let's just say some of my suspicions have been confirmed.
    im_not_afraid_to_admit_when_im_wrong_node_uuid = '9349d1c9-f48c-4d73-b409-7211df1d6aa5' # But I'm not afraid to admit when I'm wrong... you seem good company so far.
    the_only_way_is_up_from_there_node_uuid = 'feb24713-e114-4115-bbae-552af376e3dc' # Though I suppose the only way is up from there. You'll do for now.
    im_watching_you_node_uuid = 'ce52e13f-36f4-45f7-bb6e-ec5022db3911' # I'm watching you.
    seems_like_even_those_were_too_high_node_uuid = 'a3338d1a-4348-4b53-9b36-68689c1a03a9' # Seems like even those were too high.

    jump_back_node_uuid = '5dd6ef35-5f32-452f-bc05-0cf67335d4e8'

    # new nodes
    partnered_embarce_durge_node_uuid = '330e93aa-c57f-4ae6-b97a-8100600ae3a4'
    partnered_embarce_durge2_node_uuid = 'a3a53b37-387e-4d23-ac28-9c5516c0055a'

    partnered_approval_80_node_uuid = 'ba14542a-82b5-404e-bf04-3e7b9a9de735'
    partnered_approval_60_node_uuid = 'cbba6c6b-61f1-4a53-89bb-2821f0b2a4e7'
    partnered_approval_40_node_uuid = '2e03eff4-459b-4246-b8c7-f0a2dedbff74'
    partnered_approval_low_node_uuid = 'bc93e31d-de8c-4f27-965b-7322eba8230a'

    dating_approval_80_node_uuid = '21bdb7ef-4387-47a8-af56-5a138d1c0e27'
    dating_approval_60_non_confidante_node_uuid = 'b89d0f95-c52e-49a8-ad02-4c74043b6bb7'
    dating_approval_60_node_uuid = '79676ee7-e705-4a16-8e99-cb04cce4b167'
    dating_approval_40_node_uuid = '57c1470e-0a98-49c4-ac5f-3cf9bdc8183b'
    dating_approval_low_node_uuid = '36cc4b51-4cc3-4623-9c61-9e260038623a'

    approval_80_node_uuid = 'c4ff2fe3-7ce3-4105-81c2-4ea622e42a77'
    approval_60_node_uuid = '05806617-5528-428a-b947-4626715bcf2d'
    approval_40_node_uuid = 'e371f0e8-5814-47f5-875b-bd7ac87b84b0'
    approval_20_node_uuid = 'b33f7210-74b9-4230-a5cf-4fa24ff6e062'
    approval_0_node_uuid = '37c9de53-79ad-47d3-b80c-d017aea98339'
    approval_low_node_uuid = '4982a870-8594-47bf-a731-2ae79e93fadd'

    gith_approval_saved_node_uuid = '72531db9-b226-40f0-aa1e-17c32f6a7642'
    gith_approval_not_saved_node_uuid = '06dd1df1-ab28-460e-9967-676089601cab'

    # new container nodes
    responses_fork_node_uuid = '7b7293a3-45cf-494a-947f-72f9b5cc6664'
    modded_responses_node_uuid = 'd49150dc-1e66-45f5-964c-40a6e0a4d177'
    vanilla_responses_node_uuid = '34041426-080a-437e-86b4-1f0be81b9ad2'

    d.create_standard_dialog_node(
        responses_fork_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [modded_responses_node_uuid, vanilla_responses_node_uuid],
        None)
    d.create_standard_dialog_node(
        modded_responses_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [
            partnered_embarce_durge_node_uuid,
            partnered_approval_80_node_uuid,
            partnered_approval_60_node_uuid,
            partnered_approval_40_node_uuid,
            partnered_approval_low_node_uuid,
            dating_approval_80_node_uuid,
            dating_approval_60_non_confidante_node_uuid,
            dating_approval_60_node_uuid,
            dating_approval_40_node_uuid,
            dating_approval_low_node_uuid,
            approval_80_node_uuid,
            approval_60_node_uuid,
            approval_40_node_uuid,
            approval_20_node_uuid,
            approval_0_node_uuid,
            approval_low_node_uuid,
            gith_approval_saved_node_uuid,
            gith_approval_not_saved_node_uuid,
        ],
        None,
        checkflags = (
            bg3.flag_group('Global', (
                bg3.flag(Really_Shadowheart_Softened_Version.uuid, False, None),
            )),
        ))
    d.create_standard_dialog_node(
        vanilla_responses_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        d.get_children_nodes_uuids(how_am_i_holding_up_node_uuid),
        None,
        checkflags = (
            bg3.flag_group('Global', (
                bg3.flag(Really_Shadowheart_Softened_Version.uuid, True, None),
            )),
        ))

    d.delete_all_children_dialog_nodes(how_am_i_holding_up_node_uuid)

    d.add_child_dialog_node(how_am_i_holding_up_node_uuid, responses_fork_node_uuid)

    # d.add_child_dialog_node(how_am_i_holding_up_node_uuid, partnered_embarce_durge_node_uuid)

    # d.add_child_dialog_node(how_am_i_holding_up_node_uuid, partnered_approval_80_node_uuid)
    # d.add_child_dialog_node(how_am_i_holding_up_node_uuid, partnered_approval_60_node_uuid)
    # d.add_child_dialog_node(how_am_i_holding_up_node_uuid, partnered_approval_40_node_uuid)
    # d.add_child_dialog_node(how_am_i_holding_up_node_uuid, partnered_approval_low_node_uuid)

    # d.add_child_dialog_node(how_am_i_holding_up_node_uuid, dating_approval_80_node_uuid)
    # d.add_child_dialog_node(how_am_i_holding_up_node_uuid, dating_approval_60_non_confidante_node_uuid)
    # d.add_child_dialog_node(how_am_i_holding_up_node_uuid, dating_approval_60_node_uuid)
    # d.add_child_dialog_node(how_am_i_holding_up_node_uuid, dating_approval_40_node_uuid)
    # d.add_child_dialog_node(how_am_i_holding_up_node_uuid, dating_approval_low_node_uuid)

    # d.add_child_dialog_node(how_am_i_holding_up_node_uuid, approval_80_node_uuid)
    # d.add_child_dialog_node(how_am_i_holding_up_node_uuid, approval_60_node_uuid)
    # d.add_child_dialog_node(how_am_i_holding_up_node_uuid, approval_40_node_uuid)
    # d.add_child_dialog_node(how_am_i_holding_up_node_uuid, approval_20_node_uuid)
    # d.add_child_dialog_node(how_am_i_holding_up_node_uuid, approval_0_node_uuid)
    # d.add_child_dialog_node(how_am_i_holding_up_node_uuid, approval_low_node_uuid)

    # d.add_child_dialog_node(how_am_i_holding_up_node_uuid, gith_approval_saved_node_uuid)
    # d.add_child_dialog_node(how_am_i_holding_up_node_uuid, gith_approval_not_saved_node_uuid)

    d.create_standard_dialog_node(
        jump_back_node_uuid,
        bg3.SPEAKER_PLAYER,
        ['f3716c0c-e34f-4c09-96f3-0f5148baa84c'],
        None)
    d.create_jump_dialog_node('f3716c0c-e34f-4c09-96f3-0f5148baa84c', bg3.SHADOWHEART_THOUGHTS_QUESTION_BANK_NODE_UUID, 2)

    #
    # Embrace Durge
    #

    # I tried to wrest you from Bhaal's grip once already. Seems I failed.
    d.create_standard_dialog_node(
        partnered_embarce_durge_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [partnered_embarce_durge2_node_uuid],
        bg3.text_content('hec80f6bag2a2ag449cg876cgc853b866237b', 1),
        checkflags = (
            bg3.flag_group('Global', (
                bg3.flag(bg3.FLAG_ORI_DarkUrge_State_BhaalAccepted, True, None),
            )),
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_State_PartneredWithShadowheart, True, speaker_idx_tav),
            )),
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_REALLY_DARK_URGE, True, speaker_idx_tav),
            ))
        ))
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '5.96',
        partnered_embarce_durge_node_uuid,
        ((None, 'e7f21f15-f386-40f4-bb0f-2f9f42249ad1'),),
        fade_out = 1.0,
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 4, None), (3.72, 32, None), (4.78, 32, 1), (6.75, 2048, None)),
        })

    # But I won't give up on you - not just yet. I'm my own worst enemy in that regard.
    d.create_standard_dialog_node(
        partnered_embarce_durge2_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [jump_back_node_uuid],
        bg3.text_content('h291fcfd1g32a8g4bf0g9e53g7d37330080ce', 1))
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '5.96',
        partnered_embarce_durge2_node_uuid,
        ((None, 'e7f21f15-f386-40f4-bb0f-2f9f42249ad1'),),
        fade_in = 1.0,
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((1.52, 64, None), (3.01, 8, None), (4.04, 1024, None), (5.88, 64, None)),
        })

    #
    # Partnered
    #

    # 80 approval
    # No notes. You've exceeded my every expectation.
    d.create_alias_dialog_node(
        partnered_approval_80_node_uuid,
        no_notes_node_uuid,
        [
            'bd5c3553-ab67-4cbb-bf7e-c6bf87d59e6f',
            '1672d8f5-201f-40ef-a861-928b1e8f280e',
            'ed509b15-541b-4913-b9e7-489b831c3ac7',
        ],
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_Approval_AtLeast_80_For_Sp2, True, speaker_idx_shadowheart),
                bg3.flag(bg3.FLAG_ORI_State_PartneredWithShadowheart, True, speaker_idx_tav)
            )),
        ))
    # Considering all we've been through, I think I was very lucky to find such favourable company. And attractive company too, no less.
    d.create_alias_dialog_node(
        'bd5c3553-ab67-4cbb-bf7e-c6bf87d59e6f',
        and_attractive_company_too_no_less_node_uuid,
        [jump_back_node_uuid],
        checkflags = (
            bg3.flag_group('Global', (
                bg3.flag(bg3.FLAG_ORI_Shadowheart_State_Shar_SavedParents, False, None),
            )),
            bg3.flag_group('Global', (
                bg3.flag(bg3.FLAG_ORI_Shadowheart_State_RejectShar_SavedParents, False, None),
            )),
        ))
    # Even if I could have made it this far without you, I don't think I'd have wanted to.
    d.create_alias_dialog_node(
        '1672d8f5-201f-40ef-a861-928b1e8f280e',
        i_dont_think_id_have_wanted_to_node_uuid,
        [jump_back_node_uuid],
        checkflags = (
            bg3.flag_group('Global', (
                bg3.flag(bg3.FLAG_ORI_Shadowheart_State_Shar_SavedParents, True, None),
            )),
        ))
    # Even if I could have made it this far without you, I don't think I'd have wanted to.
    d.create_alias_dialog_node(
        'ed509b15-541b-4913-b9e7-489b831c3ac7',
        i_dont_think_id_have_wanted_to_node_uuid,
        [jump_back_node_uuid],
        checkflags = (
            bg3.flag_group('Global', (
                bg3.flag(bg3.FLAG_ORI_Shadowheart_State_RejectShar_SavedParents, True, None),
            )),
        ))

    # 60 approval
    # How are you holding up? Don't be so modest - I can't remember the last time I met someone like you. Perhaps I never did, and never will again.
    d.create_alias_dialog_node(
        partnered_approval_60_node_uuid,
        dont_be_so_modest_node_uuid,
        ['7402e6fb-4069-435d-acc8-760b09d7c694'],
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_Approval_AtLeast_60_For_Sp2, True, speaker_idx_shadowheart),
                bg3.flag(bg3.FLAG_ORI_State_PartneredWithShadowheart, True, speaker_idx_tav)
            )),
        ))
    # Considering all we've been through, I think I was very lucky to find such favourable company. And attractive company too, no less.
    d.create_alias_dialog_node(
        '7402e6fb-4069-435d-acc8-760b09d7c694',
        and_attractive_company_too_no_less_node_uuid,
        [jump_back_node_uuid])

    # 40 approval
    # Quite splendidly to give credit where it's due. You and I have shared some good times together, and it seems we have plenty in common...
    d.create_alias_dialog_node(
        partnered_approval_40_node_uuid,
        quite_splendidly_to_give_credit_where_its_due_node_uuid,
        ['62555aab-dbee-4795-b2af-afa986fc8d0a'],
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_Approval_AtLeast_40_For_Sp2, True, speaker_idx_shadowheart),
                bg3.flag(bg3.FLAG_ORI_State_PartneredWithShadowheart, True, speaker_idx_tav)
            )),
        ))
    # You're someone I can actually turn to, when I don't know what to do.
    d.create_alias_dialog_node(
        '62555aab-dbee-4795-b2af-afa986fc8d0a',
        youre_someone_i_can_actually_turn_to_node_uuid,
        [jump_back_node_uuid])

    # less than 40 approval
    # I opened up to you like I have with no one before. We bonded... but it's been downhill from there. Perhaps we can rekindle things, or perhaps not...
    d.create_alias_dialog_node(
        partnered_approval_low_node_uuid,
        its_been_downhill_from_there_node_uuid,
        [
            '386b6b28-0aec-4e67-9f1d-453288305041',
            jump_back_node_uuid,
        ],
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_Approval_AtLeast_40_For_Sp2, False, speaker_idx_shadowheart),
                bg3.flag(bg3.FLAG_ORI_State_PartneredWithShadowheart, True, speaker_idx_tav)
            )),
        ))
    # Besides, we've come so far now - the end isn't so distant. I may need to concentrate on what's truly important to me.
    d.create_alias_dialog_node(
        '386b6b28-0aec-4e67-9f1d-453288305041',
        concentrate_on_whats_truly_important_to_me_node_uuid,
        [jump_back_node_uuid],
        checkflags = (
            bg3.flag_group('Global', (
                bg3.flag(bg3.FLAG_VISITEDREGION_BGO_Main_A, True, None),
            )),
        ))


    #
    # Dating
    #

    # 80 approval
    # Does it even need to be asked? We're beyond me merely liking you - I think I'm a different person, owing to you.
    d.create_alias_dialog_node(
        dating_approval_80_node_uuid,
        does_it_even_need_to_be_asked_node_uuid,
        [
            'd115ff4b-07a6-4f85-9be8-0b363ce7b9fc',
            'c73da439-8be1-4610-945c-4ad41d185845',
            '59a2a067-fcb7-4efc-b06b-8013683810eb',
            '2d44dc13-d01e-4aa8-a70d-ab6b546634fb',
        ],
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_Approval_AtLeast_80_For_Sp2, True, speaker_idx_shadowheart),
                bg3.flag(bg3.FLAG_ORI_State_PartneredWithShadowheart, False, speaker_idx_tav),
                bg3.flag(bg3.FLAG_ORI_State_DatingShadowheart, True, speaker_idx_tav)
            )),
        ))
    # Trust isn't something that comes easily to me. But with you... I think I can make an exception.
    d.create_alias_dialog_node(
        'd115ff4b-07a6-4f85-9be8-0b363ce7b9fc',
        trust_isnt_something_that_comes_easily_node_uuid,
        [jump_back_node_uuid],
        checkflags = (
            bg3.flag_group('Global', (
                bg3.flag(bg3.FLAG_ORI_Shadowheart_State_NightsongPoint_HasEnoughPoints, True, None),
            )),
        ))
    # After all, what I shared with you about my past, about being saved from the wolf... that is not something I would normally even dream of sharing.
    d.create_alias_dialog_node(
        'c73da439-8be1-4610-945c-4ad41d185845',
        what_i_shared_with_you_about_my_past_node_uuid,
        [jump_back_node_uuid],
        checkflags = (
            bg3.flag_group('Global', (
                bg3.flag(bg3.FLAG_ORI_Shadowheart_Knows_HasSeenWolfDream, True, None),
            )),
        ))
    # Besides, you saved my life aboard the nautiloid. How can I do anything but sing your praises?
    d.create_alias_dialog_node(
        '59a2a067-fcb7-4efc-b06b-8013683810eb',
        how_can_i_do_anything_but_sing_your_praises_node_uuid,
        [jump_back_node_uuid],
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(Shadowheart_Thanked_For_Freeing_Her.uuid, True, speaker_idx_shadowheart),
                bg3.flag(bg3.FLAG_TUT_TransformChamber_State_FreedShadowheart, True, speaker_idx_tav),
            )),
        ))
    # We've already made great strides - both in distance travelled, and in more personal matters...
    d.create_alias_dialog_node(
        '2d44dc13-d01e-4aa8-a70d-ab6b546634fb',
        weve_already_made_great_strides_node_uuid,
        [jump_back_node_uuid])

    # 60 approval, non confidante
    # You're a better catch than I'd expected to find while fighting for survival in the wilderness.
    d.create_alias_dialog_node(
        dating_approval_60_non_confidante_node_uuid,
        youre_a_better_catch_than_id_expected_node_uuid,
        [
            'f2c7e074-8bf4-4f32-a1d8-e91f27f92353',
            '8449ed2d-194c-46a9-af16-87b0131d7899',
        ],
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_Approval_AtLeast_60_For_Sp2, True, speaker_idx_shadowheart),
                bg3.flag(bg3.FLAG_ORI_State_PartneredWithShadowheart, False, speaker_idx_tav),
                bg3.flag(bg3.FLAG_ORI_State_DatingShadowheart, True, speaker_idx_tav)
            )),
            bg3.flag_group('Global', (
                bg3.flag(bg3.FLAG_ORI_Shadowheart_State_NightsongPoint_HasEnoughPoints, False, None),
                bg3.flag(bg3.FLAG_ORI_Shadowheart_Knows_HasSeenWolfDream, False, None),
            )),
        ))
    # Besides, you saved my life aboard the nautiloid. How can I do anything but sing your praises?
    d.create_alias_dialog_node(
        'f2c7e074-8bf4-4f32-a1d8-e91f27f92353',
        how_can_i_do_anything_but_sing_your_praises_node_uuid,
        [jump_back_node_uuid],
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(Shadowheart_Thanked_For_Freeing_Her.uuid, True, speaker_idx_shadowheart),
                bg3.flag(bg3.FLAG_TUT_TransformChamber_State_FreedShadowheart, True, speaker_idx_tav),
            )),
        ))
    # We've already made great strides - both in distance travelled, and in more personal matters...
    d.create_alias_dialog_node(
        '8449ed2d-194c-46a9-af16-87b0131d7899',
        weve_already_made_great_strides_node_uuid,
        [jump_back_node_uuid])

    # 60 approval
    # I don't think I've ever had a confidante quite like you - and if I have, I can't remember them.
    d.create_alias_dialog_node(
        dating_approval_60_node_uuid,
        had_a_confidante_quite_like_you_node_uuid,
        [
            '0a067f3f-7a48-4cf9-a0a5-50e5084fba88',
            'd67cc7f8-a4ce-4bec-bf37-454b2ed1c872',
            '1de8409e-cbba-4479-8243-ecc70df8f15c',
            '452358be-3e69-4083-9936-0404002ebd06',
        ],
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_Approval_AtLeast_60_For_Sp2, True, speaker_idx_shadowheart),
                bg3.flag(bg3.FLAG_ORI_State_PartneredWithShadowheart, False, speaker_idx_tav),
                bg3.flag(bg3.FLAG_ORI_State_DatingShadowheart, True, speaker_idx_tav)
            )),
        ))
    # Trust isn't something that comes easily to me. But with you... I think I can make an exception.
    d.create_alias_dialog_node(
        '0a067f3f-7a48-4cf9-a0a5-50e5084fba88',
        trust_isnt_something_that_comes_easily_node_uuid,
        [jump_back_node_uuid],
        checkflags = (
            bg3.flag_group('Global', (
                bg3.flag(bg3.FLAG_ORI_Shadowheart_State_NightsongPoint_HasEnoughPoints, True, None),
            )),
        ))
    # After all, what I shared with you about my past, about being saved from the wolf... that is not something I would normally even dream of sharing.
    d.create_alias_dialog_node(
        'd67cc7f8-a4ce-4bec-bf37-454b2ed1c872',
        what_i_shared_with_you_about_my_past_node_uuid,
        [jump_back_node_uuid],
        checkflags = (
            bg3.flag_group('Global', (
                bg3.flag(bg3.FLAG_ORI_Shadowheart_Knows_HasSeenWolfDream, True, None),
            )),
        ))
    # Besides, you saved my life aboard the nautiloid. How can I do anything but sing your praises?
    d.create_alias_dialog_node(
        '1de8409e-cbba-4479-8243-ecc70df8f15c',
        how_can_i_do_anything_but_sing_your_praises_node_uuid,
        [jump_back_node_uuid],
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(Shadowheart_Thanked_For_Freeing_Her.uuid, True, speaker_idx_shadowheart),
                bg3.flag(bg3.FLAG_TUT_TransformChamber_State_FreedShadowheart, True, speaker_idx_tav),
            )),
        ))
    # We've already made great strides - both in distance travelled, and in more personal matters...
    d.create_alias_dialog_node(
        '452358be-3e69-4083-9936-0404002ebd06',
        weve_already_made_great_strides_node_uuid,
        [jump_back_node_uuid])

    # 40 approval
    # You're doing just fine. After all, I'd scarcely anticipated being courted while fighting for survival in the wilderness.
    d.create_alias_dialog_node(
        dating_approval_40_node_uuid,
        youre_doing_just_fine_node_uuid,
        [
            'd9053505-f65c-44e4-a47e-463f786f5a57',
            '4e864e19-655d-4720-b59e-7e4be62f7450',
            'b3f8eb32-f7bb-4761-8752-2e68bf6aa7e5',
            '21cca58f-c542-4b72-aa8a-9c7a90c119cb',
        ],
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_Approval_AtLeast_40_For_Sp2, True, speaker_idx_shadowheart),
                bg3.flag(bg3.FLAG_ORI_State_PartneredWithShadowheart, False, speaker_idx_tav),
                bg3.flag(bg3.FLAG_ORI_State_DatingShadowheart, True, speaker_idx_tav)
            )),
        ))
    # Trust isn't something that comes easily to me. But with you... I think I can make an exception.
    d.create_alias_dialog_node(
        'd9053505-f65c-44e4-a47e-463f786f5a57',
        trust_isnt_something_that_comes_easily_node_uuid,
        [jump_back_node_uuid],
        checkflags = (
            bg3.flag_group('Global', (
                bg3.flag(bg3.FLAG_ORI_Shadowheart_State_NightsongPoint_HasEnoughPoints, True, None),
            )),
        ))
    # After all, what I shared with you about my past, about being saved from the wolf... that is not something I would normally even dream of sharing.
    d.create_alias_dialog_node(
        '4e864e19-655d-4720-b59e-7e4be62f7450',
        what_i_shared_with_you_about_my_past_node_uuid,
        [jump_back_node_uuid],
        checkflags = (
            bg3.flag_group('Global', (
                bg3.flag(bg3.FLAG_ORI_Shadowheart_Knows_HasSeenWolfDream, True, None),
            )),
        ))
    # Besides, you saved my life aboard the nautiloid. How can I do anything but sing your praises?
    d.create_alias_dialog_node(
        'b3f8eb32-f7bb-4761-8752-2e68bf6aa7e5',
        how_can_i_do_anything_but_sing_your_praises_node_uuid,
        [jump_back_node_uuid],
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(Shadowheart_Thanked_For_Freeing_Her.uuid, True, speaker_idx_shadowheart),
                bg3.flag(bg3.FLAG_TUT_TransformChamber_State_FreedShadowheart, True, speaker_idx_tav),
            )),
        ))
    # We've already made great strides - both in distance travelled, and in more personal matters...
    d.create_alias_dialog_node(
        '21cca58f-c542-4b72-aa8a-9c7a90c119cb',
        weve_already_made_great_strides_node_uuid,
        [jump_back_node_uuid])

    # less than 40 approval
    # I don't know what to say. You and I shared good times together... but it's been downhill from there. Perhaps we can rekindle things, or perhaps not...
    d.create_alias_dialog_node(
        dating_approval_low_node_uuid,
        perhaps_we_can_rekindle_things_node_uuid,
        [
            '0283874b-0aa8-453a-8408-e578503d5411',
            jump_back_node_uuid,
        ],
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_Approval_AtLeast_40_For_Sp2, False, speaker_idx_shadowheart),
                bg3.flag(bg3.FLAG_ORI_State_PartneredWithShadowheart, False, speaker_idx_tav),
                bg3.flag(bg3.FLAG_ORI_State_DatingShadowheart, True, speaker_idx_tav)
            )),
        ))
    # Pity. You'd started off so well, saving my life aboard the nautiloid. I suppose now I'm seeing the real you.
    d.create_alias_dialog_node(
        '0283874b-0aa8-453a-8408-e578503d5411',
        pity_youd_started_off_so_well_node_uuid,
        [jump_back_node_uuid],
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(Shadowheart_Thanked_For_Freeing_Her.uuid, True, speaker_idx_shadowheart),
                bg3.flag(bg3.FLAG_TUT_TransformChamber_State_FreedShadowheart, True, speaker_idx_tav),
            )),
        ))

    #
    # Friendship
    #

    # 80 approval
    # How are you holding up? Don't be so modest - I can't remember the last time I met someone like you. Perhaps I never did, and never will again.
    d.create_alias_dialog_node(
        approval_80_node_uuid,
        dont_be_so_modest_node_uuid,
        [
            '8d1ed4e7-a79c-4bf3-9351-2ec9bab0671b',
            'fb86c1ce-462f-415a-ab20-7ad0ea08afdf',
            '44ff8896-b909-4c2b-a7a2-23a249c55a44',
            '6a0ee8e6-a537-4a93-9fa9-010830ac7fc8',
            jump_back_node_uuid,
        ],
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_Approval_AtLeast_80_For_Sp2, True, speaker_idx_shadowheart),
                bg3.flag(bg3.FLAG_ORI_State_PartneredWithShadowheart, False, speaker_idx_tav),
                bg3.flag(bg3.FLAG_ORI_State_DatingShadowheart, False, speaker_idx_tav)
            )),
        ))
    # Trust isn't something that comes easily to me. But with you... I think I can make an exception.
    d.create_alias_dialog_node(
        '8d1ed4e7-a79c-4bf3-9351-2ec9bab0671b',
        trust_isnt_something_that_comes_easily_node_uuid,
        [jump_back_node_uuid],
        checkflags = (
            bg3.flag_group('Global', (
                bg3.flag(Shadowheart_Turned_Away_From_Shar.uuid, True, None),
            )),
        ))
    # After all, what I shared with you about my past, about being saved from the wolf... that is not something I would normally even dream of sharing.
    d.create_alias_dialog_node(
        'fb86c1ce-462f-415a-ab20-7ad0ea08afdf',
        what_i_shared_with_you_about_my_past_node_uuid,
        [jump_back_node_uuid],
        checkflags = (
            bg3.flag_group('Global', (
                bg3.flag(bg3.FLAG_ORI_Shadowheart_Knows_HasSeenWolfDream, True, None),
            )),
        ))
    # Besides, you saved my life aboard the nautiloid. How can I do anything but sing your praises?
    d.create_alias_dialog_node(
        '44ff8896-b909-4c2b-a7a2-23a249c55a44',
        how_can_i_do_anything_but_sing_your_praises_node_uuid,
        [jump_back_node_uuid],
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(Shadowheart_Thanked_For_Freeing_Her.uuid, True, speaker_idx_shadowheart),
                bg3.flag(bg3.FLAG_TUT_TransformChamber_State_FreedShadowheart, True, speaker_idx_tav),
            )),
        ))
    and_think_of_how_far_weve_come_together_node_uuid = '97dc9105-f62d-4776-bd4f-1dfea11a846c'
    # And think of how far we've come together - all the ways from the Hells, back to civilisation.
    d.create_alias_dialog_node(
        '6a0ee8e6-a537-4a93-9fa9-010830ac7fc8',
        and_think_of_how_far_weve_come_together_node_uuid,
        [jump_back_node_uuid],
        checkflags = (
            bg3.flag_group('Global', (
                bg3.flag(bg3.FLAG_VISITEDREGION_BGO_Main_A, True, None),
            )),
        ))

    # 60 approval
    # I don't think I've ever had a confidante quite like you - and if I have, I can't remember them.
    d.create_alias_dialog_node(
        approval_60_node_uuid,
        had_a_confidante_quite_like_you_node_uuid,
        [
            '23291011-2a65-49ae-b658-69bd4588ecca',
            '04a2f204-8e06-4fe2-8924-2e5a2c112702',
        ],
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_Approval_AtLeast_60_For_Sp2, True, speaker_idx_shadowheart),
                bg3.flag(bg3.FLAG_ORI_State_PartneredWithShadowheart, False, speaker_idx_tav),
                bg3.flag(bg3.FLAG_ORI_State_DatingShadowheart, False, speaker_idx_tav)
            )),
            bg3.flag_group('Global', (
                bg3.flag(bg3.FLAG_ORI_Shadowheart_Knows_HasSeenWolfDream, True, None),
            )),
        ))
    # Trust isn't something that comes easily to me. But with you... I think I can make an exception.
    d.create_alias_dialog_node(
        '23291011-2a65-49ae-b658-69bd4588ecca',
        trust_isnt_something_that_comes_easily_node_uuid,
        [jump_back_node_uuid],
        checkflags = (
            bg3.flag_group('Global', (
                bg3.flag(Shadowheart_Turned_Away_From_Shar.uuid, True, None),
            )),
        ))
    # After all, what I shared with you about my past, about being saved from the wolf... that is not something I would normally even dream of sharing.
    d.create_alias_dialog_node(
        '04a2f204-8e06-4fe2-8924-2e5a2c112702',
        what_i_shared_with_you_about_my_past_node_uuid,
        [jump_back_node_uuid])

    # 40 approval
    # You're someone I can actually turn to, when I don't know what to do.    
    d.create_alias_dialog_node(
        approval_40_node_uuid,
        youre_someone_i_can_actually_turn_to_node_uuid,
        [
            '208dd7b2-6954-4538-bf8f-653c13b878a4',
            'c9f27dbd-e6c3-4812-92f8-1d99339bab39',
            'a8eaa23e-666d-449b-a08a-35430b366587',
            'b429d3e6-76d0-45e7-ac64-0a14451414f4',
            jump_back_node_uuid,
        ],
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_Approval_AtLeast_40_For_Sp2, True, speaker_idx_shadowheart),
                bg3.flag(bg3.FLAG_ORI_State_PartneredWithShadowheart, False, speaker_idx_tav),
                bg3.flag(bg3.FLAG_ORI_State_DatingShadowheart, False, speaker_idx_tav)
            )),
        ))
    # Trust isn't something that comes easily to me. But with you... I think I can make an exception.
    d.create_alias_dialog_node(
        '208dd7b2-6954-4538-bf8f-653c13b878a4',
        trust_isnt_something_that_comes_easily_node_uuid,
        [jump_back_node_uuid],
        checkflags = (
            bg3.flag_group('Global', (
                bg3.flag(Shadowheart_Turned_Away_From_Shar.uuid, True, None),
            )),
        ))
    # After all, what I shared with you about my past, about being saved from the wolf... that is not something I would normally even dream of sharing.
    d.create_alias_dialog_node(
        'c9f27dbd-e6c3-4812-92f8-1d99339bab39',
        what_i_shared_with_you_about_my_past_node_uuid,
        [jump_back_node_uuid],
        checkflags = (
            bg3.flag_group('Global', (
                bg3.flag(bg3.FLAG_ORI_Shadowheart_Knows_HasSeenWolfDream, True, None),
            )),
        ))
    # Besides, you saved my life aboard the nautiloid. How can I do anything but sing your praises?
    d.create_alias_dialog_node(
        'a8eaa23e-666d-449b-a08a-35430b366587',
        how_can_i_do_anything_but_sing_your_praises_node_uuid,
        [jump_back_node_uuid],
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(Shadowheart_Thanked_For_Freeing_Her.uuid, True, speaker_idx_shadowheart),
                bg3.flag(bg3.FLAG_TUT_TransformChamber_State_FreedShadowheart, True, speaker_idx_tav),
            )),
        ))
    and_think_of_how_far_weve_come_together_node_uuid = '97dc9105-f62d-4776-bd4f-1dfea11a846c'
    # And think of how far we've come together - all the ways from the Hells, back to civilisation.
    d.create_alias_dialog_node(
        'b429d3e6-76d0-45e7-ac64-0a14451414f4',
        and_think_of_how_far_weve_come_together_node_uuid,
        [jump_back_node_uuid],
        checkflags = (
            bg3.flag_group('Global', (
                bg3.flag(bg3.FLAG_VISITEDREGION_BGO_Main_A, True, None),
            )),
        ))

    # 20 approval
    # I must admit, you've been a surprise, and not an unpleasant one. Kindred spirits are few and far between for me.
    d.create_alias_dialog_node(
        approval_20_node_uuid,
        youve_been_a_surprise_and_not_an_unpleasant_one_node_uuid,
        [
            '3df4c89d-afaa-492c-8b40-4a611c1de1eb',
            'b4e02e66-48ff-4f4c-ba65-4222768760c8',
            '6e81d493-7ded-4199-b396-6f6e1561cacc',
            jump_back_node_uuid,
        ],
        checkflags = (
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_REALLY_GITHYANKI, False, speaker_idx_tav),
            )),
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_Approval_AtLeast_20_For_Sp2, True, speaker_idx_shadowheart),
                bg3.flag(bg3.FLAG_ORI_State_PartneredWithShadowheart, False, speaker_idx_tav),
                bg3.flag(bg3.FLAG_ORI_State_DatingShadowheart, False, speaker_idx_tav)
            )),
        ))
    # After all, what I shared with you about my past, about being saved from the wolf... that is not something I would normally even dream of sharing.
    d.create_alias_dialog_node(
        '3df4c89d-afaa-492c-8b40-4a611c1de1eb',
        what_i_shared_with_you_about_my_past_node_uuid,
        [jump_back_node_uuid],
        checkflags = (
            bg3.flag_group('Global', (
                bg3.flag(bg3.FLAG_ORI_Shadowheart_Knows_HasSeenWolfDream, True, None),
            )),
        ))
    # Besides, you saved my life aboard the nautiloid. How can I do anything but sing your praises?
    d.create_alias_dialog_node(
        'b4e02e66-48ff-4f4c-ba65-4222768760c8',
        how_can_i_do_anything_but_sing_your_praises_node_uuid,
        [jump_back_node_uuid],
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(Shadowheart_Thanked_For_Freeing_Her.uuid, True, speaker_idx_shadowheart),
                bg3.flag(bg3.FLAG_TUT_TransformChamber_State_FreedShadowheart, True, speaker_idx_tav),
            )),
        ))
    and_think_of_how_far_weve_come_together_node_uuid = '97dc9105-f62d-4776-bd4f-1dfea11a846c'
    # And think of how far we've come together - all the ways from the Hells, back to civilisation.
    d.create_alias_dialog_node(
        '6e81d493-7ded-4199-b396-6f6e1561cacc',
        and_think_of_how_far_weve_come_together_node_uuid,
        [jump_back_node_uuid],
        checkflags = (
            bg3.flag_group('Global', (
                bg3.flag(bg3.FLAG_VISITEDREGION_BGO_Main_A, True, None),
            )),
        ))

    # 0 approval
    # You're not the kind of company I'd keep willingly, but all things considered... you'll do.    
    d.create_alias_dialog_node(
        approval_0_node_uuid,
        all_things_considered_youll_do_node_uuid,
        [
            'c2d2b6cb-99db-4e29-81d3-8cb7190c4bd9',
            jump_back_node_uuid,
        ],
        checkflags = (
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_REALLY_GITHYANKI, False, speaker_idx_tav),
            )),
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_Approval_AtLeast_0_For_Sp2, True, speaker_idx_shadowheart),
                bg3.flag(bg3.FLAG_ORI_State_PartneredWithShadowheart, False, speaker_idx_tav),
                bg3.flag(bg3.FLAG_ORI_State_DatingShadowheart, False, speaker_idx_tav)
            )),
        ))
    # And I haven't forgotten that you saved my life aboard the nautiloid. Perhaps I'll be able to return the favour at some point.
    d.create_alias_dialog_node(
        'c2d2b6cb-99db-4e29-81d3-8cb7190c4bd9',
        i_havent_forgotten_that_you_saved_my_life_node_uuid,
        [jump_back_node_uuid],
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(Shadowheart_Thanked_For_Freeing_Her.uuid, True, speaker_idx_shadowheart),
                bg3.flag(bg3.FLAG_TUT_TransformChamber_State_FreedShadowheart, True, speaker_idx_tav),
            )),
        ))

    # low approval
    # If nothing else, you can at least soak up any arrows that are loosed at us.
    d.create_alias_dialog_node(
        approval_low_node_uuid,
        you_can_at_least_soak_up_any_arrows_node_uuid,
        [
            'ec651f4c-b261-4d34-a34c-7bb740fa6671',
            jump_back_node_uuid,
        ],
        checkflags = (
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_REALLY_GITHYANKI, False, speaker_idx_tav),
            )),
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_Approval_AtLeast_0_For_Sp2, False, speaker_idx_shadowheart),
                bg3.flag(bg3.FLAG_ORI_State_PartneredWithShadowheart, False, speaker_idx_tav),
                bg3.flag(bg3.FLAG_ORI_State_DatingShadowheart, False, speaker_idx_tav)
            )),
        ))
    # Pity. You'd started off so well, saving my life aboard the nautiloid. I suppose now I'm seeing the real you.
    d.create_alias_dialog_node(
        'ec651f4c-b261-4d34-a34c-7bb740fa6671',
        pity_youd_started_off_so_well_node_uuid,
        [jump_back_node_uuid],
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(Shadowheart_Thanked_For_Freeing_Her.uuid, True, speaker_idx_shadowheart),
                bg3.flag(bg3.FLAG_TUT_TransformChamber_State_FreedShadowheart, True, speaker_idx_tav),
            )),
        ))

    youve_seemed_reliable_node_uuid = 'dfa07b50-fe30-4f4a-a9e0-941f405327db' # And since then, you've seemed reliable. Maybe I'll have to reevaluate what I think I know about your kind.
    my_suspicions_have_been_confirmed_node_uuid = 'a13eea50-dba1-40fa-820c-7faae7dfc23b' # But since then, well... let's just say some of my suspicions have been confirmed.
    im_not_afraid_to_admit_when_im_wrong_node_uuid = '9349d1c9-f48c-4d73-b409-7211df1d6aa5' # But I'm not afraid to admit when I'm wrong... you seem good company so far.
    the_only_way_is_up_from_there_node_uuid = 'feb24713-e114-4115-bbae-552af376e3dc' # Though I suppose the only way is up from there. You'll do for now.
    im_watching_you_node_uuid = 'ce52e13f-36f4-45f7-bb6e-ec5022db3911' # I'm watching you.
    seems_like_even_those_were_too_high_node_uuid = 'a3338d1a-4348-4b53-9b36-68689c1a03a9' # Seems like even those were too high.

    # Gith saved her
    # You saved my life aboard the nautiloid. I'd never have expected that from a gith.
    d.create_alias_dialog_node(
        gith_approval_saved_node_uuid,
        id_never_have_expected_that_from_a_gith_node_uuid,
        [
            'e744ed29-95ae-4b3d-b95c-a27d52eb8612',
            'feda13bf-f902-4144-9eb9-2d781bbd463f',
            '45eb3a0b-8463-400f-b575-a0c64ea196f4',
        ],
        checkflags = (
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_REALLY_GITHYANKI, True, speaker_idx_tav),
            )),
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_TUT_TransformChamber_State_FreedShadowheart, True, speaker_idx_tav),
                bg3.flag(bg3.FLAG_ORI_State_PartneredWithShadowheart, False, speaker_idx_tav),
                bg3.flag(bg3.FLAG_ORI_State_DatingShadowheart, False, speaker_idx_tav)
            )),
        ))
    # But I'm not afraid to admit when I'm wrong... you seem good company so far.
    d.create_alias_dialog_node(
        'e744ed29-95ae-4b3d-b95c-a27d52eb8612',
        im_not_afraid_to_admit_when_im_wrong_node_uuid,
        ['f53ffb79-7b9b-4562-82e3-eb0b10a661d1'],
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_Approval_AtLeast_20_For_Sp2, True, speaker_idx_shadowheart),
            )),
        ))
    # After all, what I shared with you about my past, about being saved from the wolf... that is not something I would normally even dream of sharing.
    d.create_alias_dialog_node(
        'f53ffb79-7b9b-4562-82e3-eb0b10a661d1',
        what_i_shared_with_you_about_my_past_node_uuid,
        [jump_back_node_uuid],
        checkflags = (
            bg3.flag_group('Global', (
                bg3.flag(bg3.FLAG_ORI_Shadowheart_Knows_HasSeenWolfDream, True, None),
            )),
        ))
    # And since then, you've seemed reliable. Maybe I'll have to reevaluate what I think I know about your kind.
    d.create_alias_dialog_node(
        'feda13bf-f902-4144-9eb9-2d781bbd463f',
        youve_seemed_reliable_node_uuid,
        [jump_back_node_uuid],
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_Approval_AtLeast_0_For_Sp2, True, speaker_idx_shadowheart),
            )),
        ))
    # But since then, well... let's just say some of my suspicions have been confirmed.
    d.create_alias_dialog_node(
        '45eb3a0b-8463-400f-b575-a0c64ea196f4',
        my_suspicions_have_been_confirmed_node_uuid,
        [jump_back_node_uuid])

    # Gith not saved her
    # My estimations started at a low point as far as you're concerned, gith.
    d.create_alias_dialog_node(
        gith_approval_not_saved_node_uuid,
        my_estimations_started_at_a_low_point_gith_node_uuid,
        [
            '7fe13ca5-9695-427d-aec7-6b67a42108c9',
            '49bd89cd-a4e3-44a5-b6ee-1c8ae5119a94',
            'd7c88b17-3159-4737-b949-0d5b32ead663',
            'c67e3585-460f-42fe-a5f3-c05dffab49f0',
        ],
        checkflags = (
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_REALLY_GITHYANKI, True, speaker_idx_tav),
            )),
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_TUT_TransformChamber_State_FreedShadowheart, False, speaker_idx_tav),
                bg3.flag(bg3.FLAG_ORI_State_PartneredWithShadowheart, False, speaker_idx_tav),
                bg3.flag(bg3.FLAG_ORI_State_DatingShadowheart, False, speaker_idx_tav)
            )),
        ))
    # But I'm not afraid to admit when I'm wrong... you seem good company so far.
    d.create_alias_dialog_node(
        '7fe13ca5-9695-427d-aec7-6b67a42108c9',
        im_not_afraid_to_admit_when_im_wrong_node_uuid,
        ['0e005b5d-bcd9-4dd5-becb-be851ac8ca98'],
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_Approval_AtLeast_20_For_Sp2, True, speaker_idx_shadowheart),
            )),
        ))
    # After all, what I shared with you about my past, about being saved from the wolf... that is not something I would normally even dream of sharing.
    d.create_alias_dialog_node(
        '0e005b5d-bcd9-4dd5-becb-be851ac8ca98',
        what_i_shared_with_you_about_my_past_node_uuid,
        [jump_back_node_uuid],
        checkflags = (
            bg3.flag_group('Global', (
                bg3.flag(bg3.FLAG_ORI_Shadowheart_Knows_HasSeenWolfDream, True, None),
            )),
        ))
    # Though I suppose the only way is up from there. You'll do for now.
    d.create_alias_dialog_node(
        '49bd89cd-a4e3-44a5-b6ee-1c8ae5119a94',
        the_only_way_is_up_from_there_node_uuid,
        [jump_back_node_uuid],
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_Approval_AtLeast_10_For_Sp2, True, speaker_idx_shadowheart),
            )),
        ))
    # I'm watching you.
    d.create_alias_dialog_node(
        'd7c88b17-3159-4737-b949-0d5b32ead663',
        im_watching_you_node_uuid,
        [jump_back_node_uuid],
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_Approval_AtLeast_0_For_Sp2, True, speaker_idx_shadowheart),
            )),
        ))
    # Seems like even those were too high.
    d.create_alias_dialog_node(
        'c67e3585-460f-42fe-a5f3-c05dffab49f0',
        seems_like_even_those_were_too_high_node_uuid,
        [jump_back_node_uuid])


def add_more_selunite_lines() -> None:
    # d = bg3.dialog_object(files.get_file('Gustav', 'Mods/GustavDev/Story/DialogsBinary/Companions/ShadowHeart_InParty2_Nested_SharranChapter.lsf'))

    ab = game_assets.get_modded_dialog_asset_bundle('ShadowHeart_InParty2_Nested_SharranChapter')
    d = bg3.dialog_object(ab.dialog)

    speaker_idx_tav = d.get_speaker_slot_index(bg3.SPEAKER_PLAYER)

    ###############################################################################################################################################
    # A new selunite answer to Shadowheart's line: There's often suffering - death even. Many people break before they embrace Shar's truths.
    ###############################################################################################################################################
    many_people_break_node_uuid = 'dca96b9a-b662-495e-9991-211ab33c7abf' # existing node
    i_wont_cast_judgement_node_uuid = 'a6a92875-629e-4427-b1f1-2623d48ada6d' # existing node
    you_should_tell_me_more_node_uuid = 'bd0720b8-0b81-4cf1-9407-f0626477569a' # existing node
    # lets_see_how_you_handle_this_node_uuid = '7b33ce12-30d4-4573-8af4-8db6f798c6f8' # existing node

    perhaps_this_is_your_path_node_uuid = '45f43e8e-208d-4710-a70c-244f14bd629e'

    reaction1_plus_1 = bg3.reaction_object.create_new(files, { bg3.SPEAKER_SHADOWHEART : 1 }, uuid = 'cae819b2-b727-45ee-870b-469b0c3bcd98')
    reaction2_plus_1 = bg3.reaction_object.create_new(files, { bg3.SPEAKER_SHADOWHEART : 1 }, uuid = '8ce31bb9-e406-42ee-93ef-449fed52cc3c')
    reaction3_plus_1 = bg3.reaction_object.create_new(files, { bg3.SPEAKER_SHADOWHEART : 1 }, uuid = '38d49967-063f-48b3-8c37-d72126a3c9ad')
    # reaction4_plus_1 = bg3.reaction_object.create_new(files, { bg3.SPEAKER_SHADOWHEART : 1 }, uuid = 'ca4a2025-71b3-40e9-bebe-df3e288487b1')

    # Selûne teaches us to find our own paths through life. Perhaps, this is your path.
    d.create_standard_dialog_node(
        perhaps_this_is_your_path_node_uuid,
        bg3.SPEAKER_PLAYER,
        d.get_children_nodes_uuids(you_should_tell_me_more_node_uuid),
        bg3.text_content('hdf4bfc8eg13cdg433fgb980gf87262855ec4', 1),
        constructor = bg3.dialog_object.QUESTION,
        approval_rating_uuid = reaction1_plus_1.uuid,
        setflags = (
            bg3.flag_group('Global', (
                bg3.flag(bg3.FLAG_ORI_Shadowheart_State_BlockBackground, True, None),
                bg3.flag(bg3.FLAG_ORI_Shadowheart_State_WolfDreamPoint_WorshipGood, True, None)
            )),
        ),
        checkflags = (
            bg3.flag_group('Tag', (
                bg3.flag(bg3.GOD_SELUNE, True, speaker_idx_tav),
            )),
        ))

    d.set_approval_rating(you_should_tell_me_more_node_uuid, reaction2_plus_1.uuid)
    d.set_dialog_flags(you_should_tell_me_more_node_uuid, checkflags = (
        bg3.flag_group('Global', (
            bg3.flag(bg3.FLAG_ORI_Shadowheart_State_BlockBackground, True, None),
            bg3.flag(bg3.FLAG_ORI_Shadowheart_State_WolfDreamPoint_WorshipGood, True, None),
        )),
    ))

    d.set_approval_rating(i_wont_cast_judgement_node_uuid, reaction3_plus_1.uuid)

    # <content contentuid="h71f6aa25g7786g48fdgbf29g64a030dcbb9a" version="1">I don't care who you worship. We have bigger problems.</content> v
    # <content contentuid="h733e8096g73a4g4655gab90g5327e0c22e31" version="1">I don't care who you worship. We have bigger problems.</content>
    # <content contentuid="hbb67d9aeg316fg421egb528g2a4d5e691b0d" version="1">I don't care who you worship. We have bigger problems.</content>
    # <content contentuid="hf1a387f6gfe95g48e0g982dg94f579d0d367" version="1">I don't care who you worship. We have bigger problems.</content>
    # d.set_approval_rating(lets_see_how_you_handle_this_node_uuid, reaction4_plus_1.uuid)

    d.add_child_dialog_node(many_people_break_node_uuid, perhaps_this_is_your_path_node_uuid)


def gain_less_approval_other_topics_act1() -> None:
    ###################################################
    # ShadowHeart_InParty2_Nested_DefaultChapter.lsf
    ###################################################

    ab = game_assets.get_modded_dialog_asset_bundle('ShadowHeart_InParty2_Nested_DefaultChapter')
    d = bg3.dialog_object(ab.dialog)

    well_i_like_night_orchids_node_uuid = '85e3f8ce-7281-408d-adc9-f27f8015679c' # existing node
    youll_have_to_point_out_night_orchids_node_uuid = '1bfd6310-be4a-4f14-bc84-88adfa58409c' # existing node
    alias_youll_have_to_point_out_night_orchids_node_uuid = 'd932066d-c7dc-4260-b164-92e889b61b3c'

    # You'll have to point out night orchids to me if we ever pass some.
    reaction_plus_3 = bg3.reaction_object.create_new(files, { bg3.SPEAKER_SHADOWHEART : 3 }, uuid = '5fa21704-1ac0-4968-b5d7-c944cb063fb9')
    d.create_standard_dialog_node(
        alias_youll_have_to_point_out_night_orchids_node_uuid,
        bg3.SPEAKER_PLAYER,
        d.get_children_nodes_uuids(youll_have_to_point_out_night_orchids_node_uuid),
        bg3.text_content('haa5359c2gdcd2g4e9fga4e3gdf8cc32b9625', 1),
        constructor = bg3.dialog_object.QUESTION,
        approval_rating_uuid = reaction_plus_3.uuid,
        checkflags = (
            bg3.flag_group('Global', (
                bg3.flag(Really_Shadowheart_Softened_Version.uuid, False, None),
            )),
        ))

    d.add_dialog_flags(youll_have_to_point_out_night_orchids_node_uuid, checkflags = (
        bg3.flag_group('Global', (
            bg3.flag(Really_Shadowheart_Softened_Version.uuid, True, None),
        )),
    ))
    d.add_child_dialog_node(well_i_like_night_orchids_node_uuid, alias_youll_have_to_point_out_night_orchids_node_uuid, 0)


def gain_less_approval_sharran_topics_act1() -> None:

    ###################################################
    # ShadowHeart_InParty2_Nested_SharranChapter.lsf
    ###################################################

    ab = game_assets.get_modded_dialog_asset_bundle('ShadowHeart_InParty2_Nested_SharranChapter')
    d = bg3.dialog_object(ab.dialog)


    selunite_negative_reaction_to_shar = bg3.reaction_object.create_new(files, { bg3.SPEAKER_SHADOWHEART : -10, bg3.SPEAKER_KARLACH : -1, bg3.SPEAKER_LAEZEL : 5, bg3.SPEAKER_ASTARION : -1 }, uuid = '6981a522-2c35-4c6d-89fc-63fee1e40c5f')
    negative_reaction_to_shar = bg3.reaction_object.create_new(files, { bg3.SPEAKER_SHADOWHEART : -5, bg3.SPEAKER_KARLACH : -1, bg3.SPEAKER_LAEZEL : 5, bg3.SPEAKER_ASTARION : -1 }, uuid = '5322afd6-cb63-4007-be15-7e3fa268a66f')
    positive_reaction_to_shar = bg3.reaction_object.create_new(files, { bg3.SPEAKER_SHADOWHEART : 1, bg3.SPEAKER_KARLACH : 1, bg3.SPEAKER_LAEZEL : -1, bg3.SPEAKER_ASTARION: 1 }, uuid = 'a7fbbe50-70ac-40bb-a8a6-4c8d9a578df5')

    # I don't care who you worship. We have bigger problems.
    parent_node_uuid = '5091ae44-d334-4a5c-9012-2eef288f2a73' # existing node
    i_dont_care_who_you_worship_node_uuid = '1cc5be2e-c95b-4ffc-88c0-dc5cf2f2404d' # existing node
    alias_i_dont_care_who_you_worship_node_uuid = '78b45b6c-41c9-4302-ac0c-f9dfdc3aa10a'

    d.add_dialog_flags(i_dont_care_who_you_worship_node_uuid, checkflags = (
        bg3.flag_group('Global', (
            bg3.flag(Really_Shadowheart_Softened_Version.uuid, True, None),
        )),
    ))
    d.create_standard_dialog_node(
        alias_i_dont_care_who_you_worship_node_uuid,
        bg3.SPEAKER_PLAYER,
        d.get_children_nodes_uuids(i_dont_care_who_you_worship_node_uuid),
        bg3.text_content('h71f6aa25g7786g48fdgbf29g64a030dcbb9a', 1),
        constructor = bg3.dialog_object.QUESTION,
        approval_rating_uuid = positive_reaction_to_shar.uuid,
        checkflags = (
            bg3.flag_group('Global', (
                bg3.flag(Really_Shadowheart_Softened_Version.uuid, False, None),
            )),
        ))
    d.add_child_dialog_node_before(parent_node_uuid, alias_i_dont_care_who_you_worship_node_uuid, i_dont_care_who_you_worship_node_uuid)

    # I didn't agree to join up with a Shar worshipper.
    i_didnt_agree_node_uuid = '89be9e86-e5eb-41fc-9c86-32327a013fe7' # existing node
    alias_i_didnt_agree_node_uuid = '88636603-45ba-4618-af17-b543dfa8aa69'

    d.add_dialog_flags(i_didnt_agree_node_uuid, checkflags = (
        bg3.flag_group('Global', (
            bg3.flag(Really_Shadowheart_Softened_Version.uuid, True, None),
        )),
    ))
    d.create_standard_dialog_node(
        alias_i_didnt_agree_node_uuid,
        bg3.SPEAKER_PLAYER,
        d.get_children_nodes_uuids(i_didnt_agree_node_uuid),
        bg3.text_content('hf28bee25gca4fg4316g9920gb9232a909d2d', 1),
        constructor = bg3.dialog_object.QUESTION,
        approval_rating_uuid = negative_reaction_to_shar.uuid,
        checkflags = (
            bg3.flag_group('Global', (
                bg3.flag(Really_Shadowheart_Softened_Version.uuid, False, None),
            )),
        ))
    d.add_child_dialog_node_before(parent_node_uuid, alias_i_didnt_agree_node_uuid, i_didnt_agree_node_uuid)

    # Shar is an abomination. You deceived me.
    shar_is_an_abomination_node_uuid = '00c919a9-6916-45ea-a2e9-f0babebd9b8e' # existing node
    alias_shar_is_an_abomination_node_uuid = 'e14cd22c-a3de-4f58-8e60-71b507fb960c'

    d.add_dialog_flags(shar_is_an_abomination_node_uuid, checkflags = (
        bg3.flag_group('Global', (
            bg3.flag(Really_Shadowheart_Softened_Version.uuid, True, None),
        )),
    ))
    d.create_standard_dialog_node(
        alias_shar_is_an_abomination_node_uuid,
        bg3.SPEAKER_PLAYER,
        d.get_children_nodes_uuids(shar_is_an_abomination_node_uuid),
        bg3.text_content('h8ea889c1g9703g4b2egaa9cgce56edd1e77d', 1),
        text_tags = [bg3.TAG_CLERIC_SELUNE],
        constructor = bg3.dialog_object.QUESTION,
        approval_rating_uuid = selunite_negative_reaction_to_shar.uuid,
        checkflags = (
            bg3.flag_group('Global', (
                bg3.flag(Really_Shadowheart_Softened_Version.uuid, False, None),
            )),
        ))
    d.add_child_dialog_node_before(parent_node_uuid, alias_shar_is_an_abomination_node_uuid, shar_is_an_abomination_node_uuid)

    # Very well. Perhaps there's potential in you. Let's see how you handle this.
    shar_persuade_roll_result_success_node_uuid = '20360535-696b-48bc-9978-9a69887b2f43' # existing node
    very_well_perhaps_theres_potential_in_you_node_uuid = '7b33ce12-30d4-4573-8af4-8db6f798c6f8' # existing node

    reaction_plus_1 = bg3.reaction_object.create_new(files, { bg3.SPEAKER_SHADOWHEART : 1 }, uuid = 'b7357692-9e81-4445-a999-f3b41756271a')
    approval_fork_node_uuid = create_approval_fork(d, very_well_perhaps_theres_potential_in_you_node_uuid, reaction_plus_1)
    d.delete_all_children_dialog_nodes(shar_persuade_roll_result_success_node_uuid)
    d.add_child_dialog_node(shar_persuade_roll_result_success_node_uuid, approval_fork_node_uuid)

    ###################################################
    # GOB_SeluneTemple_OM_ShadowHeart_COM.lsf
    ###################################################
    
    ab = game_assets.get_modded_dialog_asset_bundle('GOB_SeluneTemple_OM_ShadowHeart_COM')
    d = bg3.dialog_object(ab.dialog)

    parent_node_uuid = '670cf213-7c67-e237-17c3-e7cf62578ba1' # existing node

    sharran_tav_node_uuid = '1e34fa98-ab78-1e5f-2e66-7af27675e374' # existing node
    d.remove_dialog_attribute(sharran_tav_node_uuid, 'ApprovalRatingID')

    # I don't care who you worship. We have bigger problems.
    i_dont_care_who_you_worship_node_uuid = '80ce8470-21e6-ff1f-7978-b0238f237203' # existing node
    alias_i_dont_care_who_you_worship_node_uuid = '1962915f-ca4d-4807-b3bc-707fefd2dfbc'

    d.add_dialog_flags(i_dont_care_who_you_worship_node_uuid, checkflags = (
        bg3.flag_group('Global', (
            bg3.flag(Really_Shadowheart_Softened_Version.uuid, True, None),
        )),
    ))
    d.create_standard_dialog_node(
        alias_i_dont_care_who_you_worship_node_uuid,
        bg3.SPEAKER_PLAYER,
        d.get_children_nodes_uuids(i_dont_care_who_you_worship_node_uuid),
        bg3.text_content('h733e8096g73a4g4655gab90g5327e0c22e31', 1),
        constructor = bg3.dialog_object.QUESTION,
        approval_rating_uuid = positive_reaction_to_shar.uuid,
        checkflags = (
            bg3.flag_group('Global', (
                bg3.flag(Really_Shadowheart_Softened_Version.uuid, False, None),
            )),
        ))
    d.add_child_dialog_node_before(parent_node_uuid, alias_i_dont_care_who_you_worship_node_uuid, i_dont_care_who_you_worship_node_uuid)

    # I didn't agree to join up with a Shar worshipper.
    i_didnt_agree_node_uuid = '4f38d1eb-5ac1-be25-9e77-212ad8ae212d' # existing node
    alias_i_didnt_agree_node_uuid = '55dc7105-c7ea-4ca8-bdcf-cca662b51208'

    d.add_dialog_flags(i_didnt_agree_node_uuid, checkflags = (
        bg3.flag_group('Global', (
            bg3.flag(Really_Shadowheart_Softened_Version.uuid, True, None),
        )),
    ))
    d.create_standard_dialog_node(
        alias_i_didnt_agree_node_uuid,
        bg3.SPEAKER_PLAYER,
        d.get_children_nodes_uuids(i_didnt_agree_node_uuid),
        bg3.text_content('hf28bee25gca4fg4316g9920gb9232a909d2d', 1),
        constructor = bg3.dialog_object.QUESTION,
        approval_rating_uuid = negative_reaction_to_shar.uuid,
        checkflags = (
            bg3.flag_group('Global', (
                bg3.flag(Really_Shadowheart_Softened_Version.uuid, False, None),
            )),
        ))
    d.add_child_dialog_node_before(parent_node_uuid, alias_i_didnt_agree_node_uuid, i_didnt_agree_node_uuid)

    # Shar is an abomination. You deceived me.
    shar_is_an_abomination_node_uuid = '2390295c-610d-ad8f-ea33-7056be49d62d' # existing node
    alias_shar_is_an_abomination_node_uuid = 'acd0ec01-8e1f-4c0b-9c7d-681058eac2ae'

    d.add_dialog_flags(shar_is_an_abomination_node_uuid, checkflags = (
        bg3.flag_group('Global', (
            bg3.flag(Really_Shadowheart_Softened_Version.uuid, True, None),
        )),
    ))
    d.create_standard_dialog_node(
        alias_shar_is_an_abomination_node_uuid,
        bg3.SPEAKER_PLAYER,
        d.get_children_nodes_uuids(shar_is_an_abomination_node_uuid),
        bg3.text_content('h8ea889c1g9703g4b2egaa9cgce56edd1e77d', 1),
        text_tags = [bg3.TAG_CLERIC_SELUNE],
        constructor = bg3.dialog_object.QUESTION,
        approval_rating_uuid = selunite_negative_reaction_to_shar.uuid,
        checkflags = (
            bg3.flag_group('Global', (
                bg3.flag(Really_Shadowheart_Softened_Version.uuid, False, None),
            )),
        ))
    d.add_child_dialog_node_before(parent_node_uuid, alias_shar_is_an_abomination_node_uuid, shar_is_an_abomination_node_uuid)


    ###################################################
    # CAMP_Shadowheart_CRD_WildMagic.lsf
    ###################################################

    ab = game_assets.get_modded_dialog_asset_bundle('CAMP_Shadowheart_IVB_CFM_WildMagic')
    d = bg3.dialog_object(ab.dialog)

    parent_node_uuid = '14db9d10-a45b-f0a4-3756-73ea58842fc3' # existing node
    shar_is_an_abomination_node_uuid = 'd52d9723-0332-6821-b53a-9d163100eed7' # existing node

    sharran_tav_node_uuid = 'e6dda4cd-6c77-0857-7637-6df1c8ca9d84' # existing node
    d.remove_dialog_attribute(sharran_tav_node_uuid, 'ApprovalRatingID')

    # I don't care who you worship. We have bigger problems.
    i_dont_care_who_you_worship_node_uuid = '85c8aa11-22db-b00c-4014-183c75080371' # existing node
    alias_i_dont_care_who_you_worship_node_uuid = 'cf3c04f1-0c66-4ec2-9680-e1e65f0b975a'

    d.add_dialog_flags(i_dont_care_who_you_worship_node_uuid, checkflags = (
        bg3.flag_group('Global', (
            bg3.flag(Really_Shadowheart_Softened_Version.uuid, True, None),
        )),
    ))
    d.create_standard_dialog_node(
        alias_i_dont_care_who_you_worship_node_uuid,
        bg3.SPEAKER_PLAYER,
        d.get_children_nodes_uuids(i_dont_care_who_you_worship_node_uuid),
        bg3.text_content('hbb67d9aeg316fg421egb528g2a4d5e691b0d', 1),
        constructor = bg3.dialog_object.QUESTION,
        approval_rating_uuid = positive_reaction_to_shar.uuid,
        checkflags = (
            bg3.flag_group('Global', (
                bg3.flag(Really_Shadowheart_Softened_Version.uuid, False, None),
            )),
        ))
    d.add_child_dialog_node_before(parent_node_uuid, alias_i_dont_care_who_you_worship_node_uuid, i_dont_care_who_you_worship_node_uuid)

    # I didn't agree to join up with a Shar worshipper.
    i_didnt_agree_node_uuid = '21cd97fb-f5dc-82e1-c709-4e4bd3c09e48' # existing node
    alias_i_didnt_agree_node_uuid = 'cc3ac6ba-e445-4313-a56b-0f3d7226ebc6'

    d.add_dialog_flags(i_didnt_agree_node_uuid, checkflags = (
        bg3.flag_group('Global', (
            bg3.flag(Really_Shadowheart_Softened_Version.uuid, True, None),
        )),
    ))
    d.create_standard_dialog_node(
        alias_i_didnt_agree_node_uuid,
        bg3.SPEAKER_PLAYER,
        d.get_children_nodes_uuids(i_didnt_agree_node_uuid),
        bg3.text_content('h8f1ea62cgd69ag4e7ag9bc0ge025e45e41a6', 1),
        constructor = bg3.dialog_object.QUESTION,
        approval_rating_uuid = negative_reaction_to_shar.uuid,
        checkflags = (
            bg3.flag_group('Global', (
                bg3.flag(Really_Shadowheart_Softened_Version.uuid, False, None),
            )),
        ))
    d.add_child_dialog_node_before(parent_node_uuid, alias_i_didnt_agree_node_uuid, i_didnt_agree_node_uuid)


    # Shar is an abomination. You deceived me.
    shar_is_an_abomination_node_uuid = 'd52d9723-0332-6821-b53a-9d163100eed7' # existing node
    alias_shar_is_an_abomination_node_uuid = '4866196c-2e97-4694-89b4-b82978538a3f'

    d.add_dialog_flags(shar_is_an_abomination_node_uuid, checkflags = (
        bg3.flag_group('Global', (
            bg3.flag(Really_Shadowheart_Softened_Version.uuid, True, None),
        )),
    ))
    d.create_standard_dialog_node(
        alias_shar_is_an_abomination_node_uuid,
        bg3.SPEAKER_PLAYER,
        d.get_children_nodes_uuids(shar_is_an_abomination_node_uuid),
        bg3.text_content('h381d7e8ag9729g4281ga115g04e456b0d807', 1),
        text_tags = [bg3.TAG_CLERIC_SELUNE],
        constructor = bg3.dialog_object.QUESTION,
        approval_rating_uuid = selunite_negative_reaction_to_shar.uuid,
        checkflags = (
            bg3.flag_group('Global', (
                bg3.flag(Really_Shadowheart_Softened_Version.uuid, False, None),
            )),
        ))
    d.add_child_dialog_node_before(parent_node_uuid, alias_shar_is_an_abomination_node_uuid, shar_is_an_abomination_node_uuid)


    ###################################################
    # FOR_Owlbear_OM_Shadowheart_COM.lsf
    ###################################################

    ab = game_assets.get_modded_dialog_asset_bundle('FOR_Owlbear_OM_Shadowheart_COM')
    d = bg3.dialog_object(ab.dialog)

    parent_node_uuid = '28c08276-a3ab-8359-985a-e7e7119289b5' # existing node

    # I don't care who you worship. We have bigger problems.
    i_dont_care_who_you_worship_node_uuid = '80c696fb-f433-1af9-16de-258f8da80580' # existing node
    alias_i_dont_care_who_you_worship_node_uuid = '3b11c6c9-57b6-4d1a-a159-45fe3d3e0661'

    d.add_dialog_flags(i_dont_care_who_you_worship_node_uuid, checkflags = (
        bg3.flag_group('Global', (
            bg3.flag(Really_Shadowheart_Softened_Version.uuid, True, None),
        )),
    ))
    d.create_standard_dialog_node(
        alias_i_dont_care_who_you_worship_node_uuid,
        bg3.SPEAKER_PLAYER,
        d.get_children_nodes_uuids(i_dont_care_who_you_worship_node_uuid),
        bg3.text_content('hf1a387f6gfe95g48e0g982dg94f579d0d367', 1),
        constructor = bg3.dialog_object.QUESTION,
        approval_rating_uuid = positive_reaction_to_shar.uuid,
        checkflags = (
            bg3.flag_group('Global', (
                bg3.flag(Really_Shadowheart_Softened_Version.uuid, False, None),
            )),
        ))
    d.add_child_dialog_node(parent_node_uuid, alias_i_dont_care_who_you_worship_node_uuid, 4)

    # I didn't agree to join up with a Shar worshipper.
    i_didnt_agree_node_uuid = '9dd87df4-91ce-46ed-1b04-abb4e9f0f524' # existing node
    alias_i_didnt_agree_node_uuid = 'f38ef8c7-6824-4c84-98e8-6041ead2338c'

    d.add_dialog_flags(i_didnt_agree_node_uuid, checkflags = (
        bg3.flag_group('Global', (
            bg3.flag(Really_Shadowheart_Softened_Version.uuid, True, None),
        )),
    ))
    d.create_standard_dialog_node(
        alias_i_didnt_agree_node_uuid,
        bg3.SPEAKER_PLAYER,
        d.get_children_nodes_uuids(i_didnt_agree_node_uuid),
        bg3.text_content('h82adbbc8g774dg478bg92e5gfffafa910876', 1),
        constructor = bg3.dialog_object.QUESTION,
        approval_rating_uuid = negative_reaction_to_shar.uuid,
        checkflags = (
            bg3.flag_group('Global', (
                bg3.flag(Really_Shadowheart_Softened_Version.uuid, False, None),
            )),
        ))
    d.add_child_dialog_node_before(parent_node_uuid, alias_i_didnt_agree_node_uuid, i_didnt_agree_node_uuid)

    # Shar is an abomination. You deceived me.
    shar_is_an_abomination_node_uuid = '9042645e-2c51-6304-7364-9f272de98124' # existing node
    alias_shar_is_an_abomination_node_uuid = '65a4d7f9-00f2-47f0-b35b-19c27187e407'

    d.add_dialog_flags(shar_is_an_abomination_node_uuid, checkflags = (
        bg3.flag_group('Global', (
            bg3.flag(Really_Shadowheart_Softened_Version.uuid, True, None),
        )),
    ))
    d.create_standard_dialog_node(
        alias_shar_is_an_abomination_node_uuid,
        bg3.SPEAKER_PLAYER,
        d.get_children_nodes_uuids(shar_is_an_abomination_node_uuid),
        bg3.text_content('hef64e78eg5734g4a5fgadf4gc24af75f2c67', 1),
        text_tags = [bg3.TAG_CLERIC_SELUNE],
        constructor = bg3.dialog_object.QUESTION,
        approval_rating_uuid = selunite_negative_reaction_to_shar.uuid,
        checkflags = (
            bg3.flag_group('Global', (
                bg3.flag(Really_Shadowheart_Softened_Version.uuid, False, None),
            )),
        ))
    d.add_child_dialog_node_before(parent_node_uuid, alias_shar_is_an_abomination_node_uuid, shar_is_an_abomination_node_uuid)


def increase_approval_requirements() -> None:
    ###################################################
    # CAMP_Night1_CRD_Shadowheart
    ###################################################
    ab = game_assets.get_modded_dialog_asset_bundle('CAMP_Night1_CRD_Shadowheart')
    d = bg3.dialog_object(ab.dialog)

    speaker_idx_shadowheart = d.get_speaker_slot_index(bg3.SPEAKER_SHADOWHEART)
    speaker_idx_tav = d.get_speaker_slot_index(bg3.SPEAKER_PLAYER)

    if_were_to_survive_node_uuid = '216376c0-a16c-b9ca-c604-f7cebbcdb099' # existing node
    you_seem_reliable_node_uuid = 'f3e147cb-2ebe-58b8-380d-5bc37a57d5a0' # existing node
    alias_you_seem_reliable_node_uuid = 'ce92ae0a-d12e-4573-810b-d133d2a78f30'

    dont_question_me_node_uuid = 'c533fcc0-7173-b819-7ba9-5efe790ea01b'  # existing node
    spare_me_the_petty_tyrant_routine_node_uuid = 'f60adf6f-19f8-d4c3-00bc-b04030e8b2ac' # existing node
    alias_spare_me_the_petty_tyrant_routine_node_uuid = '5a2c0445-a537-49a4-bdfe-a1fde3a745b4'

    you_strike_me_as_the_reliable_sort_node_uuid = 'd419a52e-f818-2a0b-9ac5-131eb60d273c' # existing node
    alias_you_strike_me_as_the_reliable_sort_node_uuid = '309f54f4-ee7a-492e-bd5a-b68d973ccb8d'

    # d.replace_dialog_flag(you_seem_reliable_node_uuid, 'checkflags', 'Object', bg3.FLAG_Approval_AtLeast_0_For_Sp2, bg3.FLAG_Approval_AtLeast_5_For_Sp2, True, speaker_idx_shadowheart)
    # d.replace_dialog_flag(you_strike_me_as_the_reliable_sort_node_uuid, 'checkflags', 'Object', bg3.FLAG_Approval_AtLeast_0_For_Sp2, bg3.FLAG_Approval_AtLeast_5_For_Sp2, True, speaker_idx_shadowheart)
    # d.replace_dialog_flag(spare_me_the_petty_tyrant_routine_node_uuid, 'checkflags', 'Object', bg3.FLAG_Approval_AtLeast_0_For_Sp2, bg3.FLAG_Approval_AtLeast_10_For_Sp2, True, speaker_idx_shadowheart)

    # You strike me as the reliable sort, but are you sure this is a good idea?
    d.add_dialog_flags(you_strike_me_as_the_reliable_sort_node_uuid, checkflags = (
        bg3.flag_group('Global', (
            bg3.flag(Really_Shadowheart_Softened_Version.uuid, True, None),
        )),
    ))
    d.create_alias_dialog_node(
        alias_you_strike_me_as_the_reliable_sort_node_uuid,
        you_strike_me_as_the_reliable_sort_node_uuid,
        d.get_children_nodes_uuids(you_strike_me_as_the_reliable_sort_node_uuid),
        root = True,
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_Approval_AtLeast_5_For_Sp2, True, speaker_idx_shadowheart),
                # CAMP_Night1_State_SpoenToSecond_079513d2-155d-5c1a-38d2-1626c4171fd1
                bg3.flag('079513d2-155d-5c1a-38d2-1626c4171fd1', False, speaker_idx_tav),
                # CAMP_Night1_State_SpokenToFirst_01411728-20b1-cfed-d0bf-d278a589eeae
                bg3.flag('01411728-20b1-cfed-d0bf-d278a589eeae', False, speaker_idx_tav),
            )),
            bg3.flag_group('Global', (
                bg3.flag(Really_Shadowheart_Softened_Version.uuid, False, None),
            )),
        ),
        setflags = (
            bg3.flag_group('Dialog', (
                # CAMP_Night1_Event_ShadowheartSpokenToFirst_332508e1-9a38-8251-5787-3b1a664acdd2
                bg3.flag('332508e1-9a38-8251-5787-3b1a664acdd2', True, speaker_idx_tav),
            )),
            bg3.flag_group('Object', (
                # CAMP_Night1_State_SpokenToFirst_01411728-20b1-cfed-d0bf-d278a589eeae
                bg3.flag('01411728-20b1-cfed-d0bf-d278a589eeae', True, speaker_idx_tav),
            )),
        ))
    d.add_root_node_before(you_strike_me_as_the_reliable_sort_node_uuid, alias_you_strike_me_as_the_reliable_sort_node_uuid)

    # You seem reliable. I think you know how important it is that we find someone who can cure us. Best if we focus on that.
    d.add_dialog_flags(you_seem_reliable_node_uuid, checkflags = (
        bg3.flag_group('Global', (
            bg3.flag(Really_Shadowheart_Softened_Version.uuid, True, None),
        )),
    ))
    d.create_alias_dialog_node(
        alias_you_seem_reliable_node_uuid,
        you_seem_reliable_node_uuid,
        d.get_children_nodes_uuids(you_seem_reliable_node_uuid),
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_Approval_AtLeast_5_For_Sp2, True, speaker_idx_shadowheart),
            )),
            bg3.flag_group('Global', (
                bg3.flag(Really_Shadowheart_Softened_Version.uuid, False, None),
            )),
        ))
    d.add_child_dialog_node(if_were_to_survive_node_uuid, alias_you_seem_reliable_node_uuid, 0)

    # Spare me the petty tyrant routine - you're better than that.
    d.add_dialog_flags(spare_me_the_petty_tyrant_routine_node_uuid, checkflags = (
        bg3.flag_group('Global', (
            bg3.flag(Really_Shadowheart_Softened_Version.uuid, True, None),
        )),
    ))
    d.create_alias_dialog_node(
        alias_spare_me_the_petty_tyrant_routine_node_uuid,
        spare_me_the_petty_tyrant_routine_node_uuid,
        d.get_children_nodes_uuids(spare_me_the_petty_tyrant_routine_node_uuid),
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_Approval_AtLeast_10_For_Sp2, True, speaker_idx_shadowheart),
            )),
            bg3.flag_group('Global', (
                bg3.flag(Really_Shadowheart_Softened_Version.uuid, False, None),
            )),
        ))
    d.add_child_dialog_node(dont_question_me_node_uuid, alias_spare_me_the_petty_tyrant_routine_node_uuid, 0)


    ###################################################
    # CAMP_Night2_CRD_Shadowheart
    ###################################################
    ab = game_assets.get_modded_dialog_asset_bundle('CAMP_Night2_CRD_Shadowheart')
    d = bg3.dialog_object(ab.dialog)

    speaker_idx_shadowheart = d.get_speaker_slot_index(bg3.SPEAKER_SHADOWHEART)

    i_was_trying_not_to_dwell_on_it_node_uuid = 'c9f18d52-896d-657a-340d-2667ba8203f4' # existing node
    sorry_but_a_problem_shared_node_uuid = 'b6bc5d34-4e7e-b93d-df83-7a0ba28e8662' # existing node
    alias_sorry_but_a_problem_shared_node_uuid = 'a20158a7-36e7-41ed-b51b-372ec12770d5'

    d.add_dialog_flags(sorry_but_a_problem_shared_node_uuid, checkflags = (
        bg3.flag_group('Global', (
            bg3.flag(Really_Shadowheart_Softened_Version.uuid, True, None),
        )),
    ))
    d.create_alias_dialog_node(
        alias_sorry_but_a_problem_shared_node_uuid,
        sorry_but_a_problem_shared_node_uuid,
        d.get_children_nodes_uuids(sorry_but_a_problem_shared_node_uuid),
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_Approval_AtLeast_10_For_Sp2, True, speaker_idx_shadowheart),
            )),
            bg3.flag_group('Global', (
                bg3.flag(Really_Shadowheart_Softened_Version.uuid, False, None),
            )),
        ))
    d.add_child_dialog_node(i_was_trying_not_to_dwell_on_it_node_uuid, alias_sorry_but_a_problem_shared_node_uuid, 0)    


    ###################################################
    # CAMP_Night3_CRD_Shadowheart
    ###################################################
    ab = game_assets.get_modded_dialog_asset_bundle('CAMP_Night3_CRD_Shadowheart')
    d = bg3.dialog_object(ab.dialog)

    speaker_idx_shadowheart = d.get_speaker_slot_index(bg3.SPEAKER_SHADOWHEART)

    you_know_this_could_be_our_last_night_together_node_uuid = 'bc745bc0-f353-221c-40f2-91580d5fd011' # existing node
    what_do_you_have_in_mind_node_uuid = '5d77e3f8-1142-a664-b8d0-85d0d19e6c92' # existing node
    alias_what_do_you_have_in_mind_node_uuid = '7eb08114-e9df-4f90-b54d-88c4f8c4b776'
    id_miss_our_little_conversations_node_uuid = '18fc6ff8-3db2-3382-90ae-85bfa6c75cde' # existing node
    alias_id_miss_our_little_conversations_node_uuid = '220e4948-055e-48c7-9189-4146fe25a063'
    i_hope_so_node_uuid = '9065095f-720b-0b41-8502-42b08547c35c' # existing node

    # I hadn't thought of that. What do you have in mind?
    d.create_alias_dialog_node(
        alias_what_do_you_have_in_mind_node_uuid,
        what_do_you_have_in_mind_node_uuid,
        d.get_children_nodes_uuids(what_do_you_have_in_mind_node_uuid),
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_Approval_AtLeast_10_For_Sp2, True, speaker_idx_shadowheart),
            )),
            bg3.flag_group('Global', (
                bg3.flag(Really_Shadowheart_Softened_Version.uuid, False, None),
            )),
        ))
    d.add_dialog_flags(what_do_you_have_in_mind_node_uuid, checkflags = (
        bg3.flag_group('Global', (
            bg3.flag(Really_Shadowheart_Softened_Version.uuid, True, None),
        )),
    ))

    # I hope not. I'd miss our little conversations... wouldn't you miss them as well?
    d.create_alias_dialog_node(
        alias_id_miss_our_little_conversations_node_uuid,
        id_miss_our_little_conversations_node_uuid,
        d.get_children_nodes_uuids(id_miss_our_little_conversations_node_uuid),
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_Approval_AtLeast_5_For_Sp2, True, speaker_idx_shadowheart),
                bg3.flag(bg3.FLAG_Approval_AtLeast_10_For_Sp2, False, speaker_idx_shadowheart),
            )),
            bg3.flag_group('Global', (
                bg3.flag(Really_Shadowheart_Softened_Version.uuid, False, None),
            )),
        ))
    d.add_dialog_flags(id_miss_our_little_conversations_node_uuid, checkflags = (
        bg3.flag_group('Global', (
            bg3.flag(Really_Shadowheart_Softened_Version.uuid, True, None),
        )),
    ))

    d.delete_all_children_dialog_nodes(you_know_this_could_be_our_last_night_together_node_uuid)
    d.add_child_dialog_node(you_know_this_could_be_our_last_night_together_node_uuid, alias_what_do_you_have_in_mind_node_uuid)
    d.add_child_dialog_node(you_know_this_could_be_our_last_night_together_node_uuid, what_do_you_have_in_mind_node_uuid)
    d.add_child_dialog_node(you_know_this_could_be_our_last_night_together_node_uuid, alias_id_miss_our_little_conversations_node_uuid)
    d.add_child_dialog_node(you_know_this_could_be_our_last_night_together_node_uuid, id_miss_our_little_conversations_node_uuid)
    d.add_child_dialog_node(you_know_this_could_be_our_last_night_together_node_uuid, i_hope_so_node_uuid)


def brain_defeated_always_show_shadowheart_swim_comment() -> None:
    ab = game_assets.get_modded_dialog_asset_bundle('END_BrainBattle_CombatOver_Nested_StandardIntro')
    d = bg3.dialog_object(ab.dialog)

    speaker_idx_shadowheart = d.get_speaker_slot_index(bg3.SPEAKER_SHADOWHEART)

    # existing nodes
    entry_point_cinematic_node_uuid = '31c57f67-b84f-9341-889a-9d6a6d9e1add'
    hells_im_lucky_i_learned_to_swim_node_uuid = 'd328f7f7-a369-9f97-9c0d-e9789aeafb2c'
    ugh_shouldve_learned_to_swim_node_uuid = '7a290a94-ea54-dc90-0dbb-946112d80042'

    # new nodes
    shadowheart_comment_fork_node_uuid = '62b6c613-7a21-4ef1-8633-5e211962d777'
    alias_hells_im_lucky_i_learned_to_swim_node_uuid = '49253219-d1b7-42a3-9fde-cec0de7f457f'
    alias_ugh_shouldve_learned_to_swim_node_uuid = '183765b3-3e09-45b0-942d-c67f4de271af'
    post_shadowheart_comment_fork_node_uuid = '3ebc4713-5de7-4e13-9b57-035248475985'

    children_nodes = d.get_children_nodes_uuids(entry_point_cinematic_node_uuid)
    children_nodes.remove(hells_im_lucky_i_learned_to_swim_node_uuid)
    children_nodes.remove(ugh_shouldve_learned_to_swim_node_uuid)

    d.create_standard_dialog_node(
        shadowheart_comment_fork_node_uuid,
        bg3.SPEAKER_PLAYER,
        [alias_hells_im_lucky_i_learned_to_swim_node_uuid, alias_ugh_shouldve_learned_to_swim_node_uuid, post_shadowheart_comment_fork_node_uuid],
        None)

    d.create_alias_dialog_node(
        alias_hells_im_lucky_i_learned_to_swim_node_uuid,
        hells_im_lucky_i_learned_to_swim_node_uuid,
        [post_shadowheart_comment_fork_node_uuid],
        checkflags = (
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_REALLY_SHADOWHEART, True, speaker_idx_shadowheart),
            )),
            bg3.flag_group('Global', (
                bg3.flag(bg3.FLAG_NIGHT_Shadowheart_Skinnydipping, True, None),
            ))
        ))

    d.create_alias_dialog_node(
        alias_ugh_shouldve_learned_to_swim_node_uuid,
        ugh_shouldve_learned_to_swim_node_uuid,
        [post_shadowheart_comment_fork_node_uuid],
        checkflags = (
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_REALLY_SHADOWHEART, True, speaker_idx_shadowheart),
            )),
            bg3.flag_group('Global', (
                bg3.flag(bg3.FLAG_NIGHT_Shadowheart_Skinnydipping, False, None),
            ))
        ))

    d.create_standard_dialog_node(
        post_shadowheart_comment_fork_node_uuid,
        bg3.SPEAKER_PLAYER,
        children_nodes,
        None)

    d.delete_all_children_dialog_nodes(entry_point_cinematic_node_uuid)
    d.add_child_dialog_node(entry_point_cinematic_node_uuid, shadowheart_comment_fork_node_uuid)


def shadowheart_laezel_fight() -> None:
    ab = game_assets.get_modded_dialog_asset_bundle('CAMP_Shadowheart_IVB_CFM_LaezelFight')
    d = bg3.dialog_object(ab.dialog)

    speaker_idx_tav = d.get_speaker_slot_index(bg3.SPEAKER_PLAYER)
    speaker_idx_laezel = d.get_speaker_slot_index(bg3.SPEAKER_LAEZEL)

    you_carry_a_githyanki_relic_node_uuid = '033f593f-ad97-fbb9-84e1-91d6ee3a5bbb'
    you_hear_that_laezel_common_sense_node_uuid = 'ce999e63-b31f-6866-c699-142395b39d6a'
    we_cant_appease_artefact_stays_with_me_node_uuid = '9f31b2ac-2629-9a16-534c-1d304185aea2'
    laezel_stop_high_approval_node_uuid = '6c88fae6-1851-3e35-13dd-692e94e98cb4'
    laezel_stop_low_approval_node_uuid = '965958c6-5a98-c67e-0dcb-7ce95a12fa29'

    # This flag will trigger osiris logic that decides who is the one to sneak up later
    d.add_dialog_flags(you_carry_a_githyanki_relic_node_uuid, setflags = (
        bg3.flag_group('Object', (
            bg3.flag(Shadowheart_Laezel_Fight_Start.uuid, True, speaker_idx_tav),
        )),
    ))

    d.add_dialog_flags(you_hear_that_laezel_common_sense_node_uuid, setflags = (
        bg3.flag_group('Global', (
            bg3.flag(bg3.FLAG_ORI_Shadowheart_Event_LaezelFirst, True, None),
        )),
    ))
    
    d.add_dialog_flags(we_cant_appease_artefact_stays_with_me_node_uuid, setflags = (
        bg3.flag_group('Global', (
            bg3.flag(bg3.FLAG_ORI_Shadowheart_Event_LaezelFirst, False, None),
        )),
    ))

    d.set_dialog_flags(laezel_stop_high_approval_node_uuid, checkflags = (
        bg3.flag_group('Object', (
            bg3.flag(bg3.FLAG_Approval_AtLeast_20_For_Sp3, True, speaker_idx_laezel),
        )),
    ))
    d.set_dialog_flags(laezel_stop_low_approval_node_uuid, checkflags = (
        bg3.flag_group('Object', (
            bg3.flag(bg3.FLAG_Approval_AtLeast_20_For_Sp3, False, speaker_idx_laezel),
        )),
    ))
    low_approval_active_roll_node = d.find_dialog_node(laezel_stop_low_approval_node_uuid)
    bg3.set_bg3_attribute(low_approval_active_roll_node, 'Advantage', '2')
    bg3.set_bg3_attribute(low_approval_active_roll_node, 'DifficultyClassID', bg3.Act1_Challenging)


def enable_impostor_tg_for_durge() -> None:
    ab = game_assets.get_modded_dialog_asset_bundle('Shadowheart_InParty_Nested_TopicalGreetings')
    d = bg3.dialog_object(ab.dialog)
    t = bg3.timeline_object(ab.timeline, d)

    # This moves the Dark Urge revelation TG before the impostor warning TG
    d.remove_root_node('0852473d-0922-ba1d-8eb3-e2e5132f99bf')
    d.add_root_node_before('91a159b9-49df-fcb3-1238-77c10b456458', '0852473d-0922-ba1d-8eb3-e2e5132f99bf')

    # This keeps camera on Shadowheart the whole time
    start, _ = t.get_tl_node_start_end('d13042dd-c57b-4b5c-abdf-d921f308c52e')
    t.edit_tl_shot('3f3e1896-d94e-4996-899f-7f6f5f2e6ffc', end = start)
    t.remove_effect_component('ca76e63f-8391-402a-9d53-f77d0994ef72')
    t.remove_effect_component('c3a56a1e-25f1-460b-9f9b-6849c1fbf6d2')


def enable_selunite_answer_to_how_are_you() -> None:
    ab = game_assets.get_modded_dialog_asset_bundle('ShadowHeart_InParty2_Nested_DefaultChapter')
    d = bg3.dialog_object(ab.dialog)

    speaker_idx_shadowheart = d.get_speaker_slot_index(bg3.SPEAKER_SHADOWHEART)

    how_are_you_node_uuid = 'd6882eaf-132e-440e-8416-4b2fa547506a' # existing node
    better_now_i_think_node_uuid = '885250cf-7624-4824-a1f0-5ef9febccdb5' # existing node
    whole_at_last_node_uuid = 'e70ff66b-5199-4aa3-870f-c1592c207d26' # existing node
    alias_whole_at_last_node_uuid = '72baf1fb-040e-4724-bda9-c0395c67e091'
    alias_better_now_i_think_node_uuid = 'a5ddf851-21de-4890-8ed7-7b9a3bc957ad'

    d.create_alias_dialog_node(
        alias_whole_at_last_node_uuid,
        whole_at_last_node_uuid,
        [],
        end_node = True,
        checkflags = (
            bg3.flag_group('Global', (
                bg3.flag(Tav_Asked_How_Are_You.uuid, True, None),
                bg3.flag(bg3.FLAG_ORI_Shadowheart_State_Shar_SavedParents, True, None),
            )),
            bg3.flag_group('Object', (
                bg3.flag(Shadowheart_More_Sandcastles.uuid, True, speaker_idx_shadowheart),
            )),
        ))
    d.add_child_dialog_node(how_are_you_node_uuid, alias_whole_at_last_node_uuid, index = 0)

    d.create_alias_dialog_node(
        alias_better_now_i_think_node_uuid,
        better_now_i_think_node_uuid,
        [],
        end_node = True,
        checkflags = (
            bg3.flag_group('Global', (
                bg3.flag(Tav_Asked_How_Are_You.uuid, True, None),
                bg3.flag(bg3.FLAG_ORI_Shadowheart_State_Shar_SavedParents, True, None),
            )),
            bg3.flag_group('Object', (
                bg3.flag(Shadowheart_More_Sandcastles.uuid, False, speaker_idx_shadowheart),
            )),
        ))
    d.add_child_dialog_node(how_are_you_node_uuid, alias_better_now_i_think_node_uuid, index = 0)

    d.add_dialog_flags(better_now_i_think_node_uuid, setflags = (
        bg3.flag_group('Global', (
            bg3.flag(Tav_Asked_How_Are_You.uuid, True, None),
        )),
    ))


def romanced_reaction_join_me() -> None:
    ab = game_assets.get_modded_dialog_asset_bundle('ShadowHeart_InParty')
    d = bg3.dialog_object(ab.dialog)
    t = bg3.timeline_object(ab.timeline, d)

    speaker_idx_tav = d.get_speaker_slot_index(bg3.SPEAKER_PLAYER)
    speaker_idx_shadowheart = d.get_speaker_slot_index(bg3.SPEAKER_SHADOWHEART)

    join_me_node_uuid = '65aab93f-c533-4b96-9e3f-10a74038ec26' # existing node
    wonderful_node_uuid = '4941a8c5-185c-4d91-a5a9-bd2da3271dd5'

    d.create_standard_dialog_node(
        wonderful_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [],
        bg3.text_content('h6cdc1333ga846g4a87g85dbg8df814df7a05', 1),
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_State_PartneredWithShadowheart, True, speaker_idx_tav),
                bg3.flag(bg3.FLAG_Approval_AtLeast_40_For_Sp2, True, speaker_idx_shadowheart)
            )),
        ),
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_OriginAddToParty, True, speaker_idx_shadowheart),
            )),
        ),
        end_node = True)
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '3.6',
        wonderful_node_uuid,
        ((None, '0e8837db-4344-48d0-9175-12262c73806b'),),
        phase_duration = '3.9',
        fade_in = 1.0,
        performance_fade = 1.0,
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 2, None), (1.64, 1024, 1))
        })
    d.add_child_dialog_node(join_me_node_uuid, wonderful_node_uuid, 1)


def patch_noblestalk_line() -> None:
    ab = game_assets.get_modded_dialog_asset_bundle('ShadowHeart_InParty')
    d = bg3.dialog_object(ab.dialog)

    speaker_idx_tav = d.get_speaker_slot_index(bg3.SPEAKER_PLAYER)

    you_should_eat_the_noblestalk_node_uuid = 'f79e7087-259b-29bb-0a44-b17b2e34e322'
    d.set_dialog_flags(
        you_should_eat_the_noblestalk_node_uuid,
        checkflags = (
            bg3.flag_group('Global', (
                bg3.flag(bg3.FLAG_ORI_Shadowheart_State_NobleStalkMemory, False, None),
                bg3.flag(bg3.FLAG_LOW_SharGrotto_State_UnlockedFriendDialog, False, None),
            )),
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_Shadowheart_Event_FailedNoblestalkEating, False, speaker_idx_tav),
                bg3.flag(bg3.FLAG_UND_MushroomHunter_State_HasMushroom, True, speaker_idx_tav),
            )),
            bg3.flag_group('Quest', (
                bg3.flag(bg3.FLAG_ORI_COM_Shadowheart_Travel_Memory_Suppressed, True, speaker_idx_tav),
            )),
        ))



bg3.add_build_procedure('grove_squirell_encounter_wound_flare', grove_squirell_encounter_wound_flare)
bg3.add_build_procedure('mean_greetings', mean_greetings)
bg3.add_build_procedure('shadowheart_laezel_fight', shadowheart_laezel_fight)
bg3.add_build_procedure('add_more_selunite_lines', add_more_selunite_lines)
bg3.add_build_procedure('shadowheart_recruitment', shadowheart_recruitment)
bg3.add_build_procedure('gain_less_approval_other_topics_act1', gain_less_approval_other_topics_act1)
bg3.add_build_procedure('gain_less_approval_sharran_topics_act1', gain_less_approval_sharran_topics_act1)
bg3.add_build_procedure('rejecting_half_illithid', rejecting_half_illithid)
bg3.add_build_procedure('increase_approval_requirements', increase_approval_requirements)
bg3.add_build_procedure('brain_defeated_always_show_shadowheart_swim_comment', brain_defeated_always_show_shadowheart_swim_comment)
bg3.add_build_procedure('shadowheart_how_am_i_holding_up', shadowheart_how_am_i_holding_up)
bg3.add_build_procedure('enable_impostor_tg_for_durge', enable_impostor_tg_for_durge)
bg3.add_build_procedure('enable_selunite_answer_to_how_are_you', enable_selunite_answer_to_how_are_you)
bg3.add_build_procedure('romanced_reaction_join_me', romanced_reaction_join_me)
bg3.add_build_procedure('patch_noblestalk_line', patch_noblestalk_line)


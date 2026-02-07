from __future__ import annotations

import bg3moddinglib as bg3

from .context import get_context
from .flags import *


def patch_nightsong_fate_dialog() -> None:
    game_assets = get_context().assets

    ################################################################################################
    # Dialog: SHA_NightsongsFate_OM_Shadowheart_AOM_OOM_COM.lsf
    # This changes the flow of the scene.
    # Shadowheart may spare Nightsong before she mentiones wolves.
    # Shadowheart may not ask Tav's opinion if Tav trusts her.
    ################################################################################################

    ab = game_assets.get_modded_dialog_asset_bundle('SHA_NightsongsFate_OM_Shadowheart_AOM_OOM_COM')
    d = bg3.dialog_object(ab.dialog)

    speaker_idx_shadowheart = d.get_speaker_slot_index(bg3.SPEAKER_SHADOWHEART)
    speaker_idx_tav = d.get_speaker_slot_index(bg3.SPEAKER_PLAYER)

    trust_shadowheart_do_not_interfere_node_uuid = '47a52989-7b3e-ec9f-0780-8498c528eef0' # existing node
    i_sense_more_in_you_than_you_know_node_uuid = 'df57b11c-03df-93df-65b6-c2cc8a4fe02a' # existing node

    is_this_truly_what_you_want_node_uuid = 'e5fa0eeb-195d-cd93-bb26-fe4fe4dcbfc9' # existing node
    whatever_you_think_node_uuid = '917ee67f-720d-299d-65b8-db261d8b428b' # existing node
    spear_throwaway_alias_first_node_uuid = '9781870a-b05f-6f1b-4331-b04ddf5d493a' # existing node
    spear_throwaway_alias_second_node_uuid = '11bb766f-f81e-a08d-06ad-8fbca76caab9' # existing node
    spear_throwaway_high_approval_node_uuid = '9774808d-43be-c733-90d9-ea6695ce25de' # existing node
    jump_to_decision_node_uuid = 'f48c4366-12f8-47c5-c8e8-91cfa9db0ca5' # existing node
    shadowheart_throws_the_spear_away_node_uuid = '8a910082-021c-412b-885f-ab5eb765f728'
    jump_to_spear_throwaway_high_approval_node_uuid = 'f7bef787-4a94-4859-bde1-3c51d73af6ee'
    shadowheart_hesitates_node_uuid = 'a54d5c74-a5de-4df5-885c-156bd5a35ddc'
    jump_to_spear_throwaway_node_uuid = '167c8bb3-0861-49f4-99b7-52c042efb7dc'
    alias_whatever_you_think_dont_interfere_node_uuid = 'dbd6f20f-81c3-4f08-a57e-2c840b594ad8'


    # If Tav decided to not interfere, set the flag to use it down the line.
    # Trust Shadowheart - do not interfere.
    d.set_dialog_flags(trust_shadowheart_do_not_interfere_node_uuid, setflags = (
        bg3.flag_group('Object', (
            bg3.flag(Nightsong_Fate_Tav_Does_Not_Interfere.uuid, True, speaker_idx_tav),
        )),
    ))

    # If Tav asked this question, Shadowheart will ask what to do if she has enough Nightsong points
    # Is this truly what you want?
    d.set_dialog_flags(is_this_truly_what_you_want_node_uuid, setflags = (
        bg3.flag_group('Object', (
            bg3.flag(Nightsong_Fate_Is_This_Truly_What_You_Want.uuid, True, speaker_idx_tav),
        )),
    ))

    # The following adds a new branch:
    # if approval is 40+,
    # Shadowheart and Tav are dating,
    # Shadowheart read the DJ plea book,
    # Shadowheart read the Unclaimed book,
    # Tav didn't ask "Is this truly what you want"
    # and Shadowheart had the faith crisis,
    # she throws the spear away before Nightsong tells her about the wolves
    d.create_standard_dialog_node(
        shadowheart_throws_the_spear_away_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [jump_to_spear_throwaway_high_approval_node_uuid],
        None,
        checkflags = (
            bg3.flag_group('Global', (
                bg3.flag(bg3.FLAG_ORI_Shadowheart_State_NightsongPoint_HasEnoughPoints, True, None),
                bg3.flag(Really_Shadowheart_Softened_Version.uuid, False, None),
            )),
            bg3.flag_group('Object', (
                bg3.flag(Tav_Gave_DJ_Book_To_Shadowheart.uuid, True, speaker_idx_shadowheart),
                bg3.flag(Tav_Gave_Unclaimed_Book_To_Shadowheart.uuid, True, speaker_idx_shadowheart),
                bg3.flag(bg3.FLAG_Approval_AtLeast_40_For_Sp3, True, speaker_idx_shadowheart),
                bg3.flag(bg3.FLAG_ORI_State_DatingShadowheart, True, speaker_idx_tav),
                bg3.flag(Nightsong_Fate_Is_This_Truly_What_You_Want.uuid, False, speaker_idx_tav),
            )),
        ))
    d.create_jump_dialog_node(jump_to_spear_throwaway_high_approval_node_uuid, spear_throwaway_high_approval_node_uuid, 1)

    d.create_standard_dialog_node(
        shadowheart_hesitates_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [jump_to_decision_node_uuid],
        None)

    d.add_child_dialog_node(trust_shadowheart_do_not_interfere_node_uuid, shadowheart_hesitates_node_uuid, 0)
    d.add_child_dialog_node(trust_shadowheart_do_not_interfere_node_uuid, shadowheart_throws_the_spear_away_node_uuid, 0)
    d.delete_child_dialog_node(trust_shadowheart_do_not_interfere_node_uuid, jump_to_decision_node_uuid) # remove unnecessary jump node

    # Remove flag SHA_NightsongPrison_State_HasSpear_08b1de4b-9f5c-41aa-93ec-9bf4376754b6
    # from animations (Shadowheart throws the spear away)
    # It is way too late to check that flag there
    d.set_dialog_flags(spear_throwaway_alias_first_node_uuid, checkflags = ())
    d.set_dialog_flags(spear_throwaway_alias_second_node_uuid, checkflags = ())

    # The following alias bypasses "I... what do you think? What should I do?"
    # Shadowheart spares Nightsong on her own if Tav decided to not interfere

    # Whatever you think you know of me won't matter, once I become whom I'm meant to be.
    d.create_alias_dialog_node(
        alias_whatever_you_think_dont_interfere_node_uuid,
        whatever_you_think_node_uuid,
        [jump_to_spear_throwaway_node_uuid],
        checkflags = (
            bg3.flag_group('Global', (
                bg3.flag(Really_Shadowheart_Softened_Version.uuid, False, None),
            )),
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_Approval_AtLeast_40_For_Sp3, True, speaker_idx_shadowheart),
                bg3.flag(Nightsong_Fate_Tav_Does_Not_Interfere.uuid, True, speaker_idx_tav),
                bg3.flag(Nightsong_Fate_Is_This_Truly_What_You_Want.uuid, False, speaker_idx_tav),
            )),
        ))
    d.create_jump_dialog_node(jump_to_spear_throwaway_node_uuid, spear_throwaway_alias_first_node_uuid, 1)
    d.add_child_dialog_node(i_sense_more_in_you_than_you_know_node_uuid, alias_whatever_you_think_dont_interfere_node_uuid, 0)


def fix_nightsong_fate_dialog() -> None:
    game_assets = get_context().assets

    ################################################################################################
    # Dialog: SHA_NightsongsFate_OM_Shadowheart_AOM_OOM_COM.lsf
    # Fix the Nightsong decision choice: if Tav accumulated enough Nightsong points and
    # the approval is 20 to 40, add skill checks to persuade Shadowheart.
    ################################################################################################

    # d = bg3.dialog_object(files.get_file('Gustav', 'Mods/GustavDev/Story/DialogsBinary/Companions/Origin_Moments/SHA_NightsongsFate_OM_Shadowheart_AOM_OOM_COM.lsf'))

    ab = game_assets.get_modded_dialog_asset_bundle('SHA_NightsongsFate_OM_Shadowheart_AOM_OOM_COM')
    d = bg3.dialog_object(ab.dialog)

    speaker_idx_shadowheart = d.get_speaker_slot_index(bg3.SPEAKER_SHADOWHEART)

    what_should_i_do_enough_points_node_uuid = 'c742bd23-9e60-a37d-d120-b93ce5367014' # existing node
    roll_she_knows_something_about_you_node_uuid = '700be25e-710f-d3fe-ccee-d46283a14cd8' # existing node, approval < 40
    roll_dont_do_it_node_uuid = 'fa32d463-6547-e866-1624-f513bf01c4c3' # existing node, approval < 20

    alias_she_knows_something_about_you_node_uuid = 'ba492f66-1884-4cf2-9ddd-9ad930d40f2e'
    alias_dont_do_it_node_uuid = '580ab6cd-f3a1-4414-9ada-55720c986746'

    # She knows something about you. Spare her, and see what she has to say.
    d.create_alias_dialog_node(
        alias_she_knows_something_about_you_node_uuid,
        roll_she_knows_something_about_you_node_uuid,
        d.get_children_nodes_uuids(roll_she_knows_something_about_you_node_uuid),
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_Approval_AtLeast_40_For_Sp3, False, speaker_idx_shadowheart),
            )),
        ))

    # Don't do it, Shadowheart. Don't kill her - you'll regret it.
    d.create_alias_dialog_node(
        alias_dont_do_it_node_uuid,
        roll_dont_do_it_node_uuid,
        d.get_children_nodes_uuids(roll_dont_do_it_node_uuid),
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_Approval_AtLeast_40_For_Sp3, False, speaker_idx_shadowheart),
            )),
        ))

    d.add_child_dialog_node(what_should_i_do_enough_points_node_uuid, alias_dont_do_it_node_uuid, 1)
    d.add_child_dialog_node(what_should_i_do_enough_points_node_uuid, alias_she_knows_something_about_you_node_uuid, 1)


def fix_skinny_dipping_crd() -> None:
    game_assets = get_context().assets

    ################################################################################################
    # Dialog: SHA_NightsongsFate_OM_Shadowheart_AOM_OOM_COM.lsf
    # This updates the skinny dipping romance conversation with lines for cases when
    # Tav didn't ask Shadowheart about swimming and night orchids in act 1.
    ################################################################################################

    # d = bg3.dialog_object(files.get_file('Gustav', 'Mods/GustavDev/Story/DialogsBinary/Camp/Camp_Relationship_Dialogs/CAMP_Shadowheart_CRD_SkinnyDippingRomance.lsf'))

    ab = game_assets.get_modded_dialog_asset_bundle('CAMP_Shadowheart_CRD_SkinnyDippingRomance')
    d = bg3.dialog_object(ab.dialog)

    speaker_idx_shadowheart = d.get_speaker_slot_index(bg3.SPEAKER_SHADOWHEART)
    speaker_idx_tav = d.get_speaker_slot_index(bg3.SPEAKER_PLAYER)

    but_what_then_node_uuid = 'ea7134e2-8b0c-a2cd-68a7-bc38a55b015d'
    do_you_remember_i_cant_swim_node_uuid = 'fe4e2f3c-30f6-84b2-fbdd-bda36f6dbc71'
    dont_laugh_but_one_thing_i_rememeber_node_uuid = '54faeb09-bab5-4f65-9a21-becd6c615072'
    i_sacrificed_memories_to_preserve_mission_node_uuid = '9330c8d9-cd67-668c-d73a-01cb1b10b7fa'

    d.set_dialog_flags(i_sacrificed_memories_to_preserve_mission_node_uuid, checkflags = (
        bg3.flag_group('Object', (
            bg3.flag(bg3.FLAG_ORI_Shadowheart_Knows_PersonalInfo, False, speaker_idx_tav),
        )),
        bg3.flag_group('Global', (
            bg3.flag(bg3.FLAG_ORI_Shadowheart_State_Shar_SavedParents, True, None),
        )),

    ))
    d.set_dialog_flags(dont_laugh_but_one_thing_i_rememeber_node_uuid, checkflags = (
        bg3.flag_group('Object', (
            bg3.flag(bg3.FLAG_ORI_Shadowheart_Knows_PersonalInfo, False, speaker_idx_tav),
        )),
    ))

    # Fix the typo in the unused line
    d.set_tagged_text(i_sacrificed_memories_to_preserve_mission_node_uuid, bg3.text_content('h9be538c7g1ec6g43c7g89ebge43d29b981e3', 1))

    d.delete_all_children_dialog_nodes(but_what_then_node_uuid)
    d.add_child_dialog_node(but_what_then_node_uuid, i_sacrificed_memories_to_preserve_mission_node_uuid)
    d.add_child_dialog_node(but_what_then_node_uuid, dont_laugh_but_one_thing_i_rememeber_node_uuid)
    d.add_child_dialog_node(but_what_then_node_uuid, do_you_remember_i_cant_swim_node_uuid)


def fix_waterfall_date_invitation() -> None:
    game_assets = get_context().assets

    ################################################################################################
    # Dialog: ShadowHeart_InParty2.lsf
    # The 'truly connect' line is supposed to appear after the party, not before.
    # This fixes the flag value for the tiefling party such that this line correctly
    # appears after the party when Tav sides with the grove.
    ################################################################################################

    # d = bg3.dialog_object(files.get_file('Gustav', 'Mods/GustavDev/Story/DialogsBinary/Companions/ShadowHeart_InParty2.lsf'))

    ab = game_assets.get_modded_dialog_asset_bundle('ShadowHeart_InParty')
    d = bg3.dialog_object(ab.dialog)

    speaker_idx_tav = d.get_speaker_slot_index(bg3.SPEAKER_PLAYER)
    speaker_idx_shadowheart = d.get_speaker_slot_index(bg3.SPEAKER_SHADOWHEART)

    # exsiting nodes

    # This is the Tav's question after the tiefling party
    i_cant_help_but_feel_truly_connect_after_tiefling_party_vanilla_node_uuid = 'c23ea93d-84ed-0866-0285-bd22a78d0048'
    d.set_dialog_flags(
        i_cant_help_but_feel_truly_connect_after_tiefling_party_vanilla_node_uuid,
        checkflags = (
            bg3.flag_group('Global', (
                bg3.flag(bg3.FLAG_ORI_Shadowheart_Romance1_AfterCelebration_State_QueueInvitation, False, None),
                bg3.flag(bg3.FLAG_VISITEDREGION_INT_Main_A_ACT_3, False, None),
                bg3.flag(bg3.FLAG_ORI_Shadowheart_State_StartedRomance, False, None),
                bg3.flag(bg3.FLAG_CAMP_GoblinHuntCelebration_SD_ROM_NightWithShadowheart_State_Happened, False, None),
                bg3.flag(Shadowheart_After_Shadowfell.uuid, False, None),
                bg3.flag(Really_Shadowheart_Softened_Version.uuid, True, None),
            )),
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_Approval_AtLeast_40_For_Sp2, True, speaker_idx_shadowheart),
                bg3.flag(bg3.FLAG_ORI_State_Partnered, False, speaker_idx_tav),
                bg3.flag(bg3.FLAG_ORI_State_DoubleDating, False, speaker_idx_tav),
                bg3.flag(bg3.FLAG_ORI_State_Dating, False, speaker_idx_shadowheart)
            )),
        ))

    # This is the Tav's question after the goblin/raider party
    i_cant_help_but_feel_truly_connect_after_goblin_party_vanilla_node_uuid = 'aceb7ac7-5b7f-b7c4-bab2-b4d777ac119b'
    d.delete_child_dialog_node(bg3.SHADOWHEART_QUESTION_BANK_ROOT_NODE_UUID, i_cant_help_but_feel_truly_connect_after_goblin_party_vanilla_node_uuid)
    # d.set_dialog_flags(
    #     i_cant_help_but_feel_truly_connect_after_goblin_party_node_uuid,
    #     checkflags = (
    #         bg3.flag_group('Global', (
    #             bg3.flag(bg3.FLAG_NIGHT_GoblinHunt_RaiderCelebration, True, None),
    #             bg3.flag(bg3.FLAG_ORI_Shadowheart_Romance1_AfterCelebration_State_QueueInvitation, False, None),
    #             bg3.flag(bg3.FLAG_VISITEDREGION_INT_Main_A_ACT_3, False, None),
    #             bg3.flag(bg3.FLAG_ORI_Shadowheart_State_StartedRomance, False, None),
    #             bg3.flag(bg3.FLAG_CAMP_GoblinHuntCelebration_SD_ROM_NightWithShadowheart_State_Happened, False, None),
    #             bg3.flag(Shadowheart_After_Shadowfell.uuid, False, None),
    #             bg3.flag(Really_Shadowheart_Softened_Version.uuid, True, None),
    #         )),
    #         bg3.flag_group('Object', (
    #             bg3.flag(bg3.FLAG_Approval_AtLeast_40_For_Sp2, True, speaker_idx_shadowheart),
    #             bg3.flag(bg3.FLAG_ORI_State_Partnered, False, speaker_idx_tav),
    #             bg3.flag(bg3.FLAG_ORI_State_DoubleDating, False, speaker_idx_tav),
    #             bg3.flag(bg3.FLAG_ORI_State_Dating, False, speaker_idx_shadowheart)
    #         )),
    #     ))

    # New nodes

    insertion_pos = d.get_child_node_index(bg3.SHADOWHEART_QUESTION_BANK_ROOT_NODE_UUID, i_cant_help_but_feel_truly_connect_after_tiefling_party_vanilla_node_uuid)
    if insertion_pos is None:
        raise RuntimeError(f"Cannot find node {i_cant_help_but_feel_truly_connect_after_tiefling_party_vanilla_node_uuid} in Shadowheart's main dialog")

    i_cant_help_but_feel_truly_connect_after_tiefling_party_node_uuid = '282a778d-f2cc-42c4-aed5-18dd7995a4c0'
    i_cant_help_but_feel_truly_connect_after_goblin_party_node_uuid = '52b38628-b5ea-4e14-a373-befb9eebaafe'
    i_cant_help_but_feel_truly_connect_no_party_node_uuid = '212ba667-d9d0-49bd-863f-41287db856ec'

    children_nodes = d.get_children_nodes_uuids(i_cant_help_but_feel_truly_connect_after_tiefling_party_vanilla_node_uuid)

    # This is the Tav's question after the tiefling party
    d.create_standard_dialog_node(
        i_cant_help_but_feel_truly_connect_after_tiefling_party_node_uuid,
        bg3.SPEAKER_PLAYER,
        children_nodes,
        bg3.text_content('h517c0615g4362g4851gbd3cg5ad9f7996ee0', 3),
        constructor = bg3.dialog_object.QUESTION,
        checkflags = (
            bg3.flag_group('Global', (
                bg3.flag(bg3.FLAG_NIGHT_GoblinHunt_TieflingCelebration, True, None),
                bg3.flag(bg3.FLAG_NIGHT_GoblinHunt_RaiderCelebration, False, None),
                bg3.flag(bg3.DEN_Lockdown_State_Active, False, None),
                bg3.flag(bg3.FLAG_ORI_Shadowheart_Romance1_AfterCelebration_State_QueueInvitation, False, None),
                bg3.flag(bg3.FLAG_VISITEDREGION_INT_Main_A_ACT_3, False, None),
                bg3.flag(bg3.FLAG_ORI_Shadowheart_State_StartedRomance, False, None),
                bg3.flag(bg3.FLAG_CAMP_GoblinHuntCelebration_SD_ROM_NightWithShadowheart_State_Happened, False, None),
                bg3.flag(Shadowheart_After_Shadowfell.uuid, False, None),
                bg3.flag(Really_Shadowheart_Softened_Version.uuid, False, None),
            )),
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_Approval_AtLeast_40_For_Sp2, True, speaker_idx_shadowheart),
                bg3.flag(bg3.FLAG_ORI_State_Partnered, False, speaker_idx_tav),
                bg3.flag(bg3.FLAG_ORI_State_DoubleDating, False, speaker_idx_tav),
                bg3.flag(bg3.FLAG_ORI_State_Dating, False, speaker_idx_shadowheart)
            )),
        ),
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_Shadowheart_InParty_Event_MissedRomanceStart, True, speaker_idx_tav),
            )),
        ))
    d.add_child_dialog_node(bg3.SHADOWHEART_QUESTION_BANK_ROOT_NODE_UUID, i_cant_help_but_feel_truly_connect_after_tiefling_party_node_uuid, insertion_pos)

    # This is the Tav's question after the goblin/raider party
    d.create_standard_dialog_node(
        i_cant_help_but_feel_truly_connect_after_goblin_party_node_uuid,
        bg3.SPEAKER_PLAYER,
        children_nodes,
        bg3.text_content('h517c0615g4362g4851gbd3cg5ad9f7996ee0', 3),
        constructor = bg3.dialog_object.QUESTION,
        checkflags = (
            bg3.flag_group('Global', (
                bg3.flag(bg3.FLAG_NIGHT_GoblinHunt_RaiderCelebration, True, None),
                bg3.flag(bg3.FLAG_NIGHT_GoblinHunt_TieflingCelebration, False, None),
                bg3.flag(bg3.DEN_Lockdown_State_Active, False, None),
                bg3.flag(bg3.FLAG_ORI_Shadowheart_Romance1_AfterCelebration_State_QueueInvitation, False, None),
                bg3.flag(bg3.FLAG_VISITEDREGION_INT_Main_A_ACT_3, False, None),
                bg3.flag(bg3.FLAG_ORI_Shadowheart_State_StartedRomance, False, None),
                bg3.flag(bg3.FLAG_CAMP_GoblinHuntCelebration_SD_ROM_NightWithShadowheart_State_Happened, False, None),
                bg3.flag(Shadowheart_After_Shadowfell.uuid, False, None),
                bg3.flag(Really_Shadowheart_Softened_Version.uuid, False, None),
            )),
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_Approval_AtLeast_40_For_Sp2, True, speaker_idx_shadowheart),
                bg3.flag(bg3.FLAG_ORI_State_Partnered, False, speaker_idx_tav),
                bg3.flag(bg3.FLAG_ORI_State_DoubleDating, False, speaker_idx_tav),
                bg3.flag(bg3.FLAG_ORI_State_Dating, False, speaker_idx_shadowheart)
            )),
        ),
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_Shadowheart_InParty_Event_MissedRomanceStart, True, speaker_idx_tav),
            )),
        ))
    d.add_child_dialog_node(bg3.SHADOWHEART_QUESTION_BANK_ROOT_NODE_UUID, i_cant_help_but_feel_truly_connect_after_goblin_party_node_uuid, insertion_pos)

    # If druid lair is locked down
    d.create_standard_dialog_node(
        i_cant_help_but_feel_truly_connect_no_party_node_uuid,
        bg3.SPEAKER_PLAYER,
        children_nodes,
        bg3.text_content('h517c0615g4362g4851gbd3cg5ad9f7996ee0', 3),
        constructor = bg3.dialog_object.QUESTION,
        checkflags = (
            bg3.flag_group('Global', (
                bg3.flag(bg3.DEN_Lockdown_State_Active, True, None),
                bg3.flag(bg3.FLAG_NIGHT_GoblinHunt_TieflingCelebration, False, None),
                bg3.flag(bg3.FLAG_NIGHT_GoblinHunt_RaiderCelebration, False, None),
                bg3.flag(bg3.FLAG_ORI_Shadowheart_Romance1_AfterCelebration_State_QueueInvitation, False, None),
                bg3.flag(bg3.FLAG_VISITEDREGION_INT_Main_A_ACT_3, False, None),
                bg3.flag(bg3.FLAG_ORI_Shadowheart_State_StartedRomance, False, None),
                bg3.flag(bg3.FLAG_CAMP_GoblinHuntCelebration_SD_ROM_NightWithShadowheart_State_Happened, False, None),
                bg3.flag(Shadowheart_After_Shadowfell.uuid, False, None),
                bg3.flag(Really_Shadowheart_Softened_Version.uuid, False, None),
            )),
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_Approval_AtLeast_40_For_Sp2, True, speaker_idx_shadowheart),
                bg3.flag(bg3.FLAG_ORI_State_Partnered, False, speaker_idx_tav),
                bg3.flag(bg3.FLAG_ORI_State_DoubleDating, False, speaker_idx_tav),
                bg3.flag(bg3.FLAG_ORI_State_Dating, False, speaker_idx_shadowheart)
            )),
        ),
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_Shadowheart_InParty_Event_MissedRomanceStart, True, speaker_idx_tav),
            )),
        ))
    d.add_child_dialog_node(bg3.SHADOWHEART_QUESTION_BANK_ROOT_NODE_UUID, i_cant_help_but_feel_truly_connect_no_party_node_uuid, insertion_pos)

    # Fallback questions in case if druid/goblin conflict wasn't concluded
    # When the party has reached the shadow curse
    i_cant_help_but_feel_truly_connect_fallback_scl_node_uuid = 'cecefb62-0ac8-42c5-af32-4963d58781b9'
    d.create_standard_dialog_node(
        i_cant_help_but_feel_truly_connect_fallback_scl_node_uuid,
        bg3.SPEAKER_PLAYER,
        children_nodes,
        bg3.text_content('h517c0615g4362g4851gbd3cg5ad9f7996ee0', 3),
        constructor = bg3.dialog_object.QUESTION,
        checkflags = (
            bg3.flag_group('Global', (
                bg3.flag(bg3.FLAG_VISITEDREGION_SCL_Main_A_ACT_2, True, None),
                bg3.flag(bg3.FLAG_NIGHT_GoblinHunt_TieflingCelebration, False, None),
                bg3.flag(bg3.FLAG_NIGHT_GoblinHunt_RaiderCelebration, False, None),
                bg3.flag(bg3.DEN_Lockdown_State_Active, False, None),
                bg3.flag(bg3.FLAG_ORI_Shadowheart_Romance1_AfterCelebration_State_QueueInvitation, False, None),
                bg3.flag(bg3.FLAG_VISITEDREGION_INT_Main_A_ACT_3, False, None),
                bg3.flag(bg3.FLAG_ORI_Shadowheart_State_StartedRomance, False, None),
                bg3.flag(bg3.FLAG_CAMP_GoblinHuntCelebration_SD_ROM_NightWithShadowheart_State_Happened, False, None),
                bg3.flag(Shadowheart_After_Shadowfell.uuid, False, None),
                bg3.flag(Really_Shadowheart_Softened_Version.uuid, False, None),
            )),
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_Approval_AtLeast_40_For_Sp2, True, speaker_idx_shadowheart),
                bg3.flag(bg3.FLAG_ORI_State_Partnered, False, speaker_idx_tav),
                bg3.flag(bg3.FLAG_ORI_State_DoubleDating, False, speaker_idx_tav),
                bg3.flag(bg3.FLAG_ORI_State_Dating, False, speaker_idx_shadowheart)
            )),
        ),
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_Shadowheart_InParty_Event_MissedRomanceStart, True, speaker_idx_tav),
            )),
        ))
    d.add_child_dialog_node(bg3.SHADOWHEART_QUESTION_BANK_ROOT_NODE_UUID, i_cant_help_but_feel_truly_connect_fallback_scl_node_uuid, insertion_pos)

    # When the party has reached the creche
    i_cant_help_but_feel_truly_connect_fallback_cre_node_uuid = '14deced7-4080-43d1-ab34-054335484c43'
    d.create_standard_dialog_node(
        i_cant_help_but_feel_truly_connect_fallback_cre_node_uuid,
        bg3.SPEAKER_PLAYER,
        children_nodes,
        bg3.text_content('h517c0615g4362g4851gbd3cg5ad9f7996ee0', 3),
        constructor = bg3.dialog_object.QUESTION,
        checkflags = (
            bg3.flag_group('Global', (
                bg3.flag(bg3.FLAG_VISITEDREGION_CRE_Main_A, True, None),
                bg3.flag(bg3.FLAG_NIGHT_GoblinHunt_TieflingCelebration, False, None),
                bg3.flag(bg3.FLAG_NIGHT_GoblinHunt_RaiderCelebration, False, None),
                bg3.flag(bg3.DEN_Lockdown_State_Active, False, None),
                bg3.flag(bg3.FLAG_ORI_Shadowheart_Romance1_AfterCelebration_State_QueueInvitation, False, None),
                bg3.flag(bg3.FLAG_VISITEDREGION_INT_Main_A_ACT_3, False, None),
                bg3.flag(bg3.FLAG_ORI_Shadowheart_State_StartedRomance, False, None),
                bg3.flag(bg3.FLAG_CAMP_GoblinHuntCelebration_SD_ROM_NightWithShadowheart_State_Happened, False, None),
                bg3.flag(Shadowheart_After_Shadowfell.uuid, False, None),
                bg3.flag(Really_Shadowheart_Softened_Version.uuid, False, None),
            )),
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_Approval_AtLeast_40_For_Sp2, True, speaker_idx_shadowheart),
                bg3.flag(bg3.FLAG_ORI_State_Partnered, False, speaker_idx_tav),
                bg3.flag(bg3.FLAG_ORI_State_DoubleDating, False, speaker_idx_tav),
                bg3.flag(bg3.FLAG_ORI_State_Dating, False, speaker_idx_shadowheart)
            )),
        ),
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_Shadowheart_InParty_Event_MissedRomanceStart, True, speaker_idx_tav),
            )),
        ))
    d.add_child_dialog_node(bg3.SHADOWHEART_QUESTION_BANK_ROOT_NODE_UUID, i_cant_help_but_feel_truly_connect_fallback_cre_node_uuid, insertion_pos)

 
def fix_now_and_always_thorm_mausoleum() -> None:
    game_assets = get_context().assets

    ################################################################################################
    # Dialog: ShadowHeart_InParty2_Nested_ShadowCurseChapter.lsf
    # At the entrance of the Thorm mausoleum, when Tav & Shadowheart return from the Shadowfell,
    # Tav should not be able to tell her "You're not alone. You have me." if they are in
    # exclusive relationship with someone else.
    ################################################################################################

    ab = game_assets.get_modded_dialog_asset_bundle('ShadowHeart_InParty2_Nested_ShadowCurseChapter')
    d = bg3.dialog_object(ab.dialog)

    speaker_idx_tav = d.get_speaker_slot_index(bg3.SPEAKER_PLAYER)

    youre_not_alone_you_have_me_node_uuid = '10072be5-fffc-455d-9b41-7d5cf0c0ecf5'
    
    d.set_dialog_flags(youre_not_alone_you_have_me_node_uuid, setflags = (
        bg3.flag_group('Global', (
            bg3.flag(bg3.FLAG_VISITEDREGION_BGO_Main_A, False, None),
        )),
        bg3.flag_group('Object', (
            bg3.flag(bg3.FLAG_ORI_State_DatingShadowheart, True, speaker_idx_tav),
            bg3.flag(bg3.FLAG_ORI_State_Partnered, False, speaker_idx_tav),
        ))
    ))


def fix_lolth_sworn_drow() -> None:
    game_assets = get_context().assets

    ab = game_assets.get_modded_dialog_asset_bundle('ShadowHeart_InParty2_Nested_SharranChapter')
    d = bg3.dialog_object(ab.dialog)

    speaker_idx_tav = d.get_speaker_slot_index(bg3.SPEAKER_PLAYER)

    # I worship Lolth - your secret does not shock me. I've seen and done so much worse.
    d.set_dialog_flags('e12daa56-c03e-4ca0-ad53-0d1323997a4c', checkflags = (
        bg3.flag_group('Tag', (
            bg3.flag(bg3.GOD_LOLTH, True, speaker_idx_tav),
        )),
    ))


def fix_all_that_happened_raider_victory() -> None:
    game_assets = get_context().assets

    ab = game_assets.get_modded_dialog_asset_bundle('ShadowHeart_InParty2_Nested_DefaultChapter')
    d = bg3.dialog_object(ab.dialog)

    # Fix for goblin victory
    all_that_happened_node_uuid = '23d586aa-5f3e-4ca6-9e19-2568e8846003' # existing alias to a node
    new_jump_node_uuid = '5735031d-ad19-435f-8aa3-6c90555fb72c'
    d.create_jump_dialog_node(new_jump_node_uuid, bg3.SHADOWHEART_THOUGHTS_QUESTION_BANK_NODE_UUID, 2)
    d.add_child_dialog_node(all_that_happened_node_uuid, new_jump_node_uuid)

    # Fix for grove lockdown
    all_that_happened_node_uuid = 'c1feb3fd-2770-45f1-b63a-e79e0523e119' # existing alias to a node
    new_jump_node_uuid = '5735031d-ad19-435f-8aa3-6c90555fb72c'
    d.create_jump_dialog_node(new_jump_node_uuid, bg3.SHADOWHEART_THOUGHTS_QUESTION_BANK_NODE_UUID, 2)
    d.add_child_dialog_node(all_that_happened_node_uuid, new_jump_node_uuid)


def fix_topical_greetings() -> None:
    game_assets = get_context().assets

    ################################################################################################
    # Dialog: Shadowheart_InParty_Nested_TopicalGreetings.lsf
    ################################################################################################

    ab = game_assets.get_modded_dialog_asset_bundle('Shadowheart_InParty_Nested_TopicalGreetings')
    d = bg3.dialog_object(ab.dialog)

    speaker_idx_shadowheart = d.get_speaker_slot_index(bg3.SPEAKER_SHADOWHEART)

    it_feels_like_my_entire_world_has_been_upended_node_uuid = '5cae008d-231e-4668-abf5-3d81c9f8e5ab'
    d.set_dialog_flags(
        it_feels_like_my_entire_world_has_been_upended_node_uuid,
        checkflags = (
            bg3.flag_group('Object', (
                # TG_ORI_Shadowheart_NightsongMeeting_b5281f81-60b9-4dea-87ed-f3b8b95e4364
                bg3.flag('b5281f81-60b9-4dea-87ed-f3b8b95e4364', True, speaker_idx_shadowheart),
            )),
            bg3.flag_group('Global', (
                # NIGHT_NightsongShadowheartVisit_5cf06d9e-44ce-4431-a1c6-839bfdad5f79
                bg3.flag('5cf06d9e-44ce-4431-a1c6-839bfdad5f79', False, None),
            )),
        ),
        setflags = (
            bg3.flag_group('Object', (
                # TG_ORI_Shadowheart_NightsongMeeting_b5281f81-60b9-4dea-87ed-f3b8b95e4364
                bg3.flag('b5281f81-60b9-4dea-87ed-f3b8b95e4364', False, speaker_idx_shadowheart),
            )),
        ))

    # remove Shadowheart_InParty_State_EndDialog_83c61046-f6c7-4d0b-a012-37fdce36d957
    # keep only TG_ORI_Astarion_KidnappedByGurHunter_d2df26ef-545e-43c4-99e1-cfe0f4e1ac06
    # I'll miss Astarion... though perhaps my neck won't.
    d.set_dialog_flags('2bda6e84-9c72-43ed-b2a3-f53fed3c431a', setflags = (
        bg3.flag_group('Object', (
            bg3.flag('d2df26ef-545e-43c4-99e1-cfe0f4e1ac06', False, speaker_idx_shadowheart),
        )),
    ))

    ################################################################################################
    # Dialog: SHA_TempleLeave_OM_Shadowheart_COM.lsf
    ################################################################################################

    ab = game_assets.get_modded_dialog_asset_bundle('SHA_TempleLeave_OM_Shadowheart_COM')
    d = bg3.dialog_object(ab.dialog)

    speaker_idx_shadowheart = d.get_speaker_slot_index(bg3.SPEAKER_SHADOWHEART)
    speaker_idx_tav = d.get_speaker_slot_index(bg3.SPEAKER_PLAYER)

    # Sets the topical greetings when Shadowheart leaves the party after Tav didn't take her to the Nightsong
    you_would_be_wise_to_forget_me_node_uuid = '5c6911ac-4fa1-4d0d-8ef1-41e9e6b7cf3b'
    d.set_dialog_flags(you_would_be_wise_to_forget_me_node_uuid, setflags = (
        bg3.flag_group('Object', (
            bg3.flag(bg3.FLAG_Companion_Leaves_Party, True, speaker_idx_shadowheart),
            # TG_ORI_Shadowheart_TempleLeftParty_e5a8262e-26bc-4349-ac30-1ecb45733642
            bg3.flag('e5a8262e-26bc-4349-ac30-1ecb45733642', True, speaker_idx_tav),
        )),
    ))


def fix_nightsong_meeting() -> None:
    game_assets = get_context().assets
    files = get_context().files

    ################################################################################################
    # Dialog: CAMP_NightsongShadowheartVisit_CFM.lsf
    ################################################################################################

    ab = game_assets.get_modded_dialog_asset_bundle('CAMP_NightsongShadowheartVisit_CFM')
    d = bg3.dialog_object(ab.dialog)
    t = bg3.timeline_object(ab.timeline, d)

    reaction_plus_5 = bg3.reaction_object.create_new(files, { bg3.SPEAKER_SHADOWHEART: 5 })
    reaction_minus_10_1 = bg3.reaction_object.create_new(files, { bg3.SPEAKER_SHADOWHEART: -10 })
    reaction_minus_10_2 = bg3.reaction_object.create_new(files, { bg3.SPEAKER_SHADOWHEART: -10 })

    my_parents_i_need_to_save_them_node_uuid = 'c0bc8c5a-b4ca-d0c4-b373-481911aadd66' # existing node
    your_parents_are_with_your_abductors_node_uuid = '33740734-0d3e-17f4-7e9a-fb8fdfc06a1c' # existing node
    ill_help_node_uuid = '36870dc1-0ba7-c2ed-4dbc-d64231b82f1e' # existing node
    perhaps_this_isnt_a_good_idea_node_uuid = '6d78331c-796b-1868-7e91-2d998d51c683' # existing node
    getting_your_parents_back_sounds_dangerous_node_uuid = '1ef8872b-da28-f740-0bae-4e6432d7e32e' # existing node
    weve_got_other_concerns_node_uuid = '2f64eb7c-12af-9fbf-2513-7948547ac6b7' # existing node
    we_have_other_concerns_node_uuid = 'c9942c9c-be95-dc8b-8d53-afc23931c27a' # existing node
    there_are_always_other_concerns_node_uuid = '66885154-4691-2d40-43f5-95553bbca7c3' # existing node
    your_parents_both_followed_the_moonmaiden_node_uuid = 'cfff47bc-2b5e-9f84-81c2-b0081acd532d' # existing node
    you_were_to_receive_selunes_guidance_node_uuid = '72ec2b40-383a-fe28-eadc-5725158ab4f3' # existing node
    it_is_a_tragedy_node_uuid = 'd354193b-f271-967d-dcff-62ef7056d774' # existing node

    post_isobel_questions_node_uuid = 'bed4fc40-6bfc-4f4c-8dfb-c61d6b7edb29' # new node
    jump_to_post_isobel_questions_node_uuid = '84856100-8792-458b-ba96-1f38470becdc' # new node
    say_nothing_node_uuid = 'f96efc7c-db8e-41a0-bb6f-037833cf322b' # new node

    # Responses to Shadowheart's "My parents. I need to save them."

    # I'll help.
    d.set_approval_rating(ill_help_node_uuid, reaction_plus_5.uuid)


    # Perhaps this isn't a good idea.
    d.set_approval_rating(perhaps_this_isnt_a_good_idea_node_uuid, reaction_minus_10_1.uuid)
    d.set_approval_rating(getting_your_parents_back_sounds_dangerous_node_uuid, reaction_minus_10_1.uuid)

    # We've got other concerns.
    d.set_approval_rating(weve_got_other_concerns_node_uuid, reaction_minus_10_2.uuid)
    d.set_approval_rating(we_have_other_concerns_node_uuid, reaction_minus_10_2.uuid)

    # Remove negative reactions from these two nodes beacuse they are replaced by -10
    d.remove_approval_rating(your_parents_are_with_your_abductors_node_uuid)
    d.remove_approval_rating(there_are_always_other_concerns_node_uuid)

    # Say nothing.
    d.create_standard_dialog_node(
        say_nothing_node_uuid,
        bg3.SPEAKER_PLAYER,
        [your_parents_are_with_your_abductors_node_uuid],
        bg3.text_content('h0a252ff5g9784g4fd1ga881g34a06ef65b84', 1),
        constructor = bg3.dialog_object.QUESTION)

    d.add_child_dialog_node(my_parents_i_need_to_save_them_node_uuid, say_nothing_node_uuid)

    # Isobel's line "It is a tragedy that the Moonmaiden's rite was perverted by Shar. Your future was stolen from you."

    d.delete_child_dialog_node(your_parents_both_followed_the_moonmaiden_node_uuid, it_is_a_tragedy_node_uuid)
    d.set_dialog_flags(you_were_to_receive_selunes_guidance_node_uuid, checkflags = ())
    d.delete_all_children_dialog_nodes(you_were_to_receive_selunes_guidance_node_uuid)
    d.delete_all_children_dialog_nodes(it_is_a_tragedy_node_uuid)
    d.add_child_dialog_node(you_were_to_receive_selunes_guidance_node_uuid, it_is_a_tragedy_node_uuid)
    d.add_child_dialog_node(you_were_to_receive_selunes_guidance_node_uuid, post_isobel_questions_node_uuid)
    d.add_child_dialog_node(it_is_a_tragedy_node_uuid, jump_to_post_isobel_questions_node_uuid)

    d.create_standard_dialog_node(
        post_isobel_questions_node_uuid,
        bg3.SPEAKER_NIGHTSONG,
        [
            ill_help_node_uuid,
            getting_your_parents_back_sounds_dangerous_node_uuid,
            we_have_other_concerns_node_uuid,
            say_nothing_node_uuid
        ],
        None,
        checkflags = (
            bg3.flag_group('Script', (
                # GEN_IsSpeakerPresent_4_7fd98b6e-11d5-28e0-bc67-bb0925834fa3
                bg3.flag('7fd98b6e-11d5-28e0-bc67-bb0925834fa3', False, None),
            )),
        ))
    d.create_jump_dialog_node(jump_to_post_isobel_questions_node_uuid, post_isobel_questions_node_uuid, 2)

    # Fix Isobel's camera

    # Phase 15, dialog node 72ec2b40-383a-fe28-eadc-5725158ab4f3
    # Nightsong: You were to receive Selune's guidance in those woods. You were to come of age. Instead, Shar's followers snatched you. They must have been watching you for a long time.
    tl_phase = t.use_existing_phase(15)
    t.remove_effect_component('eab347ee-138e-4387-a41c-42ba8a4573b3') # TLShot 116.85506 to 127.87506
    t.remove_effect_component('09fc0251-0084-4ed8-98c3-e27c7aadc355') # TLShot 127.87506 to 128.18506
    t.create_tl_shot('d16ba983-3fcc-4c9f-9f91-50086372f49a', '0.0', tl_phase.duration, is_snapped_to_end = True)

    # Phase 27, dialog node d354193b-f271-967d-dcff-62ef7056d774
    # Isobel: It is a tragedy that the Moonmaiden's rite was perverted by Shar. Your future was stolen from you.
    isobel_cam1 = 'f81968dd-219e-46be-9adc-05d13b4df47b'
    isobel_cam2 = '6a8fc012-6956-4d18-8ecb-48ca6888c66d'
    tl_phase = t.use_existing_phase(27)
    t.remove_effect_component('3f279f59-3547-4d78-8659-5af185546a31') # TLShot 206.72334 to 213.61334
    t.remove_effect_component('cffd2ea5-fd23-4d4d-a125-8a86830ed08b') # TLShot 213.61334 to 214.23334
    time_delta = bg3.decimal_from_str('0.7')
    t.create_tl_actor_node(bg3.timeline_object.SHOW_VISUAL, bg3.SPEAKER_ISOBEL, '0.0', tl_phase.duration, (
        t.create_value_key(time = '0.0', interpolation_type = 3, value_name = 'ShowVisual', value = True),
    ))
    t.create_tl_shot(isobel_cam1, '0.0', tl_phase.duration - time_delta)
    t.create_tl_shot('bbc70139-a7c3-4fe1-9015-1a8fa5ddc302', tl_phase.duration - time_delta, tl_phase.duration, is_snapped_to_end = True)

    ################################################################################################
    # Dialog: Shadowheart_InParty.lsf
    ################################################################################################

    # The following adds a temporary greeting:
    # It feels like my entire world has been upended.

    ab = game_assets.get_modded_dialog_asset_bundle('Shadowheart_InParty')
    d = bg3.dialog_object(ab.dialog)
    t = bg3.timeline_object(ab.timeline, d)

    speaker_idx_tav = d.get_speaker_slot_index(bg3.SPEAKER_PLAYER)

    nightsong_discussion_entry_node_uuid = '6315b369-c63a-1fbe-3b09-c9c0b4b2a834' # existing node
    it_feels_like_my_entire_world_has_been_upended_node_uuid = 'c8080ecb-2c3c-434e-88ed-dd1f5c83cec9' # new node
    i_wanted_to_ask_you_about_node_uuid = '98cc5f86-d136-4132-a564-7bbe0bd45bf7' # new node
    i_think_you_need_some_time_alone_node_uuid = '3ee737a1-14c7-4f19-b96c-ee88b8b2fffd' # new node
    im_sorry_it_might_be_best_kept_until_later_node_uuid = 'f8ff71d9-f1ff-4220-a60e-33c5c300d97d' # new node
    thank_you_we_can_talk_again_soon_node_uuid = 'beddf0f4-f37f-42d2-840b-9ef2dfbf0e75' # new node

    # It feels like my entire world has been upended.
    d.create_standard_dialog_node(
        it_feels_like_my_entire_world_has_been_upended_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [i_wanted_to_ask_you_about_node_uuid, i_think_you_need_some_time_alone_node_uuid],
        bg3.text_content('h3a502df3g6868g4454g9ea2ga732fe01434f', 2),
        checkflags = (
            bg3.flag_group("Dialog", (
                # Shadowheart_InParty_State_DiscussedNightsongMeeting_2a470bae-37a3-4ca4-937c-be2b7c90ab44
                bg3.flag('2a470bae-37a3-4ca4-937c-be2b7c90ab44', False, speaker_idx_tav),
            )),
            bg3.flag_group("Global", (
                bg3.flag(bg3.FLAG_CAMP_Shadowheart_State_HadNightsongMeeting, True, None),
            )),
        ))
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '3.2',
        it_feels_like_my_entire_world_has_been_upended_node_uuid,
        ((None, '8942c483-83c9-4974-9f47-87cd1dd10828'),),
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 64, 2), (1.31, 32, None)),
            bg3.SPEAKER_PLAYER: ((0.0, 2048, None),)
        })

    # I wanted to ask you about what Nightsong said.
    d.create_standard_dialog_node(
        i_wanted_to_ask_you_about_node_uuid,
        bg3.SPEAKER_PLAYER,
        [im_sorry_it_might_be_best_kept_until_later_node_uuid],
        bg3.text_content('h913ca6e1g36f2g44d4g9bcdg3606070423ac', 1),
        constructor = bg3.dialog_object.QUESTION)

    # I'm sorry, I think you need some time alone. Let's talk later.
    d.create_standard_dialog_node(
        i_think_you_need_some_time_alone_node_uuid,
        bg3.SPEAKER_PLAYER,
        [thank_you_we_can_talk_again_soon_node_uuid],
        bg3.text_content('he395601bg05fcg416agabc4gdf8ee6ce70c1', 1),
        constructor = bg3.dialog_object.QUESTION)

    # I'm sorry. It might be best kept until later. I'd be a poor counsel and worse company just now.
    d.create_standard_dialog_node(
        im_sorry_it_might_be_best_kept_until_later_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [],
        bg3.text_content('hd4953918g2c68g4e38g8d97g59f78056fddf', 1),
        end_node = True)
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '11.2',
        im_sorry_it_might_be_best_kept_until_later_node_uuid,
        ((None, '0e8837db-4344-48d0-9175-12262c73806b'),),
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 2048, None), (6.45, 32, None)),
            bg3.SPEAKER_PLAYER: ((0.0, 2048, None),)
        })

    # Thank you. We can talk again soon.
    d.create_standard_dialog_node(
        thank_you_we_can_talk_again_soon_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [],
        bg3.text_content('h7e834aecg306ag4955g91f4g864e101655d1', 1),
        end_node = True)
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '3.011',
        thank_you_we_can_talk_again_soon_node_uuid,
        ((None, '0e8837db-4344-48d0-9175-12262c73806b'),),
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 64, 2), (1.95, 64, None), (2.77, 32, None)),
            bg3.SPEAKER_PLAYER: ((0.0, 64, 2),)
        })


    d.add_root_node_after(nightsong_discussion_entry_node_uuid, it_feels_like_my_entire_world_has_been_upended_node_uuid)




def fix_shadowheart_pod_opening_scene() -> None:
    game_assets = get_context().assets

    ################################################################################################
    # Dialog: TUT_TransformChamber_PodLock.lsf
    # The following doesn't fix the scene yet, need to figure it out
    ################################################################################################

    ab = game_assets.get_modded_dialog_asset_bundle('TUT_TransformChamber_PodLock')
    d = bg3.dialog_object(ab.dialog)

    speaker_idx_tav = d.get_speaker_slot_index(bg3.SPEAKER_PLAYER)

    pod_opening_first_node_uuid = 'd43c5da2-d8a5-ce3c-496d-928e17bd550b' # existing node
    pod_opening_second_node_uuid = '8ee32e1a-ddb6-ee34-5585-710c78c264e3' # existing node
    set_flag_node_uuid = '6a605691-dcdc-41fb-8380-089d2e0b7624'

    d.create_standard_dialog_node(
        set_flag_node_uuid,
        bg3.SPEAKER_PLAYER,
        [],
        None,
        end_node = True,
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_TUT_TransformChamber_State_FreedShadowheart, True, speaker_idx_tav),
            )),
        ))
    d.set_dialog_flags(pod_opening_first_node_uuid, setflags = (
        bg3.flag_group('Global', (
            bg3.flag(bg3.FLAG_ORI_Shadowheart_State_WolfDreamPoint_NautiloidSaved, True, None),
            bg3.flag(bg3.TUT_TransformChamber_State_DisableWard, True, None),
            bg3.flag(bg3.TUT_TransformChamber_State_EndPodDialogue, True, None),
        )),
    ))
    d.add_child_dialog_node(pod_opening_second_node_uuid, set_flag_node_uuid)
    d.remove_dialog_attribute(pod_opening_second_node_uuid, 'endnode')


def fix_act3_romance_conversation() -> None:
    game_assets = get_context().assets

    ab = game_assets.get_modded_dialog_asset_bundle('ShadowHeart_InParty')
    d = bg3.dialog_object(ab.dialog)

    post_sd_discussion_available_node_uuid = 'bc2cc2d6-a402-ded1-b206-85015005c19f'
    d.set_dialog_flags(post_sd_discussion_available_node_uuid, checkflags = (
        bg3.flag_group('Global', (
            bg3.flag(bg3.FLAG_NIGHT_Shadowheart_Skinnydipping, True, None),
            bg3.flag(bg3.FLAG_ORI_Shadowheart_State_PostSkinnyDipping_DiscussionAvailable, False, None),
            bg3.flag(bg3.FLAG_ORI_Shadowheart_State_PostSkinnydipping_Discussed, False, None),
            bg3.flag(bg3.FLAG_ORI_Shadowheart_State_AbortedSkinnydipping, False, None),
        )),
    ))

    post_nf_discussion_available_node_uuid = 'bdcd9103-6871-b539-1b9e-edf75baf22fb'
    d.set_dialog_flags(post_nf_discussion_available_node_uuid, checkflags = (
        bg3.flag_group('Global', (
            bg3.flag(bg3.FLAG_NIGHT_Shadowheart_NightfallRitual, True, None),
            bg3.flag(bg3.FLAG_ORI_Shadowheart_Event_PostNightfall_DiscussionAvailable, False, None),
            bg3.flag(bg3.FLAG_ORI_Shadowheart_State_PostNightfall_Discussed, False, None),
            bg3.flag(bg3.FLAG_ORI_Shadowheart_State_AbortedNightfall, False, None),
        )),
    ))

    aborted_nf_discussion_available_node_uuid = '64e3e9d2-e249-d00e-4923-4427f0b66d8b'
    d.set_dialog_flags(aborted_nf_discussion_available_node_uuid, setflags = (
        bg3.flag_group('Global', (
            bg3.flag(bg3.FLAG_Shadowheart_InParty_State_DiscussedAbortedNightfall, True, None),
            bg3.flag(bg3.FLAG_ORI_Shadowheart_State_PostNightfall_Discussed, True, None),
        )),
    ))


def fix_jaheira_greetings() -> None:
    game_assets = get_context().assets

    ################################################################################################
    # Dialog: Jaheira_InParty.lsf
    ################################################################################################

    ab = game_assets.get_modded_dialog_asset_bundle('Jaheira_InParty')
    d = bg3.dialog_object(ab.dialog)

    yes_1_node_uuid = '1571c212-ded1-c591-ac1a-c19507870ed2'
    #yes_2_node_uuid = 'c9604a6c-8891-cd7d-8a45-df5d258c8c6c'

    d.set_tagged_text(yes_1_node_uuid, bg3.text_content('ha20070e6gb6d1g4d97g87c5g8a71ea60ef13', 1))

    d.set_dialog_flags(
        yes_1_node_uuid,
        checkflags = (
            bg3.flag_group('Global', (
                bg3.flag(bg3.FLAG_GLO_Origin_PartOfTheTeam_Minsc, False, None),
                bg3.flag(bg3.FLAG_LOW_CountingHouse_State_RobbersEscaped, True, None),
                bg3.flag(bg3.FLAG_Jaheira_InParty_SpokeOfDoppelgangerJaheira, True, None),
                bg3.flag(bg3.FLAG_ORI_Jaheira_Event_FoundLinkToSewers, False, None),
            )),
        ))

    #d.remove_root_node(yes_2_node_uuid)


def patch_shadowheart_path_tags_in_dialog(dialog_name: str, patch_shar_path: bool, patch_selune_path: bool) -> None:
    game_assets = get_context().assets

    ab = game_assets.get_modded_dialog_asset_bundle(dialog_name)
    d = bg3.dialog_object(ab.dialog)

    try:
        speaker_idx_shadowheart = d.get_speaker_slot_index(bg3.SPEAKER_SHADOWHEART)
    except:
        # This is for Origin Shadowheart
        speaker_idx_shadowheart = d.get_speaker_slot_index(bg3.SPEAKER_PLAYER)

    if patch_shar_path:
        d.replace_text_tag(bg3.TAG_SHADOWHEART_SHARPATH, Really_Shar_Path.tag_uuid)
        d.replace_flags(
            'Tag',
            bg3.TAG_SHADOWHEART_SHARPATH,
            Really_Shar_Path.tag_uuid,
            speaker_override = speaker_idx_shadowheart)
    if patch_selune_path:
        d.replace_text_tag(bg3.TAG_SHADOWHEART_ENEMYOFSHARPATH, Really_Selune_Path.tag_uuid)
        d.replace_flags(
            'Tag',
            bg3.TAG_SHADOWHEART_ENEMYOFSHARPATH,
            Really_Selune_Path.tag_uuid,
            speaker_override = speaker_idx_shadowheart)


def patch_shadowheart_path_tags() -> None:
    game_assets = get_context().assets

    ################################################################################################
    # Late redemption path doesn't remove SHADOWHEART_SHARPATH tag from Shadowheart;
    # this causes lots of sharran reactions even though she turned away from Shar.
    # To fix that, I introduced new tags: Really_Shar_Path and Really_Selune_Path.
    # This procedure patches all the dialogs that refernce the original tags and
    # replaces the old tags with the new ones.
    ################################################################################################

    # SHARPATH
    ###################
    # PB_Shadowheart_Wyll_WaterQueen
    # PB_Shadowheart_Wyll_UpperTracks
    # PB_Shadowheart_Laezel_ROM_Act3

    # EPI_Epilogue_AD_WelcomeShadowheart
    # EPI_Epilogue_AD_Shadowheart_WineSupply
    # EPI_Epilogue_AD_IdleShadowheart
    # EPI_Epilogue_AD_GhostReactionShadowheart
    # LOW_StormshoreTabernacle_PAD_RespectsToMystra

    # ORI_Karlach_AvatarTransformsIntoMindflayer
    # Karlach_InPartyEND
    # Gale_IPRDs2
    # CAMP_Wyll_CRD_Act3Romance_ROM
    # CAMP_Shadowheart_CRD_DefeatedParents
    # WYR_DapperDrow_Intimacy
    # WYR_Circus_LoveDryad only SHADOWHEART_ENEMYOFSHARPATH_8eca8027-996c-4c61-bec6-77f853de295b
    # LOW_StormshoreTabernacle_GenericShrine
    # LOW_CazadorsPalace_Coffin errors in 531d6746-fc03-690e-e93e-ad79f032402b, 99b246ce-deee-9c97-04ef-0c1ee0e9ef56, 7f4cec18-7ecb-9edb-1cc9-12495a65eeff, 7e271cf3-b4a8-5108-6120-dfe0af743d18
    # EPI_Epilogue_Minsc
    # EPI_Epilogue_Halsin
    # EPI_Epilogue_GodGale
    # END_GameFinale_RomanceFates_Wyll
    # END_GameFinale_RomanceFates_Laezel
    # END_GameFinale_RomanceFates_Karlach
    # END_BrainBattle_CombatOver
    # END_BrainBattle_CombatOver_Nested_WhatNext

    # ENEMYOFSHARPATH
    ###################

    # PB_Shadowheart_Wyll_BhaalTemple
    # PB_Shadowheart_Wyll_AbandonedCistern
    # PB_Karlach_Shadowheart_BaldursMouth
    # PB_Jaheira_Shadowheart_WyrmSouth
    # PB_Jaheira_Shadowheart_MorphicPool

    # Jaheira_InParty_Nested_SecretScroll
    # LOW_StormshoreTabernacle_MystraShrine_OM_Gale_COM
    # LOW_StormshoreTabernacle_MystraShrine_OM_Gale_AOM_OOM
    # LOW_SharGrotto_FamiliarFace_OM_Shadowheart_AOM_OOM
    # WYR_KillDirectorGortash_Ceremony
    # EPI_Epilogue_Astarion_Lord
    # END_GameFinale_DeathofKarlach
    # END_BrainBattle_Intro
    # END_BrainBattle_CombatOver_Nested_AfterGithLeave

    # ORI_Shadowheart_PAD_WoundFlareUp
    # ORI_Shadowheart_PAD_SeluneReactivity_Misc
    # ORI_Shadowheart_PAD_SeluneReactivity_Item
    # ORI_Shadowheart_PAD_SeluneReactivity_Book
    # ORI_Shadowheart_PAD_SeluneReactivity_Altar

    dialogs_for_patching = {
        'Shadowheart_InParty': (True, True),
        'ShadowHeart_InPartyEND': (True, True),
        'Shadowheart_InParty_Nested_TopicalGreetings': (True, True),
        'ShadowHeart_InParty2_Nested_CityChapter': (True, True),
        'ShadowHeart_InParty2_Nested_DefaultChapter': (True, True),
        'ShadowHeart_InParty2_Nested_OriginChapter': (True, True),
        'Jaheira_InParty_Nested_SecretScroll': (True, True),
        'ORI_Karlach_AvatarTransformsIntoMindflayer': (True, True),
        'Karlach_InPartyEND': (True, True),
        'Gale_IPRDs2': (True, True),
        'CAMP_Wyll_CRD_Act3Romance_ROM': (True, True),
        'CAMP_Shadowheart_CRD_DefeatedParents': (True, True),
        'WYR_DapperDrow_Intimacy': (True, True),
        'WYR_Circus_LoveDryad': (False, True),
        'LOW_StormshoreTabernacle_GenericShrine': (True, True),
        'LOW_CazadorsPalace_Coffin': (True, True),
        'EPI_Epilogue_Minsc': (True, True),
        'EPI_Epilogue_Halsin': (True, True),
        'EPI_Epilogue_GodGale': (True, True),
        'END_GameFinale_RomanceFates_Wyll': (True, True),
        'END_GameFinale_RomanceFates_Laezel': (True, True),
        'END_GameFinale_RomanceFates_Karlach': (True, True),
        'END_BrainBattle_CombatOver': (True, True),
        'END_BrainBattle_CombatOver_Nested_WhatNext': (True, True),
        'LOW_StormshoreTabernacle_MystraShrine_OM_Gale_COM': (True, True),
        'LOW_StormshoreTabernacle_MystraShrine_OM_Gale_AOM_OOM': (True, True),
        'LOW_SharGrotto_FamiliarFace_OM_Shadowheart_AOM_OOM': (True, True),
        'LOW_SharGrotto_FamiliarFace_OM_Shadowheart_COM': (True, True),
        'WYR_KillDirectorGortash_Ceremony': (True, True),
        'EPI_Epilogue_Astarion_Lord': (True, True),
        'END_GameFinale_DeathofKarlach': (True, True),
        'END_BrainBattle_Intro': (True, True),
        'END_BrainBattle_CombatOver_Nested_AfterGithLeave': (True, True),
        'PB_Shadowheart_Wyll_BhaalTemple': (True, True),
        'PB_Shadowheart_Wyll_AbandonedCistern': (True, True),
        'PB_Karlach_Shadowheart_BaldursMouth': (True, True),
        'PB_Jaheira_Shadowheart_WyrmSouth': (True, True),
        'PB_Jaheira_Shadowheart_MorphicPool': (True, True),
        'PB_Shadowheart_Wyll_WaterQueen': (True, True),
        'PB_Shadowheart_Wyll_UpperTracks': (True, True),
        'PB_Shadowheart_Laezel_ROM_Act3': (True, True),
        'EPI_Epilogue_AD_WelcomeShadowheart': (True, True),
        'EPI_Epilogue_AD_Shadowheart_WineSupply': (True, True),
        'EPI_Epilogue_AD_IdleShadowheart': (True, True),
        'EPI_Epilogue_AD_GhostReactionShadowheart': (True, True),
        'LOW_StormshoreTabernacle_PAD_RespectsToMystra': (True, True),
        'ORI_Shadowheart_PAD_WoundFlareUp': (True, True),
        'ORI_Shadowheart_PAD_SeluneReactivity_Misc': (True, True),
        'ORI_Shadowheart_PAD_SeluneReactivity_Item': (True, True),
        'ORI_Shadowheart_PAD_SeluneReactivity_Book': (True, True),
        'ORI_Shadowheart_PAD_SeluneReactivity_Altar': (True, True),
    }

    for dialog_name, patch_flags in dialogs_for_patching.items():
        patch_shar_path, patch_selune_path = patch_flags
        patch_shadowheart_path_tags_in_dialog(dialog_name, patch_shar_path, patch_selune_path)

    ################################################################################################
    # Dialog: Jaheira_InParty_Nested_SecretScroll.lsf
    # Fix: the Shadowheart's tag is checked on the player
    ################################################################################################

    ab = game_assets.get_modded_dialog_asset_bundle('Jaheira_InParty_Nested_SecretScroll')
    d = bg3.dialog_object(ab.dialog)

    speaker_idx_shadowheart = d.get_speaker_slot_index(bg3.SPEAKER_SHADOWHEART)

    # And use it to do more than fight, I'd hope. Shar and SelÃ»ne have already claimed more than their share of your years, I think.
    # Perhaps. But if the darkness is really going to swallow everything, as you Sharrans say, it should at least have to work for its supper.
    node = d.find_dialog_node('b81a2a84-5212-40b6-8868-b20eaa9ab3e9')
    rules = node.findall('./children/node[@id="TaggedTexts"]/children/node[@id="TaggedText"]/children/node[@id="RuleGroup"]/children/node[@id="Rules"]/children/node[@id="Rule"]')
    for rule in rules:
        tags = rule.findall('./children/node[@id="Tags"]/children/node[@id="Tag"]')
        tags_uuids = {bg3.get_bg3_attribute(tag, 'Object') for tag in tags}
        if Really_Selune_Path.tag_uuid in tags_uuids:
            bg3.set_bg3_attribute(rule, 'speaker', speaker_idx_shadowheart)

    ################################################################################################
    # Dialog: Shadowheart_InParty2_Nested_DefaultChapter
    # Fix: Do you think perhaps another Nightfall ceremony is out of the question...?
    ################################################################################################

    ab = game_assets.get_modded_dialog_asset_bundle('Shadowheart_InParty2_Nested_DefaultChapter')
    d = bg3.dialog_object(ab.dialog)

    speaker_idx_shadowheart = d.get_speaker_slot_index(bg3.SPEAKER_SHADOWHEART)

    d.set_dialog_flags('a4730914-1ba8-412f-a5d9-0580648846bb', checkflags = (
        bg3.flag_group('Global', (
            bg3.flag(bg3.FLAG_NIGHT_Shadowheart_NightfallRitual, True, None),
        )),
        bg3.flag_group('Tag', (
            bg3.flag(Really_Shar_Path.tag_uuid, True, speaker_idx_shadowheart),
        )),
    ))

    ################################################################################################
    # Dialog: ShadowHeart_InPartyEND
    # Fix: ...I don't think Lady Shar would approve of a mind flayer leading her flock.
    ################################################################################################

    ab = game_assets.get_modded_dialog_asset_bundle('ShadowHeart_InPartyEND')
    d = bg3.dialog_object(ab.dialog)

    speaker_idx_shadowheart = d.get_speaker_slot_index(bg3.SPEAKER_SHADOWHEART)
    speaker_idx_tav = d.get_speaker_slot_index(bg3.SPEAKER_PLAYER)

    # I'd offer to take the plunge, but, well... somehow, I don't think Lady Shar would approve of a mind flayer leading her flock.
    d.set_dialog_flags('8af10cef-82c6-4982-98e1-b90b6849fd0f', checkflags = (
        bg3.flag_group('Global', (
            bg3.flag(Shadowheart_Turned_Away_From_Shar.uuid, False, None),
        )),
    ))

    ################################################################################################
    # Dialog: Minthara_InParty_Nested_PartyMemberThoughts
    # Fix: It would have been better for us had she embraced Shar, and claimed the power of the goddess.
    ################################################################################################

    ab = game_assets.get_modded_dialog_asset_bundle('Minthara_InParty_Nested_PartyMemberThoughts')
    d = bg3.dialog_object(ab.dialog)

    speaker_idx_tav = d.get_speaker_slot_index(bg3.SPEAKER_PLAYER)

    d.set_dialog_flags('bce95bf5-84ab-4530-9f38-17c02501ba5c', checkflags = (
        bg3.flag_group('Global', (
            bg3.flag(Shadowheart_Turned_Away_From_Shar.uuid, True, None),
        )),
    ))
    # The following creates two 'question' nodes:
    # one is when Tav is not a sharran but Shadowheart is a sharran yet
    # another one is when Tav is sharran but Shadowheart is no longer a sharran
    d.set_dialog_flags('6592ec65-2474-410f-b438-8d6b473e6a1c', checkflags = (
        bg3.flag_group('Global', (
            bg3.flag(Shadowheart_Turned_Away_From_Shar.uuid, False, None),
        )),
        bg3.flag_group('Tag', (
            bg3.flag(bg3.GOD_SHAR, False, speaker_idx_tav),
        ))
    ))
    # I agree - she worships the wrong god.
    d.create_standard_dialog_node(
        '33fc2a70-2252-4cef-9837-6627a0bcaf31',
        bg3.SPEAKER_PLAYER,
        ['64b9711f-feb2-439a-a726-f72d2380da6d'],
        bg3.text_content('h387da20cg362dg4b98gba10g680cc8c1984b', 1),
        constructor = bg3.dialog_object.QUESTION,
        checkflags = (
            bg3.flag_group('Global', (
                bg3.flag(Shadowheart_Turned_Away_From_Shar.uuid, True, None),
            )),
            bg3.flag_group('Tag', (
                bg3.flag(bg3.GOD_SHAR, True, speaker_idx_tav),
            ))
        ))
    d.add_child_dialog_node('a566bbc2-e093-4926-9b6c-ab1a5e53fcde', '33fc2a70-2252-4cef-9837-6627a0bcaf31', 0)

    ################################################################################################
    # Dialog: EPI_Epilogue_Minsc
    # Fix: Shadowheart, foul Sharran. Trust no woman who makes an enemy of the moon.
    ################################################################################################

    ab = game_assets.get_modded_dialog_asset_bundle('EPI_Epilogue_Minsc')
    d = bg3.dialog_object(ab.dialog)

    speaker_idx_player = d.get_speaker_slot_index(bg3.SPEAKER_PLAYER)


    # Shadowheart! Two gods tugged at her soul, but she managed to keep it for all herself in the end. Wait, Boo - did she do something with her hair...?
    d.set_dialog_flags('321fcb71-3611-10b6-00a1-4527ef1b1215', checkflags = (
        bg3.flag_group('Global', (
            bg3.flag(Shadowheart_Turned_Away_From_Shar.uuid, True, None),
            bg3.flag(bg3.FLAG_EPI_Epilogue_State_ShadowheartPresent, True, None),
        )),
        bg3.flag_group('Tag', (
            bg3.flag(bg3.TAG_REALLY_SHADOWHEART, False, speaker_idx_player),
        )),
    ))

    # Shadowheart, foul Sharran. Trust no woman who makes an enemy of the moon.
    d.set_dialog_flags('fb5df842-4494-9dbb-68bb-60c5cf26f59f', checkflags = (
        bg3.flag_group('Global', (
            bg3.flag(Shadowheart_Turned_Away_From_Shar.uuid, False, None),
            bg3.flag(bg3.FLAG_EPI_Epilogue_State_ShadowheartPresent, True, None),
        )),
        bg3.flag_group('Tag', (
            bg3.flag(bg3.TAG_REALLY_SHADOWHEART, False, speaker_idx_player),
        )),
    ))

    ################################################################################################
    # Dialog: END_BrainBattle_FinalDecision_Nested_EvilDurge
    # Fix: I... I'm coming to you, Lady Shar. Embrace me.
    ################################################################################################

    ab = game_assets.get_modded_dialog_asset_bundle('END_BrainBattle_FinalDecision_Nested_EvilDurge')
    d = bg3.dialog_object(ab.dialog)

    # I... I'm coming to you, Lady Shar. Embrace me.
    d.set_dialog_flags(
        'c5340dd2-0571-7c94-18e6-5eff6bc1545e',
        checkflags = (
            bg3.flag_group('Global', (
                bg3.flag(Shadowheart_Turned_Away_From_Shar.uuid, False, None),
            )),
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_State_PartneredWithShadowheart, True, 1),
            )),
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_REALLY_SHADOWHEART, True, 15),
            ))),
        setflags = (
            bg3.flag_group('Object', (
                # END_General_State_InclusionExcluded_98c42fdb-7511-72c1-3861-a9232a4c40f7
                bg3.flag('98c42fdb-7511-72c1-3861-a9232a4c40f7', True, 15),
            )),
        ))

    ################################################################################################
    # Dialog: EPI_Epilogue_FinalToast
    # Fix: To finding what was lost.
    ################################################################################################

    ab = game_assets.get_modded_dialog_asset_bundle('EPI_Epilogue_FinalToast')
    d = bg3.dialog_object(ab.dialog)

    # To finding what was lost.
    d.set_dialog_flags('fc77e312-79a2-ed4f-9bfb-3039764daae2', checkflags = (
        bg3.flag_group('Global', (
            bg3.flag(Shadowheart_Turned_Away_From_Shar.uuid, True, None),
        )),
        bg3.flag_group('Tag', (
            bg3.flag(bg3.TAG_REALLY_SHADOWHEART, True, 1),
        )),
    ))

    # To all those we lost on the way.
    d.set_dialog_flags('2a07f5d5-6601-1eac-c421-7841f74c612a', checkflags = (
        bg3.flag_group('Global', (
            bg3.flag(Shadowheart_Turned_Away_From_Shar.uuid, False, None),
        )),
        bg3.flag_group('Tag', (
            bg3.flag(bg3.TAG_REALLY_SHADOWHEART, True, 1),
        )),
    ))


bg3.add_build_procedure('fix_nightsong_fate_dialog', fix_nightsong_fate_dialog)
bg3.add_build_procedure('patch_nightsong_fate_dialog', patch_nightsong_fate_dialog)
bg3.add_build_procedure('fix_skinny_dipping_crd', fix_skinny_dipping_crd)
bg3.add_build_procedure('fix_waterfall_date_invitation', fix_waterfall_date_invitation)
bg3.add_build_procedure('fix_now_and_always_thorm_mausoleum', fix_now_and_always_thorm_mausoleum)
bg3.add_build_procedure('fix_lolth_sworn_drow', fix_lolth_sworn_drow)
bg3.add_build_procedure('fix_all_that_happened_raider_victory', fix_all_that_happened_raider_victory)
bg3.add_build_procedure('fix_topical_greetings', fix_topical_greetings)
bg3.add_build_procedure('fix_shadowheart_pod_opening_scene', fix_shadowheart_pod_opening_scene)
bg3.add_build_procedure('fix_act3_romance_conversation', fix_act3_romance_conversation)
bg3.add_build_procedure('fix_jaheira_greetings', fix_jaheira_greetings)
bg3.add_build_procedure('patch_shadowheart_path_tags', patch_shadowheart_path_tags)
bg3.add_build_procedure('fix_nightsong_meeting', fix_nightsong_meeting)

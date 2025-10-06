from __future__ import annotations

import bg3moddinglib as bg3

from .context import game_assets
from .flags import *

def fix_nightsong_choice_dialog() -> None:
    ################################################################################################
    # Dialog: SHA_NightsongsFate_OM_Shadowheart_AOM_OOM_COM.lsf
    # Fix the Nightsong decision choice: if Tav accumulated enough Nightsong points and
    # the approval is 20+, Shadowheart doesn't need to be persuaded into sparing her.
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

    d.create_alias_dialog_node(
        alias_she_knows_something_about_you_node_uuid,
        roll_she_knows_something_about_you_node_uuid,
        d.get_children_nodes_uuids(roll_she_knows_something_about_you_node_uuid),
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_Approval_AtLeast_40_For_Sp3, False, speaker_idx_shadowheart),
            )),
        ))

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
    'fe4e2f3c-30f6-84b2-fbdd-bda36f6dbc71'


def fix_skinny_dipping_crd() -> None:
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
    ################################################################################################
    # Dialog: ShadowHeart_InParty2_Nested_ShadowCurseChapter.lsf
    # At the entrance of the Thorm mausoleum, when Tav & Shadowheart return from the Shadowfell,
    # Tav should not be able to tell her "You're not alone. You have me." if they are in
    # exclusive relationship with someone else.
    ################################################################################################

#    d = bg3.dialog_object(files.get_file('Gustav', 'Mods/GustavDev/Story/DialogsBinary/Companions/ShadowHeart_InParty2_Nested_ShadowCurseChapter.lsf'))

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
    # d = bg3.dialog_object(files.get_file('Gustav', 'Mods/GustavDev/Story/DialogsBinary/Companions/ShadowHeart_InParty2_Nested_SharranChapter.lsf'))

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
    ab = game_assets.get_modded_dialog_asset_bundle('Shadowheart_InParty_Nested_TopicalGreetings')
    d = bg3.dialog_object(ab.dialog)

    speaker_idx_shadowheart = d.get_speaker_slot_index(bg3.SPEAKER_SHADOWHEART)

    # remove Shadowheart_InParty_State_EndDialog_83c61046-f6c7-4d0b-a012-37fdce36d957
    # keep only TG_ORI_Astarion_KidnappedByGurHunter_d2df26ef-545e-43c4-99e1-cfe0f4e1ac06
    d.set_dialog_flags('2bda6e84-9c72-43ed-b2a3-f53fed3c431a', setflags = (
        bg3.flag_group('Object', (
            bg3.flag('d2df26ef-545e-43c4-99e1-cfe0f4e1ac06', False, speaker_idx_shadowheart),
        )),
    ))


def fix_shadowheart_pod_opening_scene() -> None:
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


bg3.add_build_procedure('fix_nightsong_choice_dialog', fix_nightsong_choice_dialog)
bg3.add_build_procedure('fix_skinny_dipping_crd', fix_skinny_dipping_crd)
bg3.add_build_procedure('fix_waterfall_date_invitation', fix_waterfall_date_invitation)
bg3.add_build_procedure('fix_now_and_always_thorm_mausoleum', fix_now_and_always_thorm_mausoleum)
bg3.add_build_procedure('fix_lolth_sworn_drow', fix_lolth_sworn_drow)
bg3.add_build_procedure('fix_all_that_happened_raider_victory', fix_all_that_happened_raider_victory)
bg3.add_build_procedure('fix_topical_greetings', fix_topical_greetings)
bg3.add_build_procedure('fix_shadowheart_pod_opening_scene', fix_shadowheart_pod_opening_scene)
bg3.add_build_procedure('fix_act3_romance_conversation', fix_act3_romance_conversation)
bg3.add_build_procedure('fix_jaheira_greetings', fix_jaheira_greetings)
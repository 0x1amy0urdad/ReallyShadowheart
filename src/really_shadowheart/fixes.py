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


def patch_shadowheart_path_tags_in_dialog(dialog_name: str, patch_shar_path: bool, patch_selune_path: bool) -> None:
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
    # Dialog: Shadowheart_InParty_Nested_TopicalGreetings.lsf
    ################################################################################################

    # 937f0b41-7f51-3e01-fa3b-34cf8ec155e9
    # Lady Shar's power will soon fade from these lands, but it is a price that had to be paid, so that the traitor Ketheric Thorm could face justice at last.
    # The shadows are losing their grip on these lands - Shar can indeed be thwarted. Comforting to know.

    # 812d420d-f84a-0114-f92a-9551af1bbd23
    # So, you're free from your hunger, free from any lingering fear of the sun... but all those lives you sacrificed, Astarion. I'm not sure I'll forget their final screams any time soon.
    # 'Vampire Ascendant'. A fine prize, Astarion, paid for with a sea of blood. I'm glad to know I have an ally who understands the value of sacrifice - congratulations.

    # 23387c5a-03fb-1952-9a47-538886f537ef
    # Jaheira's adept at keeping secrets - and for good reason. She was wise to try and keep her family safe... I just wish I could've done the same.
    # Jaheira's adept at keeping secrets - to conceal a family is no mean feat. Perhaps her skills lean more towards the Dark Lady than she realises...

    # 4c65dd02-f2a6-ba42-6f43-a5695ff29431
    # Be careful, consuming shadow magic. The darkness tends to take more than it gives. I would know.
    # You couldn't resist the allure of the shadows, Gale? I don't blame you - it's the only power that truly counts.

    # 58851469-2818-dce7-6339-ff63524ba1b4
    # A goddess abandoning you needn't be the end, Gale. Trust me, I know.
    # I'm sorry, Gale. To be abandoned by your goddess... I cannot imagine how that must feel. May the Dark Lady comfort you.

    # c01040e4-ee7a-77c8-f676-dcc71bc24b51
    # Shar's power still grips this land. A shame we could not banish it - it would have felt good to spite her.
    # This land remains cloaked by Lady Shar's power - good. A shame it cost us Halsin as a travelling companion though. He may have been misguided, but I liked looking at him.

    # 5199a136-f3d9-8135-56b8-a066e302b9ac
    # Karlach has offered to take on the duty. She doesn't have much time left, so there's a certain logic in leaving this to her. A somewhat callous logic, mind you.
    # Karlach has offered to take on the duty. She doesn't have much time left, so there's a certain logic in leaving this to her. The Dark Lady would approve, I'm sure.

    # 45de2fe4-d193-2fd2-4d02-a6e699c77d2c
    # It seems you have made up with Mystra, Gale. Congratulations - though I don't see any such reconciliation between myself and Shar any time soon...
    # It seems you have made up with Mystra, Gale. Congratulations. Lady Shar has no love for your goddess... but I am glad you have someone to turn to.

    # 224a654e-57f1-e17a-0f3b-a6df1d9a2a17
    # I'm sorry, Gale. You tried. Mystra was wrong to turn on you, no matter what mistakes you made in the past.
    # Mystra was never worthy of your devotion, Gale. She will rue the day she turned on you, I am sure.

    # 1b497a37-45bb-541c-25eb-6da065b835a3
    # It seems Gale has made amends with Mystra. Good for him - though I don't see any such reconciliation between myself and Shar any time soon...
    # It seems Gale has made amends with Mystra. Good for him - though his choice of goddesses leaves something to be desired...

    # abb342d5-a0fd-356c-e450-d874bfef0b82
    # Defying a goddess, Gale? Well, they do say imitation is a form of flattery. I just hope you know what you're doing.
    # Defying a goddess, Gale? Bold, but Mystra was never worthy of your love.

    # 0213dd07-7f84-9367-c37c-13d71330ebc0
    # Mystra has forsaken Gale entirely. A crushing blow... but he is strong enough to persevere, I think.
    # Mystra has forsaken Gale entirely. Imagine how he must be feeling... I doubt I could go on, if Lady Shar turned on me.

    # 82b19bf3-e349-ec87-6b0a-01336865b6c7
    # Gale defied Mystra herself. Good - not every goddess is deserving of such love. I would know.
    # Gale defied Mystra herself. I hope he does not come to regret it.

    # 56aff281-4118-4ffd-a07c-f2b74e3e2305
    # It seems Viconia sought a greater purpose than Lady Shar had decided for her.
    # Shar did not come to Viconia's defence. All who bow to her are disposable pawns, in the end.

    # e998d502-080b-3bae-0868-fe7dd0a83377
    # I thought perhaps you'd be tempted to seize Cazador's prize in his stead... but you didn't. Perhaps that makes you the better man - I'm sure all those people you spared would agree.
    # I thought perhaps you'd be tempted to seize Cazador's prize in his stead... but you didn't. Pity - a vampire lord would have been a fine ally... but no matter. It's done.

    # 9fee8202-3a05-9838-62eb-59c6e3cd0d5b
    # You sacrificed your own father, Wyll? Not a step that many could take, but the Nightsinger would appreciate your resolve, I think.
    # You... you sacrificed your own father? I hope freedom from the pact was worth it.

    # 661ad9fd-918b-0198-3e42-4e1a114fe6a3
    # Your father won't be around forever, Wyll. But the pact? That's a different matter. I hope you won't live to regret being sentimental.
    # It can't have been easy, to resign yourself to keeping the pact. But I'm glad you choose your father.

    # c0433db6-5425-424f-98e1-3d187ff4ffb1
    # Tag SHADOWHEART_SHARPATH_9624a3fe-bb9e-47c5-b9ab-417e6da6f84b

    # d77be7c6-00af-4463-a091-d7e19eb84fd6
    # Tag SHADOWHEART_SHARPATH_9624a3fe-bb9e-47c5-b9ab-417e6da6f84b

    ################################################################################################
    # Dialog: Jaheira_InParty_Nested_SecretScroll.lsf
    ################################################################################################

    # Selune path:
    # Shadowheart line
    # I wallowed in darkness for too long. If I could extend the time I have left in the light, I think I'd take it.
    # h07e1eddbgd749g4be9ga9e1g3dc1312bb101
    # TLVoice c2fec939-7511-4080-92f9-9030b936e795
    # timeline phase 16
    #
    # Jaheira line
    # And use it to do more than fight, I'd hope. Shar and Selune have already claimed more than their share of your years, I think.
    # h14df7cd7g6f36g45b9gb6a9g9af1e390ffa9
    # TLVoice b81a2a84-5212-40b6-8868-b20eaa9ab3e9
    # timeline phase 7

    # Shar path:
    # Shadowheart line
    # The darkness will prevail in the end, Jaheira. You're clinging on just to wage an unwinnable war.
    # h236a244ag72b5g49d1gb05bgae38ecdd9cb8
    # TLVoice a7e12ba8-5003-4958-8572-e0acfd2355cb
    # timeline phase 60
    #
    # Jaheira line
    # Perhaps. But if the darkness is really going to swallow everything, as you Sharrans say, it should at least have to work for its supper.
    # h58de1cd4g10b2g43bbg962fg6f2253c92286
    # 



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
bg3.add_build_procedure('patch_shadowheart_path_tags', patch_shadowheart_path_tags)

from __future__ import annotations

import bg3moddinglib as bg3

from .context import game_assets
from .flags import *

########################################################################################
# Minthara about copmpanions
########################################################################################

def patch_minthara_conversations() -> None:
    ########################################################################################
    # Minthara_InParty.lsf
    ########################################################################################
    # d = bg3.dialog_object(files.get_file('Gustav', 'Mods/GustavDev/Story/DialogsBinary/Companions/Minthara_InParty.lsf'))

    ab = game_assets.get_modded_dialog_asset_bundle('Minthara_InParty')
    d = bg3.dialog_object(ab.dialog)

    # I'm curious to hear your thoughts about our companions.
    d.remove_dialog_attribute('9b0f15eb-4dfd-011a-964f-b9b8c4c596d5', 'ShowOnce')
    d.set_dialog_flags('9b0f15eb-4dfd-011a-964f-b9b8c4c596d5', checkflags = (
        bg3.flag_group('Global', (
            bg3.flag(bg3.FLAG_GEN_SoloPlayer, False, None),
        )),
    ))


    ########################################################################################
    # Minthara_InParty_Nested_PartyMemberThoughts.lsf
    ########################################################################################
    # d = bg3.dialog_object(files.get_file('Gustav', 'Mods/GustavDev/Story/DialogsBinary/Companions/Minthara_InParty_Nested_PartyMemberThoughts.lsf'))

    ab = game_assets.get_modded_dialog_asset_bundle('Minthara_InParty_Nested_PartyMemberThoughts')
    d = bg3.dialog_object(ab.dialog)

    # I'm curious to hear what you think of Shadowheart.
    d.remove_dialog_attribute('c390d470-6d3d-4605-bf2b-03a75e72ca1c', 'ShowOnce')
    d.set_dialog_flags('c390d470-6d3d-4605-bf2b-03a75e72ca1c', setflags = (), checkflags = (
        bg3.flag_group('Global', (
            bg3.flag(bg3.FLAG_GLO_Origin_Avatar_Shadowheart, False, None),
            bg3.flag(bg3.FLAG_GLO_Origin_PartOfTheTeam_Shadowheart, True, None),
        )),
    ))

    # How do you and Lae'zel get along?
    d.remove_dialog_attribute('d96b1c54-8903-4eac-9976-b44b8984aad3', 'ShowOnce')
    d.set_dialog_flags('d96b1c54-8903-4eac-9976-b44b8984aad3', setflags = (), checkflags = (
        bg3.flag_group('Global', (
            bg3.flag(bg3.FLAG_GLO_Origin_Avatar_Laezel, False, None),
            bg3.flag(bg3.FLAG_GLO_Origin_PartOfTheTeam_Laezel, True, None),
        )),
    ))

    # What do you make of Astarion?
    d.remove_dialog_attribute('ff494699-3d8a-4333-a709-27f6b3796dfc', 'ShowOnce')
    d.set_dialog_flags('ff494699-3d8a-4333-a709-27f6b3796dfc', setflags = (), checkflags = (
        bg3.flag_group('Global', (
            bg3.flag(bg3.FLAG_GLO_Origin_Avatar_Astarion, False, None),
            bg3.flag(bg3.FLAG_GLO_Origin_PartOfTheTeam_Astarion, True, None),
            bg3.flag(bg3.FLAG_ORI_Astarion_State_StayedVampireSpawn, False, None),
            bg3.flag(bg3.FLAG_ORI_Astarion_State_BecameVampireLord, False, None),
        )),
    ))


    # Have you spent much time with Gale?
    d.remove_dialog_attribute('03bdf98e-ab18-4452-b88a-6921f0755ff1', 'ShowOnce')
    d.set_dialog_flags('03bdf98e-ab18-4452-b88a-6921f0755ff1', setflags = (), checkflags = (
        bg3.flag_group('Global', (
            bg3.flag(bg3.FLAG_GLO_Origin_Avatar_Gale, False, None),
            bg3.flag(bg3.FLAG_GLO_Origin_PartOfTheTeam_Gale, True, None),
            bg3.flag(bg3.FLAG_ORI_Gale_Event_BombDisarmed, True, None),
        )),
    ))

    # Any thoughts on Wyll?
    d.remove_dialog_attribute('62ca8389-3502-4c56-8164-4130eafcb737', 'ShowOnce')
    d.set_dialog_flags('62ca8389-3502-4c56-8164-4130eafcb737', setflags = (), checkflags = (
        bg3.flag_group('Global', (
            bg3.flag(bg3.FLAG_GLO_Origin_Avatar_Wyll, False, None),
            bg3.flag(bg3.FLAG_GLO_Origin_PartOfTheTeam_Wyll, True, None),
            bg3.flag(bg3.FLAG_CAMP_MizorasPact_State_WyllReleasedFromPact, False, None),
            bg3.flag(bg3.FLAG_GLO_Wyll_State_GrandDuke, False, None),
            bg3.flag(bg3.FLAG_CAMP_MizorasPact_State_WyllEternalPact, False, None),
            bg3.flag(bg3.FLAG_GLO_Wyll_State_BladeOfFrontiers, False, None),
            bg3.flag(bg3.FLAG_GLO_Wyll_State_BladeOfAvernus, False, None),
        )),
    ))


    # You and Karlach seem to be friendly.
    d.remove_dialog_attribute('ad478103-114e-4250-8afa-05141b3627fc', 'ShowOnce')
    d.set_dialog_flags('ad478103-114e-4250-8afa-05141b3627fc', setflags = (), checkflags = (
        bg3.flag_group('Global', (
            bg3.flag(bg3.FLAG_GLO_Origin_Avatar_Karlach, False, None),
            bg3.flag(bg3.FLAG_GLO_Origin_PartOfTheTeam_Karlach, True, None),
        )),
    ))

    # What do you make of Jaheira?
    d.remove_dialog_attribute('4d323bd3-8403-4246-ae83-0db89ab5689b', 'ShowOnce')
    d.set_dialog_flags('4d323bd3-8403-4246-ae83-0db89ab5689b', setflags = (), checkflags = (
        bg3.flag_group('Global', (
            bg3.flag(bg3.FLAG_GLO_Jaheira_State_PermaDefeated, False, None),
            bg3.flag(bg3.FLAG_GLO_Origin_PartOfTheTeam_Jaheira, True, None),
        )),
    ))

    # You and Minsc are unusual allies.
    d.remove_dialog_attribute('3e3e6869-d30a-4bf9-831c-54847a77dfdc', 'ShowOnce')
    d.set_dialog_flags('3e3e6869-d30a-4bf9-831c-54847a77dfdc', setflags = (), checkflags = (
        bg3.flag_group('Global', (
            bg3.flag(bg3.FLAG_GLO_Origin_PartOfTheTeam_Minsc, True, None),
        )),
    ))

    # Leave
    d.remove_dialog_attribute('aad7d24d-8576-40d0-93ac-73d045054069', 'ShowOnce')


def patch_minthara_creep_confrontation() -> None:
    ab = game_assets.get_modded_dialog_asset_bundle('CAMP_Halsin_Minthara_CFM_Confrontation')
    d = bg3.dialog_object(ab.dialog)
    t = bg3.timeline_object(ab.timeline, d)

    speaker_idx_creep = d.get_speaker_slot_index(bg3.SPEAKER_HALSIN)
    speaker_idx_minthy = d.get_speaker_slot_index(bg3.SPEAKER_MINTHARA)
    speaker_idx_tav = d.get_speaker_slot_index(bg3.SPEAKER_PLAYER)

    # Add flags to nodes where the creep leaves the party
    creep_is_leaving_nodes_uuids = [
        'bbdf05f6-0711-4512-b0cb-6b8e02a8aa03',
        '40d0640f-10e4-4004-8542-747579379470',
        'ad6b012c-80f0-bda6-0731-a8b4befc5e3e',
    ]
    for node_uuid in creep_is_leaving_nodes_uuids:
        d.set_dialog_flags(node_uuid, setflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_Companion_Leaves_Party, True, speaker_idx_creep),
                bg3.flag(Creep_Ran_Away.uuid, True, speaker_idx_tav)
            )),
        ))

    # Add flag to "I'm sorry, Minthara, but you need to leave."
    d.set_dialog_flags('bbfde148-a8f1-b805-8b62-0b8418085218', setflags = (
        bg3.flag_group('Object', (
            bg3.flag(bg3.FLAG_Companion_Leaves_Party, True, speaker_idx_minthy),
        )),
    ))
    # Remove "Not my problem. You're on your own."
    d.delete_child_dialog_node('d1fe4725-c998-2ea8-243c-9d521a199970', '6f1a6e8a-8918-3b71-66da-457c465c402d')

    if_i_leave_i_die_node_uuid = '928f2e6f-ed26-44a4-8a0b-698b73a53c9a' # existing node
    ultimatum_node_uuid = '2b13ab60-51ac-527f-671c-c3ccd52d79c2' # existing node

    tame_yourself_node_uuid = '61f0e9e3-575f-4508-831f-818df4d7d201'
    redemption_path_node_uuid = 'a19a9d46-95c1-4cc8-ac7e-5915cee92a46'
    carry_more_resentment_node_uuid = 'a0df361d-20f8-41fd-a0df-24e571cd953a'
    i_am_lucky_to_have_your_counsel_node_uuid = '19039834-21e0-45f2-85ef-0c33229331b5'

    d.add_child_dialog_node(ultimatum_node_uuid, tame_yourself_node_uuid, 0)
    d.add_child_dialog_node(ultimatum_node_uuid, redemption_path_node_uuid, 0)

    # Halsin, tame yourself. Nobody's leaving. You know what's at stake, and you will stop this quarrel.
    d.create_roll_dialog_node(
        tame_yourself_node_uuid,
        bg3.SPEAKER_PLAYER,
        bg3.SPEAKER_HALSIN,
        bg3.dialog_object.ABILITY_CHARISMA,
        bg3.dialog_object.SKILL_PERSUASION,
        bg3.Act2_Challenging,
        carry_more_resentment_node_uuid,
        if_i_leave_i_die_node_uuid,
        bg3.text_content('hce7c0c72g0207g48d2g95eag63d16b3433c7', 1))

    # Halsin, I read your diary in the grove. You redeemed yourself and lifted the curse. Stop the quarrel and help Minthara on her path to redemption.
    d.create_roll_dialog_node(
        redemption_path_node_uuid,
        bg3.SPEAKER_PLAYER,
        bg3.SPEAKER_HALSIN,
        bg3.dialog_object.ABILITY_WISDOM,
        bg3.dialog_object.SKILL_HISTORY,
        bg3.Act2_Medium,
        carry_more_resentment_node_uuid,
        if_i_leave_i_die_node_uuid,
        bg3.text_content('h46e2124fg95f5g4f56g810dg050666a9693c', 1),
        advantage = 1,
        advantage_reason = 'h2a032d7dg3c4eg42f1g91dfg7e1d157cbc7a',
        checkflags = (
            bg3.flag_group('Global', (
                bg3.flag(bg3.DEN_DruidLair_Knows_SharDagger, True, None),
            )),
        ))

    # Indeed... perhaps I carry more resentment than I realise.
    d.create_standard_dialog_node(
        carry_more_resentment_node_uuid,
        bg3.SPEAKER_HALSIN,
        [i_am_lucky_to_have_your_counsel_node_uuid],
        bg3.text_content('h39b66ad3gc20bg4bb2g98a6g76a2a377b770', 1))
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_HALSIN,
        '5.6',
        carry_more_resentment_node_uuid,
        ((None, 'bfaff89d-a5fa-4191-b928-c255af604c24'),),
        phase_duration = '6.0',
        emotions = {
            bg3.SPEAKER_HALSIN: ((0.0, 4, None), (1.25, 4, 2), (2.5, 16, None), (4.55, 32, None)),
        })

    # I am lucky to have your counsel. It was sorely needed.
    d.create_standard_dialog_node(
        i_am_lucky_to_have_your_counsel_node_uuid,
        bg3.SPEAKER_HALSIN,
        [],
        bg3.text_content('h8ea36684g4d49g402fg9b7cgf1e4c9feb7e2', 1),
        end_node = True)
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_HALSIN,
        '6.79',
        i_am_lucky_to_have_your_counsel_node_uuid,
        ((None, '6b7bd606-5eea-4cfe-90ce-19d8331d4573'),),
        phase_duration = '7.2',
        emotions = {
            bg3.SPEAKER_HALSIN: ((0.78, 32, None), (5.14, 64, 2), (6.34, 32, None),),
        })


bg3.add_build_procedure('patch_minthara_conversations', patch_minthara_conversations)
bg3.add_build_procedure('patch_minthara_creep_confrontation', patch_minthara_creep_confrontation)

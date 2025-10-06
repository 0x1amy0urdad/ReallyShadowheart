from __future__ import annotations

import bg3moddinglib as bg3

from .context import game_assets
from .flags import *

################################################################################################
# Shadowheart's greetings
################################################################################################
sleep_together_entry_point_node_uuid = '80ad286d-cf0a-4737-9261-3b4a8e6ee797'
existing_partnered_greetings_node_uuid = '4c2f28c3-4a1b-370a-73f8-d2bfcea53e9d' # existing node

def create_greetings() -> None:
    ############################################################################################
    # Dialog: ShadowHeart_InParty2.lsf
    ############################################################################################

    # d = bg3.dialog_object(files.get_file('Gustav', 'Mods/GustavDev/Story/DialogsBinary/Companions/ShadowHeart_InParty2.lsf'))
    # t = bg3.timeline_object(files.get_file('Gustav', 'Public/GustavDev/Timeline/Generated/ShadowHeart_InParty2.lsf'), d)

    ab = game_assets.get_modded_dialog_asset_bundle('ShadowHeart_InParty')
    d = bg3.dialog_object(ab.dialog)
    t = bg3.timeline_object(ab.timeline, d)

    slot_idx_shadowheart = d.get_speaker_slot_index(bg3.SPEAKER_SHADOWHEART)
    slot_idx_tav = d.get_speaker_slot_index(bg3.SPEAKER_PLAYER)

    tav_cheated_greeting_node_uuid = '3d54008c-057f-47ed-8bde-6c236d7da47e'
    i_need_to_think_node_uuid = 'ac9ea285-9901-4fae-b7f6-785fafb82814'
    i_digress_node_uuid = 'c95f06c1-3b2d-4f3a-89a0-47e90c1761db'
    approval_80_greetings_male_node_uuid = '80fc8153-9363-4c6f-a3bc-ec5e81cbc08a'
    approval_80_greetings_female_node_uuid = '8d8076e7-1bf1-4a91-95f2-469986a6a5bb'
    every_day_is_an_adventure_node_uuid = '0bc3d936-8a92-4f4e-bc51-26658a78c35b'
    did_you_want_something_node_uuid = 'f7e507b8-80f0-4f29-ba83-94f872db1329'

    shadowheart_hesitates_to_ask_node_uuid = 'e0fbf080-1b83-4de8-9ddd-717b4c56b011'
    dialog_flow_node_uuid = '313eed6b-ac15-4ebe-894d-4844163fb36c'
    please_tell_me_node_uuid = 'fb1fae6d-386f-4a2f-be91-12f3b61658ca'
    very_well_node_uuid = '28faa883-7814-4786-91bc-6b3a4f269a93'
    wine_more_often_node_uuid = '9e750a0a-3de3-47d7-bf64-724f2bf4d3b9'
    awfully_cold_node_uuid = '730c51a2-aa91-43c9-8b0d-27b56260268b'
    you_dont_need_wine_node_uuid = '8d5b9ad9-7186-48d3-98c9-892640b532ec'
    id_gladly_kill_a_bottle_node_uuid = 'c6774d31-9526-4f5d-8209-5d2abc4b9bb6'
    i_feel_the_same_way_node_uuid = '64aab437-c9b0-4e61-948b-4e285a25bd37'
    more_than_one_way_keep_me_warm_node_uuid = '9dc01dba-c3ff-4f10-8d35-6d247a76783e'
    room_for_you_and_the_bottle_node_uuid = '6552fdfa-a30b-4f2d-b5aa-5715a689efc6'
    good_enough_for_me_node_uuid = 'd9248dcf-2289-43f2-a180-3e9837ab18c4'
    jump_back_node_uuid = 'f09c2d44-ef52-43ae-ae80-254fc05c9db1'

    children_nodes = d.get_children_nodes_uuids(existing_partnered_greetings_node_uuid)
    d.delete_all_children_dialog_nodes(existing_partnered_greetings_node_uuid)
    d.add_child_dialog_node(existing_partnered_greetings_node_uuid, sleep_together_entry_point_node_uuid)

    d.create_jump_dialog_node(jump_back_node_uuid, bg3.SHADOWHEART_QUESTION_BANK_ROOT_NODE_UUID, 2)

    # Shadowheart hesitates to ask Tav about sleeping together at night
    d.create_standard_dialog_node(
        sleep_together_entry_point_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [shadowheart_hesitates_to_ask_node_uuid, dialog_flow_node_uuid],
        None)

    d.create_cinematic_dialog_node(
        shadowheart_hesitates_to_ask_node_uuid,
        [dialog_flow_node_uuid],
        checkflags = (
            bg3.flag_group('Global', (
                bg3.flag(bg3.FLAG_GLO_CAMP_State_NightMode, True, None),
                bg3.flag(bg3.FLAG_VISITEDREGION_BGO_Main_A, True, None),
                bg3.flag(Shadowheart_Turned_Away_From_Shar.uuid, True, None),
            )),
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_State_PartneredWithShadowheart, True, slot_idx_tav),
                bg3.flag(Shadowheart_Tav_Sleep_Together.uuid, False, slot_idx_tav),
                bg3.flag(Shadowheart_Has_Doubts_About_Tav.uuid, False, slot_idx_tav),
                bg3.flag(Shadowheart_Hesitated_To_Ask.uuid, False, slot_idx_shadowheart),
            )),
        ),
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(Shadowheart_Hesitated_To_Ask.uuid, True, slot_idx_shadowheart),
                bg3.flag(Tav_Noticed_Shadowheart_Hesitated_To_Ask.uuid, True, slot_idx_shadowheart),
            )),
        ))
    d.create_standard_dialog_node(
        dialog_flow_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        children_nodes,
        None)

    phase_duration = '4.5'
    t.create_new_phase(shadowheart_hesitates_to_ask_node_uuid, phase_duration)
    t.create_tl_actor_node(bg3.timeline_object.ATTITUDE, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.ATTITUDE, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.EMOTION, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_emotion_key(0.0, 64),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(
        bg3.timeline_object.LOOK_AT,
        bg3.SPEAKER_SHADOWHEART,
        '0.0', phase_duration,
        (t.create_look_at_key(0.0, target = bg3.SPEAKER_PLAYER, bone = 'Head_M', turn_mode = 2, reset = True),),
        is_snapped_to_end = True)
    t.create_tl_actor_node(
        bg3.timeline_object.LOOK_AT,
        bg3.SPEAKER_PLAYER,
        '0.0', phase_duration,
        (t.create_look_at_key(0.0, target = bg3.SPEAKER_SHADOWHEART, bone = 'Head_M', turn_mode = 2, reset = True),),
        is_snapped_to_end = True)
    t.create_tl_shot('95a53513-08ce-4d80-ae74-e306b51db565', '0.0', '2.0')
    t.create_tl_shot('8942c483-83c9-4974-9f47-87cd1dd10828', '2.0', '4.4')
    t.create_tl_animation(
        bg3.SPEAKER_SHADOWHEART,
        '2.0', phase_duration,
        '5db0326e-fb0e-d3dd-a56d-51aa4da6ab00',
        '13ccbef4-3a1f-4c55-988d-b79aa094db1d',
        animation_play_rate = 0.8,
        fade_in = 0.0,
        fade_out = 0.0,
        is_snapped_to_end = False)
    t.create_tl_shot('cde43894-62c3-4f23-8ea7-b772f9357697', '4.4', phase_duration, is_snapped_to_end = True)

    # You were looking at me like you wanted to say something. Don't be shy, tell me.
    d.create_standard_dialog_node(
        please_tell_me_node_uuid,
        bg3.SPEAKER_PLAYER,
        [very_well_node_uuid],
        bg3.text_content('h35eecf11g59ceg496bg9d60g37fe40337891', 1),
        constructor = bg3.dialog_object.QUESTION,
        checkflags = (
            bg3.flag_group('Global', (
                bg3.flag(bg3.FLAG_GLO_CAMP_State_NightMode, True, None),
                bg3.flag(bg3.FLAG_VISITEDREGION_BGO_Main_A, True, None),
            )),
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_State_PartneredWithShadowheart, True, slot_idx_tav),
                bg3.flag(Shadowheart_Tav_Sleep_Together.uuid, False, slot_idx_tav),
                bg3.flag(Tav_Noticed_Shadowheart_Hesitated_To_Ask.uuid, True, slot_idx_shadowheart),
            )),
        ))
    d.add_child_dialog_node(bg3.SHADOWHEART_QUESTION_BANK_ROOT_NODE_UUID, please_tell_me_node_uuid, 0)

    # Very well...
    d.create_standard_dialog_node(
        very_well_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [wine_more_often_node_uuid],
        bg3.text_content('h93eaf8e9g2808g47cdgbd6egc9add28a87c0', 1))
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '0.9135',
        very_well_node_uuid,
        ((None, '8942c483-83c9-4974-9f47-87cd1dd10828'),),
        phase_duration = '1.1',
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 1, None),),
            bg3.SPEAKER_PLAYER: ((0.0, 1, None),)
        },
        attitudes = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_R_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, 3),),
            bg3.SPEAKER_PLAYER: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_L_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, 3),)
        }
    )
    t.create_tl_actor_node(
        bg3.timeline_object.LOOK_AT,
        bg3.SPEAKER_SHADOWHEART,
        '0.0',
        '1.1',
        (t.create_look_at_key(0.0, target = bg3.SPEAKER_PLAYER, bone = 'Head_M', turn_mode = 2, reset = True),),
        is_snapped_to_end = True
    )
    t.create_tl_actor_node(
        bg3.timeline_object.LOOK_AT,
        bg3.SPEAKER_PLAYER,
        '0.0',
        '1.1',
        (t.create_look_at_key(0.0, target = bg3.SPEAKER_SHADOWHEART, bone = 'Head_M', turn_mode = 2, reset = True),),
        is_snapped_to_end = True
    )

    # We should've had wine more often. More warming than the fire.
    d.create_standard_dialog_node(
        wine_more_often_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [awfully_cold_node_uuid],
        bg3.text_content('h1717338fga82bg4f20ga158g6dbca07e41f3', 1))
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '3.96',
        wine_more_often_node_uuid,
        ((None, '0e8837db-4344-48d0-9175-12262c73806b'),),
        phase_duration = '3.96',
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 1024, 2), (2.9, 1024, None)),
            bg3.SPEAKER_PLAYER: ((0.0, 1, None),)
        },
        attitudes = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_R_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, 3),),
            bg3.SPEAKER_PLAYER: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_L_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, 3),)
        }
    )
    t.create_tl_actor_node(
        bg3.timeline_object.LOOK_AT,
        bg3.SPEAKER_SHADOWHEART,
        '0.0',
        '3.96',
        (t.create_look_at_key(0.0, target = bg3.SPEAKER_PLAYER, bone = 'Head_M', turn_mode = 2, reset = True),),
        is_snapped_to_end = True
    )
    t.create_tl_actor_node(
        bg3.timeline_object.LOOK_AT,
        bg3.SPEAKER_PLAYER,
        '0.0',
        '3.96',
        (t.create_look_at_key(0.0, target = bg3.SPEAKER_SHADOWHEART, bone = 'Head_M', turn_mode = 2, reset = True),),
        is_snapped_to_end = True
    )

    # After all, it can get awfully cold at night out here in this wilderness...
    d.create_standard_dialog_node(
        awfully_cold_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [id_gladly_kill_a_bottle_node_uuid, you_dont_need_wine_node_uuid],
        bg3.text_content('h592daa08g31f9g418eg9be7g0ed58daf3b49', 1))
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '5.7',
        awfully_cold_node_uuid,
        (('5.65', '8942c483-83c9-4974-9f47-87cd1dd10828'), (None, '95a53513-08ce-4d80-ae74-e306b51db565')),
        phase_duration = '5.7',
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 16, None), (2.16, 32, None), (4.7, 1024, 1)),
            bg3.SPEAKER_PLAYER: ((0.0, 1, None),)
        },
        attitudes = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_R_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, 3),),
            bg3.SPEAKER_PLAYER: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_L_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, 3),)
        }
    )
    t.create_tl_actor_node(
        bg3.timeline_object.LOOK_AT,
        bg3.SPEAKER_SHADOWHEART,
        '0.0',
        '5.7',
        (t.create_look_at_key(0.0, target = bg3.SPEAKER_PLAYER, bone = 'Head_M', turn_mode = 2, reset = True),),
        is_snapped_to_end = True
    )
    t.create_tl_actor_node(
        bg3.timeline_object.LOOK_AT,
        bg3.SPEAKER_PLAYER,
        '0.0',
        '5.7',
        (t.create_look_at_key(0.0, target = bg3.SPEAKER_SHADOWHEART, bone = 'Head_M', turn_mode = 2, reset = True),),
        is_snapped_to_end = True
    )

    # You don't need wine if you have me. I can keep you warm all night. There's room for you in my bedroll.
    d.create_standard_dialog_node(
        you_dont_need_wine_node_uuid,
        bg3.SPEAKER_PLAYER,
        [i_feel_the_same_way_node_uuid],
        bg3.text_content('h0d248adbg6d7cg4e55gb525gd439c5d526d9', 1),
        constructor = bg3.dialog_object.QUESTION,
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(Shadowheart_Tav_Sleep_Together.uuid, True, slot_idx_tav),
            )),
        ))

    # I'm glad. I feel the same way.
    reaction_plus_5 = bg3.reaction_object.create_new(files, { bg3.SPEAKER_SHADOWHEART : 5 }, uuid = '9f79f483-4cc1-4aef-9402-83ec7502ed25')
    d.create_standard_dialog_node(
        i_feel_the_same_way_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [jump_back_node_uuid],
        bg3.text_content('h5fb51729g09b2g4e2dgbdceg2d86d3c32275', 1),
        approval_rating_uuid=reaction_plus_5.uuid)
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '4.09',
        i_feel_the_same_way_node_uuid,
        (('4.05', '8942c483-83c9-4974-9f47-87cd1dd10828'), (None, 'd76eaab3-040b-4871-9c1d-4a8624f37cd2')),
        phase_duration = '4.09',
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 2, 1),),
            bg3.SPEAKER_PLAYER: ((0.0, 2, None),)
        },
        attitudes = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_R_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, 3),),
            bg3.SPEAKER_PLAYER: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_L_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, 3),)
        }
    )
    t.create_tl_actor_node(
        bg3.timeline_object.LOOK_AT,
        bg3.SPEAKER_SHADOWHEART,
        '0.0',
        '4.09',
        (t.create_look_at_key(0.0, target = bg3.SPEAKER_PLAYER, bone = 'Head_M', turn_mode = 2, reset = True),),
        is_snapped_to_end = True
    )
    t.create_tl_actor_node(
        bg3.timeline_object.LOOK_AT,
        bg3.SPEAKER_PLAYER,
        '0.0',
        '4.09',
        (t.create_look_at_key(0.0, target = bg3.SPEAKER_SHADOWHEART, bone = 'Head_M', turn_mode = 2, reset = True),),
        is_snapped_to_end = True
    )

    # Did you manage to save one of those liberated vintages? I'd gladly kill a bottle or two.
    d.create_standard_dialog_node(
        id_gladly_kill_a_bottle_node_uuid,
        bg3.SPEAKER_PLAYER,
        [more_than_one_way_keep_me_warm_node_uuid],
        bg3.text_content('h1cde79d9g165bg4f6fg9025g57881c3491f6', 1),
        constructor = bg3.dialog_object.QUESTION)

    # There's more than one way to keep me warm.
    d.create_standard_dialog_node(
        more_than_one_way_keep_me_warm_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [you_dont_need_wine_node_uuid, room_for_you_and_the_bottle_node_uuid],
        bg3.text_content('hc792b085g2c19g430fgb461g700fd3588775', 1))
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '2.7',
        more_than_one_way_keep_me_warm_node_uuid,
        (('2.65', '8942c483-83c9-4974-9f47-87cd1dd10828'), (None, '95a53513-08ce-4d80-ae74-e306b51db565')),
        phase_duration = '2.7',
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 1024, 1), (2.0, 1024, 2)),
            bg3.SPEAKER_PLAYER: ((0.0, 2, None),)
        },
        attitudes = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_R_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, 3),),
            bg3.SPEAKER_PLAYER: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_L_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, 3),)
        })
    t.create_tl_actor_node(
        bg3.timeline_object.LOOK_AT,
        bg3.SPEAKER_SHADOWHEART,
        '0.0',
        '2.7',
        (t.create_look_at_key(0.0, target = bg3.SPEAKER_PLAYER, bone = 'Head_M', turn_mode = 2, reset = True),),
        is_snapped_to_end = True)
    t.create_tl_actor_node(
        bg3.timeline_object.LOOK_AT,
        bg3.SPEAKER_PLAYER,
        '0.0',
        '2.7',
        (t.create_look_at_key(0.0, target = bg3.SPEAKER_SHADOWHEART, bone = 'Head_M', turn_mode = 2, reset = True),),
        is_snapped_to_end = True)

    # There's room for you in my bedroll. And the bottle.
    d.create_standard_dialog_node(
        room_for_you_and_the_bottle_node_uuid,
        bg3.SPEAKER_PLAYER,
        [good_enough_for_me_node_uuid],
        bg3.text_content('hc875bd6cgdffag4bc1gb668g133a1cf06ba5', 1),
        constructor = bg3.dialog_object.QUESTION,
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(Shadowheart_Tav_Sleep_Together.uuid, True, slot_idx_tav),
            )),
        ))

    # That's good enough for me.
    d.create_standard_dialog_node(
        good_enough_for_me_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [jump_back_node_uuid],
        bg3.text_content('h08ccc8afgb1dag4ea7g907eg5760821bdca7', 1))
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '1.94',
        good_enough_for_me_node_uuid,
        (('1.90', '8942c483-83c9-4974-9f47-87cd1dd10828'), (None, 'd76eaab3-040b-4871-9c1d-4a8624f37cd2')),
        phase_duration = '1.94',
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 2, 1),),
            bg3.SPEAKER_PLAYER: ((0.0, 2, None),)
        },
        attitudes = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_R_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, 3),),
            bg3.SPEAKER_PLAYER: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_L_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, 3),)
        })
    t.create_tl_actor_node(
        bg3.timeline_object.LOOK_AT,
        bg3.SPEAKER_SHADOWHEART,
        '0.0',
        '1.94',
        (t.create_look_at_key(0.0, target = bg3.SPEAKER_PLAYER, bone = 'Head_M', turn_mode = 2, reset = True),),
        is_snapped_to_end = True)
    t.create_tl_actor_node(
        bg3.timeline_object.LOOK_AT,
        bg3.SPEAKER_PLAYER,
        '0.0',
        '1.94',
        (t.create_look_at_key(0.0, target = bg3.SPEAKER_SHADOWHEART, bone = 'Head_M', turn_mode = 2, reset = True),),
        is_snapped_to_end = True)


    # I can't help but notice you seem happier of late. There's a spring in your step that wasn't there before.
    d.create_standard_dialog_node(
        tav_cheated_greeting_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [i_need_to_think_node_uuid],
        bg3.text_content('h9a16a3c8g8292g4e7ag93f0g2b5e721d602e', 1),
        constructor = bg3.dialog_object.GREETING,
        root = True,
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_State_PartneredWithShadowheart, True, slot_idx_tav),
                bg3.flag(Cheated_On_Shadowheart.uuid, True, slot_idx_tav),
                bg3.flag(Shadowheart_Reacted_To_Cheating.uuid, False, slot_idx_shadowheart),
            )),
        ),
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(Shadowheart_Reacted_To_Cheating.uuid, True, slot_idx_shadowheart),
            )),
        ))
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '7.7',
        tav_cheated_greeting_node_uuid,
        ((None, '8942c483-83c9-4974-9f47-87cd1dd10828'),),
        phase_duration = '8.0',
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 4, None), (2.54, 1024, 2), (4.46, 2, None)),
            bg3.SPEAKER_PLAYER: ((0.0, 1, None), (4.0, 4, None))
        },
        attitudes = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_R_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, 3),),
            bg3.SPEAKER_PLAYER: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_L_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, 3),)
        }
    )
    t.create_tl_actor_node(
        bg3.timeline_object.LOOK_AT,
        bg3.SPEAKER_SHADOWHEART,
        '0.0',
        '8.0',
        (t.create_look_at_key(0.0, target = bg3.SPEAKER_PLAYER, bone = 'Head_M', turn_mode = 2, reset = True),),
        is_snapped_to_end = True
    )
    t.create_tl_actor_node(
        bg3.timeline_object.LOOK_AT,
        bg3.SPEAKER_PLAYER,
        '0.0',
        '8.0',
        (t.create_look_at_key(0.0, target = bg3.SPEAKER_SHADOWHEART, bone = 'Head_M', turn_mode = 2, reset = True),),
        is_snapped_to_end = True
    )

    # I'm not sure I want to know...
    d.create_standard_dialog_node(
        i_need_to_think_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [i_digress_node_uuid],
        bg3.text_content('h9f205acbg8e31g462bgbfbbg956e9f1fb647', 1),
        constructor = bg3.dialog_object.ANSWER)
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '5.477',
        i_need_to_think_node_uuid,
        (('4.0', 'cde43894-62c3-4f23-8ea7-b772f9357697'), (None, 'd76eaab3-040b-4871-9c1d-4a8624f37cd2'),),
        phase_duration = '5.5',
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((4.0, 64, None),),
            bg3.SPEAKER_PLAYER: ((0.0, 4, None),)
        },
        attitudes = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_R_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, 3),),
            bg3.SPEAKER_PLAYER: ((1.0, '8128cb03-b18f-46c9-aca9-1c93991cf4ef', bg3.ATTITUDE_DIAG_T_Pose, 3),)
        }
    )
    t.create_tl_actor_node(
        bg3.timeline_object.LOOK_AT,
        bg3.SPEAKER_SHADOWHEART,
        '0.0',
        '5.5',
        (t.create_look_at_key(0.0, target = bg3.SPEAKER_PLAYER, bone = 'Head_M', turn_mode = 2, reset = True),),
        is_snapped_to_end = True
    )
    t.create_tl_actor_node(
        bg3.timeline_object.LOOK_AT,
        bg3.SPEAKER_PLAYER,
        '0.0',
        '5.5',
        (t.create_look_at_key(0.0, target = bg3.SPEAKER_SHADOWHEART, bone = 'Head_M', turn_mode = 2, reset = True),),
        is_snapped_to_end = True
    )

    # But I digress. Did you want something?
    d.create_standard_dialog_node(
        i_digress_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        children_nodes,
        bg3.text_content('hdcd786d5gf823g4367g8227gc8254d5ac7e8', 2),
        constructor = bg3.dialog_object.ANSWER)
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '3.96',
        i_digress_node_uuid,
        (('4.0', '8942c483-83c9-4974-9f47-87cd1dd10828'), (None, '95a53513-08ce-4d80-ae74-e306b51db565')),
        phase_duration = '4.1',
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 4, None), (2.2, 64, None)),
            bg3.SPEAKER_PLAYER: ((0.0, 4, None),)
        },
        attitudes = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_R_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, 3),),
            bg3.SPEAKER_PLAYER: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_L_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, 3),)
        }
    )
    t.create_tl_actor_node(
        bg3.timeline_object.LOOK_AT,
        bg3.SPEAKER_SHADOWHEART,
        '0.0',
        '4.1',
        (t.create_look_at_key(0.0, target = bg3.SPEAKER_PLAYER, bone = 'Head_M', turn_mode = 2, reset = True),),
        is_snapped_to_end = True
    )
    t.create_tl_actor_node(
        bg3.timeline_object.LOOK_AT,
        bg3.SPEAKER_PLAYER,
        '0.0',
        '4.1',
        (t.create_look_at_key(0.0, target = bg3.SPEAKER_SHADOWHEART, bone = 'Head_M', turn_mode = 2, reset = True),),
        is_snapped_to_end = True
    )


    #
    # High approval greetings
    #
    d.create_standard_dialog_node(
        approval_80_greetings_male_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [sleep_together_entry_point_node_uuid],
        [
            bg3.text_content('hd0509e5dgee24g4e38g9e53gd72e5795cba6', 1, 'e4b1d9bf-135b-45e6-847a-8463012c6866', custom_sequence_id = 'e4b1d9bf-135b-45e6-847a-8463012c6866'),
            bg3.text_content('h58a61da8g7b5ag4f8agbac5g354f62512e77', 3, 'a577d549-8937-4e3a-b988-d8ccaaebb569', custom_sequence_id = 'a577d549-8937-4e3a-b988-d8ccaaebb569'),
            bg3.text_content('ha2c23788g2acdg4d58gabe0g0caffdc54064', 3, 'd208eefa-aad3-47af-ab98-ea9a42441a71', custom_sequence_id = 'd208eefa-aad3-47af-ab98-ea9a42441a71'),
            bg3.text_content('h089930fdg3555g4822gae62g09abc9d6fee2', 3, '59aa4791-0680-46f4-9950-a3f89e632a48', custom_sequence_id = '59aa4791-0680-46f4-9950-a3f89e632a48'),
            bg3.text_content('h0633cd9bg74dfg4126g9e4fg65ca5667b814', 2, '62719932-ea92-4880-a0c0-92b1e4d7cdb4', custom_sequence_id = '62719932-ea92-4880-a0c0-92b1e4d7cdb4'),
            bg3.text_content('hd0509e5dgee24g4e38g9e53gd72e5795cba6', 1, 'fd040b4f-2f98-4a14-8637-871e005f3f4a', custom_sequence_id = 'fd040b4f-2f98-4a14-8637-871e005f3f4a'),
            #bg3.text_content('hd0509e5dgee24g4e38g9e53gd72e5795cba6', 1, '2a0925e2-918f-454a-b959-1088b620adf5', custom_sequence_id = '2a0925e2-918f-454a-b959-1088b620adf5'),
            #bg3.text_content('hd0509e5dgee24g4e38g9e53gd72e5795cba6', 1, '93e2cc80-a6d8-44d2-8199-28d9acb49966', custom_sequence_id = '93e2cc80-a6d8-44d2-8199-28d9acb49966'),
        ],
        constructor = bg3.dialog_object.GREETING,
        root = True,
        checkflags = (
            bg3.flag_group('Global', (
                bg3.flag(Shadowheart_Turned_Away_From_Shar.uuid, True, None),
            )),
            bg3.flag_group('Object', (
                bg3.flag(Shadowheart_More_Sandcastles.uuid, True, slot_idx_shadowheart),
                bg3.flag(bg3.FLAG_ORI_State_PartneredWithShadowheart, True, slot_idx_tav),
                bg3.flag(bg3.FLAG_Approval_AtLeast_80_For_Sp2, True, slot_idx_shadowheart),
                bg3.flag(Shadowheart_Has_Doubts_About_Tav.uuid, False, slot_idx_tav)
            )),
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_MALE, True, slot_idx_tav),
            ))
        ))

    # Checking in on me? I'm right where I'm supposed to be - with the man I love.
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '5.696',
        approval_80_greetings_male_node_uuid,
        (('5.8', '8942c483-83c9-4974-9f47-87cd1dd10828'), (None, '95a53513-08ce-4d80-ae74-e306b51db565')),
        phase_duration = '6.2',
        line_index = 0,
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 1024, 1), (2.29, 2, 1)),
            bg3.SPEAKER_PLAYER: ((0.0, 2, None),)
        },
        attitudes = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_R_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, 3),),
            bg3.SPEAKER_PLAYER: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_L_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, 3),)
        }
    )
    t.create_tl_actor_node(
        bg3.timeline_object.LOOK_AT,
        bg3.SPEAKER_SHADOWHEART,
        '0.0',
        '6.2',
        (t.create_look_at_key(0.0, target = bg3.SPEAKER_PLAYER, bone = 'Head_M', turn_mode = 2, reset = True),),
        is_snapped_to_end = True
    )
    t.create_tl_actor_node(
        bg3.timeline_object.LOOK_AT,
        bg3.SPEAKER_PLAYER,
        '0.0',
        '6.2',
        (t.create_look_at_key(0.0, target = bg3.SPEAKER_SHADOWHEART, bone = 'Head_M', turn_mode = 2, reset = True),),
        is_snapped_to_end = True
    )

    # Checking in on me? I'm right where I'm supposed to be - with the man I love.
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '5.696',
        approval_80_greetings_male_node_uuid,
        (('5.8', '8942c483-83c9-4974-9f47-87cd1dd10828'), (None, '95a53513-08ce-4d80-ae74-e306b51db565')),
        phase_duration = '6.2',
        line_index = 5,
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 1024, 1), (2.29, 2, 1)),
            bg3.SPEAKER_PLAYER: ((0.0, 2, None),)
        },
        attitudes = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_R_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, 3),),
            bg3.SPEAKER_PLAYER: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_L_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, 3),)
        }
    )
    t.create_tl_actor_node(
        bg3.timeline_object.LOOK_AT,
        bg3.SPEAKER_SHADOWHEART,
        '0.0',
        '6.2',
        (t.create_look_at_key(0.0, target = bg3.SPEAKER_PLAYER, bone = 'Head_M', turn_mode = 2, reset = True),),
        is_snapped_to_end = True
    )
    t.create_tl_actor_node(
        bg3.timeline_object.LOOK_AT,
        bg3.SPEAKER_PLAYER,
        '0.0',
        '6.2',
        (t.create_look_at_key(0.0, target = bg3.SPEAKER_SHADOWHEART, bone = 'Head_M', turn_mode = 2, reset = True),),
        is_snapped_to_end = True
    )

    # # Checking in on me? I'm right where I'm supposed to be - with the man I love.
    # t.create_simple_dialog_answer_phase(
    #     bg3.SPEAKER_SHADOWHEART,
    #     '5.696',
    #     approval_80_greetings_male_node_uuid,
    #     (('5.8', '8942c483-83c9-4974-9f47-87cd1dd10828'), (None, '95a53513-08ce-4d80-ae74-e306b51db565')),
    #     phase_duration = '6.2',
    #     line_index = 2,
    #     emotions = {
    #         bg3.SPEAKER_SHADOWHEART: ((0.0, 1024, 1), (2.29, 2, 1)),
    #         bg3.SPEAKER_PLAYER: ((0.0, 2, None),)
    #     },
    #     attitudes = {
    #         bg3.SPEAKER_SHADOWHEART: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_R_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, 3),),
    #         bg3.SPEAKER_PLAYER: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_L_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, 3),)
    #     }
    # )
    # t.create_tl_actor_node(
    #     bg3.timeline_object.LOOK_AT,
    #     bg3.SPEAKER_SHADOWHEART,
    #     '0.0',
    #     '6.2',
    #     (t.create_look_at_key(0.0, target = bg3.SPEAKER_PLAYER, bone = 'Head_M', turn_mode = 2, reset = True),),
    #     is_snapped_to_end = True
    # )
    # t.create_tl_actor_node(
    #     bg3.timeline_object.LOOK_AT,
    #     bg3.SPEAKER_PLAYER,
    #     '0.0',
    #     '6.2',
    #     (t.create_look_at_key(0.0, target = bg3.SPEAKER_SHADOWHEART, bone = 'Head_M', turn_mode = 2, reset = True),),
    #     is_snapped_to_end = True
    # )

    # # Checking in on me? I'm right where I'm supposed to be - with the man I love.
    # t.create_simple_dialog_answer_phase(
    #     bg3.SPEAKER_SHADOWHEART,
    #     '5.696',
    #     approval_80_greetings_male_node_uuid,
    #     (('5.8', '8942c483-83c9-4974-9f47-87cd1dd10828'), (None, '95a53513-08ce-4d80-ae74-e306b51db565')),
    #     phase_duration = '6.2',
    #     line_index = 3,
    #     emotions = {
    #         bg3.SPEAKER_SHADOWHEART: ((0.0, 1024, 1), (2.29, 2, 1)),
    #         bg3.SPEAKER_PLAYER: ((0.0, 2, None),)
    #     },
    #     attitudes = {
    #         bg3.SPEAKER_SHADOWHEART: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_R_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, 3),),
    #         bg3.SPEAKER_PLAYER: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_L_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, 3),)
    #     }
    # )
    # t.create_tl_actor_node(
    #     bg3.timeline_object.LOOK_AT,
    #     bg3.SPEAKER_SHADOWHEART,
    #     '0.0',
    #     '6.2',
    #     (t.create_look_at_key(0.0, target = bg3.SPEAKER_PLAYER, bone = 'Head_M', turn_mode = 2, reset = True),),
    #     is_snapped_to_end = True
    # )
    # t.create_tl_actor_node(
    #     bg3.timeline_object.LOOK_AT,
    #     bg3.SPEAKER_PLAYER,
    #     '0.0',
    #     '6.2',
    #     (t.create_look_at_key(0.0, target = bg3.SPEAKER_SHADOWHEART, bone = 'Head_M', turn_mode = 2, reset = True),),
    #     is_snapped_to_end = True
    # )

    # Aren't you a sight for sore eyes.
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '2.01',
        approval_80_greetings_male_node_uuid,
        (('2.23', '8942c483-83c9-4974-9f47-87cd1dd10828'), (None, '95a53513-08ce-4d80-ae74-e306b51db565')),
        phase_duration = '2.6',
        line_index = 1,
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 2, None),),
            bg3.SPEAKER_PLAYER: ((0.0, 2, None),)
        },
        attitudes = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_R_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, 3),),
            bg3.SPEAKER_PLAYER: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_L_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, 3),)
        }
    )
    t.create_tl_actor_node(
        bg3.timeline_object.LOOK_AT,
        bg3.SPEAKER_SHADOWHEART,
        '0.0',
        '2.6',
        (t.create_look_at_key(0.0, target = bg3.SPEAKER_PLAYER, bone = 'Head_M', turn_mode = 2, reset = True),),
        is_snapped_to_end = True
    )
    t.create_tl_actor_node(
        bg3.timeline_object.LOOK_AT,
        bg3.SPEAKER_PLAYER,
        '0.0',
        '2.6',
        (t.create_look_at_key(0.0, target = bg3.SPEAKER_SHADOWHEART, bone = 'Head_M', turn_mode = 2, reset = True),),
        is_snapped_to_end = True
    )

    # Did you want something? If not, I'm perfectly happy to just gaze upon you a while.
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '7.5',
        approval_80_greetings_male_node_uuid,
        (('7.5', '8942c483-83c9-4974-9f47-87cd1dd10828'), (None, '95a53513-08ce-4d80-ae74-e306b51db565')),
        phase_duration = '8.0',
        line_index = 2,
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 64, None), (2.23, 4, None), (4.02, 1024, 1), (5.83, 2, None)),
            bg3.SPEAKER_PLAYER: ((0.0, 2, None),)
        },
        attitudes = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_R_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, 3),),
            bg3.SPEAKER_PLAYER: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_L_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, 3),)
        }
    )
    t.create_tl_actor_node(
        bg3.timeline_object.LOOK_AT,
        bg3.SPEAKER_SHADOWHEART,
        '0.0',
        '8.0',
        (t.create_look_at_key(0.0, target = bg3.SPEAKER_PLAYER, bone = 'Head_M', turn_mode = 2, reset = True),),
        is_snapped_to_end = True
    )
    t.create_tl_actor_node(
        bg3.timeline_object.LOOK_AT,
        bg3.SPEAKER_PLAYER,
        '0.0',
        '8.0',
        (t.create_look_at_key(0.0, target = bg3.SPEAKER_SHADOWHEART, bone = 'Head_M', turn_mode = 2, reset = True),),
        is_snapped_to_end = True
    )

    # Why hello, lover... that sounded more debonaire in my head, I'll admit. Do you need something?<br>
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '7.72',
        approval_80_greetings_male_node_uuid,
        (('7.8', 'd76eaab3-040b-4871-9c1d-4a8624f37cd2'), (None, '95a53513-08ce-4d80-ae74-e306b51db565')),
        phase_duration = '8.1',
        line_index = 3,
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 64, None), (1.91, 2, 23), (2.79, 2, 1), (6.48, 1024, 2)),
            bg3.SPEAKER_PLAYER: ((0.0, 2, None),)
        },
        attitudes = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_R_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, 3),),
            bg3.SPEAKER_PLAYER: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_L_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, 3),)
        }
    )
    t.create_tl_actor_node(
        bg3.timeline_object.LOOK_AT,
        bg3.SPEAKER_SHADOWHEART,
        '0.0',
        '8.1',
        (t.create_look_at_key(0.0, target = bg3.SPEAKER_PLAYER, bone = 'Head_M', turn_mode = 2, reset = True),),
        is_snapped_to_end = True
    )
    t.create_tl_actor_node(
        bg3.timeline_object.LOOK_AT,
        bg3.SPEAKER_PLAYER,
        '0.0',
        '8.1',
        (t.create_look_at_key(0.0, target = bg3.SPEAKER_SHADOWHEART, bone = 'Head_M', turn_mode = 2, reset = True),),
        is_snapped_to_end = True
    )

    # Good. I was just starting to miss the sound of your voice.
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '4.96',
        approval_80_greetings_male_node_uuid,
        (('5.0', 'd76eaab3-040b-4871-9c1d-4a8624f37cd2'), (None, '95a53513-08ce-4d80-ae74-e306b51db565')),
        phase_duration = '5.36',
        line_index = 4,
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 2, 1), (1.6, 64, 1),),
            bg3.SPEAKER_PLAYER: ((0.0, 2, None),)
        },
        attitudes = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_R_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, 3),),
            bg3.SPEAKER_PLAYER: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_L_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, 3),)
        }
    )
    t.create_tl_actor_node(
        bg3.timeline_object.LOOK_AT,
        bg3.SPEAKER_SHADOWHEART,
        '0.0',
        '5.36',
        (t.create_look_at_key(0.0, target = bg3.SPEAKER_PLAYER, bone = 'Head_M', turn_mode = 2, reset = True),),
        is_snapped_to_end = True
    )
    t.create_tl_actor_node(
        bg3.timeline_object.LOOK_AT,
        bg3.SPEAKER_PLAYER,
        '0.0',
        '5.36',
        (t.create_look_at_key(0.0, target = bg3.SPEAKER_SHADOWHEART, bone = 'Head_M', turn_mode = 2, reset = True),),
        is_snapped_to_end = True
    )

    # Every day's an adventure when I'm at my love's side.
    d.create_standard_dialog_node(
        every_day_is_an_adventure_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [did_you_want_something_node_uuid],
        bg3.text_content('h93c12043g6cceg437cgb60eg8c0e6d55f466', 1),
        constructor = bg3.dialog_object.GREETING,
        root = True,
        checkflags = (
            bg3.flag_group('Global', (
                bg3.flag(Shadowheart_Turned_Away_From_Shar.uuid, True, None),
                bg3.flag(Shadowheart_FemTav_Greeting1.uuid, True, None)
            )),
            bg3.flag_group('Object', (
                bg3.flag(Shadowheart_More_Sandcastles.uuid, True, slot_idx_shadowheart),
                bg3.flag(bg3.FLAG_ORI_State_PartneredWithShadowheart, True, slot_idx_tav),
                bg3.flag(bg3.FLAG_Approval_AtLeast_80_For_Sp2, True, slot_idx_shadowheart),
                bg3.flag(Shadowheart_Has_Doubts_About_Tav.uuid, False, slot_idx_tav)
            )),
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_FEMALE, True, slot_idx_tav),
            ))
        ))
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '3.216',
        every_day_is_an_adventure_node_uuid,
        (('2.2', 'd76eaab3-040b-4871-9c1d-4a8624f37cd2'), (None, 'fd96b957-6a74-4f97-a035-eb9641c48242')),
        phase_duration = '3.6',
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 2, 1), (1.0, 2, 23), (1.5, 2, 2)),
            bg3.SPEAKER_PLAYER: ((2.5, 2, 1),)
        })

    # Did you want something?
    d.create_standard_dialog_node(
        did_you_want_something_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [sleep_together_entry_point_node_uuid],
        bg3.text_content('h17d75cacg075bg4c4ag93eegb085da3f124e', 1),
        setflags = (
            bg3.flag_group('Global', (
                bg3.flag(Shadowheart_FemTav_Greeting1.uuid, False, None),
            )),
        ))
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '1.5',
        did_you_want_something_node_uuid,
        (('0.3', 'fd96b957-6a74-4f97-a035-eb9641c48242'), ('1.8', '0e8837db-4344-48d0-9175-12262c73806b'), (None, 'cde43894-62c3-4f23-8ea7-b772f9357697')),
        phase_duration = '2.0',
        voice_delay = '0.3',
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.3, 1024, None), (1.2, 2, None)),
            bg3.SPEAKER_PLAYER: ((0.0, 2, None),)
        })

    # You may be what's been missing from my life.
    d.create_standard_dialog_node(
        approval_80_greetings_female_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [sleep_together_entry_point_node_uuid],
        [
            bg3.text_content('h8d6dc67fg9d25g4231g9188g177f1c53b322', 2, '6d564eb5-06d4-485a-807d-41520b49a54f', custom_sequence_id = '6d564eb5-06d4-485a-807d-41520b49a54f'),
            # bg3.text_content('h8d6dc67fg9d25g4231g9188g177f1c53b322', 2, '1216b29f-d790-4f92-aa27-335ef85b9090', custom_sequence_id = '1216b29f-d790-4f92-aa27-335ef85b9090'),
            # bg3.text_content('h8d6dc67fg9d25g4231g9188g177f1c53b322', 2, 'd1cb10d5-b80c-47a0-a720-fa4e21e3328c', custom_sequence_id = 'd1cb10d5-b80c-47a0-a720-fa4e21e3328c'),
            # bg3.text_content('h8d6dc67fg9d25g4231g9188g177f1c53b322', 2, 'baa40e34-2d0c-4a9a-8e96-dc9eac53955f', custom_sequence_id = 'baa40e34-2d0c-4a9a-8e96-dc9eac53955f'),
            bg3.text_content('h58a61da8g7b5ag4f8agbac5g354f62512e77', 3, '8a7f1a61-c327-48ea-932b-90709cf7a9e8', custom_sequence_id = '8a7f1a61-c327-48ea-932b-90709cf7a9e8'),
            bg3.text_content('ha2c23788g2acdg4d58gabe0g0caffdc54064', 3, 'd2f5a568-b211-4e55-ab6e-ed8fc04c4761', custom_sequence_id = 'd2f5a568-b211-4e55-ab6e-ed8fc04c4761'),
            bg3.text_content('h089930fdg3555g4822gae62g09abc9d6fee2', 3, 'e7878c05-d73e-469a-9f83-a687e45a2c1f', custom_sequence_id = 'e7878c05-d73e-469a-9f83-a687e45a2c1f'),
            bg3.text_content('h0633cd9bg74dfg4126g9e4fg65ca5667b814', 2, '55bc1c66-c6f1-477c-b710-877e8ec19e44', custom_sequence_id = '55bc1c66-c6f1-477c-b710-877e8ec19e44'),
        ],
        constructor = bg3.dialog_object.GREETING,
        root = True,
        checkflags = (
            bg3.flag_group('Global', (
                bg3.flag(Shadowheart_Turned_Away_From_Shar.uuid, True, None),
            )),
            bg3.flag_group('Object', (
                bg3.flag(Shadowheart_More_Sandcastles.uuid, True, slot_idx_shadowheart),
                bg3.flag(bg3.FLAG_ORI_State_PartneredWithShadowheart, True, slot_idx_tav),
                bg3.flag(bg3.FLAG_Approval_AtLeast_80_For_Sp2, True, slot_idx_shadowheart),
                bg3.flag(Shadowheart_Has_Doubts_About_Tav.uuid, False, slot_idx_tav)
            )),
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_FEMALE, True, slot_idx_tav),
            ))
        ))

    # You may be what's been missing from my life.
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '2.604',
        approval_80_greetings_female_node_uuid,
        (('2.604', '8942c483-83c9-4974-9f47-87cd1dd10828'), (None, '95a53513-08ce-4d80-ae74-e306b51db565')),
        phase_duration = '2.7',
        line_index = 0,
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 2, None),),
            bg3.SPEAKER_PLAYER: ((0.0, 2, None),)
        },
        attitudes = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_R_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, 3),),
            bg3.SPEAKER_PLAYER: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_L_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, 3),)
        }
    )
    t.create_tl_actor_node(
        bg3.timeline_object.LOOK_AT,
        bg3.SPEAKER_SHADOWHEART,
        '0.0',
        '2.7',
        (t.create_look_at_key(0.0, target = bg3.SPEAKER_PLAYER, bone = 'Head_M', turn_mode = 2, reset = True),),
        is_snapped_to_end = True
    )
    t.create_tl_actor_node(
        bg3.timeline_object.LOOK_AT,
        bg3.SPEAKER_PLAYER,
        '0.0',
        '2.7',
        (t.create_look_at_key(0.0, target = bg3.SPEAKER_SHADOWHEART, bone = 'Head_M', turn_mode = 2, reset = True),),
        is_snapped_to_end = True
    )

    # # You may be what's been missing from my life.
    # t.create_simple_dialog_answer_phase(
    #     bg3.SPEAKER_SHADOWHEART,
    #     2.604,
    #     approval_80_greetings_female_node_uuid,
    #     ((2.604, '8942c483-83c9-4974-9f47-87cd1dd10828'), (None, '95a53513-08ce-4d80-ae74-e306b51db565')),
    #     phase_duration = 2.7,
    #     line_index = 1,
    #     emotions = {
    #         bg3.SPEAKER_SHADOWHEART: ((0.0, 2, None),),
    #         bg3.SPEAKER_PLAYER: ((0.0, 2, None),)
    #     },
    #     attitudes = {
    #         bg3.SPEAKER_SHADOWHEART: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_R_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, 3),),
    #         bg3.SPEAKER_PLAYER: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_L_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, 3),)
    #     }
    # )
    # t.create_tl_actor_node(
    #     bg3.timeline_object.LOOK_AT,
    #     bg3.SPEAKER_SHADOWHEART,
    #     0.0,
    #     2.7,
    #     (t.create_look_at_key(0.0, target = bg3.SPEAKER_PLAYER, bone = 'Head_M', turn_mode = 2, reset = True),),
    #     is_snapped_to_end = True
    # )
    # t.create_tl_actor_node(
    #     bg3.timeline_object.LOOK_AT,
    #     bg3.SPEAKER_PLAYER,
    #     0.0,
    #     2.7,
    #     (t.create_look_at_key(0.0, target = bg3.SPEAKER_SHADOWHEART, bone = 'Head_M', turn_mode = 2, reset = True),),
    #     is_snapped_to_end = True
    # )

    # # You may be what's been missing from my life.
    # t.create_simple_dialog_answer_phase(
    #     bg3.SPEAKER_SHADOWHEART,
    #     2.604,
    #     approval_80_greetings_female_node_uuid,
    #     ((2.604, '8942c483-83c9-4974-9f47-87cd1dd10828'), (None, '95a53513-08ce-4d80-ae74-e306b51db565')),
    #     phase_duration = 2.7,
    #     line_index = 2,
    #     emotions = {
    #         bg3.SPEAKER_SHADOWHEART: ((0.0, 2, None),),
    #         bg3.SPEAKER_PLAYER: ((0.0, 2, None),)
    #     },
    #     attitudes = {
    #         bg3.SPEAKER_SHADOWHEART: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_R_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, 3),),
    #         bg3.SPEAKER_PLAYER: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_L_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, 3),)
    #     }
    # )
    # t.create_tl_actor_node(
    #     bg3.timeline_object.LOOK_AT,
    #     bg3.SPEAKER_SHADOWHEART,
    #     0.0,
    #     2.7,
    #     (t.create_look_at_key(0.0, target = bg3.SPEAKER_PLAYER, bone = 'Head_M', turn_mode = 2, reset = True),),
    #     is_snapped_to_end = True
    # )
    # t.create_tl_actor_node(
    #     bg3.timeline_object.LOOK_AT,
    #     bg3.SPEAKER_PLAYER,
    #     0.0,
    #     2.7,
    #     (t.create_look_at_key(0.0, target = bg3.SPEAKER_SHADOWHEART, bone = 'Head_M', turn_mode = 2, reset = True),),
    #     is_snapped_to_end = True
    # )

    # # You may be what's been missing from my life.
    # t.create_simple_dialog_answer_phase(
    #     bg3.SPEAKER_SHADOWHEART,
    #     2.604,
    #     approval_80_greetings_female_node_uuid,
    #     ((2.604, '8942c483-83c9-4974-9f47-87cd1dd10828'), (None, '95a53513-08ce-4d80-ae74-e306b51db565')),
    #     phase_duration = 2.7,
    #     line_index = 3,
    #     emotions = {
    #         bg3.SPEAKER_SHADOWHEART: ((0.0, 2, None),),
    #         bg3.SPEAKER_PLAYER: ((0.0, 2, None),)
    #     },
    #     attitudes = {
    #         bg3.SPEAKER_SHADOWHEART: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_R_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, 3),),
    #         bg3.SPEAKER_PLAYER: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_L_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, 3),)
    #     }
    # )
    # t.create_tl_actor_node(
    #     bg3.timeline_object.LOOK_AT,
    #     bg3.SPEAKER_SHADOWHEART,
    #     0.0,
    #     2.7,
    #     (t.create_look_at_key(0.0, target = bg3.SPEAKER_PLAYER, bone = 'Head_M', turn_mode = 2, reset = True),),
    #     is_snapped_to_end = True
    # )
    # t.create_tl_actor_node(
    #     bg3.timeline_object.LOOK_AT,
    #     bg3.SPEAKER_PLAYER,
    #     0.0,
    #     2.7,
    #     (t.create_look_at_key(0.0, target = bg3.SPEAKER_SHADOWHEART, bone = 'Head_M', turn_mode = 2, reset = True),),
    #     is_snapped_to_end = True
    # )

    # Aren't you a sight for sore eyes.
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '2.01',
        approval_80_greetings_female_node_uuid,
        (('2.23', '8942c483-83c9-4974-9f47-87cd1dd10828'), (None, '95a53513-08ce-4d80-ae74-e306b51db565')),
        phase_duration = '2.6',
        line_index = 1,
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 2, None),),
            bg3.SPEAKER_PLAYER: ((0.0, 2, None),)
        },
        attitudes = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_R_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, 3),),
            bg3.SPEAKER_PLAYER: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_L_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, 3),)
        }
    )
    t.create_tl_actor_node(
        bg3.timeline_object.LOOK_AT,
        bg3.SPEAKER_SHADOWHEART,
        '0.0',
        '2.6',
        (t.create_look_at_key(0.0, target = bg3.SPEAKER_PLAYER, bone = 'Head_M', turn_mode = 2, reset = True),),
        is_snapped_to_end = True
    )
    t.create_tl_actor_node(
        bg3.timeline_object.LOOK_AT,
        bg3.SPEAKER_PLAYER,
        '0.0',
        '2.6',
        (t.create_look_at_key(0.0, target = bg3.SPEAKER_SHADOWHEART, bone = 'Head_M', turn_mode = 2, reset = True),),
        is_snapped_to_end = True
    )

    # Did you want something? If not, I'm perfectly happy to just gaze upon you a while.
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '7.5',
        approval_80_greetings_female_node_uuid,
        (('7.5', '8942c483-83c9-4974-9f47-87cd1dd10828'), (None, '95a53513-08ce-4d80-ae74-e306b51db565')),
        phase_duration = '8.0',
        line_index = 2,
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 64, None), (2.23, 4, None), (4.02, 1024, 1), (5.83, 2, None)),
            bg3.SPEAKER_PLAYER: ((0.0, 2, None),)
        },
        attitudes = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_R_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, 3),),
            bg3.SPEAKER_PLAYER: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_L_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, 3),)
        }
    )
    t.create_tl_actor_node(
        bg3.timeline_object.LOOK_AT,
        bg3.SPEAKER_SHADOWHEART,
        '0.0',
        '8.0',
        (t.create_look_at_key(0.0, target = bg3.SPEAKER_PLAYER, bone = 'Head_M', turn_mode = 2, reset = True),),
        is_snapped_to_end = True
    )
    t.create_tl_actor_node(
        bg3.timeline_object.LOOK_AT,
        bg3.SPEAKER_PLAYER,
        '0.0',
        '8.0',
        (t.create_look_at_key(0.0, target = bg3.SPEAKER_SHADOWHEART, bone = 'Head_M', turn_mode = 2, reset = True),),
        is_snapped_to_end = True
    )

    # Why hello, lover... that sounded more debonaire in my head, I'll admit. Do you need something?<br>
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '7.72',
        approval_80_greetings_female_node_uuid,
        (('7.8', 'd76eaab3-040b-4871-9c1d-4a8624f37cd2'), (None, '95a53513-08ce-4d80-ae74-e306b51db565')),
        phase_duration = '8.1',
        line_index = 3,
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 64, None), (1.91, 2, 23), (2.79, 2, 1), (6.48, 1024, 2)),
            bg3.SPEAKER_PLAYER: ((0.0, 2, None),)
        },
        attitudes = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_R_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, 3),),
            bg3.SPEAKER_PLAYER: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_L_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, 3),)
        }
    )
    t.create_tl_actor_node(
        bg3.timeline_object.LOOK_AT,
        bg3.SPEAKER_SHADOWHEART,
        '0.0',
        '8.1',
        (t.create_look_at_key(0.0, target = bg3.SPEAKER_PLAYER, bone = 'Head_M', turn_mode = 2, reset = True),),
        is_snapped_to_end = True
    )
    t.create_tl_actor_node(
        bg3.timeline_object.LOOK_AT,
        bg3.SPEAKER_PLAYER,
        '0.0',
        '8.1',
        (t.create_look_at_key(0.0, target = bg3.SPEAKER_SHADOWHEART, bone = 'Head_M', turn_mode = 2, reset = True),),
        is_snapped_to_end = True
    )

    # Good. I was just starting to miss the sound of your voice.
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '4.96',
        approval_80_greetings_female_node_uuid,
        (('5.0', 'd76eaab3-040b-4871-9c1d-4a8624f37cd2'), (None, '95a53513-08ce-4d80-ae74-e306b51db565')),
        phase_duration = '5.36',
        line_index = 4,
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 2, 1), (1.6, 64, 1),),
            bg3.SPEAKER_PLAYER: ((0.0, 2, None),)
        },
        attitudes = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_R_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, 3),),
            bg3.SPEAKER_PLAYER: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_L_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, 3),)
        }
    )
    t.create_tl_actor_node(
        bg3.timeline_object.LOOK_AT,
        bg3.SPEAKER_SHADOWHEART,
        '0.0',
        '5.36',
        (t.create_look_at_key(0.0, target = bg3.SPEAKER_PLAYER, bone = 'Head_M', turn_mode = 2, reset = True),),
        is_snapped_to_end = True
    )
    t.create_tl_actor_node(
        bg3.timeline_object.LOOK_AT,
        bg3.SPEAKER_PLAYER,
        '0.0',
        '5.36',
        (t.create_look_at_key(0.0, target = bg3.SPEAKER_SHADOWHEART, bone = 'Head_M', turn_mode = 2, reset = True),),
        is_snapped_to_end = True
    )


    ###############################################################################
    # Tav did something that will cause Shadowheart to reject marriage proposal
    ###############################################################################
    in_need_of_attention_node_uuid = '5da1bb39-0494-4787-80f9-26413183c498'
    few_occasions_given_me_doubts_node_uuid = '12bde6cd-12ee-4219-aedc-a17ff830483d'
    i_hesitated_node_uuid = '083fa325-df71-4c2b-8751-873e50d9f8b5'
    a_list_of_charges_node_uuid = '4d525d69-8745-452b-b375-3edef00a91f5'
    were_just_too_different_node_uuid = '6d2d7f03-7e0e-4ebc-9989-53354790028a'
    we_cant_pretend_node_uuid = '92fe1f40-15b9-456a-b724-ba2e7b117d47'
    take_things_as_they_come_node_uuid = 'faeeef9a-65a1-4938-b648-92972ccd0413'
    if_thats_how_you_feel_node_uuid = '8dc12926-888d-42e1-8a7a-af2694073cb7'

    you_dont_sound_like_yourself_node_uuid = 'b530f360-a727-486d-9cd7-4a6b409db33d'
    you_hesitated_to_tell_me_something_node_uuid = 'f0d16e08-74c6-4392-af2e-750f361d57e5'
    i_can_do_better_node_uuid = '6470fa48-85cb-41b8-82cc-74ebe76b9365'
    you_can_always_find_someone_else_node_uuid = '9239cba3-380e-4517-8d58-065b8795f17f'

    # In need of attention, I take it?
    d.create_standard_dialog_node(
        in_need_of_attention_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [
            you_dont_sound_like_yourself_node_uuid,
            you_hesitated_to_tell_me_something_node_uuid,
        ],
        bg3.text_content('hdcf8e090g9bbeg4352ga4b7g955471d143c4', 3),
        constructor = bg3.dialog_object.GREETING,
        root = True,
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(Shadowheart_Has_Doubts_About_Tav.uuid, True, slot_idx_tav),
                bg3.flag(Shadowheart_Rejects_Proposal.uuid, False, slot_idx_shadowheart),
            )),
        ),
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(Shadowheart_Rejects_Proposal.uuid, True, slot_idx_shadowheart),
                bg3.flag(Shadowheart_Tav_Sleep_Together.uuid, False, slot_idx_tav),
            )),
        ))
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '2.49',
        in_need_of_attention_node_uuid,
        (('2.49', '0e8837db-4344-48d0-9175-12262c73806b'), (None, '95a53513-08ce-4d80-ae74-e306b51db565')),
        phase_duration = '2.8',
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 4, None), (1.01, 4, 2)),
            bg3.SPEAKER_PLAYER: ((0.0, 1, None),),
        },
        attitudes = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_R_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, 3),),
            bg3.SPEAKER_PLAYER: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_L_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, 3),),
        })

    # You don't sound like yourself since we arrived here. Should I be concerned?
    d.create_standard_dialog_node(
        you_dont_sound_like_yourself_node_uuid,
        bg3.SPEAKER_PLAYER,
        [few_occasions_given_me_doubts_node_uuid],
        bg3.text_content('h6a2c1bbbg2dfcg4525g93eag287aaea2de8f', 1),
        constructor = bg3.dialog_object.QUESTION,
        show_once = True)

    # You hesitated to tell me something. What's bothering you?
    d.create_standard_dialog_node(
        you_hesitated_to_tell_me_something_node_uuid,
        bg3.SPEAKER_PLAYER,
        [i_hesitated_node_uuid],
        bg3.text_content('h6d4158c7g11aag4eedg9d70g2811e83a7800', 1),
        constructor = bg3.dialog_object.QUESTION,
        show_once = True)

    # Well... since then, there's been a few occasions where you've given me doubts. Said things, or done things...
    d.create_standard_dialog_node(
        few_occasions_given_me_doubts_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [a_list_of_charges_node_uuid],
        bg3.text_content('h0fb40b24gb09dg4c37gade4gd03b7e79d750', 1))
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '11.56',
        few_occasions_given_me_doubts_node_uuid,
        ((None, 'd76eaab3-040b-4871-9c1d-4a8624f37cd2'),),
        phase_duration = '11.7',
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 16, None), (1.4, 4, None), (3.12, 64, None), (5.62, 4, None), (8.98, 32, None)),
            bg3.SPEAKER_PLAYER: ((0.0, 1, None),),
        },
        attitudes = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_R_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, 3),),
            bg3.SPEAKER_PLAYER: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_L_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, 3),)
        })

    # I hesitated? Probably because I was coming to realise what a poor match we are for each other.
    d.create_standard_dialog_node(
        i_hesitated_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [a_list_of_charges_node_uuid],
        bg3.text_content('h0b36cc12gf68bg4543g91ddg329318005c48', 1))
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '6.28',
        i_hesitated_node_uuid,
        ((None, 'd76eaab3-040b-4871-9c1d-4a8624f37cd2'),),
        phase_duration = '6.55',
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 16, None), (0.95, 1024, 2), (1.89, 128, None),),
            bg3.SPEAKER_PLAYER: ((0.0, 1, None),),
        },
        attitudes = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_R_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, 3),),
            bg3.SPEAKER_PLAYER: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_L_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, 3),)
        })

    # It's not like I've been keeping a list of charges to throw at you. There's just... moments.
    d.create_standard_dialog_node(
        a_list_of_charges_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [were_just_too_different_node_uuid],
        bg3.text_content('h1a0fb4f0g2d87g4c5cgbfd4g455259452c83', 1))
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '6.52',
        a_list_of_charges_node_uuid,
        ((None, '0e8837db-4344-48d0-9175-12262c73806b'),),
        phase_duration = '6.8',
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 16, None), (5.11, 32, None),),
            bg3.SPEAKER_PLAYER: ((0.0, 1, None),),
        },
        attitudes = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_R_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, 3),),
            bg3.SPEAKER_PLAYER: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_L_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, 3),)
        })

    # Made me wonder if perhaps we're just too different. If we should just let things lie.
    d.create_standard_dialog_node(
        were_just_too_different_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [
            i_can_do_better_node_uuid,
            you_can_always_find_someone_else_node_uuid,
        ],
        bg3.text_content('he3fb77aag6e0ag4cc4gb1cfgc7d96426324f', 1))
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '6.19',
        were_just_too_different_node_uuid,
        (('6.19', 'd76eaab3-040b-4871-9c1d-4a8624f37cd2'), (None, '95a53513-08ce-4d80-ae74-e306b51db565')),
        phase_duration = '6.3',
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 2048, None), (3.68, 4, None), (5.55, 16, None),),
            bg3.SPEAKER_PLAYER: ((0.0, 1, None),),
        },
        attitudes = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_R_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, 3),),
            bg3.SPEAKER_PLAYER: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_L_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, 3),)
        })

    # I can do better. I just need to know what I did wrong.
    d.create_standard_dialog_node(
        i_can_do_better_node_uuid,
        bg3.SPEAKER_PLAYER,
        [we_cant_pretend_node_uuid],
        bg3.text_content('hff321ee7g55dfg47a7g8ca3ga842eb015d0e', 1),
        constructor = bg3.dialog_object.QUESTION,
        show_once = True)

    # Well, you can always find someone else who is not that different.
    d.create_standard_dialog_node(
        you_can_always_find_someone_else_node_uuid,
        bg3.SPEAKER_PLAYER,
        [if_thats_how_you_feel_node_uuid],
        bg3.text_content('hd5cd72bcg5c33g48adgbce9gec28e4c84b0f', 1),
        constructor = bg3.dialog_object.QUESTION,
        show_once = True)

    # Don't. We can't pretend to be someone we're not - either of us. It'll just end badly.
    d.create_standard_dialog_node(
        we_cant_pretend_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [take_things_as_they_come_node_uuid],
        bg3.text_content('h6d8757ccgc91eg4d61gb239g5399f29ff092', 1))
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '8.52',
        we_cant_pretend_node_uuid,
        ((None, 'd76eaab3-040b-4871-9c1d-4a8624f37cd2'),),
        phase_duration = '8.6',
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 128, None), (1.61, 32, None), (5.69, 2048, 1),),
            bg3.SPEAKER_PLAYER: ((0.0, 1, None),),
        },
        attitudes = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_R_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, 3),),
            bg3.SPEAKER_PLAYER: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_L_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, 3),)
        })

    # Let's just... take things in as they come.
    d.create_standard_dialog_node(
        take_things_as_they_come_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [],
        bg3.text_content('h4148e233g5535g4c07ga75cg34aea80fea52', 1),
        end_node = True)
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '3.85',
        take_things_as_they_come_node_uuid,
        ((None, '0e8837db-4344-48d0-9175-12262c73806b'),),
        phase_duration = '4.0',
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 32, None),),
            bg3.SPEAKER_PLAYER: ((0.0, 32, None),),
        },
        attitudes = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_R_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, 3),),
            bg3.SPEAKER_PLAYER: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_L_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, 3),)
        })

    # Oh... if that's how you feel about it, fine. Not every sapling is destined to grow tall, I suppose.
    d.create_standard_dialog_node(
        if_thats_how_you_feel_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [],
        bg3.text_content('hdf52392eg6d0fg4a70gaaf2gcd533d48750b', 1),
        end_node = True,
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(Shadowheart_Approval_Set_To_35.uuid, True, slot_idx_tav),
            )),
        ))
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '10.86',
        if_thats_how_you_feel_node_uuid,
        ((None, 'd76eaab3-040b-4871-9c1d-4a8624f37cd2'),),
        phase_duration = '11.3',
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 16, None), (0.65, 128, None), (1.88, 16, 1), (4.4, 2048, None), (5.66, 4, None), (7.49, 2048, None)),
            bg3.SPEAKER_PLAYER: ((0.0, 1, None),),
        },
        attitudes = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_R_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, 3),),
            bg3.SPEAKER_PLAYER: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_L_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, 3),)
        })


    node_index = d.get_root_node_index(existing_partnered_greetings_node_uuid)
    d.add_root_node(approval_80_greetings_male_node_uuid, index = node_index)
    d.add_root_node(approval_80_greetings_female_node_uuid, index = node_index)
    d.add_root_node(every_day_is_an_adventure_node_uuid, index = node_index)
    d.add_root_node(in_need_of_attention_node_uuid, index = node_index)
    d.add_root_node(tav_cheated_greeting_node_uuid, index = node_index)


def create_sharran_greetings() -> None:
    ############################################################################################
    # Dialog: ShadowHeart_InParty2.lsf
    ############################################################################################

    # d = bg3.dialog_object(files.get_file('Gustav', 'Mods/GustavDev/Story/DialogsBinary/Companions/ShadowHeart_InParty2.lsf'))
    # t = bg3.timeline_object(files.get_file('Gustav', 'Public/GustavDev/Timeline/Generated/ShadowHeart_InParty2.lsf'), d)

    ab = game_assets.get_modded_dialog_asset_bundle('ShadowHeart_InParty')
    d = bg3.dialog_object(ab.dialog)
    t = bg3.timeline_object(ab.timeline, d)

    speaker_idx_shadowheart = d.get_speaker_slot_index(bg3.SPEAKER_SHADOWHEART)
    speaker_idx_tav = d.get_speaker_slot_index(bg3.SPEAKER_PLAYER)

    existing_greetings_ex_lover_node_uuid = '0d1ba1b6-eb42-edd9-d615-0a01b50d9712' # existing node

    existing_greetings_low_approval_node_uuid = '35e88436-e6ac-4812-90e4-98dfcd504eb8' # existing node

    sharran_greetings_lover_node_uuid = '772cf63d-0efb-4f39-9be8-1eebadb5a370'
    sharran_greetings_ex_lover_node_uuid = '3186657b-3026-49ae-a4d5-3eb805e4374a'

    sharran_greetings_lover_low_approval_node_uuid = '8ccc19f8-5a23-4cbd-a9a1-9b03d9b4e91b'
    sharran_greetings_ex_lover_low_approval_node_uuid = '47cae9bb-2d08-4a4d-9e92-791e34d23b53'

    sharran_greetings_node_uuid = 'af8ebb13-4ee6-4f23-84a1-35f76bfe9ae3'
    sharran_greetings_low_approval_node_uuid = 'aa4698c2-fc60-4108-9235-b9fc0312bd7f'

    sharran_greetings_neutral_node_uuid = 'f42546d9-893b-4217-b15b-422e0219853e'

    d.create_alias_dialog_node(
        sharran_greetings_ex_lover_node_uuid,
        sharran_greetings_lover_node_uuid,
        [sleep_together_entry_point_node_uuid],
        root = True,
        checkflags = (
            bg3.flag_group('Global', (
                bg3.flag(Shadowheart_Turned_Away_From_Shar.uuid, False, None),
                bg3.flag(Shadowheart_After_Shadowfell.uuid, True, None),
            )),
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_State_WasPartneredWithShadowheart, True, speaker_idx_tav),
                bg3.flag(bg3.FLAG_Approval_AtLeast_40_For_Sp2, True, speaker_idx_shadowheart)
            )),
        ))

    d.create_alias_dialog_node(
        sharran_greetings_lover_low_approval_node_uuid,
        existing_greetings_low_approval_node_uuid,
        [sleep_together_entry_point_node_uuid],
        root = True,
        checkflags = (
            bg3.flag_group('Global', (
                bg3.flag(Shadowheart_Turned_Away_From_Shar.uuid, False, None),
                bg3.flag(Shadowheart_After_Shadowfell.uuid, True, None),
            )),
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_State_PartneredWithShadowheart, True, speaker_idx_tav),
                bg3.flag(bg3.FLAG_Approval_AtLeast_40_For_Sp2, False, speaker_idx_shadowheart)
            )),
        ))

    d.create_alias_dialog_node(
        sharran_greetings_ex_lover_low_approval_node_uuid,
        existing_greetings_low_approval_node_uuid,
        [sleep_together_entry_point_node_uuid],
        root = True,
        checkflags = (
            bg3.flag_group('Global', (
                bg3.flag(Shadowheart_Turned_Away_From_Shar.uuid, False, None),
                bg3.flag(Shadowheart_After_Shadowfell.uuid, True, None),
            )),
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_State_WasPartneredWithShadowheart, True, speaker_idx_tav),
                bg3.flag(bg3.FLAG_Approval_AtLeast_40_For_Sp2, False, speaker_idx_shadowheart)
            )),
        ))

    d.create_alias_dialog_node(
        sharran_greetings_node_uuid,
        sharran_greetings_lover_node_uuid,
        [sleep_together_entry_point_node_uuid],
        root = True,
        checkflags = (
            bg3.flag_group('Global', (
                bg3.flag(Shadowheart_Turned_Away_From_Shar.uuid, False, None),
                bg3.flag(Shadowheart_After_Shadowfell.uuid, True, None),
            )),
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_Approval_AtLeast_30_For_Sp2, True, speaker_idx_shadowheart),
            )),
        ))

    d.create_alias_dialog_node(
        sharran_greetings_low_approval_node_uuid,
        existing_greetings_low_approval_node_uuid,
        [sleep_together_entry_point_node_uuid],
        root = True,
        checkflags = (
            bg3.flag_group('Global', (
                bg3.flag(Shadowheart_Turned_Away_From_Shar.uuid, False, None),
                bg3.flag(Shadowheart_After_Shadowfell.uuid, True, None),
            )),
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_Approval_AtLeast_10_For_Sp2, False, speaker_idx_shadowheart),
            )),
        ))

    d.create_alias_dialog_node(
        sharran_greetings_neutral_node_uuid,
        bg3.SHADOWHEART_QUESTION_BANK_ROOT_NODE_UUID,
        [sleep_together_entry_point_node_uuid],
        root = True,
        checkflags = (
            bg3.flag_group('Global', (
                bg3.flag(Shadowheart_Turned_Away_From_Shar.uuid, False, None),
                bg3.flag(Shadowheart_After_Shadowfell.uuid, True, None),
            )),
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_Approval_AtLeast_10_For_Sp2, True, speaker_idx_shadowheart),
            )),
        ))

    d.create_standard_dialog_node(
        sharran_greetings_lover_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [sleep_together_entry_point_node_uuid],
        [
            bg3.text_content('h20e0f1e8gc58dg4487gb93bg32fe1e2082fa', 1, '3a00a291-9b21-4181-9ee8-71c73a75505b', custom_sequence_id = '03901dbb-cd0e-49d7-a29d-d313226bde85'),
            bg3.text_content('h6df7d349gb7afg494fg8096g407170de4fc7', 2, '09a69cf2-bec8-4cb2-be45-05b6bd8da21b', custom_sequence_id = '09a69cf2-bec8-4cb2-be45-05b6bd8da21b'),
            bg3.text_content('h53cfdba9ge64fg4f18g9a0eg7144f580ae98', 1, 'ec930886-3e68-4e63-a39d-f0dedabf55fa', custom_sequence_id = 'ec930886-3e68-4e63-a39d-f0dedabf55fa'),
            bg3.text_content('h5be6f751g3b65g421eg8742gfc536fa68662', 1, '85c1c4db-4854-4a59-81b1-cf8bba331e2e', custom_sequence_id = '85c1c4db-4854-4a59-81b1-cf8bba331e2e'),
        ],
        constructor = bg3.dialog_object.GREETING,
        root = True,
        checkflags = (
            bg3.flag_group('Global', (
                bg3.flag(Shadowheart_Turned_Away_From_Shar.uuid, False, None),
                bg3.flag(Shadowheart_After_Shadowfell.uuid, True, None),
            )),
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_State_PartneredWithShadowheart, True, speaker_idx_tav),
                bg3.flag(bg3.FLAG_Approval_AtLeast_40_For_Sp2, True, speaker_idx_shadowheart)
            )),
        ))
    # Lady Shar's blessings be upon you.
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '2.28',
        sharran_greetings_lover_node_uuid,
        (('3.4', '8942c483-83c9-4974-9f47-87cd1dd10828'), (None, '95a53513-08ce-4d80-ae74-e306b51db565')),
        phase_duration = '3.5',
        line_index = 0,
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 64, 1), (1.81, 2, 1)),
            bg3.SPEAKER_PLAYER: ((0.0, 2, None),)
        },
        attitudes = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_R_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, 3),),
            bg3.SPEAKER_PLAYER: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_L_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, 3),)
        }
    )
    t.create_tl_actor_node(bg3.timeline_object.LOOK_AT, bg3.SPEAKER_SHADOWHEART, '0.0', '3.5', (
        t.create_look_at_key(0.0, target = bg3.SPEAKER_PLAYER, bone = 'Head_M', turn_mode = 2, reset = True),
    ),is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.LOOK_AT, bg3.SPEAKER_PLAYER, '0.0', '3.5', (
        t.create_look_at_key(0.0, target = bg3.SPEAKER_SHADOWHEART, bone = 'Head_M', turn_mode = 2, reset = True),
    ), is_snapped_to_end = True)

    # Lady Shar's blessings be upon you.
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '3.9',
        sharran_greetings_lover_node_uuid,
        (('3.8', 'd76eaab3-040b-4871-9c1d-4a8624f37cd2'), (None, '95a53513-08ce-4d80-ae74-e306b51db565')),
        phase_duration = '4.0',
        line_index = 1,
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 2, None),),
            bg3.SPEAKER_PLAYER: ((0.0, 2, None),)
        },
        attitudes = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_R_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, 3),),
            bg3.SPEAKER_PLAYER: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_L_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, 3),)
        }
    )
    t.create_tl_actor_node(bg3.timeline_object.LOOK_AT, bg3.SPEAKER_SHADOWHEART, '0.0', '4.5', (
        t.create_look_at_key(0.0, target = bg3.SPEAKER_PLAYER, bone = 'Head_M', turn_mode = 2, reset = True),
    ),is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.LOOK_AT, bg3.SPEAKER_PLAYER, '0.0', '4.5', (
        t.create_look_at_key(0.0, target = bg3.SPEAKER_SHADOWHEART, bone = 'Head_M', turn_mode = 2, reset = True),
    ), is_snapped_to_end = True)

    # May Lady Shar's blessings be upon you.
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '2.15',
        sharran_greetings_lover_node_uuid,
        (('3.5', 'd76eaab3-040b-4871-9c1d-4a8624f37cd2'), (None, '95a53513-08ce-4d80-ae74-e306b51db565')),
        phase_duration = '4.0',
        line_index = 2,
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 4, None),),
            bg3.SPEAKER_PLAYER: ((0.0, 2, None),)
        },
        attitudes = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_R_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, 3),),
            bg3.SPEAKER_PLAYER: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_L_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, 3),)
        }
    )
    t.create_tl_actor_node(bg3.timeline_object.LOOK_AT, bg3.SPEAKER_SHADOWHEART, '0.0', '4.0', (
        t.create_look_at_key(0.0, target = bg3.SPEAKER_PLAYER, bone = 'Head_M', turn_mode = 2, reset = True),
    ),is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.LOOK_AT, bg3.SPEAKER_PLAYER, '0.0', '4.0', (
        t.create_look_at_key(0.0, target = bg3.SPEAKER_SHADOWHEART, bone = 'Head_M', turn_mode = 2, reset = True),
    ), is_snapped_to_end = True)

    # May the darkness protect you.
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '1.5',
        sharran_greetings_lover_node_uuid,
        (('2.6', '8942c483-83c9-4974-9f47-87cd1dd10828'), (None, '95a53513-08ce-4d80-ae74-e306b51db565')),
        phase_duration = '3.0',
        line_index = 3,
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 4, None),),
            bg3.SPEAKER_PLAYER: ((0.0, 2, None),)
        },
        attitudes = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_R_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, 3),),
            bg3.SPEAKER_PLAYER: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_L_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, 3),)
        }
    )
    t.create_tl_actor_node(bg3.timeline_object.LOOK_AT, bg3.SPEAKER_SHADOWHEART, '0.0', '3.0', (
        t.create_look_at_key(0.0, target = bg3.SPEAKER_PLAYER, bone = 'Head_M', turn_mode = 2, reset = True),
    ),is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.LOOK_AT, bg3.SPEAKER_PLAYER, '0.0', '3.0', (
        t.create_look_at_key(0.0, target = bg3.SPEAKER_SHADOWHEART, bone = 'Head_M', turn_mode = 2, reset = True),
    ), is_snapped_to_end = True)

    node_index = d.get_root_node_index(existing_greetings_ex_lover_node_uuid)
    d.add_root_node(sharran_greetings_low_approval_node_uuid, index = node_index)
    d.add_root_node(sharran_greetings_neutral_node_uuid, index = node_index)
    d.add_root_node(sharran_greetings_node_uuid, index = node_index)
    d.add_root_node(sharran_greetings_lover_low_approval_node_uuid, index = node_index)
    d.add_root_node(sharran_greetings_ex_lover_low_approval_node_uuid, index = node_index)
    d.add_root_node(sharran_greetings_ex_lover_node_uuid, index = node_index)
    d.add_root_node(sharran_greetings_lover_node_uuid, index = node_index)


bg3.add_build_procedure('create_greetings', create_greetings)
bg3.add_build_procedure('create_sharran_greetings', create_sharran_greetings)

from __future__ import annotations

import bg3moddinglib as bg3

from .context import game_assets
from .flags import *


def patch_daughter_tears() -> None:
    ########################################################################################
    # CAMP_Shadowheart_DaughterTears_SD.lsf
    ########################################################################################

    ab = game_assets.get_modded_dialog_asset_bundle('CAMP_Shadowheart_DaughterTears_SD')
    d = bg3.dialog_object(ab.dialog)

    speaker_idx_tav = d.get_speaker_slot_index(bg3.SPEAKER_PLAYER)

    # I wanted to come here. To see if I felt anything that I hadn't done before. Now that I know what I know. Now that I know who I am.
    now_that_i_know_who_i_am_node_uuid = '43bf9478-59e8-9e5e-18b9-e81785abb7bd'
    tav_and_do_you_feel_anything_node_uuid = '023ff9e1-e4b6-4aa5-afbf-38fb6825908c'
    tav_youve_turned_from_shar_node_uuid = 'ac061cd4-b73e-45e0-8c23-242ba7904e72'
    are_eager_to_bow_node_uuid = '7a6ef221-23fb-4483-8382-d7c8c7919025'
    alias_are_eager_to_bow_node_uuid = '4d3d0ccd-5f0e-4d53-92ca-7800ccc3b7c0'
    a_dead_girls_name_node_uuid = '11d19698-dec9-491e-af8d-b2e113a1259f'
    much_times_been_lost_already_node_uuid = '7777fc9a-954d-53d7-1ef9-ea45c9b05235'
    youre_as_much_a_traitor_as_anyone_node_uuid = 'c4921d00-ac42-03b2-1802-0893fca49669'
    shar_node_uuid = '5db9cf18-9c2a-4299-a648-d5e38e4680d8'
    alias_to_response_to_evil_cleric_node_uuid = '0f4c0e44-6999-462f-b6a5-439d3cde7d01'
    jump_back_node_uuid = 'e4fbae26-a1d9-4e36-bccb-b918ddbb2a07'

    d.create_jump_dialog_node(jump_back_node_uuid, now_that_i_know_who_i_am_node_uuid, 2)

    d.set_tagged_text(tav_and_do_you_feel_anything_node_uuid, bg3.text_content('he9498ba4g20c8g491fgaa1eg91ef900f3da7', 1))

    d.delete_all_children_dialog_nodes(tav_youve_turned_from_shar_node_uuid)
    d.add_child_dialog_node(tav_youve_turned_from_shar_node_uuid, alias_are_eager_to_bow_node_uuid)
    d.create_alias_dialog_node(alias_are_eager_to_bow_node_uuid, are_eager_to_bow_node_uuid, [jump_back_node_uuid])

    d.delete_all_children_dialog_nodes(a_dead_girls_name_node_uuid)
    d.add_child_dialog_node(a_dead_girls_name_node_uuid, jump_back_node_uuid)

    d.delete_all_children_dialog_nodes(much_times_been_lost_already_node_uuid)
    d.add_child_dialog_node(much_times_been_lost_already_node_uuid, jump_back_node_uuid)

    d.delete_all_children_dialog_nodes(youre_as_much_a_traitor_as_anyone_node_uuid)
    d.add_child_dialog_node(youre_as_much_a_traitor_as_anyone_node_uuid, jump_back_node_uuid)

    approval_minus_20 = bg3.reaction_object.create_new(files, {bg3.SPEAKER_SHADOWHEART: -20})
    d.set_approval_rating(youre_as_much_a_traitor_as_anyone_node_uuid, approval_minus_20.uuid)

    d.create_standard_dialog_node(
        shar_node_uuid,
        bg3.SPEAKER_PLAYER,
        [alias_to_response_to_evil_cleric_node_uuid],
        bg3.text_content('h7d99100fg9332g4ec3g8ff0gf438bba71a65', 1),
        constructor = bg3.dialog_object.QUESTION,
        approval_rating_uuid = approval_minus_20.uuid,
        checkflags = (
            bg3.flag_group('Tag', (
                bg3.flag(bg3.GOD_SHAR, True, speaker_idx_tav),
            )),
        ))
    d.create_alias_dialog_node(
        alias_to_response_to_evil_cleric_node_uuid,
        youre_as_much_a_traitor_as_anyone_node_uuid,
        [jump_back_node_uuid])

    d.create_jump_dialog_node(jump_back_node_uuid, now_that_i_know_who_i_am_node_uuid, 2)

    # I... I don't know. For so long I only felt what she wanted me to. Now I have to do it for myself, and I feel like I'm drowning.
    i_feel_like_im_drowning_node_uuid = '4839757a-8171-191c-db46-1320a106c0dc'
    a_very_good_thing_node_uuid = 'f1d2fbbc-bdb3-7032-f0fc-0c8b4dd07921'
    tav_give_it_time_node_uuid = '1e2c06d0-673a-c269-212a-1a6e8d527a13'
    tav_remain_silent_node_uuid = '93bd9ea7-bcdf-6321-7a12-fc040c2c9ab1'
    alias_much_times_been_lost_already_node_uuid = '766b1b3c-e033-48b7-b032-89b79608e6b2'
    jump_back2_node_uuid = '485fd3b8-1af9-4c3e-bda0-15991d399e9d'
    d.delete_all_children_dialog_nodes(a_very_good_thing_node_uuid)
    d.add_child_dialog_node(a_very_good_thing_node_uuid, jump_back2_node_uuid)
    d.delete_all_children_dialog_nodes(tav_give_it_time_node_uuid)
    d.add_child_dialog_node(tav_give_it_time_node_uuid, alias_much_times_been_lost_already_node_uuid)
    d.create_alias_dialog_node(alias_much_times_been_lost_already_node_uuid, much_times_been_lost_already_node_uuid, [jump_back2_node_uuid])
    d.create_jump_dialog_node(jump_back2_node_uuid, i_feel_like_im_drowning_node_uuid, 2)
    d.set_tagged_text(tav_remain_silent_node_uuid, bg3.text_content('h47ab25a9g984ag487fg87fcgf53f6f0939a3', 1))

    # this is neede to avoid duplication of the "Give it time" option
    d.set_dialog_flags(tav_give_it_time_node_uuid, checkflags = (
        bg3.flag_group('Tag', (
            bg3.flag(bg3.GOD_SELUNE, False, speaker_idx_tav),
        )),
    ))


    # Loss. Actual loss, not Shar's oblivion. I had my family, for too short a moment. Now they're gone. By my hand.
    loss_actuall_loss_node_uuid = 'b48a38c8-60de-4b3a-a8be-7d6b706d076e'
    they_cant_comfort_me_node_uuid = 'acc73817-c742-2d55-709b-f7cda30d0be4'
    ive_lost_everything_node_uuid = '292498ce-b412-a885-21a6-eb20256a7c96'
    perhaps_not_for_long_node_uuid = '02639c8c-fe85-7160-7180-f8cf59152e6a'
    jump_back3_node_uuid = 'd3151d90-a25d-44d7-9272-c72926888655'

    d.create_jump_dialog_node(jump_back3_node_uuid, loss_actuall_loss_node_uuid, 2)

    d.delete_all_children_dialog_nodes(they_cant_comfort_me_node_uuid)
    d.add_child_dialog_node(they_cant_comfort_me_node_uuid, jump_back3_node_uuid)

    d.delete_all_children_dialog_nodes(ive_lost_everything_node_uuid)
    d.add_child_dialog_node(ive_lost_everything_node_uuid, jump_back3_node_uuid)

    d.delete_all_children_dialog_nodes(perhaps_not_for_long_node_uuid)
    d.add_child_dialog_node(perhaps_not_for_long_node_uuid, jump_back3_node_uuid)


def patch_nightfall() -> None:
    ########################################################################################
    # CAMP_Shadowheart_Nightfall_SD_ROM.lsf
    ########################################################################################

    ab = game_assets.get_modded_dialog_asset_bundle('CAMP_Shadowheart_Nightfall_SD_ROM')
    d = bg3.dialog_object(ab.dialog)

    you_did_well_node_uuid = 'e7724952-12c3-5fb8-8384-2432caad1227'
    d.add_dialog_flags(you_did_well_node_uuid, setflags = (
        bg3.flag_group('Global', (
            bg3.flag(Nightfall_Selune_Desecrated.uuid, True, None),
        )),
    ))


def cine_post_dj_selune_prayer_loop(
    d: bg3.dialog_object,
    t: bg3.timeline_object,
    dialog_node_uuid: str,
    next_dialog_node_uuid: str,
    scenery_selune_statue_actor_uuid: str,
    selune_statue_actor_uuid: str | None,
) -> None:

    # animation daba9ea1-f36c-c8c1-7888-0a6314647b5c
    # animation group 8eaf8ff2-7841-42db-9595-97fe0aa54dce

    if selune_statue_actor_uuid is not None:
        d.create_cinematic_dialog_node(
            dialog_node_uuid,
            [next_dialog_node_uuid],
            checkflags = (
                bg3.flag_group('Global', (
                    bg3.flag(Nightfall_Selune_Desecrated.uuid, True, None),
                )),
            ))
    else:
        d.create_cinematic_dialog_node(
            dialog_node_uuid,
            [next_dialog_node_uuid],
            checkflags = (
                bg3.flag_group('Global', (
                    bg3.flag(Nightfall_Selune_Desecrated.uuid, False, None),
                )),
            ))

    phase_duration = '10.9'
    t.create_new_phase(dialog_node_uuid, phase_duration)

    t.create_tl_non_actor_node(
        bg3.timeline_object.SWITCH_LOCATION,
        '0.0',
        phase_duration,
        (
            t.create_switch_location_event_key('0.0', 3, 'd6c0352c-0d68-44b9-9b19-6e6eeb075683'),
        ),
        is_snapped_to_end = True
    )
    t.create_tl_non_actor_node(
        bg3.timeline_object.SWITCH_STAGE,
        '0.0',
        phase_duration,
        (
            t.create_switch_stage_event_key('0.0', event_uuid = '43285cd8-9b30-4717-a963-4cf0d73302ad'),
        ),
        is_snapped_to_end = True
    )

    # Hide the existing Selune statue
    t.create_tl_actor_node(
        bg3.timeline_object.SHOW_VISUAL,
        scenery_selune_statue_actor_uuid,
        '0.0',
        phase_duration,
        (
            t.create_value_key(time = 0.0, value = False),
        ),
        is_snapped_to_end = True)

    t.create_tl_actor_node(
        bg3.timeline_object.ATTITUDE,
        bg3.SPEAKER_PLAYER,
        '0.0',
        phase_duration,
        (
            t.create_attitude_key('0.0', bg3.ATTITUDE_DIAG_Pose_Stand_R_Forward_01, bg3.ATTITUDE_DIAG_T_Pose),
        ),
        is_snapped_to_end = True)
    t.create_tl_actor_node(
        bg3.timeline_object.ATTITUDE,
        bg3.SPEAKER_SHADOWHEART,
        '0.0',
        phase_duration,
        (
            t.create_attitude_key('0.0', bg3.ATTITUDE_DIAG_Pose_Stand_L_Forward_01, bg3.ATTITUDE_DIAG_T_Pose),
        ),
        is_snapped_to_end = True)
    t.create_tl_actor_node(
        bg3.timeline_object.EMOTION,
        bg3.SPEAKER_PLAYER,
        '0.0',
        phase_duration,
        (
            t.create_emotion_key('0.0', 32),
            t.create_emotion_key('8.5', 32, 2),
        ),
        is_snapped_to_end = True)
    t.create_tl_actor_node(
        bg3.timeline_object.EMOTION,
        bg3.SPEAKER_SHADOWHEART,
        '0.0',
        phase_duration,
        (
            t.create_emotion_key('0.0', 256),
        ),
        is_snapped_to_end = True)
    t.create_tl_actor_node(
        bg3.timeline_object.LOOK_AT,
        bg3.SPEAKER_PLAYER,
        '0.0',
        phase_duration,
        (
            t.create_look_at_key(
                '0.0',
                target = bg3.SPEAKER_SHADOWHEART,
                bone = 'Head_M',
                turn_mode = 2,
                reset = True
            ),
        ),
        is_snapped_to_end = True)
    t.create_tl_actor_node(
        bg3.timeline_object.LOOK_AT,
        bg3.SPEAKER_SHADOWHEART,
        '0.0',
        phase_duration,
        (
            t.create_look_at_key(
                '0.0',
                bone = 'Head_M',
                turn_mode = 2,
                offset = (0.105, 1.677, 11.366),
                reset = True
            ),
        ),
        is_snapped_to_end = True)
    t.create_tl_actor_node(
        bg3.timeline_object.SHOW_WEAPON,
        bg3.SPEAKER_PLAYER,
        '0.0',
        phase_duration,
        (
            t.create_value_key(time = '0.0', value_name = 'ShowWeapon', value_type = 'bool', value = 'False', interpolation_type = 3)
        ),
        is_snapped_to_end = True)
    t.create_tl_actor_node(
        bg3.timeline_object.SHOW_WEAPON,
        bg3.SPEAKER_SHADOWHEART,
        '0.0',
        phase_duration,
        (
            t.create_value_key(time = '0.0', value_name = 'ShowWeapon', value_type = 'bool', value = 'False', interpolation_type = 3)
        ),
        is_snapped_to_end = True)
    t.create_tl_actor_node(
        bg3.timeline_object.PHYSICS,
        bg3.SPEAKER_PLAYER,
        '0.0',
        phase_duration,
        (
            t.create_value_key(time = '0.0', value_name = 'InverseKinematics', value_type = 'bool', value = 'False', interpolation_type = 3)
        ),
        is_snapped_to_end = True)
    t.create_tl_actor_node(
        bg3.timeline_object.PHYSICS,
        bg3.SPEAKER_SHADOWHEART,
        '0.0',
        phase_duration,
        (
            t.create_value_key(time = '0.0', value_name = 'InverseKinematics', value_type = 'bool', value = 'False', interpolation_type = 3)
        ),
        is_snapped_to_end = True)

    # ca3baf92-e461-4229-8822-614a7d9c1971 --> Tav actor
    # ac8826d8-ddb4-46f3-9bdd-ca6cea70f73e --> Shadowheart actor

    # cameras
    # ca37294b-681b-4ae4-bcce-72541d827157

    # 80a7fed2-0492-4bd4-b9ca-80359eac65d9 Tav         --> Tav
    # b3f9b0b9-0652-4599-9ae0-4a4b421e76ce Tav         --> Tav
    # f9cccdb9-0aa8-4a7b-b2e3-4fe68a512bee Tav         --> Tav
    # 61f85839-b74b-4aa9-b651-2cff24788b2d Tav         --> Tav
    # 1164eb14-57d6-4b63-b76a-bb5efc0e0607 Tav         --> Tav

    # 7920525e-55c0-48cf-bade-69ade1388499 Shadowheart --> Shadowheart
    # b13dfa40-0455-41bb-83fa-bcc1ef7d9ce1 Shadowheart --> Shadowheart
    # bf8da42b-a7a5-4091-819d-fe7013a7de77 Shadowheart --> Shadowheart

    # c5566219-0808-434f-b228-3d7ec87b65e7 Shadowheart --> Tav

    # 19f4fa29-832b-49e1-b8a5-de8f8b1d2b13 Tav         --> Shadowheart
    # 1dc34381-5e7c-4e9a-bb18-d7f2af6b8f18 Tav         --> Shadowheart
    # 80559072-95e0-4804-886d-13933a9d9dca Tav         --> Shadowheart

    camera0 = 'ca37294b-681b-4ae4-bcce-72541d827157'
    camera1 = 'ec978200-bbbb-4c97-ac87-f231fe4e5344'
    camera2 = 'f9cccdb9-0aa8-4a7b-b2e3-4fe68a512bee'

    t.create_tl_camera_dof(
        camera1,
        '0.0',
        phase_duration,
        (
            (
                t.create_value_key(time = '0.0', value = '2.3', value_type = 'float', interpolation_type = 0),
            ),
            (
                t.create_value_key(time = '0.0', value = '18.0', value_type = 'float', interpolation_type = 0),
            ),
            (
                t.create_value_key(time = '0.0', value = '1.0', value_type = 'float', interpolation_type = 0),
            ),
            (), (), (), ()
        ),
        is_snapped_to_end = True)
    t.create_tl_camera_fov(
        camera1,
        '0.0',
        '8.0',
        (
            t.create_value_key(time = '0.0', value_name = 'FoV', value = '32.0', value_type = 'float', interpolation_type = 0),
            t.create_value_key(time = '7.0', value_name = 'FoV', value = '30.0', value_type = 'float', interpolation_type = 0),
        ))
    t.create_tl_transform(
        camera1,
        '0.0',
        phase_duration,
        (
            (
                # + right; - left
                #t.create_value_key(time = '0.0', value = '0.05931377', value_type = 'float', interpolation_type = 0),
                t.create_value_key(time = '0.0', value = '0.07', value_type = 'float', interpolation_type = 0),
            ),
            (
                t.create_value_key(time = '0.0', value = '1.4', value_type = 'float', interpolation_type = 0),
            ),
            (
                # + forward; - backward
                t.create_value_key(time = '0.0', value = '6.5', value_type = 'float', interpolation_type = 0),
            ),
            (
                # tilt down
                t.create_value_key(time = '0.0', value = bg3.euler_to_quaternion(10.0, 0.0, 0.0, sequence = 'xyz'), interpolation_type = 0),
            ),
            (), ()
        ))

    t.create_tl_transform(
        bg3.SPEAKER_SHADOWHEART,
        '0.0',
        phase_duration,
        (
            (), (), (),
            (
                t.create_value_key(time = '0.0', value = bg3.euler_to_quaternion(179.9, 0.0, 0.0, sequence = 'yxz'), interpolation_type = 0),
            ),
            (), ()
        ),
        is_snapped_to_end = True)
    t.create_tl_transform(
        bg3.SPEAKER_PLAYER,
        '0.0',
        phase_duration,
        (
            (), (),
            (
                t.create_value_key(time = '0.0', value = '6.0', value_type = 'float', interpolation_type = 0),
            ),
            (), (), ()
        ),
        is_snapped_to_end = True)

    t.create_tl_animation(
        bg3.SPEAKER_SHADOWHEART,
        '0.0',
        phase_duration,
        # HEL_F_Rig_SCENE_SHA_NSPrison_OMSH_PrayingShar_rfix_LOOP_SH
        #'76b4bff3-d290-1ad2-791f-8e18cf0cd874',
        # HEL_F_Rig_SCENE_SHA_NSPrison_OMSH_PrayingShar_LOOP
        'dccfaecd-7399-e328-1270-f07fcf47ad10',
        #'8eaf8ff2-7841-42db-9595-97fe0aa54dce',
        'a7891437-8ba1-4ffa-80a4-fbf3d434b01e',
        continuous = True,
        fade_in = 0.0,
        fade_out = 0.0,
    )

    if selune_statue_actor_uuid is not None:
        # Bloody materials
        t.create_tl_material(
            selune_statue_actor_uuid,
            '0.0',
            phase_duration,
            '749a21e9-fb0f-4b57-8459-541dbcb8e458',
            (
                t.create_material_parameter('Opacity', (t.create_value_key(time = 0.0, value = 1.0, interpolation_type = 2),)),
                t.create_material_parameter('MaskContrast', (t.create_value_key(time = 0.0, value = 0.5, interpolation_type = 2),)),
            ),
            (
                t.create_value_key(time = 0.0, value = True),
            ),
            is_continuous = True,
            is_snapped_to_end = True,
            is_overlay = True,
            overlay_priority = 1)
        t.create_tl_material(
            selune_statue_actor_uuid,
            '0.0',
            phase_duration,
            '6655b2b4-d20e-4a51-9043-ee0c2b59bfae',
            (
                t.create_material_parameter('MaskRadius', (t.create_value_key(time = 0.0, value = 0.25, interpolation_type = 2),)),
            ),
            (
                t.create_value_key(time = 0.0, value = True),
            ),
            is_continuous = True,
            is_snapped_to_end = True,
            is_overlay = True)
        t.create_tl_material(
            selune_statue_actor_uuid,
            '0.0',
            phase_duration,
            '9f54e010-7594-4ed2-b055-f06f0216e647',
            (
                t.create_material_parameter('MaskRadius', (t.create_value_key(time = 0.0, value = 0.25, interpolation_type = 2),)),
            ),
            (
                t.create_value_key(time = 0.0, value = True),
            ),
            is_continuous = True,
            is_snapped_to_end = True,
            is_overlay = True,
            overlay_priority = 5)

    t.create_tl_shot(camera1, '0.0', '8.0')
    # 80a7fed2-0492-4bd4-b9ca-80359eac65d9 Tav         --> Tav
    # b3f9b0b9-0652-4599-9ae0-4a4b421e76ce Tav         --> Tav
    # f9cccdb9-0aa8-4a7b-b2e3-4fe68a512bee Tav         --> Tav
    # 61f85839-b74b-4aa9-b651-2cff24788b2d Tav         --> Tav
    # 1164eb14-57d6-4b63-b76a-bb5efc0e0607 Tav         --> Tav
    t.create_tl_shot(camera2, '8.0', '10.0')
    t.create_tl_transform(
        camera1,
        '8.0',
        phase_duration,
        (
            (
                # + right; - left
                #t.create_value_key(time = '0.0', value = '0.05931377', value_type = 'float', interpolation_type = 0),
                t.create_value_key(time = '0.0', value = '0.07', value_type = 'float', interpolation_type = 0),
            ),
            (
                t.create_value_key(time = '0.0', value = '1.4', value_type = 'float', interpolation_type = 0),
            ),
            (
                # + forward; - backward
                t.create_value_key(time = '0.0', value = '6.5', value_type = 'float', interpolation_type = 0),
            ),
            (
                # tilt down
                t.create_value_key(time = '0.0', value = bg3.euler_to_quaternion(7.0, 0.0, 0.0, sequence = 'xyz'), interpolation_type = 0),
            ),
            (), ()
        ),
        is_snapped_to_end = True)
    t.create_tl_camera_fov(
        camera1,
        '8.0',
        phase_duration,
        (
            t.create_value_key(time = '8.0', value_name = 'FoV', value = '35.0', value_type = 'float', interpolation_type = 0),
        ),
        is_snapped_to_end = True)
    t.create_tl_shot(camera1, '10.0', phase_duration, is_snapped_to_end = True)


def cine_post_dj_selune_prayer_end(
    d: bg3.dialog_object,
    t: bg3.timeline_object,
    dialog_node_uuid: str,
    next_dialog_node_uuid: str,
    called_her: bool
) -> None:
    d.create_cinematic_dialog_node(
        dialog_node_uuid,
        [next_dialog_node_uuid])

    camera1 = 'ec978200-bbbb-4c97-ac87-f231fe4e5344'

    #phase_duration = '7.33' if called_her else '10.3'
    phase_duration = '3.5' if called_her else '8.5'
    t.create_new_phase(dialog_node_uuid, phase_duration)

    t.create_tl_transform(
        bg3.SPEAKER_SHADOWHEART,
        '0.0',
        phase_duration,
        (
            (), (), (),
            (
                t.create_value_key(time = '0.0', value = bg3.euler_to_quaternion(179.9, 0.0, 0.0, sequence = 'yxz'), interpolation_type = 0),
            ),
            (), ()
        ),
        is_snapped_to_end = True)
    t.create_tl_transform(
        bg3.SPEAKER_PLAYER,
        '0.0',
        phase_duration,
        (
            (), (),
            (
                t.create_value_key(time = '0.0', value = '6.0', value_type = 'float', interpolation_type = 0),
            ),
            (), (), ()
        ),
        is_snapped_to_end = True)

    t.create_tl_camera_fov(
        camera1,
        '0.0',
        phase_duration,
        (
            t.create_value_key(time = '8.0', value_name = 'FoV', value = '35.0', value_type = 'float', interpolation_type = 0),
        ),
        is_snapped_to_end = True)
    t.create_tl_transform(
        camera1,
        '0.0',
        phase_duration,
        (
            (
                # + right; - left
                #t.create_value_key(time = '0.0', value = '0.05931377', value_type = 'float', interpolation_type = 0),
                t.create_value_key(time = '0.0', value = '0.07', value_type = 'float', interpolation_type = 0),
            ),
            (
                t.create_value_key(time = '0.0', value = '1.4', value_type = 'float', interpolation_type = 0),
            ),
            (
                # + forward; - backward
                t.create_value_key(time = '0.0', value = '6.5', value_type = 'float', interpolation_type = 0),
            ),
            (
                # tilt down
                t.create_value_key(time = '0.0', value = bg3.euler_to_quaternion(7.0, 0.0, 0.0, sequence = 'xyz'), interpolation_type = 0),
            ),
            (), ()
        ),
        is_snapped_to_end = True)

    if called_her:
        t.create_tl_animation(
            bg3.SPEAKER_SHADOWHEART,
            '0.0',
            phase_duration,
            # HEL_F_Rig_SCENE_SHA_NSPrison_OMSH_PrayingShar_OUT_Angry
            '091246fb-96bc-777b-e4c8-30d32b247ced',
            'a7891437-8ba1-4ffa-80a4-fbf3d434b01e',
            fade_in = 1.0,
            fade_out = 2.0,
        )
    else:
        t.create_tl_animation(
            bg3.SPEAKER_SHADOWHEART,
            '0.0',
            '5.0',
            # HEL_F_Rig_SCENE_SHA_NSPrison_OMSH_PrayingShar_LOOP
            'dccfaecd-7399-e328-1270-f07fcf47ad10',
            'a7891437-8ba1-4ffa-80a4-fbf3d434b01e',
            continuous = True,
            fade_in = 0.5,
            fade_out = 0.5,
        )
        t.create_tl_animation(
            bg3.SPEAKER_SHADOWHEART,
            '5.0',
            phase_duration,
            # HEL_F_Rig_SCENE_SHA_NSPrison_OMSH_PrayingShar_OUT
            '74a00837-f4cf-2781-d768-95f8ee64cab2',
            'a7891437-8ba1-4ffa-80a4-fbf3d434b01e',
            fade_in = 0.5,
            fade_out = 2.0,
            enable_root_motion = True,
        )


def create_daughter_tears_entry_point() -> None:
    ###########################################################################
    # Dialog: CAMP_Shadowheart_DaughterTears_SD.lsf
    # if hugs weren't enabled in act 2, this enables them in act 3.
    # If parents saved, hugs are always enabled.
    # If parents moonmoted, Tav snould embrace her to enable hugs.
    # Also this adds an ex-DJ entry point
    ###########################################################################

    ab = game_assets.get_modded_dialog_asset_bundle('CAMP_Shadowheart_DaughterTears_SD')
    d = bg3.dialog_object(ab.dialog)
    t = bg3.timeline_object(ab.timeline, d)

    speaker_idx_shadowheart = d.get_speaker_slot_index(bg3.SPEAKER_SHADOWHEART)
    speaker_idx_tav = d.get_speaker_slot_index(bg3.SPEAKER_PLAYER)

    shadowheart_hugs_enabled_group = bg3.flag_group('Object', (
        bg3.flag(Shadowheart_State_Hugs_Enabled.uuid, True, speaker_idx_shadowheart),
        bg3.flag(Shadowheart_State_Smiles_When_Hugged.uuid, True, speaker_idx_shadowheart),
    ))

    # 'Embrace her', parents not saved
    d.add_dialog_flags('315b082c-97cb-34be-3e9b-7b70c9b79b65', setflags=[shadowheart_hugs_enabled_group])
    d.add_dialog_flags('39baeaf3-3d49-d4af-d83f-f9bf40455bbe', setflags=[shadowheart_hugs_enabled_group])
    d.add_dialog_flags('602bfbe9-c61b-56d9-5c73-3d7086a0c0e1', setflags=[shadowheart_hugs_enabled_group])
    d.add_dialog_flags('6bd93424-91db-d2fc-b0f4-41a11b8535b1', setflags=[shadowheart_hugs_enabled_group])
    d.add_dialog_flags('d75095a4-ecad-4899-f5c5-99fe0a896fb4', setflags=[shadowheart_hugs_enabled_group])
    d.add_dialog_flags('ec90059f-b14f-2344-2a6a-1c450374f488', setflags=[shadowheart_hugs_enabled_group])

    # The following creates a new entry point to the Daughter's Tears scene
    # This new entry point sets flags:
    # * Shadowheart's irregular behavior flag (after the Chamber of Loss) is reset
    # * if parents are saved, hugs are enabled

    selunite_original_root_node_uuid = '2f265d42-c7b4-411d-9379-abe173de325a' # existing node
    new_entry_point_node_uuid = '1273c14a-d71f-4e36-9ba2-3ab50eefc7e9'
    selune_parents_saved_node_uuid = '9dd3ad2c-8b0d-4fb5-bb81-e96a94635619'
    selune_parents_killed_node_uuid = '433e9cdd-dd86-4cd6-a3b2-900713ff74a7'
    shar_parents_saved_node_uuid = '0c9f93bc-9fdf-4a25-821a-fd14869c3c4e'

    ex_dj_prayer_selune_intact_node_uuid = '06f6c262-d53e-48cf-8860-18e2f90f0f4b'
    ex_dj_prayer_selune_desecrated_node_uuid = 'ea17032d-426b-455e-aa79-ad3de6e85295'
    ex_dj_prayer_out_called_her_node_uuid = 'eba743f8-9596-40e7-a64e-b8d18e28a827'
    ex_dj_prayer_out_node_uuid = '2e1e43ce-3cec-42f1-9178-5241889ebba4'

    d.create_standard_dialog_node(
        new_entry_point_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [selune_parents_saved_node_uuid, selune_parents_killed_node_uuid, shar_parents_saved_node_uuid],
        None,
        constructor = bg3.dialog_object.GREETING,
        root = True,
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(Shadowheart_After_Parents_Crisis.uuid, False, speaker_idx_shadowheart),
                bg3.flag(Shadowheart_Cried_After_Parents.uuid, True, speaker_idx_shadowheart),
            )),
        )
    )
    d.create_standard_dialog_node(
        selune_parents_saved_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [selunite_original_root_node_uuid],
        None,
        checkflags = (
            bg3.flag_group('Global', (
                bg3.flag(bg3.FLAG_ORI_Shadowheart_State_RejectShar_SavedParents, True, None),
            )),
        ),
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(Shadowheart_State_Hugs_Enabled.uuid, True, speaker_idx_shadowheart),
                bg3.flag(Shadowheart_State_Smiles_When_Hugged.uuid, True, speaker_idx_shadowheart),
            )),
        ))
    d.create_standard_dialog_node(
        selune_parents_killed_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [selunite_original_root_node_uuid],
        None,
        checkflags = (
            bg3.flag_group('Global', (
                bg3.flag(bg3.FLAG_ORI_Shadowheart_State_RejectShar_KilledParents, True, None),
            )),
        ))
    d.create_standard_dialog_node(
        shar_parents_saved_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [ex_dj_prayer_selune_desecrated_node_uuid, ex_dj_prayer_selune_intact_node_uuid],
        None,
        checkflags = (
            bg3.flag_group('Global', (
                bg3.flag(bg3.FLAG_ORI_Shadowheart_State_Shar_SavedParents, True, None),
            )),
        ))
    d.remove_dialog_attribute(selunite_original_root_node_uuid, 'Root')
    d.set_dialog_attribute(selunite_original_root_node_uuid, 'constructor', 'TagAnswer')
    d.remove_root_node(selunite_original_root_node_uuid)
    d.add_root_node(new_entry_point_node_uuid)

    ###########################################################################
    # Ex-DJ entry point
    ###########################################################################

    selune_statue_actor_uuid = '3a4bcda8-f0cc-481f-b78c-b8e75ae9c542'
    scenery_selune_statue_actor_uuid = '6a1de5c8-c483-479b-86bf-f84f1bfa8fad'

    game_assets.append_dependency_to_timeline('reallyshadowheart_camp_shadowheart_daughtertears_sd', selune_statue_actor_uuid)

    t.create_scene_actor(
        selune_statue_actor_uuid,
        {
            'ActorTypeId:FixedString': 'scenery',
            'ActorType:uint8': '3',
            'DefaultStepOutDelay:float': '0.77490157',
        },
        scale = 0.5,
        position = (0.05931377, 0.324894, 10.9867))
    t.create_scene_actor(
        scenery_selune_statue_actor_uuid,
        {
            'ActorTypeId:FixedString': 'scenery',
            'ActorType:uint8': '0',
            'DefaultStepOutDelay:float': '0.6672811',
        },
        scale = 0.5,
        position = (0.05931377, 0.324894, 10.9867))


    # Hide the existing Selune statue on Selunite branch of the cutscene
    phase = t.use_existing_phase(selunite_original_root_node_uuid)
    t.create_tl_actor_node(
        bg3.timeline_object.SHOW_VISUAL,
        scenery_selune_statue_actor_uuid,
        '0.0',
        phase.duration,
        (
            t.create_value_key(time = 0.0, value = False),
        ),
        is_snapped_to_end = True)


    tav_questions_node_uuid = 'c5804f51-0972-4a18-9780-d0f7c00aafc5'
    shadowheart_node_uuid = '5266cc45-b9f1-439e-9bef-d0a4f8ad7f6a'
    sha_jenevelle_node_uuid = 'be46fcc7-7f72-4500-b463-5ef0db5c5f6b'
    jenevelle_node_uuid = 'd0ddc2f4-506c-4469-a7d7-637827dbb570'
    wait_patiently_node_uuid = 'f24e4f23-8797-4a3c-b452-21114074565f'
    turn_around_and_leave_node_uuid = '5dc04555-e5dd-46f5-86d2-5038736704ff'

    cine_post_dj_selune_prayer_loop(d, t, ex_dj_prayer_selune_desecrated_node_uuid, tav_questions_node_uuid, scenery_selune_statue_actor_uuid, selune_statue_actor_uuid)
    cine_post_dj_selune_prayer_loop(d, t, ex_dj_prayer_selune_intact_node_uuid, tav_questions_node_uuid, scenery_selune_statue_actor_uuid, None)

    d.create_standard_dialog_node(
        tav_questions_node_uuid,
        bg3.SPEAKER_PLAYER,
        [
            shadowheart_node_uuid,
            sha_jenevelle_node_uuid,
            jenevelle_node_uuid,
            wait_patiently_node_uuid,
            turn_around_and_leave_node_uuid,
        ],
        None)

    # Shadowheart?
    d.create_standard_dialog_node(
        shadowheart_node_uuid,
        bg3.SPEAKER_PLAYER,
        [ex_dj_prayer_out_called_her_node_uuid],
        bg3.text_content('hd3542486g7197g41c1g840bgdebcac83aae9', 1),
        constructor = bg3.dialog_object.QUESTION,
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(Shadowheart_State_Hugs_Enabled.uuid, True, speaker_idx_shadowheart),
                bg3.flag(Shadowheart_State_Smiles_When_Hugged.uuid, True, speaker_idx_shadowheart),
            )),
        ))

    # Sha... Jenevelle?
    d.create_standard_dialog_node(
        sha_jenevelle_node_uuid,
        bg3.SPEAKER_PLAYER,
        [ex_dj_prayer_out_called_her_node_uuid],
        bg3.text_content('h0c3be373g5b8dg474cg9d83gb5c0541854da', 1),
        constructor = bg3.dialog_object.QUESTION,
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(Shadowheart_State_Hugs_Enabled.uuid, True, speaker_idx_shadowheart),
                bg3.flag(Shadowheart_State_Smiles_When_Hugged.uuid, True, speaker_idx_shadowheart),
            )),
        ))

    # Jenevelle?
    d.create_standard_dialog_node(
        jenevelle_node_uuid,
        bg3.SPEAKER_PLAYER,
        [ex_dj_prayer_out_called_her_node_uuid],
        bg3.text_content('h295f5410g87edg4ae8gacd9g0435674745c5', 1),
        constructor = bg3.dialog_object.QUESTION,
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(Shadowheart_State_Hugs_Enabled.uuid, True, speaker_idx_shadowheart),
                bg3.flag(Shadowheart_State_Smiles_When_Hugged.uuid, True, speaker_idx_shadowheart),
            )),
        ))

    # Wait patiently.
    d.create_standard_dialog_node(
        wait_patiently_node_uuid,
        bg3.SPEAKER_PLAYER,
        [ex_dj_prayer_out_node_uuid],
        bg3.text_content('h3a7c10c6g7b25g4695ga371g0a9504a60d9a', 1),
        constructor = bg3.dialog_object.QUESTION,
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(Shadowheart_State_Hugs_Enabled.uuid, True, speaker_idx_shadowheart),
                bg3.flag(Shadowheart_State_Smiles_When_Hugged.uuid, True, speaker_idx_shadowheart),
            )),
        ))

    # Turn around and leave. Let her deal with that on her own.
    d.create_standard_dialog_node(
        turn_around_and_leave_node_uuid,
        bg3.SPEAKER_PLAYER,
        [],
        bg3.text_content('h8d2f7d9ag2829g4d51gb7e1g026f4125b1d1', 1),
        constructor = bg3.dialog_object.QUESTION,
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(Shadowheart_Rejects_Proposal.uuid, True, speaker_idx_shadowheart),
            )),
        ),
        end_node = True)

    cine_post_dj_selune_prayer_end(d, t, ex_dj_prayer_out_called_her_node_uuid, selunite_original_root_node_uuid, True)
    cine_post_dj_selune_prayer_end(d, t, ex_dj_prayer_out_node_uuid, selunite_original_root_node_uuid, False)


bg3.add_build_procedure('patch_daughter_tears', patch_daughter_tears)
bg3.add_build_procedure('create_post_dj_opening', create_daughter_tears_entry_point)

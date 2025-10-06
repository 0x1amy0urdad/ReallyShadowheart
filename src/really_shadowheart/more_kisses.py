from __future__ import annotations

import bg3moddinglib as bg3

from .context import game_assets

###############################################################
# This adds Lae'zel's kiss
###############################################################

def add_laezel_kiss_bt2_animation(d: bg3.dialog_object, t: bg3.timeline_object, dialog_node_uuid: str) -> None:

    # t = bg3.timeline_object(files.get_file('Gustav', 'Public/GustavDev/Timeline/Generated/ShadowHeart_InParty2_Nested_ShadowheartKiss.lsf'), d)

    #slot_idx_shadowheart = d.get_speaker_slot_index(bg3.SPEAKER_SHADOWHEART)
    #slot_idx_tav = d.get_speaker_slot_index(bg3.SPEAKER_PLAYER)

    phase_duration = '33.14'
    t.create_new_phase(dialog_node_uuid, phase_duration)

    t.create_tl_actor_node(bg3.timeline_object.ATTITUDE, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.ATTITUDE, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (), is_snapped_to_end = True)

    t.create_tl_actor_node(bg3.timeline_object.EMOTION, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.EMOTION, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (), is_snapped_to_end = True)

    t.create_tl_actor_node(bg3.timeline_object.LOOK_AT, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_look_at_key(
            0.0,
            target = bg3.SPEAKER_PLAYER,
            bone = 'Head_M',
            turn_mode = 3,
            turn_speed_multiplier = 0.3,
            head_turn_speed_multiplier = 0.05,
            weight = 1.0,
            safe_zone_angle = 80.0,
            head_safe_zone_angle = 80.0,
            look_at_mode = 1,
            eye_look_at_bone = 'Head_M'),
        t.create_look_at_key(
            32.14,
            target = bg3.SPEAKER_PLAYER,
            bone = 'Head_M',
            turn_mode = 3,
            turn_speed_multiplier = 0.3,
            head_turn_speed_multiplier = 0.3,
            weight = 0.0,
            reset = True,
            eye_look_at_bone = 'Head_M'),
    ), is_snapped_to_end = True)

    t.create_tl_actor_node(bg3.timeline_object.LOOK_AT, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        t.create_look_at_key(
            0.0,
            target = bg3.SPEAKER_SHADOWHEART,
            bone = 'Head_M',
            turn_mode = 3,
            turn_speed_multiplier = 0.3,
            head_turn_speed_multiplier = 0.05,
            weight = 1.0,
            head_safe_zone_angle = 80.0,
            eye_look_at_bone = 'Head_M'),
        t.create_look_at_key(
            0.86,
            target = bg3.SPEAKER_SHADOWHEART,
            bone = 'Head_M',
            turn_mode = 3,
            turn_speed_multiplier = 0.3,
            head_turn_speed_multiplier = 0.05,
            weight = 1.0,
            safe_zone_angle = 80.0,
            head_safe_zone_angle = 80.0,
            look_at_mode = 1,
            eye_look_at_bone = 'Head_M'),
        t.create_look_at_key(
            32.14,
            target = bg3.SPEAKER_SHADOWHEART,
            bone = 'Head_M',
            turn_mode = 3,
            turn_speed_multiplier = 0.3,
            head_turn_speed_multiplier = 0.05,
            weight = 0.0,
            head_safe_zone_angle = 80.0,
            reset = True,
            eye_look_at_bone = 'Head_M'),
    ), is_snapped_to_end = True)

    t.create_tl_actor_node(bg3.timeline_object.EMOTION, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        t.create_emotion_key(0.0, 64),
        t.create_emotion_key(14.5, 2, variation = 1),
        t.create_emotion_key(23.9, 2, variation = 2),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.EMOTION, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_emotion_key(0.0, 64),
        t.create_emotion_key(6.5, 2, is_sustained = False),
        t.create_emotion_key(7.0, 64),
        t.create_emotion_key(24.8, 2, variation = 1),
    ), is_snapped_to_end = True)

    t.create_tl_actor_node(bg3.timeline_object.LOOK_AT, bg3.PEANUT_SLOT_0, '0.0', phase_duration, (), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.LOOK_AT, bg3.PEANUT_SLOT_1, '0.0', phase_duration, (), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.LOOK_AT, bg3.PEANUT_SLOT_2, '0.0', phase_duration, (), is_snapped_to_end = True)

    # Hide helmets
    t.create_tl_show_armor(bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        (
            t.create_value_key(time = 0.0, value = False, interpolation_type = 0),
            t.create_value_key(time = phase_duration, interpolation_type = 0)
        ),
        (), (), (), (), (), (), (), (), (), ()
    ), is_snapped_to_end = True)
    t.create_tl_show_armor(bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        (
            t.create_value_key(time = 0.0, value = False, interpolation_type = 0),
            t.create_value_key(time = phase_duration, interpolation_type = 0)
        ),
        (), (), (), (), (), (), (), (), (), ()
    ), is_snapped_to_end = True)

    t.create_tl_actor_node(bg3.timeline_object.SOUND, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_sound_event_key(13.48, sound_event_id = '6ffc5af2-ae64-48a2-9068-4996d4cdceab', sound_object_index = 4),
        t.create_sound_event_key(15.07, sound_event_id = 'aa8db628-8c78-4632-ab7a-2ac210393e93', sound_object_index = 4),
        t.create_sound_event_key(21.22, sound_event_id = '90a31a12-9f32-47e1-899e-cdced0705f27', sound_object_index = 4),
        t.create_sound_event_key(21.33, sound_event_id = '6ffc5af2-ae64-48a2-9068-4996d4cdceab', sound_object_index = 4),
        t.create_sound_event_key(21.97, sound_event_id = 'ffbbbd57-5c31-444d-bc3a-c3d14df0be53', sound_object_index = 4),
        t.create_sound_event_key(23.88, sound_event_id = 'ffbbbd57-5c31-444d-bc3a-c3d14df0be53', sound_object_index = 4),
        t.create_sound_event_key(25.15, sound_event_id = '55647a99-7f83-42b4-8493-3ab9b58d824f', sound_object_index = 4),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.SOUND, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        t.create_sound_event_key(0.61, sound_event_id = 'f728f472-57d5-45ce-be9e-6e2f927bee0d', sound_object_index = 4),
    ), is_snapped_to_end = True)

    t.create_tl_actor_node(bg3.timeline_object.PHYSICS, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        t.create_value_key(time = 0.0, interpolation_type = 3, value_name = 'InverseKinematics', value = False),
        t.create_value_key(time = 29.44, interpolation_type = 3),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.PHYSICS, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_value_key(time = 0.0, interpolation_type = 3, value_name = 'InverseKinematics', value = False),
        t.create_value_key(time = 29.44, interpolation_type = 3),
    ), is_snapped_to_end = True)

    t.create_tl_transform(bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 0.0),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 0.0),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 0.38),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = (0.0, 0.0, 0.0, 1.0)),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 1),
        ),
        (),
    ), is_snapped_to_end = True)
    t.create_tl_transform(bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = -0.17),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 0.0),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = -1.06),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = (0.0, 1.0, 0.0, 0.0)),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 1),
        ),
        (),
    ), is_snapped_to_end = True)

    t.create_tl_animation(
        bg3.SPEAKER_SHADOWHEART, '0.0', '32.14',
        '8e459a21-cee9-71e8-258f-9aacc0e71417',
        '4587fb8c-2427-45a9-a4a2-4a33ca04cb1e',
        fade_in = 0.0,
        fade_out = 2.0,
        is_snapped_to_end = True)
    t.create_tl_animation(
        bg3.SPEAKER_PLAYER, '0.0', '32.14',
        'ff4e02ff-9235-44a2-a885-c87ca5797309',
        'a2ca8e61-fbc1-48bb-b9a4-fef4c8c3682d',
        fade_in = 0.0,
        fade_out = 0.0,
        is_snapped_to_end = True)

    # Cameras
    # fb91b3e2-b1b9-47d5-8478-659cececad9b SH -> Tav 0.3067965
    # befcdee8-6352-4be6-b2ea-23c2ac0dfe60 SH -> Tav 0.66813564
    # 89eeac49-0759-420d-8f99-3b76a8b2b7e8 Tav -> SH 0.47918946
    # 18c5bd4f-c066-4c52-8cdb-d8bbe1d8034e Tav -> SH 0.0042237616
    # cb95fcb5-efd7-48f4-9352-5eaeb3e44274 Tav -> Tav 0.024341565
    # 64edf86f-1d72-47fd-b908-a444cadb2fc3 Tav -> Tav 0.5685232
    # 99480a46-e5ff-4101-ab73-d0ce43403c57 Tav -> SH 0.35174415
    # a43f207a-ed78-4acf-9815-9103e41577d0 SH -> Tav 0.26702476
    # 1df3c3cc-13c4-4876-b76f-ad6dd2759185 Tav -> SH 0.58995944
    # c3eb0d95-3e47-4b67-9dd2-036c93fb0a44 Tav -> Tav 0.6237983
    # 33a18aa0-5996-441f-940b-1179758c5834 Tav -> SH 0.68747216
    # 9de43fdc-0612-4161-9f37-d975d5ca409c SH -> Tav 0.4817774
    # 7c0cf47f-81b5-4949-bf43-ae0fb233324f SH -> SH 0.10044252

    # Camera shot 1
    # 563a9cc6-a183-456e-b3ea-c196a07711b8 Tav -> SH
    # c4f6737b-2cee-4f55-8cc4-0766bc4d2f97 SH -> Tav ff9136ca-e96e-4709-8d3c-f4a6d0de5690
    # t.create_tl_camera_fov('89eeac49-0759-420d-8f99-3b76a8b2b7e8', 0.0, 3.18, (
    #     t.create_value_key(time = 4.2, value_name = 'FoV', value = 28.0, interpolation_type = 2),
    # ))
    # t.create_tl_transform('89eeac49-0759-420d-8f99-3b76a8b2b7e8', 0.0, 3.18, (
    #     (
    #         t.create_value_key(time = 0.0, interpolation_type = 5, value = -0.6),
    #         t.create_value_key(time = '3.18', interpolation_type = 5, value = -0.8),
    #     ),
    #     (
    #         t.create_value_key(time = 0.0, interpolation_type = 5, value = 1.6),
    #     ),
    #     (
    #         t.create_value_key(time = 0.0, interpolation_type = 5, value = 0.6),
    #         t.create_value_key(time = '3.18', interpolation_type = 5, value = 0.4),
    #     ),
    #     (
    #         t.create_value_key(time = 0.0, interpolation_type = 5, value = bg3.euler_to_quaternion(165.0, 0.0, 0.0, sequence = 'yxz')),
    #         t.create_value_key(time = '3.18', interpolation_type = 5, value = bg3.euler_to_quaternion(157.0, 0.0, 0.0, sequence = 'yxz')),
    #     ),
    #     (),
    #     (),
    # ))
    t.create_tl_shot('9de43fdc-0612-4161-9f37-d975d5ca409c', '0.0', '3.18')

    # Camera shot 2
    # 6f87ec93-2f4e-4ff1-8a0f-56a2c50546d7 Tav -> SH
    t.create_tl_camera_fov('89eeac49-0759-420d-8f99-3b76a8b2b7e8', '3.18', '11.73', (
        t.create_value_key(time = '3.18', value_name = 'FoV', value = 40.0, interpolation_type = 2),
        t.create_value_key(time = '11.73', value_name = 'FoV', value = 25.0, interpolation_type = 2),
    ))
    t.create_tl_transform('89eeac49-0759-420d-8f99-3b76a8b2b7e8', '3.18', '11.73', (
        (
            t.create_value_key(time = '3.18', interpolation_type = 5, value = -0.6),
            t.create_value_key(time = '11.73', interpolation_type = 5, value = -0.8),
        ),
        (
            t.create_value_key(time = '3.18', interpolation_type = 5, value = 1.72),
            t.create_value_key(time = '11.73', interpolation_type = 5, value = 1.72),
        ),
        (
            t.create_value_key(time = '3.18', interpolation_type = 5, value = -0.3),
            t.create_value_key(time = '11.73', interpolation_type = 5, value = -0.4),
        ),
        (
            t.create_value_key(time = '3.18', interpolation_type = 5, value = bg3.euler_to_quaternion(120.0, 0.0, 0.0, sequence = 'yxz')),
            t.create_value_key(time = '11.73', interpolation_type = 5, value = bg3.euler_to_quaternion(102.0, 0.0, 0.0, sequence = 'yxz')),
        ),
        (),
        (),
    ))
    t.create_tl_shot('89eeac49-0759-420d-8f99-3b76a8b2b7e8', '3.18', '11.73')


    # # Camera shot 3
    # # e68b591d-d8e7-469d-bd8f-61a17d957ed6 Tav -> SH
    # t.create_tl_camera_fov('89eeac49-0759-420d-8f99-3b76a8b2b7e8', 8.61, '11.73', (
    #     t.create_value_key(time = 4.2, value_name = 'FoV', value = 30.0, interpolation_type = 2),
    # ))
    # t.create_tl_transform('89eeac49-0759-420d-8f99-3b76a8b2b7e8', 8.61, '11.73', (
    #     (
    #         t.create_value_key(time = 8.61, interpolation_type = 5, value = -0.8),
    #     ),
    #     (
    #         t.create_value_key(time = 8.61, interpolation_type = 5, value = 1.72),
    #     ),
    #     (
    #         t.create_value_key(time = 8.61, interpolation_type = 5, value = -0.4),
    #     ),
    #     (
    #         t.create_value_key(time = 8.61, interpolation_type = 5, value = bg3.euler_to_quaternion(102.0, 0.0, 0.0, sequence = 'yxz')),
    #     ),
    #     (),
    #     (),
    # ))
    # t.create_tl_shot('89eeac49-0759-420d-8f99-3b76a8b2b7e8', 8.61, 11.73)

    # Camera shot 4
    # 617c4c96-b6d8-4077-8708-a65a6c4faf17 SH -> Tav
    #t.create_tl_shot('a43f207a-ed78-4acf-9815-9103e41577d0', '11.73', 15.07)
    # t.create_tl_camera_fov('89eeac49-0759-420d-8f99-3b76a8b2b7e8', '11.73', 15.07, (
    #     t.create_value_key(time = 4.2, value_name = 'FoV', value = 30.0, interpolation_type = 2),
    # ))
    # t.create_tl_transform('89eeac49-0759-420d-8f99-3b76a8b2b7e8', '11.73', 15.07, (
    #     (
    #         t.create_value_key(time = '11.73', interpolation_type = 5, value = -0.95),
    #     ),
    #     (
    #         t.create_value_key(time = '11.73', interpolation_type = 5, value = 1.72),
    #     ),
    #     (
    #         t.create_value_key(time = '11.73', interpolation_type = 5, value = -0.3),
    #     ),
    #     (
    #         t.create_value_key(time = '11.73', interpolation_type = 5, value = bg3.euler_to_quaternion(96.0, 0.0, 0.0, sequence = 'yxz')),
    #     ),
    #     (),
    #     (),
    # ))
    # t.create_tl_shot('89eeac49-0759-420d-8f99-3b76a8b2b7e8', '11.73', 15.07)

    t.create_tl_animation(
        bg3.SPEAKER_SHADOWHEART, '12.97', '16.17',
        'c26b9b0a-20cc-44a4-a499-18d6d78abec5',
        '58cf7977-b766-4cfa-8328-370c91da3547',
        animation_slot = 1,
        animation_play_start_offset = 6.8,
        fade_in = 1.0,
        fade_out = 1.0)

    # Camera shot 5
    # e68b591d-d8e7-469d-bd8f-61a17d957ed6 Tav -> SH
    #t.create_tl_shot('64edf86f-1d72-47fd-b908-a444cadb2fc3', 15.07, 19.58)
    t.create_tl_camera_fov('89eeac49-0759-420d-8f99-3b76a8b2b7e8', '11.73', '17.58', (
        t.create_value_key(time = '11.73', value_name = 'FoV', value = 30.0, interpolation_type = 2),
        t.create_value_key(time = '17.58', value_name = 'FoV', value = 25.0, interpolation_type = 2),
    ))
    t.create_tl_transform('89eeac49-0759-420d-8f99-3b76a8b2b7e8', '11.73', '17.58', (
        (
            t.create_value_key(time = '11.73', interpolation_type = 5, value = 0.95),
            t.create_value_key(time = '17.58', interpolation_type = 5, value = 0.5),
        ),
        (
            t.create_value_key(time = '11.73', interpolation_type = 5, value = 1.70),
            t.create_value_key(time = '17.58', interpolation_type = 5, value = 1.70),
        ),
        (
            t.create_value_key(time = '11.73', interpolation_type = 5, value = -0.4),
            t.create_value_key(time = '17.58', interpolation_type = 5, value = -0.1),
        ),
        (
            t.create_value_key(time = '11.73', interpolation_type = 5, value = bg3.euler_to_quaternion(-90.0, 0.0, 0.0, sequence = 'yxz')),
            t.create_value_key(time = '17.58', interpolation_type = 5, value = bg3.euler_to_quaternion(-128.0, 0.0, 0.0, sequence = 'yxz')),
        ),
        (),
        (),
    ))
    t.create_tl_shot('89eeac49-0759-420d-8f99-3b76a8b2b7e8', '11.73', '17.58')


    # # Camera shot 6
    # # 617c4c96-b6d8-4077-8708-a65a6c4faf17 SH -> Tav
    # t.create_tl_camera_fov('89eeac49-0759-420d-8f99-3b76a8b2b7e8', '17.58', 20.44, (
    #     t.create_value_key(time = 4.2, value_name = 'FoV', value = 30.0, interpolation_type = 2),
    # ))
    # t.create_tl_transform('89eeac49-0759-420d-8f99-3b76a8b2b7e8', '17.58', 20.44, (
    #     (
    #         t.create_value_key(time = '17.58', interpolation_type = 5, value = -0.7),
    #     ),
    #     (
    #         t.create_value_key(time = '17.58', interpolation_type = 5, value = 1.70),
    #     ),
    #     (
    #         t.create_value_key(time = '17.58', interpolation_type = 5, value = -0.9),
    #     ),
    #     (
    #         t.create_value_key(time = '17.58', interpolation_type = 5, value = bg3.euler_to_quaternion(45.0, 0.0, 0.0, sequence = 'yxz')),
    #     ),
    #     (),
    #     (),
    # ))
    # t.create_tl_shot('89eeac49-0759-420d-8f99-3b76a8b2b7e8', '17.58', 20.44)

    # Camera shot 7
    # 617c4c96-b6d8-4077-8708-a65a6c4faf17 SH -> Tav
    t.create_tl_camera_fov('89eeac49-0759-420d-8f99-3b76a8b2b7e8', '17.58', '29.44', (
        t.create_value_key(time = '17.58', value_name = 'FoV', value = 30.0, interpolation_type = 2),
    ))
    t.create_tl_transform('89eeac49-0759-420d-8f99-3b76a8b2b7e8', '17.58', '29.44', (
        (
            t.create_value_key(time = '17.58', interpolation_type = 5, value = -0.7),
        ),
        (
            t.create_value_key(time = '17.58', interpolation_type = 5, value = 1.70),
        ),
        (
            t.create_value_key(time = '17.58', interpolation_type = 5, value = -0.25),
        ),
        (
            t.create_value_key(time = '17.58', interpolation_type = 5, value = bg3.euler_to_quaternion(114.0, 0.0, 0.0, sequence = 'yxz')),
        ),
        (),
        (),
    ))
    t.create_tl_shot('89eeac49-0759-420d-8f99-3b76a8b2b7e8', '17.58', '29.44')


    t.create_tl_voice(bg3.SPEAKER_SHADOWHEART, '19.9', '20.9', dialog_node_uuid)

    t.create_tl_animation(
        bg3.SPEAKER_PLAYER, '20.76', '25.86',
        'c26b9b0a-20cc-44a4-a499-18d6d78abec5',
        '75879d7a-1352-4561-b159-2eb8429bc7c1',
        animation_slot = 1,
        animation_play_start_offset = 6.8,
        fade_in = 1.0,
        fade_out = 1.0)
    t.create_tl_animation(
        bg3.SPEAKER_SHADOWHEART, '20.76', '25.86',
        'c26b9b0a-20cc-44a4-a499-18d6d78abec5',
        '58cf7977-b766-4cfa-8328-370c91da3547',
        animation_slot = 1,
        animation_play_start_offset = 6.8,
        fade_in = 1.0,
        fade_out = 1.0)

    # Camera shot 8
    # c4f6737b-2cee-4f55-8cc4-0766bc4d2f97 SH -> Tav
    t.create_tl_shot('9de43fdc-0612-4161-9f37-d975d5ca409c', '29.44', '32.14')

    # Camera shot 9
    # eec1066a-3301-4f2b-b54d-27467f94c7b3 Tav -> Sh
    t.create_tl_shot('18c5bd4f-c066-4c52-8cdb-d8bbe1d8034e', '32.14', phase_duration, is_snapped_to_end = True)


def add_laezel_kiss_bt1_animation(d: bg3.dialog_object, t: bg3.timeline_object, dialog_node_uuid: str) -> None:

    # t = bg3.timeline_object(files.get_file('Gustav', 'Public/GustavDev/Timeline/Generated/ShadowHeart_InParty2_Nested_ShadowheartKiss.lsf'), d)

    #slot_idx_shadowheart = d.get_speaker_slot_index(bg3.SPEAKER_SHADOWHEART)
    #slot_idx_tav = d.get_speaker_slot_index(bg3.SPEAKER_PLAYER)

    phase_duration = '33.14'
    t.create_new_phase(dialog_node_uuid, phase_duration)

    t.create_tl_actor_node(bg3.timeline_object.ATTITUDE, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.ATTITUDE, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (), is_snapped_to_end = True)

    t.create_tl_actor_node(bg3.timeline_object.EMOTION, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.EMOTION, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (), is_snapped_to_end = True)

    t.create_tl_actor_node(bg3.timeline_object.LOOK_AT, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_look_at_key(
            0.0,
            target = bg3.SPEAKER_PLAYER,
            bone = 'Head_M',
            turn_mode = 3,
            turn_speed_multiplier = 0.3,
            head_turn_speed_multiplier = 0.05,
            weight = 1.0,
            safe_zone_angle = 80.0,
            head_safe_zone_angle = 80.0,
            look_at_mode = 1,
            eye_look_at_bone = 'Head_M'),
        t.create_look_at_key(
            32.09,
            target = bg3.SPEAKER_PLAYER,
            bone = 'Head_M',
            turn_mode = 3,
            turn_speed_multiplier = 0.3,
            head_turn_speed_multiplier = 0.3,
            weight = 0.0,
            reset = True,
            eye_look_at_bone = 'Head_M'),
    ), is_snapped_to_end = True)

    t.create_tl_actor_node(bg3.timeline_object.LOOK_AT, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        t.create_look_at_key(
            0.0,
            target = bg3.SPEAKER_SHADOWHEART,
            bone = 'Head_M',
            turn_mode = 3,
            turn_speed_multiplier = 0.3,
            head_turn_speed_multiplier = 0.05,
            weight = 1.0,
            head_safe_zone_angle = 80.0,
            eye_look_at_bone = 'Head_M'),
        t.create_look_at_key(
            0.86,
            target = bg3.SPEAKER_SHADOWHEART,
            bone = 'Head_M',
            turn_mode = 3,
            turn_speed_multiplier = 0.3,
            head_turn_speed_multiplier = 0.05,
            weight = 1.0,
            safe_zone_angle = 80.0,
            head_safe_zone_angle = 80.0,
            look_at_mode = 1,
            eye_look_at_bone = 'Head_M'),
        t.create_look_at_key(
            32.09,
            target = bg3.SPEAKER_SHADOWHEART,
            bone = 'Head_M',
            turn_mode = 3,
            turn_speed_multiplier = 0.3,
            head_turn_speed_multiplier = 0.05,
            weight = 0.0,
            head_safe_zone_angle = 80.0,
            reset = True,
            eye_look_at_bone = 'Head_M'),
    ), is_snapped_to_end = True)

    t.create_tl_actor_node(bg3.timeline_object.EMOTION, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        t.create_emotion_key(0.0, 64),
        t.create_emotion_key(14.5, 2, variation = 1),
        t.create_emotion_key(23.9, 2, variation = 2),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.EMOTION, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_emotion_key(0.0, 64),
        t.create_emotion_key(6.5, 2, is_sustained = False),
        t.create_emotion_key(7.0, 64),
        t.create_emotion_key(24.8, 2, variation = 1),
    ), is_snapped_to_end = True)

    t.create_tl_actor_node(bg3.timeline_object.LOOK_AT, bg3.PEANUT_SLOT_0, '0.0', phase_duration, (), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.LOOK_AT, bg3.PEANUT_SLOT_1, '0.0', phase_duration, (), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.LOOK_AT, bg3.PEANUT_SLOT_2, '0.0', phase_duration, (), is_snapped_to_end = True)

    # Hide helmets
    t.create_tl_show_armor(bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        (
            t.create_value_key(time = 0.0, value = False, interpolation_type = 0),
            t.create_value_key(time = phase_duration, interpolation_type = 0)
        ),
        (), (), (), (), (), (), (), (), (), ()
    ), is_snapped_to_end = True)
    t.create_tl_show_armor(bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        (
            t.create_value_key(time = 0.0, value = False, interpolation_type = 0),
            t.create_value_key(time = phase_duration, interpolation_type = 0)
        ),
        (), (), (), (), (), (), (), (), (), ()
    ), is_snapped_to_end = True)

    t.create_tl_actor_node(bg3.timeline_object.SOUND, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_sound_event_key(13.45, sound_event_id = '6ffc5af2-ae64-48a2-9068-4996d4cdceab', sound_object_index = 4),
        t.create_sound_event_key(15.47, sound_event_id = 'aa8db628-8c78-4632-ab7a-2ac210393e93', sound_object_index = 4),
        t.create_sound_event_key(21.03, sound_event_id = '90a31a12-9f32-47e1-899e-cdced0705f27', sound_object_index = 4),
        t.create_sound_event_key(21.14, sound_event_id = '6ffc5af2-ae64-48a2-9068-4996d4cdceab', sound_object_index = 4),
        t.create_sound_event_key(21.78, sound_event_id = 'ffbbbd57-5c31-444d-bc3a-c3d14df0be53', sound_object_index = 4),
        t.create_sound_event_key(23.37, sound_event_id = 'ffbbbd57-5c31-444d-bc3a-c3d14df0be53', sound_object_index = 4),
        t.create_sound_event_key(24.68, sound_event_id = '55647a99-7f83-42b4-8493-3ab9b58d824f', sound_object_index = 4),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.SOUND, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        t.create_sound_event_key(0.61, sound_event_id = 'f728f472-57d5-45ce-be9e-6e2f927bee0d', sound_object_index = 4),
    ), is_snapped_to_end = True)

    t.create_tl_actor_node(bg3.timeline_object.PHYSICS, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        t.create_value_key(time = 0.0, interpolation_type = 3, value_name = 'InverseKinematics', value = False),
        t.create_value_key(time = 29.44, interpolation_type = 3),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.PHYSICS, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_value_key(time = 0.0, interpolation_type = 3, value_name = 'InverseKinematics', value = False),
        t.create_value_key(time = 29.44, interpolation_type = 3),
    ), is_snapped_to_end = True)

    t.create_tl_transform(bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 0.0),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 0.0),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 0.38),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = (0.0, 0.0, 0.0, 1.0)),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 1),
        ),
        (),
    ), is_snapped_to_end = True)
    t.create_tl_transform(bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = -0.17),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 0.0),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = -1.06),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = (0.0, 1.0, 0.0, 0.0)),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 1),
        ),
        (),
    ), is_snapped_to_end = True)

    t.create_tl_animation(
        bg3.SPEAKER_SHADOWHEART, '0.0', '32.09',
        '8e459a21-cee9-71e8-258f-9aacc0e71417',
        '4587fb8c-2427-45a9-a4a2-4a33ca04cb1e',
        fade_in = 0.0,
        fade_out = 2.0,
        is_snapped_to_end = True)
    t.create_tl_animation(
        bg3.SPEAKER_PLAYER, '0.0', '32.09',
        'ff4e02ff-9235-44a2-a885-c87ca5797309',
        'a2ca8e61-fbc1-48bb-b9a4-fef4c8c3682d',
        fade_in = 0.0,
        fade_out = 0.0,
        is_snapped_to_end = True)

    # Camera shot 1
    # 563a9cc6-a183-456e-b3ea-c196a07711b8 Tav -> SH
    # c4f6737b-2cee-4f55-8cc4-0766bc4d2f97 SH -> Tav ff9136ca-e96e-4709-8d3c-f4a6d0de5690
    # t.create_tl_camera_fov('89eeac49-0759-420d-8f99-3b76a8b2b7e8', 0.0, 3.18, (
    #     t.create_value_key(time = 4.2, value_name = 'FoV', value = 28.0, interpolation_type = 2),
    # ))
    # t.create_tl_transform('89eeac49-0759-420d-8f99-3b76a8b2b7e8', 0.0, 3.18, (
    #     (
    #         t.create_value_key(time = 0.0, interpolation_type = 5, value = -0.6),
    #         t.create_value_key(time = '3.18', interpolation_type = 5, value = -0.8),
    #     ),
    #     (
    #         t.create_value_key(time = 0.0, interpolation_type = 5, value = 1.6),
    #     ),
    #     (
    #         t.create_value_key(time = 0.0, interpolation_type = 5, value = 0.6),
    #         t.create_value_key(time = '3.18', interpolation_type = 5, value = 0.4),
    #     ),
    #     (
    #         t.create_value_key(time = 0.0, interpolation_type = 5, value = bg3.euler_to_quaternion(165.0, 0.0, 0.0, sequence = 'yxz')),
    #         t.create_value_key(time = '3.18', interpolation_type = 5, value = bg3.euler_to_quaternion(157.0, 0.0, 0.0, sequence = 'yxz')),
    #     ),
    #     (),
    #     (),
    # ))
    t.create_tl_shot('9de43fdc-0612-4161-9f37-d975d5ca409c', '0.0', '3.18')

    # Camera shot 2
    # 6f87ec93-2f4e-4ff1-8a0f-56a2c50546d7 Tav -> SH
    t.create_tl_camera_fov('89eeac49-0759-420d-8f99-3b76a8b2b7e8', '3.18', '11.73', (
        t.create_value_key(time = '3.18', value_name = 'FoV', value = 40.0, interpolation_type = 2),
        t.create_value_key(time = '11.73', value_name = 'FoV', value = 25.0, interpolation_type = 2),
    ))
    t.create_tl_transform('89eeac49-0759-420d-8f99-3b76a8b2b7e8', '3.18', '11.73', (
        (
            t.create_value_key(time = '3.18', interpolation_type = 5, value = -0.6),
            t.create_value_key(time = '11.73', interpolation_type = 5, value = -0.8),
        ),
        (
            t.create_value_key(time = '3.18', interpolation_type = 5, value = 1.72),
            t.create_value_key(time = '11.73', interpolation_type = 5, value = 1.72),
        ),
        (
            t.create_value_key(time = '3.18', interpolation_type = 5, value = -0.3),
            t.create_value_key(time = '11.73', interpolation_type = 5, value = -0.4),
        ),
        (
            t.create_value_key(time = '3.18', interpolation_type = 5, value = bg3.euler_to_quaternion(120.0, 0.0, 0.0, sequence = 'yxz')),
            t.create_value_key(time = '11.73', interpolation_type = 5, value = bg3.euler_to_quaternion(102.0, 0.0, 0.0, sequence = 'yxz')),
        ),
        (),
        (),
    ))
    t.create_tl_shot('89eeac49-0759-420d-8f99-3b76a8b2b7e8', '3.18', '11.73')

    t.create_tl_animation(
        bg3.SPEAKER_SHADOWHEART, '12.97', '16.17',
        'c26b9b0a-20cc-44a4-a499-18d6d78abec5',
        '58cf7977-b766-4cfa-8328-370c91da3547',
        animation_slot = 1,
        animation_play_start_offset = 6.8,
        fade_in = 1.0,
        fade_out = 1.0)

    # Camera shot 5
    # e68b591d-d8e7-469d-bd8f-61a17d957ed6 Tav -> SH
    #t.create_tl_shot('64edf86f-1d72-47fd-b908-a444cadb2fc3', 15.07, 19.58)
    t.create_tl_camera_fov('89eeac49-0759-420d-8f99-3b76a8b2b7e8', '11.73', '17.58', (
        t.create_value_key(time = 4.2, value_name = 'FoV', value = 30.0, interpolation_type = 2),
    ))
    t.create_tl_transform('89eeac49-0759-420d-8f99-3b76a8b2b7e8', '11.73', '17.58', (
        (
            t.create_value_key(time = '11.73', interpolation_type = 5, value = 0.95),
            t.create_value_key(time = '17.58', interpolation_type = 5, value = 0.5),
        ),
        (
            t.create_value_key(time = '11.73', interpolation_type = 5, value = 1.70),
            t.create_value_key(time = '17.58', interpolation_type = 5, value = 1.70),
        ),
        (
            t.create_value_key(time = '11.73', interpolation_type = 5, value = -0.4),
            t.create_value_key(time = '17.58', interpolation_type = 5, value = -0.1),
        ),
        (
            t.create_value_key(time = '11.73', interpolation_type = 5, value = bg3.euler_to_quaternion(-90.0, 0.0, 0.0, sequence = 'yxz')),
            t.create_value_key(time = '17.58', interpolation_type = 5, value = bg3.euler_to_quaternion(-128.0, 0.0, 0.0, sequence = 'yxz')),
        ),
        (),
        (),
    ))
    t.create_tl_shot('89eeac49-0759-420d-8f99-3b76a8b2b7e8', '11.73', '17.58')

    # Camera shot 7
    # 617c4c96-b6d8-4077-8708-a65a6c4faf17 SH -> Tav
    t.create_tl_camera_fov('89eeac49-0759-420d-8f99-3b76a8b2b7e8', '17.58', '29.44', (
        t.create_value_key(time = 4.2, value_name = 'FoV', value = 30.0, interpolation_type = 2),
    ))
    t.create_tl_transform('89eeac49-0759-420d-8f99-3b76a8b2b7e8', '17.58', '29.44', (
        (
            t.create_value_key(time = '17.58', interpolation_type = 5, value = -0.7),
        ),
        (
            t.create_value_key(time = '17.58', interpolation_type = 5, value = 1.70),
        ),
        (
            t.create_value_key(time = '17.58', interpolation_type = 5, value = -0.25),
        ),
        (
            t.create_value_key(time = '17.58', interpolation_type = 5, value = bg3.euler_to_quaternion(114.0, 0.0, 0.0, sequence = 'yxz')),
        ),
        (),
        (),
    ))
    t.create_tl_shot('89eeac49-0759-420d-8f99-3b76a8b2b7e8', '17.58', '29.44')

    t.create_tl_voice(bg3.SPEAKER_SHADOWHEART, '19.9', '20.9', dialog_node_uuid)

    t.create_tl_animation(
        bg3.SPEAKER_PLAYER, '20.76', '25.86',
        'c26b9b0a-20cc-44a4-a499-18d6d78abec5',
        '75879d7a-1352-4561-b159-2eb8429bc7c1',
        animation_slot = 1,
        animation_play_start_offset = 6.8,
        fade_in = 1.0,
        fade_out = 1.0)
    t.create_tl_animation(
        bg3.SPEAKER_SHADOWHEART, '20.76', '25.86',
        'c26b9b0a-20cc-44a4-a499-18d6d78abec5',
        '58cf7977-b766-4cfa-8328-370c91da3547',
        animation_slot = 1,
        animation_play_start_offset = 6.8,
        fade_in = 1.0,
        fade_out = 1.0)

    # Camera shot 8
    # c4f6737b-2cee-4f55-8cc4-0766bc4d2f97 SH -> Tav
    t.create_tl_shot('9de43fdc-0612-4161-9f37-d975d5ca409c', '29.44', '32.09')

    # Camera shot 9
    # eec1066a-3301-4f2b-b54d-27467f94c7b3 Tav -> Sh
    t.create_tl_shot('18c5bd4f-c066-4c52-8cdb-d8bbe1d8034e', '32.09', phase_duration, is_snapped_to_end = True)


def add_laezel_kiss_bt34_animation(d: bg3.dialog_object, t: bg3.timeline_object, dialog_node_uuid: str) -> None:

    # t = bg3.timeline_object(files.get_file('Gustav', 'Public/GustavDev/Timeline/Generated/ShadowHeart_InParty2_Nested_ShadowheartKiss.lsf'), d)

    #slot_idx_shadowheart = d.get_speaker_slot_index(bg3.SPEAKER_SHADOWHEART)
    #slot_idx_tav = d.get_speaker_slot_index(bg3.SPEAKER_PLAYER)

    phase_duration = '33.14'
    t.create_new_phase(dialog_node_uuid, phase_duration)

    t.create_tl_actor_node(bg3.timeline_object.ATTITUDE, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.ATTITUDE, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (), is_snapped_to_end = True)

    t.create_tl_actor_node(bg3.timeline_object.EMOTION, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.EMOTION, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (), is_snapped_to_end = True)

    t.create_tl_actor_node(bg3.timeline_object.LOOK_AT, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_look_at_key(
            0.0,
            target = bg3.SPEAKER_PLAYER,
            bone = 'Head_M',
            turn_mode = 3,
            turn_speed_multiplier = 0.3,
            head_turn_speed_multiplier = 0.05,
            weight = 1.0,
            safe_zone_angle = 80.0,
            head_safe_zone_angle = 80.0,
            look_at_mode = 1,
            eye_look_at_bone = 'Head_M'),
        t.create_look_at_key(
            32.635,
            target = bg3.SPEAKER_PLAYER,
            bone = 'Head_M',
            turn_mode = 3,
            turn_speed_multiplier = 0.3,
            head_turn_speed_multiplier = 0.3,
            weight = 0.0,
            reset = True,
            eye_look_at_bone = 'Head_M'),
    ), is_snapped_to_end = True)

    t.create_tl_actor_node(bg3.timeline_object.LOOK_AT, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        t.create_look_at_key(
            0.0,
            target = bg3.SPEAKER_SHADOWHEART,
            bone = 'Head_M',
            turn_mode = 3,
            turn_speed_multiplier = 0.3,
            head_turn_speed_multiplier = 0.05,
            weight = 1.0,
            safe_zone_angle = 80.0,
            head_safe_zone_angle = 80.0,
            look_at_mode = 1,
            eye_look_at_bone = 'Head_M'),
        t.create_look_at_key(
            32.635,
            target = bg3.SPEAKER_SHADOWHEART,
            bone = 'Head_M',
            turn_mode = 3,
            turn_speed_multiplier = 0.3,
            head_turn_speed_multiplier = 0.05,
            weight = 0.0,
            head_safe_zone_angle = 80.0,
            reset = True,
            eye_look_at_bone = 'Head_M'),
    ), is_snapped_to_end = True)

    t.create_tl_actor_node(bg3.timeline_object.EMOTION, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        t.create_emotion_key(0.0, 64),
        t.create_emotion_key(14.5, 2, variation = 1),
        t.create_emotion_key(23.9, 2, variation = 2),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.EMOTION, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_emotion_key(0.0, 64),
        t.create_emotion_key(6.5, 2, is_sustained = False),
        t.create_emotion_key(7.0, 64),
        t.create_emotion_key(24.8, 2, variation = 1),
    ), is_snapped_to_end = True)

    t.create_tl_actor_node(bg3.timeline_object.LOOK_AT, bg3.PEANUT_SLOT_0, '0.0', phase_duration, (), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.LOOK_AT, bg3.PEANUT_SLOT_1, '0.0', phase_duration, (), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.LOOK_AT, bg3.PEANUT_SLOT_2, '0.0', phase_duration, (), is_snapped_to_end = True)

    # Hide helmets
    t.create_tl_show_armor(bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        (
            t.create_value_key(time = 0.0, value = False, interpolation_type = 0),
            t.create_value_key(time = phase_duration, interpolation_type = 0)
        ),
        (), (), (), (), (), (), (), (), (), ()
    ), is_snapped_to_end = True)
    t.create_tl_show_armor(bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        (
            t.create_value_key(time = 0.0, value = False, interpolation_type = 0),
            t.create_value_key(time = phase_duration, interpolation_type = 0)
        ),
        (), (), (), (), (), (), (), (), (), ()
    ), is_snapped_to_end = True)

    t.create_tl_actor_node(bg3.timeline_object.SOUND, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_sound_event_key(13.33, sound_event_id = '6ffc5af2-ae64-48a2-9068-4996d4cdceab', sound_object_index = 4),
        t.create_sound_event_key(15.33, sound_event_id = 'aa8db628-8c78-4632-ab7a-2ac210393e93', sound_object_index = 4),
        t.create_sound_event_key(21.19, sound_event_id = '90a31a12-9f32-47e1-899e-cdced0705f27', sound_object_index = 4),
        t.create_sound_event_key(21.30, sound_event_id = '6ffc5af2-ae64-48a2-9068-4996d4cdceab', sound_object_index = 4),
        t.create_sound_event_key(21.94, sound_event_id = 'ffbbbd57-5c31-444d-bc3a-c3d14df0be53', sound_object_index = 4),
        t.create_sound_event_key(23.53, sound_event_id = 'ffbbbd57-5c31-444d-bc3a-c3d14df0be53', sound_object_index = 4),
        t.create_sound_event_key(24.84, sound_event_id = '55647a99-7f83-42b4-8493-3ab9b58d824f', sound_object_index = 4),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.SOUND, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        t.create_sound_event_key(0.61, sound_event_id = 'f728f472-57d5-45ce-be9e-6e2f927bee0d', sound_object_index = 4),
    ), is_snapped_to_end = True)

    t.create_tl_actor_node(bg3.timeline_object.PHYSICS, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        t.create_value_key(time = 0.0, interpolation_type = 3, value_name = 'InverseKinematics', value = False),
        t.create_value_key(time = 29.44, interpolation_type = 3),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.PHYSICS, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_value_key(time = 0.0, interpolation_type = 3, value_name = 'InverseKinematics', value = False),
        t.create_value_key(time = 29.44, interpolation_type = 3),
    ), is_snapped_to_end = True)

    t.create_tl_transform(bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 0.10),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 0.0),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 0.46),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = (0.0, 0.0, 0.0, 1.0)),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 1),
        ),
        (),
    ), is_snapped_to_end = True)
    t.create_tl_transform(bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = -0.17),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 0.0),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = -1.06),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = (0.0, 1.0, 0.0, 0.0)),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 1),
        ),
        (),
    ), is_snapped_to_end = True)

    t.create_tl_animation(
        bg3.SPEAKER_SHADOWHEART, '0.0', '32.635',
        'd1785dac-9bae-c5bb-588c-dfc3cdc2e0b8',
        '4587fb8c-2427-45a9-a4a2-4a33ca04cb1e',
        fade_in = 0.0,
        fade_out = 2.0,
        is_snapped_to_end = True)
    t.create_tl_animation(
        bg3.SPEAKER_PLAYER, '0.0', '32.635',
        'afbfbaaf-83b2-472a-9061-bf6d84c44cc3',
        'a2ca8e61-fbc1-48bb-b9a4-fef4c8c3682d',
        fade_in = 0.0,
        fade_out = 0.0,
        is_snapped_to_end = True)

    # Camera shot 1
    # 563a9cc6-a183-456e-b3ea-c196a07711b8 Tav -> SH
    # c4f6737b-2cee-4f55-8cc4-0766bc4d2f97 SH -> Tav ff9136ca-e96e-4709-8d3c-f4a6d0de5690
    # t.create_tl_camera_fov('89eeac49-0759-420d-8f99-3b76a8b2b7e8', 0.0, 3.18, (
    #     t.create_value_key(time = 4.2, value_name = 'FoV', value = 28.0, interpolation_type = 2),
    # ))
    # t.create_tl_transform('89eeac49-0759-420d-8f99-3b76a8b2b7e8', 0.0, 3.18, (
    #     (
    #         t.create_value_key(time = 0.0, interpolation_type = 5, value = -0.6),
    #         t.create_value_key(time = '3.18', interpolation_type = 5, value = -0.8),
    #     ),
    #     (
    #         t.create_value_key(time = 0.0, interpolation_type = 5, value = 1.6),
    #     ),
    #     (
    #         t.create_value_key(time = 0.0, interpolation_type = 5, value = 0.6),
    #         t.create_value_key(time = '3.18', interpolation_type = 5, value = 0.4),
    #     ),
    #     (
    #         t.create_value_key(time = 0.0, interpolation_type = 5, value = bg3.euler_to_quaternion(165.0, 0.0, 0.0, sequence = 'yxz')),
    #         t.create_value_key(time = '3.18', interpolation_type = 5, value = bg3.euler_to_quaternion(157.0, 0.0, 0.0, sequence = 'yxz')),
    #     ),
    #     (),
    #     (),
    # ))
    t.create_tl_shot('9de43fdc-0612-4161-9f37-d975d5ca409c', '0.0', '3.18')

    # Camera shot 2
    # 6f87ec93-2f4e-4ff1-8a0f-56a2c50546d7 Tav -> SH
    t.create_tl_camera_fov('89eeac49-0759-420d-8f99-3b76a8b2b7e8', '3.18', '11.73', (
        t.create_value_key(time = 4.2, value_name = 'FoV', value = 40.0, interpolation_type = 2),
    ))
    t.create_tl_transform('89eeac49-0759-420d-8f99-3b76a8b2b7e8', '3.18', '11.73', (
        (
            t.create_value_key(time = '3.18', interpolation_type = 5, value = -0.6),
            t.create_value_key(time = '11.73', interpolation_type = 5, value = -0.8),
        ),
        (
            t.create_value_key(time = '3.18', interpolation_type = 5, value = 1.72),
            t.create_value_key(time = '11.73', interpolation_type = 5, value = 1.72),
        ),
        (
            t.create_value_key(time = '3.18', interpolation_type = 5, value = -0.3),
            t.create_value_key(time = '11.73', interpolation_type = 5, value = -0.4),
        ),
        (
            t.create_value_key(time = '3.18', interpolation_type = 5, value = bg3.euler_to_quaternion(120.0, 0.0, 0.0, sequence = 'yxz')),
            t.create_value_key(time = '11.73', interpolation_type = 5, value = bg3.euler_to_quaternion(102.0, 0.0, 0.0, sequence = 'yxz')),
        ),
        (),
        (),
    ))
    t.create_tl_shot('89eeac49-0759-420d-8f99-3b76a8b2b7e8', '3.18', '11.73')

    t.create_tl_animation(
        bg3.SPEAKER_SHADOWHEART, '12.97', '16.17',
        'c26b9b0a-20cc-44a4-a499-18d6d78abec5',
        '58cf7977-b766-4cfa-8328-370c91da3547',
        animation_slot = 1,
        animation_play_start_offset = 6.8,
        fade_in = 1.0,
        fade_out = 1.0)

    # Camera shot 5
    # e68b591d-d8e7-469d-bd8f-61a17d957ed6 Tav -> SH
    #t.create_tl_shot('64edf86f-1d72-47fd-b908-a444cadb2fc3', 15.07, 19.58)
    t.create_tl_camera_fov('89eeac49-0759-420d-8f99-3b76a8b2b7e8', '11.73', '17.58', (
        t.create_value_key(time = 4.2, value_name = 'FoV', value = 30.0, interpolation_type = 2),
    ))
    t.create_tl_transform('89eeac49-0759-420d-8f99-3b76a8b2b7e8', '11.73', '17.58', (
        (
            t.create_value_key(time = '11.73', interpolation_type = 5, value = 0.95),
            t.create_value_key(time = '17.58', interpolation_type = 5, value = 0.5),
        ),
        (
            t.create_value_key(time = '11.73', interpolation_type = 5, value = 1.70),
            t.create_value_key(time = '17.58', interpolation_type = 5, value = 1.70),
        ),
        (
            t.create_value_key(time = '11.73', interpolation_type = 5, value = -0.4),
            t.create_value_key(time = '17.58', interpolation_type = 5, value = -0.1),
        ),
        (
            t.create_value_key(time = '11.73', interpolation_type = 5, value = bg3.euler_to_quaternion(-90.0, 0.0, 0.0, sequence = 'yxz')),
            t.create_value_key(time = '17.58', interpolation_type = 5, value = bg3.euler_to_quaternion(-128.0, 0.0, 0.0, sequence = 'yxz')),
        ),
        (),
        (),
    ))
    t.create_tl_shot('89eeac49-0759-420d-8f99-3b76a8b2b7e8', '11.73', '17.58')

    # Camera shot 7
    # 617c4c96-b6d8-4077-8708-a65a6c4faf17 SH -> Tav
    t.create_tl_camera_fov('89eeac49-0759-420d-8f99-3b76a8b2b7e8', '17.58', '29.44', (
        t.create_value_key(time = 4.2, value_name = 'FoV', value = 30.0, interpolation_type = 2),
    ))
    t.create_tl_transform('89eeac49-0759-420d-8f99-3b76a8b2b7e8', '17.58', '29.44', (
        (
            t.create_value_key(time = '17.58', interpolation_type = 5, value = -0.7),
        ),
        (
            t.create_value_key(time = '17.58', interpolation_type = 5, value = 1.70),
        ),
        (
            t.create_value_key(time = '17.58', interpolation_type = 5, value = -0.25),
        ),
        (
            t.create_value_key(time = '17.58', interpolation_type = 5, value = bg3.euler_to_quaternion(114.0, 0.0, 0.0, sequence = 'yxz')),
        ),
        (),
        (),
    ))
    t.create_tl_shot('89eeac49-0759-420d-8f99-3b76a8b2b7e8', '17.58', '29.44')

    t.create_tl_voice(bg3.SPEAKER_SHADOWHEART, '19.9', '20.9', dialog_node_uuid)

    t.create_tl_animation(
        bg3.SPEAKER_PLAYER, '20.76', '25.86',
        'c26b9b0a-20cc-44a4-a499-18d6d78abec5',
        '75879d7a-1352-4561-b159-2eb8429bc7c1',
        animation_slot = 1,
        animation_play_start_offset = 6.8,
        fade_in = 1.0,
        fade_out = 1.0)
    t.create_tl_animation(
        bg3.SPEAKER_SHADOWHEART, '20.76', '25.86',
        'c26b9b0a-20cc-44a4-a499-18d6d78abec5',
        '58cf7977-b766-4cfa-8328-370c91da3547',
        animation_slot = 1,
        animation_play_start_offset = 6.8,
        fade_in = 1.0,
        fade_out = 1.0)

    # Camera shot 8
    # c4f6737b-2cee-4f55-8cc4-0766bc4d2f97 SH -> Tav
    t.create_tl_shot('9de43fdc-0612-4161-9f37-d975d5ca409c', '29.44', '32.635')

    # Camera shot 9
    # eec1066a-3301-4f2b-b54d-27467f94c7b3 Tav -> Sh
    t.create_tl_shot('18c5bd4f-c066-4c52-8cdb-d8bbe1d8034e', '32.635', phase_duration, is_snapped_to_end = True)


def add_laezel_kiss_dragonborn_animation(d: bg3.dialog_object, t: bg3.timeline_object, dialog_node_uuid: str) -> None:

    # t = bg3.timeline_object(files.get_file('Gustav', 'Public/GustavDev/Timeline/Generated/ShadowHeart_InParty2_Nested_ShadowheartKiss.lsf'), d)

    #slot_idx_shadowheart = d.get_speaker_slot_index(bg3.SPEAKER_SHADOWHEART)
    #slot_idx_tav = d.get_speaker_slot_index(bg3.SPEAKER_PLAYER)

    phase_duration = '35.14'
    t.create_new_phase(dialog_node_uuid, phase_duration)

    t.create_tl_actor_node(bg3.timeline_object.ATTITUDE, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.ATTITUDE, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (), is_snapped_to_end = True)

    t.create_tl_actor_node(bg3.timeline_object.EMOTION, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.EMOTION, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (), is_snapped_to_end = True)

    t.create_tl_actor_node(bg3.timeline_object.LOOK_AT, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_look_at_key(
            0.0,
            target = bg3.SPEAKER_PLAYER,
            bone = 'Head_M',
            turn_mode = 3,
            turn_speed_multiplier = 0.3,
            head_turn_speed_multiplier = 0.05,
            weight = 1.0,
            safe_zone_angle = 80.0,
            head_safe_zone_angle = 80.0,
            look_at_mode = 1,
            eye_look_at_bone = 'Head_M'),
        t.create_look_at_key(
            34.67,
            target = bg3.SPEAKER_PLAYER,
            bone = 'Head_M',
            turn_mode = 3,
            turn_speed_multiplier = 0.3,
            head_turn_speed_multiplier = 0.3,
            weight = 0.0,
            reset = True,
            eye_look_at_bone = 'Head_M'),
    ), is_snapped_to_end = True)

    t.create_tl_actor_node(bg3.timeline_object.LOOK_AT, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        t.create_look_at_key(
            0.0,
            target = bg3.SPEAKER_SHADOWHEART,
            bone = 'Head_M',
            turn_mode = 3,
            turn_speed_multiplier = 0.3,
            head_turn_speed_multiplier = 0.05,
            weight = 1.0,
            safe_zone_angle = 80.0,
            head_safe_zone_angle = 80.0,
            look_at_mode = 1,
            eye_look_at_bone = 'Head_M'),
        t.create_look_at_key(
            34.67,
            target = bg3.SPEAKER_SHADOWHEART,
            bone = 'Head_M',
            turn_mode = 3,
            turn_speed_multiplier = 0.3,
            head_turn_speed_multiplier = 0.05,
            weight = 0.0,
            head_safe_zone_angle = 80.0,
            reset = True,
            eye_look_at_bone = 'Head_M'),
    ), is_snapped_to_end = True)

    t.create_tl_actor_node(bg3.timeline_object.EMOTION, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        t.create_emotion_key(0.0, 64),
        t.create_emotion_key(14.5, 2, variation = 1),
        t.create_emotion_key(23.9, 2, variation = 2),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.EMOTION, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_emotion_key(0.0, 64),
        t.create_emotion_key(6.5, 2, is_sustained = False),
        t.create_emotion_key(7.0, 64),
        t.create_emotion_key(24.8, 2, variation = 1),
    ), is_snapped_to_end = True)

    t.create_tl_actor_node(bg3.timeline_object.LOOK_AT, bg3.PEANUT_SLOT_0, '0.0', phase_duration, (), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.LOOK_AT, bg3.PEANUT_SLOT_1, '0.0', phase_duration, (), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.LOOK_AT, bg3.PEANUT_SLOT_2, '0.0', phase_duration, (), is_snapped_to_end = True)

    # Hide helmets
    t.create_tl_show_armor(bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        (
            t.create_value_key(time = 0.0, value = False, interpolation_type = 0),
            t.create_value_key(time = phase_duration, interpolation_type = 0)
        ),
        (), (), (), (), (), (), (), (), (), ()
    ), is_snapped_to_end = True)
    t.create_tl_show_armor(bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        (
            t.create_value_key(time = 0.0, value = False, interpolation_type = 0),
            t.create_value_key(time = phase_duration, interpolation_type = 0)
        ),
        (), (), (), (), (), (), (), (), (), ()
    ), is_snapped_to_end = True)

    t.create_tl_actor_node(bg3.timeline_object.SOUND, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_sound_event_key(13.8, sound_event_id = '6ffc5af2-ae64-48a2-9068-4996d4cdceab', sound_object_index = 4),
        t.create_sound_event_key(15.57, sound_event_id = 'aa8db628-8c78-4632-ab7a-2ac210393e93', sound_object_index = 4),
        t.create_sound_event_key(20.93, sound_event_id = '90a31a12-9f32-47e1-899e-cdced0705f27', sound_object_index = 4),
        t.create_sound_event_key(21.05, sound_event_id = '6ffc5af2-ae64-48a2-9068-4996d4cdceab', sound_object_index = 4),
        t.create_sound_event_key(21.68, sound_event_id = 'ffbbbd57-5c31-444d-bc3a-c3d14df0be53', sound_object_index = 4),
        t.create_sound_event_key(23.27, sound_event_id = 'ffbbbd57-5c31-444d-bc3a-c3d14df0be53', sound_object_index = 4),
        t.create_sound_event_key(24.75, sound_event_id = '55647a99-7f83-42b4-8493-3ab9b58d824f', sound_object_index = 4),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.SOUND, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        t.create_sound_event_key(0.61, sound_event_id = 'f728f472-57d5-45ce-be9e-6e2f927bee0d', sound_object_index = 4),
    ), is_snapped_to_end = True)

    t.create_tl_actor_node(bg3.timeline_object.PHYSICS, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        t.create_value_key(time = 0.0, interpolation_type = 3, value_name = 'InverseKinematics', value = False),
        t.create_value_key(time = 29.44, interpolation_type = 3),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.PHYSICS, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_value_key(time = 0.0, interpolation_type = 3, value_name = 'InverseKinematics', value = False),
        t.create_value_key(time = 29.44, interpolation_type = 3),
    ), is_snapped_to_end = True)

    t.create_tl_transform(bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 0.10),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 0.0),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 0.46),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = (0.0, 0.0, 0.0, 1.0)),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 1),
        ),
        (),
    ), is_snapped_to_end = True)
    t.create_tl_transform(bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = -0.17),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 0.0),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = -1.06),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = (0.0, 1.0, 0.0, 0.0)),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 1),
        ),
        (),
    ), is_snapped_to_end = True)

    t.create_tl_animation(
        bg3.SPEAKER_SHADOWHEART, '0.0', '34.67',
        '3bb3cb56-fcba-cd00-a5a3-527f02d4a0b4',
        '4587fb8c-2427-45a9-a4a2-4a33ca04cb1e',
        fade_in = 0.0,
        fade_out = 2.0,
        is_snapped_to_end = True)
    t.create_tl_animation(
        bg3.SPEAKER_PLAYER, '0.0', '34.67',
        '7b0e91c7-a32f-48a3-a253-195194db5124',
        'a2ca8e61-fbc1-48bb-b9a4-fef4c8c3682d',
        fade_in = 0.0,
        fade_out = 0.0,
        is_snapped_to_end = True)

    # Camera shot 1
    # 563a9cc6-a183-456e-b3ea-c196a07711b8 Tav -> SH
    # c4f6737b-2cee-4f55-8cc4-0766bc4d2f97 SH -> Tav ff9136ca-e96e-4709-8d3c-f4a6d0de5690
    # t.create_tl_camera_fov('89eeac49-0759-420d-8f99-3b76a8b2b7e8', 0.0, 3.18, (
    #     t.create_value_key(time = 4.2, value_name = 'FoV', value = 28.0, interpolation_type = 2),
    # ))
    # t.create_tl_transform('89eeac49-0759-420d-8f99-3b76a8b2b7e8', 0.0, 3.18, (
    #     (
    #         t.create_value_key(time = 0.0, interpolation_type = 5, value = -0.6),
    #         t.create_value_key(time = '3.18', interpolation_type = 5, value = -0.8),
    #     ),
    #     (
    #         t.create_value_key(time = 0.0, interpolation_type = 5, value = 1.6),
    #     ),
    #     (
    #         t.create_value_key(time = 0.0, interpolation_type = 5, value = 0.6),
    #         t.create_value_key(time = '3.18', interpolation_type = 5, value = 0.4),
    #     ),
    #     (
    #         t.create_value_key(time = 0.0, interpolation_type = 5, value = bg3.euler_to_quaternion(165.0, 0.0, 0.0, sequence = 'yxz')),
    #         t.create_value_key(time = '3.18', interpolation_type = 5, value = bg3.euler_to_quaternion(157.0, 0.0, 0.0, sequence = 'yxz')),
    #     ),
    #     (),
    #     (),
    # ))
    t.create_tl_shot('9de43fdc-0612-4161-9f37-d975d5ca409c', '0.0', '3.18')

    # Camera shot 2
    # 6f87ec93-2f4e-4ff1-8a0f-56a2c50546d7 Tav -> SH
    t.create_tl_camera_fov('89eeac49-0759-420d-8f99-3b76a8b2b7e8', '3.18', '11.73', (
        t.create_value_key(time = 4.2, value_name = 'FoV', value = 40.0, interpolation_type = 2),
    ))
    t.create_tl_transform('89eeac49-0759-420d-8f99-3b76a8b2b7e8', '3.18', '11.73', (
        (
            t.create_value_key(time = '3.18', interpolation_type = 5, value = -0.6),
            t.create_value_key(time = '11.73', interpolation_type = 5, value = -0.8),
        ),
        (
            t.create_value_key(time = '3.18', interpolation_type = 5, value = 1.72),
            t.create_value_key(time = '11.73', interpolation_type = 5, value = 1.72),
        ),
        (
            t.create_value_key(time = '3.18', interpolation_type = 5, value = -0.3),
            t.create_value_key(time = '11.73', interpolation_type = 5, value = -0.4),
        ),
        (
            t.create_value_key(time = '3.18', interpolation_type = 5, value = bg3.euler_to_quaternion(120.0, 0.0, 0.0, sequence = 'yxz')),
            t.create_value_key(time = '11.73', interpolation_type = 5, value = bg3.euler_to_quaternion(102.0, 0.0, 0.0, sequence = 'yxz')),
        ),
        (),
        (),
    ))
    t.create_tl_shot('89eeac49-0759-420d-8f99-3b76a8b2b7e8', '3.18', '11.73')

    t.create_tl_animation(
        bg3.SPEAKER_SHADOWHEART, '12.97', '16.17',
        'c26b9b0a-20cc-44a4-a499-18d6d78abec5',
        '58cf7977-b766-4cfa-8328-370c91da3547',
        animation_slot = 1,
        animation_play_start_offset = 6.8,
        fade_in = 1.0,
        fade_out = 1.0)

    # Camera shot 5
    # e68b591d-d8e7-469d-bd8f-61a17d957ed6 Tav -> SH
    #t.create_tl_shot('64edf86f-1d72-47fd-b908-a444cadb2fc3', 15.07, 19.58)
    t.create_tl_camera_fov('89eeac49-0759-420d-8f99-3b76a8b2b7e8', '11.73', '17.58', (
        t.create_value_key(time = 4.2, value_name = 'FoV', value = 30.0, interpolation_type = 2),
    ))
    t.create_tl_transform('89eeac49-0759-420d-8f99-3b76a8b2b7e8', '11.73', '17.58', (
        (
            t.create_value_key(time = '11.73', interpolation_type = 5, value = 0.95),
            t.create_value_key(time = '17.58', interpolation_type = 5, value = 0.5),
        ),
        (
            t.create_value_key(time = '11.73', interpolation_type = 5, value = 1.70),
            t.create_value_key(time = '17.58', interpolation_type = 5, value = 1.70),
        ),
        (
            t.create_value_key(time = '11.73', interpolation_type = 5, value = -0.4),
            t.create_value_key(time = '17.58', interpolation_type = 5, value = -0.1),
        ),
        (
            t.create_value_key(time = '11.73', interpolation_type = 5, value = bg3.euler_to_quaternion(-90.0, 0.0, 0.0, sequence = 'yxz')),
            t.create_value_key(time = '17.58', interpolation_type = 5, value = bg3.euler_to_quaternion(-128.0, 0.0, 0.0, sequence = 'yxz')),
        ),
        (),
        (),
    ))
    t.create_tl_shot('89eeac49-0759-420d-8f99-3b76a8b2b7e8', '11.73', '17.58')

    # Camera shot 7
    # 617c4c96-b6d8-4077-8708-a65a6c4faf17 SH -> Tav
    t.create_tl_camera_fov('89eeac49-0759-420d-8f99-3b76a8b2b7e8', '17.58', '29.44', (
        t.create_value_key(time = 4.2, value_name = 'FoV', value = 30.0, interpolation_type = 2),
    ))
    t.create_tl_transform('89eeac49-0759-420d-8f99-3b76a8b2b7e8', '17.58', '29.44', (
        (
            t.create_value_key(time = '17.58', interpolation_type = 5, value = -0.7),
        ),
        (
            t.create_value_key(time = '17.58', interpolation_type = 5, value = 1.70),
        ),
        (
            t.create_value_key(time = '17.58', interpolation_type = 5, value = -0.25),
        ),
        (
            t.create_value_key(time = '17.58', interpolation_type = 5, value = bg3.euler_to_quaternion(114.0, 0.0, 0.0, sequence = 'yxz')),
        ),
        (),
        (),
    ))
    t.create_tl_shot('89eeac49-0759-420d-8f99-3b76a8b2b7e8', '17.58', '29.44')

    t.create_tl_voice(bg3.SPEAKER_SHADOWHEART, '19.9', '20.9', dialog_node_uuid)

    t.create_tl_animation(
        bg3.SPEAKER_PLAYER, '20.76', '25.86',
        'c26b9b0a-20cc-44a4-a499-18d6d78abec5',
        '75879d7a-1352-4561-b159-2eb8429bc7c1',
        animation_slot = 1,
        animation_play_start_offset = 6.8,
        fade_in = 1.0,
        fade_out = 1.0)
    t.create_tl_animation(
        bg3.SPEAKER_SHADOWHEART, '20.76', '25.86',
        'c26b9b0a-20cc-44a4-a499-18d6d78abec5',
        '58cf7977-b766-4cfa-8328-370c91da3547',
        animation_slot = 1,
        animation_play_start_offset = 6.8,
        fade_in = 1.0,
        fade_out = 1.0)

    # Camera shot 8
    # c4f6737b-2cee-4f55-8cc4-0766bc4d2f97 SH -> Tav
    t.create_tl_shot('9de43fdc-0612-4161-9f37-d975d5ca409c', '29.44', '34.67')

    # Camera shot 9
    # eec1066a-3301-4f2b-b54d-27467f94c7b3 Tav -> Sh
    t.create_tl_shot('18c5bd4f-c066-4c52-8cdb-d8bbe1d8034e', '34.67', phase_duration, is_snapped_to_end = True)


def add_laezel_kiss_short_animation(d: bg3.dialog_object, t: bg3.timeline_object, dialog_node_uuid: str) -> None:

    # t = bg3.timeline_object(files.get_file('Gustav', 'Public/GustavDev/Timeline/Generated/ShadowHeart_InParty2_Nested_ShadowheartKiss.lsf'), d)

    #slot_idx_shadowheart = d.get_speaker_slot_index(bg3.SPEAKER_SHADOWHEART)
    #slot_idx_tav = d.get_speaker_slot_index(bg3.SPEAKER_PLAYER)

    phase_duration = '34.54'
    t.create_new_phase(dialog_node_uuid, phase_duration)

    t.create_tl_actor_node(bg3.timeline_object.ATTITUDE, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.ATTITUDE, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (), is_snapped_to_end = True)

    t.create_tl_actor_node(bg3.timeline_object.EMOTION, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.EMOTION, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (), is_snapped_to_end = True)

    t.create_tl_actor_node(bg3.timeline_object.LOOK_AT, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_look_at_key(
            0.0,
            target = bg3.SPEAKER_PLAYER,
            bone = 'Head_M',
            turn_mode = 3,
            turn_speed_multiplier = 0.3,
            head_turn_speed_multiplier = 0.05,
            weight = 1.0,
            safe_zone_angle = 80.0,
            head_safe_zone_angle = 80.0,
            reset = True,
            look_at_mode = 1,
            eye_look_at_bone = 'Head_M'),
        t.create_look_at_key(
            34.04,
            target = bg3.SPEAKER_PLAYER,
            bone = 'Head_M',
            turn_mode = 3,
            turn_speed_multiplier = 0.3,
            head_turn_speed_multiplier = 0.3,
            weight = 0.0,
            reset = True,
            eye_look_at_bone = 'Head_M'),
    ), is_snapped_to_end = True)

    t.create_tl_actor_node(bg3.timeline_object.LOOK_AT, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        t.create_look_at_key(
            0.0,
            target = bg3.SPEAKER_SHADOWHEART,
            bone = 'Head_M',
            turn_mode = 3,
            turn_speed_multiplier = 0.3,
            head_turn_speed_multiplier = 0.05,
            weight = 0.0,
            head_safe_zone_angle = 80.0,
            eye_look_at_bone = 'Head_M'),
        t.create_look_at_key(
            0.86,
            target = bg3.SPEAKER_SHADOWHEART,
            bone = 'Head_M',
            turn_mode = 3,
            turn_speed_multiplier = 0.3,
            head_turn_speed_multiplier = 0.05,
            weight = 1.0,
            safe_zone_angle = 80.0,
            head_safe_zone_angle = 80.0,
            look_at_mode = 1,
            eye_look_at_bone = 'Head_M'),
        t.create_look_at_key(
            34.04,
            target = bg3.SPEAKER_SHADOWHEART,
            bone = 'Head_M',
            turn_mode = 3,
            turn_speed_multiplier = 0.3,
            head_turn_speed_multiplier = 0.05,
            weight = 0.0,
            head_safe_zone_angle = 80.0,
            reset = True,
            eye_look_at_bone = 'Head_M'),
    ), is_snapped_to_end = True)

    t.create_tl_actor_node(bg3.timeline_object.EMOTION, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        t.create_emotion_key(0.0, 64),
        t.create_emotion_key(14.5, 2, variation = 1),
        t.create_emotion_key(23.9, 2, variation = 2),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.EMOTION, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_emotion_key(0.0, 64),
        t.create_emotion_key(6.5, 2, is_sustained = False),
        t.create_emotion_key(7.0, 64),
        t.create_emotion_key(24.8, 2, variation = 1),
    ), is_snapped_to_end = True)

    t.create_tl_actor_node(bg3.timeline_object.LOOK_AT, bg3.PEANUT_SLOT_0, '0.0', phase_duration, (), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.LOOK_AT, bg3.PEANUT_SLOT_1, '0.0', phase_duration, (), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.LOOK_AT, bg3.PEANUT_SLOT_2, '0.0', phase_duration, (), is_snapped_to_end = True)

    # Hide helmets
    t.create_tl_show_armor(bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        (
            t.create_value_key(time = 0.0, value = False, interpolation_type = 0),
            t.create_value_key(time = phase_duration, interpolation_type = 0)
        ),
        (), (), (), (), (), (), (), (), (), ()
    ), is_snapped_to_end = True)
    t.create_tl_show_armor(bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        (
            t.create_value_key(time = 0.0, value = False, interpolation_type = 0),
            t.create_value_key(time = phase_duration, interpolation_type = 0)
        ),
        (), (), (), (), (), (), (), (), (), ()
    ), is_snapped_to_end = True)

    t.create_tl_actor_node(bg3.timeline_object.SOUND, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_sound_event_key(14.45, sound_event_id = '6ffc5af2-ae64-48a2-9068-4996d4cdceab', sound_object_index = 4),
        t.create_sound_event_key(16.42, sound_event_id = 'aa8db628-8c78-4632-ab7a-2ac210393e93', sound_object_index = 4),
        t.create_sound_event_key(21.44, sound_event_id = '90a31a12-9f32-47e1-899e-cdced0705f27', sound_object_index = 4),
        t.create_sound_event_key(21.55, sound_event_id = '6ffc5af2-ae64-48a2-9068-4996d4cdceab', sound_object_index = 4),
        t.create_sound_event_key(22.19, sound_event_id = 'ffbbbd57-5c31-444d-bc3a-c3d14df0be53', sound_object_index = 4),
        t.create_sound_event_key(23.78, sound_event_id = 'ffbbbd57-5c31-444d-bc3a-c3d14df0be53', sound_object_index = 4),
        t.create_sound_event_key(25.1, sound_event_id = '55647a99-7f83-42b4-8493-3ab9b58d824f', sound_object_index = 4),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.SOUND, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        t.create_sound_event_key(0.61, sound_event_id = 'f728f472-57d5-45ce-be9e-6e2f927bee0d', sound_object_index = 4),
    ), is_snapped_to_end = True)

    t.create_tl_actor_node(bg3.timeline_object.PHYSICS, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        t.create_value_key(time = 0.0, interpolation_type = 3, value_name = 'InverseKinematics', value = False),
        t.create_value_key(time = 29.44, interpolation_type = 3),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.PHYSICS, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_value_key(time = 0.0, interpolation_type = 3, value_name = 'InverseKinematics', value = False),
        t.create_value_key(time = 29.44, interpolation_type = 3),
    ), is_snapped_to_end = True)

    t.create_tl_transform(bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 0.0),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 0.0),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 0.37),
            #t.create_value_key(time = 0.0, interpolation_type = 5, value = 0.4),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = (0.0, 0.0, 0.0, 1.0)),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 1),
        ),
        (),
    ), is_snapped_to_end = True)
    t.create_tl_transform(bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = -0.17),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 0.0),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = -1.06),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = (0.0, 1.0, 0.0, 0.0)),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 1),
        ),
        (),
    ), is_snapped_to_end = True)

    t.create_tl_animation(
        bg3.SPEAKER_SHADOWHEART, '0.0', '34.04',
        'd7abb08f-3c39-d733-8269-903c0a2a6c5c',
        '4587fb8c-2427-45a9-a4a2-4a33ca04cb1e',
        fade_in = 0.0,
        fade_out = 2.0,
        is_snapped_to_end = True)
    t.create_tl_animation(
        bg3.SPEAKER_PLAYER, '0.0', '34.04',
        '2a96d6c4-03bb-459d-af74-bc7cc35420f4',
        'a2ca8e61-fbc1-48bb-b9a4-fef4c8c3682d',
        fade_in = 0.0,
        fade_out = 0.0,
        is_snapped_to_end = True)

    # Camera shot 1
    # 563a9cc6-a183-456e-b3ea-c196a07711b8 Tav -> SH
    t.create_tl_shot('9de43fdc-0612-4161-9f37-d975d5ca409c', '0.0', '3.18')

    # Camera shot 2
    # 6f87ec93-2f4e-4ff1-8a0f-56a2c50546d7 Tav -> SH
    t.create_tl_camera_fov('89eeac49-0759-420d-8f99-3b76a8b2b7e8', '3.18', '11.73', (
        t.create_value_key(time = '3.18', value_name = 'FoV', value = 40.0, interpolation_type = 2),
        t.create_value_key(time = '11.73', value_name = 'FoV', value = 25.0, interpolation_type = 2),
    ))
    t.create_tl_transform('89eeac49-0759-420d-8f99-3b76a8b2b7e8', '3.18', '11.73', (
        (
            t.create_value_key(time = '3.18', interpolation_type = 5, value = -0.6),
            t.create_value_key(time = '11.73', interpolation_type = 5, value = -0.8),
        ),
        (
            t.create_value_key(time = '3.18', interpolation_type = 5, value = 1.3),
            t.create_value_key(time = '11.73', interpolation_type = 5, value = 1.35),
        ),
        (
            t.create_value_key(time = '3.18', interpolation_type = 5, value = 0.35),
            t.create_value_key(time = '11.73', interpolation_type = 5, value = 0.25),
        ),
        (
            t.create_value_key(time = '3.18', interpolation_type = 5, value = bg3.euler_to_quaternion(120.0, 0.0, 0.0, sequence = 'yxz')),
            t.create_value_key(time = '11.73', interpolation_type = 5, value = bg3.euler_to_quaternion(108.0, 0.0, 0.0, sequence = 'yxz')),
        ),
        (),
        (),
    ))
    t.create_tl_shot('89eeac49-0759-420d-8f99-3b76a8b2b7e8', '3.18', '11.73')

    t.create_tl_animation(
        bg3.SPEAKER_SHADOWHEART, '14.02', '17.02',
        'c26b9b0a-20cc-44a4-a499-18d6d78abec5',
        '58cf7977-b766-4cfa-8328-370c91da3547',
        animation_slot = 1,
        animation_play_start_offset = 6.8,
        fade_in = 1.0,
        fade_out = 1.0)

    # Camera shot 5
    # e68b591d-d8e7-469d-bd8f-61a17d957ed6 Tav -> SH
    #t.create_tl_shot('64edf86f-1d72-47fd-b908-a444cadb2fc3', 15.07, 19.58)
    t.create_tl_camera_fov('89eeac49-0759-420d-8f99-3b76a8b2b7e8', '11.73', '18.58', (
        t.create_value_key(time = '11.73', value_name = 'FoV', value = 30.0, interpolation_type = 2),
        #t.create_value_key(time = 18.58, value_name = 'FoV', value = 28.0, interpolation_type = 2),
    ))
    t.create_tl_transform('89eeac49-0759-420d-8f99-3b76a8b2b7e8', '11.73', '18.58', (
        (
            t.create_value_key(time = '11.73', interpolation_type = 5, value = 0.95),
            t.create_value_key(time = 18.58, interpolation_type = 5, value = 0.65),
        ),
        (
            t.create_value_key(time = '11.73', interpolation_type = 5, value = 1.3),
            t.create_value_key(time = 18.58, interpolation_type = 5, value = 1.4),
        ),
        (
            t.create_value_key(time = '11.73', interpolation_type = 5, value = 0.0),
            t.create_value_key(time = 18.58, interpolation_type = 5, value = 0.15),
            #t.create_value_key(time = 18.58, interpolation_type = 5, value = 0.45),
        ),
        (
            t.create_value_key(time = '11.73', interpolation_type = 5, value = bg3.euler_to_quaternion(-90.0, 0.0, 0.0, sequence = 'yxz')),
            t.create_value_key(time = 18.58, interpolation_type = 5, value = bg3.euler_to_quaternion(-98.0, 0.0, 0.0, sequence = 'yxz')),
        ),
        (),
        (),
    ))
    t.create_tl_shot('89eeac49-0759-420d-8f99-3b76a8b2b7e8', '11.73', '18.58')

    # Camera shot 7
    # 617c4c96-b6d8-4077-8708-a65a6c4faf17 SH -> Tav
    t.create_tl_camera_fov('89eeac49-0759-420d-8f99-3b76a8b2b7e8', '18.58', '29.44', (
        t.create_value_key(time = 18.58, value_name = 'FoV', value = 30.0, interpolation_type = 2),
        t.create_value_key(time = 29.44, value_name = 'FoV', value = 28.0, interpolation_type = 2),
    ))
    t.create_tl_transform('89eeac49-0759-420d-8f99-3b76a8b2b7e8', '18.58', '29.44', (
        (
            t.create_value_key(time = 18.58, interpolation_type = 5, value = -0.7),
        ),
        (
            t.create_value_key(time = 18.58, interpolation_type = 5, value = 1.35),
        ),
        (
            t.create_value_key(time = 18.58, interpolation_type = 5, value = 0.3),
            t.create_value_key(time = 29.44, interpolation_type = 5, value = 0.2),
        ),
        (
            t.create_value_key(time = 18.58, interpolation_type = 5, value = bg3.euler_to_quaternion(114.0, 0.0, 0.0, sequence = 'yxz')),
            t.create_value_key(time = 29.44, interpolation_type = 5, value = bg3.euler_to_quaternion(118.0, 0.0, 0.0, sequence = 'yxz')),
        ),
        (),
        (),
    ))
    t.create_tl_shot('89eeac49-0759-420d-8f99-3b76a8b2b7e8', '18.58', '29.44')

    t.create_tl_voice(bg3.SPEAKER_SHADOWHEART, '19.9', '20.9', dialog_node_uuid)

    t.create_tl_animation(
        bg3.SPEAKER_PLAYER, '20.76', '25.86',
        'c26b9b0a-20cc-44a4-a499-18d6d78abec5',
        '75879d7a-1352-4561-b159-2eb8429bc7c1',
        animation_slot = 1,
        animation_play_start_offset = 6.8,
        fade_in = 1.0,
        fade_out = 1.0)
    t.create_tl_animation(
        bg3.SPEAKER_SHADOWHEART, '20.76', '25.86',
        'c26b9b0a-20cc-44a4-a499-18d6d78abec5',
        '58cf7977-b766-4cfa-8328-370c91da3547',
        animation_slot = 1,
        animation_play_start_offset = 6.8,
        fade_in = 1.0,
        fade_out = 1.0)

    # Camera shot 8
    # c4f6737b-2cee-4f55-8cc4-0766bc4d2f97 SH -> Tav
    t.create_tl_shot('9de43fdc-0612-4161-9f37-d975d5ca409c', '29.44', '34.04')

    # Camera shot 9
    # eec1066a-3301-4f2b-b54d-27467f94c7b3 Tav -> Sh
    t.create_tl_shot('18c5bd4f-c066-4c52-8cdb-d8bbe1d8034e', '34.04', phase_duration, is_snapped_to_end = True)


def add_laezel_kiss_dwarf_animation(d: bg3.dialog_object, t: bg3.timeline_object, dialog_node_uuid: str) -> None:

    # t = bg3.timeline_object(files.get_file('Gustav', 'Public/GustavDev/Timeline/Generated/ShadowHeart_InParty2_Nested_ShadowheartKiss.lsf'), d)

    #slot_idx_shadowheart = d.get_speaker_slot_index(bg3.SPEAKER_SHADOWHEART)
    #slot_idx_tav = d.get_speaker_slot_index(bg3.SPEAKER_PLAYER)

    phase_duration = '34.54'
    t.create_new_phase(dialog_node_uuid, phase_duration)

    t.create_tl_actor_node(bg3.timeline_object.ATTITUDE, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.ATTITUDE, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (), is_snapped_to_end = True)

    t.create_tl_actor_node(bg3.timeline_object.EMOTION, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.EMOTION, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (), is_snapped_to_end = True)

    t.create_tl_actor_node(bg3.timeline_object.LOOK_AT, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_look_at_key(
            0.0,
            target = bg3.SPEAKER_PLAYER,
            bone = 'Head_M',
            turn_mode = 3,
            turn_speed_multiplier = 0.3,
            head_turn_speed_multiplier = 0.05,
            weight = 1.0,
            safe_zone_angle = 80.0,
            head_safe_zone_angle = 80.0,
            reset = True,
            look_at_mode = 1,
            eye_look_at_bone = 'Head_M'),
        t.create_look_at_key(
            34.04,
            target = bg3.SPEAKER_PLAYER,
            bone = 'Head_M',
            turn_mode = 3,
            turn_speed_multiplier = 0.3,
            head_turn_speed_multiplier = 0.3,
            weight = 0.0,
            reset = True,
            eye_look_at_bone = 'Head_M'),
    ), is_snapped_to_end = True)

    t.create_tl_actor_node(bg3.timeline_object.LOOK_AT, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        t.create_look_at_key(
            0.0,
            target = bg3.SPEAKER_SHADOWHEART,
            bone = 'Head_M',
            turn_mode = 3,
            turn_speed_multiplier = 0.3,
            head_turn_speed_multiplier = 0.05,
            weight = 0.0,
            head_safe_zone_angle = 80.0,
            eye_look_at_bone = 'Head_M'),
        t.create_look_at_key(
            0.86,
            target = bg3.SPEAKER_SHADOWHEART,
            bone = 'Head_M',
            turn_mode = 3,
            turn_speed_multiplier = 0.3,
            head_turn_speed_multiplier = 0.05,
            weight = 1.0,
            safe_zone_angle = 80.0,
            head_safe_zone_angle = 80.0,
            look_at_mode = 1,
            eye_look_at_bone = 'Head_M'),
        t.create_look_at_key(
            34.04,
            target = bg3.SPEAKER_SHADOWHEART,
            bone = 'Head_M',
            turn_mode = 3,
            turn_speed_multiplier = 0.3,
            head_turn_speed_multiplier = 0.05,
            weight = 0.0,
            head_safe_zone_angle = 80.0,
            reset = True,
            eye_look_at_bone = 'Head_M'),
    ), is_snapped_to_end = True)

    t.create_tl_actor_node(bg3.timeline_object.EMOTION, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        t.create_emotion_key(0.0, 64),
        t.create_emotion_key(14.5, 2, variation = 1),
        t.create_emotion_key(23.9, 2, variation = 2),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.EMOTION, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_emotion_key(0.0, 64),
        t.create_emotion_key(6.5, 2, is_sustained = False),
        t.create_emotion_key(7.0, 64),
        t.create_emotion_key(24.8, 2, variation = 1),
    ), is_snapped_to_end = True)

    t.create_tl_actor_node(bg3.timeline_object.LOOK_AT, bg3.PEANUT_SLOT_0, '0.0', phase_duration, (), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.LOOK_AT, bg3.PEANUT_SLOT_1, '0.0', phase_duration, (), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.LOOK_AT, bg3.PEANUT_SLOT_2, '0.0', phase_duration, (), is_snapped_to_end = True)

    # Hide helmets
    t.create_tl_show_armor(bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        (
            t.create_value_key(time = 0.0, value = False, interpolation_type = 0),
            t.create_value_key(time = phase_duration, interpolation_type = 0)
        ),
        (), (), (), (), (), (), (), (), (), ()
    ), is_snapped_to_end = True)
    t.create_tl_show_armor(bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        (
            t.create_value_key(time = 0.0, value = False, interpolation_type = 0),
            t.create_value_key(time = phase_duration, interpolation_type = 0)
        ),
        (), (), (), (), (), (), (), (), (), ()
    ), is_snapped_to_end = True)

    t.create_tl_actor_node(bg3.timeline_object.SOUND, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_sound_event_key(14.45, sound_event_id = '6ffc5af2-ae64-48a2-9068-4996d4cdceab', sound_object_index = 4),
        t.create_sound_event_key(16.42, sound_event_id = 'aa8db628-8c78-4632-ab7a-2ac210393e93', sound_object_index = 4),
        t.create_sound_event_key(21.44, sound_event_id = '90a31a12-9f32-47e1-899e-cdced0705f27', sound_object_index = 4),
        t.create_sound_event_key(21.55, sound_event_id = '6ffc5af2-ae64-48a2-9068-4996d4cdceab', sound_object_index = 4),
        t.create_sound_event_key(22.19, sound_event_id = 'ffbbbd57-5c31-444d-bc3a-c3d14df0be53', sound_object_index = 4),
        t.create_sound_event_key(23.78, sound_event_id = 'ffbbbd57-5c31-444d-bc3a-c3d14df0be53', sound_object_index = 4),
        t.create_sound_event_key(25.1, sound_event_id = '55647a99-7f83-42b4-8493-3ab9b58d824f', sound_object_index = 4),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.SOUND, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        t.create_sound_event_key(0.61, sound_event_id = 'f728f472-57d5-45ce-be9e-6e2f927bee0d', sound_object_index = 4),
    ), is_snapped_to_end = True)

    t.create_tl_actor_node(bg3.timeline_object.PHYSICS, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        t.create_value_key(time = 0.0, interpolation_type = 3, value_name = 'InverseKinematics', value = False),
        t.create_value_key(time = 29.44, interpolation_type = 3),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.PHYSICS, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_value_key(time = 0.0, interpolation_type = 3, value_name = 'InverseKinematics', value = False),
        t.create_value_key(time = 29.44, interpolation_type = 3),
    ), is_snapped_to_end = True)

    t.create_tl_transform(bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 0.0),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 0.0),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 0.38),
            #t.create_value_key(time = 0.0, interpolation_type = 5, value = 0.4),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = (0.0, 0.0, 0.0, 1.0)),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 1),
        ),
        (),
    ), is_snapped_to_end = True)
    t.create_tl_transform(bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = -0.17),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 0.0),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = -1.06),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = (0.0, 1.0, 0.0, 0.0)),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 1),
        ),
        (),
    ), is_snapped_to_end = True)

    t.create_tl_animation(
        bg3.SPEAKER_SHADOWHEART, '0.0', '34.04',
        'd7abb08f-3c39-d733-8269-903c0a2a6c5c',
        '4587fb8c-2427-45a9-a4a2-4a33ca04cb1e',
        fade_in = 0.0,
        fade_out = 2.0,
        is_snapped_to_end = True)
    t.create_tl_animation(
        bg3.SPEAKER_PLAYER, '0.0', '34.04',
        '2a96d6c4-03bb-459d-af74-bc7cc35420f4',
        'a2ca8e61-fbc1-48bb-b9a4-fef4c8c3682d',
        fade_in = 0.0,
        fade_out = 0.0,
        is_snapped_to_end = True)

    # Camera shot 1
    # 563a9cc6-a183-456e-b3ea-c196a07711b8 Tav -> SH
    t.create_tl_shot('9de43fdc-0612-4161-9f37-d975d5ca409c', '0.0', '3.18')

    # Camera shot 2
    # 6f87ec93-2f4e-4ff1-8a0f-56a2c50546d7 Tav -> SH
    t.create_tl_camera_fov('89eeac49-0759-420d-8f99-3b76a8b2b7e8', '3.18', '11.73', (
        t.create_value_key(time = '3.18', value_name = 'FoV', value = 40.0, interpolation_type = 2),
        t.create_value_key(time = '11.73', value_name = 'FoV', value = 25.0, interpolation_type = 2),
    ))
    t.create_tl_transform('89eeac49-0759-420d-8f99-3b76a8b2b7e8', '3.18', '11.73', (
        (
            t.create_value_key(time = '3.18', interpolation_type = 5, value = -0.6),
            t.create_value_key(time = '11.73', interpolation_type = 5, value = -0.8),
        ),
        (
            t.create_value_key(time = '3.18', interpolation_type = 5, value = 1.3),
            t.create_value_key(time = '11.73', interpolation_type = 5, value = 1.35),
        ),
        (
            t.create_value_key(time = '3.18', interpolation_type = 5, value = 0.35),
            t.create_value_key(time = '11.73', interpolation_type = 5, value = 0.25),
        ),
        (
            t.create_value_key(time = '3.18', interpolation_type = 5, value = bg3.euler_to_quaternion(120.0, 0.0, 0.0, sequence = 'yxz')),
            t.create_value_key(time = '11.73', interpolation_type = 5, value = bg3.euler_to_quaternion(108.0, 0.0, 0.0, sequence = 'yxz')),
        ),
        (),
        (),
    ))
    t.create_tl_shot('89eeac49-0759-420d-8f99-3b76a8b2b7e8', '3.18', '11.73')

    t.create_tl_animation(
        bg3.SPEAKER_SHADOWHEART, '14.02', '17.02',
        'c26b9b0a-20cc-44a4-a499-18d6d78abec5',
        '58cf7977-b766-4cfa-8328-370c91da3547',
        animation_slot = 1,
        animation_play_start_offset = 6.8,
        fade_in = 1.0,
        fade_out = 1.0)

    # Camera shot 5
    # e68b591d-d8e7-469d-bd8f-61a17d957ed6 Tav -> SH
    #t.create_tl_shot('64edf86f-1d72-47fd-b908-a444cadb2fc3', 15.07, 19.58)
    t.create_tl_camera_fov('89eeac49-0759-420d-8f99-3b76a8b2b7e8', '11.73', '18.58', (
        t.create_value_key(time = '11.73', value_name = 'FoV', value = 30.0, interpolation_type = 2),
        #t.create_value_key(time = 18.58, value_name = 'FoV', value = 28.0, interpolation_type = 2),
    ))
    t.create_tl_transform('89eeac49-0759-420d-8f99-3b76a8b2b7e8', '11.73', '18.58', (
        (
            t.create_value_key(time = '11.73', interpolation_type = 5, value = 0.95),
            t.create_value_key(time = 18.58, interpolation_type = 5, value = 0.65),
        ),
        (
            t.create_value_key(time = '11.73', interpolation_type = 5, value = 1.3),
            t.create_value_key(time = 18.58, interpolation_type = 5, value = 1.4),
        ),
        (
            t.create_value_key(time = '11.73', interpolation_type = 5, value = 0.0),
            t.create_value_key(time = 18.58, interpolation_type = 5, value = 0.15),
            #t.create_value_key(time = 18.58, interpolation_type = 5, value = 0.45),
        ),
        (
            t.create_value_key(time = '11.73', interpolation_type = 5, value = bg3.euler_to_quaternion(-90.0, 0.0, 0.0, sequence = 'yxz')),
            t.create_value_key(time = 18.58, interpolation_type = 5, value = bg3.euler_to_quaternion(-98.0, 0.0, 0.0, sequence = 'yxz')),
        ),
        (),
        (),
    ))
    t.create_tl_shot('89eeac49-0759-420d-8f99-3b76a8b2b7e8', '11.73', '18.58')

    # Camera shot 7
    # 617c4c96-b6d8-4077-8708-a65a6c4faf17 SH -> Tav
    t.create_tl_camera_fov('89eeac49-0759-420d-8f99-3b76a8b2b7e8', '18.58', '29.44', (
        t.create_value_key(time = 18.58, value_name = 'FoV', value = 30.0, interpolation_type = 2),
        t.create_value_key(time = 29.44, value_name = 'FoV', value = 28.0, interpolation_type = 2),
    ))
    t.create_tl_transform('89eeac49-0759-420d-8f99-3b76a8b2b7e8', '18.58', '29.44', (
        (
            t.create_value_key(time = 18.58, interpolation_type = 5, value = -0.7),
        ),
        (
            t.create_value_key(time = 18.58, interpolation_type = 5, value = 1.35),
        ),
        (
            t.create_value_key(time = 18.58, interpolation_type = 5, value = 0.3),
            t.create_value_key(time = 29.44, interpolation_type = 5, value = 0.2),
        ),
        (
            t.create_value_key(time = 18.58, interpolation_type = 5, value = bg3.euler_to_quaternion(114.0, 0.0, 0.0, sequence = 'yxz')),
            t.create_value_key(time = 29.44, interpolation_type = 5, value = bg3.euler_to_quaternion(118.0, 0.0, 0.0, sequence = 'yxz')),
        ),
        (),
        (),
    ))
    t.create_tl_shot('89eeac49-0759-420d-8f99-3b76a8b2b7e8', '18.58', '29.44')

    t.create_tl_voice(bg3.SPEAKER_SHADOWHEART, '19.9', '20.9', dialog_node_uuid)

    t.create_tl_animation(
        bg3.SPEAKER_PLAYER, '20.76', '25.86',
        'c26b9b0a-20cc-44a4-a499-18d6d78abec5',
        '75879d7a-1352-4561-b159-2eb8429bc7c1',
        animation_slot = 1,
        animation_play_start_offset = 6.8,
        fade_in = 1.0,
        fade_out = 1.0)
    t.create_tl_animation(
        bg3.SPEAKER_SHADOWHEART, '20.76', '25.86',
        'c26b9b0a-20cc-44a4-a499-18d6d78abec5',
        '58cf7977-b766-4cfa-8328-370c91da3547',
        animation_slot = 1,
        animation_play_start_offset = 6.8,
        fade_in = 1.0,
        fade_out = 1.0)

    # Camera shot 8
    # c4f6737b-2cee-4f55-8cc4-0766bc4d2f97 SH -> Tav
    t.create_tl_shot('9de43fdc-0612-4161-9f37-d975d5ca409c', '29.44', '34.04')

    # Camera shot 9
    # eec1066a-3301-4f2b-b54d-27467f94c7b3 Tav -> Sh
    t.create_tl_shot('18c5bd4f-c066-4c52-8cdb-d8bbe1d8034e', '34.04', phase_duration, is_snapped_to_end = True)

from __future__ import annotations

import bg3moddinglib as bg3

from .context import game_assets
from .flags import *

########################################################
# If parents are saved, Tav proposes to Shadowheart
# in the romance fate cutscene
########################################################

########################################################
# Dialog: END_GameFinale_RomanceFates_Shadowheart.lsf
########################################################

def create_proposal_cinematic_bt1(dialog_node_uuid: str, t: bg3.timeline_object) -> None:

    phase_duration = '40.38'
    t.create_new_phase(dialog_node_uuid, phase_duration)

    t.create_tl_actor_node(bg3.timeline_object.ATTITUDE, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.ATTITUDE, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (), is_snapped_to_end = True)

    t.create_tl_actor_node(bg3.timeline_object.EMOTION, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        t.create_emotion_key(0.0, 2),
        t.create_emotion_key(5.49, 2, variation = 1),
        t.create_emotion_key(9.97 + 7.0, 256, variation = 24),
        t.create_emotion_key(10.9 + 7.0, 256, variation = 25),
        t.create_emotion_key(14.2 + 7.0, 16, is_sustained = False),
        t.create_emotion_key(17.64 + 7.0, 2, variation = 1, is_sustained = False),
        t.create_emotion_key(30.32 + 7.0, 2),
        t.create_emotion_key(32.39 + 7.0, 2, variation = 1, is_sustained = False)
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.EMOTION, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_emotion_key(0.5, 64),
        t.create_emotion_key(4.2, 2),
        t.create_emotion_key(10.2, 2, variation = 2, is_sustained = False),
        t.create_emotion_key(11.7, 2, variation = 1, is_sustained = False),
        t.create_emotion_key(13.8, 2, variation = 2, is_sustained = False),
        t.create_emotion_key(9.74 + 7.0, 2, variation = 1, is_sustained = False),
        t.create_emotion_key(17.2, 2, variation = 23, is_sustained = False),
        t.create_emotion_key(17.8, 2, variation = 1, is_sustained = False),
        t.create_emotion_key(25.05 + 7.0, 2, is_sustained = False),
        t.create_emotion_key(28.49 + 7.0, 2, variation = 2, is_sustained = False),
        t.create_emotion_key(29.36 + 7.0, 2, variation = 23, is_sustained = False),
        t.create_emotion_key(30.27 + 7.0, 2, variation = 1),
        t.create_emotion_key(32.0 + 7.0, 2, variation = 24),
        t.create_emotion_key(32.36 + 7.0, 2, variation = 2)
    ), is_snapped_to_end = True)

    t.create_tl_actor_node(bg3.timeline_object.LOOK_AT, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        t.create_look_at_key(
            0.0,
            turn_mode = 3,
            turn_speed_multiplier = 0.3,
            head_turn_speed_multiplier = 0.3,
            weight = 0.0,
            safe_zone_angle = 80.0,
            head_safe_zone_angle = 80.0,
            look_at_mode = 0),
        t.create_look_at_key(
            1.86,
            target = bg3.SPEAKER_SHADOWHEART,
            bone = 'Head_M',
            turn_mode = 3,
            turn_speed_multiplier = 0.3,
            head_turn_speed_multiplier = 0.3,
            weight = 0.0,
            safe_zone_angle = 80.0,
            head_safe_zone_angle = 80.0,
            offset = (0, -0.3, 0),
            is_eye_look_at_enabled = True,
            eye_look_at_target_id = bg3.SPEAKER_SHADOWHEART,
            eye_look_at_bone = 'Head_M'
        ),
        t.create_look_at_key(
            6.62,
            turn_mode = 3,
            turn_speed_multiplier = 0.3,
            head_turn_speed_multiplier = 0.3,
            weight = 0.0,
            safe_zone_angle = 80.0,
            head_safe_zone_angle = 80.0,
            look_at_mode = 0,
            is_eye_look_at_enabled = True),
        t.create_look_at_key(
            12.68,
            target = bg3.SPEAKER_SHADOWHEART,
            bone = 'Head_M',
            turn_mode = 3,
            turn_speed_multiplier = 0.3,
            head_turn_speed_multiplier = 0.3,
            weight = 0.0,
            safe_zone_angle = 80.0,
            head_safe_zone_angle = 80.0,
            look_at_mode = 1,
            eye_look_at_target_id = bg3.SPEAKER_SHADOWHEART,
            eye_look_at_bone = 'Head_M')
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.LOOK_AT, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_look_at_key(
            0.0,
            target = bg3.SPEAKER_PLAYER,
            bone = 'Head_M',
            turn_mode = 3,
            turn_speed_multiplier = 0.3,
            head_turn_speed_multiplier = 0.3,
            weight = 0.0,
            safe_zone_angle = 80.0,
            head_safe_zone_angle = 80.0,
            look_at_mode = 1,
            eye_look_at_bone = 'Head_M'),
    ), is_snapped_to_end = True)

    # Shadowheart theme
    t.create_tl_actor_node(bg3.timeline_object.SOUND, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_sound_event_key(0.0, sound_event_id = 'ec19d32b-1213-4166-ba20-405994e62381'),
    ))

    t.create_tl_actor_node(bg3.timeline_object.SOUND, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.SOUND, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        t.create_sound_event_key('16.67', sound_event_id = '6dbe237a-0c78-4023-a6b7-30349e0505db', sound_object_index = 4),
        t.create_sound_event_key('16.74', sound_event_id = '6ffc5af2-ae64-48a2-9068-4996d4cdceab', sound_object_index = 4),
        t.create_sound_event_key('22.24', sound_event_id = 'c232329e-2d4e-4f0c-a4d4-ea1585fce27c', sound_object_index = 4),
        t.create_sound_event_key('30.46', sound_event_id = '6ffc5af2-ae64-48a2-9068-4996d4cdceab', sound_object_index = 4),
        t.create_sound_event_key('30.48', sound_event_id = '5dac329f-b08a-412d-84bc-86fc1aecae45', sound_object_index = 4),
        t.create_sound_event_key('32.23', sound_event_id = 'ffbbbd57-5c31-444d-bc3a-c3d14df0be53', sound_object_index = 4),
        t.create_sound_event_key('35.19', sound_event_id = '5dac329f-b08a-412d-84bc-86fc1aecae45', sound_object_index = 4),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.SOUND, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        t.create_sound_event_key('25.91', sound_type = 4),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.SOUND, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        t.create_sound_event_key('2.43', sound_event_id = 'd572362f-b64c-4836-9c1d-4399507162fb')
    ), is_snapped_to_end = True)

    t.create_tl_actor_node(bg3.timeline_object.PHYSICS, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        t.create_value_key(time = 0.0, interpolation_type = 3),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.PHYSICS, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_value_key(time = 0.0, interpolation_type = 3, value_name = 'InverseKinematics', value = False),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.HANDS_IK, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_value_key(time = 0.0, interpolation_type = 3, value_name = 'InverseKinematics', value = False)
    ), is_snapped_to_end = True)
    

    camera_uuid = '91f50bea-c8cc-4c34-b618-227519017779'

    t.create_tl_camera_fov(camera_uuid, '0.0', '27.0', (
        t.create_value_key(time = 0.0, value = 30.0, value_name = 'FoV', interpolation_type = 3),
    ), is_snapped_to_end = True)

    t.create_tl_transform(bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = -1.219),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 0.0),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 3.0),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = bg3.euler_to_quaternion(-90, 0, 0, sequence='yxz')),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 1),
        ),
        (),
    ))


    # camera shot 1
    t.create_tl_transform(camera_uuid, '0.0', '4.2', (
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = -1.9),
            t.create_value_key(time = '4.2', interpolation_type = 5, value = -1.55),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 1.0),
            t.create_value_key(time = '4.2', interpolation_type = 5, value = 1.10),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 2.1),
            t.create_value_key(time = '4.2', interpolation_type = 5, value = 1.15),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = bg3.euler_to_quaternion(62, -18, 0, sequence='yxz')),
            t.create_value_key(time = '4.2', interpolation_type = 5, value = bg3.euler_to_quaternion(27, -6, 0, sequence='yxz')),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 1),
        ),
        (),
    ))
    t.create_tl_shot(camera_uuid, '0.0', phase_duration, is_snapped_to_end = True)

    t.create_tl_animation(
        bg3.SPEAKER_PLAYER, '0.0', '4.2',
        'ad48ef7a-e01d-4894-e41a-c97670e0f45b',
        '494aa8f4-9a3f-4156-a111-befb5461f276',
        fade_in = 0.0,
        fade_out = 0.0)

    t.create_tl_transform(bg3.SPEAKER_SHADOWHEART, '0.0', '9.9', (
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = -0.02),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = -0.05),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 3.0),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = bg3.euler_to_quaternion(90, 0, 0, sequence='yxz')),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 1),
        ),
        (),
    ))
    t.create_tl_animation(
        bg3.SPEAKER_SHADOWHEART, '0.0', '4.2',
        '73a0acd3-1b93-4bfa-b7f3-be44a431a256',
        '8fc9bad5-96fa-4e4b-9e7f-8126d4187d73',
        fade_in = 0.0,
        fade_out = 0.0,
        enable_root_motion = True)
        #target_transform = t.create_animation_target_transform(
        #    1.0, (-0.04, -0.075, 3.0), bg3.euler_to_quaternion(90, 0, 0, sequence='yxz')
        #))

    # camera shot 2
    t.create_tl_transform(camera_uuid, '4.2', '9.9', (
        (
            t.create_value_key(time = '4.2', interpolation_type = 5, value = 0.5),
        ),
        (
            #t.create_value_key(time = '4.2', interpolation_type = 5, value = 1.75),
            t.create_value_key(time = '16.2', interpolation_type = 5, value = 2.05),
        ),
        (
            t.create_value_key(time = '4.2', interpolation_type = 5, value = 2.4),
        ),
        (
            #t.create_value_key(time = '4.2', interpolation_type = 5, value = bg3.euler_to_quaternion(-58, 12, 0, sequence='yxz')),
            t.create_value_key(time = '16.2', interpolation_type = 5, value = bg3.euler_to_quaternion(-58, 23, 0, sequence='yxz')),
        ),
        (
            t.create_value_key(time = '4.2', interpolation_type = 5, value = 1),
        ),
        (),
    ))

    t.create_tl_animation(
        bg3.SPEAKER_PLAYER, '4.2', '9.9',
        'ad48ef7a-e01d-4894-e41a-c97670e0f45b',
        '494aa8f4-9a3f-4156-a111-befb5461f276',
        #animation_play_start_offset = 3.2,
        animation_play_start_offset = 3.5,
        animation_play_rate = 0.9142857,
        fade_in = 0.0,
        fade_out = 0.0)

    t.create_tl_animation(
        bg3.SPEAKER_SHADOWHEART, '4.2', '9.9',
        '73a0acd3-1b93-4bfa-b7f3-be44a431a256',
        '8fc9bad5-96fa-4e4b-9e7f-8126d4187d73',
        #animation_play_start_offset = 3.2,
        animation_play_start_offset = 3.5,
        animation_play_rate = 0.9142857,
        fade_in = 0.0,
        fade_out = 0.0)
        #target_transform = t.create_animation_target_transform(
        #    1.0, (-0.04, -0.075, 3.0), bg3.euler_to_quaternion(90, 0, 0, sequence='yxz')
        #))

    t.create_tl_voice(bg3.SPEAKER_SHADOWHEART, '4.2', '16.2', dialog_node_uuid, hold_mocap = False)

    
    # camera shot 3
    t.create_tl_camera_fov(camera_uuid, '9.9', '16.2', (
        t.create_value_key(time = 9.9, value = 22.0, value_name = 'FoV', interpolation_type = 3),
    ))
    t.create_tl_transform(camera_uuid, '9.9', '16.2', (
        (
            t.create_value_key(time = 9.9, interpolation_type = 5, value = -1.8),
        ),
        (
            t.create_value_key(time = 9.9, interpolation_type = 5, value = 0.98),
        ),
        (
            t.create_value_key(time = 9.9, interpolation_type = 5, value = 1.95),
        ),
        (
            t.create_value_key(time = 9.9, interpolation_type = 5, value = bg3.euler_to_quaternion(46, -14, 0, sequence='yxz')),
        ),
        (
            t.create_value_key(time = 9.9, interpolation_type = 5, value = 1),
        ),
        (),
    ))

    t.create_tl_animation(
        bg3.SPEAKER_PLAYER, '9.9', '16.2',
        'ad48ef7a-e01d-4894-e41a-c97670e0f45b',
        '494aa8f4-9a3f-4156-a111-befb5461f276',
        #animation_play_start_offset = 3.8,
        animation_play_start_offset = 4.75,
        animation_play_rate = 0.8,
        fade_in = 0.0,
        fade_out = 0.0)

    t.create_tl_transform(bg3.SPEAKER_SHADOWHEART, '9.9', '19.2', (
        (
            t.create_value_key(time = 9.9, interpolation_type = 5, value = -0.02),
        ),
        (
            t.create_value_key(time = 9.9, interpolation_type = 5, value = -0.075),
        ),
        (
            t.create_value_key(time = 9.9, interpolation_type = 5, value = 3.0),
        ),
        (
            t.create_value_key(time = 9.9, interpolation_type = 5, value = bg3.euler_to_quaternion(90, 0, 0, sequence='yxz')),
        ),
        (
            t.create_value_key(time = 9.9, interpolation_type = 5, value = 1),
        ),
        (),
    ))
    t.create_tl_animation(
        bg3.SPEAKER_SHADOWHEART, '9.9', '16.2',
        '73a0acd3-1b93-4bfa-b7f3-be44a431a256',
        '8fc9bad5-96fa-4e4b-9e7f-8126d4187d73',
        #animation_play_start_offset = 3.8,
        animation_play_start_offset = 4.75,
        animation_play_rate = 0.8,
        fade_in = 0.0,
        fade_out = 0.0)
        #target_transform = t.create_animation_target_transform(
        #    1.0, (-0.04, -0.075, 3.0), bg3.euler_to_quaternion(90, 0, 0, sequence='yxz')
        #))

    t.create_tl_animation(
        bg3.SPEAKER_PLAYER, '15.67', '18.89',
        'c26b9b0a-20cc-44a4-a499-18d6d78abec5',
        '2b7b7a61-dbaf-4b0a-baf0-be4e414128f3',
        animation_slot = 1,
        animation_play_rate = 0.2,
        animation_play_start_offset = 7.5,
        fade_in = 2.0,
        fade_out = 0.0)

    # camera shot 3.1
    t.create_tl_camera_fov(camera_uuid, '16.2', '19.2', (
        t.create_value_key(time = '16.2', value = 30.0, value_name = 'FoV', interpolation_type = 3),
    ))
    t.create_tl_transform(camera_uuid, '16.2', '19.2', (
        (
            t.create_value_key(time = '16.2', interpolation_type = 5, value = 0.5),
        ),
        (
            t.create_value_key(time = '16.2', interpolation_type = 5, value = 2.05),
        ),
        (
            t.create_value_key(time = '16.2', interpolation_type = 5, value = 2.4),
        ),
        (
            t.create_value_key(time = '16.2', interpolation_type = 5, value = bg3.euler_to_quaternion(-58, 23, 0, sequence='yxz')),
        ),
        (
            t.create_value_key(time = '16.2', interpolation_type = 5, value = 1),
        ),
        (),
    ))
    t.create_tl_transform(bg3.SPEAKER_SHADOWHEART, '16.2', '19.2', (
        (
            t.create_value_key(time = '16.2', interpolation_type = 5, value = -0.02),
        ),
        (
            t.create_value_key(time = '16.2', interpolation_type = 5, value = -0.08),
        ),
        (
            t.create_value_key(time = '16.2', interpolation_type = 5, value = 2.96),
        ),
        (
            t.create_value_key(time = '16.2', interpolation_type = 5, value = bg3.euler_to_quaternion(90, 0, 0, sequence='yxz')),
        ),
        (
            t.create_value_key(time = '16.2', interpolation_type = 5, value = 1),
        ),
        (),
    ))

    t.create_tl_animation(
        bg3.SPEAKER_PLAYER, '16.2', '19.2',
        'ad48ef7a-e01d-4894-e41a-c97670e0f45b',
        '494aa8f4-9a3f-4156-a111-befb5461f276',
        animation_play_start_offset = 8.5,
        fade_in = 0.0,
        fade_out = 0.0)
    t.create_tl_animation(
        bg3.SPEAKER_SHADOWHEART, '16.2', '19.2',
        '73a0acd3-1b93-4bfa-b7f3-be44a431a256',
        '8fc9bad5-96fa-4e4b-9e7f-8126d4187d73',
        animation_play_start_offset = 8.5,
        fade_in = 0.0,
        fade_out = 0.0)

    t.create_tl_animation(
        bg3.SPEAKER_PLAYER, '18.89', '22.4',
        'a0e37a8e-c619-4d0a-840a-061831fb0523',
        '2b7b7a61-dbaf-4b0a-baf0-be4e414128f3',
        animation_slot = 1,
        animation_play_rate = 0.9,
        animation_play_start_offset = 4.02,
        fade_in = 0.0,
        fade_out = 2.0)

    # camera shot 4
    t.create_tl_camera_fov(camera_uuid, '19.2', '21.3', (
        t.create_value_key(time = '19.2', value = 30.0, value_name = 'FoV', interpolation_type = 3),
    ))
    t.create_tl_transform(camera_uuid, '19.2', '21.3', (
        (
            t.create_value_key(time = '19.2', interpolation_type = 5, value = -2.3),
        ),
        (
            t.create_value_key(time = '19.2', interpolation_type = 5, value = 1.6),
        ),
        (
            t.create_value_key(time = '19.2', interpolation_type = 5, value = 2.3),
        ),
        (
            t.create_value_key(time = '19.2', interpolation_type = 5, value = bg3.euler_to_quaternion(72, 8, 0, sequence='yxz')),
        ),
        (
            t.create_value_key(time = '19.2', interpolation_type = 5, value = 1),
        ),
        (),
    ))
    t.create_tl_transform(bg3.SPEAKER_SHADOWHEART, '19.2', '21.3', (
        (
            t.create_value_key(time = '19.2', interpolation_type = 5, value = -0.02),
        ),
        (
            t.create_value_key(time = '19.2', interpolation_type = 5, value = -0.075),
        ),
        (
            t.create_value_key(time = '19.2', interpolation_type = 5, value = 3.0),
        ),
        (
            t.create_value_key(time = '19.2', interpolation_type = 5, value = bg3.euler_to_quaternion(90, 0, 0, sequence='yxz')),
        ),
        (
            t.create_value_key(time = '19.2', interpolation_type = 5, value = 1),
        ),
        (),
    ))

    t.create_tl_animation(
        bg3.SPEAKER_PLAYER, '19.2', phase_duration,
        'ad48ef7a-e01d-4894-e41a-c97670e0f45b',
        '494aa8f4-9a3f-4156-a111-befb5461f276',
        animation_play_start_offset = 12.2,
        fade_in = 0.0,
        fade_out = 0.0)
    t.create_tl_animation(
        bg3.SPEAKER_SHADOWHEART, '19.2', phase_duration,
        '73a0acd3-1b93-4bfa-b7f3-be44a431a256',
        '8fc9bad5-96fa-4e4b-9e7f-8126d4187d73',
        animation_play_start_offset = 12.2,
        fade_in = 0.0,
        fade_out = 0.0)

    """
    t.create_tl_animation(
        bg3.SPEAKER_PLAYER, '17.7', phase_duration,
        'ad48ef7a-e01d-4894-e41a-c97670e0f45b',
        '494aa8f4-9a3f-4156-a111-befb5461f276',
        animation_play_start_offset = 10.7,
        fade_in = 0.0,
        fade_out = 0.0)

    t.create_tl_animation(
        bg3.SPEAKER_SHADOWHEART, '17.7', phase_duration,
        '73a0acd3-1b93-4bfa-b7f3-be44a431a256',
        '8fc9bad5-96fa-4e4b-9e7f-8126d4187d73',
        animation_play_start_offset = 10.7,
        fade_in = 0.0,
        fade_out = 0.0)
        #target_transform = t.create_animation_target_transform(
        #    1.0, (-0.04, -0.075, 3.0), bg3.euler_to_quaternion(90, 0, 0, sequence='yxz')
        #))
    """

    # camera shot 5
    t.create_tl_camera_fov(camera_uuid, '21.3', '25.3', (
        t.create_value_key(time = '21.3', value = 22.0, value_name = 'FoV', interpolation_type = 3),
    ))
    t.create_tl_transform(bg3.SPEAKER_SHADOWHEART, '21.3', '25.3', (
        (
            t.create_value_key(time = '21.3', interpolation_type = 5, value = 0.0),
        ),
        (
            t.create_value_key(time = '21.3', interpolation_type = 5, value = -0.08),
        ),
        (
            t.create_value_key(time = '21.3', interpolation_type = 5, value = 2.96),
        ),
        (
            t.create_value_key(time = '21.3', interpolation_type = 5, value = bg3.euler_to_quaternion(90, 0, 0, sequence='yxz')),
        ),
        (
            t.create_value_key(time = '21.3', interpolation_type = 5, value = 1),
        ),
        (),
    ))
    t.create_tl_transform(camera_uuid, '21.3', '25.3', (
        (
            #t.create_value_key(time = '21.3', interpolation_type = 5, value = -0.6),
            t.create_value_key(time = '21.3', interpolation_type = 5, value = -0.1),
        ),
        (
            t.create_value_key(time = '21.3', interpolation_type = 5, value = 2.1),
        ),
        (
            #t.create_value_key(time = '21.3', interpolation_type = 5, value = 0.8),
            t.create_value_key(time = '21.3', interpolation_type = 5, value = 1.9),
        ),
        (
            #t.create_value_key(time = '21.3', interpolation_type = 5, value = bg3.euler_to_quaternion(3, 17, 0, sequence='yxz')),
            t.create_value_key(time = '21.3', interpolation_type = 5, value = bg3.euler_to_quaternion(-24, 28, 0, sequence='yxz')),
        ),
        (
            t.create_value_key(time = '21.3', interpolation_type = 5, value = 1),
        ),
        (),
    ))

    # camera shot 6
    t.create_tl_camera_fov(camera_uuid, '25.3', '33.3', (
        t.create_value_key(time = '25.3', value = 30.0, value_name = 'FoV', interpolation_type = 3),
    ))
    t.create_tl_transform(bg3.SPEAKER_SHADOWHEART, '25.3', '33.3', (
        (
            t.create_value_key(time = '25.3', interpolation_type = 5, value = 0.01),
        ),
        (
            t.create_value_key(time = '25.3', interpolation_type = 5, value = -0.075),
        ),
        (
            t.create_value_key(time = '25.3', interpolation_type = 5, value = 2.96),
        ),
        (
            t.create_value_key(time = '25.3', interpolation_type = 5, value = bg3.euler_to_quaternion(90, 0, 0, sequence='yxz')),
        ),
        (
            t.create_value_key(time = '25.3', interpolation_type = 5, value = 1),
        ),
        (),
    ))
    t.create_tl_transform(camera_uuid, '25.3', '33.3', (
        (
            t.create_value_key(time = '25.3', interpolation_type = 5, value = -0.6),
        ),
        (
            t.create_value_key(time = '25.3', interpolation_type = 5, value = 2.1),
        ),
        (
            t.create_value_key(time = '25.3', interpolation_type = 5, value = 0.8),
        ),
        (
            t.create_value_key(time = '25.3', interpolation_type = 5, value = bg3.euler_to_quaternion(3, 17, 0, sequence='yxz')),
        ),
        (
            t.create_value_key(time = '25.3', interpolation_type = 5, value = 1),
        ),
        (),
    ))

    # camera shot 7
    t.create_tl_camera_fov(camera_uuid, '33.3', '39.5', (
        t.create_value_key(time = '33.3', value = 15.0, value_name = 'FoV', interpolation_type = 3),
    ))
    t.create_tl_transform(bg3.SPEAKER_SHADOWHEART, '33.3', phase_duration, (
        (
            t.create_value_key(time = '33.3', interpolation_type = 5, value = 0.01),
        ),
        (
            t.create_value_key(time = '33.3', interpolation_type = 5, value = -0.08),
        ),
        (
            t.create_value_key(time = '33.3', interpolation_type = 5, value = 2.95),
        ),
        (
            t.create_value_key(time = '33.3', interpolation_type = 5, value = bg3.euler_to_quaternion(90, 0, 0, sequence='yxz')),
        ),
        (
            t.create_value_key(time = '33.3', interpolation_type = 5, value = 1),
        ),
        (),
    ))
    t.create_tl_transform(camera_uuid, '33.3', '39.5', (
        (
            t.create_value_key(time = '33.3', interpolation_type = 5, value = -0.4),
        ),
        (
            t.create_value_key(time = '33.3', interpolation_type = 5, value = 2.1),
        ),
        (
            t.create_value_key(time = '33.3', interpolation_type = 5, value = 0.8),
        ),
        (
            t.create_value_key(time = '33.3', interpolation_type = 5, value = bg3.euler_to_quaternion(-2, 12, 0, sequence='yxz')),
        ),
        (
            t.create_value_key(time = '33.3', interpolation_type = 5, value = 1),
        ),
        (),
    ))

    # camera shot 8
    t.create_tl_camera_fov(camera_uuid, '39.5', phase_duration, (
        t.create_value_key(time = '39.5', value = 30.0, value_name = 'FoV', interpolation_type = 3),
    ))
    t.create_tl_transform(camera_uuid, '39.5', phase_duration, (
        (
            t.create_value_key(time = '39.5', interpolation_type = 5, value = -0.6),
        ),
        (
            t.create_value_key(time = '39.5', interpolation_type = 5, value = 2.1),
        ),
        (
            t.create_value_key(time = '39.5', interpolation_type = 5, value = 0.8),
        ),
        (
            t.create_value_key(time = '39.5', interpolation_type = 5, value = bg3.euler_to_quaternion(3, 17, 0, sequence='yxz')),
        ),
        (
            t.create_value_key(time = '39.5', interpolation_type = 5, value = 1),
        ),
        (),
    ))

    """
    # camera shot 6
    t.create_tl_camera_fov(camera_uuid, '27.0', phase_duration, (
        t.create_value_key(time = '27.0', value = 25.0, value_name = 'FoV', interpolation_type = 3),
    ))
    t.create_tl_transform(camera_uuid, '27.0', phase_duration, (
        (
            t.create_value_key(time = '27.0', interpolation_type = 5, value = -0.8),
        ),
        (
            t.create_value_key(time = '27.0', interpolation_type = 5, value = 2.0),
        ),
        (
            t.create_value_key(time = '27.0', interpolation_type = 5, value = 0.7),
        ),
        (
            t.create_value_key(time = '27.0', interpolation_type = 5, value = bg3.euler_to_quaternion(8, 15, 0, sequence='yxz')),
        ),
        (
            t.create_value_key(time = '27.0', interpolation_type = 5, value = 1),
        ),
        (),
    ))
    t.create_tl_transform(bg3.SPEAKER_SHADOWHEART, '27.0', phase_duration, (
        (
            t.create_value_key(time = '27.0', interpolation_type = 5, value = 0.01),
        ),
        (
            t.create_value_key(time = '27.0', interpolation_type = 5, value = -0.075),
        ),
        (
            t.create_value_key(time = '27.0', interpolation_type = 5, value = 3.0),
        ),
        (
            t.create_value_key(time = '27.0', interpolation_type = 5, value = bg3.euler_to_quaternion(90, 0, 0, sequence='yxz')),
        ),
        (
            t.create_value_key(time = '27.0', interpolation_type = 5, value = 1),
        ),
        (),
    ))
    """


    t.create_tl_animation(
        bg3.SPEAKER_PLAYER, '29.06', '34.2',
        'c26b9b0a-20cc-44a4-a499-18d6d78abec5',
        '2b7b7a61-dbaf-4b0a-baf0-be4e414128f3',
        animation_slot = 1,
        animation_play_start_offset = 1.0,
        fade_in = 2.0,
        fade_out = 0.0
    )
    t.create_tl_animation(
        bg3.SPEAKER_SHADOWHEART, '29.06', '34.2',
        'a0e37a8e-c619-4d0a-840a-061831fb0523',
        '7871ce8b-b26e-48c2-969b-347c61560f95',
        animation_slot = 1,
        animation_play_start_offset = 1.8,
        fade_in = 2.0,
        fade_out = 0.0
    )
    t.create_tl_animation(
        bg3.SPEAKER_SHADOWHEART, '34.2', '36.82',
        'a0e37a8e-c619-4d0a-840a-061831fb0523',
        '7871ce8b-b26e-48c2-969b-347c61560f95',
        animation_slot = 1,
        animation_play_start_offset = 6.804,
        fade_in = 0.0,
        fade_out = 2.0
    )
    t.create_tl_animation(
        bg3.SPEAKER_PLAYER, '34.2', '37.05',
        'a0e37a8e-c619-4d0a-840a-061831fb0523',
        '2b7b7a61-dbaf-4b0a-baf0-be4e414128f3',
        animation_slot = 1,
        animation_play_start_offset = 6.804,
        fade_in = 0.0,
        fade_out = 2.0
    )


def create_proposal_cinematic_bt2(dialog_node_uuid: str, t: bg3.timeline_object) -> None:

    phase_duration = '40.38'
    t.create_new_phase(dialog_node_uuid, phase_duration)

    t.create_tl_actor_node(bg3.timeline_object.ATTITUDE, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.ATTITUDE, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (), is_snapped_to_end = True)

    t.create_tl_actor_node(bg3.timeline_object.EMOTION, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        t.create_emotion_key(0.0, 2),
        t.create_emotion_key(5.49, 2, variation = 1),
        t.create_emotion_key(9.97 + 7.0, 256, variation = 24),
        t.create_emotion_key(10.9 + 7.0, 256, variation = 25),
        t.create_emotion_key(14.2 + 7.0, 16, is_sustained = False),
        t.create_emotion_key(17.64 + 7.0, 2, variation = 1, is_sustained = False),
        t.create_emotion_key(30.32 + 7.0, 2),
        t.create_emotion_key(32.39 + 7.0, 2, variation = 1, is_sustained = False)
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.EMOTION, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_emotion_key(0.5, 64),
        t.create_emotion_key(4.2, 2),
        t.create_emotion_key(10.2, 2, variation = 2, is_sustained = False),
        t.create_emotion_key(11.7, 2, variation = 1, is_sustained = False),
        t.create_emotion_key(13.8, 2, variation = 2, is_sustained = False),
        t.create_emotion_key(9.74 + 7.0, 2, variation = 1, is_sustained = False),
        t.create_emotion_key(20.0, 2, variation = 23, is_sustained = False),
        t.create_emotion_key(20.8, 2, variation = 1, is_sustained = False),
        t.create_emotion_key(25.05 + 7.0, 2, is_sustained = False),
        t.create_emotion_key(28.49 + 7.0, 2, variation = 2, is_sustained = False),
        t.create_emotion_key(29.36 + 7.0, 2, variation = 23, is_sustained = False),
        t.create_emotion_key(30.27 + 7.0, 2, variation = 1),
        t.create_emotion_key(32.0 + 7.0, 2, variation = 24),
        t.create_emotion_key(32.36 + 7.0, 2, variation = 2)
    ), is_snapped_to_end = True)

    t.create_tl_actor_node(bg3.timeline_object.LOOK_AT, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        t.create_look_at_key(
            0.0,
            turn_mode = 3,
            turn_speed_multiplier = 0.3,
            head_turn_speed_multiplier = 0.3,
            weight = 0.0,
            safe_zone_angle = 80.0,
            head_safe_zone_angle = 80.0,
            look_at_mode = 0),
        t.create_look_at_key(
            '1.86',
            target = bg3.SPEAKER_SHADOWHEART,
            bone = 'Head_M',
            turn_mode = 3,
            turn_speed_multiplier = 0.3,
            head_turn_speed_multiplier = 0.3,
            weight = 0.0,
            safe_zone_angle = 80.0,
            head_safe_zone_angle = 80.0,
            offset = (0, -0.3, 0),
            is_eye_look_at_enabled = True,
            eye_look_at_target_id = bg3.SPEAKER_SHADOWHEART,
            eye_look_at_bone = 'Head_M'
        ),
        t.create_look_at_key(
            '6.62',
            turn_mode = 3,
            turn_speed_multiplier = 0.3,
            head_turn_speed_multiplier = 0.3,
            weight = 0.0,
            safe_zone_angle = 80.0,
            head_safe_zone_angle = 80.0,
            look_at_mode = 0,
            is_eye_look_at_enabled = True),
        t.create_look_at_key(
            12.68,
            target = bg3.SPEAKER_SHADOWHEART,
            bone = 'Head_M',
            turn_mode = 3,
            turn_speed_multiplier = 0.3,
            head_turn_speed_multiplier = 0.3,
            weight = 0.0,
            safe_zone_angle = 80.0,
            head_safe_zone_angle = 80.0,
            look_at_mode = 1,
            eye_look_at_target_id = bg3.SPEAKER_SHADOWHEART,
            eye_look_at_bone = 'Head_M')
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.LOOK_AT, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_look_at_key(
            0.0,
            target = bg3.SPEAKER_PLAYER,
            bone = 'Head_M',
            turn_mode = 3,
            turn_speed_multiplier = 0.3,
            head_turn_speed_multiplier = 0.3,
            weight = 0.0,
            safe_zone_angle = 80.0,
            head_safe_zone_angle = 80.0,
            look_at_mode = 1,
            eye_look_at_bone = 'Head_M'),
    ), is_snapped_to_end = True)

    # Shadowheart theme
    t.create_tl_actor_node(bg3.timeline_object.SOUND, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_sound_event_key(0.0, sound_event_id = 'ec19d32b-1213-4166-ba20-405994e62381'),
    ))

    t.create_tl_actor_node(bg3.timeline_object.SOUND, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (), is_snapped_to_end = True)
    """
    t.create_tl_actor_node(bg3.timeline_object.SOUND, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.SOUND, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
    ), is_snapped_to_end = True)
    """
    t.create_tl_actor_node(bg3.timeline_object.SOUND, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        t.create_sound_event_key('16.67', sound_event_id = '6dbe237a-0c78-4023-a6b7-30349e0505db', sound_object_index = 4),
        t.create_sound_event_key('16.7', sound_event_id = 'c232329e-2d4e-4f0c-a4d4-ea1585fce27c', sound_object_index = 4),
        t.create_sound_event_key('16.74', sound_event_id = '6ffc5af2-ae64-48a2-9068-4996d4cdceab', sound_object_index = 4),
        t.create_sound_event_key('21.8', sound_event_id = 'c232329e-2d4e-4f0c-a4d4-ea1585fce27c', sound_object_index = 4),
        #t.create_sound_event_key(21.9, sound_event_id = 'c232329e-2d4e-4f0c-a4d4-ea1585fce27c', sound_object_index = 4),
        t.create_sound_event_key('30.46', sound_event_id = '6ffc5af2-ae64-48a2-9068-4996d4cdceab', sound_object_index = 4),
        t.create_sound_event_key('30.48', sound_event_id = '5dac329f-b08a-412d-84bc-86fc1aecae45', sound_object_index = 4),
        t.create_sound_event_key('32.23', sound_event_id = 'ffbbbd57-5c31-444d-bc3a-c3d14df0be53', sound_object_index = 4),
        t.create_sound_event_key('35.19', sound_event_id = '5dac329f-b08a-412d-84bc-86fc1aecae45', sound_object_index = 4),
    ), is_snapped_to_end = True)

    t.create_tl_actor_node(bg3.timeline_object.SOUND, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        t.create_sound_event_key(25.91, sound_type = 4),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.SOUND, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        t.create_sound_event_key(2.43, sound_event_id = 'd572362f-b64c-4836-9c1d-4399507162fb')
    ), is_snapped_to_end = True)

    t.create_tl_actor_node(bg3.timeline_object.PHYSICS, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        t.create_value_key(time = 0.0, interpolation_type = 3),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.PHYSICS, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_value_key(time = 0.0, interpolation_type = 3),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.HANDS_IK, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        t.create_value_key(time = 0.0, interpolation_type = 3, value_name = 'InverseKinematics', value = False),
        t.create_value_key(time = 4.26, interpolation_type = 3),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.HANDS_IK, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_value_key(time = 0.0, interpolation_type = 3, value_name = 'InverseKinematics', value = False),
        t.create_value_key(time = 4.26, interpolation_type = 3),
    ), is_snapped_to_end = True)

    # Shadowheart
    t.create_tl_transform(bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 0.06),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 0.0),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 3.0),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = bg3.euler_to_quaternion(90, 0, 0, sequence='yxz')),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 1),
        ),
        (),
    ))

    # Tav
    t.create_tl_transform(bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = -1.219),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 0.0),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 3.0),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = bg3.euler_to_quaternion(-90, 0, 0, sequence='yxz')),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 1),
        ),
        (),
    ))

    camera_uuid = '91f50bea-c8cc-4c34-b618-227519017779'

    t.create_tl_camera_fov(camera_uuid, '0.0', phase_duration, (
        t.create_value_key(time = 0.0, value = 30.0, value_name = 'FoV', interpolation_type = 3),
    ), is_snapped_to_end = True)

    # camera shot 1
    t.create_tl_transform(camera_uuid, '0.0', '4.2', (
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = -1.9),
            t.create_value_key(time = '4.2', interpolation_type = 5, value = -1.55),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 1.0),
            t.create_value_key(time = '4.2', interpolation_type = 5, value = 1.10),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 2.1),
            t.create_value_key(time = '4.2', interpolation_type = 5, value = 1.15),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = bg3.euler_to_quaternion(62, -18, 0, sequence='yxz')),
            t.create_value_key(time = '4.2', interpolation_type = 5, value = bg3.euler_to_quaternion(27, -6, 0, sequence='yxz')),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 1),
        ),
        (),
    ))
    t.create_tl_shot(camera_uuid, '0.0', phase_duration, is_snapped_to_end = True)

    t.create_tl_animation(
        bg3.SPEAKER_PLAYER, '0.0', '4.2',
        'ad48ef7a-e01d-4894-e41a-c97670e0f45b',
        '494aa8f4-9a3f-4156-a111-befb5461f276',
        fade_in = 0.0,
        fade_out = 0.0,
        offset_type = 5)
    t.create_tl_animation(
        bg3.SPEAKER_SHADOWHEART, '0.0', '4.2',
        '73a0acd3-1b93-4bfa-b7f3-be44a431a256',
        '8fc9bad5-96fa-4e4b-9e7f-8126d4187d73',
        fade_in = 0.0,
        fade_out = 0.0,
        offset_type = 5)


    """
    t.create_tl_transform(camera_uuid, '4.2', '9.9', (
        (
            t.create_value_key(time = '4.2', interpolation_type = 5, value = 0.5),
        ),
        (
            t.create_value_key(time = '4.2', interpolation_type = 5, value = 1.8),
        ),
        (
            t.create_value_key(time = '4.2', interpolation_type = 5, value = 2.6),
        ),
        (
            t.create_value_key(time = '4.2', interpolation_type = 5, value = bg3.euler_to_quaternion(-62, 14, 0, sequence='yxz')),
        ),
        (
            t.create_value_key(time = '4.2', interpolation_type = 5, value = 1),
        ),
        (),
    ))"""

    # camera shot 2
    t.create_tl_transform(camera_uuid, '4.2', '9.9', (
        (
            t.create_value_key(time = '16.2', interpolation_type = 5, value = 0.5),
        ),
        (
            t.create_value_key(time = '16.2', interpolation_type = 5, value = 2.05),
        ),
        (
            t.create_value_key(time = '16.2', interpolation_type = 5, value = 2.4),
        ),
        (
            t.create_value_key(time = '16.2', interpolation_type = 5, value = bg3.euler_to_quaternion(-58, 23, 0, sequence='yxz')),
        ),
        (
            t.create_value_key(time = '16.2', interpolation_type = 5, value = 1),
        ),
        (),
    ))

    t.create_tl_animation(
        bg3.SPEAKER_PLAYER, '4.2', '9.9',
        'ad48ef7a-e01d-4894-e41a-c97670e0f45b',
        '494aa8f4-9a3f-4156-a111-befb5461f276',
        #animation_play_start_offset = 3.2,
        animation_play_start_offset = 3.5,
        animation_play_rate = 0.9142857,
        fade_in = 0.0,
        fade_out = 0.0)
    t.create_tl_animation(
        bg3.SPEAKER_SHADOWHEART, '4.2', '9.9',
        '73a0acd3-1b93-4bfa-b7f3-be44a431a256',
        '8fc9bad5-96fa-4e4b-9e7f-8126d4187d73',
        #animation_play_start_offset = 3.2,
        animation_play_start_offset = 3.5,
        animation_play_rate = 0.9142857,
        fade_in = 0.0,
        fade_out = 0.0)

    t.create_tl_voice(bg3.SPEAKER_SHADOWHEART, '4.2', '16.2', dialog_node_uuid, hold_mocap = False)

    
    # camera shot 3
    t.create_tl_camera_fov(camera_uuid, '9.9', '16.2', (
        t.create_value_key(time = 9.9, value = 22.0, value_name = 'FoV', interpolation_type = 3),
    ))
    t.create_tl_transform(camera_uuid, '9.9', '16.2', (
        (
            t.create_value_key(time = 9.9, interpolation_type = 5, value = -1.8),
        ),
        (
            t.create_value_key(time = 9.9, interpolation_type = 5, value = 1.04),
        ),
        (
            t.create_value_key(time = 9.9, interpolation_type = 5, value = 1.95),
        ),
        (
            t.create_value_key(time = 11.9, interpolation_type = 5, value = bg3.euler_to_quaternion(46, -14, 0, sequence='yxz')),
        ),
        (
            t.create_value_key(time = 9.9, interpolation_type = 5, value = 1),
        ),
        (),
    ))

    t.create_tl_animation(
        bg3.SPEAKER_PLAYER, '9.9', '16.2',
        'ad48ef7a-e01d-4894-e41a-c97670e0f45b',
        '494aa8f4-9a3f-4156-a111-befb5461f276',
        #animation_play_start_offset = 3.8,
        animation_play_start_offset = 4.75,
        animation_play_rate = 0.8,
        fade_in = 0.0,
        fade_out = 0.0)
    t.create_tl_animation(
        bg3.SPEAKER_SHADOWHEART, '9.9', '16.2',
        '73a0acd3-1b93-4bfa-b7f3-be44a431a256',
        '8fc9bad5-96fa-4e4b-9e7f-8126d4187d73',
        animation_play_start_offset = 4.75,
        animation_play_rate = 0.8,
        fade_in = 0.0,
        fade_out = 0.0)

    t.create_tl_animation(
        bg3.SPEAKER_PLAYER, '15.67', '18.89',
        'c26b9b0a-20cc-44a4-a499-18d6d78abec5',
        '2b7b7a61-dbaf-4b0a-baf0-be4e414128f3',
        animation_slot = 1,
        animation_play_rate = 0.2,
        animation_play_start_offset = 7.5,
        fade_in = 2.0,
        fade_out = 0.0)

    # camera shot 3.1
    t.create_tl_camera_fov(camera_uuid, '16.2', '19.2', (
        t.create_value_key(time = '16.2', value = 30.0, value_name = 'FoV', interpolation_type = 3),
    ))
    t.create_tl_transform(camera_uuid, '16.2', '19.2', (
        (
            t.create_value_key(time = '16.2', interpolation_type = 5, value = 0.5),
        ),
        (
            t.create_value_key(time = '16.2', interpolation_type = 5, value = 2.05),
        ),
        (
            t.create_value_key(time = '16.2', interpolation_type = 5, value = 2.4),
        ),
        (
            t.create_value_key(time = '16.2', interpolation_type = 5, value = bg3.euler_to_quaternion(-58, 23, 0, sequence='yxz')),
        ),
        (
            t.create_value_key(time = '16.2', interpolation_type = 5, value = 1),
        ),
        (),
    ))

    t.create_tl_animation(
        bg3.SPEAKER_PLAYER, '16.2', '19.2',
        'ad48ef7a-e01d-4894-e41a-c97670e0f45b',
        '494aa8f4-9a3f-4156-a111-befb5461f276',
        animation_play_start_offset = 8.5,
        fade_in = 0.0,
        fade_out = 0.0)
    t.create_tl_animation(
        bg3.SPEAKER_SHADOWHEART, '16.2', '19.2',
        '73a0acd3-1b93-4bfa-b7f3-be44a431a256',
        '8fc9bad5-96fa-4e4b-9e7f-8126d4187d73',
        animation_play_start_offset = 8.5,
        fade_in = 0.0,
        fade_out = 0.0)

    t.create_tl_animation(
        bg3.SPEAKER_PLAYER, '18.89', '22.4',
        'a0e37a8e-c619-4d0a-840a-061831fb0523',
        '2b7b7a61-dbaf-4b0a-baf0-be4e414128f3',
        animation_slot = 1,
        animation_play_rate = 0.9,
        animation_play_start_offset = 4.02,
        fade_in = 0.0,
        fade_out = 2.0)

    # camera shot 4
    t.create_tl_camera_fov(camera_uuid, '19.2', '21.3', (
        t.create_value_key(time = '19.2', value = 30.0, value_name = 'FoV', interpolation_type = 3),
    ))
    t.create_tl_transform(camera_uuid, '19.2', '21.3', (
        (
            t.create_value_key(time = '19.2', interpolation_type = 5, value = -2.3),
        ),
        (
            t.create_value_key(time = '19.2', interpolation_type = 5, value = 1.6),
        ),
        (
            t.create_value_key(time = '19.2', interpolation_type = 5, value = 2.3),
        ),
        (
            t.create_value_key(time = '19.2', interpolation_type = 5, value = bg3.euler_to_quaternion(72, 8, 0, sequence='yxz')),
        ),
        (
            t.create_value_key(time = '19.2', interpolation_type = 5, value = 1),
        ),
        (),
    ))

    t.create_tl_animation(
        bg3.SPEAKER_PLAYER, '19.2', phase_duration,
        'ad48ef7a-e01d-4894-e41a-c97670e0f45b',
        '494aa8f4-9a3f-4156-a111-befb5461f276',
        animation_play_start_offset = 12.2,
        fade_in = 0.0,
        fade_out = 0.0)
    t.create_tl_animation(
        bg3.SPEAKER_SHADOWHEART, '19.2', phase_duration,
        '73a0acd3-1b93-4bfa-b7f3-be44a431a256',
        '8fc9bad5-96fa-4e4b-9e7f-8126d4187d73',
        animation_play_start_offset = 12.2,
        fade_in = 0.0,
        fade_out = 0.0)

    # camera shot 5
    t.create_tl_camera_fov(camera_uuid, '21.3', '25.3', (
        t.create_value_key(time = '21.3', value = 22.0, value_name = 'FoV', interpolation_type = 3),
    ))
    t.create_tl_transform(camera_uuid, '21.3', '25.3', (
        (
            #t.create_value_key(time = '21.3', interpolation_type = 5, value = -0.5),
            t.create_value_key(time = '21.3', interpolation_type = 5, value = -0.1),
        ),
        (
            t.create_value_key(time = '21.3', interpolation_type = 5, value = 2.1),
        ),
        (
            #t.create_value_key(time = '21.3', interpolation_type = 5, value = 0.8),
            t.create_value_key(time = '21.3', interpolation_type = 5, value = 1.9),
        ),
        (
            #t.create_value_key(time = '21.3', interpolation_type = 5, value = bg3.euler_to_quaternion(-15, 17, 0, sequence='yxz')),
            t.create_value_key(time = '21.3', interpolation_type = 5, value = bg3.euler_to_quaternion(-24, 28, 0, sequence='yxz')),
        ),
        (
            t.create_value_key(time = '21.3', interpolation_type = 5, value = 1),
        ),
        (),
    ))

    # camera shot 6
    t.create_tl_camera_fov(camera_uuid, '25.3', '33.3', (
        t.create_value_key(time = '25.3', value = 30.0, value_name = 'FoV', interpolation_type = 3),
    ))
    t.create_tl_transform(camera_uuid, '25.3', '33.3', (
        (
            t.create_value_key(time = '25.3', interpolation_type = 5, value = -0.6),
        ),
        (
            t.create_value_key(time = '25.3', interpolation_type = 5, value = 2.1),
        ),
        (
            t.create_value_key(time = '25.3', interpolation_type = 5, value = 0.8),
        ),
        (
            t.create_value_key(time = '25.3', interpolation_type = 5, value = bg3.euler_to_quaternion(3, 17, 0, sequence='yxz')),
        ),
        (
            t.create_value_key(time = '25.3', interpolation_type = 5, value = 1),
        ),
        (),
    ))

    # camera shot 7
    t.create_tl_camera_fov(camera_uuid, '33.3', '39.5', (
        t.create_value_key(time = '33.3', value = 15.0, value_name = 'FoV', interpolation_type = 3),
    ))
    t.create_tl_transform(camera_uuid, '33.3', '39.5', (
        (
            t.create_value_key(time = '33.3', interpolation_type = 5, value = -0.4),
        ),
        (
            t.create_value_key(time = '33.3', interpolation_type = 5, value = 2.1),
        ),
        (
            t.create_value_key(time = '33.3', interpolation_type = 5, value = 0.8),
        ),
        (
            t.create_value_key(time = '33.3', interpolation_type = 5, value = bg3.euler_to_quaternion(-2, 12, 0, sequence='yxz')),
        ),
        (
            t.create_value_key(time = '33.3', interpolation_type = 5, value = 1),
        ),
        (),
    ))

    # camera shot 8
    t.create_tl_camera_fov(camera_uuid, '39.5', phase_duration, (
        t.create_value_key(time = 39.5, value = 30.0, value_name = 'FoV', interpolation_type = 3),
    ))
    t.create_tl_transform(camera_uuid, '39.5', phase_duration, (
        (
            t.create_value_key(time = '25.3', interpolation_type = 5, value = -0.6),
        ),
        (
            t.create_value_key(time = '25.3', interpolation_type = 5, value = 2.1),
        ),
        (
            t.create_value_key(time = '25.3', interpolation_type = 5, value = 0.8),
        ),
        (
            t.create_value_key(time = '25.3', interpolation_type = 5, value = bg3.euler_to_quaternion(3, 17, 0, sequence='yxz')),
        ),
        (
            t.create_value_key(time = '25.3', interpolation_type = 5, value = 1),
        ),
        (),
    ))

    t.create_tl_animation(
        bg3.SPEAKER_PLAYER, '29.06', '34.2',
        'c26b9b0a-20cc-44a4-a499-18d6d78abec5',
        '2b7b7a61-dbaf-4b0a-baf0-be4e414128f3',
        animation_slot = 1,
        animation_play_start_offset = 1.0,
        fade_in = 2.0,
        fade_out = 0.0
    )
    t.create_tl_animation(
        bg3.SPEAKER_SHADOWHEART, '29.06', '34.2',
        'a0e37a8e-c619-4d0a-840a-061831fb0523',
        '7871ce8b-b26e-48c2-969b-347c61560f95',
        animation_slot = 1,
        animation_play_start_offset = 1.8,
        fade_in = 2.0,
        fade_out = 0.0
    )
    t.create_tl_animation(
        bg3.SPEAKER_SHADOWHEART, '34.2', '36.82',
        'a0e37a8e-c619-4d0a-840a-061831fb0523',
        '7871ce8b-b26e-48c2-969b-347c61560f95',
        animation_slot = 1,
        animation_play_start_offset = 6.804,
        fade_in = 0.0,
        fade_out = 2.0
    )
    t.create_tl_animation(
        bg3.SPEAKER_PLAYER, '34.2', '37.05',
        'a0e37a8e-c619-4d0a-840a-061831fb0523',
        '2b7b7a61-dbaf-4b0a-baf0-be4e414128f3',
        animation_slot = 1,
        animation_play_start_offset = 6.804,
        fade_in = 0.0,
        fade_out = 2.0
    )


def create_proposal_cinematic_bt3(dialog_node_uuid: str, t: bg3.timeline_object) -> None:

    phase_duration = '40.38'
    t.create_new_phase(dialog_node_uuid, phase_duration)

    t.create_tl_actor_node(bg3.timeline_object.ATTITUDE, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.ATTITUDE, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (), is_snapped_to_end = True)

    t.create_tl_actor_node(bg3.timeline_object.EMOTION, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        t.create_emotion_key(0.0, 2),
        t.create_emotion_key(5.49, 2, variation = 1),
        t.create_emotion_key(9.97 + 7.0, 256, variation = 24),
        t.create_emotion_key(10.9 + 7.0, 256, variation = 25),
        t.create_emotion_key(14.2 + 7.0, 16, is_sustained = False),
        t.create_emotion_key(17.64 + 7.0, 2, variation = 1, is_sustained = False),
        t.create_emotion_key(30.32 + 7.0, 2),
        t.create_emotion_key(32.39 + 7.0, 2, variation = 1, is_sustained = False)
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.EMOTION, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_emotion_key(0.5, 64),
        t.create_emotion_key(4.2, 2),
        t.create_emotion_key(10.2, 2, variation = 2, is_sustained = False),
        t.create_emotion_key(11.7, 2, variation = 1, is_sustained = False),
        t.create_emotion_key(13.8, 2, variation = 2, is_sustained = False),
        t.create_emotion_key(9.74 + 7.0, 2, variation = 1, is_sustained = False),
        t.create_emotion_key(17.2, 2, variation = 23, is_sustained = False),
        t.create_emotion_key(17.8, 2, variation = 1, is_sustained = False),
        t.create_emotion_key(25.05 + 7.0, 2, is_sustained = False),
        t.create_emotion_key(28.49 + 7.0, 2, variation = 2, is_sustained = False),
        t.create_emotion_key(29.36 + 7.0, 2, variation = 23, is_sustained = False),
        t.create_emotion_key(30.27 + 7.0, 2, variation = 1),
        t.create_emotion_key(32.0 + 7.0, 2, variation = 24),
        t.create_emotion_key(32.36 + 7.0, 2, variation = 2)
    ), is_snapped_to_end = True)

    t.create_tl_actor_node(bg3.timeline_object.LOOK_AT, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        t.create_look_at_key(
            0.0,
            turn_mode = 3,
            turn_speed_multiplier = 0.3,
            head_turn_speed_multiplier = 0.3,
            weight = 0.0,
            safe_zone_angle = 80.0,
            head_safe_zone_angle = 80.0,
            look_at_mode = 0),
        t.create_look_at_key(
            '1.86',
            target = bg3.SPEAKER_SHADOWHEART,
            bone = 'Head_M',
            turn_mode = 3,
            turn_speed_multiplier = 0.3,
            head_turn_speed_multiplier = 0.3,
            weight = 0.0,
            safe_zone_angle = 80.0,
            head_safe_zone_angle = 80.0,
            offset = (0, -0.3, 0),
            is_eye_look_at_enabled = True,
            eye_look_at_target_id = bg3.SPEAKER_SHADOWHEART,
            eye_look_at_bone = 'Head_M'
        ),
        t.create_look_at_key(
            '6.62',
            turn_mode = 3,
            turn_speed_multiplier = 0.3,
            head_turn_speed_multiplier = 0.3,
            weight = 0.0,
            safe_zone_angle = 80.0,
            head_safe_zone_angle = 80.0,
            look_at_mode = 0,
            is_eye_look_at_enabled = True),
        t.create_look_at_key(
            '12.68',
            target = bg3.SPEAKER_SHADOWHEART,
            bone = 'Head_M',
            turn_mode = 3,
            turn_speed_multiplier = 0.3,
            head_turn_speed_multiplier = 0.3,
            weight = 0.0,
            safe_zone_angle = 80.0,
            head_safe_zone_angle = 80.0,
            look_at_mode = 1,
            eye_look_at_target_id = bg3.SPEAKER_SHADOWHEART,
            eye_look_at_bone = 'Head_M')
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.LOOK_AT, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_look_at_key(
            0.0,
            target = bg3.SPEAKER_PLAYER,
            bone = 'Head_M',
            turn_mode = 3,
            turn_speed_multiplier = 0.3,
            head_turn_speed_multiplier = 0.3,
            weight = 0.0,
            safe_zone_angle = 80.0,
            head_safe_zone_angle = 80.0,
            look_at_mode = 1,
            eye_look_at_bone = 'Head_M'),
    ), is_snapped_to_end = True)

    # Shadowheart theme
    t.create_tl_actor_node(bg3.timeline_object.SOUND, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_sound_event_key(0.0, sound_event_id = 'ec19d32b-1213-4166-ba20-405994e62381'),
    ))

    t.create_tl_actor_node(bg3.timeline_object.SOUND, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.SOUND, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        t.create_sound_event_key(9.74 + 7.0, sound_event_id = '6ffc5af2-ae64-48a2-9068-4996d4cdceab', sound_object_index = 4),
        t.create_sound_event_key(23.46 + 7.0, sound_event_id = '6ffc5af2-ae64-48a2-9068-4996d4cdceab', sound_object_index = 4),
        t.create_sound_event_key(25.23 + 7.0, sound_event_id = 'ffbbbd57-5c31-444d-bc3a-c3d14df0be53', sound_object_index = 4),
        t.create_sound_event_key(28.19 + 7.0, sound_event_id = '5dac329f-b08a-412d-84bc-86fc1aecae45', sound_object_index = 4),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.SOUND, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        t.create_sound_event_key(9.67 + 7.0, sound_event_id = '6dbe237a-0c78-4023-a6b7-30349e0505db', sound_object_index = 4),
        t.create_sound_event_key(15.24 + 7.0, sound_event_id = 'c232329e-2d4e-4f0c-a4d4-ea1585fce27c', sound_object_index = 4),
        t.create_sound_event_key(23.48 + 7.0, sound_event_id = '5dac329f-b08a-412d-84bc-86fc1aecae45', sound_object_index = 4),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.SOUND, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        t.create_sound_event_key(18.91 + 7.0, sound_type = 4),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.SOUND, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        t.create_sound_event_key(2.43, sound_event_id = 'd572362f-b64c-4836-9c1d-4399507162fb')
    ), is_snapped_to_end = True)

    t.create_tl_actor_node(bg3.timeline_object.PHYSICS, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        t.create_value_key(time = 0.0, interpolation_type = 3, value_name = 'InverseKinematics', value = False),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.PHYSICS, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_value_key(time = 0.0, interpolation_type = 3, value_name = 'InverseKinematics', value = False),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.HANDS_IK, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_value_key(time = 0.0, interpolation_type = 3, value_name = 'InverseKinematics', value = False)
    ), is_snapped_to_end = True)
    

    camera_uuid = '91f50bea-c8cc-4c34-b618-227519017779'

    t.create_tl_camera_fov(camera_uuid, '0.0', '27.0', (
        t.create_value_key(time = 0.0, value = 30.0, value_name = 'FoV', interpolation_type = 3),
    ), is_snapped_to_end = True)

    t.create_tl_transform(bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = -1.319),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = -0.105),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 3.0),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = bg3.euler_to_quaternion(-90, 0, 0, sequence='yxz')),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 1),
        ),
        (),
    ))


    # camera shot 1
    t.create_tl_transform(camera_uuid, '0.0', '4.2', (
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = -1.9),
            t.create_value_key(time = '4.2', interpolation_type = 5, value = -1.55),
            #t.create_value_key(time = 8.2, interpolation_type = 5, value = -1.5),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 1.0),
            t.create_value_key(time = '4.2', interpolation_type = 5, value = 1.10),
            #t.create_value_key(time = 8.2, interpolation_type = 5, value = 1.15),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 2.1),
            t.create_value_key(time = '4.2', interpolation_type = 5, value = 1.15),
            #t.create_value_key(time = 8.2, interpolation_type = 5, value = 1.2),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = bg3.euler_to_quaternion(62, -18, 0, sequence='yxz')),
            t.create_value_key(time = '4.2', interpolation_type = 5, value = bg3.euler_to_quaternion(27, -6, 0, sequence='yxz')),
            #t.create_value_key(time = 8.2, interpolation_type = 5, value = bg3.euler_to_quaternion(25, -7, 0, sequence='yxz')),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 1),
        ),
        (),
    ))
    t.create_tl_shot(camera_uuid, '0.0', phase_duration, is_snapped_to_end = True)

    t.create_tl_animation(
        bg3.SPEAKER_PLAYER, '0.0', '4.2',
        'ad48ef7a-e01d-4894-e41a-c97670e0f45b',
        '494aa8f4-9a3f-4156-a111-befb5461f276',
        fade_in = 0.0,
        fade_out = 0.0)

    t.create_tl_transform(bg3.SPEAKER_SHADOWHEART, '0.0', '4.2', (
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = -0.02),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = -0.05),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 3.0),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = bg3.euler_to_quaternion(90, 0, 0, sequence='yxz')),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 1),
        ),
        (),
    ))
    t.create_tl_animation(
        bg3.SPEAKER_SHADOWHEART, '0.0', '4.2',
        '73a0acd3-1b93-4bfa-b7f3-be44a431a256',
        '8fc9bad5-96fa-4e4b-9e7f-8126d4187d73',
        fade_in = 0.0,
        fade_out = 0.0,
        enable_root_motion = True,
        target_transform = t.create_animation_target_transform(
            1.0, (-0.04, -0.075, 3.0), bg3.euler_to_quaternion(90, 0, 0, sequence='yxz')
        ))

    # camera shot 2
    t.create_tl_transform(camera_uuid, '4.2', '9.9', (
        (
            t.create_value_key(time = '4.2', interpolation_type = 5, value = 0.5),
        ),
        (
            t.create_value_key(time = '4.2', interpolation_type = 5, value = 1.75),
        ),
        (
            t.create_value_key(time = '4.2', interpolation_type = 5, value = 2.4),
        ),
        (
            t.create_value_key(time = '4.2', interpolation_type = 5, value = bg3.euler_to_quaternion(-58, 12, 0, sequence='yxz')),
        ),
        (
            t.create_value_key(time = '4.2', interpolation_type = 5, value = 1),
        ),
        (),
    ))

    t.create_tl_animation(
        bg3.SPEAKER_PLAYER, '4.2', '9.9',
        'ad48ef7a-e01d-4894-e41a-c97670e0f45b',
        '494aa8f4-9a3f-4156-a111-befb5461f276',
        animation_play_start_offset = 3.2,
        fade_in = 0.0,
        fade_out = 0.0)

    t.create_tl_transform(bg3.SPEAKER_SHADOWHEART, '4.2', '9.9', (
        (
            t.create_value_key(time = '4.2', interpolation_type = 5, value = -0.02),
        ),
        (
            t.create_value_key(time = '4.2', interpolation_type = 5, value = -0.05),
        ),
        (
            t.create_value_key(time = '4.2', interpolation_type = 5, value = 3.0),
        ),
        (
            t.create_value_key(time = '4.2', interpolation_type = 5, value = bg3.euler_to_quaternion(90, 0, 0, sequence='yxz')),
        ),
        (
            t.create_value_key(time = '4.2', interpolation_type = 5, value = 1),
        ),
        (),
    ))
    t.create_tl_animation(
        bg3.SPEAKER_SHADOWHEART, '4.2', '9.9',
        '73a0acd3-1b93-4bfa-b7f3-be44a431a256',
        '8fc9bad5-96fa-4e4b-9e7f-8126d4187d73',
        animation_play_start_offset = 3.2,
        fade_in = 0.0,
        fade_out = 0.0,
        target_transform = t.create_animation_target_transform(
            1.0, (-0.04, -0.075, 3.0), bg3.euler_to_quaternion(90, 0, 0, sequence='yxz')
        ))

    t.create_tl_voice(bg3.SPEAKER_SHADOWHEART, '4.2', '16.2', dialog_node_uuid, hold_mocap = False)

    
    # camera shot 3
    t.create_tl_transform(camera_uuid, '9.9', '18.3', (
        (
            t.create_value_key(time = 9.9, interpolation_type = 5, value = -1.8),
        ),
        (
            t.create_value_key(time = 9.9, interpolation_type = 5, value = 1.04),
        ),
        (
            t.create_value_key(time = 9.9, interpolation_type = 5, value = 1.95),
        ),
        (
            t.create_value_key(time = 9.9, interpolation_type = 5, value = bg3.euler_to_quaternion(56, -14, 0, sequence='yxz')),
        ),
        (
            t.create_value_key(time = 9.9, interpolation_type = 5, value = 1),
        ),
        (),
    ))

    t.create_tl_animation(
        bg3.SPEAKER_PLAYER, '9.9', '18.3',
        'ad48ef7a-e01d-4894-e41a-c97670e0f45b',
        '494aa8f4-9a3f-4156-a111-befb5461f276',
        animation_play_start_offset = 3.8,
        fade_in = 0.0,
        fade_out = 0.0)

    t.create_tl_transform(bg3.SPEAKER_SHADOWHEART, '9.9', '18.3', (
        (
            t.create_value_key(time = 9.9, interpolation_type = 5, value = -0.02),
        ),
        (
            t.create_value_key(time = 9.9, interpolation_type = 5, value = -0.075),
        ),
        (
            t.create_value_key(time = 9.9, interpolation_type = 5, value = 3.0),
        ),
        (
            t.create_value_key(time = 9.9, interpolation_type = 5, value = bg3.euler_to_quaternion(90, 0, 0, sequence='yxz')),
        ),
        (
            t.create_value_key(time = 9.9, interpolation_type = 5, value = 1),
        ),
        (),
    ))
    t.create_tl_animation(
        bg3.SPEAKER_SHADOWHEART, '9.9', '17.7',
        '73a0acd3-1b93-4bfa-b7f3-be44a431a256',
        '8fc9bad5-96fa-4e4b-9e7f-8126d4187d73',
        animation_play_start_offset = 3.8,
        fade_in = 0.0,
        fade_out = 0.0,
        target_transform = t.create_animation_target_transform(
            1.0, (-0.04, -0.075, 3.0), bg3.euler_to_quaternion(90, 0, 0, sequence='yxz')
        ))

    # camera shot 4
    t.create_tl_transform(camera_uuid, '17.7', '23.3', (
        (
            t.create_value_key(time = '17.7', interpolation_type = 5, value = -2.3),
        ),
        (
            t.create_value_key(time = '17.7', interpolation_type = 5, value = 1.6),
        ),
        (
            t.create_value_key(time = '17.7', interpolation_type = 5, value = 2.3),
        ),
        (
            t.create_value_key(time = '17.7', interpolation_type = 5, value = bg3.euler_to_quaternion(72, 8, 0, sequence='yxz')),
        ),
        (
            t.create_value_key(time = '17.7', interpolation_type = 5, value = 1),
        ),
        (),
    ))


    t.create_tl_animation(
        bg3.SPEAKER_PLAYER, '17.7', phase_duration,
        'ad48ef7a-e01d-4894-e41a-c97670e0f45b',
        '494aa8f4-9a3f-4156-a111-befb5461f276',
        animation_play_start_offset = 10.7,
        fade_in = 0.0,
        fade_out = 0.0)

    t.create_tl_transform(bg3.SPEAKER_SHADOWHEART, '17.7', '27.0', (
        (
            t.create_value_key(time = '17.7', interpolation_type = 5, value = -0.02),
        ),
        (
            t.create_value_key(time = '17.7', interpolation_type = 5, value = -0.075),
        ),
        (
            t.create_value_key(time = '17.7', interpolation_type = 5, value = 3.0),
        ),
        (
            t.create_value_key(time = '17.7', interpolation_type = 5, value = bg3.euler_to_quaternion(90, 0, 0, sequence='yxz')),
        ),
        (
            t.create_value_key(time = '17.7', interpolation_type = 5, value = 1),
        ),
        (),
    ))
    t.create_tl_animation(
        bg3.SPEAKER_SHADOWHEART, '17.7', phase_duration,
        '73a0acd3-1b93-4bfa-b7f3-be44a431a256',
        '8fc9bad5-96fa-4e4b-9e7f-8126d4187d73',
        animation_play_start_offset = 10.7,
        fade_in = 0.0,
        fade_out = 0.0,
        target_transform = t.create_animation_target_transform(
            1.0, (-0.04, -0.075, 3.0), bg3.euler_to_quaternion(90, 0, 0, sequence='yxz')
        ))

    # camera shot 5
    t.create_tl_transform(camera_uuid, '23.3', '27.0', (
        (
            t.create_value_key(time = '23.3', interpolation_type = 5, value = -0.6),
        ),
        (
            t.create_value_key(time = '23.3', interpolation_type = 5, value = 2.1),
        ),
        (
            t.create_value_key(time = '23.3', interpolation_type = 5, value = 0.8),
        ),
        (
            t.create_value_key(time = '23.3', interpolation_type = 5, value = bg3.euler_to_quaternion(3, 17, 0, sequence='yxz')),
        ),
        (
            t.create_value_key(time = '23.3', interpolation_type = 5, value = 1),
        ),
        (),
    ))

    # camera shot 6
    t.create_tl_camera_fov(camera_uuid, '27.0', phase_duration, (
        t.create_value_key(time = '27.0', value = 25.0, value_name = 'FoV', interpolation_type = 3),
    ))
    t.create_tl_transform(camera_uuid, '27.0', phase_duration, (
        (
            t.create_value_key(time = '27.0', interpolation_type = 5, value = -0.8),
        ),
        (
            t.create_value_key(time = '27.0', interpolation_type = 5, value = 2.1),
        ),
        (
            t.create_value_key(time = '27.0', interpolation_type = 5, value = 1.0),
        ),
        (
            t.create_value_key(time = '27.0', interpolation_type = 5, value = bg3.euler_to_quaternion(8, 15, 0, sequence='yxz')),
        ),
        (
            t.create_value_key(time = '27.0', interpolation_type = 5, value = 1),
        ),
        (),
    ))
    t.create_tl_transform(bg3.SPEAKER_SHADOWHEART, '27.0', phase_duration, (
        (
            t.create_value_key(time = '27.0', interpolation_type = 5, value = 0.0),
        ),
        (
            t.create_value_key(time = '27.0', interpolation_type = 5, value = -0.05),
        ),
        (
            t.create_value_key(time = '27.0', interpolation_type = 5, value = 3.0),
        ),
        (
            t.create_value_key(time = '27.0', interpolation_type = 5, value = bg3.euler_to_quaternion(90, 0, 0, sequence='yxz')),
        ),
        (
            t.create_value_key(time = '27.0', interpolation_type = 5, value = 1),
        ),
        (),
    ))


    t.create_tl_animation(
        bg3.SPEAKER_PLAYER, '15.67', '18.89',
        'c26b9b0a-20cc-44a4-a499-18d6d78abec5',
        '2b7b7a61-dbaf-4b0a-baf0-be4e414128f3',
        animation_slot = 1,
        animation_play_rate = 0.2,
        animation_play_start_offset = 7.5,
        fade_in = 2.0,
        fade_out = 0.0)

    t.create_tl_animation(
        bg3.SPEAKER_PLAYER, '18.89', '22.4',
        'a0e37a8e-c619-4d0a-840a-061831fb0523',
        '2b7b7a61-dbaf-4b0a-baf0-be4e414128f3',
        animation_slot = 1,
        animation_play_rate = 0.9,
        animation_play_start_offset = 4.02,
        fade_in = 0.0,
        fade_out = 2.0)

    t.create_tl_animation(
        bg3.SPEAKER_PLAYER, '29.06', '34.2',
        'c26b9b0a-20cc-44a4-a499-18d6d78abec5',
        '2b7b7a61-dbaf-4b0a-baf0-be4e414128f3',
        animation_slot = 1,
        animation_play_start_offset = 1.0,
        fade_in = 2.0,
        fade_out = 0.0
    )
    t.create_tl_animation(
        bg3.SPEAKER_SHADOWHEART, '29.06', '34.2',
        'a0e37a8e-c619-4d0a-840a-061831fb0523',
        '7871ce8b-b26e-48c2-969b-347c61560f95',
        animation_slot = 1,
        animation_play_start_offset = 1.8,
        fade_in = 2.0,
        fade_out = 0.0
    )
    t.create_tl_animation(
        bg3.SPEAKER_SHADOWHEART, '34.2', '36.82',
        'a0e37a8e-c619-4d0a-840a-061831fb0523',
        '7871ce8b-b26e-48c2-969b-347c61560f95',
        animation_slot = 1,
        animation_play_start_offset = 6.804,
        fade_in = 0.0,
        fade_out = 2.0
    )
    t.create_tl_animation(
        bg3.SPEAKER_PLAYER, '34.2', '37.05',
        'a0e37a8e-c619-4d0a-840a-061831fb0523',
        '2b7b7a61-dbaf-4b0a-baf0-be4e414128f3',
        animation_slot = 1,
        animation_play_start_offset = 6.804,
        fade_in = 0.0,
        fade_out = 2.0
    )


def create_proposal_cinematic_bt4(dialog_node_uuid: str, t: bg3.timeline_object) -> None:

    phase_duration = '40.38'
    t.create_new_phase(dialog_node_uuid, phase_duration)

    t.create_tl_actor_node(bg3.timeline_object.ATTITUDE, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.ATTITUDE, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (), is_snapped_to_end = True)

    t.create_tl_actor_node(bg3.timeline_object.EMOTION, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        t.create_emotion_key(0.0, 2),
        t.create_emotion_key(5.49, 2, variation = 1),
        t.create_emotion_key(9.97 + 7.0, 256, variation = 24),
        t.create_emotion_key(10.9 + 7.0, 256, variation = 25),
        t.create_emotion_key(14.2 + 7.0, 16, is_sustained = False),
        t.create_emotion_key(17.64 + 7.0, 2, variation = 1, is_sustained = False),
        t.create_emotion_key(30.32 + 7.0, 2),
        t.create_emotion_key(32.39 + 7.0, 2, variation = 1, is_sustained = False)
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.EMOTION, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_emotion_key(0.5, 64),
        t.create_emotion_key(4.2, 2),
        t.create_emotion_key(10.2, 2, variation = 2, is_sustained = False),
        t.create_emotion_key(11.7, 2, variation = 1, is_sustained = False),
        t.create_emotion_key(13.8, 2, variation = 2, is_sustained = False),
        t.create_emotion_key(9.74 + 7.0, 2, variation = 1, is_sustained = False),
        t.create_emotion_key(17.2, 2, variation = 23, is_sustained = False),
        t.create_emotion_key(17.8, 2, variation = 1, is_sustained = False),
        t.create_emotion_key(25.05 + 7.0, 2, is_sustained = False),
        t.create_emotion_key(28.49 + 7.0, 2, variation = 2, is_sustained = False),
        t.create_emotion_key(29.36 + 7.0, 2, variation = 23, is_sustained = False),
        t.create_emotion_key(30.27 + 7.0, 2, variation = 1),
        t.create_emotion_key(32.0 + 7.0, 2, variation = 24),
        t.create_emotion_key(32.36 + 7.0, 2, variation = 2)
    ), is_snapped_to_end = True)

    t.create_tl_actor_node(bg3.timeline_object.LOOK_AT, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        t.create_look_at_key(
            0.0,
            turn_mode = 3,
            turn_speed_multiplier = 0.3,
            head_turn_speed_multiplier = 0.3,
            weight = 0.0,
            safe_zone_angle = 80.0,
            head_safe_zone_angle = 80.0,
            look_at_mode = 0),
        t.create_look_at_key(
            1.86,
            target = bg3.SPEAKER_SHADOWHEART,
            bone = 'Head_M',
            turn_mode = 3,
            turn_speed_multiplier = 0.3,
            head_turn_speed_multiplier = 0.3,
            weight = 0.0,
            safe_zone_angle = 80.0,
            head_safe_zone_angle = 80.0,
            offset = (0, -0.3, 0),
            is_eye_look_at_enabled = True,
            eye_look_at_target_id = bg3.SPEAKER_SHADOWHEART,
            eye_look_at_bone = 'Head_M'
        ),
        t.create_look_at_key(
            6.62,
            turn_mode = 3,
            turn_speed_multiplier = 0.3,
            head_turn_speed_multiplier = 0.3,
            weight = 0.0,
            safe_zone_angle = 80.0,
            head_safe_zone_angle = 80.0,
            look_at_mode = 0,
            is_eye_look_at_enabled = True),
        t.create_look_at_key(
            12.68,
            target = bg3.SPEAKER_SHADOWHEART,
            bone = 'Head_M',
            turn_mode = 3,
            turn_speed_multiplier = 0.3,
            head_turn_speed_multiplier = 0.3,
            weight = 0.0,
            safe_zone_angle = 80.0,
            head_safe_zone_angle = 80.0,
            look_at_mode = 1,
            eye_look_at_target_id = bg3.SPEAKER_SHADOWHEART,
            eye_look_at_bone = 'Head_M')
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.LOOK_AT, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_look_at_key(
            0.0,
            target = bg3.SPEAKER_PLAYER,
            bone = 'Head_M',
            turn_mode = 3,
            turn_speed_multiplier = 0.3,
            head_turn_speed_multiplier = 0.3,
            weight = 0.0,
            safe_zone_angle = 80.0,
            head_safe_zone_angle = 80.0,
            look_at_mode = 1,
            eye_look_at_bone = 'Head_M'),
    ), is_snapped_to_end = True)

    # Shadowheart theme
    t.create_tl_actor_node(bg3.timeline_object.SOUND, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_sound_event_key(0.0, sound_event_id = 'ec19d32b-1213-4166-ba20-405994e62381'),
    ))

    t.create_tl_actor_node(bg3.timeline_object.SOUND, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.SOUND, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        t.create_sound_event_key(9.74 + 7.0, sound_event_id = '6ffc5af2-ae64-48a2-9068-4996d4cdceab', sound_object_index = 4),
        t.create_sound_event_key(23.46 + 7.0, sound_event_id = '6ffc5af2-ae64-48a2-9068-4996d4cdceab', sound_object_index = 4),
        t.create_sound_event_key(25.23 + 7.0, sound_event_id = 'ffbbbd57-5c31-444d-bc3a-c3d14df0be53', sound_object_index = 4),
        t.create_sound_event_key(28.19 + 7.0, sound_event_id = '5dac329f-b08a-412d-84bc-86fc1aecae45', sound_object_index = 4),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.SOUND, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        t.create_sound_event_key(9.67 + 7.0, sound_event_id = '6dbe237a-0c78-4023-a6b7-30349e0505db', sound_object_index = 4),
        t.create_sound_event_key(15.24 + 7.0, sound_event_id = 'c232329e-2d4e-4f0c-a4d4-ea1585fce27c', sound_object_index = 4),
        t.create_sound_event_key(23.48 + 7.0, sound_event_id = '5dac329f-b08a-412d-84bc-86fc1aecae45', sound_object_index = 4),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.SOUND, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        t.create_sound_event_key(18.91 + 7.0, sound_type = 4),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.SOUND, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        t.create_sound_event_key(2.43, sound_event_id = 'd572362f-b64c-4836-9c1d-4399507162fb')
    ), is_snapped_to_end = True)

    t.create_tl_actor_node(bg3.timeline_object.PHYSICS, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        t.create_value_key(time = 0.0, interpolation_type = 3, value_name = 'InverseKinematics', value = False),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.PHYSICS, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_value_key(time = 0.0, interpolation_type = 3, value_name = 'InverseKinematics', value = False),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.HANDS_IK, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        t.create_value_key(time = 0.0, interpolation_type = 3, value_name = 'InverseKinematics', value = False)
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.HANDS_IK, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_value_key(time = 0.0, interpolation_type = 3, value_name = 'InverseKinematics', value = False)
    ), is_snapped_to_end = True)
    

    camera_uuid = '91f50bea-c8cc-4c34-b618-227519017779'

    t.create_tl_camera_fov(camera_uuid, '0.0', '27.0', (
        t.create_value_key(time = 0.0, value = 30.0, value_name = 'FoV', interpolation_type = 3),
    ), is_snapped_to_end = True)

    t.create_tl_transform(bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = -1.319),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = -0.2),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 3.0),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = bg3.euler_to_quaternion(-90, 0, 0, sequence='yxz')),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 1),
        ),
        (),
    ))


    # camera shot 1
    t.create_tl_transform(camera_uuid, '0.0', '4.2', (
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = -1.9),
            t.create_value_key(time = '4.2', interpolation_type = 5, value = -1.55),
            #t.create_value_key(time = 8.2, interpolation_type = 5, value = -1.5),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 1.0),
            t.create_value_key(time = '4.2', interpolation_type = 5, value = 1.10),
            #t.create_value_key(time = 8.2, interpolation_type = 5, value = 1.15),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 2.1),
            t.create_value_key(time = '4.2', interpolation_type = 5, value = 1.15),
            #t.create_value_key(time = 8.2, interpolation_type = 5, value = 1.2),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = bg3.euler_to_quaternion(62, -18, 0, sequence='yxz')),
            t.create_value_key(time = '4.2', interpolation_type = 5, value = bg3.euler_to_quaternion(27, -6, 0, sequence='yxz')),
            #t.create_value_key(time = 8.2, interpolation_type = 5, value = bg3.euler_to_quaternion(25, -7, 0, sequence='yxz')),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 1),
        ),
        (),
    ))
    t.create_tl_shot(camera_uuid, '0.0', phase_duration, is_snapped_to_end = True)

    t.create_tl_animation(
        bg3.SPEAKER_PLAYER, '0.0', '4.2',
        'ad48ef7a-e01d-4894-e41a-c97670e0f45b',
        '494aa8f4-9a3f-4156-a111-befb5461f276',
        fade_in = 0.0,
        fade_out = 0.0)

    t.create_tl_transform(bg3.SPEAKER_SHADOWHEART, '0.0', '4.2', (
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = -0.02),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 0.0),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 3.0),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = bg3.euler_to_quaternion(90, 0, 0, sequence='yxz')),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 1),
        ),
        (),
    ))
    t.create_tl_animation(
        bg3.SPEAKER_SHADOWHEART, '0.0', '4.2',
        '73a0acd3-1b93-4bfa-b7f3-be44a431a256',
        '8fc9bad5-96fa-4e4b-9e7f-8126d4187d73',
        fade_in = 0.0,
        fade_out = 0.0,
        enable_root_motion = True,
        target_transform = t.create_animation_target_transform(
            1.0, (-0.04, -0.075, 3.0), bg3.euler_to_quaternion(90, 0, 0, sequence='yxz')
        ))

    # camera shot 2
    t.create_tl_transform(camera_uuid, '4.2', '9.9', (
        (
            t.create_value_key(time = '4.2', interpolation_type = 5, value = 0.5),
        ),
        (
            t.create_value_key(time = '4.2', interpolation_type = 5, value = 1.75),
        ),
        (
            t.create_value_key(time = '4.2', interpolation_type = 5, value = 2.4),
        ),
        (
            t.create_value_key(time = '4.2', interpolation_type = 5, value = bg3.euler_to_quaternion(-58, 12, 0, sequence='yxz')),
        ),
        (
            t.create_value_key(time = '4.2', interpolation_type = 5, value = 1),
        ),
        (),
    ))

    t.create_tl_animation(
        bg3.SPEAKER_PLAYER, '4.2', '9.9',
        'ad48ef7a-e01d-4894-e41a-c97670e0f45b',
        '494aa8f4-9a3f-4156-a111-befb5461f276',
        animation_play_start_offset = 3.2,
        fade_in = 0.0,
        fade_out = 0.0)

    t.create_tl_transform(bg3.SPEAKER_SHADOWHEART, '4.2', '9.9', (
        (
            t.create_value_key(time = '4.2', interpolation_type = 5, value = -0.02),
        ),
        (
            t.create_value_key(time = '4.2', interpolation_type = 5, value = 0.0),
        ),
        (
            t.create_value_key(time = '4.2', interpolation_type = 5, value = 3.0),
        ),
        (
            t.create_value_key(time = '4.2', interpolation_type = 5, value = bg3.euler_to_quaternion(90, 0, 0, sequence='yxz')),
        ),
        (
            t.create_value_key(time = '4.2', interpolation_type = 5, value = 1),
        ),
        (),
    ))
    t.create_tl_animation(
        bg3.SPEAKER_SHADOWHEART, '4.2', '9.9',
        '73a0acd3-1b93-4bfa-b7f3-be44a431a256',
        '8fc9bad5-96fa-4e4b-9e7f-8126d4187d73',
        animation_play_start_offset = 3.2,
        fade_in = 0.0,
        fade_out = 0.0,
        target_transform = t.create_animation_target_transform(
            1.0, (-0.04, -0.075, 3.0), bg3.euler_to_quaternion(90, 0, 0, sequence='yxz')
        ))

    t.create_tl_voice(bg3.SPEAKER_SHADOWHEART, '4.2', '16.2', dialog_node_uuid, hold_mocap = False)

    
    # camera shot 3
    t.create_tl_transform(camera_uuid, '9.9', '18.3', (
        (
            t.create_value_key(time = 9.9, interpolation_type = 5, value = -1.8),
        ),
        (
            t.create_value_key(time = 9.9, interpolation_type = 5, value = 1.04),
        ),
        (
            t.create_value_key(time = 9.9, interpolation_type = 5, value = 1.95),
        ),
        (
            t.create_value_key(time = 9.9, interpolation_type = 5, value = bg3.euler_to_quaternion(56, -14, 0, sequence='yxz')),
        ),
        (
            t.create_value_key(time = 9.9, interpolation_type = 5, value = 1),
        ),
        (),
    ))

    t.create_tl_animation(
        bg3.SPEAKER_PLAYER, '9.9', '18.3',
        'ad48ef7a-e01d-4894-e41a-c97670e0f45b',
        '494aa8f4-9a3f-4156-a111-befb5461f276',
        animation_play_start_offset = 3.8,
        fade_in = 0.0,
        fade_out = 0.0)

    t.create_tl_transform(bg3.SPEAKER_SHADOWHEART, '9.9', '14.7', (
        (
            t.create_value_key(time = 9.9, interpolation_type = 5, value = -0.02),
        ),
        (
            t.create_value_key(time = 9.9, interpolation_type = 5, value = 0.0),
        ),
        (
            t.create_value_key(time = 9.9, interpolation_type = 5, value = 3.0),
        ),
        (
            t.create_value_key(time = 9.9, interpolation_type = 5, value = bg3.euler_to_quaternion(90, 0, 0, sequence='yxz')),
        ),
        (
            t.create_value_key(time = 9.9, interpolation_type = 5, value = 1),
        ),
        (),
    ))
    t.create_tl_animation(
        bg3.SPEAKER_SHADOWHEART, '9.9', '14.7',
        '73a0acd3-1b93-4bfa-b7f3-be44a431a256',
        '8fc9bad5-96fa-4e4b-9e7f-8126d4187d73',
        animation_play_start_offset = 3.8,
        fade_in = 0.0,
        fade_out = 0.0,
        target_transform = t.create_animation_target_transform(
            1.0, (-0.04, -0.075, 3.0), bg3.euler_to_quaternion(90, 0, 0, sequence='yxz')
        ))

    # camera shot 4
    t.create_tl_transform(camera_uuid, '14.7', '23.3', (
        (
            t.create_value_key(time = 14.7, interpolation_type = 5, value = -2.5),
        ),
        (
            t.create_value_key(time = 14.7, interpolation_type = 5, value = 1.6),
        ),
        (
            t.create_value_key(time = 14.7, interpolation_type = 5, value = 2.7),
        ),
        (
            t.create_value_key(time = 14.7, interpolation_type = 5, value = bg3.euler_to_quaternion(78, 8, 0, sequence='yxz')),
        ),
        (
            t.create_value_key(time = 14.7, interpolation_type = 5, value = 1),
        ),
        (),
    ))


    t.create_tl_animation(
        bg3.SPEAKER_PLAYER, '14.7', phase_duration,
        'ad48ef7a-e01d-4894-e41a-c97670e0f45b',
        '494aa8f4-9a3f-4156-a111-befb5461f276',
        animation_play_start_offset = 7.7,
        fade_in = 0.0,
        fade_out = 0.0)

    t.create_tl_transform(bg3.SPEAKER_SHADOWHEART, '14.7', '27.0', (
        (
            t.create_value_key(time = 14.7, interpolation_type = 5, value = -0.02),
        ),
        (
            t.create_value_key(time = 14.7, interpolation_type = 5, value = 0.0),
        ),
        (
            t.create_value_key(time = 14.7, interpolation_type = 5, value = 3.0),
        ),
        (
            t.create_value_key(time = 14.7, interpolation_type = 5, value = bg3.euler_to_quaternion(90, 0, 0, sequence='yxz')),
        ),
        (
            t.create_value_key(time = 14.7, interpolation_type = 5, value = 1),
        ),
        (),
    ))
    t.create_tl_animation(
        bg3.SPEAKER_SHADOWHEART, '14.7', phase_duration,
        '73a0acd3-1b93-4bfa-b7f3-be44a431a256',
        '8fc9bad5-96fa-4e4b-9e7f-8126d4187d73',
        animation_play_start_offset = 7.7,
        fade_in = 0.0,
        fade_out = 0.0,
        target_transform = t.create_animation_target_transform(
            1.0, (-0.04, -0.075, 3.0), bg3.euler_to_quaternion(90, 0, 0, sequence='yxz')
        ))

    # camera shot 5
    t.create_tl_transform(camera_uuid, '23.3', '27.0', (
        (
            t.create_value_key(time = '23.3', interpolation_type = 5, value = -0.6),
        ),
        (
            t.create_value_key(time = '23.3', interpolation_type = 5, value = 2.1),
        ),
        (
            t.create_value_key(time = '23.3', interpolation_type = 5, value = 0.8),
        ),
        (
            t.create_value_key(time = '23.3', interpolation_type = 5, value = bg3.euler_to_quaternion(3, 17, 0, sequence='yxz')),
        ),
        (
            t.create_value_key(time = '23.3', interpolation_type = 5, value = 1),
        ),
        (),
    ))

    # camera shot 6
    t.create_tl_camera_fov(camera_uuid, '27.0', phase_duration, (
        t.create_value_key(time = '27.0', value = 25.0, value_name = 'FoV', interpolation_type = 3),
    ))
    t.create_tl_transform(camera_uuid, '27.0', phase_duration, (
        (
            t.create_value_key(time = '27.0', interpolation_type = 5, value = -0.8),
        ),
        (
            t.create_value_key(time = '27.0', interpolation_type = 5, value = 2.1),
        ),
        (
            t.create_value_key(time = '27.0', interpolation_type = 5, value = 5.0),
        ),
        (
            t.create_value_key(time = '27.0', interpolation_type = 5, value = bg3.euler_to_quaternion(172, 15, 0, sequence='yxz')),
        ),
        (
            t.create_value_key(time = '27.0', interpolation_type = 5, value = 1),
        ),
        (),
    ))
    t.create_tl_transform(bg3.SPEAKER_SHADOWHEART, '27.0', phase_duration, (
        (
            t.create_value_key(time = '27.0', interpolation_type = 5, value = 0.05),
        ),
        (
            t.create_value_key(time = '27.0', interpolation_type = 5, value = 0.0),
        ),
        (
            t.create_value_key(time = '27.0', interpolation_type = 5, value = 3.0),
        ),
        (
            t.create_value_key(time = '27.0', interpolation_type = 5, value = bg3.euler_to_quaternion(90, 0, 0, sequence='yxz')),
        ),
        (
            t.create_value_key(time = '27.0', interpolation_type = 5, value = 1),
        ),
        (),
    ))


    t.create_tl_animation(
        bg3.SPEAKER_PLAYER, '15.67', '18.89',
        'c26b9b0a-20cc-44a4-a499-18d6d78abec5',
        '2b7b7a61-dbaf-4b0a-baf0-be4e414128f3',
        animation_slot = 1,
        animation_play_rate = 0.2,
        animation_play_start_offset = 7.5,
        fade_in = 2.0,
        fade_out = 0.0)

    t.create_tl_animation(
        bg3.SPEAKER_PLAYER, '18.89', '22.4',
        'a0e37a8e-c619-4d0a-840a-061831fb0523',
        '2b7b7a61-dbaf-4b0a-baf0-be4e414128f3',
        animation_slot = 1,
        animation_play_rate = 0.9,
        animation_play_start_offset = 4.02,
        fade_in = 0.0,
        fade_out = 2.0)

    t.create_tl_animation(
        bg3.SPEAKER_PLAYER, '29.06', '34.2',
        'c26b9b0a-20cc-44a4-a499-18d6d78abec5',
        '2b7b7a61-dbaf-4b0a-baf0-be4e414128f3',
        animation_slot = 1,
        animation_play_start_offset = 1.0,
        fade_in = 2.0,
        fade_out = 0.0
    )
    t.create_tl_animation(
        bg3.SPEAKER_SHADOWHEART, '29.06', '34.2',
        'a0e37a8e-c619-4d0a-840a-061831fb0523',
        '7871ce8b-b26e-48c2-969b-347c61560f95',
        animation_slot = 1,
        animation_play_start_offset = 1.8,
        fade_in = 2.0,
        fade_out = 0.0
    )
    t.create_tl_animation(
        bg3.SPEAKER_SHADOWHEART, '34.2', '36.82',
        'a0e37a8e-c619-4d0a-840a-061831fb0523',
        '7871ce8b-b26e-48c2-969b-347c61560f95',
        animation_slot = 1,
        animation_play_start_offset = 6.804,
        fade_in = 0.0,
        fade_out = 2.0
    )
    t.create_tl_animation(
        bg3.SPEAKER_PLAYER, '34.2', '37.05',
        'a0e37a8e-c619-4d0a-840a-061831fb0523',
        '2b7b7a61-dbaf-4b0a-baf0-be4e414128f3',
        animation_slot = 1,
        animation_play_start_offset = 6.804,
        fade_in = 0.0,
        fade_out = 2.0
    )


def create_scene_marriage_proposal() -> None:
    ################################################################################################
    # Dialog: END_GameFinale_RomanceFates_Shadowheart.lsf
    ################################################################################################

    # d = bg3.dialog_object(files.get_file('Gustav', 'Mods/GustavDev/Story/DialogsBinary/Act3/EndGame/END_GameFinale_RomanceFates_Shadowheart.lsf'))
    # t = bg3.timeline_object(files.get_file('Gustav', 'Public/GustavDev/Timeline/Generated/END_GameFinale_RomanceFates_Shadowheart.lsf'), d)

    ab = game_assets.get_modded_dialog_asset_bundle('END_GameFinale_RomanceFates_Shadowheart')
    d = bg3.dialog_object(ab.dialog)
    t = bg3.timeline_object(ab.timeline, d)

    speaker_idx_tav = d.get_speaker_slot_index(bg3.SPEAKER_PLAYER)
    speaker_idx_shadowheart = d.get_speaker_slot_index(bg3.SPEAKER_SHADOWHEART)

    # 91a8325d-1459-2217-ee8a-c172f8e5adee - mind flayer entry point
    # 4ad0bd1e-5cc1-1d9b-cc27-84c466ddc49d - Shar path, killed parents
    # f87f78dd-6113-7dd3-0a25-30dc1b4e45c7 - Shar path, saved parents
    # 78380d5b-cdb0-b39f-e230-e4c604c0c215 - Selune path, saved parents
    # e566423f-90fd-8b94-5be0-4acdaed3979d - Selune path, killed parents
    # ab53db8d-015d-fce5-c444-f9ce225eea6c - didn't go to the cloister

    entry_points = [
        '91a8325d-1459-2217-ee8a-c172f8e5adee',
        '4ad0bd1e-5cc1-1d9b-cc27-84c466ddc49d',
        'f87f78dd-6113-7dd3-0a25-30dc1b4e45c7',
        '78380d5b-cdb0-b39f-e230-e4c604c0c215',
        'e566423f-90fd-8b94-5be0-4acdaed3979d',
        'ab53db8d-015d-fce5-c444-f9ce225eea6c',
    ]

    root_node_uuid = '54747622-aa4f-44cc-b243-58b7c952f32c'
    
    d.create_standard_dialog_node(
        root_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        entry_points,
        None)
        # setflags = (
        #     bg3.flag_group('Object', (
        #         bg3.flag(Shadowheart_Stop_PDA_Trigger.uuid, True, speaker_idx_shadowheart),
        #     )),
        # ))

    d.add_root_node(root_node_uuid, index = 0)

    its_not_an_exciting_life_selune_path_node_uuid = 'cc85bbdb-0b50-276b-f638-064e23ca9844'
    proposal_selune_path_node_uuid = 'cd1b875b-88b5-4d2f-9a18-ac10859fb794'
    proposal_declined_selune_path_node_uuid = 'ca9e5cb6-c864-431f-8dc6-d89b4078a335'
    time_to_find_myself_selune_path_node_uuid = '64302a82-76cb-44ea-8842-cb8d481a1d48'
    what_did_you_have_in_mind_selune_path_node_uuid = 'h0c288c21gd8b4g4b7aga34bg5ab2a5b2bda8'

    proposal_selune_dead_parents_path_node_uuid = 'db110fb9-7071-4088-b6b5-d7940dc43bb9'
    time_to_find_myself_node_uuid = '80f78526-0763-45a1-8155-0d512222776e'

    its_not_an_exciting_life_late_redemption_path_node_uuid = '61b7b9ca-9867-f3c7-fcff-e950fd556383'
    proposal_late_redemption_path_node_uuid = '9521b783-8d6b-4315-985d-c81448ef86b1'
    proposal_declined_late_redemption_path_node_uuid = 'f69ec2de-2b55-43db-bedb-1e23064aa342'
    time_to_find_myself_late_redemption_path_node_uuid = 'b1cadb23-f9ca-4b85-82f3-885504445148'
    what_did_you_have_in_mind_late_redemption_path_node_uuid = '05238cb0-6326-4f1e-8ab8-eb36ec38d47a'
    
    im_hoping_to_find_some_place_selune_path_node_uuid = '47b0cf5d-ba1e-9cad-a161-acb460817d99' # existing node
    im_hoping_to_find_some_place_late_redemption_path_node_uuid = '4df37205-34b0-8a2f-8d49-a8a3e76ea5a0' # existing node
    perhaps_we_shouldnt_selune_path_node_uuid = '3164e1e9-9db8-2af2-70fb-cde7deaa58aa' # existing node
    perhaps_we_shouldnt_late_redemption_path_node_uuid = 'd63d62ad-d7ee-9cb2-5140-8db2fa20fa19' # existing node
    ive_got_to_move_on_node_uuid = '8ebf7ba3-ae8c-712a-74bc-62c4e563e0a0' # existing node
    i_can_choose_my_own_path_node_uuid = '6046cd40-1cab-99fb-2065-2ff0ace182f2' # existing node

    # "yes" nodes
    yes_bt1_node_uuid = '1ce61a60-7290-410c-af4c-e4dbb1249ab8'
    yes_bt2_node_uuid = 'bccc107b-acf8-4a13-a7a0-b498481264e4'
    yes_bt3_node_uuid = 'cc64d16a-b5ef-4656-9cea-944c1f3b8b88'
    yes_bt4_node_uuid = '512d065e-f4dd-40a4-9f3a-bfc5564f3056'
    yes_short_node_uuid = '227cb0dd-0999-482d-93e6-affea7a4f4d1'
    yes_dragonborn_node_uuid = '566da43a-d1c1-4478-b7ee-0caada8cce4d'
    what_more_could_i_need_node_uuid = '468a5596-9336-4257-8729-fbc514d5c0c5'

    # proposal cinematic nodes
    proposal_cinematic_bt1_node_uuid = '29d784d0-bf85-48cc-8410-1a766b059b9e'
    proposal_cinematic_bt2_node_uuid = 'a108f6fa-43e7-4432-9b41-98a6ee3d5257'
    proposal_cinematic_bt3_node_uuid = '06cc03bc-95f1-44a3-8be9-63333e97d373'
    proposal_cinematic_bt4_node_uuid = 'c7536cf6-590b-41c8-9102-a7831d86db23'
    proposal_cinematic_short_node_uuid = 'b5abd9e0-d040-4cf0-8e3c-3bc593168213'
    proposal_cinematic_dragonborn_node_uuid = '361d3199-caf1-4305-8bb8-198429ce3f11'

    # continuation node
    end_cinematic_node_uuid = 'd3c4e608-8352-6aff-ebad-d4ab8ffe72d3' # alias to efbdf0bf-738d-35da-eff4-346ff2c1b950

    shadowheart_tav_married_true = bg3.flag_group(bg3.flag_group.GLOBAL, (
        bg3.flag(Shadowheart_Tav_State_Married.uuid, True),
        bg3.flag(bg3.FLAG_ORI_Shadowheart_State_RetiredToFarmWithAvatar, True)
    ))

    #
    # Selune path, parents saved
    #

    # I want to spend my life with you. Would you marry me? --> yes
    d.create_standard_dialog_node(
        proposal_selune_path_node_uuid,
        bg3.SPEAKER_PLAYER,
        [
            yes_short_node_uuid,
            yes_dragonborn_node_uuid,
            yes_bt3_node_uuid,
            yes_bt4_node_uuid,
            yes_bt1_node_uuid,
            yes_bt2_node_uuid
        ],
        bg3.text_content('h2155d8e8g3584g48fbg95fdg5651ebed00ee', 1),
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(Shadowheart_Rejects_Proposal.uuid, False, speaker_idx_shadowheart),
            )),
        ),
        setflags = (shadowheart_tav_married_true,),
        constructor = bg3.dialog_object.QUESTION)

    # I want to spend my life with you. Would you marry me? --> no
    d.create_standard_dialog_node(
        proposal_declined_selune_path_node_uuid,
        bg3.SPEAKER_PLAYER,
        [time_to_find_myself_selune_path_node_uuid],
        bg3.text_content('h2155d8e8g3584g48fbg95fdg5651ebed00ee', 1),
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(Shadowheart_Rejects_Proposal.uuid, True, speaker_idx_shadowheart),
            )),
        ),
        show_once = True,
        constructor = bg3.dialog_object.QUESTION)

    # I can't... at least not right now. I'm sorry. After everything that happened with my parents, with Shar, I need time to myself. Time to find myself.
    d.create_standard_dialog_node(
        time_to_find_myself_selune_path_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [what_did_you_have_in_mind_selune_path_node_uuid, perhaps_we_shouldnt_selune_path_node_uuid],
        bg3.text_content('h70a5193egc2c9g4b82g9752g7545e7c73658', 1),
        constructor = bg3.dialog_object.ANSWER)
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '19.0',
        time_to_find_myself_selune_path_node_uuid,
        (('18.9', 'f3318a30-48f3-4e93-b87b-b272d92ee652'), (None, '03a396b5-c8f4-4e25-8f21-819f7999996c')),
        emotions = {
            bg3.SPEAKER_SHADOWHEART: [(0.0, 32, None), (1.7, 2048, 1), (8.44, 16, None), (11.72, 32, None)],
            bg3.SPEAKER_PLAYER: [(0.0, 32, None),]
        }
    )

    # What you said about our time together... What did you have in mind?
    d.create_standard_dialog_node(
        what_did_you_have_in_mind_selune_path_node_uuid,
        bg3.SPEAKER_PLAYER,
        [im_hoping_to_find_some_place_selune_path_node_uuid],
        bg3.text_content('hd559506cg8e88g4afcg8035g762fee0051d7', 1),
        setflags = (
            bg3.flag_group('Global', (
                bg3.flag(bg3.FLAG_ORI_Shadowheart_State_RetiredToFarmWithAvatar, True, None),
            )),
        ),
        constructor = bg3.dialog_object.QUESTION)
    

    d.add_child_dialog_node(its_not_an_exciting_life_selune_path_node_uuid, proposal_declined_selune_path_node_uuid, 0)
    d.add_child_dialog_node(its_not_an_exciting_life_selune_path_node_uuid, proposal_selune_path_node_uuid, 0)

    #
    # Selune path, parents killed
    #

    # I want to spend my life with you. Would you marry me?
    d.create_standard_dialog_node(
        proposal_selune_dead_parents_path_node_uuid,
        bg3.SPEAKER_PLAYER,
        [time_to_find_myself_node_uuid],
        bg3.text_content('h2155d8e8g3584g48fbg95fdg5651ebed00ee', 1),
        constructor = bg3.dialog_object.QUESTION)

    # I can't... at least not right now. I'm sorry. After everything that happened with my parents, with Shar, I need time to myself. Time to find myself.
    d.create_standard_dialog_node(
        time_to_find_myself_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [i_can_choose_my_own_path_node_uuid],
        bg3.text_content('h70a5193egc2c9g4b82g9752g7545e7c73658', 1),
        constructor = bg3.dialog_object.ANSWER)

    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '19.0',
        time_to_find_myself_node_uuid,
        ((None, 'f3318a30-48f3-4e93-b87b-b272d92ee652'),),
        emotions = {
            bg3.SPEAKER_SHADOWHEART: [(0.0, 32, None), (1.7, 2048, 1), (8.44, 16, None), (11.72, 32, None)],
            bg3.SPEAKER_PLAYER: [(0.0, 32, None),]
        }
    )

    d.add_child_dialog_node(ive_got_to_move_on_node_uuid, proposal_selune_dead_parents_path_node_uuid, 0)

    #
    # Late redemption path (DJ Shadowheart saved parents)
    #

    # I want to spend my life with you. Would you marry me? --> yes
    d.create_standard_dialog_node(
        proposal_late_redemption_path_node_uuid,
        bg3.SPEAKER_PLAYER,
        [
            yes_short_node_uuid,
            yes_dragonborn_node_uuid,
            yes_bt3_node_uuid,
            yes_bt4_node_uuid,
            yes_bt1_node_uuid,
            yes_bt2_node_uuid
        ],
        bg3.text_content('h2155d8e8g3584g48fbg95fdg5651ebed00ee', 1),
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(Shadowheart_Rejects_Proposal.uuid, False, speaker_idx_shadowheart),
            )),
        ),
        setflags = (shadowheart_tav_married_true,),
        constructor = bg3.dialog_object.QUESTION)

    # I want to spend my life with you. Would you marry me? --> no
    d.create_standard_dialog_node(
        proposal_declined_late_redemption_path_node_uuid,
        bg3.SPEAKER_PLAYER,
        [time_to_find_myself_late_redemption_path_node_uuid],
        bg3.text_content('h2155d8e8g3584g48fbg95fdg5651ebed00ee', 1),
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(Shadowheart_Rejects_Proposal.uuid, True, speaker_idx_shadowheart),
            )),
        ),
        constructor = bg3.dialog_object.QUESTION)

    # I can't... at least not right now. I'm sorry. After everything that happened with my parents, with Shar, I need time to myself. Time to find myself.
    d.create_standard_dialog_node(
        time_to_find_myself_late_redemption_path_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [what_did_you_have_in_mind_late_redemption_path_node_uuid, perhaps_we_shouldnt_late_redemption_path_node_uuid],
        bg3.text_content('h70a5193egc2c9g4b82g9752g7545e7c73658', 1),
        constructor = bg3.dialog_object.ANSWER)

    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '19.0',
        time_to_find_myself_late_redemption_path_node_uuid,
        ((None, 'f3318a30-48f3-4e93-b87b-b272d92ee652'),),
        emotions = {
            bg3.SPEAKER_SHADOWHEART: [(0.0, 32, None), (1.7, 2048, 1), (8.44, 16, None), (11.72, 32, None)],
            bg3.SPEAKER_PLAYER: [(0.0, 32, None),]
        }
    )

    # What you said about our time together... What did you have in mind?
    d.create_standard_dialog_node(
        what_did_you_have_in_mind_late_redemption_path_node_uuid,
        bg3.SPEAKER_PLAYER,
        [im_hoping_to_find_some_place_late_redemption_path_node_uuid],
        bg3.text_content('hd559506cg8e88g4afcg8035g762fee0051d7', 1),
        setflags = (
            bg3.flag_group('Global', (
                bg3.flag(bg3.FLAG_ORI_Shadowheart_State_RetiredToFarmWithAvatar, True, None),
            )),
        ),
        constructor = bg3.dialog_object.QUESTION)


    d.add_child_dialog_node(its_not_an_exciting_life_late_redemption_path_node_uuid, proposal_late_redemption_path_node_uuid, 0)
    d.add_child_dialog_node(its_not_an_exciting_life_late_redemption_path_node_uuid, proposal_declined_late_redemption_path_node_uuid, 0)


    #
    # Shadowheart marries Tav
    #

    d.create_standard_dialog_node(
        yes_short_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [what_more_could_i_need_node_uuid],
        None,
        checkflags = (
            bg3.flag_group("Tag", (
                bg3.flag(bg3.TAG_SHORT, True, speaker_idx_tav),
            )),
        ))
    d.create_standard_dialog_node(
        yes_dragonborn_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [what_more_could_i_need_node_uuid],
        None,
        checkflags = (
            bg3.flag_group("Tag", (
                bg3.flag(bg3.TAG_DRAGONBORN, True, speaker_idx_tav),
            )),
        ))
    d.create_standard_dialog_node(
        yes_bt3_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [proposal_cinematic_bt3_node_uuid],
        None,
        checkflags = (
            bg3.flag_group("Tag", (
                bg3.flag(bg3.TAG_BODYTYPE_STRONG, True, speaker_idx_tav),
                bg3.flag(bg3.TAG_FEMALE, True, speaker_idx_tav),
            )),
        ))
    d.create_standard_dialog_node(
        yes_bt4_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [proposal_cinematic_bt4_node_uuid],
        None,
        checkflags = (
            bg3.flag_group("Tag", (
                bg3.flag(bg3.TAG_BODYTYPE_STRONG, True, speaker_idx_tav),
            )),
        ))
    d.create_standard_dialog_node(
        yes_bt1_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [proposal_cinematic_bt1_node_uuid],
        None,
        checkflags = (
            bg3.flag_group("Tag", (
                bg3.flag(bg3.TAG_FEMALE, True, speaker_idx_tav),
            )),
        ))
    d.create_standard_dialog_node(
        yes_bt2_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [proposal_cinematic_bt2_node_uuid],
        None)

    # What more could I need? If I had all that, and I had you... Yes. I want to share everything that lies ahead of me with you.
    d.create_standard_dialog_node(
        what_more_could_i_need_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [end_cinematic_node_uuid],
        bg3.text_content('h0a14be70g6828g4ed5g8202g288788d68b6e', 1),
        constructor=bg3.dialog_object.ANSWER)

    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '12.0',
        what_more_could_i_need_node_uuid,
        (('5.7', '3206da4a-d3c6-46aa-ba8f-d6f1a8cdef72'), (None, '4ba153f7-42ff-401a-88c3-2620964e041b')),
        emotions={
            bg3.SPEAKER_SHADOWHEART: [(0.0, 2, None), (9.2, 2, 2)],
            bg3.SPEAKER_PLAYER: [(0.0, 64, None), (3.3, 64, 1), (4.7, 2, None)]
        }
    )
    t.create_tl_actor_node(bg3.timeline_object.SOUND, bg3.SPEAKER_SHADOWHEART, '0.0', '12.0', (
        t.create_sound_event_key(0.0, sound_event_id = 'ec19d32b-1213-4166-ba20-405994e62381'),
    ))

    d.create_standard_dialog_node(proposal_cinematic_short_node_uuid, bg3.SPEAKER_SHADOWHEART, [end_cinematic_node_uuid], None, checkflags = (
        bg3.flag_group("Tag", (
            bg3.flag(bg3.TAG_SHORT, True, speaker_idx_tav),
        )),
    ))
    d.create_standard_dialog_node(proposal_cinematic_dragonborn_node_uuid, bg3.SPEAKER_SHADOWHEART, [end_cinematic_node_uuid], None, checkflags = (
        bg3.flag_group("Tag", (
            bg3.flag(bg3.TAG_DRAGONBORN, True, speaker_idx_tav),
        )),
    ))
    d.create_standard_dialog_node(proposal_cinematic_bt4_node_uuid, bg3.SPEAKER_SHADOWHEART, [end_cinematic_node_uuid], None, checkflags = (
        bg3.flag_group("Tag", (
            bg3.flag(bg3.TAG_BODYTYPE_STRONG, True, speaker_idx_tav),
        )),
    ))

    d.create_standard_dialog_node(
        proposal_cinematic_bt1_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [end_cinematic_node_uuid],
        bg3.text_content('h0a14be70g6828g4ed5g8202g288788d68b6e', 1))
    create_proposal_cinematic_bt1(proposal_cinematic_bt1_node_uuid, t)

    d.create_standard_dialog_node(
        proposal_cinematic_bt2_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [end_cinematic_node_uuid],
        bg3.text_content('h0a14be70g6828g4ed5g8202g288788d68b6e', 1))
    create_proposal_cinematic_bt2(proposal_cinematic_bt2_node_uuid, t)

    d.create_standard_dialog_node(
        proposal_cinematic_bt3_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [end_cinematic_node_uuid],
        bg3.text_content('h0a14be70g6828g4ed5g8202g288788d68b6e', 1))
    create_proposal_cinematic_bt3(proposal_cinematic_bt3_node_uuid, t)

    d.create_standard_dialog_node(
        proposal_cinematic_bt4_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [end_cinematic_node_uuid],
        bg3.text_content('h0a14be70g6828g4ed5g8202g288788d68b6e', 1))
    create_proposal_cinematic_bt4(proposal_cinematic_bt4_node_uuid, t)


bg3.add_build_procedure('create_scene_marriage_proposal', create_scene_marriage_proposal)

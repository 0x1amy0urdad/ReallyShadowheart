from __future__ import annotations

import bg3moddinglib as bg3

from .context import get_context

# c4b9b0a8-af8a-610a-4981-a2db809ef87d kiss A phase index 5
# 830571c2-217a-6d3e-4d77-de044e1f4ad1 kiss B phase index 29
# d10c8085-9d36-6d3d-f9c2-62d2d71d9d8a kiss C phase index 9
# ce9bf7b9-661a-861b-a311-94f943403e35 kiss D phase index 6

# Tav         9d41ff4c-5b2e-4b27-a753-a56142c786b4 (Minthara)
# Shadowheart 2cae72ad-2930-45fa-a798-726ef4ccbe7c (Tav)

def create_minthara_kiss_A_timeline(t: bg3.timeline_object, dialog_uuid: str) -> None:
    phase_duration = '6.08'

    t.create_new_phase(dialog_uuid, phase_duration)

    t.create_tl_actor_node(bg3.timeline_object.ATTITUDE, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.ATTITUDE, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (), is_snapped_to_end = True)

    t.create_tl_actor_node(bg3.timeline_object.EMOTION, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        t.create_emotion_key(0.12, 2),
        t.create_emotion_key(3.32, 2, variation = 1),
    ), is_snapped_to_end = True)

    t.create_tl_actor_node(bg3.timeline_object.EMOTION, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_emotion_key(0.0, 4),
        t.create_emotion_key(1.25, 2),
        t.create_emotion_key(4.4, 2, variation = 1),
    ), is_snapped_to_end = True)

    t.create_tl_actor_node(bg3.timeline_object.LOOK_AT, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_look_at_key('0.0', target = bg3.SPEAKER_PLAYER, bone = 'Head_M', turn_mode = 3, weight = 0.0, safe_zone_angle = 80, head_safe_zone_angle = 80, reset = True, look_at_mode = 1, eye_look_at_bone = 'Head_M'),
        t.create_look_at_key('4.4', target = bg3.SPEAKER_PLAYER, bone = 'Head_M', turn_mode = 3, turn_speed_multiplier = 0.3, head_turn_speed_multiplier = 0.3, weight = 0.0, eye_look_at_bone = 'Head_M'),
    ), is_snapped_to_end = True)

    t.create_tl_actor_node(bg3.timeline_object.LOOK_AT, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        t.create_look_at_key('0.0', target = bg3.SPEAKER_SHADOWHEART, bone = 'Head_M', turn_mode = 3, weight = 0.0, safe_zone_angle = 80, head_safe_zone_angle = 80, reset = True, look_at_mode = 1, eye_look_at_bone = 'Head_M'),
        t.create_look_at_key('4.4', target = bg3.SPEAKER_SHADOWHEART, bone = 'Head_M', turn_mode = 3, turn_speed_multiplier = 0.3, head_turn_speed_multiplier = 0.3, weight = 0.0, eye_look_at_bone = 'Head_M'),
    ), is_snapped_to_end = True)


    t.create_tl_actor_node(bg3.timeline_object.SHOW_WEAPON, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        t.create_value_key(time = '0.0', interpolation_type = 3, value_name = 'ShowWeapon', value = False),
    ), is_snapped_to_end = True)

    t.create_tl_actor_node(bg3.timeline_object.SHOW_WEAPON, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_value_key(time = '0.0', interpolation_type = 3, value_name = 'ShowWeapon', value = False),
    ), is_snapped_to_end = True)

    t.create_tl_show_armor(bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
        (), (), (),
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
        (), (), (), (), (), (),
    ), is_snapped_to_end = True)

    t.create_tl_show_armor(bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
        (), (), (),
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
        (), (), (), (), (), (),
    ), is_snapped_to_end = True)

    t.create_tl_actor_node(bg3.timeline_object.SOUND, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        t.create_sound_event_key('2.05', sound_event_id = '025fa6be-55ec-43fe-af6a-03b746163d72', sound_object_index = 4),
    ), is_snapped_to_end = True)

    t.create_tl_actor_node(bg3.timeline_object.SOUND, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        t.create_sound_event_key('2.21', sound_event_id = 'ffbbbd57-5c31-444d-bc3a-c3d14df0be53', sound_object_index = 4),
        t.create_sound_event_key('3.18', sound_event_id = 'aa8db628-8c78-4632-ab7a-2ac210393e93', sound_object_index = 4),
    ), is_snapped_to_end = True)

    t.create_tl_actor_node(bg3.timeline_object.PHYSICS, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        t.create_value_key(time = '0.0', interpolation_type = 3, value_name = 'InverseKinematics', value = False),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.PHYSICS, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_value_key(time = '0.0', interpolation_type = 3, value_name = 'InverseKinematics', value = False),
    ), is_snapped_to_end = True)


    t.create_tl_non_actor_node(bg3.timeline_object.SWITCH_STAGE, '0.0', phase_duration, (
        t.create_value_key(time = '0.0', interpolation_type = 3, value_name = 'SwitchStageEventID', value_type = 'guid', value = 'a60b7f65-3604-445d-9555-5d1b9d03466a'),
    ), is_snapped_to_end = True)

    t.create_tl_transform(bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        (t.create_value_key(time = '0.0', interpolation_type = 3, value_type = 'float', value = '0'),),
        (t.create_value_key(time = '0.0', interpolation_type = 3, value_type = 'float', value = '0.0'),),
        (t.create_value_key(time = '0.0', interpolation_type = 3, value_type = 'float', value = '0.38'),),
        (t.create_value_key(time = '0.0', interpolation_type = 3, value_type = 'fvec4', value = (0, 0, 0, 1)),),
        (),
        (),
    ), is_snapped_to_end = True)

    t.create_tl_transform(bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        (t.create_value_key(time = '0.0', interpolation_type = 3, value_type = 'float', value = '0'),),
        (t.create_value_key(time = '0.0', interpolation_type = 3, value_type = 'float', value = '0.0'),),
        (t.create_value_key(time = '0.0', interpolation_type = 3, value_type = 'float', value = '-0.83'),),
        (t.create_value_key(time = '0.0', interpolation_type = 3, value_type = 'fvec4', value = (0, 1, 0, 0)),),
        (),
        (),
    ), is_snapped_to_end = True)

    camera = '1df3c3cc-13c4-4876-b76f-ad6dd2759185'

    t.create_tl_animation(bg3.SPEAKER_SHADOWHEART, '0.0', '1.27', '20246174-0205-4fe1-9c84-f820ab81e9af', '44947527-98b9-40b8-9257-fc1e93dd2d6d', fade_in = 0.0, fade_out = 0.0)
    t.create_tl_animation(bg3.SPEAKER_PLAYER, '0.0', '1.27', '94758517-627a-4c60-8c12-0ab6db989735', '892fd6c7-3dcb-4b9a-9cd2-d459ad535041', fade_in = 0.0, fade_out = 0.0)

    # Shot 1
    t.create_tl_camera_fov(camera, '0.0', '1.27', (
        t.create_value_key(time = '0.0', interpolation_type = 0, value_name = 'FoV', value_type = 'float', value = '25'),
    ))
    t.create_tl_transform(camera, '0.0', '1.27', (
        (t.create_value_key(time = '0.0', interpolation_type = 3, value_type = 'float', value = '0.4'),),
        (t.create_value_key(time = '0.0', interpolation_type = 3, value_type = 'float', value = '1.6'),),
        (t.create_value_key(time = '0.0', interpolation_type = 3, value_type = 'float', value = '-1.33'),),
        (t.create_value_key(time = '0.0', interpolation_type = 3, value_type = 'fvec4', value = bg3.euler_to_quaternion(-25, 0, 0, sequence='yxz')),),
        (),
        (),
    ))
    t.create_tl_shot(camera, '0.0', '1.27', disable_conditional_staging = True)


    t.create_tl_animation(bg3.SPEAKER_SHADOWHEART, '1.27', '4.4', '20246174-0205-4fe1-9c84-f820ab81e9af', '44947527-98b9-40b8-9257-fc1e93dd2d6d', fade_in = 0.0, fade_out = 0.0, animation_play_start_offset = 1.17)
    t.create_tl_animation(bg3.SPEAKER_PLAYER, '1.27', '4.4', '94758517-627a-4c60-8c12-0ab6db989735', '892fd6c7-3dcb-4b9a-9cd2-d459ad535041', fade_in = 0.0, fade_out = 0.0, animation_play_start_offset = 1.17)

    # Shot 2
    t.create_tl_camera_fov(camera, '1.27', '3.13', (
        t.create_value_key(time = '1.27', interpolation_type = 0, value_name = 'FoV', value_type = 'float', value = '30'),
    ))
    t.create_tl_transform(camera, '1.27', '3.13', (
        (t.create_value_key(time = '1.27', interpolation_type = 3, value_type = 'float', value = '0.5'),),
        (t.create_value_key(time = '1.27', interpolation_type = 3, value_type = 'float', value = '1.64'),),
        (t.create_value_key(time = '1.27', interpolation_type = 3, value_type = 'float', value = '0.45'),),
        (t.create_value_key(time = '1.27', interpolation_type = 3, value_type = 'fvec4', value = bg3.euler_to_quaternion(-125, 0, 0, sequence='yxz')),),
        (),
        (),
    ))
    t.create_tl_shot(camera, '1.27', '3.13', disable_conditional_staging = True)

    t.create_tl_animation(bg3.SPEAKER_SHADOWHEART, '1.6', '3.98', 'a0e37a8e-c619-4d0a-840a-061831fb0523', '9f1c3f9f-a2da-4859-8787-c2ecccfd901a', fade_in = 1.5, fade_out = 0.8, animation_play_start_offset = 1.8, animation_slot = 1)
    t.create_tl_animation(bg3.SPEAKER_PLAYER, '1.6', '3.98', 'a0e37a8e-c619-4d0a-840a-061831fb0523', '4aa23917-7cb8-48c5-9484-c08820191cca', fade_in = 0.73, fade_out = 0.8, animation_play_start_offset = 1.79, animation_slot = 1)

    # Shot 3
    t.create_tl_camera_fov(camera, '3.13', '4.4', (
        t.create_value_key(time = '3.13', interpolation_type = 0, value_name = 'FoV', value_type = 'float', value = '25'),
    ))
    t.create_tl_transform(camera, '3.13', '4.4', (
        (t.create_value_key(time = '3.13', interpolation_type = 3, value_type = 'float', value = '1.3'),),
        (t.create_value_key(time = '3.13', interpolation_type = 3, value_type = 'float', value = '1.6'),),
        (t.create_value_key(time = '3.13', interpolation_type = 3, value_type = 'float', value = '-0.8'),),
        (t.create_value_key(time = '3.13', interpolation_type = 3, value_type = 'fvec4', value = bg3.euler_to_quaternion(-50, 0, 0, sequence='yxz')),),
        (),
        (),
    ))
    t.create_tl_shot(camera, '3.13', '4.4', disable_conditional_staging = True)

    t.create_tl_animation(bg3.SPEAKER_SHADOWHEART, '4.4', phase_duration, '20246174-0205-4fe1-9c84-f820ab81e9af', '44947527-98b9-40b8-9257-fc1e93dd2d6d', fade_in = 0.0, fade_out = 1.4, animation_play_start_offset = 5.08, animation_play_rate = 0.8)
    t.create_tl_animation(bg3.SPEAKER_PLAYER, '4.4', phase_duration, '94758517-627a-4c60-8c12-0ab6db989735', '892fd6c7-3dcb-4b9a-9cd2-d459ad535041', fade_in = 0.0, fade_out = 1.1, animation_play_start_offset = 5.08, animation_play_rate = 0.8)

    # Shot 4
    t.create_tl_camera_fov('33a18aa0-5996-441f-940b-1179758c5834', '4.4', phase_duration, (), is_snapped_to_end = True)
    t.create_tl_transform('33a18aa0-5996-441f-940b-1179758c5834', '4.4', phase_duration, ((), (), (), (), (), ()), is_snapped_to_end = True)
    t.create_tl_shot('33a18aa0-5996-441f-940b-1179758c5834', '4.4', phase_duration, disable_conditional_staging = True, is_snapped_to_end = True)


def create_minthara_kiss_B_timeline(t: bg3.timeline_object, dialog_uuid: str) -> None:
    phase_duration = '18.14'

    t.create_new_phase(dialog_uuid, phase_duration)

    t.create_tl_actor_node(bg3.timeline_object.ATTITUDE, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.ATTITUDE, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (), is_snapped_to_end = True)

    t.create_tl_actor_node(bg3.timeline_object.EMOTION, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        t.create_emotion_key(0.0, 2),
        t.create_emotion_key(11.98, 2, variation = 1),
    ), is_snapped_to_end = True)

    t.create_tl_actor_node(bg3.timeline_object.EMOTION, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_emotion_key(0.0, 2, variation = 1),
    ), is_snapped_to_end = True)

    t.create_tl_actor_node(bg3.timeline_object.LOOK_AT, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_look_at_key('0.0', target = bg3.SPEAKER_PLAYER, bone = 'Head_M', turn_mode = 3, turn_speed_multiplier = 0.3, head_turn_speed_multiplier = 0.3, weight = 0.0, safe_zone_angle = 80, head_safe_zone_angle = 80, reset = True, look_at_mode = 1, eye_look_at_bone = 'Head_M'),
    ), is_snapped_to_end = True)

    t.create_tl_actor_node(bg3.timeline_object.LOOK_AT, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        t.create_look_at_key('0.0', target = bg3.SPEAKER_SHADOWHEART, bone = 'Head_M', turn_mode = 3, turn_speed_multiplier = 0.3, head_turn_speed_multiplier = 0.3, weight = 0.0, safe_zone_angle = 80, head_safe_zone_angle = 80, reset = True, look_at_mode = 1, eye_look_at_bone = 'Head_M'),
    ), is_snapped_to_end = True)


    t.create_tl_actor_node(bg3.timeline_object.SHOW_WEAPON, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        t.create_value_key(time = '0.0', interpolation_type = 3, value_name = 'ShowWeapon', value = False),
    ), is_snapped_to_end = True)

    t.create_tl_actor_node(bg3.timeline_object.SHOW_WEAPON, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_value_key(time = '0.0', interpolation_type = 3, value_name = 'ShowWeapon', value = False),
    ), is_snapped_to_end = True)

    t.create_tl_show_armor(bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
        (), (), (),
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
        (), (), (), (), (), (),
    ), is_snapped_to_end = True)

    t.create_tl_show_armor(bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
        (), (), (),
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
        (), (), (), (), (), (),
    ), is_snapped_to_end = True)

    t.create_tl_actor_node(bg3.timeline_object.SOUND, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        t.create_sound_event_key('3.15', sound_event_id = 'd0756d07-fd81-4fab-b4af-03d565c7f059', sound_object_index = 4),
        t.create_sound_event_key('4.0', sound_event_id = 'ffbbbd57-5c31-444d-bc3a-c3d14df0be53', sound_object_index = 4),
    ), is_snapped_to_end = True)

    t.create_tl_actor_node(bg3.timeline_object.SOUND, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        t.create_sound_event_key('3.22', sound_event_id = '90a31a12-9f32-47e1-899e-cdced0705f27', sound_object_index = 4),
        t.create_sound_event_key('5.31', sound_event_id = 'c6295e80-586c-4fd9-8777-d754514b6bb6', sound_object_index = 4),
        t.create_sound_event_key('6.67', sound_event_id = 'ffbbbd57-5c31-444d-bc3a-c3d14df0be53', sound_object_index = 4),
        t.create_sound_event_key('8.15', sound_event_id = 'c232329e-2d4e-4f0c-a4d4-ea1585fce27c', sound_object_index = 4),
        t.create_sound_event_key('10.91', sound_event_id = '99648c10-b438-4c56-8dcc-5999b5a69e48', sound_object_index = 4),
        t.create_sound_event_key('12.53', sound_event_id = '94b5ef10-e510-4253-83ef-c76d9e4f3487', sound_object_index = 4),
    ), is_snapped_to_end = True)

    t.create_tl_actor_node(bg3.timeline_object.SOUND, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        t.create_sound_event_key('2.51', sound_event_id = '3a82ed81-3970-461a-91dc-4687caa05cce', sound_object_index = 2),
    ), is_snapped_to_end = True)

    t.create_tl_actor_node(bg3.timeline_object.SOUND, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_sound_event_key('2.43', sound_event_id = '4117782b-5bc4-43eb-8e1b-4f1d4b7a84f2', sound_object_index = 4),
        t.create_sound_event_key('5.31', sound_event_id = '99648c10-b438-4c56-8dcc-5999b5a69e48', sound_object_index = 4),
    ), is_snapped_to_end = True)

    t.create_tl_actor_node(bg3.timeline_object.PHYSICS, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        t.create_value_key(time = '0.0', interpolation_type = 3, value_name = 'InverseKinematics', value = False),
        t.create_value_key(time = '14.32', interpolation_type = 3),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.HANDS_IK, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        t.create_value_key(time = '0.0', interpolation_type = 3, value_name = 'InverseKinematics', value = False),
        t.create_value_key(time = '3.7', interpolation_type = 3),
        t.create_value_key(time = '13.6', interpolation_type = 3, value_name = 'InverseKinematics', value = False),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.PHYSICS, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_value_key(time = '0.0', interpolation_type = 3, value_name = 'InverseKinematics', value = False),
        t.create_value_key(time = '14.32', interpolation_type = 3),
    ), is_snapped_to_end = True)

    t.create_tl_non_actor_node(bg3.timeline_object.SWITCH_STAGE, '0.0', phase_duration, (
        t.create_value_key(time = '0.0', interpolation_type = 3, value_name = 'SwitchStageEventID', value_type = 'guid', value = 'a60b7f65-3604-445d-9555-5d1b9d03466a'),
    ), is_snapped_to_end = True)

    t.create_tl_transform(bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        (t.create_value_key(time = '0.0', interpolation_type = 3, value_type = 'float', value = '0'),),
        (t.create_value_key(time = '0.0', interpolation_type = 3, value_type = 'float', value = '0.0'),),
        (t.create_value_key(time = '0.0', interpolation_type = 3, value_type = 'float', value = '0.38'),),
        (t.create_value_key(time = '0.0', interpolation_type = 3, value_type = 'fvec4', value = (0, 0, 0, 1)),),
        (),
        (),
    ), is_snapped_to_end = True)

    t.create_tl_transform(bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        (t.create_value_key(time = '0.0', interpolation_type = 3, value_type = 'float', value = '0'),),
        (t.create_value_key(time = '0.0', interpolation_type = 3, value_type = 'float', value = '0.0'),),
        (t.create_value_key(time = '0.0', interpolation_type = 3, value_type = 'float', value = '-0.83'),),
        (t.create_value_key(time = '0.0', interpolation_type = 3, value_type = 'fvec4', value = (0, 1, 0, 0)),),
        (),
        (),
    ), is_snapped_to_end = True)

    # Animations
    t.create_tl_animation(bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, '6783365f-daa5-40a1-ae73-d77f6e85754a', '44947527-98b9-40b8-9257-fc1e93dd2d6d', fade_in = 0.0, fade_out = 1.4, is_mirrored = True, is_snapped_to_end = True)
    t.create_tl_animation(bg3.SPEAKER_PLAYER, '0.0', phase_duration, 'c093ab60-b18c-cf00-95d8-49e92a7ebfcf', '892fd6c7-3dcb-4b9a-9cd2-d459ad535041', fade_in = 0.0, fade_out = 1.7, is_mirrored = True, is_snapped_to_end = True)

    camera = '1df3c3cc-13c4-4876-b76f-ad6dd2759185'

    # Shot 1
    t.create_tl_camera_fov(camera, '0.0', '3.59', (
        t.create_value_key(time = '0.0', interpolation_type = 0, value_name = 'FoV', value_type = 'float', value = '34'),
    ))
    t.create_tl_transform(camera, '0.0', '3.59', (
        (t.create_value_key(time = '0.0', interpolation_type = 3, value_type = 'float', value = '0.4'),),
        (t.create_value_key(time = '0.0', interpolation_type = 3, value_type = 'float', value = '1.6'),),
        (t.create_value_key(time = '0.0', interpolation_type = 3, value_type = 'float', value = '-1.5'),),
        (t.create_value_key(time = '0.0', interpolation_type = 3, value_type = 'fvec4', value = bg3.euler_to_quaternion(-25, 0, 0, sequence='yxz')),),
        (),
        (),
    ))
    t.create_tl_shot(camera, '0.0', '3.59', disable_conditional_staging = True)

    # Lips
    t.create_tl_animation(bg3.SPEAKER_PLAYER, '2.43', '11.05', 'c26b9b0a-20cc-44a4-a499-18d6d78abec5', '4aa23917-7cb8-48c5-9484-c08820191cca', animation_slot = 1, fade_in = 1.5, fade_out = 1.5, animation_play_start_offset = 0.29)
    t.create_tl_animation(bg3.SPEAKER_SHADOWHEART, '3.15', '6.14', 'c26b9b0a-20cc-44a4-a499-18d6d78abec5', '9f1c3f9f-a2da-4859-8787-c2ecccfd901a', animation_slot = 1, fade_in = 1.5, fade_out = 0.0, animation_play_start_offset = 1.0)
    
    # Shot 2
    t.create_tl_camera_fov(camera, '3.59', '6.14', (
        t.create_value_key(time = '3.59', interpolation_type = 0, value_name = 'FoV', value_type = 'float', value = '22'),
    ))
    t.create_tl_transform(camera, '3.59', '6.14', (
        (t.create_value_key(time = '3.59', interpolation_type = 3, value_type = 'float', value = '1.2'),),
        (t.create_value_key(time = '3.59', interpolation_type = 3, value_type = 'float', value = '1.74'),),
        (t.create_value_key(time = '3.59', interpolation_type = 3, value_type = 'float', value = '-1.2'),),
        (t.create_value_key(time = '3.59', interpolation_type = 3, value_type = 'fvec4', value = bg3.euler_to_quaternion(-65, 0, 0, sequence='yxz')),),
        (),
        (),
    ))
    t.create_tl_shot(camera, '3.59', '6.14', disable_conditional_staging = True)

    # Lips
    t.create_tl_animation(bg3.SPEAKER_SHADOWHEART, '6.14', '10.04', 'c26b9b0a-20cc-44a4-a499-18d6d78abec5', '9f1c3f9f-a2da-4859-8787-c2ecccfd901a', animation_slot = 1, fade_in = 0.0, fade_out = 1.5, animation_play_start_offset = 2.3)

    # Shot 3
    t.create_tl_camera_fov(camera, '6.14', '10.44', (
        t.create_value_key(time = '6.14', interpolation_type = 0, value_name = 'FoV', value_type = 'float', value = '32'),
    ))
    t.create_tl_transform(camera, '6.14', '10.44', (
        (t.create_value_key(time = '6.14', interpolation_type = 3, value_type = 'float', value = '0.4'),),
        (t.create_value_key(time = '6.14', interpolation_type = 3, value_type = 'float', value = '1.72'),),
        (t.create_value_key(time = '6.14', interpolation_type = 3, value_type = 'float', value = '-0.2'),),
        (t.create_value_key(time = '6.14', interpolation_type = 3, value_type = 'fvec4', value = bg3.euler_to_quaternion(-130, 0, 0, sequence='yxz')),),
        (),
        (),
    ))
    t.create_tl_shot(camera, '6.14', '10.44', disable_conditional_staging = True)

    # Shot 4
    t.create_tl_camera_fov(camera, '10.44', '14.32', (
        t.create_value_key(time = '10.44', interpolation_type = 0, value_name = 'FoV', value_type = 'float', value = '22'),
    ))
    t.create_tl_transform(camera, '10.44', '14.32', (
        (t.create_value_key(time = '10.44', interpolation_type = 3, value_type = 'float', value = '0.4'),),
        (t.create_value_key(time = '10.44', interpolation_type = 3, value_type = 'float', value = '1.75'),),
        (t.create_value_key(time = '10.44', interpolation_type = 3, value_type = 'float', value = '-0.9'),),
        (t.create_value_key(time = '10.44', interpolation_type = 3, value_type = 'fvec4', value = bg3.euler_to_quaternion(-50, 4, 0, sequence='yxz')),),
        (),
        (),
    ))
    t.create_tl_shot(camera, '10.44', '14.32', disable_conditional_staging = True)

    # Shot 5
    t.create_tl_camera_fov('99480a46-e5ff-4101-ab73-d0ce43403c57', '14.32', phase_duration, ())
    t.create_tl_transform('99480a46-e5ff-4101-ab73-d0ce43403c57', '14.32', phase_duration, ((), (), (), (), (), ()))
    t.create_tl_shot('99480a46-e5ff-4101-ab73-d0ce43403c57', '14.32', phase_duration, is_snapped_to_end = True)


def create_minthara_kiss_C_timeline(t: bg3.timeline_object, dialog_uuid: str) -> None:
    phase_duration = '20.93'

    t.create_new_phase(dialog_uuid, phase_duration)

    t.create_tl_actor_node(bg3.timeline_object.ATTITUDE, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.ATTITUDE, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (), is_snapped_to_end = True)

    t.create_tl_actor_node(bg3.timeline_object.EMOTION, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        t.create_emotion_key(0.0, 2),
        t.create_emotion_key(1.5, 2, variation = 23, is_sustained = False),
        t.create_emotion_key(2.3, 2, variation = 2),
        t.create_emotion_key(3.3, 256),
        t.create_emotion_key(6.78, 2),
        t.create_emotion_key(16.7, 2, is_sustained = False),
        t.create_emotion_key(17.36, 2, variation = 1, is_sustained = False),
        t.create_emotion_key(17.7, 2, variation = 23, is_sustained = False),
        t.create_emotion_key(19.14, 2, variation = 1, is_sustained = False),
    ), is_snapped_to_end = True)

    t.create_tl_actor_node(bg3.timeline_object.EMOTION, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_emotion_key(2.57, 64),
        t.create_emotion_key(5.53, 2),
        t.create_emotion_key(19.63, 2, variation = 2),
    ), is_snapped_to_end = True)

    t.create_tl_actor_node(bg3.timeline_object.LOOK_AT, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_look_at_key('0.0', target = bg3.SPEAKER_PLAYER, bone = 'Head_M', turn_mode = 3, turn_speed_multiplier = 0.3, head_turn_speed_multiplier = 0.3, weight = 0.0, safe_zone_angle = 80, head_safe_zone_angle = 80, look_at_mode = 1, eye_look_at_bone = 'Head_M'),
        t.create_look_at_key('4.02', turn_mode = 3, turn_speed_multiplier = 0.3, head_turn_speed_multiplier = 0.3, weight = 0.0, safe_zone_angle = 80, head_safe_zone_angle = 80, look_at_mode = 0),
        t.create_look_at_key('0.0', target = bg3.SPEAKER_PLAYER, bone = 'Head_M', turn_mode = 3, turn_speed_multiplier = 0.3, head_turn_speed_multiplier = 0.3, weight = 0.0, safe_zone_angle = 80, head_safe_zone_angle = 80, look_at_mode = 1, eye_look_at_bone = 'Head_M'),
    ), is_snapped_to_end = True)

    t.create_tl_actor_node(bg3.timeline_object.LOOK_AT, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        t.create_look_at_key('0.0', target = bg3.SPEAKER_SHADOWHEART, bone = 'Head_M', turn_mode = 3, turn_speed_multiplier = 0.3, head_turn_speed_multiplier = 0.3, weight = 0.0, safe_zone_angle = 80, head_safe_zone_angle = 80, look_at_mode = 1, eye_look_at_bone = 'Head_M'),
        t.create_look_at_key('2.35', turn_mode = 3, turn_speed_multiplier = 0.3, head_turn_speed_multiplier = 0.3, weight = 0.0, safe_zone_angle = 80, head_safe_zone_angle = 80, look_at_mode = 0),
        t.create_look_at_key('7.44', target = bg3.SPEAKER_SHADOWHEART, bone = 'Head_M', turn_mode = 3, turn_speed_multiplier = 0.3, head_turn_speed_multiplier = 0.3, weight = 0.0, safe_zone_angle = 80, head_safe_zone_angle = 80, look_at_mode = 1, eye_look_at_bone = 'Head_M'),
    ), is_snapped_to_end = True)


    t.create_tl_actor_node(bg3.timeline_object.SHOW_WEAPON, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        t.create_value_key(time = '0.0', interpolation_type = 3, value_name = 'ShowWeapon', value = False),
    ), is_snapped_to_end = True)

    t.create_tl_actor_node(bg3.timeline_object.SHOW_WEAPON, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_value_key(time = '0.0', interpolation_type = 3, value_name = 'ShowWeapon', value = False),
    ), is_snapped_to_end = True)

    t.create_tl_show_armor(bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
        (), (), (),
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
        (), (), (), (), (), (),
    ), is_snapped_to_end = True)

    t.create_tl_show_armor(bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
        (), (), (),
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
        (), (), (), (), (), (),
    ), is_snapped_to_end = True)

    t.create_tl_actor_node(bg3.timeline_object.SOUND, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_sound_event_key('9.98', sound_event_id = '50ab7087-b822-455f-9a61-6b10b6e6d968', sound_object_index = 4),
    ), is_snapped_to_end = True)

    t.create_tl_actor_node(bg3.timeline_object.SOUND, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        t.create_sound_event_key('2.09', sound_type = 4),
    ), is_snapped_to_end = True)

    t.create_tl_actor_node(bg3.timeline_object.SOUND, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        t.create_sound_event_key('8.72', sound_event_id = 'd0756d07-fd81-4fab-b4af-03d565c7f059', sound_object_index = 4),
        t.create_sound_event_key('10.75', sound_event_id = 'ffbbbd57-5c31-444d-bc3a-c3d14df0be53', sound_object_index = 4),
    ), is_snapped_to_end = True)

    t.create_tl_actor_node(bg3.timeline_object.SOUND, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        t.create_sound_event_key('8.69', sound_event_id = '6dbe237a-0c78-4023-a6b7-30349e0505db', sound_object_index = 2),
        t.create_sound_event_key('13.42', sound_event_id = '6ffc5af2-ae64-48a2-9068-4996d4cdceab', sound_object_index = 2),
    ), is_snapped_to_end = True)

    t.create_tl_actor_node(bg3.timeline_object.PHYSICS, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        t.create_value_key(time = '0.0', interpolation_type = 3, value_name = 'InverseKinematics', value = False),
        t.create_value_key(time = '19.44', interpolation_type = 3),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.PHYSICS, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_value_key(time = '0.0', interpolation_type = 3, value_name = 'InverseKinematics', value = False),
        t.create_value_key(time = '19.44', interpolation_type = 3),
    ), is_snapped_to_end = True)

    t.create_tl_non_actor_node(bg3.timeline_object.SWITCH_STAGE, '0.0', phase_duration, (
        t.create_value_key(time = '0.0', interpolation_type = 3, value_name = 'SwitchStageEventID', value_type = 'guid', value = 'a60b7f65-3604-445d-9555-5d1b9d03466a'),
    ), is_snapped_to_end = True)

    t.create_tl_transform(bg3.SPEAKER_PLAYER, '0.0', '19.44', (
        (t.create_value_key(time = '0.0', interpolation_type = 3, value_type = 'float', value = '0'),),
        (t.create_value_key(time = '0.0', interpolation_type = 3, value_type = 'float', value = '0.0'),),
        (t.create_value_key(time = '0.0', interpolation_type = 3, value_type = 'float', value = '0.47'),),
        (t.create_value_key(time = '0.0', interpolation_type = 3, value_type = 'fvec4', value = (0, 0, 0, 1)),),
        (),
        (),
    ))

    t.create_tl_transform(bg3.SPEAKER_SHADOWHEART, '0.0', '19.44', (
        (t.create_value_key(time = '0.0', interpolation_type = 3, value_type = 'float', value = '0'),),
        (t.create_value_key(time = '0.0', interpolation_type = 3, value_type = 'float', value = '0.0'),),
        (t.create_value_key(time = '0.0', interpolation_type = 3, value_type = 'float', value = '-0.41'),),
        (t.create_value_key(time = '0.0', interpolation_type = 3, value_type = 'fvec4', value = (0, 1, 0, 0)),),
        (),
        (),
    ))

    # Animations
    t.create_tl_animation(bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, 'f36f8fb5-c497-4bd4-9fd0-7d9cf96b09a6', '44947527-98b9-40b8-9257-fc1e93dd2d6d', fade_in = 0.0, fade_out = 1.4, animation_play_start_offset = 1.72, is_snapped_to_end = True)
    t.create_tl_animation(bg3.SPEAKER_PLAYER, '0.0', phase_duration, '971c9f1c-e5bf-b14e-bb46-f46a01424d4e', '892fd6c7-3dcb-4b9a-9cd2-d459ad535041', fade_in = 0.0, fade_out = 1.7, animation_play_start_offset = 1.72, is_snapped_to_end = True)

    camera = '1df3c3cc-13c4-4876-b76f-ad6dd2759185'

    # Shot 1
    t.create_tl_camera_fov(camera, '0.0', '4.39', (
        t.create_value_key(time = '0.0', interpolation_type = 0, value_name = 'FoV', value_type = 'float', value = '25'),
    ))
    t.create_tl_transform(camera, '0.0', '4.39', (
        (t.create_value_key(time = '0.0', interpolation_type = 3, value_type = 'float', value = '0.6'),),
        (t.create_value_key(time = '0.0', interpolation_type = 3, value_type = 'float', value = '1.75'),),
        (t.create_value_key(time = '0.0', interpolation_type = 3, value_type = 'float', value = '-1.0'),),
        (
            t.create_value_key(time = '0.0', interpolation_type = 3, value_type = 'fvec4', value = bg3.euler_to_quaternion(-40, 7, 0, sequence='yxz')),
        ),
        (),
        (),
    ))
    t.create_tl_shot(camera, '0.0', '4.39', disable_conditional_staging = True)

    # Lips 1
    t.create_tl_animation(bg3.SPEAKER_SHADOWHEART, '3.42', '7.16', 'c26b9b0a-20cc-44a4-a499-18d6d78abec5', '9f1c3f9f-a2da-4859-8787-c2ecccfd901a', animation_slot = 1, animation_play_rate = 0.1, animation_play_start_offset = 9.44, fade_in = 1.0, fade_out = 1.5)

    # Shot 2
    t.create_tl_camera_fov(camera, '4.39', '7.44', (
        t.create_value_key(time = '4.39', interpolation_type = 0, value_name = 'FoV', value_type = 'float', value = '20'),
    ))
    t.create_tl_transform(camera, '4.39', '7.44', (
        (t.create_value_key(time = '4.39', interpolation_type = 3, value_type = 'float', value = '0.45'),),
        (t.create_value_key(time = '4.39', interpolation_type = 3, value_type = 'float', value = '1.75'),),
        (t.create_value_key(time = '4.39', interpolation_type = 3, value_type = 'float', value = '1.0'),),
        (
            t.create_value_key(time = '4.39', interpolation_type = 3, value_type = 'fvec4', value = bg3.euler_to_quaternion(-160, 7, 0, sequence='yxz')),
        ),
        (),
        (),
    ))
    t.create_tl_shot(camera, '4.39', '7.44', disable_conditional_staging = True)

    # Shot 3
    t.create_tl_camera_fov(camera, '7.44', '10.73', (
        t.create_value_key(time = '0.0', interpolation_type = 0, value_name = 'FoV', value_type = 'float', value = '25'),
    ))
    t.create_tl_transform(camera, '7.44', '10.73', (
        (t.create_value_key(time = '7.44', interpolation_type = 3, value_type = 'float', value = '1.4'),),
        (t.create_value_key(time = '7.44', interpolation_type = 3, value_type = 'float', value = '1.8'),),
        (t.create_value_key(time = '8.44', interpolation_type = 5, value_type = 'float', value = '-0.2'),),
        (t.create_value_key(time = '7.44', interpolation_type = 3, value_type = 'fvec4', value = bg3.euler_to_quaternion(-90, 7, 0, sequence='yxz')),),
        (),
        (),
    ))
    t.create_tl_shot(camera, '7.44', '10.73', disable_conditional_staging = True)

    # Lips 2
    t.create_tl_animation(bg3.SPEAKER_PLAYER, '7.92', '10.73', 'c26b9b0a-20cc-44a4-a499-18d6d78abec5', '4aa23917-7cb8-48c5-9484-c08820191cca', animation_slot = 1, animation_play_start_offset = 8.66, fade_in = 1.2, fade_out = 0.0)
    t.create_tl_animation(bg3.SPEAKER_SHADOWHEART, '8.23', '10.73', 'c26b9b0a-20cc-44a4-a499-18d6d78abec5', '9f1c3f9f-a2da-4859-8787-c2ecccfd901a', animation_slot = 1, animation_play_start_offset = 8.66, fade_in = 1.5, fade_out = 0.0)
    t.create_tl_animation(bg3.SPEAKER_PLAYER, '10.73', '15.48', 'c26b9b0a-20cc-44a4-a499-18d6d78abec5', '4aa23917-7cb8-48c5-9484-c08820191cca', animation_slot = 1, animation_play_start_offset = 5.8, fade_in = 0.0, fade_out = 1.5)
    t.create_tl_animation(bg3.SPEAKER_SHADOWHEART, '10.73', '15.48', 'c26b9b0a-20cc-44a4-a499-18d6d78abec5', '9f1c3f9f-a2da-4859-8787-c2ecccfd901a', animation_slot = 1, animation_play_start_offset = 5.5, fade_in = 0.0, fade_out = 2.0)

    # Shot 4
    t.create_tl_camera_fov(camera, '10.73', '15.35', (
        t.create_value_key(time = '10.73', interpolation_type = 0, value_name = 'FoV', value_type = 'float', value = '25'),
    ))
    t.create_tl_transform(camera, '10.73', '15.35', (
        (t.create_value_key(time = '10.73', interpolation_type = 3, value_type = 'float', value = '0.1'),),
        (t.create_value_key(time = '10.73', interpolation_type = 3, value_type = 'float', value = '1.7'),),
        (t.create_value_key(time = '10.73', interpolation_type = 3, value_type = 'float', value = '0.65'),),
        (
            t.create_value_key(time = '10.73', interpolation_type = 3, value_type = 'fvec4', value = bg3.euler_to_quaternion(-165, 3, 0, sequence='yxz')),
        ),
        (),
        (),
    ))
    t.create_tl_shot(camera, '10.73', '15.35', disable_conditional_staging = True)

    # Shot 5
    t.create_tl_camera_fov(camera, '15.35', '19.44', (
        t.create_value_key(time = '0.0', interpolation_type = 0, value_name = 'FoV', value_type = 'float', value = '40'),
    ))
    t.create_tl_transform(camera, '15.35', '19.44', (
        (t.create_value_key(time = '15.35', interpolation_type = 3, value_type = 'float', value = '0.3'),),
        (t.create_value_key(time = '15.35', interpolation_type = 3, value_type = 'float', value = '1.7'),),
        (t.create_value_key(time = '15.35', interpolation_type = 3, value_type = 'float', value = '-0.65'),),
        (
            t.create_value_key(time = '15.35', interpolation_type = 3, value_type = 'fvec4', value = bg3.euler_to_quaternion(-40, 3, 0, sequence='yxz')),
        ),
        (),
        (),
    ))
    t.create_tl_shot(camera, '15.35', '19.44', disable_conditional_staging = True)

    # Shot 6
    t.create_tl_camera_fov('33a18aa0-5996-441f-940b-1179758c5834', '19.44', phase_duration, (), is_snapped_to_end = True)
    t.create_tl_transform('33a18aa0-5996-441f-940b-1179758c5834', '19.44', phase_duration, ((), (), (), (), (), ()), is_snapped_to_end = True)
    t.create_tl_shot('33a18aa0-5996-441f-940b-1179758c5834', '19.44', phase_duration, is_snapped_to_end = True)


def create_minthara_kiss_D_timeline(t: bg3.timeline_object, dialog_uuid: str) -> None:
    phase_duration = '11.95'

    t.create_new_phase(dialog_uuid, phase_duration)

    t.create_tl_actor_node(bg3.timeline_object.ATTITUDE, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        t.create_attitude_key('0.16', bg3.ATTITUDE_DIAG_Pose_Squared_Wide_01, bg3.ATTITUDE_DIAG_T_Pose),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.ATTITUDE, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (), is_snapped_to_end = True)

    t.create_tl_actor_node(bg3.timeline_object.EMOTION, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        t.create_emotion_key(0.32, 64, variation = 1, is_sustained = False),
        t.create_emotion_key(6.55, 2, is_sustained = False),
        t.create_emotion_key(7.21, 2, variation = 1, is_sustained = False),
        t.create_emotion_key(7.55, 2, variation = 23, is_sustained = False),
        t.create_emotion_key(8.27, 2, variation = 1, is_sustained = False),
    ), is_snapped_to_end = True)

    t.create_tl_actor_node(bg3.timeline_object.EMOTION, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_emotion_key(0.0, 2, is_sustained = False),
        t.create_emotion_key(6.74, 2, variation = 1),
    ), is_snapped_to_end = True)

    t.create_tl_actor_node(bg3.timeline_object.LOOK_AT, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_look_at_key('0.0', target = bg3.SPEAKER_PLAYER, bone = 'Head_M', turn_mode = 3, weight = 0.0, safe_zone_angle = 80, head_safe_zone_angle = 80, reset = True, look_at_mode = 1, eye_look_at_bone = 'Head_M'),
    ), is_snapped_to_end = True)

    t.create_tl_actor_node(bg3.timeline_object.LOOK_AT, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        t.create_look_at_key('0.0', target = bg3.SPEAKER_SHADOWHEART, bone = 'Head_M', turn_mode = 3, weight = 0.0, safe_zone_angle = 80, head_safe_zone_angle = 80, reset = True, look_at_mode = 1, eye_look_at_bone = 'Head_M'),
    ), is_snapped_to_end = True)


    t.create_tl_actor_node(bg3.timeline_object.SHOW_WEAPON, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        t.create_value_key(time = '0.0', interpolation_type = 3, value_name = 'ShowWeapon', value = False),
    ), is_snapped_to_end = True)

    t.create_tl_actor_node(bg3.timeline_object.SHOW_WEAPON, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_value_key(time = '0.0', interpolation_type = 3, value_name = 'ShowWeapon', value = False),
    ), is_snapped_to_end = True)

    t.create_tl_show_armor(bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
        (), (), (),
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
        (), (), (), (), (), (),
    ), is_snapped_to_end = True)

    t.create_tl_show_armor(bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
        (), (), (),
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
        (), (), (), (), (), (),
    ), is_snapped_to_end = True)

    t.create_tl_actor_node(bg3.timeline_object.SOUND, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        t.create_sound_event_key('1.47', sound_event_id = 'd0756d07-fd81-4fab-b4af-03d565c7f059', sound_object_index = 4),
        t.create_sound_event_key('5.18', sound_event_id = 'c232329e-2d4e-4f0c-a4d4-ea1585fce27c', sound_object_index = 4),
        t.create_sound_event_key('6.46', sound_event_id = '5dac329f-b08a-412d-84bc-86fc1aecae45', sound_object_index = 4),
    ), is_snapped_to_end = True)

    t.create_tl_actor_node(bg3.timeline_object.SOUND, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        t.create_sound_event_key('2.08', sound_event_id = 'ffbbbd57-5c31-444d-bc3a-c3d14df0be53', sound_object_index = 4),
        t.create_sound_event_key('3.51', sound_event_id = 'ffbbbd57-5c31-444d-bc3a-c3d14df0be53', sound_object_index = 4),
        t.create_sound_event_key('5.03', sound_event_id = '6dbe237a-0c78-4023-a6b7-30349e0505db', sound_object_index = 4),
    ), is_snapped_to_end = True)


    t.create_tl_actor_node(bg3.timeline_object.SOUND, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        t.create_sound_event_key('1.25', sound_type = 4),
    ), is_snapped_to_end = True)

    t.create_tl_actor_node(bg3.timeline_object.PHYSICS, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        t.create_value_key(time = '0.0', interpolation_type = 3, value_name = 'InverseKinematics', value = False),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.PHYSICS, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_value_key(time = '0.0', interpolation_type = 3, value_name = 'InverseKinematics', value = False),
    ), is_snapped_to_end = True)

    t.create_tl_non_actor_node(bg3.timeline_object.SWITCH_STAGE, '0.0', phase_duration, (
        t.create_value_key(time = '0.0', interpolation_type = 3, value_name = 'SwitchStageEventID', value_type = 'guid', value = 'a60b7f65-3604-445d-9555-5d1b9d03466a'),
    ), is_snapped_to_end = True)

    t.create_tl_transform(bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        (t.create_value_key(time = '0.0', interpolation_type = 3, value_type = 'float', value = '0'),),
        (t.create_value_key(time = '0.0', interpolation_type = 3, value_type = 'float', value = '0.0'),),
        (t.create_value_key(time = '0.0', interpolation_type = 3, value_type = 'float', value = '0.51'),),
        (t.create_value_key(time = '0.0', interpolation_type = 3, value_type = 'fvec4', value = (0, 0, 0, 1)),),
        (),
        (),
    ), is_snapped_to_end = True)

    t.create_tl_transform(bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        (t.create_value_key(time = '0.0', interpolation_type = 3, value_type = 'float', value = '0'),),
        (t.create_value_key(time = '0.0', interpolation_type = 3, value_type = 'float', value = '0.0'),),
        (t.create_value_key(time = '0.0', interpolation_type = 3, value_type = 'float', value = '-1.43'),),
        (t.create_value_key(time = '0.0', interpolation_type = 3, value_type = 'fvec4', value = (0, 1, 0, 0)),),
        (),
        (),
    ), is_snapped_to_end = True)

    # Animation
    t.create_tl_animation(bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, '2f5c6a06-f8d6-47fe-ae02-2a813a072ee1', '44947527-98b9-40b8-9257-fc1e93dd2d6d', fade_in = 0.0, fade_out = 2.0, animation_play_start_offset = 0.89, is_snapped_to_end = True)

    camera = '1df3c3cc-13c4-4876-b76f-ad6dd2759185'

    # Shot 1
    t.create_tl_camera_fov(camera, '0.0', '0.94', (
        t.create_value_key(time = '0.0', interpolation_type = 0, value_name = 'FoV', value_type = 'float', value = '25'),
    ))
    t.create_tl_transform(camera, '0.0', '0.94', (
        (t.create_value_key(time = '0.0', interpolation_type = 3, value_type = 'float', value = '0.6'),),
        (t.create_value_key(time = '0.0', interpolation_type = 3, value_type = 'float', value = '1.7'),),
        (t.create_value_key(time = '0.0', interpolation_type = 3, value_type = 'float', value = '-1.9'),),
        (t.create_value_key(time = '0.0', interpolation_type = 5, value_type = 'fvec4', value = bg3.euler_to_quaternion(-30, 6, 0, sequence='yxz')),),
        (),
        (),
    ))
    t.create_tl_shot(camera, '0.0', '0.94', disable_conditional_staging = True)

    # Animation
    t.create_tl_animation(bg3.SPEAKER_PLAYER, '0.94', phase_duration, 'ea57b48c-5037-b94a-20dd-f00a53fafa83', '892fd6c7-3dcb-4b9a-9cd2-d459ad535041', fade_in = 0.0, fade_out = 1.7, animation_play_start_offset = 1.83, is_snapped_to_end = True)

    # Lips 1
    t.create_tl_animation(bg3.SPEAKER_PLAYER, '0.94', '5.76', 'c26b9b0a-20cc-44a4-a499-18d6d78abec5', '4aa23917-7cb8-48c5-9484-c08820191cca', animation_slot = 1, animation_play_start_offset = 6.33, fade_in = 1.0, fade_out = 1.0)
    t.create_tl_animation(bg3.SPEAKER_SHADOWHEART, '0.94', '5.76', 'c26b9b0a-20cc-44a4-a499-18d6d78abec5', '9f1c3f9f-a2da-4859-8787-c2ecccfd901a', animation_slot = 1, animation_play_start_offset = 6.8, fade_in = 1.0, fade_out = 1.0)

    # Shot 2
    t.create_tl_camera_fov(camera, '0.94', '3.27', (
        t.create_value_key(time = '0.94', interpolation_type = 0, value_name = 'FoV', value_type = 'float', value = '25'),
    ))
    t.create_tl_transform(camera, '0.94', '3.27', (
        (t.create_value_key(time = '0.94', interpolation_type = 3, value_type = 'float', value = '0.4'),),
        (t.create_value_key(time = '0.94', interpolation_type = 3, value_type = 'float', value = '1.7'),),
        (t.create_value_key(time = '0.94', interpolation_type = 3, value_type = 'float', value = '0.9'),),
        (t.create_value_key(time = '0.94', interpolation_type = 5, value_type = 'fvec4', value = bg3.euler_to_quaternion(-164, 5, 0, sequence='yxz')),),
        (),
        (),
    ))
    t.create_tl_shot(camera, '0.94', '3.27', disable_conditional_staging = True)

    # Shot 3
    t.create_tl_camera_fov(camera, '3.27', '5.45', (
        t.create_value_key(time = '3.27', interpolation_type = 0, value_name = 'FoV', value_type = 'float', value = '25'),
    ))
    t.create_tl_transform(camera, '3.27', '5.45', (
        (t.create_value_key(time = '3.27', interpolation_type = 3, value_type = 'float', value = '1.2'),),
        (t.create_value_key(time = '3.27', interpolation_type = 3, value_type = 'float', value = '1.7'),),
        (t.create_value_key(time = '3.27', interpolation_type = 3, value_type = 'float', value = '-0.5'),),
        (t.create_value_key(time = '3.27', interpolation_type = 5, value_type = 'fvec4', value = bg3.euler_to_quaternion(-95, 0, 0, sequence='yxz')),),
        (),
        (),
    ))
    t.create_tl_shot(camera, '3.27', '5.45', disable_conditional_staging = True)

    # Shot 4
    t.create_tl_camera_fov(camera, '5.45', '7.67', (
        t.create_value_key(time = '5.45', interpolation_type = 0, value_name = 'FoV', value_type = 'float', value = '27'),
    ))
    t.create_tl_transform(camera, '5.45', '7.67', (
        (t.create_value_key(time = '5.45', interpolation_type = 3, value_type = 'float', value = '0.5'),),
        (t.create_value_key(time = '5.45', interpolation_type = 3, value_type = 'float', value = '1.75'),),
        (t.create_value_key(time = '5.45', interpolation_type = 3, value_type = 'float', value = '-0.5'),),
        (t.create_value_key(time = '5.45', interpolation_type = 5, value_type = 'fvec4', value = bg3.euler_to_quaternion(-87, 7, 0, sequence='yxz')),),
        (),
        (),
    ))
    t.create_tl_shot(camera, '05.45', '7.67', disable_conditional_staging = True)

    # Lips 2
    t.create_tl_animation(bg3.SPEAKER_PLAYER, '6.13', '7.1', 'c26b9b0a-20cc-44a4-a499-18d6d78abec5', '4aa23917-7cb8-48c5-9484-c08820191cca', animation_slot = 1, animation_play_start_offset = 7.3, fade_in = 0.41, fade_out = 0.55)
    t.create_tl_animation(bg3.SPEAKER_SHADOWHEART, '6.13', '6.97', 'c26b9b0a-20cc-44a4-a499-18d6d78abec5', '9f1c3f9f-a2da-4859-8787-c2ecccfd901a', animation_slot = 1, animation_play_start_offset = 7.85)

    # Shot 5
    t.create_tl_camera_fov(camera, '7.67', '9.0', (
        t.create_value_key(time = '7.67', interpolation_type = 0, value_name = 'FoV', value_type = 'float', value = '30'),
    ))
    t.create_tl_transform(camera, '7.67', '9.0', (
        (t.create_value_key(time = '7.67', interpolation_type = 3, value_type = 'float', value = '0.4'),),
        (t.create_value_key(time = '7.67', interpolation_type = 3, value_type = 'float', value = '1.75'),),
        (t.create_value_key(time = '7.67', interpolation_type = 3, value_type = 'float', value = '-0.9'),),
        (t.create_value_key(time = '7.67', interpolation_type = 5, value_type = 'fvec4', value = bg3.euler_to_quaternion(-48, 7, 0, sequence='yxz')),),
        (),
        (),
    ))
    t.create_tl_shot(camera, '7.67', '9.0', disable_conditional_staging = True)

    # Shot 6
    t.create_tl_camera_fov('c3eb0d95-3e47-4b67-9dd2-036c93fb0a44', '9.0', phase_duration, (), is_snapped_to_end = True)
    t.create_tl_transform('c3eb0d95-3e47-4b67-9dd2-036c93fb0a44', '9.0', phase_duration, ((), (), (), (), (), ()), is_snapped_to_end = True)
    t.create_tl_shot('c3eb0d95-3e47-4b67-9dd2-036c93fb0a44', '9.0', phase_duration, is_snapped_to_end = True)


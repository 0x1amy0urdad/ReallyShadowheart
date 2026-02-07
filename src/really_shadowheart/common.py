from __future__ import annotations

import bg3moddinglib as bg3

from .flags import Really_Shadowheart_Softened_Version

def create_approval_fork(
    d: bg3.dialog_object,
    target_node_uuid: str,
    new_approval: bg3.reaction_object,
    skip_new_approval_global_flag_uuid: str | None = None
) -> str:
    if skip_new_approval_global_flag_uuid is None:
        skip_new_approval_global_flag_uuid = Really_Shadowheart_Softened_Version.uuid
    target_node = d.find_dialog_node(target_node_uuid)
    ori_approval_uuid = bg3.get_bg3_attribute(target_node, 'ApprovalRatingID')
    if ori_approval_uuid is not None:
        bg3.delete_bg3_attribute(target_node, 'ApprovalRatingID')
    result_node_uuid = bg3.new_random_uuid()
    new_approval_node_uuid = bg3.new_random_uuid()
    old_approval_node_uuid = bg3.new_random_uuid()
    d.create_standard_dialog_node(
        result_node_uuid,
        bg3.SPEAKER_PLAYER,
        [new_approval_node_uuid, old_approval_node_uuid],
        None)
    d.create_standard_dialog_node(
        new_approval_node_uuid,
        bg3.SPEAKER_PLAYER,
        [target_node_uuid],
        None,
        checkflags = (
            bg3.flag_group('Global', (
                bg3.flag(skip_new_approval_global_flag_uuid, False, None),
            )),
        ),
        approval_rating_uuid = new_approval.uuid)
    d.create_standard_dialog_node(
        old_approval_node_uuid,
        bg3.SPEAKER_PLAYER,
        [target_node_uuid],
        None,
        checkflags = (
            bg3.flag_group('Global', (
                bg3.flag(skip_new_approval_global_flag_uuid, True, None),
            )),
        ),
        approval_rating_uuid = ori_approval_uuid)
    return result_node_uuid

def create_hug_timeline(
        dialog_node_uuid: str,
        t: bg3.timeline_object,
        actor1: str,
        actor2: str,
        camera1: str,
        camera2: str,
        camera3: str,
        camera4: str
) -> None:
    phase_duration = '24.55'
    t.create_new_phase(dialog_node_uuid, phase_duration)

    t.create_tl_actor_node(bg3.timeline_object.ATTITUDE, actor1, '0.0', phase_duration, (
        t.create_attitude_key(0.0, bg3.ATTITUDE_DIAG_Pose_Stand_L_Forward_01, bg3.ATTITUDE_DIAG_T_Pose),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.ATTITUDE, actor2, '0.0', phase_duration, (
        t.create_attitude_key(0.0, bg3.ATTITUDE_DIAG_Pose_Stand_L_Forward_01, bg3.ATTITUDE_DIAG_T_Pose),
    ), is_snapped_to_end = True)

    t.create_tl_actor_node(bg3.timeline_object.EMOTION, actor1, '0.0', phase_duration, (
        t.create_emotion_key(9.87, 2, variation = 1),
        t.create_emotion_key(12.71, 2, variation = 2),
        t.create_emotion_key(15.96, 2, variation = 1),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.EMOTION, actor2, '0.0', phase_duration, (
        t.create_emotion_key(0.0, 2),
        t.create_emotion_key(5.22, 2, variation = 2),
        t.create_emotion_key(19.67, 2, variation = 1),
    ), is_snapped_to_end = True)

    t.create_tl_actor_node(bg3.timeline_object.LOOK_AT, actor1, '0.0', phase_duration, (
        t.create_look_at_key(
            0.0,
            target = actor2,
            bone = 'Head_M',
            turn_mode = 3,
            turn_speed_multiplier = 0.3,
            head_turn_speed_multiplier = 0.3,
            weight = 0,
            safe_zone_angle = 80,
            head_safe_zone_angle = 80,
            reset = True,
            look_at_mode = 1,
            eye_look_at_bone = 'Head_M'
        ),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.LOOK_AT, actor2, '0.0', phase_duration, (
        t.create_look_at_key(
            0.0,
            target = actor1,
            bone = 'Head_M',
            turn_mode = 3,
            turn_speed_multiplier = 0.3,
            head_turn_speed_multiplier = 0.3,
            weight = 0,
            safe_zone_angle = 80,
            head_safe_zone_angle = 80,
            reset = True,
            look_at_mode = 1,
            eye_look_at_bone = 'Head_M'
        ),
    ), is_snapped_to_end = True)

    t.create_tl_non_actor_node(bg3.timeline_object.SWITCH_LOCATION, '0.0', phase_duration, (), is_snapped_to_end = True)

    t.create_tl_transform(actor1, '0.0', phase_duration, (
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 0.282674465),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 0.0),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = -0.5080471000000006),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = (0.0, 0.96666896, 0.0, 0.25602978)),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 1.0),
        ),
        (),
    ), is_snapped_to_end = True)
    t.create_tl_transform(actor2, '0.0', phase_duration, (
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = -0.282674465),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 0.0),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 0.5080471000000006),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = (0.0, -0.24996054, 0.0, 0.96825606)),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 1.0),
        ),
        (),
    ), is_snapped_to_end = True)

    t.create_tl_animation(
        actor1,
        '0.0', '13.06',
        '882164de-1f6b-4d2a-b336-1f366cb36f14',
        'a2dae3f2-e3c9-4fc7-b8ac-82abf4a153b0',
        fade_in = 0.0,
        fade_out = 0.94)
    t.create_tl_animation(
        actor2,
        '0.0', '13.06',
        'a46f695f-051b-be6d-20cd-32f733524930',
        'c8dad77b-5b76-44fe-bfeb-61d676ede3f6',
        fade_in = 0.0,
        fade_out = 0.94)

    t.create_tl_shot(camera1, '0.0', '7.32')
    t.create_tl_shot(camera2, '7.32', '14.11')

    t.create_tl_animation(
        actor1,
        '12.12', '21.67',
        '882164de-1f6b-4d2a-b336-1f366cb36f14',
        'a2dae3f2-e3c9-4fc7-b8ac-82abf4a153b0',
        fade_in = 0.0,
        fade_out = 0.0,
        animation_play_start_offset = 6.29)
    t.create_tl_animation(
        actor2,
        '12.12', '21.67',
        'a46f695f-051b-be6d-20cd-32f733524930',
        'c8dad77b-5b76-44fe-bfeb-61d676ede3f6',
        fade_in = 0.0,
        fade_out = 0.0,
        animation_play_start_offset = 6.29)

    t.create_tl_shot(camera3, '14.11', '21.67')
    t.create_tl_shot(camera4, '21.67', phase_duration, is_snapped_to_end = True)

    t.create_tl_animation(
        actor1,
        '21.67', phase_duration,
        '882164de-1f6b-4d2a-b336-1f366cb36f14',
        'a2dae3f2-e3c9-4fc7-b8ac-82abf4a153b0',
        fade_in = 0.0,
        fade_out = 2.0,
        animation_play_start_offset = 16.79,
        is_snapped_to_end = True)
    t.create_tl_animation(
        actor2,
        '21.67', phase_duration,
        'a46f695f-051b-be6d-20cd-32f733524930',
        'c8dad77b-5b76-44fe-bfeb-61d676ede3f6',
        fade_in = 0.0,
        fade_out = 1.44,
        animation_play_start_offset = 16.79,
        is_snapped_to_end = True)

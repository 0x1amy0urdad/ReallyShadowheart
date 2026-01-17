from __future__ import annotations

import bg3moddinglib as bg3

from .context import get_context

# Karlach_InParty cameras
# faff6369-2b1f-43ab-84c6-ce9c94647e1e Tav -> Tav
# e254b080-47c1-4728-a3ba-6bba37077445 Tav -> Tav
# cf1398b0-4598-4712-ab14-4443d0fc5d2f Tav -> Tav
# aecf415c-184a-4a0d-a7c2-2737d537d88f Tav -> SH
# 94f83a30-dda7-4f70-a9de-42ab121ba651 Tav -> SH
# cc7b5bb2-af67-4efd-9590-7fea09608cc1 Tav -> SH
# ca9238a1-755c-4a26-8a2a-fa9e101a4b59 Tav -> SH
# 9b7836f2-518c-485a-b203-38daccae8079 Tav -> SH
# 7bcc10aa-f1c1-4de3-b073-40c9e7c6704c SH  -> Tav
# 41f80ee2-9674-45b9-a7ed-b0e03323c3e0 SH  -> Tav
# ba57ffaf-99d3-423c-bdda-4eeb62b8846a SH  -> Tav
# 964b853c-2f1e-4295-a91d-b16c3f005f94 SH  -> Tav
# 384ed026-1542-4714-9383-1fcf418302a5 SH  -> SH
# b5174f2a-9890-4673-91e6-955b1a3071f1 SH  -> SH

# 0c6b1ef9-01d1-4433-b5ed-aa85d01cb220 Push Back
# 42192fe3-33b5-4a60-8f78-f8eedcc6b430 VariationBaseStageId 0c6b1ef9-01d1-4433-b5ed-aa85d01cb220
# 85465820-04dc-4e33-ae22-d9123f00da86 Push Side
# 5ddb2829-dfa1-4f42-83a3-9890b16e7866 Kiss Tall (A)
# f12979e6-d959-4074-bec0-382aa26ace5b Kiss Tall (C)
# 2c361b29-c4db-4441-b32a-35d52af6d9dd Kiss Tall (D)
# c5f14459-3546-4873-a16a-dc5b75cb5ecb Kiss Short (A)
# 50055889-90c7-48a3-9153-66ae67781965 Kiss Short (C)
# ca30fd09-fdd6-42df-9c97-f20f7288b16c Kiss Short (D)
# 7190860d-f11d-4ed4-b270-dca21d2bd49b Kiss Strong (A)
# 568cdfc7-a642-46a9-be72-40e12aa607b3 Kiss Strong (C)
# 2890e875-b9cf-4c2d-ae35-437d4cc34baa Kiss Strong (D)
# 92089f00-7898-4299-9136-b06de010749a Kiss Short (Reuse) (B)
# 0ade66ba-2f91-4a6d-b9e5-8cc3bece62d7 Kiss Tall (Reuse) (B)
# 8002bea3-7c3a-47ba-b702-e2439caafc22 Kiss Stong (Reuse) (B)


# Shadowheart_InParty2_Nested_ShadowheartKiss cameras
# cb95fcb5-efd7-48f4-9352-5eaeb3e44274 Tav -> Tav
# 64edf86f-1d72-47fd-b908-a444cadb2fc3 Tav -> Tav
# c3eb0d95-3e47-4b67-9dd2-036c93fb0a44 Tav -> Tav
# 1df3c3cc-13c4-4876-b76f-ad6dd2759185 Tav -> SH
# 33a18aa0-5996-441f-940b-1179758c5834 Tav -> SH
# 89eeac49-0759-420d-8f99-3b76a8b2b7e8 Tav -> SH
# 18c5bd4f-c066-4c52-8cdb-d8bbe1d8034e Tav -> SH
# 99480a46-e5ff-4101-ab73-d0ce43403c57 Tav -> SH
# fb91b3e2-b1b9-47d5-8478-659cececad9b SH  -> Tav
# befcdee8-6352-4be6-b2ea-23c2ac0dfe60 SH  -> Tav
# a43f207a-ed78-4acf-9815-9103e41577d0 SH  -> Tav
# 9de43fdc-0612-4161-9f37-d975d5ca409c SH  -> Tav
# 7c0cf47f-81b5-4949-bf43-ae0fb233324f SH  -> SH

# Shadowheart_InParty2_Nested_ShadowheartKiss stages
# a60b7f65-3604-445d-9555-5d1b9d03466a Kiss_Tall
# 1534d564-e4f1-463f-b685-cc75ee2b0271 Kiss_Short
# d4b2d3ac-d576-4bad-b6aa-abadfce41f0e Kiss_Strong/DGB
# 3c108a72-4181-44af-baf1-e919eab6b84c Nightfall kiss Tall
# 22f273d7-f95d-47ea-b9b5-3bc1c636472f Nightfall kiss Strong/DGB
# 238c6f45-ecd5-4c0c-b673-5b7eba63d737 Nightfall kiss Short
# 59ff581c-2c1e-4374-80d6-907e2639207f Kiss_Tall_Selune01
# cfe7addb-43c0-499d-8cec-27f11eb2c871 Kiss_Strong/DGB_Selune01
# 11b556ac-b4cd-43b3-82c7-63b7dbd7c3d3 Kiss_Tall_WalkAroundSelune
# fa340083-8918-46d0-a452-9a1fb82458bb Kiss_Short_WalkAroundSelune
# 8da6a55d-fc88-43d4-84dd-eaf52a2266e9 Kiss_Dwarf_WalkAroundSelune
# f71e36cc-bba2-4c9d-ab6b-73b8da9192fa Kiss_Strong_WalkAroundSelune
# c292d1a6-e717-4c26-b889-87c07a8e1dad Kiss_Tall_WalkAroundShar
# 8e34a1c6-1386-46c9-b3c0-9fc018fe1780 Kiss_Short_WalkAroundShar
# 13887d67-83bd-40e7-92c2-add3aa02b278 Kiss_Dwarf_WalkAroundShar
# ae072353-9eab-4c9c-a660-8ea7442813fe Kiss_Strong_WalkAroundShar


# kiss A phase 188 c70f4b7d-8714-6563-321e-28d659e035b4   stage 5ddb2829-dfa1-4f42-83a3-9890b16e7866
# kiss B phase 133 4a16c3aa-729e-2db5-7ace-140138032565   stage 0ade66ba-2f91-4a6d-b9e5-8cc3bece62d7
# kiss C phase 232 4fcc5a07-b232-aa59-f94f-6febc4e36aad   stage f12979e6-d959-4074-bec0-382aa26ace5b
# kiss D phase 129 3ac67837-2c58-913a-7ea9-a4b1e24dee71   stage 2c361b29-c4db-4441-b32a-35d52af6d9dd

# d09df5a0-557c-fe01-1281-b28df602d692 BT1 actor (Shadowheart)
# 26b59002-38c0-2867-3511-20d1d8184db6 BT3 actor (Tav)

def create_karlach_kiss_A_timeline(t: bg3.timeline_object, dialog_uuid: str, body_type: str) -> None:
    phase_duration = '28.9'

    t.create_new_phase(dialog_uuid, phase_duration)

    t.create_tl_actor_node(bg3.timeline_object.ATTITUDE, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.ATTITUDE, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (), is_snapped_to_end = True)

    t.create_tl_actor_node(bg3.timeline_object.EMOTION, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        t.create_emotion_key(0.0, 2),
        t.create_emotion_key(2.41, 64, variation = 1),
        t.create_emotion_key(3.8399, 2, variation = 1),
        t.create_emotion_key(6.53, 2, variation = 2),
        t.create_emotion_key(16.9218, 256),
        t.create_emotion_key(19.02, 2, variation = 23),
        t.create_emotion_key(20.17, 2, variation = 2),
        t.create_emotion_key(21.37, 1024, variation = 2),
        t.create_emotion_key(24.56, 2, variation = 1),
        t.create_emotion_key(27.3599, 2),
    ), is_snapped_to_end = True)

    t.create_tl_actor_node(bg3.timeline_object.EMOTION, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_emotion_key(0.0, 64, variation = 1),
        t.create_emotion_key(0.8299, 2, variation = 1),
        t.create_emotion_key(6.3199, 2, variation = 2),
        t.create_emotion_key(16.04, 2, variation = 1),
        t.create_emotion_key(18.54, 256, variation = 24),
        t.create_emotion_key(19.2199, 2, variation = 2),
        t.create_emotion_key(25.88, 2, variation = 1),
        t.create_emotion_key(27.91, 2),
    ), is_snapped_to_end = True)

    t.create_tl_actor_node(bg3.timeline_object.LOOK_AT, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        t.create_look_at_key('0.0', target = bg3.SPEAKER_SHADOWHEART, bone = 'Head_M', turn_mode = 3, turn_speed_multiplier = 0.3, head_turn_speed_multiplier = 0.3, weight = 0.5, safe_zone_angle = 80, reset = True, look_at_mode = 1, eye_look_at_bone = 'Head_M'),
        t.create_look_at_key('2.41', target = bg3.SPEAKER_SHADOWHEART, bone = 'Dummy_EyeFX_01', turn_mode = 3, turn_speed_multiplier = 0.3, head_turn_speed_multiplier = 0.3, weight = 0.5, safe_zone_angle = 80, head_safe_zone_angle = 80, offset = (0.097, -0.024, 0), reset = True, look_at_mode = 1, eye_look_at_bone = 'Head_M'),
        t.create_look_at_key('6.01', target = bg3.SPEAKER_SHADOWHEART, bone = 'Dummy_EyeFX_02', turn_mode = 3, turn_speed_multiplier = 0.3, head_turn_speed_multiplier = 0.3, weight = 0.0, safe_zone_angle = 80, head_safe_zone_angle = 80, offset = (0.2, -0.05, 0), reset = True, look_at_mode = 1, eye_look_at_bone = 'Head_M'),
        t.create_look_at_key('7.01', target = bg3.SPEAKER_SHADOWHEART, bone = 'Dummy_EyeFX_01', turn_mode = 3, turn_speed_multiplier = 0.3, head_turn_speed_multiplier = 0.3, weight = 0.0, safe_zone_angle = 80, head_safe_zone_angle = 80, reset = True, look_at_mode = 1, eye_look_at_bone = 'Head_M'),
        t.create_look_at_key('7.67', target = bg3.SPEAKER_SHADOWHEART, bone = 'Dummy_EyeFX_02', turn_mode = 3, turn_speed_multiplier = 0.3, head_turn_speed_multiplier = 0.3, weight = 0.0, safe_zone_angle = 80, head_safe_zone_angle = 80, offset = (0.1, -0.6, 0), reset = True, look_at_mode = 1, eye_look_at_bone = 'Head_M'),
        t.create_look_at_key('21.37', target = bg3.SPEAKER_SHADOWHEART, bone = 'Dummy_EyeFX_02', turn_mode = 3, turn_speed_multiplier = 0.3, head_turn_speed_multiplier = 0.3, weight = 0.0, safe_zone_angle = 80, head_safe_zone_angle = 80, reset = True, look_at_mode = 1, eye_look_at_bone = 'Head_M'),
    ), is_snapped_to_end = True)

    t.create_tl_actor_node(bg3.timeline_object.LOOK_AT, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_look_at_key('0.0', target = bg3.SPEAKER_PLAYER, bone = 'Head_M', turn_mode = 3, turn_speed_multiplier = 0.3, head_turn_speed_multiplier = 0, weight = 0.0, safe_zone_angle = 80, reset = True, look_at_mode = 1, eye_look_at_bone = 'Head_M'),
        t.create_look_at_key('3.52', target = bg3.SPEAKER_PLAYER, bone = 'Dummy_EyeFX_01', turn_mode = 3, turn_speed_multiplier = 0.3, head_turn_speed_multiplier = 0, weight = 0.0, safe_zone_angle = 80, head_safe_zone_angle = 80, reset = True, look_at_mode = 1, eye_look_at_bone = 'Head_M'),
        t.create_look_at_key('9.79', target = bg3.SPEAKER_PLAYER, bone = 'Dummy_EyeFX_01', turn_mode = 3, turn_speed_multiplier = 0.3, head_turn_speed_multiplier = 0, weight = 0.0, safe_zone_angle = 80, head_safe_zone_angle = 80, reset = True, look_at_mode = 1, eye_look_at_bone = 'Head_M'),
        t.create_look_at_key('14.12', target = bg3.SPEAKER_PLAYER, bone = 'Dummy_EyeFX_02', turn_mode = 3, turn_speed_multiplier = 0.3, head_turn_speed_multiplier = 0, weight = 0.0, safe_zone_angle = 80, head_safe_zone_angle = 80, reset = True, look_at_mode = 1, eye_look_at_bone = 'Head_M'),
        t.create_look_at_key('15.52', target = bg3.SPEAKER_PLAYER, bone = 'Chest_M', turn_mode = 3, turn_speed_multiplier = 0.3, head_turn_speed_multiplier = 0, weight = 0.0, safe_zone_angle = 80, head_safe_zone_angle = 80, offset = (0.0, 0, 0), reset = True, look_at_mode = 1, eye_look_at_bone = 'Head_M'),
        t.create_look_at_key('21.1521', target = bg3.SPEAKER_PLAYER, bone = 'Head_M', turn_mode = 3, turn_speed_multiplier = 0.3, head_turn_speed_multiplier = 0, weight = 0.0, safe_zone_angle = 80, head_safe_zone_angle = 80, reset = True, look_at_mode = 1, eye_look_at_bone = 'Head_M'),
        #t.create_look_at_key('25.1521', target = bg3.SPEAKER_PLAYER, bone = 'Head_M', turn_mode = 3, turn_speed_multiplier = 0.3, head_turn_speed_multiplier = 0, weight = 0.0, safe_zone_angle = 80, head_safe_zone_angle = 80, reset = True, look_at_mode = 1, eye_look_at_bone = 'Head_M'),
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
        t.create_sound_event_key('8.31', sound_event_id = '43838346-10a3-47a8-aa2e-34f70e75ecfd', sound_object_index = 4),
        t.create_sound_event_key('8.8618', sound_event_id = 'ffbbbd57-5c31-444d-bc3a-c3d14df0be53', sound_object_index = 4),
        t.create_sound_event_key('11.2299', sound_event_id = 'c9040e53-b055-47e3-ada2-0b5ce361f2eb', sound_object_index = 4),
        t.create_sound_event_key('18.8234', sound_event_id = '498739bb-20a9-40e0-aab4-411a4e1e4c7b', sound_object_index = 4),
        t.create_sound_event_key('24.4735', sound_event_id = '220abafa-e55f-4124-8cb7-16fca63fda5f', sound_object_index = 4),
    ), is_snapped_to_end = True)

    t.create_tl_actor_node(bg3.timeline_object.SOUND, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_sound_event_key('15.31', sound_event_id = '220abafa-e55f-4124-8cb7-16fca63fda5f', sound_object_index = 4),
    ), is_snapped_to_end = True)

    t.create_tl_actor_node(bg3.timeline_object.PHYSICS, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        t.create_value_key(time = '0.0', interpolation_type = 3, value_name = 'InverseKinematics', value = False),
    ), is_snapped_to_end = True)

    t.create_tl_actor_node(bg3.timeline_object.PHYSICS, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_value_key(time = '0.0', interpolation_type = 3, value_name = 'InverseKinematics', value = False),
    ), is_snapped_to_end = True)

    t.create_tl_non_actor_node(bg3.timeline_object.SWITCH_STAGE, '0.0', phase_duration, (
        t.create_value_key(time = '0.0', interpolation_type = 3, value_name = 'SwitchStageEventID', value_type = 'guid', value = 'd4b2d3ac-d576-4bad-b6aa-abadfce41f0e'),
    ), is_snapped_to_end = True)

    # Animations
    t.create_tl_animation(bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, 'dda67d77-e66f-454c-8312-5cb558a83fda', 'f9263445-b54b-49e6-8218-aa885673254e', fade_in = 0.0, fade_out = 2.0, offset_type = 5)
    t.create_tl_animation(bg3.SPEAKER_PLAYER, '0.0', phase_duration, '158c412a-b6a0-48b0-43a1-c8d6a43bf94d', 'fc4c399c-4634-4235-952d-51b8f5bae577', fade_in = 0.0, fade_out = 2.0, offset_type = 5)


    if body_type == 'bt2':
        t.create_tl_transform(bg3.SPEAKER_PLAYER, '0.0', '7.76', (
            (t.create_value_key(time = '0.0', interpolation_type = 3, value_type = 'float', value = '0'),),
            (t.create_value_key(time = '0.0', interpolation_type = 3, value_type = 'float', value = '0.05'),),
            (t.create_value_key(time = '0.0', interpolation_type = 3, value_type = 'float', value = '0.38'),),
            (t.create_value_key(time = '0.0', interpolation_type = 3, value_type = 'fvec4', value = (0, 0, 0, 1)),),
            (),
            (),
        ))

        t.create_tl_transform(bg3.SPEAKER_SHADOWHEART, '0.0', '7.76', (
            (t.create_value_key(time = '0.0', interpolation_type = 3, value_type = 'float', value = '0'),),
            (t.create_value_key(time = '0.0', interpolation_type = 3, value_type = 'float', value = '-0.05'),),
            (t.create_value_key(time = '0.0', interpolation_type = 3, value_type = 'float', value = '-0.81'),),
            (t.create_value_key(time = '0.0', interpolation_type = 3, value_type = 'fvec4', value = (0, 1, 0, 0)),),
            (),
            (),
        ))
    elif body_type == 'bt2_gith':
        t.create_tl_transform(bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
            (t.create_value_key(time = '0.0', interpolation_type = 3, value_type = 'float', value = '0'),),
            (t.create_value_key(time = '0.0', interpolation_type = 3, value_type = 'float', value = '0.05'),),
            (t.create_value_key(time = '0.0', interpolation_type = 3, value_type = 'float', value = '0.38'),),
            (t.create_value_key(time = '0.0', interpolation_type = 3, value_type = 'fvec4', value = (0, 0, 0, 1)),),
            (),
            (),
        ), is_snapped_to_end = True)

        t.create_tl_transform(bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
            (t.create_value_key(time = '0.0', interpolation_type = 3, value_type = 'float', value = '0'),),
            (t.create_value_key(time = '0.0', interpolation_type = 3, value_type = 'float', value = '-0.05'),),
            (t.create_value_key(time = '0.0', interpolation_type = 3, value_type = 'float', value = '-0.81'),),
            (t.create_value_key(time = '0.0', interpolation_type = 3, value_type = 'fvec4', value = (0, 1, 0, 0)),),
            (),
            (),
        ), is_snapped_to_end = True)
    else:
        t.create_tl_transform(bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
            (t.create_value_key(time = '0.0', interpolation_type = 3, value_type = 'float', value = '0'),),
            (t.create_value_key(time = '0.0', interpolation_type = 3, value_type = 'float', value = '0'),),
            (t.create_value_key(time = '0.0', interpolation_type = 3, value_type = 'float', value = '0.3820046'),),
            (t.create_value_key(time = '0.0', interpolation_type = 3, value_type = 'fvec4', value = (0, 0, 0, 1)),),
            (),
            (),
        ), is_snapped_to_end = True)

        t.create_tl_transform(bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
            (t.create_value_key(time = '0.0', interpolation_type = 3, value_type = 'float', value = '0'),),
            (t.create_value_key(time = '0.0', interpolation_type = 3, value_type = 'float', value = '0'),),
            (t.create_value_key(time = '0.0', interpolation_type = 3, value_type = 'float', value = '-0.8321319'),),
            (t.create_value_key(time = '0.0', interpolation_type = 3, value_type = 'fvec4', value = (0, 1, 0, 0)),),
            (),
            (),
        ), is_snapped_to_end = True)


    camera = '1df3c3cc-13c4-4876-b76f-ad6dd2759185'

    # Shot 1
    t.create_tl_camera_fov(camera, '0.0', '6.0',(
        t.create_value_key(time = '0.0', interpolation_type = 0, value_name = 'FoV', value_type = 'float', value = '25'),
    ))
    t.create_tl_transform(camera, '0.0', '3.52', (
        (t.create_value_key(time = '0.0', interpolation_type = 3, value_type = 'float', value = '-1.4'),),
        (t.create_value_key(time = '0.0', interpolation_type = 3, value_type = 'float', value = '1.6'),),
        (t.create_value_key(time = '0.0', interpolation_type = 3, value_type = 'float', value = '-1.3'),),
        (t.create_value_key(time = '0.0', interpolation_type = 3, value_type = 'fvec4', value = bg3.euler_to_quaternion(55, 0, 0, sequence='yxz')),),
        (),
        (),
    ))
    t.create_tl_shot(camera, '0.0', '3.52', disable_conditional_staging = True)

    # Shot 2
    t.create_tl_transform(camera, '3.52', '6.0', (
        (t.create_value_key(time = '3.52', interpolation_type = 3, value_type = 'float', value = '-1.4'),),
        (t.create_value_key(time = '3.52', interpolation_type = 3, value_type = 'float', value = '1.7'),),
        (t.create_value_key(time = '3.52', interpolation_type = 3, value_type = 'float', value = '0.4'),),
        (
            t.create_value_key(time = '3.52', interpolation_type = 5, value_type = 'fvec4', value = bg3.euler_to_quaternion(110, 0, 0, sequence='yxz')),
            t.create_value_key(time = '6.0', interpolation_type = 5, value_type = 'fvec4', value = bg3.euler_to_quaternion(120, 0, 0, sequence='yxz')),
        ),
        (),
        (),
    ))
    t.create_tl_shot(camera, '3.52', '6.0', disable_conditional_staging = True)

    # Shot 3
    t.create_tl_camera_fov(camera, '6.0', '7.76', (
        t.create_value_key(time = '6.0', interpolation_type = 0, value_name = 'FoV', value_type = 'float', value = '18'),
    ))
    t.create_tl_transform(camera, '6.0', '7.76', (
        (t.create_value_key(time = '6.0', interpolation_type = 3, value_type = 'float', value = '1.4'),),
        (t.create_value_key(time = '6.0', interpolation_type = 3, value_type = 'float', value = '1.7'),),
        (t.create_value_key(time = '6.0', interpolation_type = 3, value_type = 'float', value = '-1.3'),),
        (t.create_value_key(time = '6.0', interpolation_type = 3, value_type = 'fvec4', value = bg3.euler_to_quaternion(-55, 0, 0, sequence='yxz')),),
        (),
        (),
    ))
    t.create_tl_shot(camera, '6.0', '7.76', disable_conditional_staging = True)

    # Animations (lips)
    t.create_tl_animation(bg3.SPEAKER_PLAYER, '7.67', '13.26', 'a0e37a8e-c619-4d0a-840a-061831fb0523', 'bac848e1-c92b-41de-ac13-ad9384dc96aa', animation_slot = 1, animation_play_rate = 0.85, fade_in = 1.0, fade_out = 0.8)
    t.create_tl_animation(bg3.SPEAKER_SHADOWHEART, '7.67', '12.91', 'c26b9b0a-20cc-44a4-a499-18d6d78abec5', 'dde3a70e-60d6-44f0-902b-030ec719f697', animation_slot = 1, animation_play_rate = 0.85, fade_in = 1.0, fade_out = 0.8)

    # Shot 4
    t.create_tl_camera_fov(camera, '7.76', '14.5', (
        t.create_value_key(time = '7.76', interpolation_type = 0, value_name = 'FoV', value_type = 'float', value = '15'),
    ))
    if body_type == 'bt2':
        t.create_tl_transform(bg3.SPEAKER_PLAYER, '7.76', '14.5', (
            (t.create_value_key(time = '7.76', interpolation_type = 3, value_type = 'float', value = '0'),),
            (t.create_value_key(time = '7.76', interpolation_type = 3, value_type = 'float', value = '0.05'),),
            (t.create_value_key(time = '7.76', interpolation_type = 3, value_type = 'float', value = '0.387'),),
            (t.create_value_key(time = '7.76', interpolation_type = 3, value_type = 'fvec4', value = (0, 0, 0, 1)),),
            (),
            (),
        ))

        t.create_tl_transform(camera, '7.76', '14.5', (
            (t.create_value_key(time = '7.76', interpolation_type = 3, value_type = 'float', value = '0.8'),),
            (t.create_value_key(time = '7.76', interpolation_type = 3, value_type = 'float', value = '1.8'),),
            (t.create_value_key(time = '7.76', interpolation_type = 3, value_type = 'float', value = '0.7'),),
            (t.create_value_key(time = '7.76', interpolation_type = 3, value_type = 'fvec4', value = bg3.euler_to_quaternion(-135, 0, 0, sequence='yxz')),),
            (),
            (),
        ))        
    elif body_type == 'bt2_gith':
        t.create_tl_transform(camera, '7.76', '14.5', (
            (t.create_value_key(time = '7.76', interpolation_type = 3, value_type = 'float', value = '0.3'),),
            (t.create_value_key(time = '7.76', interpolation_type = 3, value_type = 'float', value = '1.8'),),
            (t.create_value_key(time = '7.76', interpolation_type = 3, value_type = 'float', value = '0.8'),),
            (t.create_value_key(time = '7.76', interpolation_type = 3, value_type = 'fvec4', value = bg3.euler_to_quaternion(-160, 0, 0, sequence='yxz')),),
            (),
            (),
        ))
    else:
        t.create_tl_transform(camera, '7.76', '14.5', (
            (t.create_value_key(time = '7.76', interpolation_type = 3, value_type = 'float', value = '0.8'),),
            (t.create_value_key(time = '7.76', interpolation_type = 3, value_type = 'float', value = '1.8'),),
            (t.create_value_key(time = '7.76', interpolation_type = 3, value_type = 'float', value = '0.7'),),
            (t.create_value_key(time = '7.76', interpolation_type = 3, value_type = 'fvec4', value = bg3.euler_to_quaternion(-135, 0, 0, sequence='yxz')),),
            (),
            (),
        ))
    t.create_tl_shot(camera, '7.76', '14.5', disable_conditional_staging = True)


    # Shot 5
    # t.create_tl_transform(camera, '14.5', '25.15', (
    #     (t.create_value_key(time = '14.5', interpolation_type = 3, value_type = 'float', value = '-1.1'),),
    #     (t.create_value_key(time = '14.5', interpolation_type = 3, value_type = 'float', value = '1.8'),),
    #     (t.create_value_key(time = '14.5', interpolation_type = 3, value_type = 'float', value = '-0.3'),),
    #     (t.create_value_key(time = '14.5', interpolation_type = 5, value_type = 'fvec4', value = bg3.euler_to_quaternion(80, 0, 0, sequence='yxz')),),
    #     (),
    #     (),
    # ))
    if body_type == 'bt2':
        t.create_tl_transform(bg3.SPEAKER_PLAYER, '14.5', phase_duration, (
            (t.create_value_key(time = '14.5', interpolation_type = 3, value_type = 'float', value = '0'),),
            (t.create_value_key(time = '14.5', interpolation_type = 3, value_type = 'float', value = '0.05'),),
            (t.create_value_key(time = '14.5', interpolation_type = 3, value_type = 'float', value = '0.38'),),
            (t.create_value_key(time = '14.5', interpolation_type = 3, value_type = 'fvec4', value = (0, 0, 0, 1)),),
            (),
            (),
        ))
    t.create_tl_camera_fov(camera, '14.5', phase_duration, (
        t.create_value_key(time = '14.5', interpolation_type = 0, value_name = 'FoV', value_type = 'float', value = '22'),
    ), is_snapped_to_end = True)
    t.create_tl_transform(camera, '14.5', '25.15', (
        (t.create_value_key(time = '14.5', interpolation_type = 3, value_type = 'float', value = '-1.0'),),
        (t.create_value_key(time = '14.5', interpolation_type = 3, value_type = 'float', value = '1.9'),),
        (t.create_value_key(time = '14.5', interpolation_type = 3, value_type = 'float', value = '0.1'),),
        (t.create_value_key(time = '14.5', interpolation_type = 3, value_type = 'fvec4', value = bg3.euler_to_quaternion(115, 6, 0, sequence='yxz')),),
        (),
        (),
    ))
    t.create_tl_shot(camera, '14.5', '25.15', disable_conditional_staging = True)

    # Shot 6
    t.create_tl_transform('99480a46-e5ff-4101-ab73-d0ce43403c57', '25.15', phase_duration, ((), (), (), (), (), ()), is_snapped_to_end = True)
    t.create_tl_shot('99480a46-e5ff-4101-ab73-d0ce43403c57', '25.15', phase_duration, is_snapped_to_end = True)


def create_karlach_kiss_B_timeline(t: bg3.timeline_object, dialog_uuid: str, body_type: str) -> None:
    # e254b080-47c1-4728-a3ba-6bba37077445
    # 94f83a30-dda7-4f70-a9de-42ab121ba651
    # 7bcc10aa-f1c1-4de3-b073-40c9e7c6704c
    # b5174f2a-9890-4673-91e6-955b1a3071f1
    # ba57ffaf-99d3-423c-bdda-4eeb62b8846a
    phase_duration = '9.5'

    t.create_new_phase(dialog_uuid, phase_duration)

    t.create_tl_actor_node(bg3.timeline_object.ATTITUDE, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.ATTITUDE, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (), is_snapped_to_end = True)

    t.create_tl_actor_node(bg3.timeline_object.EMOTION, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        t.create_emotion_key(0.0, 2),
        t.create_emotion_key(1.65, 2, variation = 1),
        t.create_emotion_key(2.25, 256),
        t.create_emotion_key(6.82, 2, variation = 2),
    ), is_snapped_to_end = True)

    t.create_tl_actor_node(bg3.timeline_object.EMOTION, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_emotion_key(0.0, 2),
        t.create_emotion_key(2.5, 256),
        t.create_emotion_key(5.28, 2, variation = 1),
        t.create_emotion_key(6.93, 2),
    ), is_snapped_to_end = True)

    t.create_tl_actor_node(bg3.timeline_object.LOOK_AT, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        t.create_look_at_key('0.0', target = bg3.SPEAKER_SHADOWHEART, bone = 'Head_M', turn_mode = 3, turn_speed_multiplier = 0.3, head_turn_speed_multiplier = 0.3, weight = 0.0, safe_zone_angle = 80, head_safe_zone_angle = 80, reset = True, look_at_mode = 1, eye_look_at_bone = 'Head_M'),
        t.create_look_at_key('1.25', target = bg3.SPEAKER_SHADOWHEART, bone = 'Head_M', turn_mode = 3, turn_speed_multiplier = 0.3, head_turn_speed_multiplier = 0.05, weight = 0.0, safe_zone_angle = 80, head_safe_zone_angle = 80, reset = True, look_at_mode = 1, eye_look_at_bone = 'Head_M'),
        t.create_look_at_key('6.5', target = bg3.SPEAKER_SHADOWHEART, bone = 'Head_M', turn_mode = 3, turn_speed_multiplier = 0.05, head_turn_speed_multiplier = 0.05, weight = 0.15, safe_zone_angle = 80, head_safe_zone_angle = 80, is_eye_look_at_enabled = True, eye_look_at_target_id = bg3.SPEAKER_SHADOWHEART, eye_look_at_bone = 'Head_M'),
    ), is_snapped_to_end = True)

    t.create_tl_actor_node(bg3.timeline_object.LOOK_AT, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_look_at_key('0.0', target = bg3.SPEAKER_PLAYER, bone = 'Head_M', turn_mode = 3, tracking_mode = 1, turn_speed_multiplier = 0.05, head_turn_speed_multiplier = 0.05, weight = 0.5, head_safe_zone_angle = 80, reset = True, is_eye_look_at_enabled = True, eye_look_at_target_id = bg3.SPEAKER_PLAYER, eye_look_at_bone = 'Head_M'),
        t.create_look_at_key('1.25', turn_mode = 3, tracking_mode = 1, turn_speed_multiplier = 0.1, torso_turn_speed_multiplier = 0.1, head_turn_speed_multiplier = 0.1, weight = 0.0, safe_zone_angle = 80, head_safe_zone_angle = 80, look_at_mode = 0, is_eye_look_at_enabled = True),
        t.create_look_at_key('2.75', turn_mode = 3, tracking_mode = 1, turn_speed_multiplier = 0.3, head_turn_speed_multiplier = 0.08811, weight = 0.0, safe_zone_angle = 80, head_safe_zone_angle = 80, reset = True, look_at_mode = 0),
        t.create_look_at_key('5.24', target = bg3.SPEAKER_PLAYER, bone = 'Head_M', turn_mode = 3, turn_speed_multiplier = 0.05, head_turn_speed_multiplier = 0.1, weight = 0.15, head_safe_zone_angle = 80, is_eye_look_at_enabled = True, eye_look_at_target_id = bg3.SPEAKER_PLAYER, eye_look_at_bone = 'Head_M'),
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
        t.create_sound_event_key('3.44', sound_event_id = '025fa6be-55ec-43fe-af6a-03b746163d72', sound_object_index = 4),
        t.create_sound_event_key('4.71', sound_event_id = '4f25a58c-a549-43c8-a972-8290e14916fb', sound_object_index = 4),
        t.create_sound_event_key('6.82', sound_event_id = '94b5ef10-e510-4253-83ef-c76d9e4f3487', sound_object_index = 4),
    ), is_snapped_to_end = True)

    t.create_tl_actor_node(bg3.timeline_object.SOUND, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        t.create_sound_event_key('3.28', sound_event_id = '6dbe237a-0c78-4023-a6b7-30349e0505db', sound_object_index = 4),
    ), is_snapped_to_end = True)

    t.create_tl_actor_node(bg3.timeline_object.SOUND, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_sound_event_key('2.59', sound_event_id = '99648c10-b438-4c56-8dcc-5999b5a69e48', sound_object_index = 4),
        t.create_sound_event_key('8.29', sound_event_id = 'f728f472-57d5-45ce-be9e-6e2f927bee0d', sound_object_index = 4),
    ), is_snapped_to_end = True)

    t.create_tl_actor_node(bg3.timeline_object.PHYSICS, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        t.create_value_key(time = '0.0', interpolation_type = 3, value_name = 'InverseKinematics', value = False),
    ), is_snapped_to_end = True)

    t.create_tl_actor_node(bg3.timeline_object.PHYSICS, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_value_key(time = '0.0', interpolation_type = 3, value_name = 'InverseKinematics', value = False),
    ), is_snapped_to_end = True)

    t.create_tl_non_actor_node(bg3.timeline_object.SWITCH_STAGE, '0.0', phase_duration, (
        t.create_value_key(time = '0.0', interpolation_type = 3, value_name = 'SwitchStageEventID', value_type = 'guid', value = 'd4b2d3ac-d576-4bad-b6aa-abadfce41f0e'),
    ), is_snapped_to_end = True)

    camera = '1df3c3cc-13c4-4876-b76f-ad6dd2759185'

    t.create_tl_animation(bg3.SPEAKER_SHADOWHEART, '0.0', '1.25', 'fa2229c2-20ea-48a8-a836-5390dc371188', 'f9263445-b54b-49e6-8218-aa885673254e', fade_in = 0.0, fade_out = 0.0, offset_type = 5, enable_root_motion = True)
    t.create_tl_animation(bg3.SPEAKER_PLAYER, '0.0', '1.25', '95ddb0f2-1171-4744-961b-25a0e8e56c08', 'fc4c399c-4634-4235-952d-51b8f5bae577', fade_in = 0.0, fade_out = 0.0, offset_type = 5, enable_root_motion = True)

    # Shot 1
    t.create_tl_camera_fov(camera, '0.0', phase_duration, (
        t.create_value_key(time = '0.0', interpolation_type = 0, value_name = 'FoV', value_type = 'float', value = '25'),
    ), is_snapped_to_end = True)
    t.create_tl_transform(camera, '0.0', '1.25', (
        (t.create_value_key(time = '0.0', interpolation_type = 3, value_type = 'float', value = '1.4'),),
        (t.create_value_key(time = '0.0', interpolation_type = 3, value_type = 'float', value = '1.6'),),
        (t.create_value_key(time = '0.0', interpolation_type = 3, value_type = 'float', value = '1.3'),),
        (t.create_value_key(time = '0.0', interpolation_type = 3, value_type = 'fvec4', value = bg3.euler_to_quaternion(-135, 0, 0, sequence='yxz')),),
        (),
        (),
    ))
    t.create_tl_shot(camera, '0.0', '1.25')

    t.create_tl_animation(bg3.SPEAKER_SHADOWHEART, '1.25', '2.75', 'fa2229c2-20ea-48a8-a836-5390dc371188', 'f9263445-b54b-49e6-8218-aa885673254e', animation_play_rate = 0.6, animation_play_start_offset = 1.75, fade_in = 0.0, fade_out = 0.0, offset_type = 1, enable_root_motion = True)
    t.create_tl_animation(bg3.SPEAKER_PLAYER, '1.25', '2.75', '95ddb0f2-1171-4744-961b-25a0e8e56c08', 'fc4c399c-4634-4235-952d-51b8f5bae577', animation_play_rate = 0.8, animation_play_start_offset = 1.0, fade_in = 0.0, fade_out = 0.0, offset_type = 1, enable_root_motion = True)

    if body_type == 'bt2':
        t.create_tl_transform(bg3.SPEAKER_PLAYER, '1.25', phase_duration, (
            (t.create_value_key(time = '1.25', interpolation_type = 3, value_type = 'float', value = '0'),),
            (t.create_value_key(time = '1.25', interpolation_type = 3, value_type = 'float', value = '0'),),
            (t.create_value_key(time = '1.25', interpolation_type = 3, value_type = 'float', value = '0.4'),),
            (t.create_value_key(time = '1.25', interpolation_type = 3, value_type = 'fvec4', value = (0, 0, 0, 1)),),
            (),
            (),
        ), is_snapped_to_end = True)

        t.create_tl_transform(bg3.SPEAKER_SHADOWHEART, '1.25', phase_duration, (
            (t.create_value_key(time = '1.25', interpolation_type = 3, value_type = 'float', value = '0'),),
            (t.create_value_key(time = '1.25', interpolation_type = 3, value_type = 'float', value = '0'),),
            (t.create_value_key(time = '1.25', interpolation_type = 3, value_type = 'float', value = '-0.8'),),
            (t.create_value_key(time = '1.25', interpolation_type = 3, value_type = 'fvec4', value = (0, 1, 0, 0)),),
            (),
            (),
        ), is_snapped_to_end = True)
    elif body_type == 'bt2_gith':
        t.create_tl_transform(bg3.SPEAKER_PLAYER, '1.25', phase_duration, (
            (t.create_value_key(time = '1.25', interpolation_type = 3, value_type = 'float', value = '0'),),
            (t.create_value_key(time = '1.25', interpolation_type = 3, value_type = 'float', value = '0'),),
            (t.create_value_key(time = '1.25', interpolation_type = 3, value_type = 'float', value = '0.4'),),
            (t.create_value_key(time = '1.25', interpolation_type = 3, value_type = 'fvec4', value = (0, 0, 0, 1)),),
            (),
            (),
        ), is_snapped_to_end = True)

        t.create_tl_transform(bg3.SPEAKER_SHADOWHEART, '1.25', phase_duration, (
            (t.create_value_key(time = '1.25', interpolation_type = 3, value_type = 'float', value = '0'),),
            (t.create_value_key(time = '1.25', interpolation_type = 3, value_type = 'float', value = '0'),),
            (t.create_value_key(time = '1.25', interpolation_type = 3, value_type = 'float', value = '-0.78'),),
            (t.create_value_key(time = '1.25', interpolation_type = 3, value_type = 'fvec4', value = (0, 1, 0, 0)),),
            (),
            (),
        ), is_snapped_to_end = True)
    else:
        t.create_tl_transform(bg3.SPEAKER_PLAYER, '1.25', phase_duration, (
            (t.create_value_key(time = '1.25', interpolation_type = 3, value_type = 'float', value = '0'),),
            (t.create_value_key(time = '1.25', interpolation_type = 3, value_type = 'float', value = '0'),),
            (t.create_value_key(time = '1.25', interpolation_type = 3, value_type = 'float', value = '0.42'),),
            (t.create_value_key(time = '1.25', interpolation_type = 3, value_type = 'fvec4', value = (0, 0, 0, 1)),),
            (),
            (),
        ), is_snapped_to_end = True)

        t.create_tl_transform(bg3.SPEAKER_SHADOWHEART, '1.25', phase_duration, (
            (t.create_value_key(time = '1.25', interpolation_type = 3, value_type = 'float', value = '0'),),
            (t.create_value_key(time = '1.25', interpolation_type = 3, value_type = 'float', value = '0'),),
            (t.create_value_key(time = '1.25', interpolation_type = 3, value_type = 'float', value = '-0.8'),),
            (t.create_value_key(time = '1.25', interpolation_type = 3, value_type = 'fvec4', value = (0, 1, 0, 0)),),
            (),
            (),
        ), is_snapped_to_end = True)


    # Shot 2
    t.create_tl_transform(camera, '1.25', '2.75', (
        (t.create_value_key(time = '1.25', interpolation_type = 3, value_type = 'float', value = '-0.6'),),
        (t.create_value_key(time = '1.25', interpolation_type = 3, value_type = 'float', value = '1.9'),),
        (t.create_value_key(time = '1.25', interpolation_type = 3, value_type = 'float', value = '0.7'),),
        (t.create_value_key(time = '1.25', interpolation_type = 5, value_type = 'fvec4', value = bg3.euler_to_quaternion(128, 10, 0, sequence='yxz')),),
        (),
        (),
    ))
    t.create_tl_shot(camera, '1.25', '2.75', disable_conditional_staging = True)

    t.create_tl_animation(bg3.SPEAKER_SHADOWHEART, '2.25', '5.0', 'a0e37a8e-c619-4d0a-840a-061831fb0523', 'dde3a70e-60d6-44f0-902b-030ec719f697', animation_slot = 1, animation_play_start_offset = 7.0, fade_in = 1.5, fade_out = 1.0, offset_type = 5)
    t.create_tl_animation(bg3.SPEAKER_PLAYER, '2.25', '5.0', 'c26b9b0a-20cc-44a4-a499-18d6d78abec5', 'bac848e1-c92b-41de-ac13-ad9384dc96aa', animation_slot = 1, animation_play_start_offset = 7.0, fade_in = 1.5, fade_out = 1.0, offset_type = 5)

    t.create_tl_animation(bg3.SPEAKER_SHADOWHEART, '2.75', '6.5', 'fa2229c2-20ea-48a8-a836-5390dc371188', 'f9263445-b54b-49e6-8218-aa885673254e', animation_play_rate = 0.6, animation_play_start_offset = 3.25, fade_in = 0.0, fade_out = 0.0, offset_type = 1, enable_root_motion = True)
    t.create_tl_animation(bg3.SPEAKER_PLAYER, '2.75', '6.5', '95ddb0f2-1171-4744-961b-25a0e8e56c08', 'fc4c399c-4634-4235-952d-51b8f5bae577', animation_play_rate = 0.6, animation_play_start_offset = 3.25, fade_in = 0.0, fade_out = 0.0, offset_type = 1, enable_root_motion = True)

    # Shot 3
    t.create_tl_transform(camera, '2.75', '6.5', (
        (t.create_value_key(time = '2.75', interpolation_type = 3, value_type = 'float', value = '0.8'),),
        (t.create_value_key(time = '2.75', interpolation_type = 3, value_type = 'float', value = '1.75'),),
        (t.create_value_key(time = '2.75', interpolation_type = 3, value_type = 'float', value = '0.7'),),
        (t.create_value_key(time = '2.75', interpolation_type = 3, value_type = 'fvec4', value = bg3.euler_to_quaternion(-128, 0, 0, sequence='yxz')),),
        (),
        (),
    ))
    t.create_tl_shot(camera, '2.75', '6.5', disable_conditional_staging = True)


    t.create_tl_animation(bg3.SPEAKER_SHADOWHEART, '6.5', phase_duration, 'fa2229c2-20ea-48a8-a836-5390dc371188', 'f9263445-b54b-49e6-8218-aa885673254e', animation_play_rate = 0.6, animation_play_start_offset = 6.25, fade_in = 0.0, fade_out = 1.0, offset_type = 1, enable_root_motion = True)
    t.create_tl_animation(bg3.SPEAKER_PLAYER, '6.5', phase_duration, '95ddb0f2-1171-4744-961b-25a0e8e56c08', 'fc4c399c-4634-4235-952d-51b8f5bae577', animation_play_rate = 0.6, animation_play_start_offset = 6.25, fade_in = 0.0, fade_out = 2.0, offset_type = 1, enable_root_motion = True)

    # Shot 4
    t.create_tl_transform(camera, '6.5', phase_duration, (
        (t.create_value_key(time = '6.5', interpolation_type = 3, value_type = 'float', value = '0.8'),),
        (t.create_value_key(time = '6.5', interpolation_type = 3, value_type = 'float', value = '1.8'),),
        (t.create_value_key(time = '6.5', interpolation_type = 5, value_type = 'float', value = '-0.3'),),
        (t.create_value_key(time = '8.5', interpolation_type = 5, value_type = 'fvec4', value = bg3.euler_to_quaternion(-60, 0, 0, sequence='yxz')),),
        (),
        (),
    ), is_snapped_to_end = True)
    t.create_tl_shot(camera, '6.5', phase_duration, disable_conditional_staging = True)

    # Shot 5
    t.create_tl_transform('89eeac49-0759-420d-8f99-3b76a8b2b7e8', '9.45', phase_duration, ((), (), (), (), (), ()), is_snapped_to_end = True)
    t.create_tl_shot('89eeac49-0759-420d-8f99-3b76a8b2b7e8', '9.45', phase_duration, disable_conditional_staging = True, is_snapped_to_end = True)
    

def create_karlach_kiss_C_timeline(t: bg3.timeline_object, dialog_uuid: str, body_type: str) -> None:
    phase_duration = '15.02'

    t.create_new_phase(dialog_uuid, phase_duration)

    t.create_tl_actor_node(bg3.timeline_object.ATTITUDE, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.ATTITUDE, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (), is_snapped_to_end = True)

    t.create_tl_actor_node(bg3.timeline_object.EMOTION, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        t.create_emotion_key(0.0, 2),
        t.create_emotion_key(1.89, 2, variation = 1),
        t.create_emotion_key(8.37, 2),
        t.create_emotion_key(10.7, 2, variation = 2),
    ), is_snapped_to_end = True)

    t.create_tl_actor_node(bg3.timeline_object.EMOTION, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_emotion_key(0.0, 2),
        t.create_emotion_key(0.86, 2, variation = 2),
        t.create_emotion_key(2.9, 2, variation = 1),
        t.create_emotion_key(5.97, 2, variation = 1),
        t.create_emotion_key(7.67, 2),
        t.create_emotion_key(12.8, 2, variation = 2),
    ), is_snapped_to_end = True)

    t.create_tl_actor_node(bg3.timeline_object.LOOK_AT, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        t.create_look_at_key('0.0', target = bg3.SPEAKER_SHADOWHEART, bone = 'Head_M', turn_mode = 3, turn_speed_multiplier = 0.3, head_turn_speed_multiplier = 0.3, weight = 0.0, safe_zone_angle = 80, head_safe_zone_angle = 80, reset = True, look_at_mode = 1, eye_look_at_bone = 'Head_M'),
        t.create_look_at_key('1.49', target = bg3.SPEAKER_SHADOWHEART, bone = 'Dummy_EyeFX_02', turn_mode = 3, turn_speed_multiplier = 0.3, head_turn_speed_multiplier = 0.05, weight = 0.0, safe_zone_angle = 80, head_safe_zone_angle = 80, reset = True, look_at_mode = 1, eye_look_at_bone = 'Head_M'),
        t.create_look_at_key('2.39', target = bg3.SPEAKER_SHADOWHEART, bone = 'Head_M', turn_mode = 3, turn_speed_multiplier = 0.28, head_turn_speed_multiplier = 0.05, weight = 0.0, safe_zone_angle = 80, head_safe_zone_angle = 80, offset = (0, -0.1, 0), reset = True, look_at_mode = 1, eye_look_at_bone = 'Head_M'),
        t.create_look_at_key('3.41', target = bg3.SPEAKER_SHADOWHEART, turn_mode = 3, turn_speed_multiplier = 0.2693, head_turn_speed_multiplier = 0.05, weight = 0.0, safe_zone_angle = 80, head_safe_zone_angle = 80, reset = True, look_at_mode = 0),
        t.create_look_at_key('7.67', target = bg3.SPEAKER_SHADOWHEART, bone = 'Head_M', turn_mode = 3, turn_speed_multiplier = 0.3, head_turn_speed_multiplier = 0.05, weight = 0.0, safe_zone_angle = 80, head_safe_zone_angle = 80, offset = (0, -0.1, 0), reset = True, look_at_mode = 1, eye_look_at_bone = 'Head_M'),
        t.create_look_at_key('10.54', target = bg3.SPEAKER_SHADOWHEART, bone = 'Head_M', turn_mode = 3, turn_speed_multiplier = 0.3, head_turn_speed_multiplier = 0.05, weight = 0.0, safe_zone_angle = 80, head_safe_zone_angle = 80, reset = True, look_at_mode = 1, eye_look_at_bone = 'Head_M'),
    ), is_snapped_to_end = True)

    t.create_tl_actor_node(bg3.timeline_object.LOOK_AT, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_look_at_key('0.0', target = bg3.SPEAKER_PLAYER, bone = 'Head_M', turn_mode = 3, tracking_mode = 1, turn_speed_multiplier = 0.05, head_turn_speed_multiplier = 0.05, weight = 0.5, head_safe_zone_angle = 80, reset = True, is_eye_look_at_enabled = True, eye_look_at_target_id = bg3.SPEAKER_PLAYER, eye_look_at_bone = 'Head_M'),
        t.create_look_at_key('1.49', turn_mode = 3, tracking_mode = 1, turn_speed_multiplier = 0.1, torso_turn_speed_multiplier = 0.1, head_turn_speed_multiplier = 0.1, weight = 0.0, safe_zone_angle = 80, head_safe_zone_angle = 80, look_at_mode = 0, is_eye_look_at_enabled = True),
        t.create_look_at_key('3.22', target = bg3.SPEAKER_PLAYER, bone = 'Head_M', turn_mode = 3, tracking_mode = 1, turn_speed_multiplier = 0.283, torso_turn_speed_multiplier = 0.921, head_turn_speed_multiplier = 0.089, weight = 0.0, safe_zone_angle = 80, head_safe_zone_angle = 80, offset = (0, -0.1, 0), reset = True, look_at_mode = 1, eye_look_at_target_id = bg3.SPEAKER_PLAYER, eye_look_at_bone = 'Head_M'),
        t.create_look_at_key('3.64', turn_mode = 3, tracking_mode = 1, turn_speed_multiplier = 0.3, head_turn_speed_multiplier = 0.08811, weight = 0.0, safe_zone_angle = 80, head_safe_zone_angle = 80, reset = True, look_at_mode = 0),
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
        t.create_sound_event_key('3.99', sound_event_id = '6dbe237a-0c78-4023-a6b7-30349e0505db', sound_object_index = 4),
    ), is_snapped_to_end = True)

    t.create_tl_actor_node(bg3.timeline_object.SOUND, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        t.create_sound_event_key('3.12', sound_event_id = '9be448a7-d60a-44a4-8237-68a27c6fe100', sound_object_index = 4),
    ), is_snapped_to_end = True)

    t.create_tl_actor_node(bg3.timeline_object.SOUND, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_sound_event_key('3.89', sound_event_id = '025fa6be-55ec-43fe-af6a-03b746163d72', sound_object_index = 4),
        t.create_sound_event_key('5.5592', sound_event_id = 'ffbbbd57-5c31-444d-bc3a-c3d14df0be53', sound_object_index = 4),
        t.create_sound_event_key('8.49', sound_event_id = '7a6032cd-36c2-49f2-a369-9da926c7db2f', sound_object_index = 4),
        t.create_sound_event_key('10.4499', sound_event_id = '94b5ef10-e510-4253-83ef-c76d9e4f3487', sound_object_index = 4),
    ), is_snapped_to_end = True)

    t.create_tl_actor_node(bg3.timeline_object.PHYSICS, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        t.create_value_key(time = '0.0', interpolation_type = 3, value_name = 'InverseKinematics', value = False),
    ), is_snapped_to_end = True)

    t.create_tl_actor_node(bg3.timeline_object.PHYSICS, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_value_key(time = '0.0', interpolation_type = 3, value_name = 'InverseKinematics', value = False),
    ), is_snapped_to_end = True)

    t.create_tl_non_actor_node(bg3.timeline_object.SWITCH_STAGE, '0.0', phase_duration, (
        t.create_value_key(time = '0.0', interpolation_type = 3, value_name = 'SwitchStageEventID', value_type = 'guid', value = 'd4b2d3ac-d576-4bad-b6aa-abadfce41f0e'),
    ), is_snapped_to_end = True)

    if body_type == 'bt2':
        t.create_tl_transform(bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
            (t.create_value_key(time = '0.0', interpolation_type = 3, value_type = 'float', value = '0'),),
            (t.create_value_key(time = '0.0', interpolation_type = 3, value_type = 'float', value = '0.045'),),
            (t.create_value_key(time = '0.0', interpolation_type = 3, value_type = 'float', value = '0.4'),),
            (t.create_value_key(time = '0.0', interpolation_type = 3, value_type = 'fvec4', value = (0, 0, 0, 1)),),
            (),
            (),
        ), is_snapped_to_end = True)

        t.create_tl_transform(bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
            (t.create_value_key(time = '0.0', interpolation_type = 3, value_type = 'float', value = '0'),),
            (t.create_value_key(time = '0.0', interpolation_type = 3, value_type = 'float', value = '-0.045'),),
            (t.create_value_key(time = '0.0', interpolation_type = 3, value_type = 'float', value = '-0.8'),),
            (t.create_value_key(time = '0.0', interpolation_type = 3, value_type = 'fvec4', value = (0, 1, 0, 0)),),
            (),
            (),
        ), is_snapped_to_end = True)
    elif body_type == 'bt2_gith':
        t.create_tl_transform(bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
            (t.create_value_key(time = '0.0', interpolation_type = 3, value_type = 'float', value = '0'),),
            (t.create_value_key(time = '0.0', interpolation_type = 3, value_type = 'float', value = '0.05'),),
            (t.create_value_key(time = '0.0', interpolation_type = 3, value_type = 'float', value = '0.42'),),
            (t.create_value_key(time = '0.0', interpolation_type = 3, value_type = 'fvec4', value = (0, 0, 0, 1)),),
            (),
            (),
        ), is_snapped_to_end = True)

        t.create_tl_transform(bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
            (t.create_value_key(time = '0.0', interpolation_type = 3, value_type = 'float', value = '0'),),
            (t.create_value_key(time = '0.0', interpolation_type = 3, value_type = 'float', value = '-0.05'),),
            (t.create_value_key(time = '0.0', interpolation_type = 3, value_type = 'float', value = '-0.8'),),
            (t.create_value_key(time = '0.0', interpolation_type = 3, value_type = 'fvec4', value = (0, 1, 0, 0)),),
            (),
            (),
        ), is_snapped_to_end = True)
    else:
        t.create_tl_transform(bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
            (t.create_value_key(time = '0.0', interpolation_type = 3, value_type = 'float', value = '0'),),
            (t.create_value_key(time = '0.0', interpolation_type = 3, value_type = 'float', value = '0'),),
            (t.create_value_key(time = '0.0', interpolation_type = 3, value_type = 'float', value = '0.42'),),
            (t.create_value_key(time = '0.0', interpolation_type = 3, value_type = 'fvec4', value = (0, 0, 0, 1)),),
            (),
            (),
        ), is_snapped_to_end = True)

        t.create_tl_transform(bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
            (t.create_value_key(time = '0.0', interpolation_type = 3, value_type = 'float', value = '0'),),
            (t.create_value_key(time = '0.0', interpolation_type = 3, value_type = 'float', value = '0'),),
            (t.create_value_key(time = '0.0', interpolation_type = 3, value_type = 'float', value = '-0.8'),),
            (t.create_value_key(time = '0.0', interpolation_type = 3, value_type = 'fvec4', value = (0, 1, 0, 0)),),
            (),
            (),
        ), is_snapped_to_end = True)

    camera = '1df3c3cc-13c4-4876-b76f-ad6dd2759185'
    # camera = '33a18aa0-5996-441f-940b-1179758c5834'

    t.create_tl_animation(bg3.SPEAKER_SHADOWHEART, '0.0', '3.12', '78e23547-b757-423f-9fb9-d0b1d00c14c4', 'f9263445-b54b-49e6-8218-aa885673254e', animation_play_rate = 0.9, fade_in = 0.0, fade_out = 0.0, offset_type = 5)
    t.create_tl_animation(bg3.SPEAKER_PLAYER, '0.0', '3.12', '92fdef9f-552d-3c1e-fcbc-b1c8cdab0e9d', 'fc4c399c-4634-4235-952d-51b8f5bae577', animation_play_rate = 0.9, fade_in = 0.0, fade_out = 0.0, offset_type = 5)

    # Shot 1
    t.create_tl_camera_fov(camera, '0.0', phase_duration, (
        t.create_value_key(time = '0.0', interpolation_type = 0, value_name = 'FoV', value_type = 'float', value = '25'),
    ), is_snapped_to_end = True)
    t.create_tl_transform(camera, '0.0', '1.49', (
        (t.create_value_key(time = '0.0', interpolation_type = 3, value_type = 'float', value = '0.7'),),
        (t.create_value_key(time = '0.0', interpolation_type = 3, value_type = 'float', value = '1.9'),),
        (t.create_value_key(time = '0.0', interpolation_type = 3, value_type = 'float', value = '1.1'),),
        (t.create_value_key(time = '0.0', interpolation_type = 3, value_type = 'fvec4', value = bg3.euler_to_quaternion(-150, 10, 0, sequence='yxz')),),
        (),
        (),
    ))
    t.create_tl_shot(camera, '0.0', '1.49')

    # Shot 2
    t.create_tl_transform(camera, '1.49', '3.12', (
        (t.create_value_key(time = '1.49', interpolation_type = 3, value_type = 'float', value = '1.1'),),
        (t.create_value_key(time = '1.49', interpolation_type = 3, value_type = 'float', value = '1.5'),),
        (t.create_value_key(time = '1.49', interpolation_type = 3, value_type = 'float', value = '-0.4'),),
        (t.create_value_key(time = '1.49', interpolation_type = 3, value_type = 'fvec4', value = bg3.euler_to_quaternion(-58, -12, 0, sequence='yxz')),),
        (),
        (),
    ))
    t.create_tl_shot(camera, '1.49', '3.12', disable_conditional_staging = True)

    # Lips
    # t.create_tl_animation(bg3.SPEAKER_SHADOWHEART, '2.96', '9.5327', 'a0e37a8e-c619-4d0a-840a-061831fb0523', 'dde3a70e-60d6-44f0-902b-030ec719f697', animation_slot = 1, animation_play_rate = 1.1, animation_play_start_offset = 5.5, fade_in = 1.5, fade_out = 1.5, offset_type = 5)
    # t.create_tl_animation(bg3.SPEAKER_PLAYER, '2.3319', '5.51', 'c26b9b0a-20cc-44a4-a499-18d6d78abec5', 'bac848e1-c92b-41de-ac13-ad9384dc96aa', animation_slot = 1, animation_play_start_offset = 5.5, fade_in = 1.5, fade_out = 1.18, offset_type = 5)
    t.create_tl_animation(bg3.SPEAKER_SHADOWHEART, '2.96', '9.5327', 'a0e37a8e-c619-4d0a-840a-061831fb0523', 'dde3a70e-60d6-44f0-902b-030ec719f697', animation_slot = 1, animation_play_rate = 1.1, animation_play_start_offset = 5.5, fade_in = 1.5, fade_out = 1.5, offset_type = 5)
    t.create_tl_animation(bg3.SPEAKER_PLAYER, '3.06', '5.51', 'c26b9b0a-20cc-44a4-a499-18d6d78abec5', 'bac848e1-c92b-41de-ac13-ad9384dc96aa', animation_slot = 1, animation_play_start_offset = 5.5, fade_in = 1.5, fade_out = 1.18, offset_type = 5)

    # Animations
    t.create_tl_animation(bg3.SPEAKER_SHADOWHEART, '3.12', phase_duration, '78e23547-b757-423f-9fb9-d0b1d00c14c4', 'f9263445-b54b-49e6-8218-aa885673254e', animation_play_start_offset = 2.43, fade_in = 0.0, fade_out = 2.0)
    t.create_tl_animation(bg3.SPEAKER_PLAYER, '3.12', phase_duration, '92fdef9f-552d-3c1e-fcbc-b1c8cdab0e9d', 'fc4c399c-4634-4235-952d-51b8f5bae577', animation_play_start_offset = 2.43, fade_in = 0.0, fade_out = 2.0)

    # Shot 3
    if body_type == 'bt2':
        t.create_tl_transform(camera, '3.12', '8.1', (
            (t.create_value_key(time = '3.12', interpolation_type = 3, value_type = 'float', value = '0.5'),),
            (t.create_value_key(time = '3.12', interpolation_type = 3, value_type = 'float', value = '1.9'),),
            (t.create_value_key(time = '3.12', interpolation_type = 3, value_type = 'float', value = '1.0'),),
            (t.create_value_key(time = '3.12', interpolation_type = 3, value_type = 'fvec4', value = bg3.euler_to_quaternion(-160, 12, 0, sequence='yxz')),),
            (),
            (),
        ))
        t.create_tl_shot(camera, '3.12', '8.1', disable_conditional_staging = True)
    elif body_type == 'bt2_gith':
        t.create_tl_transform(camera, '3.12', '9.1', (
            (t.create_value_key(time = '3.12', interpolation_type = 3, value_type = 'float', value = '0.1'),),
            (t.create_value_key(time = '3.12', interpolation_type = 3, value_type = 'float', value = '1.9'),),
            (t.create_value_key(time = '3.12', interpolation_type = 3, value_type = 'float', value = '1.0'),),
            (t.create_value_key(time = '3.12', interpolation_type = 3, value_type = 'fvec4', value = bg3.euler_to_quaternion(180, 12, 0, sequence='yxz')),),
            (),
            (),
        ))
        t.create_tl_shot(camera, '3.12', '9.1', disable_conditional_staging = True)
    else:
        t.create_tl_transform(camera, '3.12', '8.1', (
            (t.create_value_key(time = '3.12', interpolation_type = 3, value_type = 'float', value = '0.5'),),
            (t.create_value_key(time = '3.12', interpolation_type = 3, value_type = 'float', value = '2.0'),),
            (t.create_value_key(time = '3.12', interpolation_type = 3, value_type = 'float', value = '1.0'),),
            (t.create_value_key(time = '3.12', interpolation_type = 3, value_type = 'fvec4', value = bg3.euler_to_quaternion(-160, 11, 0, sequence='yxz')),),
            (),
            (),
        ))
        t.create_tl_shot(camera, '3.12', '8.1', disable_conditional_staging = True)

    # Lips
    #t.create_tl_animation(bg3.SPEAKER_PLAYER, '4.3319', '10.01', 'c26b9b0a-20cc-44a4-a499-18d6d78abec5', 'bac848e1-c92b-41de-ac13-ad9384dc96aa', animation_slot = 1, animation_play_start_offset = 5.17, fade_in = 0.0, fade_out = 1.0, offset_type = 5)
    t.create_tl_animation(bg3.SPEAKER_PLAYER, '4.3319', '9.01', 'c26b9b0a-20cc-44a4-a499-18d6d78abec5', 'bac848e1-c92b-41de-ac13-ad9384dc96aa', animation_slot = 1, animation_play_start_offset = 5.17, fade_in = 0.0, fade_out = 1.0, offset_type = 5)

    # Shot 4
    if body_type == 'bt2_gith':
        t.create_tl_transform(camera, '9.1', '11.9519', (
            (t.create_value_key(time = '9.1', interpolation_type = 3, value_type = 'float', value = '-1.0'),),
            (t.create_value_key(time = '9.1', interpolation_type = 3, value_type = 'float', value = '1.8'),),
            (t.create_value_key(time = '9.1', interpolation_type = 3, value_type = 'float', value = '-0.5'),),
            (t.create_value_key(time = '9.1', interpolation_type = 3, value_type = 'fvec4', value = bg3.euler_to_quaternion(65, 4, 0, sequence='yxz')),),
            (),
            (),
        ))
        t.create_tl_shot(camera, '9.1', '11.9519', disable_conditional_staging = True)
    else:
        t.create_tl_transform(camera, '8.1', '11.9519', (
            (t.create_value_key(time = '8.1', interpolation_type = 3, value_type = 'float', value = '-1.0'),),
            (t.create_value_key(time = '8.1', interpolation_type = 3, value_type = 'float', value = '1.8'),),
            (t.create_value_key(time = '8.1', interpolation_type = 3, value_type = 'float', value = '-0.5'),),
            (t.create_value_key(time = '8.1', interpolation_type = 3, value_type = 'fvec4', value = bg3.euler_to_quaternion(65, 4, 0, sequence='yxz')),),
            (),
            (),
        ))
        t.create_tl_shot(camera, '8.1', '11.9519', disable_conditional_staging = True)

    t.create_tl_transform('89eeac49-0759-420d-8f99-3b76a8b2b7e8', '11.9519', phase_duration, ((), (), (), (), (), ()), is_snapped_to_end = True)
    t.create_tl_shot('89eeac49-0759-420d-8f99-3b76a8b2b7e8', '11.9519', phase_duration, disable_conditional_staging = True, is_snapped_to_end = True)


def create_karlach_kiss_D_timeline(t: bg3.timeline_object, dialog_uuid: str, body_type: str) -> None:
    phase_duration = '33.9'

    t.create_new_phase(dialog_uuid, phase_duration)

    t.create_tl_actor_node(bg3.timeline_object.ATTITUDE, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.ATTITUDE, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (), is_snapped_to_end = True)

    t.create_tl_actor_node(bg3.timeline_object.EMOTION, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        t.create_emotion_key(0.0, 2),
        t.create_emotion_key(3.03, 2, variation = 1),
        t.create_emotion_key(4.43, 2, variation = 2),
        t.create_emotion_key(5.58, 2, variation = 24),
        t.create_emotion_key(8.82, 2, variation = 2),
        t.create_emotion_key(10.15, 256, variation = 24),
        t.create_emotion_key(10.8, 2, variation = 23),
        t.create_emotion_key(11.86, 2, variation = 24),
        t.create_emotion_key(19.61, 2, variation = 2),
        t.create_emotion_key(21.59, 256, variation = 24),
        t.create_emotion_key(23.08, 2, variation = 24),
        t.create_emotion_key(24.28, 2, variation = 23),
        t.create_emotion_key(25.36, 2, variation = 2),
    ), is_snapped_to_end = True)

    t.create_tl_actor_node(bg3.timeline_object.EMOTION, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_emotion_key(0.0, 2),
        t.create_emotion_key(1.78, 2, variation = 1),
        t.create_emotion_key(5.26, 2, variation = 23),
        t.create_emotion_key(7.05, 2, variation = 2),
        t.create_emotion_key(10.93, 2),
        t.create_emotion_key(13.57, 2, variation = 23),
        t.create_emotion_key(14.47, 2, variation = 2),
        t.create_emotion_key(22.32, 256, variation = 24),
        t.create_emotion_key(23.7, 2, variation = 23),
        t.create_emotion_key(26.0, 2, variation = 1),
        t.create_emotion_key(30.01646, 2, variation = 2),
    ), is_snapped_to_end = True)

    t.create_tl_actor_node(bg3.timeline_object.LOOK_AT, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        t.create_look_at_key('0.0', target = bg3.SPEAKER_SHADOWHEART, bone = 'Head_M', turn_mode = 3, turn_speed_multiplier = 0.3, head_turn_speed_multiplier = 0.3, weight = 0.0, safe_zone_angle = 80, head_safe_zone_angle = 80, reset = True, look_at_mode = 1, eye_look_at_bone = 'Head_M'),
        t.create_look_at_key('3.46995', target = bg3.SPEAKER_SHADOWHEART, bone = 'Dummy_EyeFX_02', turn_mode = 3, turn_speed_multiplier = 0.17995219, head_turn_speed_multiplier = 0.05, weight = 0.0, safe_zone_angle = 80, head_safe_zone_angle = 80, look_at_mode = 1, eye_look_at_bone = 'Head_M'),
        t.create_look_at_key('3.99', target = bg3.SPEAKER_SHADOWHEART, bone = 'Dummy_EyeFX_01', turn_mode = 3, turn_speed_multiplier = 0.3, head_turn_speed_multiplier = 0.05, weight = 0.0, safe_zone_angle = 80, head_safe_zone_angle = 80, reset = True, look_at_mode = 1, eye_look_at_bone = 'Head_M'),
        t.create_look_at_key('4.76', target = bg3.SPEAKER_SHADOWHEART, bone = 'Head_M', turn_mode = 3, turn_speed_multiplier = 0.12806559, head_turn_speed_multiplier = 0.05, weight = 0.0, safe_zone_angle = 80, head_safe_zone_angle = 80, offset = (-0.05, -0.2, 0), look_at_mode = 1, eye_look_at_bone = 'Head_M'),
        t.create_look_at_key('9.63', target = bg3.SPEAKER_SHADOWHEART, bone = 'Shoulder_R', turn_mode = 3, turn_speed_multiplier = 0.106890306, head_turn_speed_multiplier = 0.05, weight = 0.0, safe_zone_angle = 80, head_safe_zone_angle = 80, offset = (0.004, 0.015, 0), look_at_mode = 1, eye_look_at_bone = 'Head_M'),
        t.create_look_at_key('10.89', target = bg3.SPEAKER_SHADOWHEART, bone = 'Head_M', turn_mode = 3, turn_speed_multiplier = 0.09905564, head_turn_speed_multiplier = 0.05, weight = 0.0, safe_zone_angle = 80, head_safe_zone_angle = 80, look_at_mode = 1, eye_look_at_bone = 'Head_M'),
        t.create_look_at_key('11.31', target = bg3.SPEAKER_SHADOWHEART, bone = 'Chest_M', turn_mode = 3, turn_speed_multiplier = 0.09745491, head_turn_speed_multiplier = 0.05, weight = 0.0, safe_zone_angle = 80, head_safe_zone_angle = 80, offset = (0.005, 0.021, 0), look_at_mode = 1, eye_look_at_bone = 'Head_M'),
        t.create_look_at_key('12.79', target = bg3.SPEAKER_SHADOWHEART, bone = 'Head_M', turn_mode = 3, turn_speed_multiplier = 0.09103652, head_turn_speed_multiplier = 0.05, weight = 0.0, safe_zone_angle = 80, head_safe_zone_angle = 80, offset = (0.0, -0.001, 0), reset = True, look_at_mode = 1, eye_look_at_bone = 'Head_M'),
        t.create_look_at_key('20.54', target = bg3.SPEAKER_SHADOWHEART, bone = 'Dummy_EyeFX_01', turn_mode = 3, turn_speed_multiplier = 0.053226586, head_turn_speed_multiplier = 0.05, weight = 0.5, safe_zone_angle = 80, head_safe_zone_angle = 80, offset = (0.0, 0.001, 0.0), look_at_mode = 1, eye_look_at_bone = 'Head_M'),
        t.create_look_at_key('23.08', target = bg3.SPEAKER_SHADOWHEART, bone = 'Dummy_EyeFX_02', turn_mode = 3, turn_speed_multiplier = 0.057118252, head_turn_speed_multiplier = 0.05, weight = 0.5, safe_zone_angle = 80, head_safe_zone_angle = 80, offset = (0.0, -0.02, 0.0), look_at_mode = 1, eye_look_at_bone = 'Head_M'),
        t.create_look_at_key('25.19', target = bg3.SPEAKER_SHADOWHEART, bone = 'Head_M', turn_mode = 3, turn_speed_multiplier = 0.068764605, head_turn_speed_multiplier = 0.05, weight = 0.5, safe_zone_angle = 80, head_safe_zone_angle = 80, offset = (0.002, 0.008, 0), reset = True, look_at_mode = 1, eye_look_at_bone = 'Head_M'),
        t.create_look_at_key('26.84', target = bg3.SPEAKER_SHADOWHEART, bone = 'Head_M', turn_mode = 3, turn_speed_multiplier = 0.057118252, head_turn_speed_multiplier = 0.05, weight = 0.5, safe_zone_angle = 80, head_safe_zone_angle = 80, offset = (-0.05, -0.05, 0), look_at_mode = 1, eye_look_at_bone = 'Head_M'),
    ), is_snapped_to_end = True)

    t.create_tl_actor_node(bg3.timeline_object.LOOK_AT, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_look_at_key('0.0', target = bg3.SPEAKER_PLAYER, bone = 'Head_M', turn_mode = 3, tracking_mode = 1, turn_speed_multiplier = 0.05, head_turn_speed_multiplier = 0.05, weight = 0.5, head_safe_zone_angle = 80, reset = True, is_eye_look_at_enabled = True, eye_look_at_target_id = bg3.SPEAKER_PLAYER, eye_look_at_bone = 'Head_M'),
        t.create_look_at_key('3.47', target = bg3.SPEAKER_PLAYER, bone = 'Head_M', turn_mode = 3, tracking_mode = 1, turn_speed_multiplier = 0.1, torso_turn_speed_multiplier = 0.1, head_turn_speed_multiplier = 0.1, weight = 0.0, safe_zone_angle = 80, head_safe_zone_angle = 80, reset = True, look_at_mode = 1, eye_look_at_target_id = bg3.SPEAKER_PLAYER, eye_look_at_bone = 'Head_M'),
        t.create_look_at_key('6.67', target = bg3.SPEAKER_PLAYER, bone = 'Head_M', turn_mode = 3, tracking_mode = 1, turn_speed_multiplier = 0.1, torso_turn_speed_multiplier = 0.1, head_turn_speed_multiplier = 0.1, weight = 0.0, safe_zone_angle = 80, head_safe_zone_angle = 80, offset = (0.0, -0.1, 0.0), reset = True, look_at_mode = 1, eye_look_at_target_id = bg3.SPEAKER_PLAYER, eye_look_at_bone = 'Head_M'),
        t.create_look_at_key('7.49', target = bg3.SPEAKER_PLAYER, bone = 'Head_M', turn_mode = 3, tracking_mode = 1, turn_speed_multiplier = 0.1, torso_turn_speed_multiplier = 0.1, head_turn_speed_multiplier = 0.1, weight = 0.0, safe_zone_angle = 80, head_safe_zone_angle = 80, offset = (0.0, 0.2, 0.0), look_at_mode = 1, eye_look_at_target_id = bg3.SPEAKER_PLAYER, eye_look_at_bone = 'Head_M', eye_look_at_offset = (0.0, 0.2, 0.0)),
        t.create_look_at_key('8.77', target = bg3.SPEAKER_PLAYER, bone = 'Dummy_EyeFX_02', turn_mode = 3, tracking_mode = 1, turn_speed_multiplier = 0.1, torso_turn_speed_multiplier = 0.1, head_turn_speed_multiplier = 0.1, weight = 0.0, safe_zone_angle = 80, head_safe_zone_angle = 80, look_at_mode = 1, eye_look_at_target_id = bg3.SPEAKER_PLAYER, eye_look_at_bone = 'Head_M', eye_look_at_offset = (0.0, 0.2, 0.0)),
        t.create_look_at_key('9.14', target = bg3.SPEAKER_PLAYER, bone = 'Dummy_EyeFX_01', turn_mode = 3, tracking_mode = 1, turn_speed_multiplier = 0.1, torso_turn_speed_multiplier = 0.1, head_turn_speed_multiplier = 0.1, weight = 0.0, safe_zone_angle = 80, head_safe_zone_angle = 80, look_at_mode = 1, eye_look_at_target_id = bg3.SPEAKER_PLAYER, eye_look_at_bone = 'Head_M', eye_look_at_offset = (0.0, 0.2, 0.0)),
        t.create_look_at_key('12.79', target = bg3.SPEAKER_PLAYER, bone = 'Head_M', turn_mode = 3, tracking_mode = 1, turn_speed_multiplier = 0.1, torso_turn_speed_multiplier = 0.1, head_turn_speed_multiplier = 0.1, weight = 0.0, safe_zone_angle = 80, head_safe_zone_angle = 80, reset = True, look_at_mode = 1, eye_look_at_target_id = bg3.SPEAKER_PLAYER, eye_look_at_bone = 'Head_M', eye_look_at_offset = (0.0, 0.2, 0.0)),
        t.create_look_at_key('14.06', target = bg3.SPEAKER_PLAYER, bone = 'Head_M', turn_mode = 3, tracking_mode = 1, turn_speed_multiplier = 0.1, torso_turn_speed_multiplier = 0.1, head_turn_speed_multiplier = 0.1, weight = 0.0, safe_zone_angle = 80, head_safe_zone_angle = 80, offset = (0.1, -0.1, 0.0), reset = True, look_at_mode = 1, eye_look_at_target_id = bg3.SPEAKER_PLAYER, eye_look_at_bone = 'Head_M', eye_look_at_offset = (0.0, 0.2, 0.0)),
        t.create_look_at_key('20.67', target = bg3.SPEAKER_PLAYER, bone = 'Dummy_EyeFX_01', turn_mode = 3, tracking_mode = 1, turn_speed_multiplier = 0.1, torso_turn_speed_multiplier = 0.1, head_turn_speed_multiplier = 0.1, weight = 0.0, safe_zone_angle = 80, head_safe_zone_angle = 80, look_at_mode = 1, eye_look_at_target_id = bg3.SPEAKER_PLAYER, eye_look_at_bone = 'Head_M', eye_look_at_offset = (0.0, 0.2, 0.0)),
        t.create_look_at_key('29.06', target = bg3.SPEAKER_PLAYER, bone = 'Dummy_EyeFX_01', turn_mode = 3, tracking_mode = 1, turn_speed_multiplier = 0.1, torso_turn_speed_multiplier = 0.1, head_turn_speed_multiplier = 0.1, weight = 0.0, safe_zone_angle = 80, head_safe_zone_angle = 80, offset = (0.0, -0.05, 0.0), look_at_mode = 1, eye_look_at_target_id = bg3.SPEAKER_PLAYER, eye_look_at_bone = 'Head_M', eye_look_at_offset = (0.0, 0.2, 0.0)),
        t.create_look_at_key('30.87', target = bg3.SPEAKER_PLAYER, bone = 'Dummy_EyeFX_01', turn_mode = 3, tracking_mode = 1, turn_speed_multiplier = 0.1, torso_turn_speed_multiplier = 0.1, head_turn_speed_multiplier = 0.1, weight = 0.0, safe_zone_angle = 80, head_safe_zone_angle = 80, look_at_mode = 1, eye_look_at_target_id = bg3.SPEAKER_PLAYER, eye_look_at_bone = 'Head_M', eye_look_at_offset = (0.0, 0.2, 0.0)),
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
        t.create_sound_event_key('5.83', sound_event_id = '94b5ef10-e510-4253-83ef-c76d9e4f3487', sound_object_index = 4),
        t.create_sound_event_key('8.48', sound_event_id = '5dac329f-b08a-412d-84bc-86fc1aecae45', sound_object_index = 4),
        t.create_sound_event_key('10.43', sound_event_id = 'c6295e80-586c-4fd9-8777-d754514b6bb6', sound_object_index = 4),
        t.create_sound_event_key('11.94', sound_event_id = '5dac329f-b08a-412d-84bc-86fc1aecae45', sound_object_index = 4),
        t.create_sound_event_key('14.97', sound_event_id = '025fa6be-55ec-43fe-af6a-03b746163d72', sound_object_index = 4),
        t.create_sound_event_key('15.09', sound_event_id = '6dbe237a-0c78-4023-a6b7-30349e0505db', sound_object_index = 4),
        t.create_sound_event_key('15.84', sound_event_id = 'ffbbbd57-5c31-444d-bc3a-c3d14df0be53', sound_object_index = 4),
        t.create_sound_event_key('18.01', sound_event_id = 'c232329e-2d4e-4f0c-a4d4-ea1585fce27c', sound_object_index = 4),
        t.create_sound_event_key('19.94', sound_event_id = 'd0756d07-fd81-4fab-b4af-03d565c7f059', sound_object_index = 4),
        t.create_sound_event_key('21.85', sound_event_id = '94b5ef10-e510-4253-83ef-c76d9e4f3487', sound_object_index = 4),
    ), is_snapped_to_end = True)

    t.create_tl_actor_node(bg3.timeline_object.SOUND, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_sound_event_key('15.32', sound_event_id = 'f728f472-57d5-45ce-be9e-6e2f927bee0d', sound_object_index = 4),
        t.create_sound_event_key('17.01', sound_event_id = 'f728f472-57d5-45ce-be9e-6e2f927bee0d', sound_object_index = 4),
    ), is_snapped_to_end = True)

    t.create_tl_actor_node(bg3.timeline_object.PHYSICS, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        t.create_value_key(time = '0.0', interpolation_type = 3, value_name = 'InverseKinematics', value = False),
    ), is_snapped_to_end = True)

    t.create_tl_actor_node(bg3.timeline_object.PHYSICS, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_value_key(time = '0.0', interpolation_type = 3, value_name = 'InverseKinematics', value = False),
    ), is_snapped_to_end = True)

    t.create_tl_actor_node(bg3.timeline_object.HANDS_IK, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_value_key(time = '3.47', interpolation_type = 3),
        t.create_value_key(time = '30.87', interpolation_type = 3, value_name = 'InverseKinematics', value = False),
    ), is_snapped_to_end = True)

    t.create_tl_non_actor_node(bg3.timeline_object.SWITCH_STAGE, '0.0', phase_duration, (
        t.create_value_key(time = '0.0', interpolation_type = 3, value_name = 'SwitchStageEventID', value_type = 'guid', value = 'd4b2d3ac-d576-4bad-b6aa-abadfce41f0e'),
    ), is_snapped_to_end = True)

    if body_type == 'bt2':
        t.create_tl_transform(bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
            (t.create_value_key(time = '0.0', interpolation_type = 3, value_type = 'float', value = '0'),),
            (t.create_value_key(time = '0.0', interpolation_type = 3, value_type = 'float', value = '0.05'),),
            (t.create_value_key(time = '0.0', interpolation_type = 3, value_type = 'float', value = '0.42'),),
            (t.create_value_key(time = '0.0', interpolation_type = 3, value_type = 'fvec4', value = (0, 0, 0, 1)),),
            (),
            (),
        ), is_snapped_to_end = True)

        t.create_tl_transform(bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
            (t.create_value_key(time = '0.0', interpolation_type = 3, value_type = 'float', value = '0'),),
            (t.create_value_key(time = '0.0', interpolation_type = 3, value_type = 'float', value = '-0.05'),),
            (t.create_value_key(time = '0.0', interpolation_type = 3, value_type = 'float', value = '-0.8'),),
            (t.create_value_key(time = '0.0', interpolation_type = 3, value_type = 'fvec4', value = (0, 1, 0, 0)),),
            (),
            (),
        ), is_snapped_to_end = True)
    elif body_type == 'bt2_gith':
        t.create_tl_transform(bg3.SPEAKER_PLAYER, '0.0', '11.6', (
            (t.create_value_key(time = '0.0', interpolation_type = 3, value_type = 'float', value = '0'),),
            (t.create_value_key(time = '0.0', interpolation_type = 3, value_type = 'float', value = '0.05'),),
            (t.create_value_key(time = '0.0', interpolation_type = 3, value_type = 'float', value = '0.42'),),
            (t.create_value_key(time = '0.0', interpolation_type = 3, value_type = 'fvec4', value = (0, 0, 0, 1)),),
            (),
            (),
        ), is_snapped_to_end = True)

        t.create_tl_transform(bg3.SPEAKER_SHADOWHEART, '0.0', '11.6', (
            (t.create_value_key(time = '0.0', interpolation_type = 3, value_type = 'float', value = '0'),),
            (t.create_value_key(time = '0.0', interpolation_type = 3, value_type = 'float', value = '-0.05'),),
            (t.create_value_key(time = '0.0', interpolation_type = 3, value_type = 'float', value = '-0.8'),),
            (t.create_value_key(time = '0.0', interpolation_type = 3, value_type = 'fvec4', value = (0, 1, 0, 0)),),
            (),
            (),
        ), is_snapped_to_end = True)
    else:
        t.create_tl_transform(bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
            (t.create_value_key(time = '0.0', interpolation_type = 3, value_type = 'float', value = '0'),),
            (t.create_value_key(time = '0.0', interpolation_type = 3, value_type = 'float', value = '0'),),
            (t.create_value_key(time = '0.0', interpolation_type = 3, value_type = 'float', value = '0.42'),),
            (t.create_value_key(time = '0.0', interpolation_type = 3, value_type = 'fvec4', value = (0, 0, 0, 1)),),
            (),
            (),
        ), is_snapped_to_end = True)

        t.create_tl_transform(bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
            (t.create_value_key(time = '0.0', interpolation_type = 3, value_type = 'float', value = '0'),),
            (t.create_value_key(time = '0.0', interpolation_type = 3, value_type = 'float', value = '0'),),
            (t.create_value_key(time = '0.0', interpolation_type = 3, value_type = 'float', value = '-0.8'),),
            (t.create_value_key(time = '0.0', interpolation_type = 3, value_type = 'fvec4', value = (0, 1, 0, 0)),),
            (),
            (),
        ), is_snapped_to_end = True)


    camera = '1df3c3cc-13c4-4876-b76f-ad6dd2759185'

    t.create_tl_camera_fov(camera, '0.0', '6.67', (
        t.create_value_key(time = '0.0', interpolation_type = 0, value_name = 'FoV', value_type = 'float', value = '25'),
    ))

    # Shot 1
    t.create_tl_transform(camera, '0.0', '3.47', (
        (t.create_value_key(time = '0.0', interpolation_type = 3, value_type = 'float', value = '0.9'),),
        (t.create_value_key(time = '0.0', interpolation_type = 3, value_type = 'float', value = '1.95'),),
        (t.create_value_key(time = '0.0', interpolation_type = 3, value_type = 'float', value = '1.1'),),
        (t.create_value_key(time = '0.0', interpolation_type = 3, value_type = 'fvec4', value = bg3.euler_to_quaternion(-145, 11, 0, sequence='yxz')),),
        (),
        (),
    ))
    t.create_tl_shot(camera, '0.0', '3.47')

    # Animations
    # t.create_tl_animation(bg3.SPEAKER_SHADOWHEART, '0.0', '0.0001', '82bc7c36-4db4-4c9b-b883-0f43ca3a94da', 'f9263445-b54b-49e6-8218-aa885673254e', fade_in = 0.0, fade_out = 0.0, is_snapped_to_end = True)
    # t.create_tl_animation(bg3.SPEAKER_PLAYER, '0.0', '0.0001', '91db1490-068c-da56-2230-ccc3940013e7', 'fc4c399c-4634-4235-952d-51b8f5bae577', fade_in = 0.0, fade_out = 0.0, is_snapped_to_end = True)

    t.create_tl_animation(bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, '82bc7c36-4db4-4c9b-b883-0f43ca3a94da', 'f9263445-b54b-49e6-8218-aa885673254e', fade_in = 0.0, fade_out = 2.0, is_snapped_to_end = True)
    t.create_tl_animation(bg3.SPEAKER_PLAYER, '0.0', phase_duration, '91db1490-068c-da56-2230-ccc3940013e7', 'fc4c399c-4634-4235-952d-51b8f5bae577', fade_in = 0.0, fade_out = 2.0, is_snapped_to_end = True)

    if body_type == 'bt2_gith':
        # Shot 2
        # t.create_tl_transform(camera, '3.47', '11.6', (
        #     (t.create_value_key(time = '3.47', interpolation_type = 3, value_type = 'float', value = '1.1'),),
        #     (t.create_value_key(time = '3.47', interpolation_type = 3, value_type = 'float', value = '1.5'),),
        #     (t.create_value_key(time = '3.47', interpolation_type = 3, value_type = 'float', value = '-0.6'),),
        #     (t.create_value_key(time = '3.47', interpolation_type = 3, value_type = 'fvec4', value = bg3.euler_to_quaternion(-64, -12, 0, sequence='yxz')),),
        #     (),
        #     (),
        # ))
        t.create_tl_transform(camera, '3.47', '11.6', (
            (t.create_value_key(time = '3.47', interpolation_type = 3, value_type = 'float', value = '0.7'),),
            (t.create_value_key(time = '3.47', interpolation_type = 3, value_type = 'float', value = '1.6'),),
            (t.create_value_key(time = '3.47', interpolation_type = 3, value_type = 'float', value = '-0.56'),),
            (t.create_value_key(time = '3.47', interpolation_type = 3, value_type = 'fvec4', value = bg3.euler_to_quaternion(-54, -9, 0, sequence='yxz')),),
            (),
            (),
        ))
        t.create_tl_shot(camera, '3.47', '11.6', disable_conditional_staging = True)
    else:
        # Shot 2
        t.create_tl_transform(camera, '3.47', '6.67', (
            (t.create_value_key(time = '3.47', interpolation_type = 3, value_type = 'float', value = '1.1'),),
            (t.create_value_key(time = '3.47', interpolation_type = 3, value_type = 'float', value = '1.5'),),
            (t.create_value_key(time = '3.47', interpolation_type = 3, value_type = 'float', value = '-0.6'),),
            (t.create_value_key(time = '3.47', interpolation_type = 3, value_type = 'fvec4', value = bg3.euler_to_quaternion(-64, -12, 0, sequence='yxz')),),
            (),
            (),
        ))
        t.create_tl_shot(camera, '3.47', '6.67', disable_conditional_staging = True)

        # Shot 3 (only BT2 & BT3, no giths)
        t.create_tl_transform(camera, '6.67', '9.63', (
            (t.create_value_key(time = '6.67', interpolation_type = 3, value_type = 'float', value = '1.1'),),
            (t.create_value_key(time = '6.67', interpolation_type = 3, value_type = 'float', value = '1.7'),),
            (t.create_value_key(time = '6.67', interpolation_type = 3, value_type = 'float', value = '1.1'),),
            (t.create_value_key(time = '8.67', interpolation_type = 3, value_type = 'fvec4', value = bg3.euler_to_quaternion(-135, -2, 0, sequence='yxz')),),
            (),
            (),
        ))
        t.create_tl_camera_fov(camera, '6.67', '9.63', (
            t.create_value_key(time = '6.67', interpolation_type = 0, value_name = 'FoV', value_type = 'float', value = '18'),
        ))
        t.create_tl_shot(camera, '6.67', '9.63', disable_conditional_staging = True)

    # Lips
    t.create_tl_animation(bg3.SPEAKER_SHADOWHEART, '7.41', '9.32', 'a0e37a8e-c619-4d0a-840a-061831fb0523', 'dde3a70e-60d6-44f0-902b-030ec719f697', animation_slot = 1, animation_play_start_offset = 7, fade_in = 1.0, fade_out = 0.7, offset_type = 5)
    t.create_tl_animation(bg3.SPEAKER_SHADOWHEART, '9.63', '11.5', 'a0e37a8e-c619-4d0a-840a-061831fb0523', 'dde3a70e-60d6-44f0-902b-030ec719f697', animation_slot = 1, animation_play_start_offset = 6.72, fade_in = 1.0, fade_out = 0.8, offset_type = 5)

    # Shot 4 (only BT2 & BT3, no giths)
    if body_type == 'bt2':
        t.create_tl_transform(camera, '9.63', '11.6', (
            (t.create_value_key(time = '9.63', interpolation_type = 3, value_type = 'float', value = '0.7'),),
            (t.create_value_key(time = '9.63', interpolation_type = 3, value_type = 'float', value = '1.6'),),
            (t.create_value_key(time = '9.63', interpolation_type = 3, value_type = 'float', value = '-0.56'),),
            (t.create_value_key(time = '9.63', interpolation_type = 3, value_type = 'fvec4', value = bg3.euler_to_quaternion(-54, -9, 0, sequence='yxz')),),
            (),
            (),
        ))
        t.create_tl_camera_fov(camera, '9.63', '11.6', (
            t.create_value_key(time = '9.63', interpolation_type = 0, value_name = 'FoV', value_type = 'float', value = '35'),
        ))
        t.create_tl_shot(camera, '9.63', '11.6', disable_conditional_staging = True)
    elif body_type == 'bt3':
        t.create_tl_transform(camera, '9.63', '12.79', (
            (t.create_value_key(time = '9.63', interpolation_type = 3, value_type = 'float', value = '0.7'),),
            (t.create_value_key(time = '9.63', interpolation_type = 3, value_type = 'float', value = '1.6'),),
            (t.create_value_key(time = '9.63', interpolation_type = 3, value_type = 'float', value = '-0.56'),),
            (t.create_value_key(time = '9.63', interpolation_type = 3, value_type = 'fvec4', value = bg3.euler_to_quaternion(-54, -9, 0, sequence='yxz')),),
            (),
            (),
        ))
        t.create_tl_camera_fov(camera, '9.63', '12.79', (
            t.create_value_key(time = '9.63', interpolation_type = 0, value_name = 'FoV', value_type = 'float', value = '35'),
        ))
        t.create_tl_shot(camera, '9.63', '12.79', disable_conditional_staging = True)

    # Lips
    t.create_tl_animation(bg3.SPEAKER_SHADOWHEART, '11.6', '13.15', 'a0e37a8e-c619-4d0a-840a-061831fb0523', 'dde3a70e-60d6-44f0-902b-030ec719f697', animation_slot = 1, animation_play_start_offset = 6.74, fade_in = 0.8, fade_out = 0.5, offset_type = 5)

    # Shot 5
    if body_type == 'bt2':
        t.create_tl_transform(camera, '11.6', '20.54', (
            (t.create_value_key(time = '11.6', interpolation_type = 3, value_type = 'float', value = '0.5'),),
            (t.create_value_key(time = '11.6', interpolation_type = 3, value_type = 'float', value = '1.9'),),
            (t.create_value_key(time = '11.6', interpolation_type = 3, value_type = 'float', value = '1.2'),),
            (t.create_value_key(time = '11.6', interpolation_type = 3, value_type = 'fvec4', value = bg3.euler_to_quaternion(-158, 6, 0, sequence='yxz')),),
            (),
            (),
        ))
        t.create_tl_camera_fov(camera, '11.6', '20.54', (
            t.create_value_key(time = '11.6', interpolation_type = 0, value_name = 'FoV', value_type = 'float', value = '20'),
        ))
        t.create_tl_shot(camera, '11.6', '20.54', disable_conditional_staging = True)
    elif body_type == 'bt2_gith':
        t.create_tl_transform(bg3.SPEAKER_PLAYER, '11.6', '20.54', (
            (t.create_value_key(time = '11.6', interpolation_type = 3, value_type = 'float', value = '0.02'),),
            (t.create_value_key(time = '11.6', interpolation_type = 3, value_type = 'float', value = '0.04'),),
            (t.create_value_key(time = '11.6', interpolation_type = 3, value_type = 'float', value = '0.41'),),
            (t.create_value_key(time = '11.6', interpolation_type = 3, value_type = 'fvec4', value = (0, 0, 0, 1)),),
            (),
            (),
        ))

        t.create_tl_transform(bg3.SPEAKER_SHADOWHEART, '11.6', '20.54', (
            (t.create_value_key(time = '11.6', interpolation_type = 3, value_type = 'float', value = '0'),),
            (t.create_value_key(time = '11.6', interpolation_type = 3, value_type = 'float', value = '-0.05'),),
            (t.create_value_key(time = '11.6', interpolation_type = 3, value_type = 'float', value = '-0.8'),),
            (t.create_value_key(time = '11.6', interpolation_type = 3, value_type = 'fvec4', value = (0, 1, 0, 0)),),
            (),
            (),
        ))

        # Shot 5.1
        t.create_tl_transform(camera, '11.6', '20.54', (
            (t.create_value_key(time = '11.6', interpolation_type = 3, value_type = 'float', value = '0.1'),),
            (t.create_value_key(time = '11.6', interpolation_type = 3, value_type = 'float', value = '1.9'),),
            (t.create_value_key(time = '11.6', interpolation_type = 3, value_type = 'float', value = '1.2'),),
            (t.create_value_key(time = '11.6', interpolation_type = 3, value_type = 'fvec4', value = bg3.euler_to_quaternion(-178, 6, 0, sequence='yxz')),),
            (),
            (),
        ))
        t.create_tl_camera_fov(camera, '11.6', '20.54', (
            t.create_value_key(time = '11.6', interpolation_type = 0, value_name = 'FoV', value_type = 'float', value = '20'),
        ))
        t.create_tl_shot(camera, '11.6', '20.54', disable_conditional_staging = True)
    else:
        t.create_tl_transform(camera, '12.79', '20.54', (
            (t.create_value_key(time = '12.79', interpolation_type = 3, value_type = 'float', value = '0.5'),),
            (t.create_value_key(time = '12.79', interpolation_type = 3, value_type = 'float', value = '1.9'),),
            (t.create_value_key(time = '12.79', interpolation_type = 3, value_type = 'float', value = '1.2'),),
            (t.create_value_key(time = '12.79', interpolation_type = 3, value_type = 'fvec4', value = bg3.euler_to_quaternion(-158, 6, 0, sequence='yxz')),),
            (),
            (),
        ))
        t.create_tl_camera_fov(camera, '12.79', '20.54', (
            t.create_value_key(time = '12.79', interpolation_type = 0, value_name = 'FoV', value_type = 'float', value = '20'),
        ))
        t.create_tl_shot(camera, '12.79', '20.54', disable_conditional_staging = True)

    # Lips
    t.create_tl_animation(bg3.SPEAKER_SHADOWHEART, '14.47', '20.8', 'a0e37a8e-c619-4d0a-840a-061831fb0523', 'dde3a70e-60d6-44f0-902b-030ec719f697', animation_slot = 1, animation_play_start_offset = 7, fade_in = 1.0, fade_out = 0.7, offset_type = 5)
    t.create_tl_animation(bg3.SPEAKER_PLAYER, '13.96', '20.8', 'c26b9b0a-20cc-44a4-a499-18d6d78abec5', 'bac848e1-c92b-41de-ac13-ad9384dc96aa', animation_slot = 1, animation_play_start_offset = 7, fade_in = 1.5, fade_out = 1.0, offset_type = 5)


    if body_type == 'bt2_gith':
        t.create_tl_transform(bg3.SPEAKER_PLAYER, '20.54', phase_duration, (
            (t.create_value_key(time = '20.54', interpolation_type = 3, value_type = 'float', value = '0'),),
            (t.create_value_key(time = '20.54', interpolation_type = 3, value_type = 'float', value = '0.05'),),
            (t.create_value_key(time = '20.54', interpolation_type = 3, value_type = 'float', value = '0.42'),),
            (t.create_value_key(time = '20.54', interpolation_type = 3, value_type = 'fvec4', value = (0, 0, 0, 1)),),
            (),
            (),
        ), is_snapped_to_end = True)

        t.create_tl_transform(bg3.SPEAKER_SHADOWHEART, '20.54', phase_duration, (
            (t.create_value_key(time = '20.54', interpolation_type = 3, value_type = 'float', value = '0'),),
            (t.create_value_key(time = '20.54', interpolation_type = 3, value_type = 'float', value = '-0.05'),),
            (t.create_value_key(time = '20.54', interpolation_type = 3, value_type = 'float', value = '-0.8'),),
            (t.create_value_key(time = '20.54', interpolation_type = 3, value_type = 'fvec4', value = (0, 1, 0, 0)),),
            (),
            (),
        ), is_snapped_to_end = True)


    # Shot 6
    t.create_tl_transform(camera, '20.54', '27.58', (
        (t.create_value_key(time = '20.54', interpolation_type = 3, value_type = 'float', value = '1.2'),),
        (t.create_value_key(time = '20.54', interpolation_type = 3, value_type = 'float', value = '1.8'),),
        (t.create_value_key(time = '20.54', interpolation_type = 3, value_type = 'float', value = '0.1'),),
        (t.create_value_key(time = '20.54', interpolation_type = 3, value_type = 'fvec4', value = bg3.euler_to_quaternion(-95, 4, 0, sequence='yxz')),),
        (),
        (),
    ))
    t.create_tl_camera_fov(camera, '20.54', '27.58', (
        t.create_value_key(time = '20.54', interpolation_type = 0, value_name = 'FoV', value_type = 'float', value = '24'),
    ))
    t.create_tl_shot(camera, '20.54', '27.58', disable_conditional_staging = True)


    # Shot 7
    t.create_tl_transform(camera, '27.58', phase_duration, (
        (t.create_value_key(time = '27.58', interpolation_type = 3, value_type = 'float', value = '1.0'),),
        (t.create_value_key(time = '27.58', interpolation_type = 3, value_type = 'float', value = '1.8'),),
        (t.create_value_key(time = '27.58', interpolation_type = 3, value_type = 'float', value = '1.35'),),
        (t.create_value_key(time = '27.58', interpolation_type = 3, value_type = 'fvec4', value = bg3.euler_to_quaternion(-145, 4, 0, sequence='yxz')),),
        (),
        (),
    ), is_snapped_to_end = True)
    t.create_tl_camera_fov(camera, '27.58', phase_duration, (
        t.create_value_key(time = '27.58', interpolation_type = 0, value_name = 'FoV', value_type = 'float', value = '20'),
    ), is_snapped_to_end = True)
    t.create_tl_shot(camera, '27.58', '30.87', disable_conditional_staging = True)

    # Shot 8
    # t.create_tl_shot('99480a46-e5ff-4101-ab73-d0ce43403c57', '30.87', phase_duration, disable_conditional_staging = True, is_snapped_to_end = True)
    t.create_tl_transform('18c5bd4f-c066-4c52-8cdb-d8bbe1d8034e', '30.87', phase_duration, ((), (), (), (), (), ()), is_snapped_to_end = True)
    t.create_tl_shot('18c5bd4f-c066-4c52-8cdb-d8bbe1d8034e', '30.87', phase_duration, disable_conditional_staging = True, is_snapped_to_end = True)

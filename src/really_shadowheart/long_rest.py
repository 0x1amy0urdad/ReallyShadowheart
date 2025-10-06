from __future__ import annotations

import bg3moddinglib as bg3

from .assets import ASSETS
from .context import game_assets, files
from .flags import *

def create_act3_sleep_cutscene_cine_node(
    d: bg3.dialog_object,
    t: bg3.timeline_object,
    variant: int,
    sleep_with_shadowheart_cine_node_uuid: str,
    camera: str,
    phase_duration: str,
    scene_offset: tuple[float, float, float],
    tav_offset: tuple[float, float, float],
    shadowheart_offset: tuple[float, float, float],
    fov: float | None = None
) -> None:
    actor_tav = t.get_timeline_actors_uuids()[0]
    actor_shadowheart = t.get_timeline_peanuts_uuids()[0]
    speaker_index_shadowheart = 1

    speakers = d.xml.find('./region[@id="dialog"]/node[@id="dialog"]/children/node[@id="speakerlist"]/children')
    if speakers is None:
        raise RuntimeError(f"Cannot find speakerlist node in {d.filename}")
    shadowheart_speaker_node = bg3.et.fromstring(''.join([
        '<node id="speaker" key="index">',
        f'<attribute id="index" type="FixedString" value="{speaker_index_shadowheart}" />',
        f'<attribute id="list" type="LSString" value="{bg3.SPEAKER_SHADOWHEART}" />',
        f'<attribute id="SpeakerMappingId" type="guid" value="{actor_shadowheart}" />',
        '<attribute id="IsPeanutSpeaker" type="bool" value="True" />',
        '</node>'
    ]))
    speakers.append(shadowheart_speaker_node)

    timeline_speakers = t.xml.find('./region[@id="TimelineContent"]/node[@id="TimelineContent"]/children/node[@id="TimelineSpeakers"]/children')
    if timeline_speakers is None:
        raise RuntimeError(f"Cannot find TimelineSpeakers node in the timeline")
    shadowheart_timeline_speaker_node = bg3.et.fromstring(
        '<node id="Object" key="MapKey">' +
        f'<attribute id="MapKey" type="int32" value="{speaker_index_shadowheart}" />' +
        f'<attribute id="MapValue" type="guid" value="{actor_shadowheart}" />' +
        '</node>')
    timeline_speakers.append(shadowheart_timeline_speaker_node)
    d.create_cinematic_dialog_node(sleep_with_shadowheart_cine_node_uuid, [], end_node = True)
    t.create_new_phase(sleep_with_shadowheart_cine_node_uuid, phase_duration)

    t.create_tl_actor_node(bg3.timeline_object.ATTITUDE, actor_tav, '0.0', phase_duration, (), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.ATTITUDE, actor_shadowheart, '0.0', phase_duration, (), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.EMOTION, actor_tav, '0.0', phase_duration, (
        t.create_emotion_key(0.0, 256),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.EMOTION, actor_shadowheart, '0.0', phase_duration, (
        t.create_emotion_key(0.0, 256),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.LOOK_AT, actor_tav, '0.0', phase_duration, (), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.LOOK_AT, actor_shadowheart, '0.0', phase_duration, (), is_snapped_to_end = True)
    t.create_tl_non_actor_node(bg3.timeline_object.SHOW_PEANUTS, '0.0', phase_duration, (
        t.create_value_key(interpolation_type = 3),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.SHOW_WEAPON, actor_tav, '0.0', phase_duration, (
        t.create_value_key(value_name = 'ShowWeapon', value_type = 'bool', value = False, interpolation_type = 3),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.SHOW_WEAPON, actor_shadowheart, '0.0', phase_duration, (
        t.create_value_key(value_name = 'ShowWeapon', value_type = 'bool', value = False, interpolation_type = 3),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.SOUND, actor_tav, '0.0', phase_duration, (
        t.create_sound_event_key(4.09, sound_event_id = '50ab7087-b822-455f-9a61-6b10b6e6d968', sound_object_index = 4),
        t.create_sound_event_key(4.96, sound_event_id = 'dd918728-814a-461b-be07-2ec39e111324', sound_object_index = 4),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.PHYSICS, actor_tav, '0.0', phase_duration, (
        t.create_value_key(value_name = 'InverseKinematics', value_type = 'bool', value = False, interpolation_type = 3),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.PHYSICS, actor_shadowheart, '0.0', phase_duration, (
        t.create_value_key(value_name = 'InverseKinematics', value_type = 'bool', value = False, interpolation_type = 3),
    ), is_snapped_to_end = True)
    t.create_tl_non_actor_node(bg3.timeline_object.SWITCH_STAGE, '0.0', phase_duration, (
        t.create_value_key(value_name = 'SwitchStageEventID', value_type = 'guid', value = 'daa6afb5-6e1d-4866-9ad8-7669a36baa79', interpolation_type = 3),
    ))

    tav_default_offset = [
        (-0.2, 0.0, 0.0),
        (0.29, 0.037, 0.04)
    ]
    shadowheart_default_offset = [
        (0.25, 0.0, 0.0),
        (-0.15, -0.037, 0.0)
    ]

    t.create_tl_transform(actor_tav, '0.0', phase_duration, (
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = scene_offset[0] + tav_offset[0] + tav_default_offset[variant][0]),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = scene_offset[1] + tav_offset[1] + tav_default_offset[variant][1]),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = scene_offset[2] + tav_offset[2] + tav_default_offset[variant][2]),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = bg3.euler_to_quaternion(0, 0, 0, sequence='yxz')),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 1),
        ),
        ()
    ), is_snapped_to_end = True)
    t.create_tl_transform(actor_shadowheart, '0.0', phase_duration, (
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = scene_offset[0] + shadowheart_offset[0] + shadowheart_default_offset[variant][0]),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = scene_offset[1] + shadowheart_offset[1] + shadowheart_default_offset[variant][1]),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = scene_offset[2] + shadowheart_offset[2] + shadowheart_default_offset[variant][2]),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = bg3.euler_to_quaternion(0, 0, 0, sequence='yxz')),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 1),
        ),
        ()
    ), is_snapped_to_end = True)

    tav_animation_ids = [
        'a9aeb0c2-4ee0-4789-9514-ae50a9c36875',
        'da820672-4add-862b-74d7-af83325da027',
    ]
    tav_animation_groups = [
        '3cace32d-343c-431d-96bb-ca21cf66ba71',
        '541f0320-9792-4cca-92f1-85df96f1851d',
    ]
    shadowheart_animation_ids = [
        'da820672-4add-862b-74d7-af83325da027',
        '01ed9f38-d20e-49c7-ae75-0f528e6e5e93',
    ]
    shadowheart_animation_groups = [
        '541f0320-9792-4cca-92f1-85df96f1851d',
        '9b86ca01-fe10-4fb5-8b1d-37c2fa4b3cf5',
    ]

    t.create_tl_animation(
        actor_tav,
        '0.0', phase_duration,
        tav_animation_ids[variant],
        tav_animation_groups[variant],
        fade_in = 0.0,
        fade_out = 0.0,
        offset_type = 5,
        continuous = True,
        is_snapped_to_end = True)

    t.create_tl_animation(
        actor_shadowheart,
        '0.0', phase_duration,
        shadowheart_animation_ids[variant],
        shadowheart_animation_groups[variant],
        fade_in = 0.0,
        fade_out = 0.0,
        offset_type = 5,
        continuous = True,
        is_snapped_to_end = True)

    t1 = bg3.DECIMAL_ZERO
    t2 = bg3.decimal_from_str(phase_duration) * bg3.DECIMAL_HALF

    t.create_tl_camera_dof(camera, t1, t2, (
        (
            t.create_value_key(time = 0.0, interpolation_type = 2, value = 4.6),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 2, value = 2.5),
            #t.create_value_key(time = 0.0, interpolation_type = 2, value = 3.5),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 2, value = 1),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 2),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 2, value = 1.5),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 2),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 2),
        )
    ), is_snapped_to_end = True)

    if fov is None:
        t.create_tl_camera_fov(camera, '0.0', phase_duration, (t.create_value_key(time = 0.0, interpolation_type = 2),), is_snapped_to_end = True)
    else:
        t.create_tl_camera_fov(camera, '0.0', phase_duration, (
            t.create_value_key(time = 0.0, value = fov, value_name = 'FoV', interpolation_type = 2),
        ), is_snapped_to_end = True)

    t.create_tl_shot(camera, t1, phase_duration, is_snapped_to_end = True)

    
    t.create_tl_transform(camera, t1, t2, (
        (
            t.create_value_key(time = t1, interpolation_type = 5, value = scene_offset[0] - 0.3),
            t.create_value_key(time = t2, interpolation_type = 5, value = scene_offset[0] - 0.4),
        ),
        (
            t.create_value_key(time = t1, interpolation_type = 5, value = scene_offset[1] + 1.5),
        ),
        (
            t.create_value_key(time = t1, interpolation_type = 5, value = scene_offset[2] - 1.175),
            t.create_value_key(time = t2, interpolation_type = 5, value = scene_offset[2] - 0.975),
        ),
        (
            t.create_value_key(time = t1, interpolation_type = 5, value = bg3.euler_to_quaternion(12.5, 42.5, 0.0, sequence='yxz')),
            t.create_value_key(time = t2, interpolation_type = 5, value = bg3.euler_to_quaternion(15.0, 45.0, 0.0, sequence='yxz')),
        ),
        (
            t.create_value_key(time = t1, interpolation_type = 5, value = 1),
        ),
        ()
    ))
    t.create_tl_camera_dof(camera, t2, phase_duration, (
        (
            t.create_value_key(time = t2, interpolation_type = 2, value = 4.6),
        ),
        (
            t.create_value_key(time = t2, interpolation_type = 2, value = 5.0),
        ),
        (
            t.create_value_key(time = t2, interpolation_type = 2, value = 1),
        ),
        (
            t.create_value_key(time = t2, interpolation_type = 2),
        ),
        (
            t.create_value_key(time = t2, interpolation_type = 2, value = 1.5),
        ),
        (
            t.create_value_key(time = t2, interpolation_type = 2),
        ),
        (
            t.create_value_key(time = t2, interpolation_type = 2),
        )
    ), is_snapped_to_end = True)
    t.create_tl_transform(camera, t2, phase_duration, (
        (
            t.create_value_key(time = t2, interpolation_type = 5, value = scene_offset[0] - 0.3),
        ),
        (
            t.create_value_key(time = t2, interpolation_type = 5, value = scene_offset[1] + 1.2),
        ),
        (
            t.create_value_key(time = t2, interpolation_type = 5, value = scene_offset[2] + 0.125),
        ),
        (
            t.create_value_key(time = t2, interpolation_type = 5, value = bg3.euler_to_quaternion(45.0, 60.0, 0.0, sequence='yxz')),
        ),
        (
            t.create_value_key(time = t2, interpolation_type = 5, value = 1),
        ),
        ()
    ), is_snapped_to_end = True)


def patch_act3_camp(
    asset_name: str,
    entry_point_node_uuid: str,
    camera_uuid: str,
    scene_offset: tuple[float, float, float]
) -> None:
    # d = bg3.dialog_object(files.get_file('Gustav', f'Mods/GustavDev/Story/DialogsBinary/Camp/{file_name}.lsf'))
    # t = bg3.timeline_object(files.get_file('Gustav', f'Public/GustavDev/Timeline/Generated/{file_name}.lsf'), d)

    ab = game_assets.get_modded_dialog_asset_bundle(asset_name)
    d = bg3.dialog_object(ab.dialog)
    t = bg3.timeline_object(ab.timeline, d)

    sleep_with_shadowheart_bt1_node_uuid = bg3.new_random_uuid()
    cine_bt1_node_uuid = bg3.new_random_uuid()
    sleep_with_shadowheart_bt2_node_uuid = bg3.new_random_uuid()
    cine_bt2_node_uuid = bg3.new_random_uuid()
    sleep_with_shadowheart_bt3_node_uuid = bg3.new_random_uuid()
    cine_bt3_node_uuid = bg3.new_random_uuid()
    sleep_with_shadowheart_bt4_node_uuid = bg3.new_random_uuid()
    cine_bt4_node_uuid = bg3.new_random_uuid()
    sleep_with_shadowheart_halforc_bt1_node_uuid = bg3.new_random_uuid()
    cine_halforc_bt1_node_uuid = bg3.new_random_uuid()
    sleep_with_shadowheart_dwarf_bt2_node_uuid = bg3.new_random_uuid()
    cine_dwarf_bt2_node_uuid = bg3.new_random_uuid()
    sleep_with_shadowheart_dwarf_bt1_node_uuid = bg3.new_random_uuid()
    cine_dwarf_bt1_node_uuid = bg3.new_random_uuid()
    sleep_with_shadowheart_short_bt2_node_uuid = bg3.new_random_uuid()
    cine_short_bt2_node_uuid = bg3.new_random_uuid()
    sleep_with_shadowheart_short_bt1_node_uuid = bg3.new_random_uuid()
    cine_short_bt1_node_uuid = bg3.new_random_uuid()

    sleep_with_shadowheart_bt1_alt_node_uuid = bg3.new_random_uuid()
    cine_bt1_alt_node_uuid = bg3.new_random_uuid()
    sleep_with_shadowheart_bt2_alt_node_uuid = bg3.new_random_uuid()
    cine_bt2_alt_node_uuid = bg3.new_random_uuid()
    sleep_with_shadowheart_bt3_alt_node_uuid = bg3.new_random_uuid()
    cine_bt3_alt_node_uuid = bg3.new_random_uuid()
    sleep_with_shadowheart_bt4_alt_node_uuid = bg3.new_random_uuid()
    cine_bt4_alt_node_uuid = bg3.new_random_uuid()
    sleep_with_shadowheart_halforc_bt1_alt_node_uuid = bg3.new_random_uuid()
    cine_halforc_bt1_alt_node_uuid = bg3.new_random_uuid()
    sleep_with_shadowheart_dwarf_bt2_alt_node_uuid = bg3.new_random_uuid()
    cine_dwarf_bt2_alt_node_uuid = bg3.new_random_uuid()
    sleep_with_shadowheart_dwarf_bt1_alt_node_uuid = bg3.new_random_uuid()
    cine_dwarf_bt1_alt_node_uuid = bg3.new_random_uuid()
    sleep_with_shadowheart_short_bt2_alt_node_uuid = bg3.new_random_uuid()
    cine_short_bt2_alt_node_uuid = bg3.new_random_uuid()
    sleep_with_shadowheart_short_bt1_alt_node_uuid = bg3.new_random_uuid()
    cine_short_bt1_alt_node_uuid = bg3.new_random_uuid()

    speaker_index_tav = 0
    speaker_index_shadowheart = 1

    d.create_standard_dialog_node(
        sleep_with_shadowheart_bt2_node_uuid,
        bg3.SPEAKER_PLAYER,
        [cine_bt2_node_uuid],
        None,
        constructor = bg3.dialog_object.ANSWER,
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_State_PartneredWithShadowheart, True, speaker_index_tav),
            )),
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_AVATAR, True, speaker_index_tav),
                bg3.flag(bg3.TAG_REALLY_SHADOWHEART, True, speaker_index_shadowheart),
            ))
        ),
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(Shadowheart_Tav_Slept_Together.uuid, True, speaker_index_tav),
            )),
        ))
    d.add_child_dialog_node(entry_point_node_uuid, sleep_with_shadowheart_bt2_node_uuid, 0)

    d.create_standard_dialog_node(
        sleep_with_shadowheart_bt1_node_uuid,
        bg3.SPEAKER_PLAYER,
        [cine_bt1_node_uuid],
        None,
        constructor = bg3.dialog_object.ANSWER,
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_State_PartneredWithShadowheart, True, speaker_index_tav),
            )),
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_AVATAR, True, speaker_index_tav),
                bg3.flag(bg3.TAG_FEMALE, True, speaker_index_tav),
                bg3.flag(bg3.TAG_REALLY_SHADOWHEART, True, speaker_index_shadowheart),
            ))
        ),
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(Shadowheart_Tav_Slept_Together.uuid, True, speaker_index_tav),
            )),
        ))
    d.add_child_dialog_node(entry_point_node_uuid, sleep_with_shadowheart_bt1_node_uuid, 0)

    d.create_standard_dialog_node(
        sleep_with_shadowheart_bt4_node_uuid,
        bg3.SPEAKER_PLAYER,
        [cine_bt4_node_uuid],
        None,
        constructor = bg3.dialog_object.ANSWER,
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_State_PartneredWithShadowheart, True, speaker_index_tav),
            )),
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_AVATAR, True, speaker_index_tav),
                bg3.flag(bg3.TAG_BODYTYPE_STRONG, True, speaker_index_tav),
                bg3.flag(bg3.TAG_REALLY_SHADOWHEART, True, speaker_index_shadowheart),
            ))
        ),
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(Shadowheart_Tav_Slept_Together.uuid, True, speaker_index_tav),
            )),
        ))
    d.add_child_dialog_node(entry_point_node_uuid, sleep_with_shadowheart_bt4_node_uuid, 0)

    d.create_standard_dialog_node(
        sleep_with_shadowheart_bt3_node_uuid,
        bg3.SPEAKER_PLAYER,
        [cine_bt3_node_uuid],
        None,
        constructor = bg3.dialog_object.ANSWER,
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_State_PartneredWithShadowheart, True, speaker_index_tav),
            )),
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_AVATAR, True, speaker_index_tav),
                bg3.flag(bg3.TAG_FEMALE, True, speaker_index_tav),
                bg3.flag(bg3.TAG_BODYTYPE_STRONG, True, speaker_index_tav),
                bg3.flag(bg3.TAG_REALLY_SHADOWHEART, True, speaker_index_shadowheart),
            ))
        ),
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(Shadowheart_Tav_Slept_Together.uuid, True, speaker_index_tav),
            )),
        ))
    d.add_child_dialog_node(entry_point_node_uuid, sleep_with_shadowheart_bt3_node_uuid, 0)

    d.create_standard_dialog_node(
        sleep_with_shadowheart_halforc_bt1_node_uuid,
        bg3.SPEAKER_PLAYER,
        [cine_halforc_bt1_node_uuid],
        None,
        constructor = bg3.dialog_object.ANSWER,
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_State_PartneredWithShadowheart, True, speaker_index_tav),
            )),
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_AVATAR, True, speaker_index_tav),
                bg3.flag(bg3.TAG_FEMALE, True, speaker_index_tav),
                bg3.flag(bg3.TAG_HALFORC, True, speaker_index_tav),
                bg3.flag(bg3.TAG_REALLY_SHADOWHEART, True, speaker_index_shadowheart),
            ))
        ),
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(Shadowheart_Tav_Slept_Together.uuid, True, speaker_index_tav),
            )),
        ))
    d.add_child_dialog_node(entry_point_node_uuid, sleep_with_shadowheart_halforc_bt1_node_uuid, 0)

    d.create_standard_dialog_node(
        sleep_with_shadowheart_short_bt2_node_uuid,
        bg3.SPEAKER_PLAYER,
        [cine_short_bt2_node_uuid],
        None,
        constructor = bg3.dialog_object.ANSWER,
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_State_PartneredWithShadowheart, True, speaker_index_tav),
            )),
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_AVATAR, True, speaker_index_tav),
                bg3.flag(bg3.TAG_SHORT, True, speaker_index_tav),
                bg3.flag(bg3.TAG_REALLY_SHADOWHEART, True, speaker_index_shadowheart),
            ))
        ),
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(Shadowheart_Tav_Slept_Together.uuid, True, speaker_index_tav),
            )),
        ))
    d.add_child_dialog_node(entry_point_node_uuid, sleep_with_shadowheart_short_bt2_node_uuid, 0)

    d.create_standard_dialog_node(
        sleep_with_shadowheart_short_bt1_node_uuid,
        bg3.SPEAKER_PLAYER,
        [cine_short_bt1_node_uuid],
        None,
        constructor = bg3.dialog_object.ANSWER,
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_State_PartneredWithShadowheart, True, speaker_index_tav),
            )),
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_AVATAR, True, speaker_index_tav),
                bg3.flag(bg3.TAG_FEMALE, True, speaker_index_tav),
                bg3.flag(bg3.TAG_SHORT, True, speaker_index_tav),
                bg3.flag(bg3.TAG_REALLY_SHADOWHEART, True, speaker_index_shadowheart),
            ))
        ),
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(Shadowheart_Tav_Slept_Together.uuid, True, speaker_index_tav),
            )),
        ))
    d.add_child_dialog_node(entry_point_node_uuid, sleep_with_shadowheart_short_bt1_node_uuid, 0)

    d.create_standard_dialog_node(
        sleep_with_shadowheart_dwarf_bt2_node_uuid,
        bg3.SPEAKER_PLAYER,
        [cine_dwarf_bt2_node_uuid],
        None,
        constructor = bg3.dialog_object.ANSWER,
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_State_PartneredWithShadowheart, True, speaker_index_tav),
            )),
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_AVATAR, True, speaker_index_tav),
                bg3.flag(bg3.TAG_DWARF, True, speaker_index_tav),
                bg3.flag(bg3.TAG_SHORT, True, speaker_index_tav),
                bg3.flag(bg3.TAG_REALLY_SHADOWHEART, True, speaker_index_shadowheart),
            ))
        ),
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(Shadowheart_Tav_Slept_Together.uuid, True, speaker_index_tav),
            )),
        ))
    d.add_child_dialog_node(entry_point_node_uuid, sleep_with_shadowheart_dwarf_bt2_node_uuid, 0)

    d.create_standard_dialog_node(
        sleep_with_shadowheart_dwarf_bt1_node_uuid,
        bg3.SPEAKER_PLAYER,
        [cine_dwarf_bt1_node_uuid],
        None,
        constructor = bg3.dialog_object.ANSWER,
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_State_PartneredWithShadowheart, True, speaker_index_tav),
            )),
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_AVATAR, True, speaker_index_tav),
                bg3.flag(bg3.TAG_FEMALE, True, speaker_index_tav),
                bg3.flag(bg3.TAG_DWARF, True, speaker_index_tav),
                bg3.flag(bg3.TAG_SHORT, True, speaker_index_tav),
                bg3.flag(bg3.TAG_REALLY_SHADOWHEART, True, speaker_index_shadowheart),
            ))
        ),
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(Shadowheart_Tav_Slept_Together.uuid, True, speaker_index_tav),
            )),
        ))
    d.add_child_dialog_node(entry_point_node_uuid, sleep_with_shadowheart_dwarf_bt1_node_uuid, 0)


    d.create_standard_dialog_node(
        sleep_with_shadowheart_bt2_alt_node_uuid,
        bg3.SPEAKER_PLAYER,
        [cine_bt2_alt_node_uuid],
        None,
        constructor = bg3.dialog_object.ANSWER,
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_State_PartneredWithShadowheart, True, speaker_index_tav),
                bg3.flag(Alternative_Night_Sleep_Scene.uuid, True, speaker_index_tav),
            )),
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_AVATAR, True, speaker_index_tav),
                bg3.flag(bg3.TAG_REALLY_SHADOWHEART, True, speaker_index_shadowheart),
            ))
        ),
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(Shadowheart_Tav_Slept_Together.uuid, True, speaker_index_tav),
            )),
        ))
    d.add_child_dialog_node(entry_point_node_uuid, sleep_with_shadowheart_bt2_alt_node_uuid, 0)

    d.create_standard_dialog_node(
        sleep_with_shadowheart_bt1_alt_node_uuid,
        bg3.SPEAKER_PLAYER,
        [cine_bt1_alt_node_uuid],
        None,
        constructor = bg3.dialog_object.ANSWER,
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_State_PartneredWithShadowheart, True, speaker_index_tav),
                bg3.flag(Alternative_Night_Sleep_Scene.uuid, True, speaker_index_tav),
            )),
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_AVATAR, True, speaker_index_tav),
                bg3.flag(bg3.TAG_FEMALE, True, speaker_index_tav),
                bg3.flag(bg3.TAG_REALLY_SHADOWHEART, True, speaker_index_shadowheart),
            ))
        ),
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(Shadowheart_Tav_Slept_Together.uuid, True, speaker_index_tav),
            )),
        ))
    d.add_child_dialog_node(entry_point_node_uuid, sleep_with_shadowheart_bt1_alt_node_uuid, 0)

    d.create_standard_dialog_node(
        sleep_with_shadowheart_bt4_alt_node_uuid,
        bg3.SPEAKER_PLAYER,
        [cine_bt4_alt_node_uuid],
        None,
        constructor = bg3.dialog_object.ANSWER,
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_State_PartneredWithShadowheart, True, speaker_index_tav),
                bg3.flag(Alternative_Night_Sleep_Scene.uuid, True, speaker_index_tav),
            )),
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_AVATAR, True, speaker_index_tav),
                bg3.flag(bg3.TAG_BODYTYPE_STRONG, True, speaker_index_tav),
                bg3.flag(bg3.TAG_REALLY_SHADOWHEART, True, speaker_index_shadowheart),
            ))
        ),
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(Shadowheart_Tav_Slept_Together.uuid, True, speaker_index_tav),
            )),
        ))
    d.add_child_dialog_node(entry_point_node_uuid, sleep_with_shadowheart_bt4_alt_node_uuid, 0)

    d.create_standard_dialog_node(
        sleep_with_shadowheart_bt3_alt_node_uuid,
        bg3.SPEAKER_PLAYER,
        [cine_bt3_alt_node_uuid],
        None,
        constructor = bg3.dialog_object.ANSWER,
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_State_PartneredWithShadowheart, True, speaker_index_tav),
                bg3.flag(Alternative_Night_Sleep_Scene.uuid, True, speaker_index_tav),
            )),
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_AVATAR, True, speaker_index_tav),
                bg3.flag(bg3.TAG_FEMALE, True, speaker_index_tav),
                bg3.flag(bg3.TAG_BODYTYPE_STRONG, True, speaker_index_tav),
                bg3.flag(bg3.TAG_REALLY_SHADOWHEART, True, speaker_index_shadowheart),
            ))
        ),
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(Shadowheart_Tav_Slept_Together.uuid, True, speaker_index_tav),
            )),
        ))
    d.add_child_dialog_node(entry_point_node_uuid, sleep_with_shadowheart_bt3_alt_node_uuid, 0)

    d.create_standard_dialog_node(
        sleep_with_shadowheart_halforc_bt1_alt_node_uuid,
        bg3.SPEAKER_PLAYER,
        [cine_halforc_bt1_alt_node_uuid],
        None,
        constructor = bg3.dialog_object.ANSWER,
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_State_PartneredWithShadowheart, True, speaker_index_tav),
                bg3.flag(Alternative_Night_Sleep_Scene.uuid, True, speaker_index_tav),
            )),
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_AVATAR, True, speaker_index_tav),
                bg3.flag(bg3.TAG_FEMALE, True, speaker_index_tav),
                bg3.flag(bg3.TAG_HALFORC, True, speaker_index_tav),
                bg3.flag(bg3.TAG_REALLY_SHADOWHEART, True, speaker_index_shadowheart),
            ))
        ),
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(Shadowheart_Tav_Slept_Together.uuid, True, speaker_index_tav),
            )),
        ))
    d.add_child_dialog_node(entry_point_node_uuid, sleep_with_shadowheart_halforc_bt1_alt_node_uuid, 0)

    d.create_standard_dialog_node(
        sleep_with_shadowheart_short_bt2_alt_node_uuid,
        bg3.SPEAKER_PLAYER,
        [cine_short_bt2_alt_node_uuid],
        None,
        constructor = bg3.dialog_object.ANSWER,
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_State_PartneredWithShadowheart, True, speaker_index_tav),
                bg3.flag(Alternative_Night_Sleep_Scene.uuid, True, speaker_index_tav),
            )),
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_AVATAR, True, speaker_index_tav),
                bg3.flag(bg3.TAG_SHORT, True, speaker_index_tav),
                bg3.flag(bg3.TAG_REALLY_SHADOWHEART, True, speaker_index_shadowheart),
            ))
        ),
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(Shadowheart_Tav_Slept_Together.uuid, True, speaker_index_tav),
            )),
        ))
    d.add_child_dialog_node(entry_point_node_uuid, sleep_with_shadowheart_short_bt2_alt_node_uuid, 0)

    d.create_standard_dialog_node(
        sleep_with_shadowheart_short_bt1_alt_node_uuid,
        bg3.SPEAKER_PLAYER,
        [cine_short_bt1_alt_node_uuid],
        None,
        constructor = bg3.dialog_object.ANSWER,
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_State_PartneredWithShadowheart, True, speaker_index_tav),
                bg3.flag(Alternative_Night_Sleep_Scene.uuid, True, speaker_index_tav),
            )),
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_AVATAR, True, speaker_index_tav),
                bg3.flag(bg3.TAG_FEMALE, True, speaker_index_tav),
                bg3.flag(bg3.TAG_SHORT, True, speaker_index_tav),
                bg3.flag(bg3.TAG_REALLY_SHADOWHEART, True, speaker_index_shadowheart),
            ))
        ),
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(Shadowheart_Tav_Slept_Together.uuid, True, speaker_index_tav),
            )),
        ))
    d.add_child_dialog_node(entry_point_node_uuid, sleep_with_shadowheart_short_bt1_alt_node_uuid, 0)

    d.create_standard_dialog_node(
        sleep_with_shadowheart_dwarf_bt2_alt_node_uuid,
        bg3.SPEAKER_PLAYER,
        [cine_dwarf_bt2_alt_node_uuid],
        None,
        constructor = bg3.dialog_object.ANSWER,
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_State_PartneredWithShadowheart, True, speaker_index_tav),
                bg3.flag(Alternative_Night_Sleep_Scene.uuid, True, speaker_index_tav),
            )),
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_AVATAR, True, speaker_index_tav),
                bg3.flag(bg3.TAG_DWARF, True, speaker_index_tav),
                bg3.flag(bg3.TAG_SHORT, True, speaker_index_tav),
                bg3.flag(bg3.TAG_REALLY_SHADOWHEART, True, speaker_index_shadowheart),
            ))
        ),
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(Shadowheart_Tav_Slept_Together.uuid, True, speaker_index_tav),
            )),
        ))
    d.add_child_dialog_node(entry_point_node_uuid, sleep_with_shadowheart_dwarf_bt2_alt_node_uuid, 0)

    d.create_standard_dialog_node(
        sleep_with_shadowheart_dwarf_bt1_alt_node_uuid,
        bg3.SPEAKER_PLAYER,
        [cine_dwarf_bt1_alt_node_uuid],
        None,
        constructor = bg3.dialog_object.ANSWER,
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_State_PartneredWithShadowheart, True, speaker_index_tav),
                bg3.flag(Alternative_Night_Sleep_Scene.uuid, True, speaker_index_tav),
            )),
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_AVATAR, True, speaker_index_tav),
                bg3.flag(bg3.TAG_FEMALE, True, speaker_index_tav),
                bg3.flag(bg3.TAG_DWARF, True, speaker_index_tav),
                bg3.flag(bg3.TAG_SHORT, True, speaker_index_tav),
                bg3.flag(bg3.TAG_REALLY_SHADOWHEART, True, speaker_index_shadowheart),
            ))
        ),
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(Shadowheart_Tav_Slept_Together.uuid, True, speaker_index_tav),
            )),
        ))
    d.add_child_dialog_node(entry_point_node_uuid, sleep_with_shadowheart_dwarf_bt1_alt_node_uuid, 0)


    phase_duration = '20.0'
    create_act3_sleep_cutscene_cine_node(d, t, 0, cine_bt1_node_uuid, camera_uuid, phase_duration, scene_offset, (0.0, 0.009, 0.0), (0.0, -0.009, 0.0), 40.0)
    create_act3_sleep_cutscene_cine_node(d, t, 0, cine_bt2_node_uuid, camera_uuid, phase_duration, scene_offset, (0.0, 0.01, 0.0), (0.0, -0.01, 0.0), 40.0)
    create_act3_sleep_cutscene_cine_node(d, t, 0, cine_bt3_node_uuid, camera_uuid, phase_duration, scene_offset, (0.0, -0.015, 0.0), (0.0, 0.0, 0.0), 40.0)
    create_act3_sleep_cutscene_cine_node(d, t, 0, cine_bt4_node_uuid, camera_uuid, phase_duration, scene_offset, (0.0, 0.01, 0.0), (0.0, 0.0, 0.0), 40.0)
    create_act3_sleep_cutscene_cine_node(d, t, 0, cine_halforc_bt1_node_uuid, camera_uuid, phase_duration, scene_offset, (0.0, -0.025, 0.0), (0.0, 0.0, 0.0), 40.0)
    create_act3_sleep_cutscene_cine_node(d, t, 0, cine_dwarf_bt1_node_uuid, camera_uuid, phase_duration, scene_offset, (0.0, 0.0, 0.0), (0.0, 0.0, 0.0), 40.0)
    create_act3_sleep_cutscene_cine_node(d, t, 0, cine_dwarf_bt2_node_uuid, camera_uuid, phase_duration, scene_offset, (0.0, -0.01, 0.0), (0.0, 0.0, 0.0), 40.0)
    create_act3_sleep_cutscene_cine_node(d, t, 0, cine_short_bt1_node_uuid, camera_uuid, phase_duration, scene_offset, (0.0, 0.009, 0.0), (0.0, -0.009, 0.0), 40.0)
    create_act3_sleep_cutscene_cine_node(d, t, 0, cine_short_bt2_node_uuid, camera_uuid, phase_duration, scene_offset, (0.0, 0.01, 0.0), (0.0, -0.01, 0.0), 40.0)

    create_act3_sleep_cutscene_cine_node(d, t, 1, cine_bt1_alt_node_uuid, camera_uuid, phase_duration, scene_offset, (-0.033, -0.018, 0.0), (0.033, 0.018, 0.0), 40.0)
    create_act3_sleep_cutscene_cine_node(d, t, 1, cine_bt2_alt_node_uuid, camera_uuid, phase_duration, scene_offset, (0.0, 0.01, 0.0), (0.0, 0.0, 0.0), 40.0)
    create_act3_sleep_cutscene_cine_node(d, t, 1, cine_bt3_alt_node_uuid, camera_uuid, phase_duration, scene_offset, (0.01, -0.005, 0.0), (-0.01, 0.005, 0.0), 40.0)
    create_act3_sleep_cutscene_cine_node(d, t, 1, cine_bt4_alt_node_uuid, camera_uuid, phase_duration, scene_offset, (0.037, -0.06, -0.2), (-0.02, 0.01, 0.0), 40.0)
    create_act3_sleep_cutscene_cine_node(d, t, 1, cine_halforc_bt1_alt_node_uuid, camera_uuid, phase_duration, scene_offset, (0.02, 0.005, -0.03), (-0.02, 0.0, 0.0), 40.0)
    create_act3_sleep_cutscene_cine_node(d, t, 1, cine_dwarf_bt1_alt_node_uuid, camera_uuid, phase_duration, scene_offset, (-0.03, -0.02, 0.02), (0.03, 0.02, 0.0), 40.0)
    create_act3_sleep_cutscene_cine_node(d, t, 1, cine_dwarf_bt2_alt_node_uuid, camera_uuid, phase_duration, scene_offset, (0.01, 0.02, 0.02), (-0.01, -0.01, 0.0), 40.0)
    create_act3_sleep_cutscene_cine_node(d, t, 1, cine_short_bt1_alt_node_uuid, camera_uuid, phase_duration, scene_offset, (-0.06, 0.05, 0.04), (0.06, -0.02, 0.0), 40.0)
    create_act3_sleep_cutscene_cine_node(d, t, 1, cine_short_bt2_alt_node_uuid, camera_uuid, phase_duration, scene_offset, (-0.07, 0.0, -0.06), (0.07, 0.0, 0.0), 40.0)


def patch_act3_camp_sleep_cutscenes() -> None:
    patch_act3_camp('CAMP_FARM_SleepCutscene', '56225584-3854-48d9-8221-fdba47a55ad1', '11f44ddb-be46-4a6a-90e7-8e2bd18983f6', (0.0, 0.0, 0.22378372))
    patch_act3_camp('CAMP_SLUMS_SleepCutscene', 'df0c846b-3003-4b7d-8d1a-5e274c6b8d01', 'cfe9c47e-1c32-4ef0-911d-219a6c245a76', (0.0, 0.0, -0.12454431))
    patch_act3_camp('CAMP_ELFSONG_SleepCutscene', '56095698-b660-4ef9-83f4-507c4c35c011', '07039ecf-0d91-455a-86d3-aab1873164cc', (0.0, 0.0, -0.095))


bg3.add_build_procedure('patch_act3_camp_sleep_cutscenes', patch_act3_camp_sleep_cutscenes)

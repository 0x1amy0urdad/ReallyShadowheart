from __future__ import annotations

import bg3moddinglib as bg3

from .context import game_assets

root_victim_killed_node_uuid = '13301f86-8e73-0619-acd3-24402b712d03'
root_victim_saved_node_uuid = '27b8e711-5f07-8986-cf63-6da90796c5d4'
narrator_speaks_node_uuid = 'baa221d3-3fe5-c783-abbe-b92d234b5dca'
victim_killed_node_uuid = '13301f86-8e73-0619-acd3-24402b712d03' # TLShot 6acf4f7e-a637-49e1-83f3-e56745569de4
victim_survived_node_uuid = '27b8e711-5f07-8986-cf63-6da90796c5d4' # TLShot 5292134a-9a7a-4ab9-805a-9b5a749ad236
reaction_fork_node_uuid = '10ce0e11-42ed-4f35-8ea3-a56a6a8e19d3'
partnered_node_uuid = '0aad0986-b2e5-4ff6-92a2-aee41ed99791'
not_partnered_node_uuid = '5cda419c-1b46-4d03-baeb-78aefa7f9c08'
its_difficult_to_talk_about_node_uuid = '220709ed-2a56-4c9b-918f-23f474bab3cd'
its_difficult_to_talk_about_short_node_uuid = '962290ba-bb21-46f4-b90c-66a461da302a'
no_it_cant_be_node_uuid = '15b65667-96d0-4b37-a93f-2d46b7c5cb4c'
shadowheart_reaction_fork_node_uuid = '67c8d8d5-7125-8fc9-3fa0-ab777159f9d8'
bypass_reaction_node_uuid = '34e48748-ad74-4efb-bca5-6fbe9a5e1e65' # this node is needed to bypass the standard reaction when Tav is still kneeled
shadowheart_partnered_reaction_fork_node_uuid = '5d572cf4-65bc-4a67-94ca-4e812d64268f'
my_love_node_uuid = '8662a6cd-4aed-4924-96d1-adf8b9fb3310'
just_keep_safe_out_there_node_uuid = '40b80952-aa0c-4b27-8ed5-acd87bb39bc3'
continuation_node_uuid = '28e238b0-2d86-c423-8a7b-d93faa1ad25f'
end_node_uuid = '31c21ce1-1198-4c21-b16d-0f1b95ef341b'
durge_questions_node_uuid = '0860654c-99cf-fbd3-efe8-22f85632d02d'
youre_the_author_node_uuid = '54974771-1fe0-26a1-a86e-a46d4b729628'
i_am_with_you_come_here_node_uuid = '92132e24-4a7b-4364-8f8a-e3c3ce7317d4'
it_all_is_over_node_uuid = '87ad7853-0bee-4f80-8e33-ac0b3cb5a880'
words_got_stuck_node_uuid = 'd24606cc-a4c1-4edf-8d42-0cd435b1de01'

body_type_fork_node_uuid = '9f874f70-88d3-45aa-aeab-e8d851439a48'
bt1_reaction_node_uuid = 'fbef6376-4524-4444-97c7-cd77254ea16c'
bt2_reaction_node_uuid = '64849802-7662-4dfd-be32-d4a71d9c8888'
bt2_gith_reaction_node_uuid = 'c64398fc-fb5a-4ce3-9cfd-e8fbaf2b6498'
bt3_reaction_node_uuid = '7438cdde-c623-4e10-b309-5f789f953aa0'
bt4_reaction_node_uuid = '50862a9e-17bd-4f80-9dce-4b7c941c87d7'
dragonborn_reaction_node_uuid = 'd7c65e7c-ed64-4964-81cd-0bfe8caefea5'
dwarf_body_reaction_node_uuid = 'ba1b70b0-8b7d-4df4-a3d7-441062101b93'
short_body_reaction_node_uuid = '9ff6809b-4c59-4e54-b050-009f4042b5fd'


#################################################################################################
# Shadowheart cries when Bhaal kills Durge, if she is partnered
#################################################################################################

#################################################################################################
# Dialog: LOW_BhaalTemple_PostBattleDarkUrge_Resistance.lsf
#################################################################################################

def create_shadowheart_line_its_difficult_to_talk_about(
        d: bg3.dialog_object,
        t: bg3.timeline_object,
        dialog_node_uuid: str,
        is_short_race: bool
) -> None:
    speaker_idx_durge = d.get_speaker_slot_index(bg3.SPEAKER_DURGE)

    if is_short_race:
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_State_PartneredWithShadowheart, True, speaker_idx_durge),
            )),
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_SHORT, True, speaker_idx_durge),
            )),
        )
    else:
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_State_PartneredWithShadowheart, True, speaker_idx_durge),
            )),)

    # I... it's difficult for me to talk about...
    d.create_standard_dialog_node(
        dialog_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [it_all_is_over_node_uuid, i_am_with_you_come_here_node_uuid, words_got_stuck_node_uuid],
        bg3.text_content('h79ae6514g939dg49eega50eg86bbf7381a35', 1),
        checkflags = checkflags)
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '4.2',
        dialog_node_uuid,
        ((None, 'd35b098e-8c34-45ee-9dde-21adfd2410a9'),),
        emotions={
            bg3.SPEAKER_SHADOWHEART: ((0.0, 32, None), (2.541, 32, 1)),
            bg3.SPEAKER_DURGE: ((0.0, 32, 2),)
        },
        phase_duration = '4.2',
        speaker_player = bg3.SPEAKER_DURGE)
    # Smeared make-up on Shadowheart's face
    t.create_tl_material(bg3.SPEAKER_SHADOWHEART, '0.0', '4.2', '156a2490-d796-402c-b7fc-e00c032042c1', (), (
        t.create_value_key(time = 0.0, value = True),
    ), is_continuous = True)

    # Place Durge and Shadowheart
    t.create_tl_transform(bg3.SPEAKER_DURGE, '0.0', '4.2', (
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = -8.0),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 0.0),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = -0.83),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = (-0.0, 1.0, -0.0, -0.00020365318)),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 1),
        ),
        (),
    ))
    t.create_tl_transform(bg3.SPEAKER_SHADOWHEART, '0.0', '4.2', (
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = -8.0),
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
    ))
    # Shadowheart looks at Durge
    t.create_tl_actor_node(bg3.timeline_object.LOOK_AT, bg3.SPEAKER_SHADOWHEART, '0.0', '4.2', (
        t.create_look_at_key(
            0.0,
            target = bg3.SPEAKER_DURGE,
            bone = 'Head_M',
            turn_mode = 3,
            turn_speed_multiplier = 0.3,
            torso_turn_speed_multiplier = 0.3,
            head_turn_speed_multiplier = 0.3,
            weight = 0.0,
            reset = True,
            eye_look_at_bone = 'Head_M'),
    ), is_snapped_to_end = True)
    # Durge looks at Shadowheart
    t.create_tl_actor_node(bg3.timeline_object.LOOK_AT, bg3.SPEAKER_DURGE, '0.0', '4.2', (
        t.create_look_at_key(
            0.0,
            target = bg3.SPEAKER_SHADOWHEART,
            bone = 'Head_M',
            turn_mode = 3,
            turn_speed_multiplier = 0.3,
            torso_turn_speed_multiplier = 0.3,
            head_turn_speed_multiplier = 0.3,
            weight = 0.0,
            reset = True,
            eye_look_at_bone = 'Head_M'),
    ), is_snapped_to_end = True)

    # Hide helmet
    t.create_tl_show_armor(bg3.SPEAKER_SHADOWHEART, '0.0', '4.2', (
        (
            t.create_value_key(time = 0.0, value = False, interpolation_type = 0),
        ),
        (), (), (), (), (), (), (), (), (), ()
    ))

    # Hide everyone
    t.create_tl_actor_node(bg3.timeline_object.SHOW_VISUAL, bg3.SPEAKER_JERGAL, '0.0', '4.2', (
        t.create_value_key(time = 0.0, interpolation_type = 3, value_name = 'ShowVisual', value = False),
    ))
    t.create_tl_actor_node(bg3.timeline_object.SHOW_VISUAL, bg3.SPEAKER_ASTARION, '0.0', '4.2', (
        t.create_value_key(time = 0.0, interpolation_type = 3, value_name = 'ShowVisual', value = False),
    ))
    t.create_tl_actor_node(bg3.timeline_object.SHOW_VISUAL, bg3.SPEAKER_GALE, '0.0', '4.2', (
        t.create_value_key(time = 0.0, interpolation_type = 3, value_name = 'ShowVisual', value = False),
    ))
    t.create_tl_actor_node(bg3.timeline_object.SHOW_VISUAL, bg3.SPEAKER_HALSIN, '0.0', '4.2', (
        t.create_value_key(time = 0.0, interpolation_type = 3, value_name = 'ShowVisual', value = False),
    ))
    t.create_tl_actor_node(bg3.timeline_object.SHOW_VISUAL, bg3.SPEAKER_JAHEIRA, '0.0', '4.2', (
        t.create_value_key(time = 0.0, interpolation_type = 3, value_name = 'ShowVisual', value = False),
    ))
    t.create_tl_actor_node(bg3.timeline_object.SHOW_VISUAL, bg3.SPEAKER_KARLACH, '0.0', '4.2', (
        t.create_value_key(time = 0.0, interpolation_type = 3, value_name = 'ShowVisual', value = False),
    ))
    t.create_tl_actor_node(bg3.timeline_object.SHOW_VISUAL, bg3.SPEAKER_LAEZEL, '0.0', '4.2', (
        t.create_value_key(time = 0.0, interpolation_type = 3, value_name = 'ShowVisual', value = False),
    ))
    t.create_tl_actor_node(bg3.timeline_object.SHOW_VISUAL, bg3.SPEAKER_MINSC, '0.0', '4.2', (
        t.create_value_key(time = 0.0, interpolation_type = 3, value_name = 'ShowVisual', value = False),
    ))
    t.create_tl_actor_node(bg3.timeline_object.SHOW_VISUAL, bg3.SPEAKER_MINTHARA, '0.0', '4.2', (
        t.create_value_key(time = 0.0, interpolation_type = 3, value_name = 'ShowVisual', value = False),
    ))
    t.create_tl_actor_node(bg3.timeline_object.SHOW_VISUAL, bg3.SPEAKER_WYLL, '0.0', '4.2', (
        t.create_value_key(time = 0.0, interpolation_type = 3, value_name = 'ShowVisual', value = False),
    ))

    # Point the camera at Shadowheart
    t.create_tl_camera_fov('d35b098e-8c34-45ee-9dde-21adfd2410a9', '0.0', '4.15', (
        t.create_value_key(time = 0.0, value = 20.0, value_name = 'FoV', interpolation_type = 2),
    ), is_snapped_to_end = True)
    if is_short_race:
        t.create_tl_transform('d35b098e-8c34-45ee-9dde-21adfd2410a9', '0.0', '4.15', (
            (
                t.create_value_key(time = 0.0, interpolation_type = 5, value = -7.0),
            ),
            (
                t.create_value_key(time = 0.0, interpolation_type = 5, value = 1.4),
            ),
            (
                t.create_value_key(time = 0.0, interpolation_type = 5, value = -2.0),
            ),
            (
                t.create_value_key(time = 0.0, interpolation_type = 5, value = bg3.euler_to_quaternion(-32.0, 0.0, 0.0, sequence='yxz')),
            ),
            (),
            (),
        ))
    else:
        t.create_tl_transform('d35b098e-8c34-45ee-9dde-21adfd2410a9', '0.0', '4.15', (
            (
                t.create_value_key(time = 0.0, interpolation_type = 5, value = -7.0),
            ),
            (
                t.create_value_key(time = 0.0, interpolation_type = 5, value = 2.0),
            ),
            (
                t.create_value_key(time = 0.0, interpolation_type = 5, value = -2.0),
            ),
            (
                t.create_value_key(time = 0.0, interpolation_type = 5, value = bg3.euler_to_quaternion(-32.0, 10.0, 0.0, sequence='yxz')),
            ),
            (),
            (),
        ))
    t.create_tl_camera_fov('d35b098e-8c34-45ee-9dde-21adfd2410a9', '4.15', '4.2', (
        t.create_value_key(time = 0.0, value_name = 'FoV', value = 35.0, interpolation_type = 2),
    ))
    if is_short_race:
        t.create_tl_transform('d35b098e-8c34-45ee-9dde-21adfd2410a9', '4.15', '4.2', (
            (
                t.create_value_key(time = 0.0, interpolation_type = 5, value = -7.5),
            ),
            (
                t.create_value_key(time = 0.0, interpolation_type = 5, value = 1.2),
            ),
            (
                t.create_value_key(time = 0.0, interpolation_type = 5, value = 0.2),
            ),
            (
                t.create_value_key(time = 0.0, interpolation_type = 5, value = bg3.euler_to_quaternion(-154.0, 0.0, 0.0, sequence = 'yxz')),
            ),
            (),
            (),
        ))
    else:
        t.create_tl_transform('d35b098e-8c34-45ee-9dde-21adfd2410a9', '4.15', '4.2', (
            (
                t.create_value_key(time = 0.0, interpolation_type = 5, value = -7.5),
            ),
            (
                t.create_value_key(time = 0.0, interpolation_type = 5, value = 1.8),
            ),
            (
                t.create_value_key(time = 0.0, interpolation_type = 5, value = 0.2),
            ),
            (
                t.create_value_key(time = 0.0, interpolation_type = 5, value = bg3.euler_to_quaternion(-154.0, 0.0, 0.0, sequence = 'yxz')),
            ),
            (),
            (),
        ))


def create_scene_shadowheart_cries_when_durge_dies() -> None:

    # d = bg3.dialog_object(files.get_file('Gustav', 'Mods/GustavDev/Story/DialogsBinary/Act3/LowerCity/BhaalTemple/LOW_BhaalTemple_PostBattleDarkUrge_Resistance.lsf'))
    # t = bg3.timeline_object(files.get_file('Gustav', 'Public/GustavDev/Timeline/Generated/LOW_BhaalTemple_PostBattleDarkUrge_Resistance.lsf'), d)

    ab = game_assets.get_modded_dialog_asset_bundle('LOW_BhaalTemple_PostBattleDarkUrge_Resistance')
    d = bg3.dialog_object(ab.dialog)
    t = bg3.timeline_object(ab.timeline, d)

    speaker_idx_durge = d.get_speaker_slot_index(bg3.SPEAKER_DURGE)
    speaker_idx_shadowheart = d.get_speaker_slot_index(bg3.SPEAKER_SHADOWHEART)

    d.delete_all_children_dialog_nodes(victim_killed_node_uuid)
    d.delete_all_children_dialog_nodes(victim_survived_node_uuid)
    d.add_child_dialog_node(victim_killed_node_uuid, reaction_fork_node_uuid)
    d.add_child_dialog_node(victim_survived_node_uuid, reaction_fork_node_uuid)

    # Replace TLShot in the opening phase
    # victim_killed_node_uuid
    tl_shot = t.find_effect_component('6acf4f7e-a637-49e1-83f3-e56745569de4')
    camera_container = tl_shot.find('./children/node[@id="CameraContainer"]')
    if camera_container is None:
        raise RuntimeError(f'Cannot file CameraContainer in 6acf4f7e-a637-49e1-83f3-e56745569de4')
    bg3.set_bg3_attribute(camera_container, 'Object', 'e94156bf-b946-4a79-b197-d8f092716a21')
    # victim_survived_node_uuid
    tl_shot = t.find_effect_component('5292134a-9a7a-4ab9-805a-9b5a749ad236')
    camera_container = tl_shot.find('./children/node[@id="CameraContainer"]')
    if camera_container is None:
        raise RuntimeError(f'Cannot file CameraContainer in 5292134a-9a7a-4ab9-805a-9b5a749ad236')
    bg3.set_bg3_attribute(camera_container, 'Object', 'e94156bf-b946-4a79-b197-d8f092716a21')

    # Suppress default Shadowheart's reaction if she is in relationship with Durge
    d.set_dialog_flags(youre_the_author_node_uuid, checkflags = (
        bg3.flag_group('Object', (
            bg3.flag(bg3.FLAG_ORI_Inclusion_PickedAtRandom, True, speaker_idx_shadowheart),
            bg3.flag(bg3.FLAG_ORI_State_PartneredWithShadowheart, False, speaker_idx_durge),
        )),
        bg3.flag_group('Tag', (
            bg3.flag(bg3.TAG_REALLY_SHADOWHEART, True, speaker_idx_shadowheart),
        )),
    ))

    # Reaction fork: partnered or not partnerted with Shadowheart
    d.create_standard_dialog_node(
        reaction_fork_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [partnered_node_uuid, not_partnered_node_uuid],
        None
    )
    d.create_standard_dialog_node(
        partnered_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [no_it_cant_be_node_uuid],
        None,
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_State_PartneredWithShadowheart, True, speaker_idx_durge),
            )),
        )
    )
    d.create_standard_dialog_node(
        not_partnered_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [narrator_speaks_node_uuid],
        None,
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_State_PartneredWithShadowheart, False, speaker_idx_durge),
            )),
        )
    )

    # No... it can't be true...
    d.create_standard_dialog_node(
        no_it_cant_be_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [narrator_speaks_node_uuid],
        bg3.text_content('hcce3a355g2e43g4231g94fdg0d16de9a5cb8', 1)
    )
    t.create_new_phase(no_it_cant_be_node_uuid, '16.82')
    t.create_tl_actor_node(bg3.timeline_object.ATTITUDE, bg3.SPEAKER_DURGE, '0.0', '16.82', (), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.ATTITUDE, bg3.SPEAKER_SHADOWHEART, '0.0', '16.82', (), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.EMOTION, bg3.SPEAKER_SHADOWHEART, '0.0', '16.82', (
        t.create_emotion_key(0.0, 32),
        t.create_emotion_key(3.0, 32, variation = 1),
        t.create_emotion_key(6.2, 32, variation = 2),
        t.create_emotion_key(8.5, 32, variation = 24),
    ), is_snapped_to_end = True)

    # Hide helmet
    t.create_tl_show_armor(bg3.SPEAKER_SHADOWHEART, '0.0', '16.82', (
        (
            t.create_value_key(time = 0.0, value = False, interpolation_type = 0),
            #t.create_value_key(time = 16.82, interpolation_type = 0)
        ),
        (), (), (), (), (), (), (), (), (), ()
    ))

    t.create_tl_actor_node(bg3.timeline_object.SHOW_VISUAL, bg3.SPEAKER_JERGAL, '0.0', '16.82', (
        t.create_value_key(time = 0.0, interpolation_type = 3, value_name = 'ShowVisual', value = False),
        t.create_value_key(time = '14.1', interpolation_type = 3, value_name = 'ShowVisual', value = True),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.SHOW_VISUAL, bg3.SPEAKER_ASTARION, '0.0', '16.82', (
        t.create_value_key(time = 0.0, interpolation_type = 3, value_name = 'ShowVisual', value = False),
        t.create_value_key(time = '14.1', interpolation_type = 3, value_name = 'ShowVisual', value = True),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.SHOW_VISUAL, bg3.SPEAKER_GALE, '0.0', '16.82', (
        t.create_value_key(time = 0.0, interpolation_type = 3, value_name = 'ShowVisual', value = False),
        t.create_value_key(time = '14.1', interpolation_type = 3, value_name = 'ShowVisual', value = True),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.SHOW_VISUAL, bg3.SPEAKER_HALSIN, '0.0', '16.82', (
        t.create_value_key(time = 0.0, interpolation_type = 3, value_name = 'ShowVisual', value = False),
        t.create_value_key(time = '14.1', interpolation_type = 3, value_name = 'ShowVisual', value = True),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.SHOW_VISUAL, bg3.SPEAKER_JAHEIRA, '0.0', '16.82', (
        t.create_value_key(time = 0.0, interpolation_type = 3, value_name = 'ShowVisual', value = False),
        t.create_value_key(time = '14.1', interpolation_type = 3, value_name = 'ShowVisual', value = True),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.SHOW_VISUAL, bg3.SPEAKER_KARLACH, '0.0', '16.82', (
        t.create_value_key(time = 0.0, interpolation_type = 3, value_name = 'ShowVisual', value = False),
        t.create_value_key(time = '14.1', interpolation_type = 3, value_name = 'ShowVisual', value = True),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.SHOW_VISUAL, bg3.SPEAKER_LAEZEL, '0.0', '16.82', (
        t.create_value_key(time = 0.0, interpolation_type = 3, value_name = 'ShowVisual', value = False),
        t.create_value_key(time = '14.1', interpolation_type = 3, value_name = 'ShowVisual', value = True),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.SHOW_VISUAL, bg3.SPEAKER_MINSC, '0.0', '16.82', (
        t.create_value_key(time = 0.0, interpolation_type = 3, value_name = 'ShowVisual', value = False),
        t.create_value_key(time = '14.1', interpolation_type = 3, value_name = 'ShowVisual', value = True),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.SHOW_VISUAL, bg3.SPEAKER_MINTHARA, '0.0', '16.82', (
        t.create_value_key(time = 0.0, interpolation_type = 3, value_name = 'ShowVisual', value = False),
        t.create_value_key(time = '14.1', interpolation_type = 3, value_name = 'ShowVisual', value = True),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.SHOW_VISUAL, bg3.SPEAKER_WYLL, '0.0', '16.82', (
        t.create_value_key(time = 0.0, interpolation_type = 3, value_name = 'ShowVisual', value = False),
        t.create_value_key(time = '14.1', interpolation_type = 3, value_name = 'ShowVisual', value = True),
    ), is_snapped_to_end = True)

    # Place Shadowheart
    t.create_tl_transform(bg3.SPEAKER_SHADOWHEART, '0.0', '16.82', (
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = -8.0),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 0.0),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 2.4),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = (0.0, 0.0, 0.0, 1.0)),
        ),
        (),
        ()
    ))

    # Point the camera at Shadowheart
    # Euler angles: X = -10, Y = -7, Z = 0
    t.create_tl_transform('d35b098e-8c34-45ee-9dde-21adfd2410a9', '0.0', '9.5', (
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = -7.8),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 1.85),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 0.9),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = bg3.euler_to_quaternion(-7.0, 10.0, 0.0, sequence='yxz')),
        ),
        (),
        ()
    ))

    t.create_tl_shot('e94156bf-b946-4a79-b197-d8f092716a21', '0.0', '3.0')

    t.create_tl_actor_node(bg3.timeline_object.SOUND, bg3.SPEAKER_SHADOWHEART, '0.0', '16.82', (
        t.create_sound_event_key('9.89', sound_event_id = 'fbb1b315-cb7b-4726-85db-136aaca5b0f9', sound_object_index = 4),
        t.create_sound_event_key('11.26', sound_event_id = '8a8136ee-5103-4db4-a2f5-050d2268338a', sound_object_index = 4),
        t.create_sound_event_key('13.06', sound_event_id = 'fbb1b315-cb7b-4726-85db-136aaca5b0f9', sound_object_index = 4),
        t.create_sound_event_key('13.86', sound_event_id = '8428155b-41f4-4618-9bb6-67fe9555954b', sound_object_index = 4),
        t.create_sound_event_key('14.89', sound_event_id = '8a8136ee-5103-4db4-a2f5-050d2268338a', sound_object_index = 4),
        t.create_sound_event_key('16.26', sound_event_id = 'fbb1b315-cb7b-4726-85db-136aaca5b0f9', sound_object_index = 4),
    ), is_snapped_to_end = True)
    t.create_tl_material(bg3.SPEAKER_SHADOWHEART, '0.0', '16.82', '156a2490-d796-402c-b7fc-e00c032042c1', (), (
        t.create_value_key(time = 0.0, value = False),
        t.create_value_key(time = '10.7', value = True),
    ), is_snapped_to_end = True, is_continuous = True)

    t.create_tl_shot('d35b098e-8c34-45ee-9dde-21adfd2410a9', '3.0', '14.1')
    t.create_tl_voice(
        bg3.SPEAKER_SHADOWHEART, '3.0', '7.0',
        no_it_cant_be_node_uuid,
        is_snapped_to_end = True,
        performance_fade = 0.0,
        fade_in = 1.0,
        fade_out = 1.0)


    t.create_tl_animation(bg3.SPEAKER_SHADOWHEART, '9.0', '14.82', 'b5822e0c-f5e5-9282-851e-e8f94daf5aef', 'c8dad77b-5b76-44fe-bfeb-61d676ede3f6', is_snapped_to_end = True, fade_in = 1.5, fade_out = 1.0)

    t.create_tl_transform('d35b098e-8c34-45ee-9dde-21adfd2410a9', '9.5', '16.82', (
        (
            # -6.8 moves to the right
            t.create_value_key(time = '14.0', interpolation_type = 5, value = -6.2),
        ),
        (
            t.create_value_key(time = '14.0', interpolation_type = 5, value = 1.2),
        ),
        (
            # 1.9 moves forward
            t.create_value_key(time = '14.0', interpolation_type = 5, value = 3.5),
        ),
        (
            #t.create_value_key(time = 0.0, interpolation_type = 5, value = (0.08699, -0.06082, 0.005321, 0.9943)),
            t.create_value_key(time = '14.0', interpolation_type = 5, value = bg3.euler_to_quaternion(-135.0, -12.0, 0.0, sequence='yxz')),
        ),
        (),
        ()
    ))

    t.create_tl_shot('e94156bf-b946-4a79-b197-d8f092716a21', '14.1', '16.82')

    d.create_standard_dialog_node(
        bypass_reaction_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [continuation_node_uuid],
        None,
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_State_PartneredWithShadowheart, True, speaker_idx_durge),
            )),
        )
    )

    d.add_child_dialog_node(shadowheart_reaction_fork_node_uuid, bypass_reaction_node_uuid, 0)

    d.create_standard_dialog_node(
        shadowheart_partnered_reaction_fork_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [
            its_difficult_to_talk_about_short_node_uuid,
            its_difficult_to_talk_about_node_uuid,
            end_node_uuid
        ],
        None
    )

    d.create_standard_dialog_node(
        end_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [],
        None,
        end_node = True
    )

    end_nodes = (
        '229059ca-7ca0-55bd-feee-714d3be1ae7e',
        '25545e26-be6a-cb40-9c70-5dedbbdecbf4',
        '476d1ef8-06df-dc56-1d45-ee17c34d16e3',
        '7b262744-577d-1eb2-12b1-0fef9e6bd929')

    for end_node in end_nodes:
        d.remove_dialog_attribute(end_node, 'endnode')
        d.add_child_dialog_node(end_node, shadowheart_partnered_reaction_fork_node_uuid)

    create_shadowheart_line_its_difficult_to_talk_about(d, t, its_difficult_to_talk_about_node_uuid, False)
    create_shadowheart_line_its_difficult_to_talk_about(d, t, its_difficult_to_talk_about_short_node_uuid, True)

    d.create_standard_dialog_node(
        it_all_is_over_node_uuid,
        bg3.SPEAKER_DURGE,
        [body_type_fork_node_uuid],
        bg3.text_content('hc8894122g2583g49fagb874gec6395df6db3', 1),
        constructor = bg3.dialog_object.QUESTION)
    d.create_standard_dialog_node(
        i_am_with_you_come_here_node_uuid,
        bg3.SPEAKER_DURGE,
        [body_type_fork_node_uuid],
        bg3.text_content('hf7fae672g1197g4ba1gbc2bg5c2362431368', 1),
        constructor = bg3.dialog_object.QUESTION)
    d.create_standard_dialog_node(
        words_got_stuck_node_uuid,
        bg3.SPEAKER_DURGE,
        [body_type_fork_node_uuid],
        bg3.text_content('hbc1e6032gcbebg4226ga889gd7d1e7b7a121', 1),
        constructor = bg3.dialog_object.QUESTION)


    # Just keep safe out there, for me.
    d.create_standard_dialog_node(
        just_keep_safe_out_there_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [end_node_uuid],
        bg3.text_content('h4983a16dg6a89g46f6g962fg5dcf9078e466', 2))
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '4.5',
        just_keep_safe_out_there_node_uuid,
        ((None, 'd35b098e-8c34-45ee-9dde-21adfd2410a9'),),
        emotions={
            bg3.SPEAKER_SHADOWHEART: ((0.0, 32, None),),
            bg3.SPEAKER_DURGE: ((0.0, 1, None),)
        },
        speaker_player = bg3.SPEAKER_DURGE)

    # Smeared make-up on Shadowheart's face
    t.create_tl_material(bg3.SPEAKER_SHADOWHEART, '0.0', '4.5', '156a2490-d796-402c-b7fc-e00c032042c1', (), (
        t.create_value_key(time = 0.0, value = True),
    ), is_snapped_to_end = True, is_continuous = True)

    # Place Durge and Shadowheart
    t.create_tl_transform(bg3.SPEAKER_DURGE, '0.0', '4.5', (
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = -8.0),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 0.0),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = -0.83),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = (-0.0, 1.0, -0.0, -0.00020365318)),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 1),
        ),
        (),
    ))
    t.create_tl_transform(bg3.SPEAKER_SHADOWHEART, '0.0', '4.5', (
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = -8.0),
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
    ))
    # Shadowheart looks at Durge
    t.create_tl_actor_node(bg3.timeline_object.LOOK_AT, bg3.SPEAKER_SHADOWHEART, '0.0', '4.5', (
        t.create_look_at_key(
            0.0,
            target = bg3.SPEAKER_DURGE,
            bone = 'Head_M',
            turn_mode = 3,
            turn_speed_multiplier = 0.3,
            torso_turn_speed_multiplier = 0.3,
            head_turn_speed_multiplier = 0.3,
            weight = 0.0,
            reset = True,
            eye_look_at_bone = 'Head_M'),
    ), is_snapped_to_end = True)
    # Durge looks at Shadowheart
    t.create_tl_actor_node(bg3.timeline_object.LOOK_AT, bg3.SPEAKER_DURGE, '0.0', '4.5', (
        t.create_look_at_key(
            0.0,
            target = bg3.SPEAKER_SHADOWHEART,
            bone = 'Head_M',
            turn_mode = 3,
            turn_speed_multiplier = 0.3,
            torso_turn_speed_multiplier = 0.3,
            head_turn_speed_multiplier = 0.3,
            weight = 0.0,
            reset = True,
            eye_look_at_bone = 'Head_M'),
    ), is_snapped_to_end = True)

    # Hide helmet
    t.create_tl_show_armor(bg3.SPEAKER_SHADOWHEART, '0.0', '4.5', (
        (
            t.create_value_key(time = 0.0, value = False, interpolation_type = 0),
            #t.create_value_key(time = 4.5, interpolation_type = 0)
        ),
        (), (), (), (), (), (), (), (), (), ()
    ))

    # Hide everyone
    t.create_tl_actor_node(bg3.timeline_object.SHOW_VISUAL, bg3.SPEAKER_DURGE, '0.0', '4.5', (
        t.create_value_key(time = 0.0, interpolation_type = 3, value_name = 'ShowVisual', value = False),
        t.create_value_key(time = 4.5, interpolation_type = 3, value_name = 'ShowVisual', value = True),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.SHOW_VISUAL, bg3.SPEAKER_JERGAL, '0.0', '4.5', (
        t.create_value_key(time = 0.0, interpolation_type = 3, value_name = 'ShowVisual', value = False),
    ))
    t.create_tl_actor_node(bg3.timeline_object.SHOW_VISUAL, bg3.SPEAKER_ASTARION, '0.0', '4.5', (
        t.create_value_key(time = 0.0, interpolation_type = 3, value_name = 'ShowVisual', value = False),
    ))
    t.create_tl_actor_node(bg3.timeline_object.SHOW_VISUAL, bg3.SPEAKER_GALE, '0.0', '4.5', (
        t.create_value_key(time = 0.0, interpolation_type = 3, value_name = 'ShowVisual', value = False),
    ))
    t.create_tl_actor_node(bg3.timeline_object.SHOW_VISUAL, bg3.SPEAKER_HALSIN, '0.0', '4.5', (
        t.create_value_key(time = 0.0, interpolation_type = 3, value_name = 'ShowVisual', value = False),
    ))
    t.create_tl_actor_node(bg3.timeline_object.SHOW_VISUAL, bg3.SPEAKER_JAHEIRA, '0.0', '4.5', (
        t.create_value_key(time = 0.0, interpolation_type = 3, value_name = 'ShowVisual', value = False),
    ))
    t.create_tl_actor_node(bg3.timeline_object.SHOW_VISUAL, bg3.SPEAKER_KARLACH, '0.0', '4.5', (
        t.create_value_key(time = 0.0, interpolation_type = 3, value_name = 'ShowVisual', value = False),
    ))
    t.create_tl_actor_node(bg3.timeline_object.SHOW_VISUAL, bg3.SPEAKER_LAEZEL, '0.0', '4.5', (
        t.create_value_key(time = 0.0, interpolation_type = 3, value_name = 'ShowVisual', value = False),
    ))
    t.create_tl_actor_node(bg3.timeline_object.SHOW_VISUAL, bg3.SPEAKER_MINSC, '0.0', '4.5', (
        t.create_value_key(time = 0.0, interpolation_type = 3, value_name = 'ShowVisual', value = False),
    ))
    t.create_tl_actor_node(bg3.timeline_object.SHOW_VISUAL, bg3.SPEAKER_MINTHARA, '0.0', '4.5', (
        t.create_value_key(time = 0.0, interpolation_type = 3, value_name = 'ShowVisual', value = False),
    ))
    t.create_tl_actor_node(bg3.timeline_object.SHOW_VISUAL, bg3.SPEAKER_WYLL, '0.0', '4.5', (
        t.create_value_key(time = 0.0, interpolation_type = 3, value_name = 'ShowVisual', value = False),
    ))

    # Point the camera at Shadowheart
    t.create_tl_camera_fov('d35b098e-8c34-45ee-9dde-21adfd2410a9', '0.0', '4.5', (
        t.create_value_key(time = 0.0, interpolation_type = 2),
    ), is_snapped_to_end = True)
    t.create_tl_transform('d35b098e-8c34-45ee-9dde-21adfd2410a9', '0.0', '4.5', (
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = -8.0),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 1.6),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = -0.7),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = (0.0, 0.0, 0.0, 1.0)),
        ),
        (),
        (),
    ))

    d.create_standard_dialog_node(
        body_type_fork_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [
            dwarf_body_reaction_node_uuid,
            short_body_reaction_node_uuid,
            dragonborn_reaction_node_uuid,
            bt3_reaction_node_uuid,
            bt1_reaction_node_uuid,
            bt4_reaction_node_uuid,
            bt2_gith_reaction_node_uuid,
            bt2_reaction_node_uuid
        ],
        None)


#################################################################################################
# New Shadowheart reaction: I truly love you.
#################################################################################################

#################################################################################################
# Body type 2 except gith
#################################################################################################

def create_scene_shadowheart_reaction_body_type_2() -> None:

    # d = bg3.dialog_object(files.get_file('Gustav', 'Mods/GustavDev/Story/DialogsBinary/Act3/LowerCity/BhaalTemple/LOW_BhaalTemple_PostBattleDarkUrge_Resistance.lsf'))
    # t = bg3.timeline_object(files.get_file('Gustav', 'Public/GustavDev/Timeline/Generated/LOW_BhaalTemple_PostBattleDarkUrge_Resistance.lsf'), d)

    ab = game_assets.get_modded_dialog_asset_bundle('LOW_BhaalTemple_PostBattleDarkUrge_Resistance')
    d = bg3.dialog_object(ab.dialog)
    t = bg3.timeline_object(ab.timeline, d)

    # slot_idx_durge = d.get_speaker_slot_index(bg3.SPEAKER_DURGE)
    # slot_idx_shadowheart = d.get_speaker_slot_index(bg3.SPEAKER_SHADOWHEART)

    # d.create_cinematic_dialog_node(
    #     normal_body_reaction_node_uuid,
    #     [just_keep_safe_out_there_node_uuid])
    d.create_standard_dialog_node(
        bt2_reaction_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [just_keep_safe_out_there_node_uuid],
        bg3.text_content('hd896e304g5fc4g41e7g807cg524360fee6a9', 1)
    )

    phase_duration = '54.42' # '53.22' # 54.42 # 56.22
    t.create_new_phase(bt2_reaction_node_uuid, phase_duration)

    t.create_tl_actor_node(bg3.timeline_object.ATTITUDE, bg3.SPEAKER_DURGE, '0.0', phase_duration, (
        t.create_attitude_key(12.15, bg3.ATTITUDE_DIAG_Pose_Stand_R_Forward_01, bg3.ATTITUDE_DIAG_T_Pose),
        t.create_attitude_key(28.81, 'a2bd89b1-8ab9-4231-ac4b-e593d75aa083', bg3.ATTITUDE_DIAG_T_Pose),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.ATTITUDE, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_attitude_key(0.0, bg3.ATTITUDE_DIAG_Pose_Stand_L_Forward_01, bg3.ATTITUDE_DIAG_T_Pose),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.EMOTION, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_emotion_key(0.0, 32),
        t.create_emotion_key(6.13, 32, variation = 2),
        t.create_emotion_key(7.34, 32),
        t.create_emotion_key(15.63, 32, variation = 1),
        t.create_emotion_key(20.58, 32),
        t.create_emotion_key(44.85, 32, variation = 1, is_sustained = False),
        t.create_emotion_key(51.97, 32)
        #t.create_emotion_key(26.0, 2)
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.EMOTION, bg3.SPEAKER_DURGE, '0.0', phase_duration, (
        t.create_emotion_key(0.0, 32, variation = 1),
        t.create_emotion_key(3.51, 32),
        t.create_emotion_key(6.08, 32, variation = 1),
        t.create_emotion_key(6.56, 32),
        t.create_emotion_key(8.26, 32, variation = 2),
        t.create_emotion_key(11.26, 32, variation = 1),
        t.create_emotion_key(22.03, 32),
        t.create_emotion_key(40.14, 256),
        t.create_emotion_key(44.85, 32),
    ), is_snapped_to_end = True)
    #t.create_tl_actor_node(bg3.timeline_object.EMOTION, bg3.SPEAKER_JERGAL, '0.0', phase_duration, (
    #    t.create_emotion_key(0.0, 1, None),
    #    t.create_emotion_key(25.5, 2, variation = 2),
    #), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.LOOK_AT, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_look_at_key(
            0.0,
            target = bg3.SPEAKER_DURGE,
            bone = 'Head_M',
            turn_mode = 3,
            turn_speed_multiplier = 0.3,
            torso_turn_speed_multiplier = 0.3,
            head_turn_speed_multiplier = 0.3,
            weight = 0.0,
            reset = True,
            eye_look_at_bone = 'Head_M'),
        t.create_look_at_key(
            '4.20',
            target = bg3.SPEAKER_DURGE,
            bone = 'Head_M',
            turn_mode = 3,
            turn_speed_multiplier = 0.3,
            torso_turn_speed_multiplier = 0.3,
            head_turn_speed_multiplier = 0.3,
            weight = 0.3,
            safe_zone_angle = 80.0,
            head_safe_zone_angle = 80.0,
            reset = True,
            look_at_mode = 1,
            eye_look_at_bone = 'Head_M'),
        t.create_look_at_key(
            '9.41',
            turn_mode = 3,
            turn_speed_multiplier = 0.26370612,
            torso_turn_speed_multiplier = 0.26370612,
            head_turn_speed_multiplier = 0.26370612,
            weight = 0.3,
            safe_zone_angle = 80.0,
            head_safe_zone_angle = 80.0,
            look_at_mode = 0),
        t.create_look_at_key(
            '24.27',
            target = bg3.SPEAKER_DURGE,
            bone = 'Head_M',
            turn_mode = 3,
            turn_speed_multiplier = 0.3,
            torso_turn_speed_multiplier = 0.3,
            head_turn_speed_multiplier = 0.3,
            weight = 0.0,
            safe_zone_angle = 80.0,
            head_safe_zone_angle = 80.0,
            reset = True,
            look_at_mode = 1,
            eye_look_at_bone = 'Head_M'),
        t.create_look_at_key(
            '28.81',
            target = bg3.SPEAKER_DURGE,
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
    t.create_tl_actor_node(bg3.timeline_object.LOOK_AT, bg3.SPEAKER_DURGE, '0.0', phase_duration, (
        t.create_look_at_key(
            0.0,
            target = bg3.SPEAKER_SHADOWHEART,
            bone = 'Head_M',
            turn_mode = 3,
            turn_speed_multiplier = 0.3,
            torso_turn_speed_multiplier = 0.3,
            head_turn_speed_multiplier = 0.21843724,
            weight = 0.0,
            safe_zone_angle = 80.0,
            head_safe_zone_angle = 80.0,
            look_at_mode = 1,
            eye_look_at_bone = 'Head_M'),
        t.create_look_at_key(
            '4.20',
            turn_mode = 3,
            turn_speed_multiplier = 0.3,
            torso_turn_speed_multiplier = 0.3,
            head_turn_speed_multiplier = 0.1,
            weight = 0.0,
            safe_zone_angle = 80.0,
            head_safe_zone_angle = 80.0,
            look_at_mode = 0),
        t.create_look_at_key(
            '6.56',
            target = bg3.SPEAKER_SHADOWHEART,
            bone = 'Head_M',
            turn_mode = 3,
            turn_speed_multiplier = 0.3269225,
            torso_turn_speed_multiplier = 0.3269225,
            head_turn_speed_multiplier = 0.10897417,
            weight = 0.0,
            safe_zone_angle = 80.0,
            head_safe_zone_angle = 80.0,
            look_at_mode = 1,
            eye_look_at_bone = 'Head_M'),
        t.create_look_at_key(
            '9.4',
            turn_mode = 3,
            turn_speed_multiplier = 0.25471807,
            torso_turn_speed_multiplier = 0.25471807,
            head_turn_speed_multiplier = 0.08490602,
            weight = 0.0,
            safe_zone_angle = 80.0,
            head_safe_zone_angle = 80.0,
            look_at_mode = 0),
        t.create_look_at_key(
            '24.27',
            target = bg3.SPEAKER_SHADOWHEART,
            bone = 'Head_M',
            turn_mode = 3,
            turn_speed_multiplier = 0.3,
            torso_turn_speed_multiplier = 0.3,
            head_turn_speed_multiplier = 0.1,
            weight = 0.0,
            safe_zone_angle = 80.0,
            head_safe_zone_angle = 80.0,
            reset = True,
            look_at_mode = 1,
            eye_look_at_bone = 'Head_M'),
        t.create_look_at_key(
            '28.81',
            target = bg3.SPEAKER_SHADOWHEART,
            bone = 'Head_M',
            turn_mode = 3,
            turn_speed_multiplier = 0.3,
            head_turn_speed_multiplier = 0.1,
            weight = 0.0,
            safe_zone_angle = 80.0,
            head_safe_zone_angle = 80.0,
            look_at_mode = 1,
            eye_look_at_bone = 'Head_M'),
    ), is_snapped_to_end = True)

    t.create_tl_material(bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, '156a2490-d796-402c-b7fc-e00c032042c1', (), (
        t.create_value_key(time = 0.0, value = True),
    ), is_snapped_to_end = True, is_continuous = True)

    # Hide helmets
    t.create_tl_show_armor(bg3.SPEAKER_DURGE, '0.0', phase_duration, (
        (
            t.create_value_key(time = 0.0, value = False, interpolation_type = 0),
            t.create_value_key(time = phase_duration, interpolation_type = 0)
        ),
        (), (), (), (), (), (), (), (), (), ()
    ))
    t.create_tl_show_armor(bg3.SPEAKER_SHADOWHEART, '0.0',  phase_duration, (
        (
            t.create_value_key(time = 0.0, value = False, interpolation_type = 0),
            t.create_value_key(time = phase_duration, interpolation_type = 0)
        ),
        (), (), (), (), (), (), (), (), (), ()
    ))

    # Hide weapons
    t.create_tl_actor_node(bg3.timeline_object.SHOW_WEAPON, bg3.SPEAKER_DURGE, '0.0', phase_duration, (
        t.create_value_key(time = 0.0, value_name = 'ShowWeapon', value = False, interpolation_type = 3),
        t.create_value_key(time = phase_duration, interpolation_type = 3),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.SHOW_WEAPON, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_value_key(time = 0.0, value_name = 'ShowWeapon', value = False, interpolation_type = 3),
        t.create_value_key(time = phase_duration, interpolation_type = 3),
    ), is_snapped_to_end = True)

    # Show Durge
    t.create_tl_actor_node(bg3.timeline_object.SHOW_VISUAL, bg3.SPEAKER_DURGE, '0.0', phase_duration, (
        t.create_value_key(time = 0.0, interpolation_type = 3),
    ), is_snapped_to_end = True)

    # Sounds
    # Hug part
    t.create_tl_actor_node(bg3.timeline_object.SOUND, bg3.SPEAKER_DURGE, '0.0', phase_duration, (), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.SOUND, bg3.SPEAKER_DURGE, '0.0', phase_duration, (
        t.create_sound_event_key('5.52', sound_event_id = 'd0756d07-fd81-4fab-b4af-03d565c7f059', sound_object_index = 4),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.SOUND, bg3.SPEAKER_DURGE, '0.0', phase_duration, (
        t.create_sound_event_key('8.74', sound_type = 4, foley_type = 2),
    ), is_snapped_to_end = True)

    t.create_tl_actor_node(bg3.timeline_object.SOUND, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.SOUND, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_sound_event_key('12.07', sound_event_id = '50ab7087-b822-455f-9a61-6b10b6e6d968', sound_object_index = 4),
        t.create_sound_event_key('19.2482', sound_event_id = '220abafa-e55f-4124-8cb7-16fca63fda5f', sound_object_index = 4),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.SOUND, bg3.SPEAKER_DURGE, '0.0', phase_duration, (), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.SOUND, bg3.SPEAKER_DURGE, '0.0', phase_duration, (
        t.create_sound_event_key('5.5', sound_event_id = 'c232329e-2d4e-4f0c-a4d4-ea1585fce27c', sound_object_index = 4),
        t.create_sound_event_key('7.05', sound_event_id = 'aa8db628-8c78-4632-ab7a-2ac210393e93', sound_object_index = 4),
        t.create_sound_event_key('8.745', sound_event_id = '220abafa-e55f-4124-8cb7-16fca63fda5f', sound_object_index = 4),
        t.create_sound_event_key('24.27', sound_event_id = '220abafa-e55f-4124-8cb7-16fca63fda5f', sound_object_index = 4),
    ), is_snapped_to_end = True)

    # Kiss part
    t.create_tl_actor_node(bg3.timeline_object.SOUND, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_sound_event_key('29.73', sound_event_id = '3a82ed81-3970-461a-91dc-4687caa05cce', sound_object_index = 1),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.SOUND, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_sound_event_key('38.29', sound_event_id = '90a31a12-9f32-47e1-899e-cdced0705f27', sound_object_index = 4),
        t.create_sound_event_key('38.35', sound_event_id = '025fa6be-55ec-43fe-af6a-03b746163d72', sound_object_index = 4),
        t.create_sound_event_key('38.96', sound_event_id = 'ffbbbd57-5c31-444d-bc3a-c3d14df0be53', sound_object_index = 4),
        t.create_sound_event_key('43.49', sound_event_id = 'ffbbbd57-5c31-444d-bc3a-c3d14df0be53', sound_object_index = 4),
        t.create_sound_event_key('45.83', sound_event_id = '5dac329f-b08a-412d-84bc-86fc1aecae45', sound_object_index = 4),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.SOUND, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_sound_event_key('31.11', sound_event_id = '3a82ed81-3970-461a-91dc-4687caa05cce', sound_object_index = 2),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.SOUND, bg3.SPEAKER_DURGE, '0.0', phase_duration, (
        t.create_sound_event_key('41.19', sound_event_id = 'ffbbbd57-5c31-444d-bc3a-c3d14df0be53', sound_object_index = 4),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.SOUND, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (), is_snapped_to_end = True)

    # Physics
    t.create_tl_actor_node(bg3.timeline_object.PHYSICS, bg3.SPEAKER_DURGE, '0.0', phase_duration, (
        t.create_value_key(time = 0.0, interpolation_type = 3, value_name = 'InverseKinematics', value = False),
        t.create_value_key(time = '28.81', interpolation_type = 3),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.PHYSICS, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_value_key(time = 0.0, interpolation_type = 3, value_name = 'InverseKinematics', value = False),
        t.create_value_key(time = '28.81', interpolation_type = 3),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.HANDS_IK, bg3.SPEAKER_DURGE, '0.0', phase_duration, (), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.HANDS_IK, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (), is_snapped_to_end = True)

    t.create_tl_animation(
        bg3.SPEAKER_SHADOWHEART, '0.0', '16.97',
        'a70b0572-f371-49e6-854b-a8347e5db74a',
        '39e8f7e2-e600-47a8-a5c2-204b1ac9a5a7',
        fade_in = 2.0,
        fade_out = 0.0)
    t.create_tl_animation(
        bg3.SPEAKER_DURGE, '0.0', '16.97',
        'a0f79aae-f6c9-4b19-d854-3153658a1da2',
        '6ef6e0ea-2ae3-46d9-8464-99aa9ba8e427',
        fade_in = 2.0,
        fade_out = 0.0)

    t.create_tl_transform(bg3.SPEAKER_DURGE, '0.0', phase_duration, (
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = -8.0),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 0.0),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = -0.83),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = (0.0, 1.0, 0.0, 0.0)),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 1),
        ),
        (),
    ), is_snapped_to_end = True)
    t.create_tl_transform(bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = -8.0),
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
    ))

    # Camera shot 1
    t.create_tl_shot('d35b098e-8c34-45ee-9dde-21adfd2410a9', '0.0', '2.2')
    t.create_tl_camera_fov('d35b098e-8c34-45ee-9dde-21adfd2410a9', '0.0', '2.2', (
        t.create_value_key(time = 0.0, value_name = 'FoV', value = 35.0, interpolation_type = 2),
    ))
    t.create_tl_transform('d35b098e-8c34-45ee-9dde-21adfd2410a9', '0.0', '2.2', (
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = -7.5),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 1.8),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 0.2),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = bg3.euler_to_quaternion(-154.0, 0.0, 0.0, sequence = 'yxz')),
        ),
        (),
        (),
    ))

    # Camera shot 2
    t.create_tl_shot('d35b098e-8c34-45ee-9dde-21adfd2410a9', '2.2', '4.2')
    t.create_tl_camera_fov('d35b098e-8c34-45ee-9dde-21adfd2410a9', '2.2', '4.2', (
        t.create_value_key(time = '2.2', value_name = 'FoV', value = 25.0, interpolation_type = 2),
    ))
    t.create_tl_transform('d35b098e-8c34-45ee-9dde-21adfd2410a9', '2.2', '4.2', (
        (
            t.create_value_key(time = '2.2', interpolation_type = 5, value = -6.5),
        ),
        (
            t.create_value_key(time = '2.2', interpolation_type = 5, value = 1.8),
        ),
        (
            t.create_value_key(time = '2.2', interpolation_type = 5, value = -1.0),
        ),
        (
            t.create_value_key(time = '2.2', interpolation_type = 5, value = bg3.euler_to_quaternion(-62.0, 0.0, 0.0, sequence = 'yxz')),
        ),
        (),
        (),
    ))


    """
    t.create_tl_transform('a6db4283-ef38-4472-827c-fffd0ac04a28', '0.0', phase_duration, (
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = -10.0),
            t.create_value_key(time = phase_duration, interpolation_type = 5, value = -9.7),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 1.8),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = -0.1),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = (0.0, 0.707071, '0.0', 0.707071)),
            t.create_value_key(time = phase_duration, interpolation_type = 5, value = (0.0, 0.7081, '0.0', 0.7061)),
        ),
        (),
        (),
    ))
    t.create_tl_camera_fov('d35b098e-8c34-45ee-9dde-21adfd2410a9', '0.0', phase_duration, (
        t.create_value_key(time = 0.0, value_name = 'FoV', value = 50.0, interpolation_type = 2),
    ), is_snapped_to_end = True)

    t.create_tl_shot('d35b098e-8c34-45ee-9dde-21adfd2410a9', '0.0', phase_duration, disable_conditional_staging = True)
    #t.create_tl_shot('a6db4283-ef38-4472-827c-fffd0ac04a28', 16.5, phase_duration, disable_conditional_staging = True)
    """

    # Camera shot 3
    t.create_tl_shot('d35b098e-8c34-45ee-9dde-21adfd2410a9', '4.2', '8.74')
    t.create_tl_camera_fov('d35b098e-8c34-45ee-9dde-21adfd2410a9', '4.2', '8.74', (
        t.create_value_key(time = '4.2', value_name = 'FoV', value = 15.0, interpolation_type = 2),
    ))
    t.create_tl_transform('d35b098e-8c34-45ee-9dde-21adfd2410a9', '4.2', '8.74', (
        (
            t.create_value_key(time = '4.2', interpolation_type = 5, value = -6.0),
        ),
        (
            t.create_value_key(time = '4.2', interpolation_type = 5, value = 2.0),
        ),
        (
            t.create_value_key(time = '4.2', interpolation_type = 5, value = -0.7),
        ),
        (
            t.create_value_key(time = '4.2', interpolation_type = 5, value = bg3.euler_to_quaternion(-74.0, 10.0, 0.0, sequence = 'yxz')),
        ),
        (),
        (),
    ))

    t.create_tl_animation(
        bg3.SPEAKER_SHADOWHEART, '4.58', '8.74',
        'a0e37a8e-c619-4d0a-840a-061831fb0523',
        '16c31857-6247-46a5-9182-28926409bcaf',
        animation_slot = 1,
        animation_play_rate = 0.6,
        animation_play_start_offset = 3.5,
        fade_in = 1.76,
        fade_out = 2.3)
    t.create_tl_animation(
        bg3.SPEAKER_DURGE, '4.58', '8.74',
        'a0e37a8e-c619-4d0a-840a-061831fb0523',
        '1913a5ea-cbf7-491b-bf3e-34c829ac69dd',
        animation_slot = 1,
        animation_play_rate = 0.6,
        animation_play_start_offset = 3.5,
        fade_in = 1.76,
        fade_out = 2.3)

    # Camera shot 4
    t.create_tl_shot('d35b098e-8c34-45ee-9dde-21adfd2410a9', '8.74', '12.07')
    t.create_tl_camera_fov('d35b098e-8c34-45ee-9dde-21adfd2410a9', '8.74', '12.07', (
        t.create_value_key(time = '8.74', value_name = 'FoV', value = 25.0, interpolation_type = 2),
    ))
    t.create_tl_transform('d35b098e-8c34-45ee-9dde-21adfd2410a9', '8.74', '12.07', (
        (
            t.create_value_key(time = '8.74', interpolation_type = 5, value = -10.0),
        ),
        (
            t.create_value_key(time = '8.74', interpolation_type = 5, value = 1.8),
        ),
        (
            t.create_value_key(time = '8.74', interpolation_type = 5, value = -0.1),
        ),
        (
            t.create_value_key(time = '8.74', interpolation_type = 5, value = bg3.euler_to_quaternion(90.0, 0.0, 0.0, sequence = 'yxz')),
        ),
        (),
        (),
    ))

    t.create_tl_animation(
        bg3.SPEAKER_SHADOWHEART, '9.86', '10.56',
        'a0e37a8e-c619-4d0a-840a-061831fb0523',
        '16c31857-6247-46a5-9182-28926409bcaf',
        animation_slot = 1,
        animation_play_rate = 0.6,
        animation_play_start_offset = 3,
        fade_in = 0.25)

    # Camera shot 5
    t.create_tl_shot('d35b098e-8c34-45ee-9dde-21adfd2410a9', '12.07', '16.97')
    t.create_tl_camera_fov('d35b098e-8c34-45ee-9dde-21adfd2410a9', '12.07', '16.97', (
        t.create_value_key(time = '12.07', value_name = 'FoV', value = 40.0, interpolation_type = 2),
    ))
    t.create_tl_transform('d35b098e-8c34-45ee-9dde-21adfd2410a9', '12.07', '16.97', (
        (
            t.create_value_key(time = '12.07', interpolation_type = 5, value = -8.9),
        ),
        (
            t.create_value_key(time = '12.07', interpolation_type = 5, value = 1.8),
        ),
        (
            t.create_value_key(time = '12.07', interpolation_type = 5, value = 0.4),
        ),
        (
            t.create_value_key(time = '12.07', interpolation_type = 5, value = bg3.euler_to_quaternion(115.0, 10.0, 0.0, sequence = 'yxz')),
        ),
        (),
        (),
    ))

    t.create_tl_animation(
        bg3.SPEAKER_SHADOWHEART, '14.43', '16.97',
        'c26b9b0a-20cc-44a4-a499-18d6d78abec5',
        '16c31857-6247-46a5-9182-28926409bcaf',
        animation_slot = 1,
        animation_play_start_offset = 10.18,
        fade_in = 1,
        fade_out = 0)

    # Camera shot 6
    t.create_tl_shot('d35b098e-8c34-45ee-9dde-21adfd2410a9', '16.97', '24.27')
    t.create_tl_camera_fov('d35b098e-8c34-45ee-9dde-21adfd2410a9', '16.97', '24.27', (
        t.create_value_key(time = '16.97', value_name = 'FoV', value = 40.0, interpolation_type = 2),
    ))
    t.create_tl_transform('d35b098e-8c34-45ee-9dde-21adfd2410a9', '16.97', '24.27', (
        (
            t.create_value_key(time = '16.97', interpolation_type = 5, value = -7.1),
        ),
        (
            t.create_value_key(time = '16.97', interpolation_type = 5, value = 1.6),
        ),
        (
            t.create_value_key(time = '16.97', interpolation_type = 5, value = 0.2),
        ),
        (
            t.create_value_key(time = '16.97', interpolation_type = 5, value = bg3.euler_to_quaternion(-117.0, 0.0, 0.0, sequence = 'yxz')),
        ),
        (),
        (),
    ))

    t.create_tl_animation(
        bg3.SPEAKER_SHADOWHEART, '16.97', '28.81',
        'a70b0572-f371-49e6-854b-a8347e5db74a',
        '39e8f7e2-e600-47a8-a5c2-204b1ac9a5a7',
        animation_play_start_offset = 14.0,
        fade_in = 0.0,
        fade_out = 0.0)
    t.create_tl_animation(
        bg3.SPEAKER_DURGE, '16.97', '28.81',
        'a0f79aae-f6c9-4b19-d854-3153658a1da2',
        '6ef6e0ea-2ae3-46d9-8464-99aa9ba8e427',
        animation_play_start_offset = 14.0,
        fade_in = 0.0,
        fade_out = 0.0)

    t.create_tl_animation(
        bg3.SPEAKER_SHADOWHEART, '18.68', '24.27',
        'c26b9b0a-20cc-44a4-a499-18d6d78abec5',
        '16c31857-6247-46a5-9182-28926409bcaf',
        animation_slot = 1,
        animation_play_rate = 0.2,
        animation_play_start_offset = 3,
        fade_in = 2,
        fade_out = 2.3)

    # Camera shot 7
    t.create_tl_shot('d35b098e-8c34-45ee-9dde-21adfd2410a9', '24.27', '27.205')
    t.create_tl_camera_fov('d35b098e-8c34-45ee-9dde-21adfd2410a9', '24.27', '27.205', (
        t.create_value_key(time = '24.27', value_name = 'FoV', value = 40.0, interpolation_type = 2),
    ), is_snapped_to_end = True)
    t.create_tl_transform('d35b098e-8c34-45ee-9dde-21adfd2410a9', '24.27', '27.205', (
        (
            t.create_value_key(time = '24.27', interpolation_type = 5, value = -7.3),
        ),
        (
            t.create_value_key(time = '24.27', interpolation_type = 5, value = 1.7),
        ),
        (
            t.create_value_key(time = '24.27', interpolation_type = 5, value = -0.8),
        ),
        (
            t.create_value_key(time = '24.27', interpolation_type = 5, value = bg3.euler_to_quaternion(-47.0, 0.0, 0.0, sequence = 'yxz')),
        ),
        (),
        (),
    ))

    # Camera shot 8
    t.create_tl_shot('d35b098e-8c34-45ee-9dde-21adfd2410a9', '27.205', '28.81')
    t.create_tl_camera_fov('d35b098e-8c34-45ee-9dde-21adfd2410a9', '27.205', '28.81', (
        t.create_value_key(time = '27.205', value_name = 'FoV', value = 40.0, interpolation_type = 2),
    ), is_snapped_to_end = True)
    t.create_tl_transform('d35b098e-8c34-45ee-9dde-21adfd2410a9', '27.205', '28.81', (
        (
            t.create_value_key(time = '27.205', interpolation_type = 5, value = -9.2),
        ),
        (
            t.create_value_key(time = '27.205', interpolation_type = 5, value = 1.5),
        ),
        (
            t.create_value_key(time = '27.205', interpolation_type = 5, value = -0.4),
        ),
        (
            t.create_value_key(time = '27.205', interpolation_type = 5, value = bg3.euler_to_quaternion(84.0, 0.0, 0.0, sequence = 'yxz')),
        ),
        (),
        (),
    ))

    """
    t.create_tl_animation(
        bg3.SPEAKER_SHADOWHEART, '28.81', 30.68,
        'aee45eec-5852-9b69-1863-d5ec33bd21f0',
        '39e8f7e2-e600-47a8-a5c2-204b1ac9a5a7',
        animation_play_start_offset = 32.0,
        animation_play_rate = 0.8,
        fade_in = 0.0,
        fade_out = 2.0)
    t.create_tl_animation(
        bg3.SPEAKER_DURGE, '28.81', 30.68,
        'a0f79aae-f6c9-4b19-d854-3153658a1da2',
        '6ef6e0ea-2ae3-46d9-8464-99aa9ba8e427',
        animation_play_start_offset = 32.0,
        animation_play_rate = 0.8,
        fade_in = 0.0,
        fade_out = 2.0)

    # Camera shot 9
    t.create_tl_shot('a6db4283-ef38-4472-827c-fffd0ac04a28', '28.81', 30.68, is_snapped_to_end = True)
    t.create_tl_camera_fov('a6db4283-ef38-4472-827c-fffd0ac04a28', '28.81', 30.68, (
        t.create_value_key(time = '28.81', value_name = 'FoV', value = 30.0, interpolation_type = 2),
    ), is_snapped_to_end = True)
    t.create_tl_transform('a6db4283-ef38-4472-827c-fffd0ac04a28', '28.81', 30.68, (
        (
            #t.create_value_key(time = '28.81', interpolation_type = 5, value = -7.5),
            t.create_value_key(time = '28.81', interpolation_type = 5, value = -7.3),
        ),
        (
            t.create_value_key(time = '28.81', interpolation_type = 5, value = 1.5),
        ),
        (
            t.create_value_key(time = '28.81', interpolation_type = 5, value = -0.9),
        ),
        (
            #t.create_value_key(time = '28.81', interpolation_type = 5, value = bg3.euler_to_quaternion(0.0, 0.0, 0.0, sequence = 'yxz')),
            t.create_value_key(time = '28.81', interpolation_type = 5, value = bg3.euler_to_quaternion(-35.0, 0.0, 0.0, sequence = 'yxz')),
        ),
        (),
        (),
    ))

    """
    # 61.5 --> 28.81 - 3.1 = 25.71; rel diff -35.79
    # Camera shot 10
    t.create_tl_shot('a6db4283-ef38-4472-827c-fffd0ac04a28', '28.81', '33.22')
    t.create_tl_camera_fov('a6db4283-ef38-4472-827c-fffd0ac04a28', '28.81', '33.22', (
        t.create_value_key(time = '28.81', value_name = 'FoV', value = 30.0, interpolation_type = 2),
    ))
    t.create_tl_transform('a6db4283-ef38-4472-827c-fffd0ac04a28', '28.81', '33.22', (
        (
            t.create_value_key(time = '28.81', interpolation_type = 5, value = -7.5),
        ),
        (
            t.create_value_key(time = '28.81', interpolation_type = 5, value = 1.8),
        ),
        (
            t.create_value_key(time = '28.81', interpolation_type = 5, value = -1.2),
        ),
        (
            t.create_value_key(time = '28.81', interpolation_type = 5, value = bg3.euler_to_quaternion(-34.0, 5.0, 0.0, sequence = 'yxz')),
        ),
        (),
        (),
    ))

    t.create_tl_animation(
        bg3.SPEAKER_SHADOWHEART, '28.81', '33.22',
        '91239d58-cd15-1201-a029-a685b6434723',
        '66ce0c11-1cdb-4573-818c-a91cde00f79f',
        animation_play_start_offset = 3.1,
        fade_in = 0.0,
        fade_out = 0.0
    )
    t.create_tl_animation(
        bg3.SPEAKER_DURGE, '28.81', '33.22',
        'ee52d6f6-543f-454d-93d8-71b74ff5ac12',
        '57fa3dc0-184f-4b43-93fd-86e5496448a9',
        animation_play_start_offset = 3.1,
        fade_in = 1.5,
        fade_out = 0.0
    )

    # Camera shot 11
    t.create_tl_shot('a6db4283-ef38-4472-827c-fffd0ac04a28', '33.22', '36.2')
    t.create_tl_camera_fov('a6db4283-ef38-4472-827c-fffd0ac04a28', '33.22', '36.2', (
        t.create_value_key(time = '33.22', value_name = 'FoV', value = 25.0, interpolation_type = 2),
    ))
    t.create_tl_transform('a6db4283-ef38-4472-827c-fffd0ac04a28', '33.22', '36.2', (
        (
            t.create_value_key(time = '33.22', interpolation_type = 5, value = -8.5),
        ),
        (
            t.create_value_key(time = '33.22', interpolation_type = 5, value = 1.9),
        ),
        (
            t.create_value_key(time = '33.22', interpolation_type = 5, value = -0.8),
        ),
        (
            #t.create_value_key(time = '33.22', interpolation_type = 5, value = bg3.euler_to_quaternion(54.0, 10.0, 0.0, sequence = 'yxz')),
            t.create_value_key(time = '33.22', interpolation_type = 5, value = bg3.euler_to_quaternion(62.0, 12.0, 0.0, sequence = 'yxz')),
        ),
        (),
        (),
    ))

    t.create_tl_animation(
        bg3.SPEAKER_SHADOWHEART, '33.22', '36.2',
        '91239d58-cd15-1201-a029-a685b6434723',
        '66ce0c11-1cdb-4573-818c-a91cde00f79f',
        animation_play_start_offset = 7.01,
        fade_in = 0.0,
        fade_out = 0.0
    )
    t.create_tl_animation(
        bg3.SPEAKER_DURGE, '33.22', '36.2',
        'ee52d6f6-543f-454d-93d8-71b74ff5ac12',
        '57fa3dc0-184f-4b43-93fd-86e5496448a9',
        animation_play_start_offset = 7.01,
        fade_in = 0.0,
        fade_out = 0.0
    )

    t.create_tl_voice(
        bg3.SPEAKER_SHADOWHEART, '34.127', '36.0',
        bt2_reaction_node_uuid,
        performance_fade = 0.0,
        fade_in = 0.0,
        fade_out = 0.0)

    # Camera shot 12
    t.create_tl_shot('a6db4283-ef38-4472-827c-fffd0ac04a28', '36.2', '41.49', is_snapped_to_end = True)
    t.create_tl_camera_fov('a6db4283-ef38-4472-827c-fffd0ac04a28', '36.2', '41.49', (
        t.create_value_key(time = 0.0, value_name = 'FoV', value = 25.0, interpolation_type = 2),
    ))
    t.create_tl_transform('a6db4283-ef38-4472-827c-fffd0ac04a28', '36.2', '41.49', (
        (
            t.create_value_key(time = '36.2', interpolation_type = 5, value = -9.0),
        ),
        (
            t.create_value_key(time = '36.2', interpolation_type = 5, value = 1.8),
        ),
        (
            t.create_value_key(time = '36.2', interpolation_type = 5, value = -0.6),
        ),
        (
            t.create_value_key(time = '36.2', interpolation_type = 5, value = bg3.euler_to_quaternion(86.0, 4.0, 0.0, sequence = 'yxz')),
        ),
        (),
        (),
    ))

    t.create_tl_animation(
        bg3.SPEAKER_SHADOWHEART, '36.2', phase_duration, #56.22,
        '91239d58-cd15-1201-a029-a685b6434723',
        '66ce0c11-1cdb-4573-818c-a91cde00f79f',
        animation_play_start_offset = 11.91,
        fade_in = 0.0,
        fade_out = 2.0
    )
    t.create_tl_animation(
        bg3.SPEAKER_DURGE, '36.2', phase_duration, #56.22,
        'ee52d6f6-543f-454d-93d8-71b74ff5ac12',
        '57fa3dc0-184f-4b43-93fd-86e5496448a9',
        animation_play_start_offset = 11.91,
        fade_in = 0.0,
        fade_out = 1.0
    )

    t.create_tl_animation(
        bg3.SPEAKER_SHADOWHEART, '37.54', '41.49',
        'c26b9b0a-20cc-44a4-a499-18d6d78abec5',
        '536f3ddd-33e5-4b9d-a20a-b7109f6bbc76',
        animation_slot = 1,
        animation_play_start_offset = 6.62,
        fade_in = 1.6,
        fade_out = 0.0
    )
    t.create_tl_animation(
        bg3.SPEAKER_DURGE, '37.92', '41.49',
        'c26b9b0a-20cc-44a4-a499-18d6d78abec5',
        '90070425-bce3-4bef-b8d7-ca38a676b5cb',
        animation_slot = 1,
        animation_play_start_offset = 7,
        fade_in = 1.5,
        fade_out = 0.0
    )

    t.create_tl_animation(
        bg3.SPEAKER_DURGE, '41.49', '47.14',
        'c26b9b0a-20cc-44a4-a499-18d6d78abec5',
        '90070425-bce3-4bef-b8d7-ca38a676b5cb',
        animation_slot = 1,
        animation_play_start_offset = 3.5,
        fade_in = 0.0,
        fade_out = 1.5
    )
    t.create_tl_animation(
        bg3.SPEAKER_SHADOWHEART, '41.49', '47.14',
        'c26b9b0a-20cc-44a4-a499-18d6d78abec5',
        '536f3ddd-33e5-4b9d-a20a-b7109f6bbc76',
        animation_slot = 1,
        animation_play_start_offset = 3.5,
        fade_in = 0.0,
        fade_out = 1.5
    )

    # Camera shot 13
    t.create_tl_shot('a6db4283-ef38-4472-827c-fffd0ac04a28', '41.49', phase_duration, is_snapped_to_end = True)
    t.create_tl_camera_fov('a6db4283-ef38-4472-827c-fffd0ac04a28', '41.49', phase_duration, (
        t.create_value_key(time = '41.49', value_name = 'FoV', value = 30.0, interpolation_type = 2),
    ))
    t.create_tl_transform('a6db4283-ef38-4472-827c-fffd0ac04a28', '41.49', phase_duration, (
        (
            t.create_value_key(time = '41.49', interpolation_type = 5, value = -7.1),
        ),
        (
            t.create_value_key(time = '41.49', interpolation_type = 5, value = 1.75),
        ),
        (
            t.create_value_key(time = '41.49', interpolation_type = 5, value = -1.1),
        ),
        (
            t.create_value_key(time = '41.49', interpolation_type = 5, value = bg3.euler_to_quaternion(-60.0, 0.0, 0.0, sequence = 'yxz')),
        ),
        (),
        (),
    ), is_snapped_to_end = True)


    # Camera shot 14
    # t.create_tl_shot('a6db4283-ef38-4472-827c-fffd0ac04a28', '53.22', 56.22, is_snapped_to_end = True)
    # t.create_tl_camera_fov('a6db4283-ef38-4472-827c-fffd0ac04a28', '53.22', 56.22, (
    #     t.create_value_key(time = 53.22, value_name = 'FoV', value = 32.0, interpolation_type = 2),
    # ))
    # t.create_tl_transform('a6db4283-ef38-4472-827c-fffd0ac04a28', '53.22', 56.22, (
    #     (
    #         t.create_value_key(time = 53.22, interpolation_type = 5, value = -8.5),
    #     ),
    #     (
    #         t.create_value_key(time = 53.22, interpolation_type = 5, value = 1.75),
    #     ),
    #     (
    #         t.create_value_key(time = 53.22, interpolation_type = 5, value = -0.5),
    #     ),
    #     (
    #         #t.create_value_key(time = 53.22, interpolation_type = 5, value = bg3.euler_to_quaternion(65.0, 0.0, 0.0, sequence = 'yxz')),
    #         t.create_value_key(time = 53.22, interpolation_type = 5, value = bg3.euler_to_quaternion(45.0, 0.0, 0.0, sequence = 'yxz')),
    #     ),
    #     (),
    #     (),
    # ))


#################################################################################################
# Body type 2 gith
#################################################################################################

def create_scene_shadowheart_reaction_body_type_2_gith() -> None:

    # d = bg3.dialog_object(files.get_file('Gustav', 'Mods/GustavDev/Story/DialogsBinary/Act3/LowerCity/BhaalTemple/LOW_BhaalTemple_PostBattleDarkUrge_Resistance.lsf'))
    # t = bg3.timeline_object(files.get_file('Gustav', 'Public/GustavDev/Timeline/Generated/LOW_BhaalTemple_PostBattleDarkUrge_Resistance.lsf'), d)

    ab = game_assets.get_modded_dialog_asset_bundle('LOW_BhaalTemple_PostBattleDarkUrge_Resistance')
    d = bg3.dialog_object(ab.dialog)
    t = bg3.timeline_object(ab.timeline, d)

    slot_idx_durge = d.get_speaker_slot_index(bg3.SPEAKER_DURGE)
    #slot_idx_shadowheart = d.get_speaker_slot_index(bg3.SPEAKER_SHADOWHEART)

    # d.create_cinematic_dialog_node(
    #     normal_body_reaction_node_uuid,
    #     [just_keep_safe_out_there_node_uuid])
    d.create_standard_dialog_node(
        bt2_gith_reaction_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [just_keep_safe_out_there_node_uuid],
        bg3.text_content('hd896e304g5fc4g41e7g807cg524360fee6a9', 1),
        checkflags = (
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_GITH, True, slot_idx_durge),
            )),
        )
    )

    phase_duration = '55.42' # '53.22' # 54.42 # 56.22
    t.create_new_phase(bt2_gith_reaction_node_uuid, phase_duration)

    t.create_tl_actor_node(bg3.timeline_object.ATTITUDE, bg3.SPEAKER_DURGE, '0.0', phase_duration, (
        t.create_attitude_key(12.15, bg3.ATTITUDE_DIAG_Pose_Stand_R_Forward_01, bg3.ATTITUDE_DIAG_T_Pose),
        t.create_attitude_key(28.81, 'a2bd89b1-8ab9-4231-ac4b-e593d75aa083', bg3.ATTITUDE_DIAG_T_Pose),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.ATTITUDE, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_attitude_key(0.0, bg3.ATTITUDE_DIAG_Pose_Stand_L_Forward_01, bg3.ATTITUDE_DIAG_T_Pose),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.EMOTION, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_emotion_key(0.0, 32),
        t.create_emotion_key(6.13, 32, variation = 2),
        t.create_emotion_key(7.34, 32),
        t.create_emotion_key(15.63, 32, variation = 1),
        t.create_emotion_key(20.58, 32),
        t.create_emotion_key(44.85, 32, variation = 1, is_sustained = False),
        t.create_emotion_key(51.97, 32)
        #t.create_emotion_key(26.0, 2)
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.EMOTION, bg3.SPEAKER_DURGE, '0.0', phase_duration, (
        t.create_emotion_key(0.0, 32, variation = 1),
        t.create_emotion_key(3.51, 32),
        t.create_emotion_key(6.08, 32, variation = 1),
        t.create_emotion_key(6.56, 32),
        t.create_emotion_key(8.26, 32, variation = 2),
        t.create_emotion_key(11.26, 32, variation = 1),
        t.create_emotion_key(22.03, 32),
        t.create_emotion_key(40.14, 256),
        t.create_emotion_key(44.85, 32),
    ), is_snapped_to_end = True)
    #t.create_tl_actor_node(bg3.timeline_object.EMOTION, bg3.SPEAKER_JERGAL, '0.0', phase_duration, (
    #    t.create_emotion_key(0.0, 1, None),
    #    t.create_emotion_key(25.5, 2, variation = 2),
    #), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.LOOK_AT, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_look_at_key(
            0.0,
            target = bg3.SPEAKER_DURGE,
            bone = 'Head_M',
            turn_mode = 3,
            turn_speed_multiplier = 0.3,
            torso_turn_speed_multiplier = 0.3,
            head_turn_speed_multiplier = 0.3,
            weight = 0.0,
            reset = True,
            eye_look_at_bone = 'Head_M'),
        t.create_look_at_key(
            '4.20',
            target = bg3.SPEAKER_DURGE,
            bone = 'Head_M',
            turn_mode = 3,
            turn_speed_multiplier = 0.3,
            torso_turn_speed_multiplier = 0.3,
            head_turn_speed_multiplier = 0.3,
            weight = 0.3,
            safe_zone_angle = 80.0,
            head_safe_zone_angle = 80.0,
            reset = True,
            look_at_mode = 1,
            eye_look_at_bone = 'Head_M'),
        t.create_look_at_key(
            '9.41',
            turn_mode = 3,
            turn_speed_multiplier = 0.26370612,
            torso_turn_speed_multiplier = 0.26370612,
            head_turn_speed_multiplier = 0.26370612,
            weight = 0.3,
            safe_zone_angle = 80.0,
            head_safe_zone_angle = 80.0,
            look_at_mode = 0),
        t.create_look_at_key(
            '24.27',
            target = bg3.SPEAKER_DURGE,
            bone = 'Head_M',
            turn_mode = 3,
            turn_speed_multiplier = 0.3,
            torso_turn_speed_multiplier = 0.3,
            head_turn_speed_multiplier = 0.3,
            weight = 0.0,
            safe_zone_angle = 80.0,
            head_safe_zone_angle = 80.0,
            reset = True,
            look_at_mode = 1,
            eye_look_at_bone = 'Head_M'),
        t.create_look_at_key(
            '28.81',
            target = bg3.SPEAKER_DURGE,
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
    t.create_tl_actor_node(bg3.timeline_object.LOOK_AT, bg3.SPEAKER_DURGE, '0.0', phase_duration, (
        t.create_look_at_key(
            0.0,
            target = bg3.SPEAKER_SHADOWHEART,
            bone = 'Head_M',
            turn_mode = 3,
            turn_speed_multiplier = 0.3,
            torso_turn_speed_multiplier = 0.3,
            head_turn_speed_multiplier = 0.21843724,
            weight = 0.0,
            safe_zone_angle = 80.0,
            head_safe_zone_angle = 80.0,
            look_at_mode = 1,
            eye_look_at_bone = 'Head_M'),
        t.create_look_at_key(
            '4.20',
            turn_mode = 3,
            turn_speed_multiplier = 0.3,
            torso_turn_speed_multiplier = 0.3,
            head_turn_speed_multiplier = 0.1,
            weight = 0.0,
            safe_zone_angle = 80.0,
            head_safe_zone_angle = 80.0,
            look_at_mode = 0),
        t.create_look_at_key(
            '6.56',
            target = bg3.SPEAKER_SHADOWHEART,
            bone = 'Head_M',
            turn_mode = 3,
            turn_speed_multiplier = 0.3269225,
            torso_turn_speed_multiplier = 0.3269225,
            head_turn_speed_multiplier = 0.10897417,
            weight = 0.0,
            safe_zone_angle = 80.0,
            head_safe_zone_angle = 80.0,
            look_at_mode = 1,
            eye_look_at_bone = 'Head_M'),
        t.create_look_at_key(
            '9.4',
            turn_mode = 3,
            turn_speed_multiplier = 0.25471807,
            torso_turn_speed_multiplier = 0.25471807,
            head_turn_speed_multiplier = 0.08490602,
            weight = 0.0,
            safe_zone_angle = 80.0,
            head_safe_zone_angle = 80.0,
            look_at_mode = 0),
        t.create_look_at_key(
            '24.27',
            target = bg3.SPEAKER_SHADOWHEART,
            bone = 'Head_M',
            turn_mode = 3,
            turn_speed_multiplier = 0.3,
            torso_turn_speed_multiplier = 0.3,
            head_turn_speed_multiplier = 0.1,
            weight = 0.0,
            safe_zone_angle = 80.0,
            head_safe_zone_angle = 80.0,
            reset = True,
            look_at_mode = 1,
            eye_look_at_bone = 'Head_M'),
        t.create_look_at_key(
            '28.81',
            target = bg3.SPEAKER_SHADOWHEART,
            bone = 'Head_M',
            turn_mode = 3,
            turn_speed_multiplier = 0.3,
            head_turn_speed_multiplier = 0.1,
            weight = 0.0,
            safe_zone_angle = 80.0,
            head_safe_zone_angle = 80.0,
            look_at_mode = 1,
            eye_look_at_bone = 'Head_M'),
    ), is_snapped_to_end = True)

    t.create_tl_material(bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, '156a2490-d796-402c-b7fc-e00c032042c1', (), (
        t.create_value_key(time = 0.0, value = True),
    ), is_snapped_to_end = True, is_continuous = True)

    # Hide helmets
    t.create_tl_show_armor(bg3.SPEAKER_DURGE, '0.0', phase_duration, (
        (
            t.create_value_key(time = 0.0, value = False, interpolation_type = 0),
            t.create_value_key(time = phase_duration, interpolation_type = 0)
        ),
        (), (), (), (), (), (), (), (), (), ()
    ))
    t.create_tl_show_armor(bg3.SPEAKER_SHADOWHEART, '0.0',  phase_duration, (
        (
            t.create_value_key(time = 0.0, value = False, interpolation_type = 0),
            t.create_value_key(time = phase_duration, interpolation_type = 0)
        ),
        (), (), (), (), (), (), (), (), (), ()
    ))

    # Hide weapons
    t.create_tl_actor_node(bg3.timeline_object.SHOW_WEAPON, bg3.SPEAKER_DURGE, '0.0', phase_duration, (
        t.create_value_key(time = 0.0, value_name = 'ShowWeapon', value = False, interpolation_type = 3),
        t.create_value_key(time = phase_duration, interpolation_type = 3),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.SHOW_WEAPON, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_value_key(time = 0.0, value_name = 'ShowWeapon', value = False, interpolation_type = 3),
        t.create_value_key(time = phase_duration, interpolation_type = 3),
    ), is_snapped_to_end = True)

    # Show Durge
    t.create_tl_actor_node(bg3.timeline_object.SHOW_VISUAL, bg3.SPEAKER_DURGE, '0.0', phase_duration, (
        t.create_value_key(time = 0.0, interpolation_type = 3),
    ), is_snapped_to_end = True)

    # Sounds
    # Hug part
    t.create_tl_actor_node(bg3.timeline_object.SOUND, bg3.SPEAKER_DURGE, '0.0', phase_duration, (), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.SOUND, bg3.SPEAKER_DURGE, '0.0', phase_duration, (
        t.create_sound_event_key('5.52', sound_event_id = 'd0756d07-fd81-4fab-b4af-03d565c7f059', sound_object_index = 4),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.SOUND, bg3.SPEAKER_DURGE, '0.0', phase_duration, (
        t.create_sound_event_key('8.74', sound_type = 4, foley_type = 2),
    ), is_snapped_to_end = True)

    t.create_tl_actor_node(bg3.timeline_object.SOUND, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.SOUND, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_sound_event_key('12.07', sound_event_id = '50ab7087-b822-455f-9a61-6b10b6e6d968', sound_object_index = 4),
        t.create_sound_event_key('19.2482', sound_event_id = '220abafa-e55f-4124-8cb7-16fca63fda5f', sound_object_index = 4),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.SOUND, bg3.SPEAKER_DURGE, '0.0', phase_duration, (), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.SOUND, bg3.SPEAKER_DURGE, '0.0', phase_duration, (
        t.create_sound_event_key('5.5', sound_event_id = 'c232329e-2d4e-4f0c-a4d4-ea1585fce27c', sound_object_index = 4),
        t.create_sound_event_key('7.05', sound_event_id = 'aa8db628-8c78-4632-ab7a-2ac210393e93', sound_object_index = 4),
        t.create_sound_event_key('8.745', sound_event_id = '220abafa-e55f-4124-8cb7-16fca63fda5f', sound_object_index = 4),
        t.create_sound_event_key('24.27', sound_event_id = '220abafa-e55f-4124-8cb7-16fca63fda5f', sound_object_index = 4),
    ), is_snapped_to_end = True)

    # Kiss part
    t.create_tl_actor_node(bg3.timeline_object.SOUND, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_sound_event_key('29.73', sound_event_id = '3a82ed81-3970-461a-91dc-4687caa05cce', sound_object_index = 1),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.SOUND, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_sound_event_key('38.29', sound_event_id = '90a31a12-9f32-47e1-899e-cdced0705f27', sound_object_index = 4),
        t.create_sound_event_key('38.35', sound_event_id = '025fa6be-55ec-43fe-af6a-03b746163d72', sound_object_index = 4),
        t.create_sound_event_key('38.96', sound_event_id = 'ffbbbd57-5c31-444d-bc3a-c3d14df0be53', sound_object_index = 4),
        t.create_sound_event_key('43.49', sound_event_id = 'ffbbbd57-5c31-444d-bc3a-c3d14df0be53', sound_object_index = 4),
        t.create_sound_event_key('45.83', sound_event_id = '5dac329f-b08a-412d-84bc-86fc1aecae45', sound_object_index = 4),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.SOUND, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_sound_event_key('31.11', sound_event_id = '3a82ed81-3970-461a-91dc-4687caa05cce', sound_object_index = 2),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.SOUND, bg3.SPEAKER_DURGE, '0.0', phase_duration, (
        t.create_sound_event_key('41.19', sound_event_id = 'ffbbbd57-5c31-444d-bc3a-c3d14df0be53', sound_object_index = 4),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.SOUND, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (), is_snapped_to_end = True)

    # Physics
    t.create_tl_actor_node(bg3.timeline_object.PHYSICS, bg3.SPEAKER_DURGE, '0.0', phase_duration, (
        t.create_value_key(time = 0.0, interpolation_type = 3, value_name = 'InverseKinematics', value = False),
        t.create_value_key(time = '28.81', interpolation_type = 3),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.PHYSICS, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_value_key(time = 0.0, interpolation_type = 3, value_name = 'InverseKinematics', value = False),
        t.create_value_key(time = '28.81', interpolation_type = 3),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.HANDS_IK, bg3.SPEAKER_DURGE, '0.0', phase_duration, (), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.HANDS_IK, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (), is_snapped_to_end = True)

    t.create_tl_animation(
        bg3.SPEAKER_SHADOWHEART, '0.0', '16.97',
        'a70b0572-f371-49e6-854b-a8347e5db74a',
        '39e8f7e2-e600-47a8-a5c2-204b1ac9a5a7',
        fade_in = 1.0,
        fade_out = 0.0)
    t.create_tl_animation(
        bg3.SPEAKER_DURGE, '0.0', '16.97',
        'a0f79aae-f6c9-4b19-d854-3153658a1da2',
        '6ef6e0ea-2ae3-46d9-8464-99aa9ba8e427',
        fade_in = 1.0,
        fade_out = 0.0)

    t.create_tl_transform(bg3.SPEAKER_DURGE, '0.0', '4.2', (
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = -8.0),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 0.0),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = -0.83),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = (0.0, 1.0, 0.0, 0.0)),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 1),
        ),
        (),
    ), is_snapped_to_end = True)
    t.create_tl_transform(bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = -8.0),
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

    # Camera shot 1
    t.create_tl_shot('d35b098e-8c34-45ee-9dde-21adfd2410a9', '0.0', '2.2')
    t.create_tl_camera_fov('d35b098e-8c34-45ee-9dde-21adfd2410a9', '0.0', '2.2', (
        t.create_value_key(time = 0.0, value_name = 'FoV', value = 35.0, interpolation_type = 2),
    ))
    t.create_tl_transform('d35b098e-8c34-45ee-9dde-21adfd2410a9', '0.0', '2.2', (
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = -7.5),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 1.8),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 0.2),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = bg3.euler_to_quaternion(-154.0, 0.0, 0.0, sequence = 'yxz')),
        ),
        (),
        (),
    ))

    # Camera shot 2
    t.create_tl_shot('d35b098e-8c34-45ee-9dde-21adfd2410a9', '2.2', '4.2')
    t.create_tl_camera_fov('d35b098e-8c34-45ee-9dde-21adfd2410a9', '2.2', '4.2', (
        t.create_value_key(time = '0.0', value_name = 'FoV', value = 25.0, interpolation_type = 2),
    ))
    t.create_tl_transform('d35b098e-8c34-45ee-9dde-21adfd2410a9', '2.2', '4.2', (
        (
            t.create_value_key(time = '2.2', interpolation_type = 5, value = -6.5),
        ),
        (
            t.create_value_key(time = '2.2', interpolation_type = 5, value = 1.8),
        ),
        (
            t.create_value_key(time = '2.2', interpolation_type = 5, value = -1.0),
        ),
        (
            t.create_value_key(time = '2.2', interpolation_type = 5, value = bg3.euler_to_quaternion(-62.0, 0.0, 0.0, sequence = 'yxz')),
        ),
        (),
        (),
    ))


    # Camera shot 3
    t.create_tl_shot('d35b098e-8c34-45ee-9dde-21adfd2410a9', '4.2', '8.74')
    t.create_tl_camera_fov('d35b098e-8c34-45ee-9dde-21adfd2410a9', '4.2', '8.74', (
        t.create_value_key(time = '4.2', value_name = 'FoV', value = 15.0, interpolation_type = 2),
    ))
    t.create_tl_transform('d35b098e-8c34-45ee-9dde-21adfd2410a9', '4.2', '8.74', (
        (
            t.create_value_key(time = '4.2', interpolation_type = 5, value = -6.0),
        ),
        (
            t.create_value_key(time = '4.2', interpolation_type = 5, value = 2.0),
        ),
        (
            t.create_value_key(time = '4.2', interpolation_type = 5, value = -0.6),
        ),
        (
            t.create_value_key(time = '4.2', interpolation_type = 5, value = bg3.euler_to_quaternion(-74.0, 10.0, 0.0, sequence = 'yxz')),
        ),
        (),
        (),
    ))

    t.create_tl_transform(bg3.SPEAKER_DURGE, '4.2', '8.74', (
        (
            t.create_value_key(time = '4.2', interpolation_type = 5, value = -8.0),
        ),
        (
            t.create_value_key(time = '4.2', interpolation_type = 5, value = 0.03),
        ),
        (
            t.create_value_key(time = '4.2', interpolation_type = 5, value = -0.8),
        ),
        (
            t.create_value_key(time = '4.2', interpolation_type = 5, value = (0.0, 1.0, 0.0, 0.0)),
        ),
        (
            t.create_value_key(time = '4.2', interpolation_type = 5, value = 1),
        ),
        (),
    ), is_snapped_to_end = True)

    t.create_tl_animation(
        bg3.SPEAKER_SHADOWHEART, '4.58', '8.74',
        'a0e37a8e-c619-4d0a-840a-061831fb0523',
        '16c31857-6247-46a5-9182-28926409bcaf',
        animation_slot = 1,
        animation_play_rate = 0.6,
        animation_play_start_offset = 3.5,
        fade_in = 1.76,
        fade_out = 2.3)
    t.create_tl_animation(
        bg3.SPEAKER_DURGE, '4.58', '8.74',
        'a0e37a8e-c619-4d0a-840a-061831fb0523',
        '1913a5ea-cbf7-491b-bf3e-34c829ac69dd',
        animation_slot = 1,
        animation_play_rate = 0.6,
        animation_play_start_offset = 3.5,
        fade_in = 1.76,
        fade_out = 2.3)

    # Camera shot 4
    t.create_tl_shot('d35b098e-8c34-45ee-9dde-21adfd2410a9', '8.74', '12.07')
    t.create_tl_camera_fov('d35b098e-8c34-45ee-9dde-21adfd2410a9', '8.74', '12.07', (
        t.create_value_key(time = '8.74', value_name = 'FoV', value = 25.0, interpolation_type = 2),
    ))
    t.create_tl_transform('d35b098e-8c34-45ee-9dde-21adfd2410a9', '8.74', '12.07', (
        (
            t.create_value_key(time = '8.74', interpolation_type = 5, value = -10.0),
        ),
        (
            t.create_value_key(time = '8.74', interpolation_type = 5, value = 1.8),
        ),
        (
            t.create_value_key(time = '8.74', interpolation_type = 5, value = -0.1),
        ),
        (
            t.create_value_key(time = '8.74', interpolation_type = 5, value = bg3.euler_to_quaternion(90.0, 0.0, 0.0, sequence = 'yxz')),
        ),
        (),
        (),
    ))

    t.create_tl_transform(bg3.SPEAKER_DURGE, '8.74', '12.07', (
        (
            t.create_value_key(time = '8.74', interpolation_type = 5, value = -8.0),
        ),
        (
            t.create_value_key(time = '8.74', interpolation_type = 5, value = 0.0),
        ),
        (
            t.create_value_key(time = '8.74', interpolation_type = 5, value = -0.87),
        ),
        (
            t.create_value_key(time = '8.74', interpolation_type = 5, value = (0.0, 1.0, 0.0, 0.0)),
        ),
        (
            t.create_value_key(time = '8.74', interpolation_type = 5, value = 1),
        ),
        (),
    ), is_snapped_to_end = True)

    t.create_tl_animation(
        bg3.SPEAKER_SHADOWHEART, '9.86', '10.56',
        'a0e37a8e-c619-4d0a-840a-061831fb0523',
        '16c31857-6247-46a5-9182-28926409bcaf',
        animation_slot = 1,
        animation_play_rate = 0.6,
        animation_play_start_offset = 3,
        fade_in = 0.25)

    # Camera shot 5
    t.create_tl_shot('d35b098e-8c34-45ee-9dde-21adfd2410a9', '12.07', '16.97')
    t.create_tl_camera_fov('d35b098e-8c34-45ee-9dde-21adfd2410a9', '12.07', '16.97', (
        t.create_value_key(time = '12.07', value_name = 'FoV', value = 40.0, interpolation_type = 2),
    ))
    t.create_tl_transform('d35b098e-8c34-45ee-9dde-21adfd2410a9', '12.07', '16.97', (
        (
            t.create_value_key(time = '12.07', interpolation_type = 5, value = -8.9),
        ),
        (
            t.create_value_key(time = '12.07', interpolation_type = 5, value = 1.8),
        ),
        (
            t.create_value_key(time = '12.07', interpolation_type = 5, value = 0.4),
        ),
        (
            t.create_value_key(time = '12.07', interpolation_type = 5, value = bg3.euler_to_quaternion(115.0, 10.0, 0.0, sequence = 'yxz')),
        ),
        (),
        (),
    ))

    t.create_tl_transform(bg3.SPEAKER_DURGE, '12.07', '16.97', (
        (
            t.create_value_key(time = '12.07', interpolation_type = 5, value = -8.0),
        ),
        (
            t.create_value_key(time = '12.07', interpolation_type = 5, value = 0.0),
        ),
        (
            t.create_value_key(time = '12.07', interpolation_type = 5, value = -0.87),
        ),
        (
            t.create_value_key(time = '12.07', interpolation_type = 5, value = (0.0, 1.0, 0.0, 0.0)),
        ),
        (
            t.create_value_key(time = '12.07', interpolation_type = 5, value = 1),
        ),
        (),
    ), is_snapped_to_end = True)

    t.create_tl_animation(
        bg3.SPEAKER_SHADOWHEART, '14.43', '16.97',
        'c26b9b0a-20cc-44a4-a499-18d6d78abec5',
        '16c31857-6247-46a5-9182-28926409bcaf',
        animation_slot = 1,
        animation_play_start_offset = 10.18,
        fade_in = 1,
        fade_out = 0)

    # Camera shot 6
    t.create_tl_shot('d35b098e-8c34-45ee-9dde-21adfd2410a9', '16.97', '24.27')
    t.create_tl_camera_fov('d35b098e-8c34-45ee-9dde-21adfd2410a9', '16.97', '24.27', (
        t.create_value_key(time = '16.97', value_name = 'FoV', value = 40.0, interpolation_type = 2),
    ))
    t.create_tl_transform('d35b098e-8c34-45ee-9dde-21adfd2410a9', '16.97', '24.27', (
        (
            t.create_value_key(time = '16.97', interpolation_type = 5, value = -7.1),
        ),
        (
            t.create_value_key(time = '16.97', interpolation_type = 5, value = 1.6),
        ),
        (
            t.create_value_key(time = '16.97', interpolation_type = 5, value = 0.2),
        ),
        (
            t.create_value_key(time = '16.97', interpolation_type = 5, value = bg3.euler_to_quaternion(-117.0, 0.0, 0.0, sequence = 'yxz')),
        ),
        (),
        (),
    ))

    t.create_tl_transform(bg3.SPEAKER_DURGE, '16.97', '24.27', (
        (
            t.create_value_key(time = '16.97', interpolation_type = 5, value = -8.0),
        ),
        (
            t.create_value_key(time = '16.97', interpolation_type = 5, value = 0.0),
        ),
        (
            t.create_value_key(time = '16.97', interpolation_type = 5, value = -0.87),
        ),
        (
            t.create_value_key(time = '16.97', interpolation_type = 5, value = (0.0, 1.0, 0.0, 0.0)),
        ),
        (
            t.create_value_key(time = '16.97', interpolation_type = 5, value = 1),
        ),
        (),
    ), is_snapped_to_end = True)

    t.create_tl_animation(
        bg3.SPEAKER_SHADOWHEART, '16.97', '28.81',
        'a70b0572-f371-49e6-854b-a8347e5db74a',
        '39e8f7e2-e600-47a8-a5c2-204b1ac9a5a7',
        animation_play_start_offset = 14.0,
        fade_in = 0.0,
        fade_out = 0.0)
    t.create_tl_animation(
        bg3.SPEAKER_DURGE, '16.97', '28.81',
        'a0f79aae-f6c9-4b19-d854-3153658a1da2',
        '6ef6e0ea-2ae3-46d9-8464-99aa9ba8e427',
        animation_play_start_offset = 14.0,
        fade_in = 0.0,
        fade_out = 0.0)

    t.create_tl_animation(
        bg3.SPEAKER_SHADOWHEART, '18.68', '24.27',
        'c26b9b0a-20cc-44a4-a499-18d6d78abec5',
        '16c31857-6247-46a5-9182-28926409bcaf',
        animation_slot = 1,
        animation_play_rate = 0.2,
        animation_play_start_offset = 3,
        fade_in = 2,
        fade_out = 2.3)

    # Camera shot 7
    t.create_tl_shot('d35b098e-8c34-45ee-9dde-21adfd2410a9', '24.27', '27.205')
    t.create_tl_camera_fov('d35b098e-8c34-45ee-9dde-21adfd2410a9', '24.27', '27.205', (
        t.create_value_key(time = '24.27', value_name = 'FoV', value = 40.0, interpolation_type = 2),
    ), is_snapped_to_end = True)
    t.create_tl_transform('d35b098e-8c34-45ee-9dde-21adfd2410a9', '24.27', '27.205', (
        (
            t.create_value_key(time = '24.27', interpolation_type = 5, value = -7.3),
        ),
        (
            t.create_value_key(time = '24.27', interpolation_type = 5, value = 1.7),
        ),
        (
            t.create_value_key(time = '24.27', interpolation_type = 5, value = -0.8),
        ),
        (
            t.create_value_key(time = '24.27', interpolation_type = 5, value = bg3.euler_to_quaternion(-47.0, 0.0, 0.0, sequence = 'yxz')),
        ),
        (),
        (),
    ))

    t.create_tl_transform(bg3.SPEAKER_DURGE, '24.27', '27.205', (
        (
            t.create_value_key(time = '24.27', interpolation_type = 5, value = -8.0),
        ),
        (
            t.create_value_key(time = '24.27', interpolation_type = 5, value = 0.0),
        ),
        (
            t.create_value_key(time = '24.27', interpolation_type = 5, value = -0.83),
        ),
        (
            t.create_value_key(time = '24.27', interpolation_type = 5, value = (0.0, 1.0, 0.0, 0.0)),
        ),
        (
            t.create_value_key(time = '24.27', interpolation_type = 5, value = 1),
        ),
        (),
    ), is_snapped_to_end = True)

    # Camera shot 8
    t.create_tl_shot('d35b098e-8c34-45ee-9dde-21adfd2410a9', '27.205', '28.81')
    t.create_tl_camera_fov('d35b098e-8c34-45ee-9dde-21adfd2410a9', '27.205', '28.81', (
        t.create_value_key(time = '27.205', value_name = 'FoV', value = 40.0, interpolation_type = 2),
    ), is_snapped_to_end = True)
    t.create_tl_transform('d35b098e-8c34-45ee-9dde-21adfd2410a9', '27.205', '28.81', (
        (
            t.create_value_key(time = '27.205', interpolation_type = 5, value = -9.2),
        ),
        (
            t.create_value_key(time = '27.205', interpolation_type = 5, value = 1.5),
        ),
        (
            t.create_value_key(time = '27.205', interpolation_type = 5, value = -0.4),
        ),
        (
            t.create_value_key(time = '27.205', interpolation_type = 5, value = bg3.euler_to_quaternion(84.0, 0.0, 0.0, sequence = 'yxz')),
        ),
        (),
        (),
    ))

    t.create_tl_transform(bg3.SPEAKER_DURGE, '27.205', '28.81', (
        (
            t.create_value_key(time = '27.205', interpolation_type = 5, value = -8.0),
        ),
        (
            t.create_value_key(time = '27.205', interpolation_type = 5, value = 0.0),
        ),
        (
            t.create_value_key(time = '27.205', interpolation_type = 5, value = -0.83),
        ),
        (
            t.create_value_key(time = '27.205', interpolation_type = 5, value = (0.0, 1.0, 0.0, 0.0)),
        ),
        (
            t.create_value_key(time = '27.205', interpolation_type = 5, value = 1),
        ),
        (),
    ), is_snapped_to_end = True)

    # Camera shot 10
    t.create_tl_shot('a6db4283-ef38-4472-827c-fffd0ac04a28', '28.81', '33.22')
    t.create_tl_camera_fov('a6db4283-ef38-4472-827c-fffd0ac04a28', '28.81', '33.22', (
        t.create_value_key(time = 0.0, value_name = 'FoV', value = 30.0, interpolation_type = 2),
    ))
    t.create_tl_transform('a6db4283-ef38-4472-827c-fffd0ac04a28', '28.81', '33.22', (
        (
            t.create_value_key(time = '28.81', interpolation_type = 5, value = -7.5),
        ),
        (
            t.create_value_key(time = '28.81', interpolation_type = 5, value = 1.8),
        ),
        (
            t.create_value_key(time = '28.81', interpolation_type = 5, value = -1.2),
        ),
        (
            t.create_value_key(time = '28.81', interpolation_type = 5, value = bg3.euler_to_quaternion(-34.0, 5.0, 0.0, sequence = 'yxz')),
        ),
        (),
        (),
    ))

    t.create_tl_transform(bg3.SPEAKER_DURGE, '28.81', phase_duration, (
        (
            t.create_value_key(time = '28.81', interpolation_type = 5, value = -8.0),
        ),
        (
            t.create_value_key(time = '28.81', interpolation_type = 5, value = 0.0),
        ),
        (
            t.create_value_key(time = '28.81', interpolation_type = 5, value = -0.83),
        ),
        (
            t.create_value_key(time = '28.81', interpolation_type = 5, value = (0.0, 1.0, 0.0, 0.0)),
        ),
        (
            t.create_value_key(time = '28.81', interpolation_type = 5, value = 1),
        ),
        (),
    ), is_snapped_to_end = True)

    t.create_tl_animation(
        bg3.SPEAKER_SHADOWHEART, '28.81', '33.22',
        '91239d58-cd15-1201-a029-a685b6434723',
        '66ce0c11-1cdb-4573-818c-a91cde00f79f',
        animation_play_start_offset = 3.1,
        fade_in = 0.0,
        fade_out = 0.0
    )
    t.create_tl_animation(
        bg3.SPEAKER_DURGE, '28.81', '33.22',
        'ee52d6f6-543f-454d-93d8-71b74ff5ac12',
        '57fa3dc0-184f-4b43-93fd-86e5496448a9',
        animation_play_start_offset = 3.1,
        fade_in = 1.5,
        fade_out = 0.0
    )

    # Camera shot 11
    t.create_tl_shot('a6db4283-ef38-4472-827c-fffd0ac04a28', '33.22', '36.2')
    t.create_tl_camera_fov('a6db4283-ef38-4472-827c-fffd0ac04a28', '33.22', '36.2', (
        t.create_value_key(time = '33.22', value_name = 'FoV', value = 25.0, interpolation_type = 2),
    ))
    t.create_tl_transform('a6db4283-ef38-4472-827c-fffd0ac04a28', '33.22', '36.2', (
        (
            t.create_value_key(time = '33.22', interpolation_type = 5, value = -8.5),
        ),
        (
            t.create_value_key(time = '33.22', interpolation_type = 5, value = 1.9),
        ),
        (
            t.create_value_key(time = '33.22', interpolation_type = 5, value = -0.8),
        ),
        (
            #t.create_value_key(time = '33.22', interpolation_type = 5, value = bg3.euler_to_quaternion(54.0, 10.0, 0.0, sequence = 'yxz')),
            t.create_value_key(time = '33.22', interpolation_type = 5, value = bg3.euler_to_quaternion(62.0, 12.0, 0.0, sequence = 'yxz')),
        ),
        (),
        (),
    ))

    t.create_tl_animation(
        bg3.SPEAKER_SHADOWHEART, '33.22', '36.2',
        '91239d58-cd15-1201-a029-a685b6434723',
        '66ce0c11-1cdb-4573-818c-a91cde00f79f',
        animation_play_start_offset = 7.01,
        fade_in = 0.0,
        fade_out = 0.0
    )
    t.create_tl_animation(
        bg3.SPEAKER_DURGE, '33.22', '36.2',
        'ee52d6f6-543f-454d-93d8-71b74ff5ac12',
        '57fa3dc0-184f-4b43-93fd-86e5496448a9',
        animation_play_start_offset = 7.01,
        fade_in = 0.0,
        fade_out = 0.0
    )

    t.create_tl_voice(
        bg3.SPEAKER_SHADOWHEART, '34.127', '36.0',
        bt2_gith_reaction_node_uuid,
        fade_in = 0.0,
        fade_out = 0.0)

    # Camera shot 12
    t.create_tl_shot('a6db4283-ef38-4472-827c-fffd0ac04a28', '36.2', '41.49', is_snapped_to_end = True)
    t.create_tl_camera_fov('a6db4283-ef38-4472-827c-fffd0ac04a28', '36.2', '41.49', (
        t.create_value_key(time = 0.0, value_name = 'FoV', value = 25.0, interpolation_type = 2),
    ))
    t.create_tl_transform('a6db4283-ef38-4472-827c-fffd0ac04a28', '36.2', '41.49', (
        (
            t.create_value_key(time = '36.2', interpolation_type = 5, value = -9.0),
        ),
        (
            t.create_value_key(time = '36.2', interpolation_type = 5, value = 1.8),
        ),
        (
            t.create_value_key(time = '36.2', interpolation_type = 5, value = -0.6),
        ),
        (
            t.create_value_key(time = '36.2', interpolation_type = 5, value = bg3.euler_to_quaternion(86.0, 4.0, 0.0, sequence = 'yxz')),
        ),
        (),
        (),
    ))

    t.create_tl_animation(
        bg3.SPEAKER_SHADOWHEART, '36.2', phase_duration, #56.22,
        '91239d58-cd15-1201-a029-a685b6434723',
        '66ce0c11-1cdb-4573-818c-a91cde00f79f',
        animation_play_start_offset = 11.91,
        fade_in = 0.0,
        fade_out = 2.0
    )
    t.create_tl_animation(
        bg3.SPEAKER_DURGE, '36.2', phase_duration, #56.22,
        'ee52d6f6-543f-454d-93d8-71b74ff5ac12',
        '57fa3dc0-184f-4b43-93fd-86e5496448a9',
        animation_play_start_offset = 11.91,
        fade_in = 0.0,
        fade_out = 1.0
    )

    t.create_tl_animation(
        bg3.SPEAKER_SHADOWHEART, '37.54', '41.49',
        'c26b9b0a-20cc-44a4-a499-18d6d78abec5',
        '536f3ddd-33e5-4b9d-a20a-b7109f6bbc76',
        animation_slot = 1,
        animation_play_start_offset = 6.62,
        fade_in = 1.6,
        fade_out = 0.0
    )
    t.create_tl_animation(
        bg3.SPEAKER_DURGE, '37.92', '41.49',
        'c26b9b0a-20cc-44a4-a499-18d6d78abec5',
        '90070425-bce3-4bef-b8d7-ca38a676b5cb',
        animation_slot = 1,
        animation_play_start_offset = 7,
        fade_in = 1.5,
        fade_out = 0.0
    )

    t.create_tl_animation(
        bg3.SPEAKER_DURGE, '41.49', '47.14',
        'c26b9b0a-20cc-44a4-a499-18d6d78abec5',
        '90070425-bce3-4bef-b8d7-ca38a676b5cb',
        animation_slot = 1,
        animation_play_start_offset = 3.5,
        fade_in = 0.0,
        fade_out = 1.5
    )
    t.create_tl_animation(
        bg3.SPEAKER_SHADOWHEART, '41.49', '47.14',
        'c26b9b0a-20cc-44a4-a499-18d6d78abec5',
        '536f3ddd-33e5-4b9d-a20a-b7109f6bbc76',
        animation_slot = 1,
        animation_play_start_offset = 3.5,
        fade_in = 0.0,
        fade_out = 1.5
    )

    # Camera shot 13
    t.create_tl_shot('a6db4283-ef38-4472-827c-fffd0ac04a28', '41.49', phase_duration, is_snapped_to_end = True)
    t.create_tl_camera_fov('a6db4283-ef38-4472-827c-fffd0ac04a28', '41.49', phase_duration, (
        t.create_value_key(time = '41.49', value_name = 'FoV', value = 30.0, interpolation_type = 2),
    ))
    t.create_tl_transform('a6db4283-ef38-4472-827c-fffd0ac04a28', '41.49', phase_duration, (
        (
            t.create_value_key(time = '41.49', interpolation_type = 5, value = -7.1),
        ),
        (
            t.create_value_key(time = '41.49', interpolation_type = 5, value = 1.75),
        ),
        (
            t.create_value_key(time = '41.49', interpolation_type = 5, value = -1.1),
        ),
        (
            t.create_value_key(time = '41.49', interpolation_type = 5, value = bg3.euler_to_quaternion(-60.0, 0.0, 0.0, sequence = 'yxz')),
        ),
        (),
        (),
    ))

    # Camera shot 14
    # t.create_tl_shot('a6db4283-ef38-4472-827c-fffd0ac04a28', '53.22', 56.22, is_snapped_to_end = True)
    # t.create_tl_camera_fov('a6db4283-ef38-4472-827c-fffd0ac04a28', '53.22', 56.22, (
    #     t.create_value_key(time = 53.22, value_name = 'FoV', value = 32.0, interpolation_type = 2),
    # ))
    # t.create_tl_transform('a6db4283-ef38-4472-827c-fffd0ac04a28', '53.22', 56.22, (
    #     (
    #         t.create_value_key(time = 53.22, interpolation_type = 5, value = -8.5),
    #     ),
    #     (
    #         t.create_value_key(time = 53.22, interpolation_type = 5, value = 1.75),
    #     ),
    #     (
    #         t.create_value_key(time = 53.22, interpolation_type = 5, value = -0.5),
    #     ),
    #     (
    #         #t.create_value_key(time = 53.22, interpolation_type = 5, value = bg3.euler_to_quaternion(65.0, 0.0, 0.0, sequence = 'yxz')),
    #         t.create_value_key(time = 53.22, interpolation_type = 5, value = bg3.euler_to_quaternion(45.0, 0.0, 0.0, sequence = 'yxz')),
    #     ),
    #     (),
    #     (),
    # ))


#################################################################################################
# Body type 1
#################################################################################################

def create_scene_shadowheart_reaction_body_type_1() -> None:

    # d = bg3.dialog_object(files.get_file('Gustav', 'Mods/GustavDev/Story/DialogsBinary/Act3/LowerCity/BhaalTemple/LOW_BhaalTemple_PostBattleDarkUrge_Resistance.lsf'))
    # t = bg3.timeline_object(files.get_file('Gustav', 'Public/GustavDev/Timeline/Generated/LOW_BhaalTemple_PostBattleDarkUrge_Resistance.lsf'), d)

    ab = game_assets.get_modded_dialog_asset_bundle('LOW_BhaalTemple_PostBattleDarkUrge_Resistance')
    d = bg3.dialog_object(ab.dialog)
    t = bg3.timeline_object(ab.timeline, d)

    slot_idx_durge = d.get_speaker_slot_index(bg3.SPEAKER_DURGE)
    #slot_idx_shadowheart = d.get_speaker_slot_index(bg3.SPEAKER_SHADOWHEART)

    # d.create_cinematic_dialog_node(
    #     normal_body_reaction_node_uuid,
    #     [just_keep_safe_out_there_node_uuid])
    d.create_standard_dialog_node(
        bt1_reaction_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [just_keep_safe_out_there_node_uuid],
        bg3.text_content('hd896e304g5fc4g41e7g807cg524360fee6a9', 1),
        checkflags = (
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_FEMALE, True, slot_idx_durge),
            )),
        )
    )

    phase_duration = '54.42' # '53.22' #56.22
    t.create_new_phase(bt1_reaction_node_uuid, phase_duration)

    t.create_tl_actor_node(bg3.timeline_object.ATTITUDE, bg3.SPEAKER_DURGE, '0.0', phase_duration, (
        t.create_attitude_key(12.15, bg3.ATTITUDE_DIAG_Pose_Stand_R_Forward_01, bg3.ATTITUDE_DIAG_T_Pose),
        t.create_attitude_key(28.81, 'a2bd89b1-8ab9-4231-ac4b-e593d75aa083', bg3.ATTITUDE_DIAG_T_Pose),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.ATTITUDE, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_attitude_key(0.0, bg3.ATTITUDE_DIAG_Pose_Stand_L_Forward_01, bg3.ATTITUDE_DIAG_T_Pose),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.EMOTION, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_emotion_key(0.0, 32),
        t.create_emotion_key(6.13, 32, variation = 2),
        t.create_emotion_key(7.34, 32),
        t.create_emotion_key(15.63, 32, variation = 1),
        t.create_emotion_key(20.58, 32),
        t.create_emotion_key(44.85, 32, variation = 1, is_sustained = False),
        t.create_emotion_key(51.97, 32)
        #t.create_emotion_key(26.0, 2)
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.EMOTION, bg3.SPEAKER_DURGE, '0.0', phase_duration, (
        t.create_emotion_key(0.0, 32, variation = 1),
        t.create_emotion_key(3.51, 32),
        t.create_emotion_key(6.08, 32, variation = 1),
        t.create_emotion_key(6.56, 32),
        t.create_emotion_key(8.26, 32, variation = 2),
        t.create_emotion_key(11.26, 32, variation = 1),
        t.create_emotion_key(22.03, 32),
        t.create_emotion_key(40.14, 256),
        t.create_emotion_key(44.85, 32),
    ), is_snapped_to_end = True)
    #t.create_tl_actor_node(bg3.timeline_object.EMOTION, bg3.SPEAKER_JERGAL, '0.0', phase_duration, (
    #    t.create_emotion_key(0.0, 1, None),
    #    t.create_emotion_key(25.5, 2, variation = 2),
    #), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.LOOK_AT, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_look_at_key(
            0.0,
            target = bg3.SPEAKER_DURGE,
            bone = 'Head_M',
            turn_mode = 3,
            turn_speed_multiplier = 0.3,
            torso_turn_speed_multiplier = 0.3,
            head_turn_speed_multiplier = 0.3,
            weight = 0.0,
            reset = True,
            eye_look_at_bone = 'Head_M'),
        t.create_look_at_key(
            '4.20',
            target = bg3.SPEAKER_DURGE,
            bone = 'Head_M',
            turn_mode = 3,
            turn_speed_multiplier = 0.3,
            torso_turn_speed_multiplier = 0.3,
            head_turn_speed_multiplier = 0.3,
            weight = 0.3,
            safe_zone_angle = 80.0,
            head_safe_zone_angle = 80.0,
            reset = True,
            look_at_mode = 1,
            eye_look_at_bone = 'Head_M'),
        t.create_look_at_key(
            '9.41',
            turn_mode = 3,
            turn_speed_multiplier = 0.26370612,
            torso_turn_speed_multiplier = 0.26370612,
            head_turn_speed_multiplier = 0.26370612,
            weight = 0.3,
            safe_zone_angle = 80.0,
            head_safe_zone_angle = 80.0,
            look_at_mode = 0),
        t.create_look_at_key(
            '24.27',
            target = bg3.SPEAKER_DURGE,
            bone = 'Head_M',
            turn_mode = 3,
            turn_speed_multiplier = 0.3,
            torso_turn_speed_multiplier = 0.3,
            head_turn_speed_multiplier = 0.3,
            weight = 0.0,
            safe_zone_angle = 80.0,
            head_safe_zone_angle = 80.0,
            reset = True,
            look_at_mode = 1,
            eye_look_at_bone = 'Head_M'),
        t.create_look_at_key(
            '28.81',
            target = bg3.SPEAKER_DURGE,
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
    t.create_tl_actor_node(bg3.timeline_object.LOOK_AT, bg3.SPEAKER_DURGE, '0.0', phase_duration, (
        t.create_look_at_key(
            0.0,
            target = bg3.SPEAKER_SHADOWHEART,
            bone = 'Head_M',
            turn_mode = 3,
            turn_speed_multiplier = 0.3,
            torso_turn_speed_multiplier = 0.3,
            head_turn_speed_multiplier = 0.21843724,
            weight = 0.0,
            safe_zone_angle = 80.0,
            head_safe_zone_angle = 80.0,
            look_at_mode = 1,
            eye_look_at_bone = 'Head_M'),
        t.create_look_at_key(
            '4.20',
            turn_mode = 3,
            turn_speed_multiplier = 0.3,
            torso_turn_speed_multiplier = 0.3,
            head_turn_speed_multiplier = 0.1,
            weight = 0.0,
            safe_zone_angle = 80.0,
            head_safe_zone_angle = 80.0,
            look_at_mode = 0),
        t.create_look_at_key(
            '6.56',
            target = bg3.SPEAKER_SHADOWHEART,
            bone = 'Head_M',
            turn_mode = 3,
            turn_speed_multiplier = 0.3269225,
            torso_turn_speed_multiplier = 0.3269225,
            head_turn_speed_multiplier = 0.10897417,
            weight = 0.0,
            safe_zone_angle = 80.0,
            head_safe_zone_angle = 80.0,
            look_at_mode = 1,
            eye_look_at_bone = 'Head_M'),
        t.create_look_at_key(
            '9.4',
            turn_mode = 3,
            turn_speed_multiplier = 0.25471807,
            torso_turn_speed_multiplier = 0.25471807,
            head_turn_speed_multiplier = 0.08490602,
            weight = 0.0,
            safe_zone_angle = 80.0,
            head_safe_zone_angle = 80.0,
            look_at_mode = 0),
        t.create_look_at_key(
            '24.27',
            target = bg3.SPEAKER_SHADOWHEART,
            bone = 'Head_M',
            turn_mode = 3,
            turn_speed_multiplier = 0.3,
            torso_turn_speed_multiplier = 0.3,
            head_turn_speed_multiplier = 0.1,
            weight = 0.0,
            safe_zone_angle = 80.0,
            head_safe_zone_angle = 80.0,
            reset = True,
            look_at_mode = 1,
            eye_look_at_bone = 'Head_M'),
        t.create_look_at_key(
            '28.81',
            target = bg3.SPEAKER_SHADOWHEART,
            bone = 'Head_M',
            turn_mode = 3,
            turn_speed_multiplier = 0.3,
            head_turn_speed_multiplier = 0.1,
            weight = 0.0,
            safe_zone_angle = 80.0,
            head_safe_zone_angle = 80.0,
            look_at_mode = 1,
            eye_look_at_bone = 'Head_M'),
    ), is_snapped_to_end = True)

    t.create_tl_material(bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, '156a2490-d796-402c-b7fc-e00c032042c1', (), (
        t.create_value_key(time = 0.0, value = True),
    ), is_snapped_to_end = True, is_continuous = True)

    # Hide helmets
    t.create_tl_show_armor(bg3.SPEAKER_DURGE, '0.0', phase_duration, (
        (
            t.create_value_key(time = 0.0, value = False, interpolation_type = 0),
            t.create_value_key(time = phase_duration, interpolation_type = 0)
        ),
        (), (), (), (), (), (), (), (), (), ()
    ))
    t.create_tl_show_armor(bg3.SPEAKER_SHADOWHEART, '0.0',  phase_duration, (
        (
            t.create_value_key(time = 0.0, value = False, interpolation_type = 0),
            t.create_value_key(time = phase_duration, interpolation_type = 0)
        ),
        (), (), (), (), (), (), (), (), (), ()
    ))

    # Hide weapons
    t.create_tl_actor_node(bg3.timeline_object.SHOW_WEAPON, bg3.SPEAKER_DURGE, '0.0', phase_duration, (
        t.create_value_key(time = 0.0, value_name = 'ShowWeapon', value = False, interpolation_type = 3),
        t.create_value_key(time = phase_duration, interpolation_type = 3),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.SHOW_WEAPON, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_value_key(time = 0.0, value_name = 'ShowWeapon', value = False, interpolation_type = 3),
        t.create_value_key(time = phase_duration, interpolation_type = 3),
    ), is_snapped_to_end = True)

    # Show Durge
    t.create_tl_actor_node(bg3.timeline_object.SHOW_VISUAL, bg3.SPEAKER_DURGE, '0.0', phase_duration, (
        t.create_value_key(time = 0.0, interpolation_type = 3),
    ), is_snapped_to_end = True)

    # Sounds
    # Hug part
    t.create_tl_actor_node(bg3.timeline_object.SOUND, bg3.SPEAKER_DURGE, '0.0', phase_duration, (), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.SOUND, bg3.SPEAKER_DURGE, '0.0', phase_duration, (
        t.create_sound_event_key(5.52, sound_event_id = 'd0756d07-fd81-4fab-b4af-03d565c7f059', sound_object_index = 4),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.SOUND, bg3.SPEAKER_DURGE, '0.0', phase_duration, (
        t.create_sound_event_key(8.74, sound_type = 4, foley_type = 2),
    ), is_snapped_to_end = True)

    t.create_tl_actor_node(bg3.timeline_object.SOUND, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.SOUND, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_sound_event_key(12.07, sound_event_id = '50ab7087-b822-455f-9a61-6b10b6e6d968', sound_object_index = 4),
        t.create_sound_event_key(19.2482, sound_event_id = '220abafa-e55f-4124-8cb7-16fca63fda5f', sound_object_index = 4),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.SOUND, bg3.SPEAKER_DURGE, '0.0', phase_duration, (), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.SOUND, bg3.SPEAKER_DURGE, '0.0', phase_duration, (
        t.create_sound_event_key(5.5, sound_event_id = 'c232329e-2d4e-4f0c-a4d4-ea1585fce27c', sound_object_index = 4),
        t.create_sound_event_key(7.05, sound_event_id = 'aa8db628-8c78-4632-ab7a-2ac210393e93', sound_object_index = 4),
        t.create_sound_event_key(8.745, sound_event_id = '220abafa-e55f-4124-8cb7-16fca63fda5f', sound_object_index = 4),
        t.create_sound_event_key(24.27, sound_event_id = '220abafa-e55f-4124-8cb7-16fca63fda5f', sound_object_index = 4),
    ), is_snapped_to_end = True)

    # Kiss part
    t.create_tl_actor_node(bg3.timeline_object.SOUND, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_sound_event_key(29.73, sound_event_id = '3a82ed81-3970-461a-91dc-4687caa05cce', sound_object_index = 1),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.SOUND, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_sound_event_key(38.29, sound_event_id = '90a31a12-9f32-47e1-899e-cdced0705f27', sound_object_index = 4),
        t.create_sound_event_key(38.35, sound_event_id = '025fa6be-55ec-43fe-af6a-03b746163d72', sound_object_index = 4),
        t.create_sound_event_key(38.96, sound_event_id = 'ffbbbd57-5c31-444d-bc3a-c3d14df0be53', sound_object_index = 4),
        t.create_sound_event_key(43.49, sound_event_id = 'ffbbbd57-5c31-444d-bc3a-c3d14df0be53', sound_object_index = 4),
        t.create_sound_event_key(45.83, sound_event_id = '5dac329f-b08a-412d-84bc-86fc1aecae45', sound_object_index = 4),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.SOUND, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_sound_event_key(31.11, sound_event_id = '3a82ed81-3970-461a-91dc-4687caa05cce', sound_object_index = 2),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.SOUND, bg3.SPEAKER_DURGE, '0.0', phase_duration, (
        t.create_sound_event_key(41.19, sound_event_id = 'ffbbbd57-5c31-444d-bc3a-c3d14df0be53', sound_object_index = 4),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.SOUND, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (), is_snapped_to_end = True)

    # Physics
    t.create_tl_actor_node(bg3.timeline_object.PHYSICS, bg3.SPEAKER_DURGE, '0.0', phase_duration, (
        t.create_value_key(time = 0.0, interpolation_type = 3, value_name = 'InverseKinematics', value = False),
        t.create_value_key(time = '28.81', interpolation_type = 3),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.PHYSICS, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_value_key(time = 0.0, interpolation_type = 3, value_name = 'InverseKinematics', value = False),
        t.create_value_key(time = '28.81', interpolation_type = 3),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.HANDS_IK, bg3.SPEAKER_DURGE, '0.0', phase_duration, (), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.HANDS_IK, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (), is_snapped_to_end = True)

    t.create_tl_animation(
        bg3.SPEAKER_SHADOWHEART, '0.0', '16.97',
        'a70b0572-f371-49e6-854b-a8347e5db74a',
        '39e8f7e2-e600-47a8-a5c2-204b1ac9a5a7',
        fade_in = 1.0,
        fade_out = 0.0)
    t.create_tl_animation(
        bg3.SPEAKER_DURGE, '0.0', '16.97',
        'a0f79aae-f6c9-4b19-d854-3153658a1da2',
        '6ef6e0ea-2ae3-46d9-8464-99aa9ba8e427',
        fade_in = 1.0,
        fade_out = 0.0)

    t.create_tl_transform(bg3.SPEAKER_DURGE, '0.0', '4.2', (
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = -8.0),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 0.0),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = -0.83),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = (0.0, 1.0, 0.0, 0.0)),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 1),
        ),
        (),
    ), is_snapped_to_end = True)
    t.create_tl_transform(bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = -8.0),
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

    # Camera shot 1
    t.create_tl_shot('d35b098e-8c34-45ee-9dde-21adfd2410a9', '0.0', '2.2')
    t.create_tl_camera_fov('d35b098e-8c34-45ee-9dde-21adfd2410a9', '0.0', '2.2', (
        t.create_value_key(time = 0.0, value_name = 'FoV', value = 35.0, interpolation_type = 2),
    ))
    t.create_tl_transform('d35b098e-8c34-45ee-9dde-21adfd2410a9', '0.0', '2.2', (
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = -7.5),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 1.8),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 0.2),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = bg3.euler_to_quaternion(-154.0, 0.0, 0.0, sequence = 'yxz')),
        ),
        (),
        (),
    ))

    # Camera shot 2
    t.create_tl_shot('d35b098e-8c34-45ee-9dde-21adfd2410a9', '2.2', '4.2')
    t.create_tl_camera_fov('d35b098e-8c34-45ee-9dde-21adfd2410a9', '2.2', '4.2', (
        t.create_value_key(time = 0.0, value_name = 'FoV', value = 25.0, interpolation_type = 2),
    ))
    t.create_tl_transform('d35b098e-8c34-45ee-9dde-21adfd2410a9', '2.2', '4.2', (
        (
            t.create_value_key(time = 2.2, interpolation_type = 5, value = -6.5),
        ),
        (
            t.create_value_key(time = 2.2, interpolation_type = 5, value = 1.8),
        ),
        (
            t.create_value_key(time = 2.2, interpolation_type = 5, value = -1.0),
        ),
        (
            t.create_value_key(time = 2.2, interpolation_type = 5, value = bg3.euler_to_quaternion(-62.0, 0.0, 0.0, sequence = 'yxz')),
        ),
        (),
        (),
    ))


    # Camera shot 3
    t.create_tl_shot('d35b098e-8c34-45ee-9dde-21adfd2410a9', '4.2', '8.74')
    t.create_tl_camera_fov('d35b098e-8c34-45ee-9dde-21adfd2410a9', '4.2', '8.74', (
        t.create_value_key(time = '4.2', value_name = 'FoV', value = 15.0, interpolation_type = 2),
    ))
    t.create_tl_transform('d35b098e-8c34-45ee-9dde-21adfd2410a9', '4.2', '8.74', (
        (
            t.create_value_key(time = '4.2', interpolation_type = 5, value = -6.0),
        ),
        (
            t.create_value_key(time = '4.2', interpolation_type = 5, value = 2.0),
        ),
        (
            t.create_value_key(time = '4.2', interpolation_type = 5, value = -0.6),
        ),
        (
            t.create_value_key(time = '4.2', interpolation_type = 5, value = bg3.euler_to_quaternion(-74.0, 10.0, 0.0, sequence = 'yxz')),
        ),
        (),
        (),
    ))

    t.create_tl_transform(bg3.SPEAKER_DURGE, '4.2', '8.74', (
        (
            t.create_value_key(time = '4.2', interpolation_type = 5, value = -8.0),
        ),
        (
            t.create_value_key(time = '4.2', interpolation_type = 5, value = 0.1),
        ),
        (
            t.create_value_key(time = '4.2', interpolation_type = 5, value = -0.78),
        ),
        (
            t.create_value_key(time = '4.2', interpolation_type = 5, value = (0.0, 1.0, 0.0, 0.0)),
        ),
        (
            t.create_value_key(time = '4.2', interpolation_type = 5, value = 1),
        ),
        (),
    ), is_snapped_to_end = True)

    t.create_tl_animation(
        bg3.SPEAKER_SHADOWHEART, '4.58', '8.74',
        'a0e37a8e-c619-4d0a-840a-061831fb0523',
        '16c31857-6247-46a5-9182-28926409bcaf',
        animation_slot = 1,
        animation_play_rate = 0.6,
        animation_play_start_offset = 3.5,
        fade_in = 1.76,
        fade_out = 2.3)
    t.create_tl_animation(
        bg3.SPEAKER_DURGE, '4.58', '8.74',
        'a0e37a8e-c619-4d0a-840a-061831fb0523',
        '1913a5ea-cbf7-491b-bf3e-34c829ac69dd',
        animation_slot = 1,
        animation_play_rate = 0.6,
        animation_play_start_offset = 3.5,
        fade_in = 1.76,
        fade_out = 2.3)

    # Camera shot 4
    t.create_tl_shot('d35b098e-8c34-45ee-9dde-21adfd2410a9', '8.74', '12.07')
    t.create_tl_camera_fov('d35b098e-8c34-45ee-9dde-21adfd2410a9', '8.74', '12.07', (
        t.create_value_key(time = '8.74', value_name = 'FoV', value = 25.0, interpolation_type = 2),
    ))
    t.create_tl_transform('d35b098e-8c34-45ee-9dde-21adfd2410a9', '8.74', '12.07', (
        (
            t.create_value_key(time = '8.74', interpolation_type = 5, value = -10.0),
        ),
        (
            t.create_value_key(time = '8.74', interpolation_type = 5, value = 1.8),
        ),
        (
            t.create_value_key(time = '8.74', interpolation_type = 5, value = -0.1),
        ),
        (
            t.create_value_key(time = '8.74', interpolation_type = 5, value = bg3.euler_to_quaternion(90.0, 0.0, 0.0, sequence = 'yxz')),
        ),
        (),
        (),
    ))

    t.create_tl_transform(bg3.SPEAKER_DURGE, '8.74', '12.07', (
        (
            t.create_value_key(time = '8.74', interpolation_type = 5, value = -8.0),
        ),
        (
            t.create_value_key(time = '8.74', interpolation_type = 5, value = 0.0),
        ),
        (
            t.create_value_key(time = '8.74', interpolation_type = 5, value = -0.87),
        ),
        (
            t.create_value_key(time = '8.74', interpolation_type = 5, value = (0.0, 1.0, 0.0, 0.0)),
        ),
        (
            t.create_value_key(time = '8.74', interpolation_type = 5, value = 1),
        ),
        (),
    ), is_snapped_to_end = True)

    t.create_tl_animation(
        bg3.SPEAKER_SHADOWHEART, '9.86', '10.56',
        'a0e37a8e-c619-4d0a-840a-061831fb0523',
        '16c31857-6247-46a5-9182-28926409bcaf',
        animation_slot = 1,
        animation_play_rate = 0.6,
        animation_play_start_offset = 3,
        fade_in = 0.25)

    # Camera shot 5
    t.create_tl_shot('d35b098e-8c34-45ee-9dde-21adfd2410a9', '12.07', '16.97')
    t.create_tl_camera_fov('d35b098e-8c34-45ee-9dde-21adfd2410a9', '12.07', '16.97', (
        t.create_value_key(time = '12.07', value_name = 'FoV', value = 40.0, interpolation_type = 2),
    ))
    t.create_tl_transform('d35b098e-8c34-45ee-9dde-21adfd2410a9', '12.07', '16.97', (
        (
            t.create_value_key(time = '12.07', interpolation_type = 5, value = -8.9),
        ),
        (
            t.create_value_key(time = '12.07', interpolation_type = 5, value = 1.8),
        ),
        (
            t.create_value_key(time = '12.07', interpolation_type = 5, value = 0.4),
        ),
        (
            t.create_value_key(time = '12.07', interpolation_type = 5, value = bg3.euler_to_quaternion(115.0, 10.0, 0.0, sequence = 'yxz')),
        ),
        (),
        (),
    ))

    t.create_tl_transform(bg3.SPEAKER_DURGE, '12.07', '16.97', (
        (
            t.create_value_key(time = '12.07', interpolation_type = 5, value = -8.0),
        ),
        (
            t.create_value_key(time = '12.07', interpolation_type = 5, value = 0.0),
        ),
        (
            t.create_value_key(time = '12.07', interpolation_type = 5, value = -0.87),
        ),
        (
            t.create_value_key(time = '12.07', interpolation_type = 5, value = (0.0, 1.0, 0.0, 0.0)),
        ),
        (
            t.create_value_key(time = '12.07', interpolation_type = 5, value = 1),
        ),
        (),
    ), is_snapped_to_end = True)

    t.create_tl_animation(
        bg3.SPEAKER_SHADOWHEART, '14.43', '16.97',
        'c26b9b0a-20cc-44a4-a499-18d6d78abec5',
        '16c31857-6247-46a5-9182-28926409bcaf',
        animation_slot = 1,
        animation_play_start_offset = 10.18,
        fade_in = 1,
        fade_out = 0)

    # Camera shot 6
    t.create_tl_shot('d35b098e-8c34-45ee-9dde-21adfd2410a9', '16.97', '24.27')
    t.create_tl_camera_fov('d35b098e-8c34-45ee-9dde-21adfd2410a9', '16.97', '24.27', (
        t.create_value_key(time = '16.97', value_name = 'FoV', value = 40.0, interpolation_type = 2),
    ))
    t.create_tl_transform('d35b098e-8c34-45ee-9dde-21adfd2410a9', '16.97', '24.27', (
        (
            t.create_value_key(time = '16.97', interpolation_type = 5, value = -7.1),
        ),
        (
            t.create_value_key(time = '16.97', interpolation_type = 5, value = 1.6),
        ),
        (
            t.create_value_key(time = '16.97', interpolation_type = 5, value = 0.2),
        ),
        (
            t.create_value_key(time = '16.97', interpolation_type = 5, value = bg3.euler_to_quaternion(-117.0, 0.0, 0.0, sequence = 'yxz')),
        ),
        (),
        (),
    ))

    t.create_tl_transform(bg3.SPEAKER_DURGE, '16.97', '24.27', (
        (
            t.create_value_key(time = '16.97', interpolation_type = 5, value = -8.0),
        ),
        (
            t.create_value_key(time = '16.97', interpolation_type = 5, value = 0.0),
        ),
        (
            t.create_value_key(time = '16.97', interpolation_type = 5, value = -0.87),
        ),
        (
            t.create_value_key(time = '16.97', interpolation_type = 5, value = (0.0, 1.0, 0.0, 0.0)),
        ),
        (
            t.create_value_key(time = '16.97', interpolation_type = 5, value = 1),
        ),
        (),
    ), is_snapped_to_end = True)

    t.create_tl_animation(
        bg3.SPEAKER_SHADOWHEART, '16.97', '28.81',
        'a70b0572-f371-49e6-854b-a8347e5db74a',
        '39e8f7e2-e600-47a8-a5c2-204b1ac9a5a7',
        animation_play_start_offset = 14.0,
        fade_in = 0.0,
        fade_out = 0.0)
    t.create_tl_animation(
        bg3.SPEAKER_DURGE, '16.97', '28.81',
        'a0f79aae-f6c9-4b19-d854-3153658a1da2',
        '6ef6e0ea-2ae3-46d9-8464-99aa9ba8e427',
        animation_play_start_offset = 14.0,
        fade_in = 0.0,
        fade_out = 0.0)

    t.create_tl_animation(
        bg3.SPEAKER_SHADOWHEART, '18.68', '24.27',
        'c26b9b0a-20cc-44a4-a499-18d6d78abec5',
        '16c31857-6247-46a5-9182-28926409bcaf',
        animation_slot = 1,
        animation_play_rate = 0.2,
        animation_play_start_offset = 3,
        fade_in = 2,
        fade_out = 2.3)

    # Camera shot 7
    t.create_tl_shot('d35b098e-8c34-45ee-9dde-21adfd2410a9', '24.27', '27.205')
    t.create_tl_camera_fov('d35b098e-8c34-45ee-9dde-21adfd2410a9', '24.27', '27.205', (
        t.create_value_key(time = '24.27', value_name = 'FoV', value = 40.0, interpolation_type = 2),
    ), is_snapped_to_end = True)
    t.create_tl_transform('d35b098e-8c34-45ee-9dde-21adfd2410a9', '24.27', '27.205', (
        (
            t.create_value_key(time = '24.27', interpolation_type = 5, value = -7.3),
        ),
        (
            t.create_value_key(time = '24.27', interpolation_type = 5, value = 1.7),
        ),
        (
            t.create_value_key(time = '24.27', interpolation_type = 5, value = -0.8),
        ),
        (
            t.create_value_key(time = '24.27', interpolation_type = 5, value = bg3.euler_to_quaternion(-47.0, 0.0, 0.0, sequence = 'yxz')),
        ),
        (),
        (),
    ))

    t.create_tl_transform(bg3.SPEAKER_DURGE, '24.27', '27.205', (
        (
            t.create_value_key(time = '24.27', interpolation_type = 5, value = -8.0),
        ),
        (
            t.create_value_key(time = '24.27', interpolation_type = 5, value = 0.0),
        ),
        (
            t.create_value_key(time = '24.27', interpolation_type = 5, value = -0.83),
        ),
        (
            t.create_value_key(time = '24.27', interpolation_type = 5, value = (0.0, 1.0, 0.0, 0.0)),
        ),
        (
            t.create_value_key(time = '24.27', interpolation_type = 5, value = 1),
        ),
        (),
    ), is_snapped_to_end = True)

    # Camera shot 8
    t.create_tl_shot('d35b098e-8c34-45ee-9dde-21adfd2410a9', '27.205', '28.81')
    t.create_tl_camera_fov('d35b098e-8c34-45ee-9dde-21adfd2410a9', '27.205', '28.81', (
        t.create_value_key(time = '27.205', value_name = 'FoV', value = 40.0, interpolation_type = 2),
    ), is_snapped_to_end = True)
    t.create_tl_transform('d35b098e-8c34-45ee-9dde-21adfd2410a9', '27.205', '28.81', (
        (
            t.create_value_key(time = '27.205', interpolation_type = 5, value = -9.2),
        ),
        (
            t.create_value_key(time = '27.205', interpolation_type = 5, value = 1.5),
        ),
        (
            t.create_value_key(time = '27.205', interpolation_type = 5, value = -0.4),
        ),
        (
            t.create_value_key(time = '27.205', interpolation_type = 5, value = bg3.euler_to_quaternion(84.0, 0.0, 0.0, sequence = 'yxz')),
        ),
        (),
        (),
    ))

    t.create_tl_transform(bg3.SPEAKER_DURGE, '27.205', '28.81', (
        (
            t.create_value_key(time = '27.205', interpolation_type = 5, value = -8.0),
        ),
        (
            t.create_value_key(time = '27.205', interpolation_type = 5, value = 0.0),
        ),
        (
            t.create_value_key(time = '27.205', interpolation_type = 5, value = -0.83),
        ),
        (
            t.create_value_key(time = '27.205', interpolation_type = 5, value = (0.0, 1.0, 0.0, 0.0)),
        ),
        (
            t.create_value_key(time = '27.205', interpolation_type = 5, value = 1),
        ),
        (),
    ), is_snapped_to_end = True)

    # Camera shot 10
    t.create_tl_shot('a6db4283-ef38-4472-827c-fffd0ac04a28', '28.81', '33.22')
    t.create_tl_camera_fov('a6db4283-ef38-4472-827c-fffd0ac04a28', '28.81', '33.22', (
        t.create_value_key(time = 0.0, value_name = 'FoV', value = 30.0, interpolation_type = 2),
    ))
    t.create_tl_transform('a6db4283-ef38-4472-827c-fffd0ac04a28', '28.81', '33.22', (
        (
            t.create_value_key(time = '28.81', interpolation_type = 5, value = -7.5),
        ),
        (
            t.create_value_key(time = '28.81', interpolation_type = 5, value = 1.8),
        ),
        (
            t.create_value_key(time = '28.81', interpolation_type = 5, value = -1.2),
        ),
        (
            t.create_value_key(time = '28.81', interpolation_type = 5, value = bg3.euler_to_quaternion(-34.0, 5.0, 0.0, sequence = 'yxz')),
        ),
        (),
        (),
    ))

    t.create_tl_transform(bg3.SPEAKER_DURGE, '28.81', phase_duration, (
        (
            t.create_value_key(time = '28.81', interpolation_type = 5, value = -8.0),
        ),
        (
            t.create_value_key(time = '28.81', interpolation_type = 5, value = 0.0),
        ),
        (
            t.create_value_key(time = '28.81', interpolation_type = 5, value = -0.83),
        ),
        (
            t.create_value_key(time = '28.81', interpolation_type = 5, value = (0.0, 1.0, 0.0, 0.0)),
        ),
        (
            t.create_value_key(time = '28.81', interpolation_type = 5, value = 1),
        ),
        (),
    ), is_snapped_to_end = True)

    t.create_tl_animation(
        bg3.SPEAKER_SHADOWHEART, '28.81', '33.22',
        '91239d58-cd15-1201-a029-a685b6434723',
        '66ce0c11-1cdb-4573-818c-a91cde00f79f',
        animation_play_start_offset = 3.1,
        fade_in = 0.0,
        fade_out = 0.0
    )
    t.create_tl_animation(
        bg3.SPEAKER_DURGE, '28.81', '33.22',
        'ee52d6f6-543f-454d-93d8-71b74ff5ac12',
        '57fa3dc0-184f-4b43-93fd-86e5496448a9',
        animation_play_start_offset = 3.1,
        fade_in = 1.5,
        fade_out = 0.0
    )

    # Camera shot 11
    t.create_tl_shot('a6db4283-ef38-4472-827c-fffd0ac04a28', '33.22', '36.2')
    t.create_tl_camera_fov('a6db4283-ef38-4472-827c-fffd0ac04a28', '33.22', '36.2', (
        t.create_value_key(time = '33.22', value_name = 'FoV', value = 25.0, interpolation_type = 2),
    ))
    t.create_tl_transform('a6db4283-ef38-4472-827c-fffd0ac04a28', '33.22', '36.2', (
        (
            t.create_value_key(time = '33.22', interpolation_type = 5, value = -8.5),
        ),
        (
            t.create_value_key(time = '33.22', interpolation_type = 5, value = 1.9),
        ),
        (
            t.create_value_key(time = '33.22', interpolation_type = 5, value = -0.8),
        ),
        (
            #t.create_value_key(time = '33.22', interpolation_type = 5, value = bg3.euler_to_quaternion(54.0, 10.0, 0.0, sequence = 'yxz')),
            t.create_value_key(time = '33.22', interpolation_type = 5, value = bg3.euler_to_quaternion(62.0, 12.0, 0.0, sequence = 'yxz')),
        ),
        (),
        (),
    ))

    t.create_tl_animation(
        bg3.SPEAKER_SHADOWHEART, '33.22', '36.2',
        '91239d58-cd15-1201-a029-a685b6434723',
        '66ce0c11-1cdb-4573-818c-a91cde00f79f',
        animation_play_start_offset = 7.01,
        fade_in = 0.0,
        fade_out = 0.0
    )
    t.create_tl_animation(
        bg3.SPEAKER_DURGE, '33.22', '36.2',
        'ee52d6f6-543f-454d-93d8-71b74ff5ac12',
        '57fa3dc0-184f-4b43-93fd-86e5496448a9',
        animation_play_start_offset = 7.01,
        fade_in = 0.0,
        fade_out = 0.0
    )

    t.create_tl_voice(
        bg3.SPEAKER_SHADOWHEART, '34.127', '36.0',
        bt1_reaction_node_uuid,
        fade_in = 0.0,
        fade_out = 0.0)

    # Camera shot 12
    t.create_tl_shot('a6db4283-ef38-4472-827c-fffd0ac04a28', '36.2', '41.49', is_snapped_to_end = True)
    t.create_tl_camera_fov('a6db4283-ef38-4472-827c-fffd0ac04a28', '36.2', '41.49', (
        t.create_value_key(time = 0.0, value_name = 'FoV', value = 25.0, interpolation_type = 2),
    ))
    t.create_tl_transform('a6db4283-ef38-4472-827c-fffd0ac04a28', '36.2', '41.49', (
        (
            t.create_value_key(time = '36.2', interpolation_type = 5, value = -9.0),
        ),
        (
            t.create_value_key(time = '36.2', interpolation_type = 5, value = 1.8),
        ),
        (
            t.create_value_key(time = '36.2', interpolation_type = 5, value = -0.6),
        ),
        (
            t.create_value_key(time = '36.2', interpolation_type = 5, value = bg3.euler_to_quaternion(86.0, 4.0, 0.0, sequence = 'yxz')),
        ),
        (),
        (),
    ))

    t.create_tl_animation(
        bg3.SPEAKER_SHADOWHEART, '36.2', '54.42', #56.22,
        '91239d58-cd15-1201-a029-a685b6434723',
        '66ce0c11-1cdb-4573-818c-a91cde00f79f',
        animation_play_start_offset = 11.91,
        fade_in = 0.0,
        fade_out = 2.0
    )
    t.create_tl_animation(
        bg3.SPEAKER_DURGE, '36.2', '54.42', #56.22,
        'ee52d6f6-543f-454d-93d8-71b74ff5ac12',
        '57fa3dc0-184f-4b43-93fd-86e5496448a9',
        animation_play_start_offset = 11.91,
        fade_in = 0.0,
        fade_out = 1.0
    )

    t.create_tl_animation(
        bg3.SPEAKER_SHADOWHEART, '37.54', '41.49',
        'c26b9b0a-20cc-44a4-a499-18d6d78abec5',
        '536f3ddd-33e5-4b9d-a20a-b7109f6bbc76',
        animation_slot = 1,
        animation_play_start_offset = 6.62,
        fade_in = 1.6,
        fade_out = 0.0
    )
    t.create_tl_animation(
        bg3.SPEAKER_DURGE, '37.92', '41.49',
        'c26b9b0a-20cc-44a4-a499-18d6d78abec5',
        '90070425-bce3-4bef-b8d7-ca38a676b5cb',
        animation_slot = 1,
        animation_play_start_offset = 7,
        fade_in = 1.5,
        fade_out = 0.0
    )

    t.create_tl_animation(
        bg3.SPEAKER_DURGE, '41.49', '47.14',
        'c26b9b0a-20cc-44a4-a499-18d6d78abec5',
        '90070425-bce3-4bef-b8d7-ca38a676b5cb',
        animation_slot = 1,
        animation_play_start_offset = 3.5,
        fade_in = 0.0,
        fade_out = 1.5
    )
    t.create_tl_animation(
        bg3.SPEAKER_SHADOWHEART, '41.49', '47.14',
        'c26b9b0a-20cc-44a4-a499-18d6d78abec5',
        '536f3ddd-33e5-4b9d-a20a-b7109f6bbc76',
        animation_slot = 1,
        animation_play_start_offset = 3.5,
        fade_in = 0.0,
        fade_out = 1.5
    )

    # Camera shot 13
    t.create_tl_shot('a6db4283-ef38-4472-827c-fffd0ac04a28', '41.49', phase_duration, is_snapped_to_end = True)
    t.create_tl_camera_fov('a6db4283-ef38-4472-827c-fffd0ac04a28', '41.49', phase_duration, (
        t.create_value_key(time = '41.49', value_name = 'FoV', value = 30.0, interpolation_type = 2),
    ))
    t.create_tl_transform('a6db4283-ef38-4472-827c-fffd0ac04a28', '41.49', phase_duration, (
        (
            t.create_value_key(time = '41.49', interpolation_type = 5, value = -7.1),
        ),
        (
            t.create_value_key(time = '41.49', interpolation_type = 5, value = 1.75),
        ),
        (
            t.create_value_key(time = '41.49', interpolation_type = 5, value = -1.1),
        ),
        (
            t.create_value_key(time = '41.49', interpolation_type = 5, value = bg3.euler_to_quaternion(-60.0, 0.0, 0.0, sequence = 'yxz')),
        ),
        (),
        (),
    ))

    # Camera shot 14
    # t.create_tl_shot('a6db4283-ef38-4472-827c-fffd0ac04a28', '53.22', 56.22, is_snapped_to_end = True)
    # t.create_tl_camera_fov('a6db4283-ef38-4472-827c-fffd0ac04a28', '53.22', 56.22, (
    #     t.create_value_key(time = 53.22, value_name = 'FoV', value = 32.0, interpolation_type = 2),
    # ))
    # t.create_tl_transform('a6db4283-ef38-4472-827c-fffd0ac04a28', '53.22', 56.22, (
    #     (
    #         t.create_value_key(time = 53.22, interpolation_type = 5, value = -8.5),
    #     ),
    #     (
    #         t.create_value_key(time = 53.22, interpolation_type = 5, value = 1.75),
    #     ),
    #     (
    #         t.create_value_key(time = 53.22, interpolation_type = 5, value = -0.5),
    #     ),
    #     (
    #         #t.create_value_key(time = 53.22, interpolation_type = 5, value = bg3.euler_to_quaternion(65.0, 0.0, 0.0, sequence = 'yxz')),
    #         t.create_value_key(time = 53.22, interpolation_type = 5, value = bg3.euler_to_quaternion(45.0, 0.0, 0.0, sequence = 'yxz')),
    #     ),
    #     (),
    #     (),
    # ))


#################################################################################################
# Body type 3
#################################################################################################

def create_scene_shadowheart_reaction_body_type_3() -> None:

    # d = bg3.dialog_object(files.get_file('Gustav', 'Mods/GustavDev/Story/DialogsBinary/Act3/LowerCity/BhaalTemple/LOW_BhaalTemple_PostBattleDarkUrge_Resistance.lsf'))
    # t = bg3.timeline_object(files.get_file('Gustav', 'Public/GustavDev/Timeline/Generated/LOW_BhaalTemple_PostBattleDarkUrge_Resistance.lsf'), d)

    ab = game_assets.get_modded_dialog_asset_bundle('LOW_BhaalTemple_PostBattleDarkUrge_Resistance')
    d = bg3.dialog_object(ab.dialog)
    t = bg3.timeline_object(ab.timeline, d)

    slot_idx_durge = d.get_speaker_slot_index(bg3.SPEAKER_DURGE)
    #slot_idx_shadowheart = d.get_speaker_slot_index(bg3.SPEAKER_SHADOWHEART)

    # d.create_cinematic_dialog_node(
    #     normal_body_reaction_node_uuid,
    #     [just_keep_safe_out_there_node_uuid])
    d.create_standard_dialog_node(
        bt3_reaction_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [just_keep_safe_out_there_node_uuid],
        bg3.text_content('hd896e304g5fc4g41e7g807cg524360fee6a9', 1),
        checkflags = (
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_FEMALE, True, slot_idx_durge),
                bg3.flag(bg3.TAG_BODYTYPE_STRONG, True, slot_idx_durge),
            )),
        )
    )

    phase_duration = '53.04' # '52.5' # 53.04 # 56.37
    t.create_new_phase(bt3_reaction_node_uuid, phase_duration)

    t.create_tl_actor_node(bg3.timeline_object.ATTITUDE, bg3.SPEAKER_DURGE, '0.0', phase_duration, (
        t.create_attitude_key(12.15, bg3.ATTITUDE_DIAG_Pose_Stand_R_Forward_01, bg3.ATTITUDE_DIAG_T_Pose),
        t.create_attitude_key(28.81, 'a2bd89b1-8ab9-4231-ac4b-e593d75aa083', bg3.ATTITUDE_DIAG_T_Pose),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.ATTITUDE, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_attitude_key(0.0, bg3.ATTITUDE_DIAG_Pose_Stand_L_Forward_01, bg3.ATTITUDE_DIAG_T_Pose),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.EMOTION, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_emotion_key(0.0, 32),
        t.create_emotion_key(6.13, 32, variation = 2),
        t.create_emotion_key(7.34, 32),
        t.create_emotion_key(15.63, 32, variation = 1),
        t.create_emotion_key(20.58, 32),
        t.create_emotion_key(44.85, 32, variation = 1, is_sustained = False),
        t.create_emotion_key(51.97, 32)
        #t.create_emotion_key(26.0, 2)
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.EMOTION, bg3.SPEAKER_DURGE, '0.0', phase_duration, (
        t.create_emotion_key(0.0, 32, variation = 1),
        t.create_emotion_key(3.51, 32),
        t.create_emotion_key(6.08, 32, variation = 1),
        t.create_emotion_key(6.56, 32),
        t.create_emotion_key(8.26, 32, variation = 2),
        t.create_emotion_key(11.26, 32, variation = 1),
        t.create_emotion_key(22.03, 32),
        t.create_emotion_key(40.14, 256),
        t.create_emotion_key(44.85, 32),
    ), is_snapped_to_end = True)
    #t.create_tl_actor_node(bg3.timeline_object.EMOTION, bg3.SPEAKER_JERGAL, '0.0', phase_duration, (
    #    t.create_emotion_key(0.0, 1, None),
    #    t.create_emotion_key(25.5, 2, variation = 2),
    #), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.LOOK_AT, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_look_at_key(
            0.0,
            target = bg3.SPEAKER_DURGE,
            bone = 'Head_M',
            turn_mode = 3,
            turn_speed_multiplier = 0.3,
            torso_turn_speed_multiplier = 0.3,
            head_turn_speed_multiplier = 0.3,
            weight = 0.0,
            reset = True,
            eye_look_at_bone = 'Head_M'),
        t.create_look_at_key(
            '4.20',
            target = bg3.SPEAKER_DURGE,
            bone = 'Head_M',
            turn_mode = 3,
            turn_speed_multiplier = 0.3,
            torso_turn_speed_multiplier = 0.3,
            head_turn_speed_multiplier = 0.3,
            weight = 0.3,
            safe_zone_angle = 80.0,
            head_safe_zone_angle = 80.0,
            reset = True,
            look_at_mode = 1,
            eye_look_at_bone = 'Head_M'),
        t.create_look_at_key(
            '9.41',
            turn_mode = 3,
            turn_speed_multiplier = 0.26370612,
            torso_turn_speed_multiplier = 0.26370612,
            head_turn_speed_multiplier = 0.26370612,
            weight = 0.3,
            safe_zone_angle = 80.0,
            head_safe_zone_angle = 80.0,
            look_at_mode = 0),
        t.create_look_at_key(
            '24.27',
            target = bg3.SPEAKER_DURGE,
            bone = 'Head_M',
            turn_mode = 3,
            turn_speed_multiplier = 0.3,
            torso_turn_speed_multiplier = 0.3,
            head_turn_speed_multiplier = 0.3,
            weight = 0.0,
            safe_zone_angle = 80.0,
            head_safe_zone_angle = 80.0,
            reset = True,
            look_at_mode = 1,
            eye_look_at_bone = 'Head_M'),
        t.create_look_at_key(
            '28.81',
            target = bg3.SPEAKER_DURGE,
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
    t.create_tl_actor_node(bg3.timeline_object.LOOK_AT, bg3.SPEAKER_DURGE, '0.0', phase_duration, (
        t.create_look_at_key(
            0.0,
            target = bg3.SPEAKER_SHADOWHEART,
            bone = 'Head_M',
            turn_mode = 3,
            turn_speed_multiplier = 0.3,
            torso_turn_speed_multiplier = 0.3,
            head_turn_speed_multiplier = 0.21843724,
            weight = 0.0,
            safe_zone_angle = 80.0,
            head_safe_zone_angle = 80.0,
            look_at_mode = 1,
            eye_look_at_bone = 'Head_M'),
        t.create_look_at_key(
            '4.20',
            turn_mode = 3,
            turn_speed_multiplier = 0.3,
            torso_turn_speed_multiplier = 0.3,
            head_turn_speed_multiplier = 0.1,
            weight = 0.0,
            safe_zone_angle = 80.0,
            head_safe_zone_angle = 80.0,
            look_at_mode = 0),
        t.create_look_at_key(
            '6.56',
            target = bg3.SPEAKER_SHADOWHEART,
            bone = 'Head_M',
            turn_mode = 3,
            turn_speed_multiplier = 0.3269225,
            torso_turn_speed_multiplier = 0.3269225,
            head_turn_speed_multiplier = 0.10897417,
            weight = 0.0,
            safe_zone_angle = 80.0,
            head_safe_zone_angle = 80.0,
            look_at_mode = 1,
            eye_look_at_bone = 'Head_M'),
        t.create_look_at_key(
            '9.4',
            turn_mode = 3,
            turn_speed_multiplier = 0.25471807,
            torso_turn_speed_multiplier = 0.25471807,
            head_turn_speed_multiplier = 0.08490602,
            weight = 0.0,
            safe_zone_angle = 80.0,
            head_safe_zone_angle = 80.0,
            look_at_mode = 0),
        t.create_look_at_key(
            '24.27',
            target = bg3.SPEAKER_SHADOWHEART,
            bone = 'Head_M',
            turn_mode = 3,
            turn_speed_multiplier = 0.3,
            torso_turn_speed_multiplier = 0.3,
            head_turn_speed_multiplier = 0.1,
            weight = 0.0,
            safe_zone_angle = 80.0,
            head_safe_zone_angle = 80.0,
            reset = True,
            look_at_mode = 1,
            eye_look_at_bone = 'Head_M'),
        t.create_look_at_key(
            '28.81',
            target = bg3.SPEAKER_SHADOWHEART,
            bone = 'Head_M',
            turn_mode = 3,
            turn_speed_multiplier = 0.3,
            head_turn_speed_multiplier = 0.1,
            weight = 0.0,
            safe_zone_angle = 80.0,
            head_safe_zone_angle = 80.0,
            look_at_mode = 1,
            eye_look_at_bone = 'Head_M'),
    ), is_snapped_to_end = True)

    t.create_tl_material(bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, '156a2490-d796-402c-b7fc-e00c032042c1', (), (
        t.create_value_key(time = 0.0, value = True),
    ), is_snapped_to_end = True, is_continuous = True)

    # Hide helmets
    t.create_tl_show_armor(bg3.SPEAKER_DURGE, '0.0', phase_duration, (
        (
            t.create_value_key(time = 0.0, value = False, interpolation_type = 0),
            t.create_value_key(time = phase_duration, interpolation_type = 0)
        ),
        (), (), (), (), (), (), (), (), (), ()
    ))
    t.create_tl_show_armor(bg3.SPEAKER_SHADOWHEART, '0.0',  phase_duration, (
        (
            t.create_value_key(time = 0.0, value = False, interpolation_type = 0),
            t.create_value_key(time = phase_duration, interpolation_type = 0)
        ),
        (), (), (), (), (), (), (), (), (), ()
    ))

    # Hide weapons
    t.create_tl_actor_node(bg3.timeline_object.SHOW_WEAPON, bg3.SPEAKER_DURGE, '0.0', phase_duration, (
        t.create_value_key(time = 0.0, value_name = 'ShowWeapon', value = False, interpolation_type = 3),
        t.create_value_key(time = phase_duration, interpolation_type = 3),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.SHOW_WEAPON, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_value_key(time = 0.0, value_name = 'ShowWeapon', value = False, interpolation_type = 3),
        t.create_value_key(time = phase_duration, interpolation_type = 3),
    ), is_snapped_to_end = True)

    # Show Durge
    t.create_tl_actor_node(bg3.timeline_object.SHOW_VISUAL, bg3.SPEAKER_DURGE, '0.0', phase_duration, (
        t.create_value_key(time = 0.0, interpolation_type = 3),
    ), is_snapped_to_end = True)

    # Sounds
    # Hug part
    t.create_tl_actor_node(bg3.timeline_object.SOUND, bg3.SPEAKER_DURGE, '0.0', phase_duration, (), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.SOUND, bg3.SPEAKER_DURGE, '0.0', phase_duration, (
        t.create_sound_event_key(5.52, sound_event_id = 'd0756d07-fd81-4fab-b4af-03d565c7f059', sound_object_index = 4),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.SOUND, bg3.SPEAKER_DURGE, '0.0', phase_duration, (
        t.create_sound_event_key(8.74, sound_type = 4, foley_type = 2),
    ), is_snapped_to_end = True)

    t.create_tl_actor_node(bg3.timeline_object.SOUND, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.SOUND, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_sound_event_key(12.07, sound_event_id = '50ab7087-b822-455f-9a61-6b10b6e6d968', sound_object_index = 4),
        t.create_sound_event_key(19.2482, sound_event_id = '220abafa-e55f-4124-8cb7-16fca63fda5f', sound_object_index = 4),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.SOUND, bg3.SPEAKER_DURGE, '0.0', phase_duration, (), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.SOUND, bg3.SPEAKER_DURGE, '0.0', phase_duration, (
        t.create_sound_event_key(5.5, sound_event_id = 'c232329e-2d4e-4f0c-a4d4-ea1585fce27c', sound_object_index = 4),
        t.create_sound_event_key(7.05, sound_event_id = 'aa8db628-8c78-4632-ab7a-2ac210393e93', sound_object_index = 4),
        t.create_sound_event_key(8.745, sound_event_id = '220abafa-e55f-4124-8cb7-16fca63fda5f', sound_object_index = 4),
        t.create_sound_event_key(24.27, sound_event_id = '220abafa-e55f-4124-8cb7-16fca63fda5f', sound_object_index = 4),
    ), is_snapped_to_end = True)

    # Kiss part
    # rel diff 214.68
    t.create_tl_actor_node(bg3.timeline_object.SOUND, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_sound_event_key(40.12, sound_event_id = 'ffbbbd57-5c31-444d-bc3a-c3d14df0be53', sound_object_index = 4),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.SOUND, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_sound_event_key(37.72, sound_event_id = '90a31a12-9f32-47e1-899e-cdced0705f27', sound_object_index = 4),
        t.create_sound_event_key(37.72, sound_event_id = '025fa6be-55ec-43fe-af6a-03b746163d72', sound_object_index = 4),
        t.create_sound_event_key(38.33, sound_event_id = 'ffbbbd57-5c31-444d-bc3a-c3d14df0be53', sound_object_index = 4),
        t.create_sound_event_key(42.03, sound_event_id = 'ffbbbd57-5c31-444d-bc3a-c3d14df0be53', sound_object_index = 4),
        t.create_sound_event_key(43.69, sound_event_id = '5dac329f-b08a-412d-84bc-86fc1aecae45', sound_object_index = 4),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.SOUND, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_sound_event_key(29.56, sound_event_id = '3a82ed81-3970-461a-91dc-4687caa05cce', sound_object_index = 1),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.SOUND, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_sound_event_key(31.02, sound_event_id = '3a82ed81-3970-461a-91dc-4687caa05cce', sound_object_index = 2),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.SOUND, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (), is_snapped_to_end = True)

    # Physics
    t.create_tl_actor_node(bg3.timeline_object.PHYSICS, bg3.SPEAKER_DURGE, '0.0', phase_duration, (
        t.create_value_key(time = 0.0, interpolation_type = 3, value_name = 'InverseKinematics', value = False),
        t.create_value_key(time = '28.81', interpolation_type = 3),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.PHYSICS, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_value_key(time = 0.0, interpolation_type = 3, value_name = 'InverseKinematics', value = False),
        t.create_value_key(time = '28.81', interpolation_type = 3),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.HANDS_IK, bg3.SPEAKER_DURGE, '0.0', phase_duration, (), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.HANDS_IK, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (), is_snapped_to_end = True)

    t.create_tl_animation(
        bg3.SPEAKER_SHADOWHEART, '0.0', '16.97',
        'a70b0572-f371-49e6-854b-a8347e5db74a',
        '39e8f7e2-e600-47a8-a5c2-204b1ac9a5a7',
        fade_in = 1.0,
        fade_out = 0.0)
    t.create_tl_animation(
        bg3.SPEAKER_DURGE, '0.0', '16.97',
        'a0f79aae-f6c9-4b19-d854-3153658a1da2',
        '6ef6e0ea-2ae3-46d9-8464-99aa9ba8e427',
        fade_in = 1.0,
        fade_out = 0.0)

    t.create_tl_transform(bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = -8.0),
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

    # Camera shot 1
    t.create_tl_shot('d35b098e-8c34-45ee-9dde-21adfd2410a9', '0.0', '2.2')
    t.create_tl_camera_fov('d35b098e-8c34-45ee-9dde-21adfd2410a9', '0.0', '2.2', (
        t.create_value_key(time = 0.0, value_name = 'FoV', value = 35.0, interpolation_type = 2),
    ))
    t.create_tl_transform('d35b098e-8c34-45ee-9dde-21adfd2410a9', '0.0', '2.2', (
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = -7.5),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 1.8),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 0.2),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = bg3.euler_to_quaternion(-154.0, 0.0, 0.0, sequence = 'yxz')),
        ),
        (),
        (),
    ))

    t.create_tl_transform(bg3.SPEAKER_DURGE, '0.0', '2.2', (
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = -8.0),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 0.0),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = -0.83),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = (0.0, 1.0, 0.0, 0.0)),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 1),
        ),
        (),
    ), is_snapped_to_end = True)

    # Camera shot 2
    t.create_tl_shot('d35b098e-8c34-45ee-9dde-21adfd2410a9', '2.2', '4.2')
    t.create_tl_camera_fov('d35b098e-8c34-45ee-9dde-21adfd2410a9', '2.2', '4.2', (
        t.create_value_key(time = 0.0, value_name = 'FoV', value = 25.0, interpolation_type = 2),
    ))
    t.create_tl_transform('d35b098e-8c34-45ee-9dde-21adfd2410a9', '2.2', '4.2', (
        (
            t.create_value_key(time = 2.2, interpolation_type = 5, value = -6.5),
        ),
        (
            t.create_value_key(time = 2.2, interpolation_type = 5, value = 1.8),
        ),
        (
            t.create_value_key(time = 2.2, interpolation_type = 5, value = -1.0),
        ),
        (
            t.create_value_key(time = 2.2, interpolation_type = 5, value = bg3.euler_to_quaternion(-62.0, 0.0, 0.0, sequence = 'yxz')),
        ),
        (),
        (),
    ))

    t.create_tl_transform(bg3.SPEAKER_DURGE, '2.2', '4.2', (
        (
            t.create_value_key(time = 2.2, interpolation_type = 5, value = -8.0),
        ),
        (
            t.create_value_key(time = 2.2, interpolation_type = 5, value = -0.07),
        ),
        (
            t.create_value_key(time = 2.2, interpolation_type = 5, value = -0.83),
        ),
        (
            t.create_value_key(time = 2.2, interpolation_type = 5, value = (0.0, 1.0, 0.0, 0.0)),
        ),
        (
            t.create_value_key(time = 2.2, interpolation_type = 5, value = 1),
        ),
        (),
    ), is_snapped_to_end = True)

    # Camera shot 3
    t.create_tl_shot('d35b098e-8c34-45ee-9dde-21adfd2410a9', '4.2', '8.74')
    t.create_tl_camera_fov('d35b098e-8c34-45ee-9dde-21adfd2410a9', '4.2', '8.74', (
        t.create_value_key(time = '4.2', value_name = 'FoV', value = 15.0, interpolation_type = 2),
    ))
    t.create_tl_transform('d35b098e-8c34-45ee-9dde-21adfd2410a9', '4.2', '8.74', (
        (
            t.create_value_key(time = '4.2', interpolation_type = 5, value = -6.0),
        ),
        (
            t.create_value_key(time = '4.2', interpolation_type = 5, value = 2.0),
        ),
        (
            t.create_value_key(time = '4.2', interpolation_type = 5, value = -0.6),
        ),
        (
            t.create_value_key(time = '4.2', interpolation_type = 5, value = bg3.euler_to_quaternion(-74.0, 10.0, 0.0, sequence = 'yxz')),
        ),
        (),
        (),
    ))

    t.create_tl_transform(bg3.SPEAKER_DURGE, '4.2', '8.74', (
        (
            t.create_value_key(time = '4.2', interpolation_type = 5, value = -8.0),
        ),
        (
            t.create_value_key(time = '4.2', interpolation_type = 5, value = -0.07),
        ),
        (
            t.create_value_key(time = '4.2', interpolation_type = 5, value = -0.85),
        ),
        (
            t.create_value_key(time = '4.2', interpolation_type = 5, value = (0.0, 1.0, 0.0, 0.0)),
        ),
        (
            t.create_value_key(time = '4.2', interpolation_type = 5, value = 1),
        ),
        (),
    ), is_snapped_to_end = True)

    t.create_tl_animation(
        bg3.SPEAKER_SHADOWHEART, '4.58', '8.74',
        'a0e37a8e-c619-4d0a-840a-061831fb0523',
        '16c31857-6247-46a5-9182-28926409bcaf',
        animation_slot = 1,
        animation_play_rate = 0.6,
        animation_play_start_offset = 3.5,
        fade_in = 1.76,
        fade_out = 2.3)
    t.create_tl_animation(
        bg3.SPEAKER_DURGE, '4.58', '8.74',
        'a0e37a8e-c619-4d0a-840a-061831fb0523',
        '1913a5ea-cbf7-491b-bf3e-34c829ac69dd',
        animation_slot = 1,
        animation_play_rate = 0.6,
        animation_play_start_offset = 3.5,
        fade_in = 1.76,
        fade_out = 2.3)

    # Camera shot 4
    t.create_tl_shot('d35b098e-8c34-45ee-9dde-21adfd2410a9', '8.74', '12.07')
    t.create_tl_camera_fov('d35b098e-8c34-45ee-9dde-21adfd2410a9', '8.74', '12.07', (
        t.create_value_key(time = '8.74', value_name = 'FoV', value = 25.0, interpolation_type = 2),
    ))
    t.create_tl_transform('d35b098e-8c34-45ee-9dde-21adfd2410a9', '8.74', '12.07', (
        (
            t.create_value_key(time = '8.74', interpolation_type = 5, value = -10.0),
        ),
        (
            t.create_value_key(time = '8.74', interpolation_type = 5, value = 1.8),
        ),
        (
            t.create_value_key(time = '8.74', interpolation_type = 5, value = -0.1),
        ),
        (
            t.create_value_key(time = '8.74', interpolation_type = 5, value = bg3.euler_to_quaternion(90.0, 0.0, 0.0, sequence = 'yxz')),
        ),
        (),
        (),
    ))

    t.create_tl_transform(bg3.SPEAKER_DURGE, '8.74', '12.07', (
        (
            t.create_value_key(time = '8.74', interpolation_type = 5, value = -8.0),
        ),
        (
            t.create_value_key(time = '8.74', interpolation_type = 5, value = -0.07),
        ),
        (
            t.create_value_key(time = '8.74', interpolation_type = 5, value = -0.85),
        ),
        (
            t.create_value_key(time = '8.74', interpolation_type = 5, value = (0.0, 1.0, 0.0, 0.0)),
        ),
        (
            t.create_value_key(time = '8.74', interpolation_type = 5, value = 1),
        ),
        (),
    ), is_snapped_to_end = True)

    t.create_tl_animation(
        bg3.SPEAKER_SHADOWHEART, '9.86', '10.56',
        'a0e37a8e-c619-4d0a-840a-061831fb0523',
        '16c31857-6247-46a5-9182-28926409bcaf',
        animation_slot = 1,
        animation_play_rate = 0.6,
        animation_play_start_offset = 3,
        fade_in = 0.25)

    # Camera shot 5
    t.create_tl_shot('d35b098e-8c34-45ee-9dde-21adfd2410a9', '12.07', '16.97')
    t.create_tl_camera_fov('d35b098e-8c34-45ee-9dde-21adfd2410a9', '12.07', '16.97', (
        t.create_value_key(time = '12.07', value_name = 'FoV', value = 40.0, interpolation_type = 2),
    ))
    t.create_tl_transform('d35b098e-8c34-45ee-9dde-21adfd2410a9', '12.07', '16.97', (
        (
            t.create_value_key(time = '12.07', interpolation_type = 5, value = -8.9),
        ),
        (
            t.create_value_key(time = '12.07', interpolation_type = 5, value = 1.8),
        ),
        (
            t.create_value_key(time = '12.07', interpolation_type = 5, value = 0.4),
        ),
        (
            t.create_value_key(time = '12.07', interpolation_type = 5, value = bg3.euler_to_quaternion(115.0, 10.0, 0.0, sequence = 'yxz')),
        ),
        (),
        (),
    ))

    t.create_tl_transform(bg3.SPEAKER_DURGE, '12.07', '16.97', (
        (
            t.create_value_key(time = '12.07', interpolation_type = 5, value = -8.0),
        ),
        (
            t.create_value_key(time = '12.07', interpolation_type = 5, value = -0.07),
        ),
        (
            t.create_value_key(time = '12.07', interpolation_type = 5, value = -0.85),
        ),
        (
            t.create_value_key(time = '12.07', interpolation_type = 5, value = (0.0, 1.0, 0.0, 0.0)),
        ),
        (
            t.create_value_key(time = '12.07', interpolation_type = 5, value = 1),
        ),
        (),
    ), is_snapped_to_end = True)

    t.create_tl_animation(
        bg3.SPEAKER_SHADOWHEART, '14.43', '16.97',
        'c26b9b0a-20cc-44a4-a499-18d6d78abec5',
        '16c31857-6247-46a5-9182-28926409bcaf',
        animation_slot = 1,
        animation_play_start_offset = 10.18,
        fade_in = 1,
        fade_out = 0)

    # Camera shot 6
    t.create_tl_shot('d35b098e-8c34-45ee-9dde-21adfd2410a9', '16.97', '24.27')
    t.create_tl_camera_fov('d35b098e-8c34-45ee-9dde-21adfd2410a9', '16.97', '24.27', (
        t.create_value_key(time = '16.97', value_name = 'FoV', value = 40.0, interpolation_type = 2),
    ))
    t.create_tl_transform('d35b098e-8c34-45ee-9dde-21adfd2410a9', '16.97', '24.27', (
        (
            t.create_value_key(time = '16.97', interpolation_type = 5, value = -7.1),
        ),
        (
            t.create_value_key(time = '16.97', interpolation_type = 5, value = 1.6),
        ),
        (
            t.create_value_key(time = '16.97', interpolation_type = 5, value = 0.2),
        ),
        (
            t.create_value_key(time = '16.97', interpolation_type = 5, value = bg3.euler_to_quaternion(-117.0, 0.0, 0.0, sequence = 'yxz')),
        ),
        (),
        (),
    ))

    t.create_tl_transform(bg3.SPEAKER_DURGE, '16.97', '24.27', (
        (
            t.create_value_key(time = '16.97', interpolation_type = 5, value = -8.0),
        ),
        (
            t.create_value_key(time = '16.97', interpolation_type = 5, value = -0.07),
        ),
        (
            t.create_value_key(time = '16.97', interpolation_type = 5, value = -0.85),
        ),
        (
            t.create_value_key(time = '16.97', interpolation_type = 5, value = (0.0, 1.0, 0.0, 0.0)),
        ),
        (
            t.create_value_key(time = '16.97', interpolation_type = 5, value = 1),
        ),
        (),
    ), is_snapped_to_end = True)

    t.create_tl_animation(
        bg3.SPEAKER_SHADOWHEART, '16.97', '28.81',
        'a70b0572-f371-49e6-854b-a8347e5db74a',
        '39e8f7e2-e600-47a8-a5c2-204b1ac9a5a7',
        animation_play_start_offset = 14.0,
        fade_in = 0.0,
        fade_out = 0.0)
    t.create_tl_animation(
        bg3.SPEAKER_DURGE, '16.97', '28.81',
        'a0f79aae-f6c9-4b19-d854-3153658a1da2',
        '6ef6e0ea-2ae3-46d9-8464-99aa9ba8e427',
        animation_play_start_offset = 14.0,
        fade_in = 0.0,
        fade_out = 0.0)

    t.create_tl_animation(
        bg3.SPEAKER_SHADOWHEART, '18.68', '24.27',
        'c26b9b0a-20cc-44a4-a499-18d6d78abec5',
        '16c31857-6247-46a5-9182-28926409bcaf',
        animation_slot = 1,
        animation_play_rate = 0.2,
        animation_play_start_offset = 3,
        fade_in = 2,
        fade_out = 2.3)

    # Camera shot 7
    t.create_tl_shot('d35b098e-8c34-45ee-9dde-21adfd2410a9', '24.27', '27.205')
    t.create_tl_camera_fov('d35b098e-8c34-45ee-9dde-21adfd2410a9', '24.27', '27.205', (
        t.create_value_key(time = '24.27', value_name = 'FoV', value = 40.0, interpolation_type = 2),
    ), is_snapped_to_end = True)
    t.create_tl_transform('d35b098e-8c34-45ee-9dde-21adfd2410a9', '24.27', '27.205', (
        (
            t.create_value_key(time = '24.27', interpolation_type = 5, value = -7.3),
        ),
        (
            t.create_value_key(time = '24.27', interpolation_type = 5, value = 1.7),
        ),
        (
            t.create_value_key(time = '24.27', interpolation_type = 5, value = -0.8),
        ),
        (
            t.create_value_key(time = '24.27', interpolation_type = 5, value = bg3.euler_to_quaternion(-47.0, 0.0, 0.0, sequence = 'yxz')),
        ),
        (),
        (),
    ))

    t.create_tl_transform(bg3.SPEAKER_DURGE, '24.27', '27.205', (
        (
            t.create_value_key(time = '24.27', interpolation_type = 5, value = -8.0),
        ),
        (
            t.create_value_key(time = '24.27', interpolation_type = 5, value = -0.07),
        ),
        (
            t.create_value_key(time = '24.27', interpolation_type = 5, value = -0.85),
        ),
        (
            t.create_value_key(time = '24.27', interpolation_type = 5, value = (0.0, 1.0, 0.0, 0.0)),
        ),
        (
            t.create_value_key(time = '24.27', interpolation_type = 5, value = 1),
        ),
        (),
    ), is_snapped_to_end = True)

    # Camera shot 8
    t.create_tl_shot('d35b098e-8c34-45ee-9dde-21adfd2410a9', '27.205', '28.81')
    t.create_tl_camera_fov('d35b098e-8c34-45ee-9dde-21adfd2410a9', '27.205', '28.81', (
        t.create_value_key(time = '27.205', value_name = 'FoV', value = 40.0, interpolation_type = 2),
    ), is_snapped_to_end = True)
    t.create_tl_transform('d35b098e-8c34-45ee-9dde-21adfd2410a9', '27.205', '28.81', (
        (
            t.create_value_key(time = '27.205', interpolation_type = 5, value = -9.2),
        ),
        (
            t.create_value_key(time = '27.205', interpolation_type = 5, value = 1.5),
        ),
        (
            t.create_value_key(time = '27.205', interpolation_type = 5, value = -0.4),
        ),
        (
            t.create_value_key(time = '27.205', interpolation_type = 5, value = bg3.euler_to_quaternion(84.0, 0.0, 0.0, sequence = 'yxz')),
        ),
        (),
        (),
    ))

    t.create_tl_transform(bg3.SPEAKER_DURGE, '27.205', '28.81', (
        (
            t.create_value_key(time = '27.205', interpolation_type = 5, value = -8.0),
        ),
        (
            t.create_value_key(time = '27.205', interpolation_type = 5, value = -0.07),
        ),
        (
            t.create_value_key(time = '27.205', interpolation_type = 5, value = -0.85),
        ),
        (
            t.create_value_key(time = '27.205', interpolation_type = 5, value = (0.0, 1.0, 0.0, 0.0)),
        ),
        (
            t.create_value_key(time = '27.205', interpolation_type = 5, value = 1),
        ),
        (),
    ), is_snapped_to_end = True)

    # Camera shot 10
    t.create_tl_shot('a6db4283-ef38-4472-827c-fffd0ac04a28', '28.81', '33.65')
    t.create_tl_camera_fov('a6db4283-ef38-4472-827c-fffd0ac04a28', '28.81', '33.65', (
        t.create_value_key(time = 0.0, value_name = 'FoV', value = 30.0, interpolation_type = 2),
    ))
    t.create_tl_transform('a6db4283-ef38-4472-827c-fffd0ac04a28', '28.81', '33.65', (
        (
            t.create_value_key(time = '28.81', interpolation_type = 5, value = -7.1),
        ),
        (
            t.create_value_key(time = '28.81', interpolation_type = 5, value = 1.9),
        ),
        (
            t.create_value_key(time = '28.81', interpolation_type = 5, value = -1.2),
        ),
        (
            #t.create_value_key(time = '28.81', interpolation_type = 5, value = bg3.euler_to_quaternion(-38.0, 10.0, 0.0, sequence = 'yxz')),
            t.create_value_key(time = '28.81', interpolation_type = 5, value = bg3.euler_to_quaternion(-44.0, 10.0, 0.0, sequence = 'yxz')),
        ),
        (),
        (),
    ))

    t.create_tl_transform(bg3.SPEAKER_DURGE, '28.81', phase_duration, (
        (
            t.create_value_key(time = '28.81', interpolation_type = 5, value = -8.0),
        ),
        (
            t.create_value_key(time = '28.81', interpolation_type = 5, value = 0.0),
        ),
        (
            t.create_value_key(time = '28.81', interpolation_type = 5, value = -0.83),
        ),
        (
            t.create_value_key(time = '28.81', interpolation_type = 5, value = (0.0, 1.0, 0.0, 0.0)),
        ),
        (
            t.create_value_key(time = '28.81', interpolation_type = 5, value = 1),
        ),
        (),
    ), is_snapped_to_end = True)

    t.create_tl_animation(
        bg3.SPEAKER_SHADOWHEART, '28.81', '33.65',
        '79f7f289-33bf-1a3f-5b94-c093b06428ba',
        '66ce0c11-1cdb-4573-818c-a91cde00f79f',
        animation_play_start_offset = 3.1,
        fade_in = 0.0,
        fade_out = 0.0
    )
    t.create_tl_animation(
        bg3.SPEAKER_DURGE, '28.81', '33.65',
        'ac3a80f9-9794-4eb9-8118-9b85505daf9b',
        '57fa3dc0-184f-4b43-93fd-86e5496448a9',
        animation_play_start_offset = 3.1,
        fade_in = 1.5,
        fade_out = 0.0
    )

    # Camera shot 11
    t.create_tl_shot('a6db4283-ef38-4472-827c-fffd0ac04a28', '33.65', '40.24')
    t.create_tl_camera_fov('a6db4283-ef38-4472-827c-fffd0ac04a28', '33.65', '40.24', (
        t.create_value_key(time = '33.65', value_name = 'FoV', value = 22.0, interpolation_type = 2),
    ))
    # t.create_tl_transform('a6db4283-ef38-4472-827c-fffd0ac04a28', '33.65', '40.24', (
    #     (
    #         t.create_value_key(time = 33.65, interpolation_type = 5, value = -8.5),
    #     ),
    #     (
    #         t.create_value_key(time = 33.65, interpolation_type = 5, value = 1.9),
    #     ),
    #     (
    #         t.create_value_key(time = 33.65, interpolation_type = 5, value = -0.8),
    #     ),
    #     (
    #         t.create_value_key(time = 33.65, interpolation_type = 5, value = bg3.euler_to_quaternion(62.0, 12.0, 0.0, sequence = 'yxz')),
    #     ),
    #     (),
    #     (),
    # ))
    t.create_tl_transform('a6db4283-ef38-4472-827c-fffd0ac04a28', '33.65', '40.24', (
        (
            t.create_value_key(time = 33.65, interpolation_type = 5, value = -7.1),
        ),
        (
            t.create_value_key(time = 33.65, interpolation_type = 5, value = 1.9),
        ),
        (
            t.create_value_key(time = 33.65, interpolation_type = 5, value = -0.9),
        ),
        (
            #t.create_value_key(time = 33.65, interpolation_type = 5, value = bg3.euler_to_quaternion(-38.0, 10.0, 0.0, sequence = 'yxz')),
            t.create_value_key(time = 33.65, interpolation_type = 5, value = bg3.euler_to_quaternion(-64.0, 10.0, 0.0, sequence = 'yxz')),
        ),
        (),
        (),
    ))

    t.create_tl_animation(
        bg3.SPEAKER_SHADOWHEART, '33.65', '53.04', #56.37,
        '79f7f289-33bf-1a3f-5b94-c093b06428ba',
        '66ce0c11-1cdb-4573-818c-a91cde00f79f',
        animation_play_start_offset = 10.61,
        fade_in = 0.0,
        fade_out = 2.5
    )
    t.create_tl_animation(
        bg3.SPEAKER_DURGE, '33.65', phase_duration, #56.37,
        'ac3a80f9-9794-4eb9-8118-9b85505daf9b',
        '57fa3dc0-184f-4b43-93fd-86e5496448a9',
        animation_play_start_offset = 10.61,
        fade_in = 0.0,
        fade_out = 1.0
    )

    t.create_tl_voice(
        bg3.SPEAKER_SHADOWHEART, '34.127', '36.0',
        bt3_reaction_node_uuid,
        fade_in = 0.0,
        fade_out = 0.0)

    t.create_tl_animation(
        bg3.SPEAKER_SHADOWHEART, '36.67', '45.16',
        'c26b9b0a-20cc-44a4-a499-18d6d78abec5',
        '536f3ddd-33e5-4b9d-a20a-b7109f6bbc76',
        animation_slot = 1,
        animation_play_start_offset = 6,
        fade_in = 1.5,
        fade_out = 1.8
    )
    t.create_tl_animation(
        bg3.SPEAKER_DURGE, '36.67', '45.16',
        'c26b9b0a-20cc-44a4-a499-18d6d78abec5',
        '90070425-bce3-4bef-b8d7-ca38a676b5cb',
        animation_slot = 1,
        animation_play_start_offset = 6,
        fade_in = 1.5,
        fade_out = 1.8
    )

    # Camera shot 12
    t.create_tl_shot('a6db4283-ef38-4472-827c-fffd0ac04a28', '40.24', phase_duration, is_snapped_to_end = True)
    t.create_tl_camera_fov('a6db4283-ef38-4472-827c-fffd0ac04a28', '40.24', phase_duration, (
        t.create_value_key(time = 0.0, value_name = 'FoV', value = 25.0, interpolation_type = 2),
    ))
    t.create_tl_transform('a6db4283-ef38-4472-827c-fffd0ac04a28', '40.24', phase_duration, (
        (
            t.create_value_key(time = '40.24', interpolation_type = 5, value = -9.0),
        ),
        (
            t.create_value_key(time = '40.24', interpolation_type = 5, value = 1.8),
        ),
        (
            t.create_value_key(time = '40.24', interpolation_type = 5, value = -0.6),
        ),
        (
            t.create_value_key(time = '40.24', interpolation_type = 5, value = bg3.euler_to_quaternion(86.0, 4.0, 0.0, sequence = 'yxz')),
        ),
        (),
        (),
    ))


    # Camera shot 13
    # t.create_tl_shot('a6db4283-ef38-4472-827c-fffd0ac04a28', '53.04', '53.22', is_snapped_to_end = True)
    # t.create_tl_camera_fov('a6db4283-ef38-4472-827c-fffd0ac04a28', '41.49', '53.22', (
    #     t.create_value_key(time = '41.49', value_name = 'FoV', value = 30.0, interpolation_type = 2),
    # ))
    # t.create_tl_transform('a6db4283-ef38-4472-827c-fffd0ac04a28', '41.49', '53.22', (
    #     (
    #         t.create_value_key(time = '41.49', interpolation_type = 5, value = -7.1),
    #     ),
    #     (
    #         t.create_value_key(time = '41.49', interpolation_type = 5, value = 1.75),
    #     ),
    #     (
    #         t.create_value_key(time = '41.49', interpolation_type = 5, value = -1.1),
    #     ),
    #     (
    #         t.create_value_key(time = '41.49', interpolation_type = 5, value = bg3.euler_to_quaternion(-60.0, 0.0, 0.0, sequence = 'yxz')),
    #     ),
    #     (),
    #     (),
    # ))

    # Camera shot 14
    # t.create_tl_shot('a6db4283-ef38-4472-827c-fffd0ac04a28', '53.04', 56.37, is_snapped_to_end = True)
    # t.create_tl_camera_fov('a6db4283-ef38-4472-827c-fffd0ac04a28', '53.04', 56.37, (
    #     t.create_value_key(time = 53.04, value_name = 'FoV', value = 32.0, interpolation_type = 2),
    # ))
    # t.create_tl_transform('a6db4283-ef38-4472-827c-fffd0ac04a28', '53.04', 56.37, (
    #     (
    #         t.create_value_key(time = 53.04, interpolation_type = 5, value = -8.5),
    #     ),
    #     (
    #         t.create_value_key(time = 53.04, interpolation_type = 5, value = 1.75),
    #     ),
    #     (
    #         t.create_value_key(time = 53.04, interpolation_type = 5, value = -0.5),
    #     ),
    #     (
    #         #t.create_value_key(time = 53.22, interpolation_type = 5, value = bg3.euler_to_quaternion(65.0, 0.0, 0.0, sequence = 'yxz')),
    #         t.create_value_key(time = 53.04, interpolation_type = 5, value = bg3.euler_to_quaternion(45.0, 0.0, 0.0, sequence = 'yxz')),
    #     ),
    #     (),
    #     (),
    # ))


#################################################################################################
# Body type 4
#################################################################################################

def create_scene_shadowheart_reaction_body_type_4() -> None:

    # d = bg3.dialog_object(files.get_file('Gustav', 'Mods/GustavDev/Story/DialogsBinary/Act3/LowerCity/BhaalTemple/LOW_BhaalTemple_PostBattleDarkUrge_Resistance.lsf'))
    # t = bg3.timeline_object(files.get_file('Gustav', 'Public/GustavDev/Timeline/Generated/LOW_BhaalTemple_PostBattleDarkUrge_Resistance.lsf'), d)

    ab = game_assets.get_modded_dialog_asset_bundle('LOW_BhaalTemple_PostBattleDarkUrge_Resistance')
    d = bg3.dialog_object(ab.dialog)
    t = bg3.timeline_object(ab.timeline, d)

    slot_idx_durge = d.get_speaker_slot_index(bg3.SPEAKER_DURGE)
    #slot_idx_shadowheart = d.get_speaker_slot_index(bg3.SPEAKER_SHADOWHEART)

    d.create_standard_dialog_node(
        bt4_reaction_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [just_keep_safe_out_there_node_uuid],
        bg3.text_content('hd896e304g5fc4g41e7g807cg524360fee6a9', 1),
        checkflags = (
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_BODYTYPE_STRONG, True, slot_idx_durge),
            )),
        )
    )

    # 24.55
    # 28.81
    # 4.26
    #d = 1.8
    phase_duration = '48.28'
    t.create_new_phase(bt4_reaction_node_uuid, phase_duration)

    t.create_tl_actor_node(bg3.timeline_object.ATTITUDE, bg3.SPEAKER_DURGE, '0.0', phase_duration, (
        t.create_attitude_key(12.15, bg3.ATTITUDE_DIAG_Pose_Stand_R_Forward_01, bg3.ATTITUDE_DIAG_T_Pose),
        t.create_attitude_key(28.81, 'a2bd89b1-8ab9-4231-ac4b-e593d75aa083', bg3.ATTITUDE_DIAG_T_Pose),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.ATTITUDE, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_attitude_key(0.0, bg3.ATTITUDE_DIAG_Pose_Stand_L_Forward_01, bg3.ATTITUDE_DIAG_T_Pose),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.EMOTION, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_emotion_key(0.0, 32),
        t.create_emotion_key(6.13, 32, variation = 2),
        t.create_emotion_key(7.34, 32),
        t.create_emotion_key(15.63, 32, variation = 1),
        t.create_emotion_key(20.58, 32),
        t.create_emotion_key(44.85 - 4.26, 32, variation = 1, is_sustained = False),
        t.create_emotion_key(51.97 - 4.26, 32)
        #t.create_emotion_key(26.0, 2)
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.EMOTION, bg3.SPEAKER_DURGE, '0.0', phase_duration, (
        t.create_emotion_key(0.0, 32, variation = 1),
        t.create_emotion_key(3.51, 32),
        t.create_emotion_key(6.08, 32, variation = 1),
        t.create_emotion_key(6.56, 32),
        t.create_emotion_key(8.26, 32, variation = 2),
        t.create_emotion_key(11.26, 32, variation = 1),
        t.create_emotion_key(22.03, 32),
        t.create_emotion_key(40.14 - 4.26, 256),
        t.create_emotion_key(44.85 - 4.26, 32),
    ), is_snapped_to_end = True)

    t.create_tl_actor_node(bg3.timeline_object.LOOK_AT, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_look_at_key(
            0.0,
            target = bg3.SPEAKER_DURGE,
            bone = 'Head_M',
            turn_mode = 3,
            turn_speed_multiplier = 0.3,
            head_turn_speed_multiplier = 0.3,
            weight = 0,
            safe_zone_angle = 80,
            head_safe_zone_angle = 80,
            reset = True,
            look_at_mode = 1,
            eye_look_at_bone = 'Head_M'),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.LOOK_AT, bg3.SPEAKER_DURGE, '0.0', phase_duration, (
        t.create_look_at_key(
            0.0,
            target = bg3.SPEAKER_SHADOWHEART,
            bone = 'Head_M',
            turn_mode = 3,
            turn_speed_multiplier = 0.3,
            head_turn_speed_multiplier = 0.3,
            weight = 0,
            safe_zone_angle = 80,
            head_safe_zone_angle = 80,
            reset = True,
            look_at_mode = 1,
            eye_look_at_bone = 'Head_M'),
    ), is_snapped_to_end = True)

    t.create_tl_material(bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, '156a2490-d796-402c-b7fc-e00c032042c1', (), (
        t.create_value_key(time = 0.0, value = True),
    ), is_snapped_to_end = True, is_continuous = True)

    # Hide helmets
    t.create_tl_show_armor(bg3.SPEAKER_DURGE, '0.0', phase_duration, (
        (
            t.create_value_key(time = 0.0, value = False, interpolation_type = 0),
            t.create_value_key(time = phase_duration, interpolation_type = 0)
        ),
        (), (), (), (), (), (), (), (), (), ()
    ))
    t.create_tl_show_armor(bg3.SPEAKER_SHADOWHEART, '0.0',  phase_duration, (
        (
            t.create_value_key(time = 0.0, value = False, interpolation_type = 0),
            t.create_value_key(time = phase_duration, interpolation_type = 0)
        ),
        (), (), (), (), (), (), (), (), (), ()
    ))

    # Hide weapons
    t.create_tl_actor_node(bg3.timeline_object.SHOW_WEAPON, bg3.SPEAKER_DURGE, '0.0', phase_duration, (
        t.create_value_key(time = 0.0, value_name = 'ShowWeapon', value = False, interpolation_type = 3),
        t.create_value_key(time = phase_duration, interpolation_type = 3),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.SHOW_WEAPON, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_value_key(time = 0.0, value_name = 'ShowWeapon', value = False, interpolation_type = 3),
        t.create_value_key(time = phase_duration, interpolation_type = 3),
    ), is_snapped_to_end = True)

    # Show Durge
    t.create_tl_actor_node(bg3.timeline_object.SHOW_VISUAL, bg3.SPEAKER_DURGE, '0.0', phase_duration, (
        t.create_value_key(time = 0.0, interpolation_type = 3),
    ), is_snapped_to_end = True)

    # Sounds
    # Hug part
    # t.create_tl_actor_node(bg3.timeline_object.SOUND, bg3.SPEAKER_DURGE, '0.0', phase_duration, (), is_snapped_to_end = True)
    # t.create_tl_actor_node(bg3.timeline_object.SOUND, bg3.SPEAKER_DURGE, '0.0', phase_duration, (
    #     t.create_sound_event_key(5.52, sound_event_id = 'd0756d07-fd81-4fab-b4af-03d565c7f059', sound_object_index = 4),
    # ), is_snapped_to_end = True)
    # t.create_tl_actor_node(bg3.timeline_object.SOUND, bg3.SPEAKER_DURGE, '0.0', phase_duration, (
    #     t.create_sound_event_key(8.74, sound_type = 4, foley_type = 2),
    # ), is_snapped_to_end = True)

    # t.create_tl_actor_node(bg3.timeline_object.SOUND, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (), is_snapped_to_end = True)
    # t.create_tl_actor_node(bg3.timeline_object.SOUND, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
    #     t.create_sound_event_key(12.07, sound_event_id = '50ab7087-b822-455f-9a61-6b10b6e6d968', sound_object_index = 4),
    #     t.create_sound_event_key(19.2482, sound_event_id = '220abafa-e55f-4124-8cb7-16fca63fda5f', sound_object_index = 4),
    # ), is_snapped_to_end = True)
    # t.create_tl_actor_node(bg3.timeline_object.SOUND, bg3.SPEAKER_DURGE, '0.0', phase_duration, (), is_snapped_to_end = True)
    # t.create_tl_actor_node(bg3.timeline_object.SOUND, bg3.SPEAKER_DURGE, '0.0', phase_duration, (
    #     t.create_sound_event_key(5.5, sound_event_id = 'c232329e-2d4e-4f0c-a4d4-ea1585fce27c', sound_object_index = 4),
    #     t.create_sound_event_key(7.05, sound_event_id = 'aa8db628-8c78-4632-ab7a-2ac210393e93', sound_object_index = 4),
    #     t.create_sound_event_key(8.745, sound_event_id = '220abafa-e55f-4124-8cb7-16fca63fda5f', sound_object_index = 4),
    #     t.create_sound_event_key(24.27, sound_event_id = '220abafa-e55f-4124-8cb7-16fca63fda5f', sound_object_index = 4),
    # ), is_snapped_to_end = True)

    # Kiss part
    # rel diff 214.68
    t.create_tl_actor_node(bg3.timeline_object.SOUND, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_sound_event_key('34.06', sound_event_id = 'ffbbbd57-5c31-444d-bc3a-c3d14df0be53', sound_object_index = 4),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.SOUND, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_sound_event_key('31.66', sound_event_id = '90a31a12-9f32-47e1-899e-cdced0705f27', sound_object_index = 4),
        t.create_sound_event_key('31.66', sound_event_id = '025fa6be-55ec-43fe-af6a-03b746163d72', sound_object_index = 4),
        t.create_sound_event_key('32.27', sound_event_id = 'ffbbbd57-5c31-444d-bc3a-c3d14df0be53', sound_object_index = 4),
        t.create_sound_event_key('35.97', sound_event_id = 'ffbbbd57-5c31-444d-bc3a-c3d14df0be53', sound_object_index = 4),
        t.create_sound_event_key('37.63', sound_event_id = '5dac329f-b08a-412d-84bc-86fc1aecae45', sound_object_index = 4),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.SOUND, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_sound_event_key('23.5', sound_event_id = '3a82ed81-3970-461a-91dc-4687caa05cce', sound_object_index = 1),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.SOUND, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_sound_event_key('24.96', sound_event_id = '3a82ed81-3970-461a-91dc-4687caa05cce', sound_object_index = 2),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.SOUND, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (), is_snapped_to_end = True)

    # Physics
    t.create_tl_actor_node(bg3.timeline_object.PHYSICS, bg3.SPEAKER_DURGE, '0.0', phase_duration, (
        t.create_value_key(time = 0.0, interpolation_type = 3, value_name = 'InverseKinematics', value = False),
        t.create_value_key(time = '22.75', interpolation_type = 3),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.PHYSICS, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_value_key(time = 0.0, interpolation_type = 3, value_name = 'InverseKinematics', value = False),
        t.create_value_key(time = '22.75', interpolation_type = 3),
    ), is_snapped_to_end = True)
    # t.create_tl_actor_node(bg3.timeline_object.PHYSICS, bg3.SPEAKER_DURGE, '0.0', phase_duration, (
    #     t.create_value_key(time = 24.55, interpolation_type = 3),
    # ), is_snapped_to_end = True)
    # t.create_tl_actor_node(bg3.timeline_object.PHYSICS, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
    #     t.create_value_key(time = 24.55, interpolation_type = 3),
    # ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.HANDS_IK, bg3.SPEAKER_DURGE, '0.0', phase_duration, (), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.HANDS_IK, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (), is_snapped_to_end = True)

    t.create_tl_animation(
        bg3.SPEAKER_DURGE,
        '0.0', '13.06',
        'fb8fbad0-57be-4c54-936b-a58c8fa46876',
        'a2dae3f2-e3c9-4fc7-b8ac-82abf4a153b0',
        fade_in = 0.0,
        fade_out = 0.94)
    t.create_tl_animation(
        bg3.SPEAKER_SHADOWHEART,
        '0.0', '13.06',
        'd8684f69-0a63-33dd-3304-87e0128c21ba',
        'c8dad77b-5b76-44fe-bfeb-61d676ede3f6',
        fade_in = 0.0,
        fade_out = 0.94)

    t.create_tl_transform(bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = -8.0),
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

    t.create_tl_transform(bg3.SPEAKER_DURGE, '0.0', '24.55', (
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = -8.0),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 0.0),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = -0.79),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = (0.0, 1.0, 0.0, 0.0)),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 1),
        ),
        (),
    ), is_snapped_to_end = True)


    # Camera shot 2
    t.create_tl_shot('d35b098e-8c34-45ee-9dde-21adfd2410a9', '0.0', '4.2')
    t.create_tl_camera_fov('d35b098e-8c34-45ee-9dde-21adfd2410a9', '0.0', '4.2', (
        t.create_value_key(time = 0.0, value_name = 'FoV', value = 35.0, interpolation_type = 2),
    ))
    t.create_tl_transform('d35b098e-8c34-45ee-9dde-21adfd2410a9', '0.0', '4.2', (
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = -6.5),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 1.8),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = -1.0),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = bg3.euler_to_quaternion(-62.0, 0.0, 0.0, sequence = 'yxz')),
        ),
        (),
        (),
    ))

    # Camera shot 3
    t.create_tl_shot('d35b098e-8c34-45ee-9dde-21adfd2410a9', '4.2', '8.74')
    t.create_tl_camera_fov('d35b098e-8c34-45ee-9dde-21adfd2410a9', '4.2', '8.74', (
        t.create_value_key(time = '4.2', value_name = 'FoV', value = 30.0, interpolation_type = 2),
    ))
    t.create_tl_transform('d35b098e-8c34-45ee-9dde-21adfd2410a9', '4.2', '8.74', (
        (
            t.create_value_key(time = '4.2', interpolation_type = 5, value = -6.0),
        ),
        (
            t.create_value_key(time = '4.2', interpolation_type = 5, value = 2.0),
        ),
        (
            t.create_value_key(time = '4.2', interpolation_type = 5, value = -0.6),
        ),
        (
            t.create_value_key(time = '4.2', interpolation_type = 5, value = bg3.euler_to_quaternion(-74.0, 10.0, 0.0, sequence = 'yxz')),
        ),
        (),
        (),
    ))

    # Camera shot 4
    t.create_tl_shot('d35b098e-8c34-45ee-9dde-21adfd2410a9', '8.74', '12.07')
    t.create_tl_camera_fov('d35b098e-8c34-45ee-9dde-21adfd2410a9', '8.74', '12.07', (
        t.create_value_key(time = '8.74', value_name = 'FoV', value = 25.0, interpolation_type = 2),
    ))
    t.create_tl_transform('d35b098e-8c34-45ee-9dde-21adfd2410a9', '8.74', '12.07', (
        (
            t.create_value_key(time = '8.74', interpolation_type = 5, value = -10.0),
        ),
        (
            t.create_value_key(time = '8.74', interpolation_type = 5, value = 1.8),
        ),
        (
            t.create_value_key(time = '8.74', interpolation_type = 5, value = -0.1),
        ),
        (
            t.create_value_key(time = '8.74', interpolation_type = 5, value = bg3.euler_to_quaternion(90.0, 0.0, 0.0, sequence = 'yxz')),
        ),
        (),
        (),
    ))


    t.create_tl_animation(
        bg3.SPEAKER_DURGE,
        '12.12', '22.75',
        'fb8fbad0-57be-4c54-936b-a58c8fa46876',
        'a2dae3f2-e3c9-4fc7-b8ac-82abf4a153b0',
        fade_in = 0.0,
        fade_out = 0.0,
        animation_play_start_offset = 6.29)
    t.create_tl_animation(
        bg3.SPEAKER_SHADOWHEART,
        '12.12', '22.75',
        'd8684f69-0a63-33dd-3304-87e0128c21ba',
        'c8dad77b-5b76-44fe-bfeb-61d676ede3f6',
        fade_in = 0.0,
        fade_out = 0.0,
        animation_play_start_offset = 6.29)

    # Camera shot 5
    t.create_tl_shot('d35b098e-8c34-45ee-9dde-21adfd2410a9', '12.07', '16.97')
    t.create_tl_camera_fov('d35b098e-8c34-45ee-9dde-21adfd2410a9', '12.07', '16.97', (
        t.create_value_key(time = '12.07', value_name = 'FoV', value = 35.0, interpolation_type = 2),
    ))
    t.create_tl_transform('d35b098e-8c34-45ee-9dde-21adfd2410a9', '12.07', '16.97', (
        (
            t.create_value_key(time = '12.07', interpolation_type = 5, value = -8.9),
        ),
        (
            t.create_value_key(time = '12.07', interpolation_type = 5, value = 1.8),
        ),
        (
            t.create_value_key(time = '12.07', interpolation_type = 5, value = 0.4),
        ),
        (
            t.create_value_key(time = '12.07', interpolation_type = 5, value = bg3.euler_to_quaternion(115.0, 10.0, 0.0, sequence = 'yxz')),
        ),
        (),
        (),
    ))

    # Camera shot 6
    t.create_tl_shot('d35b098e-8c34-45ee-9dde-21adfd2410a9', '16.97', '22.75')
    t.create_tl_camera_fov('d35b098e-8c34-45ee-9dde-21adfd2410a9', '16.97', '22.75', (
        t.create_value_key(time = '16.97', value_name = 'FoV', value = 35.0, interpolation_type = 2),
    ))
    t.create_tl_transform('d35b098e-8c34-45ee-9dde-21adfd2410a9', '16.97', '22.75', (
        (
            t.create_value_key(time = '16.97', interpolation_type = 5, value = -7.1),
        ),
        (
            t.create_value_key(time = '16.97', interpolation_type = 5, value = 1.75),
        ),
        (
            t.create_value_key(time = '16.97', interpolation_type = 5, value = 0.2),
        ),
        (
            t.create_value_key(time = '16.97', interpolation_type = 5, value = bg3.euler_to_quaternion(-117.0, 0.0, 0.0, sequence = 'yxz')),
        ),
        (),
        (),
    ))

    # t.create_tl_animation(
    #     bg3.SPEAKER_DURGE,
    #     17.79 + 3.88, '24.55',
    #     '882164de-1f6b-4d2a-b336-1f366cb36f14',
    #     'a2dae3f2-e3c9-4fc7-b8ac-82abf4a153b0',
    #     fade_in = 0.0,
    #     fade_out = 2.0,
    #     animation_play_start_offset = 16.79,
    #     is_snapped_to_end = True)
    # t.create_tl_animation(
    #     bg3.SPEAKER_SHADOWHEART,
    #     17.79 + 3.88, '24.55',
    #     'a46f695f-051b-be6d-20cd-32f733524930',
    #     'c8dad77b-5b76-44fe-bfeb-61d676ede3f6',
    #     fade_in = 0.0,
    #     fade_out = 1.44,
    #     animation_play_start_offset = 16.79,
    #     is_snapped_to_end = True)


    # # Camera shot 7
    # t.create_tl_shot('d35b098e-8c34-45ee-9dde-21adfd2410a9', '24.27', '27.205')
    # t.create_tl_camera_fov('d35b098e-8c34-45ee-9dde-21adfd2410a9', '24.27', '27.205', (
    #     t.create_value_key(time = '24.27', value_name = 'FoV', value = 25.0, interpolation_type = 2),
    # ), is_snapped_to_end = True)
    # t.create_tl_transform('d35b098e-8c34-45ee-9dde-21adfd2410a9', '24.27', '27.205', (
    #     (
    #         t.create_value_key(time = '24.27', interpolation_type = 5, value = -7.3),
    #     ),
    #     (
    #         t.create_value_key(time = '24.27', interpolation_type = 5, value = 1.7),
    #     ),
    #     (
    #         t.create_value_key(time = '24.27', interpolation_type = 5, value = -0.8),
    #     ),
    #     (
    #         t.create_value_key(time = '24.27', interpolation_type = 5, value = bg3.euler_to_quaternion(-47.0, 0.0, 0.0, sequence = 'yxz')),
    #     ),
    #     (),
    #     (),
    # ))

    # # Camera shot 8
    # t.create_tl_shot('d35b098e-8c34-45ee-9dde-21adfd2410a9', '27.205', '28.81')
    # t.create_tl_camera_fov('d35b098e-8c34-45ee-9dde-21adfd2410a9', '27.205', '28.81', (
    #     t.create_value_key(time = '27.205', value_name = 'FoV', value = 25.0, interpolation_type = 2),
    # ), is_snapped_to_end = True)
    # t.create_tl_transform('d35b098e-8c34-45ee-9dde-21adfd2410a9', '27.205', '28.81', (
    #     (
    #         t.create_value_key(time = '27.205', interpolation_type = 5, value = -9.2),
    #     ),
    #     (
    #         t.create_value_key(time = '27.205', interpolation_type = 5, value = 1.65),
    #     ),
    #     (
    #         t.create_value_key(time = '27.205', interpolation_type = 5, value = -0.4),
    #     ),
    #     (
    #         t.create_value_key(time = '27.205', interpolation_type = 5, value = bg3.euler_to_quaternion(84.0, 0.0, 0.0, sequence = 'yxz')),
    #     ),
    #     (),
    #     (),
    # ))

    # Camera shot 10
    t.create_tl_shot('a6db4283-ef38-4472-827c-fffd0ac04a28', '22.75', '27.59')
    t.create_tl_camera_fov('a6db4283-ef38-4472-827c-fffd0ac04a28', '22.75', '27.59', (
        t.create_value_key(time = 0.0, value_name = 'FoV', value = 30.0, interpolation_type = 2),
    ))
    t.create_tl_transform('a6db4283-ef38-4472-827c-fffd0ac04a28', '22.75', '27.59', (
        (
            t.create_value_key(time = '22.75', interpolation_type = 5, value = -7.1),
        ),
        (
            t.create_value_key(time = '22.75', interpolation_type = 5, value = 1.9),
        ),
        (
            t.create_value_key(time = '22.75', interpolation_type = 5, value = -1.2),
        ),
        (
            t.create_value_key(time = '22.75', interpolation_type = 5, value = bg3.euler_to_quaternion(-44.0, 10.0, 0.0, sequence = 'yxz')),
        ),
        (),
        (),
    ))

    t.create_tl_transform(bg3.SPEAKER_DURGE, '22.75', phase_duration, (
        (
            t.create_value_key(time = '22.75', interpolation_type = 5, value = -8.0),
        ),
        (
            t.create_value_key(time = '22.75', interpolation_type = 5, value = 0.0),
        ),
        (
            t.create_value_key(time = '22.75', interpolation_type = 5, value = -0.83),
        ),
        (
            t.create_value_key(time = '22.75', interpolation_type = 5, value = (0.0, 1.0, 0.0, 0.0)),
        ),
        (
            t.create_value_key(time = '22.75', interpolation_type = 5, value = 1),
        ),
        (),
    ), is_snapped_to_end = True)

    t.create_tl_animation(
        bg3.SPEAKER_SHADOWHEART, '22.75', '27.59',
        '79f7f289-33bf-1a3f-5b94-c093b06428ba',
        '66ce0c11-1cdb-4573-818c-a91cde00f79f',
        animation_play_start_offset = 3.1,
        fade_in = 0.0,
        fade_out = 0.0
    )
    t.create_tl_animation(
        bg3.SPEAKER_DURGE, '22.75', '27.59',
        'ac3a80f9-9794-4eb9-8118-9b85505daf9b',
        '57fa3dc0-184f-4b43-93fd-86e5496448a9',
        animation_play_start_offset = 3.1,
        fade_in = 1.5,
        fade_out = 0.0
    )

    # Camera shot 11
    t.create_tl_shot('a6db4283-ef38-4472-827c-fffd0ac04a28', '27.59', '34.18')
    t.create_tl_camera_fov('a6db4283-ef38-4472-827c-fffd0ac04a28', '27.59', '34.18', (
        t.create_value_key(time = '27.59', value_name = 'FoV', value = 22.0, interpolation_type = 2),
    ))
    t.create_tl_transform('a6db4283-ef38-4472-827c-fffd0ac04a28', '27.59', '34.18', (
        (
            t.create_value_key(time = '27.59', interpolation_type = 5, value = -7.1),
        ),
        (
            t.create_value_key(time = '27.59', interpolation_type = 5, value = 1.9),
        ),
        (
            t.create_value_key(time = '27.59', interpolation_type = 5, value = -0.9),
        ),
        (
            t.create_value_key(time = '27.59', interpolation_type = 5, value = bg3.euler_to_quaternion(-65.0, 10.0, 0.0, sequence = 'yxz')),
        ),
        (),
        (),
    ))

    t.create_tl_animation(
        bg3.SPEAKER_SHADOWHEART, '27.59', '48.28',
        '79f7f289-33bf-1a3f-5b94-c093b06428ba',
        '66ce0c11-1cdb-4573-818c-a91cde00f79f',
        animation_play_start_offset = 10.61,
        fade_in = 0.0,
        fade_out = 1.7
    )
    t.create_tl_animation(
        bg3.SPEAKER_DURGE, '27.59', '48.28',
        'ac3a80f9-9794-4eb9-8118-9b85505daf9b',
        '57fa3dc0-184f-4b43-93fd-86e5496448a9',
        animation_play_start_offset = 10.61,
        fade_in = 0.0,
        fade_out = 1.0
    )

    t.create_tl_voice(
        bg3.SPEAKER_SHADOWHEART, '28.067', '29.94',
        bt4_reaction_node_uuid,
        fade_in = 0.0,
        fade_out = 0.0)

    t.create_tl_animation(
        bg3.SPEAKER_SHADOWHEART, '30.61', '39.1',
        'c26b9b0a-20cc-44a4-a499-18d6d78abec5',
        '536f3ddd-33e5-4b9d-a20a-b7109f6bbc76',
        animation_slot = 1,
        animation_play_start_offset = 6,
        fade_in = 1.5,
        fade_out = 1.8
    )
    t.create_tl_animation(
        bg3.SPEAKER_DURGE, '30.61', '39.1',
        'c26b9b0a-20cc-44a4-a499-18d6d78abec5',
        '90070425-bce3-4bef-b8d7-ca38a676b5cb',
        animation_slot = 1,
        animation_play_start_offset = 6,
        fade_in = 1.5,
        fade_out = 1.8
    )

    # Camera shot 12
    t.create_tl_shot('a6db4283-ef38-4472-827c-fffd0ac04a28', '34.18', '46.98', is_snapped_to_end = True)
    t.create_tl_camera_fov('a6db4283-ef38-4472-827c-fffd0ac04a28', '34.18', '46.98', (
        t.create_value_key(time = 0.0, value_name = 'FoV', value = 25.0, interpolation_type = 2),
    ))
    t.create_tl_transform('a6db4283-ef38-4472-827c-fffd0ac04a28', '34.18', '46.88', (
        (
            t.create_value_key(time = '34.18', interpolation_type = 5, value = -9.0),
        ),
        (
            t.create_value_key(time = '34.18', interpolation_type = 5, value = 1.8),
        ),
        (
            t.create_value_key(time = '34.18', interpolation_type = 5, value = -0.6),
        ),
        (
            t.create_value_key(time = '34.18', interpolation_type = 5, value = bg3.euler_to_quaternion(86.0, 4.0, 0.0, sequence = 'yxz')),
        ),
        (),
        (),
    ))


    # Camera shot 13
    # t.create_tl_shot('a6db4283-ef38-4472-827c-fffd0ac04a28', '53.04', '53.22', is_snapped_to_end = True)
    # t.create_tl_camera_fov('a6db4283-ef38-4472-827c-fffd0ac04a28', '41.49', '53.22', (
    #     t.create_value_key(time = '41.49', value_name = 'FoV', value = 30.0, interpolation_type = 2),
    # ))
    # t.create_tl_transform('a6db4283-ef38-4472-827c-fffd0ac04a28', '41.49', '53.22', (
    #     (
    #         t.create_value_key(time = '41.49', interpolation_type = 5, value = -7.1),
    #     ),
    #     (
    #         t.create_value_key(time = '41.49', interpolation_type = 5, value = 1.75),
    #     ),
    #     (
    #         t.create_value_key(time = '41.49', interpolation_type = 5, value = -1.1),
    #     ),
    #     (
    #         t.create_value_key(time = '41.49', interpolation_type = 5, value = bg3.euler_to_quaternion(-60.0, 0.0, 0.0, sequence = 'yxz')),
    #     ),
    #     (),
    #     (),
    # ))

    # Camera shot 14
    t.create_tl_shot('a6db4283-ef38-4472-827c-fffd0ac04a28', '46.98', phase_duration, is_snapped_to_end = True)
    t.create_tl_camera_fov('a6db4283-ef38-4472-827c-fffd0ac04a28', '46.98', phase_duration, (
        t.create_value_key(time = 48.78, value_name = 'FoV', value = 32.0, interpolation_type = 2),
    ))
    t.create_tl_transform('a6db4283-ef38-4472-827c-fffd0ac04a28', '46.98', phase_duration, (
        (
            t.create_value_key(time = '46.98', interpolation_type = 5, value = -8.5),
        ),
        (
            t.create_value_key(time = '46.98', interpolation_type = 5, value = 1.75),
        ),
        (
            t.create_value_key(time = '46.98', interpolation_type = 5, value = -0.5),
        ),
        (
            t.create_value_key(time = '46.98', interpolation_type = 5, value = bg3.euler_to_quaternion(45.0, 0.0, 0.0, sequence = 'yxz')),
        ),
        (),
        (),
    ))


#################################################################################################
# Dwarves
#################################################################################################

def create_scene_shadowheart_reaction_dwarf() -> None:

    # d = bg3.dialog_object(files.get_file('Gustav', 'Mods/GustavDev/Story/DialogsBinary/Act3/LowerCity/BhaalTemple/LOW_BhaalTemple_PostBattleDarkUrge_Resistance.lsf'))
    # t = bg3.timeline_object(files.get_file('Gustav', 'Public/GustavDev/Timeline/Generated/LOW_BhaalTemple_PostBattleDarkUrge_Resistance.lsf'), d)

    ab = game_assets.get_modded_dialog_asset_bundle('LOW_BhaalTemple_PostBattleDarkUrge_Resistance')
    d = bg3.dialog_object(ab.dialog)
    t = bg3.timeline_object(ab.timeline, d)

    slot_idx_durge = d.get_speaker_slot_index(bg3.SPEAKER_DURGE)
    #slot_idx_shadowheart = d.get_speaker_slot_index(bg3.SPEAKER_SHADOWHEART)

    d.create_standard_dialog_node(
        dwarf_body_reaction_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [just_keep_safe_out_there_node_uuid],
        bg3.text_content('hd896e304g5fc4g41e7g807cg524360fee6a9', 1),
        checkflags = (
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_DWARF, True, slot_idx_durge),
                bg3.flag(bg3.TAG_SHORT, True, slot_idx_durge),
            )),
        )
    )

    phase_duration = '48.99'
    t.create_new_phase(dwarf_body_reaction_node_uuid, phase_duration)

    t.create_tl_actor_node(bg3.timeline_object.ATTITUDE, bg3.SPEAKER_DURGE, '0.0', phase_duration, (
        t.create_attitude_key(12.15, bg3.ATTITUDE_DIAG_Pose_Stand_R_Forward_01, bg3.ATTITUDE_DIAG_T_Pose),
        t.create_attitude_key(28.81, 'a2bd89b1-8ab9-4231-ac4b-e593d75aa083', bg3.ATTITUDE_DIAG_T_Pose),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.ATTITUDE, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_attitude_key(0.0, bg3.ATTITUDE_DIAG_Pose_Stand_L_Forward_01, bg3.ATTITUDE_DIAG_T_Pose),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.EMOTION, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_emotion_key(0.0, 32),
        t.create_emotion_key(6.13, 32, variation = 2),
        t.create_emotion_key(7.34, 32),
        t.create_emotion_key(15.63, 32, variation = 1),
        t.create_emotion_key(20.58, 32),
        t.create_emotion_key(44.85 - 4.26, 32, variation = 1, is_sustained = False),
        t.create_emotion_key(51.97 - 4.26, 32)
        #t.create_emotion_key(26.0, 2)
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.EMOTION, bg3.SPEAKER_DURGE, '0.0', phase_duration, (
        t.create_emotion_key(0.0, 32, variation = 1),
        t.create_emotion_key(3.51, 32),
        t.create_emotion_key(6.08, 32, variation = 1),
        t.create_emotion_key(6.56, 32),
        t.create_emotion_key(8.26, 32, variation = 2),
        t.create_emotion_key(11.26, 32, variation = 1),
        t.create_emotion_key(22.03, 32),
        t.create_emotion_key(40.14 - 4.26, 256),
        t.create_emotion_key(44.85 - 4.26, 32),
    ), is_snapped_to_end = True)

    t.create_tl_actor_node(bg3.timeline_object.LOOK_AT, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_look_at_key(
            0.0,
            target = bg3.SPEAKER_DURGE,
            bone = 'Head_M',
            turn_mode = 3,
            turn_speed_multiplier = 0.3,
            head_turn_speed_multiplier = 0.3,
            weight = 0,
            safe_zone_angle = 80,
            head_safe_zone_angle = 80,
            reset = True,
            look_at_mode = 1,
            eye_look_at_bone = 'Head_M'),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.LOOK_AT, bg3.SPEAKER_DURGE, '0.0', phase_duration, (
        t.create_look_at_key(
            0.0,
            target = bg3.SPEAKER_SHADOWHEART,
            bone = 'Head_M',
            turn_mode = 3,
            turn_speed_multiplier = 0.3,
            head_turn_speed_multiplier = 0.3,
            weight = 0,
            safe_zone_angle = 80,
            head_safe_zone_angle = 80,
            reset = True,
            look_at_mode = 1,
            eye_look_at_bone = 'Head_M'),
    ), is_snapped_to_end = True)

    t.create_tl_material(bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, '156a2490-d796-402c-b7fc-e00c032042c1', (), (
        t.create_value_key(time = 0.0, value = True),
    ), is_snapped_to_end = True, is_continuous = True)

    # Hide helmets
    t.create_tl_show_armor(bg3.SPEAKER_DURGE, '0.0', phase_duration, (
        (
            t.create_value_key(time = 0.0, value = False, interpolation_type = 5),
            t.create_value_key(time = phase_duration, interpolation_type = 5)
        ),
        (), (), (), (), (), (), (), (), (), ()
    ))
    t.create_tl_show_armor(bg3.SPEAKER_SHADOWHEART, '0.0',  phase_duration, (
        (
            t.create_value_key(time = 0.0, value = False, interpolation_type = 5),
            t.create_value_key(time = phase_duration, interpolation_type = 5)
        ),
        (), (), (), (), (), (), (), (), (), ()
    ))

    # Hide weapons
    t.create_tl_actor_node(bg3.timeline_object.SHOW_WEAPON, bg3.SPEAKER_DURGE, '0.0', phase_duration, (
        t.create_value_key(time = 0.0, value_name = 'ShowWeapon', value = False, interpolation_type = 3),
        t.create_value_key(time = phase_duration, interpolation_type = 3),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.SHOW_WEAPON, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_value_key(time = 0.0, value_name = 'ShowWeapon', value = False, interpolation_type = 3),
        t.create_value_key(time = phase_duration, interpolation_type = 3),
    ), is_snapped_to_end = True)

    # Show Durge
    t.create_tl_actor_node(bg3.timeline_object.SHOW_VISUAL, bg3.SPEAKER_DURGE, '0.0', phase_duration, (
        t.create_value_key(time = 0.0, interpolation_type = 3),
    ), is_snapped_to_end = True)

    # Kiss part
    # rel diff 214.68
    t.create_tl_actor_node(bg3.timeline_object.SOUND, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_sound_event_key('31.74', sound_event_id = '90a31a12-9f32-47e1-899e-cdced0705f27', sound_object_index = 4),
        t.create_sound_event_key('31.80', sound_event_id = '025fa6be-55ec-43fe-af6a-03b746163d72', sound_object_index = 4),
        t.create_sound_event_key('32.41', sound_event_id = 'ffbbbd57-5c31-444d-bc3a-c3d14df0be53', sound_object_index = 4),
        t.create_sound_event_key('34.83', sound_event_id = 'ffbbbd57-5c31-444d-bc3a-c3d14df0be53', sound_object_index = 4),
        t.create_sound_event_key('37.61', sound_event_id = 'ffbbbd57-5c31-444d-bc3a-c3d14df0be53', sound_object_index = 4),
        t.create_sound_event_key('39.28', sound_event_id = '5dac329f-b08a-412d-84bc-86fc1aecae45', sound_object_index = 4),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.SOUND, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_sound_event_key('23.7', sound_event_id = '3a82ed81-3970-461a-91dc-4687caa05cce', sound_object_index = 1),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.SOUND, bg3.SPEAKER_DURGE, '0.0', phase_duration, (
        t.create_sound_event_key('31.8', sound_event_id = '3dcf9fdd-8a5e-4a6b-b72b-75590f2d04c2', sound_object_index = 4),
        t.create_sound_event_key('33.51', sound_event_id = 'ffbbbd57-5c31-444d-bc3a-c3d14df0be53', sound_object_index = 4),
        t.create_sound_event_key('36.03', sound_event_id = 'ffbbbd57-5c31-444d-bc3a-c3d14df0be53', sound_object_index = 4),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.SOUND, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_sound_event_key('46.08', sound_type = 4),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.SOUND, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_sound_event_key('23.92', sound_event_id = '3a82ed81-3970-461a-91dc-4687caa05cce', sound_object_index = 2),
    ), is_snapped_to_end = True)

    # Physics
    t.create_tl_actor_node(bg3.timeline_object.PHYSICS, bg3.SPEAKER_DURGE, '0.0', phase_duration, (
        t.create_value_key(time = 0.0, interpolation_type = 3, value_name = 'InverseKinematics', value = False),
        t.create_value_key(time = '22.75', interpolation_type = 3),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.PHYSICS, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_value_key(time = 0.0, interpolation_type = 3, value_name = 'InverseKinematics', value = False),
        t.create_value_key(time = '22.75', interpolation_type = 3),
    ), is_snapped_to_end = True)
    # t.create_tl_actor_node(bg3.timeline_object.PHYSICS, bg3.SPEAKER_DURGE, '0.0', phase_duration, (
    #     t.create_value_key(time = 24.55, interpolation_type = 3),
    # ), is_snapped_to_end = True)
    # t.create_tl_actor_node(bg3.timeline_object.PHYSICS, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
    #     t.create_value_key(time = 24.55, interpolation_type = 3),
    # ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.HANDS_IK, bg3.SPEAKER_DURGE, '0.0', phase_duration, (), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.HANDS_IK, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (), is_snapped_to_end = True)

    t.create_tl_animation(
        bg3.SPEAKER_DURGE,
        '0.0', '13.65',
        '54f674a3-2ae4-42c0-a0ae-b178239a79cd',
        'a2dae3f2-e3c9-4fc7-b8ac-82abf4a153b0',
        fade_in = 0.0,
        fade_out = 1.53)
    t.create_tl_animation(
        bg3.SPEAKER_SHADOWHEART,
        '0.0', '13.65',
        'e3194510-d4e1-18cc-c8c0-3174c912c168',
        'c8dad77b-5b76-44fe-bfeb-61d676ede3f6',
        fade_in = 0.0,
        fade_out = 1.53)

    t.create_tl_transform(bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = -8.0),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 0.0),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 0.395),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = (0.0, 0.0, 0.0, 1.0)),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 1),
        ),
        (),
    ), is_snapped_to_end = True)

    t.create_tl_transform(bg3.SPEAKER_DURGE, '0.0', '24.55', (
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = -8.0),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 0.0),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = -0.395),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = (0.0, 1.0, 0.0, 0.0)),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 1),
        ),
        (),
    ), is_snapped_to_end = True)


    # Camera shot 1
    t.create_tl_shot('d35b098e-8c34-45ee-9dde-21adfd2410a9', '0.0', '2.0')
    t.create_tl_camera_fov('d35b098e-8c34-45ee-9dde-21adfd2410a9', '0.0', '2.0', (
        t.create_value_key(time = 0.0, value_name = 'FoV', value = 25.0, interpolation_type = 2),
        #t.create_value_key(time = 0.0, value_name = 'FoV', value = 75.0, interpolation_type = 2),
    ))
    t.create_tl_transform('d35b098e-8c34-45ee-9dde-21adfd2410a9', '0.0', '2.0', (
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = -6.5),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 1.4),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 0.2),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = bg3.euler_to_quaternion(-117.0, 10.0, 0.0, sequence = 'yxz')),
        ),
        (),
        (),
    ))

    # Camera shot 2
    t.create_tl_shot('d35b098e-8c34-45ee-9dde-21adfd2410a9', '2.0', '4.2')
    t.create_tl_camera_fov('d35b098e-8c34-45ee-9dde-21adfd2410a9', '2.0', '4.2', (
        t.create_value_key(time = 2.0, value_name = 'FoV', value = 35.0, interpolation_type = 2),
        #t.create_value_key(time = 0.0, value_name = 'FoV', value = 75.0, interpolation_type = 2),
    ))
    t.create_tl_transform('d35b098e-8c34-45ee-9dde-21adfd2410a9', '2.0', '4.2', (
        (
            t.create_value_key(time = 2.0, interpolation_type = 5, value = -6.5),
        ),
        (
            t.create_value_key(time = 2.0, interpolation_type = 5, value = 1.4),
        ),
        (
            t.create_value_key(time = 2.0, interpolation_type = 5, value = -1.0),
        ),
        (
            t.create_value_key(time = 2.0, interpolation_type = 5, value = bg3.euler_to_quaternion(-62.0, 7.0, 0.0, sequence = 'yxz')),
        ),
        (),
        (),
    ))

    # Camera shot 3
    t.create_tl_shot('d35b098e-8c34-45ee-9dde-21adfd2410a9', '4.2', '8.74')
    t.create_tl_camera_fov('d35b098e-8c34-45ee-9dde-21adfd2410a9', '4.2', '8.74', (
        t.create_value_key(time = '4.2', value_name = 'FoV', value = 30.0, interpolation_type = 2),
    ))
    t.create_tl_transform('d35b098e-8c34-45ee-9dde-21adfd2410a9', '4.2', '8.74', (
        (
            t.create_value_key(time = '4.2', interpolation_type = 5, value = -6.0),
        ),
        (
            t.create_value_key(time = '4.2', interpolation_type = 5, value = 1.3),
        ),
        (
            t.create_value_key(time = '4.2', interpolation_type = 5, value = -0.6),
        ),
        (
            t.create_value_key(time = '4.2', interpolation_type = 5, value = bg3.euler_to_quaternion(-74.0, 10.0, 0.0, sequence = 'yxz')),
        ),
        (),
        (),
    ))

    # Camera shot 4
    t.create_tl_shot('d35b098e-8c34-45ee-9dde-21adfd2410a9', '8.74', '12.07')
    t.create_tl_camera_fov('d35b098e-8c34-45ee-9dde-21adfd2410a9', '8.74', '12.07', (
        t.create_value_key(time = '8.74', value_name = 'FoV', value = 25.0, interpolation_type = 2),
    ))
    t.create_tl_transform('d35b098e-8c34-45ee-9dde-21adfd2410a9', '8.74', '12.07', (
        (
            t.create_value_key(time = '8.74', interpolation_type = 5, value = -10.0),
        ),
        (
            t.create_value_key(time = '8.74', interpolation_type = 5, value = 1.4),
        ),
        (
            t.create_value_key(time = '8.74', interpolation_type = 5, value = -0.1),
        ),
        (
            t.create_value_key(time = '8.74', interpolation_type = 5, value = bg3.euler_to_quaternion(90.0, 10.0, 0.0, sequence = 'yxz')),
        ),
        (),
        (),
    ))

    # Camera shot 5
    t.create_tl_shot('d35b098e-8c34-45ee-9dde-21adfd2410a9', '12.07', '16.97')
    t.create_tl_camera_fov('d35b098e-8c34-45ee-9dde-21adfd2410a9', '12.07', '16.97', (
        t.create_value_key(time = '12.07', value_name = 'FoV', value = 35.0, interpolation_type = 2),
    ))
    t.create_tl_transform('d35b098e-8c34-45ee-9dde-21adfd2410a9', '12.07', '16.97', (
        (
            t.create_value_key(time = '12.07', interpolation_type = 5, value = -8.9),
        ),
        (
            t.create_value_key(time = '12.07', interpolation_type = 5, value = 1.3),
        ),
        (
            t.create_value_key(time = '12.07', interpolation_type = 5, value = 0.4),
        ),
        (
            t.create_value_key(time = '12.07', interpolation_type = 5, value = bg3.euler_to_quaternion(115.0, 10.0, 0.0, sequence = 'yxz')),
        ),
        (),
        (),
    ))

    t.create_tl_animation(
        bg3.SPEAKER_DURGE,
        '12.12', '22.75',
        '54f674a3-2ae4-42c0-a0ae-b178239a79cd',
        'a2dae3f2-e3c9-4fc7-b8ac-82abf4a153b0',
        fade_in = 0.0,
        fade_out = 0.0,
        animation_play_start_offset = 8.0)
    t.create_tl_animation(
        bg3.SPEAKER_SHADOWHEART,
        '12.12', '22.75',
        'e3194510-d4e1-18cc-c8c0-3174c912c168',
        'c8dad77b-5b76-44fe-bfeb-61d676ede3f6',
        fade_in = 0.0,
        fade_out = 0.0,
        animation_play_start_offset = 8.0)

    # Camera shot 6
    t.create_tl_shot('d35b098e-8c34-45ee-9dde-21adfd2410a9', '16.97', '22.75')
    t.create_tl_camera_fov('d35b098e-8c34-45ee-9dde-21adfd2410a9', '16.97', '22.75', (
        t.create_value_key(time = '16.97', value_name = 'FoV', value = 35.0, interpolation_type = 2),
    ))
    t.create_tl_transform('d35b098e-8c34-45ee-9dde-21adfd2410a9', '16.97', '22.75', (
        (
            t.create_value_key(time = '16.97', interpolation_type = 5, value = -7.1),
        ),
        (
            t.create_value_key(time = '16.97', interpolation_type = 5, value = 1.35),
        ),
        (
            t.create_value_key(time = '16.97', interpolation_type = 5, value = 0.2),
        ),
        (
            t.create_value_key(time = '16.97', interpolation_type = 5, value = bg3.euler_to_quaternion(-117.0, 10.0, 0.0, sequence = 'yxz')),
        ),
        (),
        (),
    ))

    # t.create_tl_animation(
    #     bg3.SPEAKER_DURGE,
    #     21.67, '22.75',
    #     '54f674a3-2ae4-42c0-a0ae-b178239a79cd',
    #     'a2dae3f2-e3c9-4fc7-b8ac-82abf4a153b0',
    #     fade_in = 0.0,
    #     fade_out = 2.5,
    #     animation_play_start_offset = 22.0)
    # t.create_tl_animation(
    #     bg3.SPEAKER_SHADOWHEART,
    #     21.67, '22.75',
    #     'e3194510-d4e1-18cc-c8c0-3174c912c168',
    #     'c8dad77b-5b76-44fe-bfeb-61d676ede3f6',
    #     fade_in = 0.0,
    #     fade_out = 1.44,
    #     animation_play_start_offset = 22.0)

    # Camera shot 7
    t.create_tl_shot('a6db4283-ef38-4472-827c-fffd0ac04a28', '22.75', '27.59')
    t.create_tl_camera_fov('a6db4283-ef38-4472-827c-fffd0ac04a28', '22.75', '27.59', (
        t.create_value_key(time = 0.0, value_name = 'FoV', value = 30.0, interpolation_type = 2),
    ))
    t.create_tl_transform('a6db4283-ef38-4472-827c-fffd0ac04a28', '22.75', '27.59', (
        (
            t.create_value_key(time = '22.75', interpolation_type = 5, value = -7.1),
        ),
        (
            t.create_value_key(time = '22.75', interpolation_type = 5, value = 1.5),
        ),
        (
            t.create_value_key(time = '22.75', interpolation_type = 5, value = -1.2),
        ),
        (
            t.create_value_key(time = '22.75', interpolation_type = 5, value = bg3.euler_to_quaternion(-44.0, 10.0, 0.0, sequence = 'yxz')),
        ),
        (),
        (),
    ))

    t.create_tl_transform(bg3.SPEAKER_DURGE, '22.75', phase_duration, (
        (
            t.create_value_key(time = '22.75', interpolation_type = 5, value = -8.0),
        ),
        (
            t.create_value_key(time = '22.75', interpolation_type = 5, value = 0.0),
        ),
        (
            t.create_value_key(time = '22.75', interpolation_type = 5, value = -0.83),
        ),
        (
            t.create_value_key(time = '22.75', interpolation_type = 5, value = (0.0, 1.0, 0.0, 0.0)),
        ),
        (
            t.create_value_key(time = '22.75', interpolation_type = 5, value = 1),
        ),
        (),
    ), is_snapped_to_end = True)
    t.create_tl_transform(bg3.SPEAKER_SHADOWHEART, '22.75', phase_duration, (
        (
            t.create_value_key(time = '22.75', interpolation_type = 5, value = -8.0),
        ),
        (
            t.create_value_key(time = '22.75', interpolation_type = 5, value = 0.0),
        ),
        (
            t.create_value_key(time = '22.75', interpolation_type = 5, value = 0.38),
        ),
        (
            t.create_value_key(time = '22.75', interpolation_type = 5, value = (0.0, 0.0, 0.0, 1.0)),
        ),
        (
            t.create_value_key(time = '22.75', interpolation_type = 5, value = 1),
        ),
        (),
    ), is_snapped_to_end = True)

    t.create_tl_animation(
        bg3.SPEAKER_SHADOWHEART, '22.75', phase_duration,
        '9624892a-fb02-113d-c5ed-bea922167bba',
        '66ce0c11-1cdb-4573-818c-a91cde00f79f',
        animation_play_start_offset = 4.8,
        fade_in = 0.0,
        fade_out = 0.0,
        is_snapped_to_end = True)
    t.create_tl_animation(
        bg3.SPEAKER_DURGE, '22.75', phase_duration,
        'a284aed0-b644-4596-8b9d-0a17c76f8bd8',
        '57fa3dc0-184f-4b43-93fd-86e5496448a9',
        animation_play_start_offset = 4.8,
        fade_in = 0.0,
        fade_out = 0.0,
        is_snapped_to_end = True)

    # Camera shot 8
    t.create_tl_shot('a6db4283-ef38-4472-827c-fffd0ac04a28', '25.89', '32.48')
    t.create_tl_camera_fov('a6db4283-ef38-4472-827c-fffd0ac04a28', '25.89', '32.48', (
        t.create_value_key(time = 29.39, value_name = 'FoV', value = 22.0, interpolation_type = 2),
    ))
    t.create_tl_transform('a6db4283-ef38-4472-827c-fffd0ac04a28', '25.89', '32.48', (
        (
            t.create_value_key(time = 25.89, interpolation_type = 5, value = -7.1),
        ),
        (
            t.create_value_key(time = 25.89, interpolation_type = 5, value = 1.5),
        ),
        (
            t.create_value_key(time = 25.89, interpolation_type = 5, value = -0.9),
        ),
        (
            t.create_value_key(time = 25.89, interpolation_type = 5, value = bg3.euler_to_quaternion(-65.0, 10.0, 0.0, sequence = 'yxz')),
        ),
        (),
        (),
    ))

    t.create_tl_voice(
        bg3.SPEAKER_SHADOWHEART, '28.867', '30.74',
        dwarf_body_reaction_node_uuid,
        fade_in = 0.0,
        fade_out = 0.0)

    # Camera shot 9
    t.create_tl_shot('a6db4283-ef38-4472-827c-fffd0ac04a28', '32.48', '45.28', is_snapped_to_end = True)
    t.create_tl_camera_fov('a6db4283-ef38-4472-827c-fffd0ac04a28', '32.48', '45.28', (
        t.create_value_key(time = 0.0, value_name = 'FoV', value = 25.0, interpolation_type = 2),
    ))
    t.create_tl_transform('a6db4283-ef38-4472-827c-fffd0ac04a28', '32.48', '45.28', (
        (
            t.create_value_key(time = 32.48, interpolation_type = 5, value = -9.0),
        ),
        (
            t.create_value_key(time = 32.48, interpolation_type = 5, value = 1.4),
        ),
        (
            t.create_value_key(time = 32.48, interpolation_type = 5, value = -0.6),
        ),
        (
            t.create_value_key(time = 32.48, interpolation_type = 5, value = bg3.euler_to_quaternion(86.0, 4.0, 0.0, sequence = 'yxz')),
        ),
        (),
        (),
    ))


    t.create_tl_animation(
        bg3.SPEAKER_SHADOWHEART, '31.58', '40.8',
        'c26b9b0a-20cc-44a4-a499-18d6d78abec5',
        '536f3ddd-33e5-4b9d-a20a-b7109f6bbc76',
        animation_slot = 1,
        animation_play_start_offset = 7,
        fade_in = 1.5,
        fade_out = 1.5
    )
    t.create_tl_animation(
        bg3.SPEAKER_DURGE, '31.21', '40.8',
        'c26b9b0a-20cc-44a4-a499-18d6d78abec5',
        '90070425-bce3-4bef-b8d7-ca38a676b5cb',
        animation_slot = 1,
        animation_play_start_offset = 6.63,
        fade_in = 1.5,
        fade_out = 1.5
    )

    # Camera shot 10
    t.create_tl_shot('a6db4283-ef38-4472-827c-fffd0ac04a28', '45.28', phase_duration, is_snapped_to_end = True)
    t.create_tl_camera_fov('a6db4283-ef38-4472-827c-fffd0ac04a28', '45.28', phase_duration, (
        t.create_value_key(time = 45.28, value_name = 'FoV', value = 35.0, interpolation_type = 2),
    ))
    t.create_tl_transform('a6db4283-ef38-4472-827c-fffd0ac04a28', '45.28', phase_duration, (
        (
            t.create_value_key(time = 45.28, interpolation_type = 5, value = -9.0),
        ),
        (
            t.create_value_key(time = 45.28, interpolation_type = 5, value = 1.5),
        ),
        (
            t.create_value_key(time = 45.28, interpolation_type = 5, value = -0.5),
        ),
        (
            t.create_value_key(time = 45.28, interpolation_type = 5, value = bg3.euler_to_quaternion(64.0, 0.0, 0.0, sequence = 'yxz')),
        ),
        (),
        (),
    ))


#################################################################################################
# Halflings and gnomes
#################################################################################################

def create_scene_shadowheart_reaction_short_races() -> None:

    # d = bg3.dialog_object(files.get_file('Gustav', 'Mods/GustavDev/Story/DialogsBinary/Act3/LowerCity/BhaalTemple/LOW_BhaalTemple_PostBattleDarkUrge_Resistance.lsf'))
    # t = bg3.timeline_object(files.get_file('Gustav', 'Public/GustavDev/Timeline/Generated/LOW_BhaalTemple_PostBattleDarkUrge_Resistance.lsf'), d)

    ab = game_assets.get_modded_dialog_asset_bundle('LOW_BhaalTemple_PostBattleDarkUrge_Resistance')
    d = bg3.dialog_object(ab.dialog)
    t = bg3.timeline_object(ab.timeline, d)

    slot_idx_durge = d.get_speaker_slot_index(bg3.SPEAKER_DURGE)
    #slot_idx_shadowheart = d.get_speaker_slot_index(bg3.SPEAKER_SHADOWHEART)

    d.create_standard_dialog_node(
        short_body_reaction_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [just_keep_safe_out_there_node_uuid],
        bg3.text_content('hd896e304g5fc4g41e7g807cg524360fee6a9', 1),
        checkflags = (
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_SHORT, True, slot_idx_durge),
            )),
        )
    )

    phase_duration = '48.84'
    t.create_new_phase(short_body_reaction_node_uuid, phase_duration)

    t.create_tl_actor_node(bg3.timeline_object.ATTITUDE, bg3.SPEAKER_DURGE, '0.0', phase_duration, (
        t.create_attitude_key(12.15, bg3.ATTITUDE_DIAG_Pose_Stand_R_Forward_01, bg3.ATTITUDE_DIAG_T_Pose),
        t.create_attitude_key(28.81, 'a2bd89b1-8ab9-4231-ac4b-e593d75aa083', bg3.ATTITUDE_DIAG_T_Pose),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.ATTITUDE, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_attitude_key(0.0, bg3.ATTITUDE_DIAG_Pose_Stand_L_Forward_01, bg3.ATTITUDE_DIAG_T_Pose),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.EMOTION, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_emotion_key(0.0, 32),
        t.create_emotion_key(6.13, 32, variation = 2),
        t.create_emotion_key(7.34, 32),
        t.create_emotion_key(15.63, 32, variation = 1),
        t.create_emotion_key(20.58, 32),
        t.create_emotion_key(44.85 - 4.26, 32, variation = 1, is_sustained = False),
        t.create_emotion_key(51.97 - 4.26, 32)
        #t.create_emotion_key(26.0, 2)
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.EMOTION, bg3.SPEAKER_DURGE, '0.0', phase_duration, (
        t.create_emotion_key(0.0, 32, variation = 1),
        t.create_emotion_key(3.51, 32),
        t.create_emotion_key(6.08, 32, variation = 1),
        t.create_emotion_key(6.56, 32),
        t.create_emotion_key(8.26, 32, variation = 2),
        t.create_emotion_key(11.26, 32, variation = 1),
        t.create_emotion_key(22.03, 32),
        t.create_emotion_key(40.14 - 4.26, 256),
        t.create_emotion_key(44.85 - 4.26, 32),
    ), is_snapped_to_end = True)

    t.create_tl_actor_node(bg3.timeline_object.LOOK_AT, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_look_at_key(
            0.0,
            target = bg3.SPEAKER_DURGE,
            bone = 'Head_M',
            turn_mode = 3,
            turn_speed_multiplier = 0.3,
            head_turn_speed_multiplier = 0.3,
            weight = 0,
            safe_zone_angle = 80,
            head_safe_zone_angle = 80,
            reset = True,
            look_at_mode = 1,
            eye_look_at_bone = 'Head_M'),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.LOOK_AT, bg3.SPEAKER_DURGE, '0.0', phase_duration, (
        t.create_look_at_key(
            0.0,
            target = bg3.SPEAKER_SHADOWHEART,
            bone = 'Head_M',
            turn_mode = 3,
            turn_speed_multiplier = 0.3,
            head_turn_speed_multiplier = 0.3,
            weight = 0,
            safe_zone_angle = 80,
            head_safe_zone_angle = 80,
            reset = True,
            look_at_mode = 1,
            eye_look_at_bone = 'Head_M'),
    ), is_snapped_to_end = True)

    t.create_tl_material(bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, '156a2490-d796-402c-b7fc-e00c032042c1', (), (
        t.create_value_key(time = 0.0, value = True),
    ), is_snapped_to_end = True, is_continuous = True)

    # Hide helmets
    t.create_tl_show_armor(bg3.SPEAKER_DURGE, '0.0', phase_duration, (
        (
            t.create_value_key(time = 0.0, value = False, interpolation_type = 5),
            t.create_value_key(time = phase_duration, interpolation_type = 5)
        ),
        (), (), (), (), (), (), (), (), (), ()
    ))
    t.create_tl_show_armor(bg3.SPEAKER_SHADOWHEART, '0.0',  phase_duration, (
        (
            t.create_value_key(time = 0.0, value = False, interpolation_type = 5),
            t.create_value_key(time = phase_duration, interpolation_type = 5)
        ),
        (), (), (), (), (), (), (), (), (), ()
    ))

    # Hide weapons
    t.create_tl_actor_node(bg3.timeline_object.SHOW_WEAPON, bg3.SPEAKER_DURGE, '0.0', phase_duration, (
        t.create_value_key(time = 0.0, value_name = 'ShowWeapon', value = False, interpolation_type = 3),
        t.create_value_key(time = phase_duration, interpolation_type = 3),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.SHOW_WEAPON, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_value_key(time = 0.0, value_name = 'ShowWeapon', value = False, interpolation_type = 3),
        t.create_value_key(time = phase_duration, interpolation_type = 3),
    ), is_snapped_to_end = True)

    # Show Durge
    t.create_tl_actor_node(bg3.timeline_object.SHOW_VISUAL, bg3.SPEAKER_DURGE, '0.0', phase_duration, (
        t.create_value_key(time = 0.0, interpolation_type = 3),
    ), is_snapped_to_end = True)

    # Kiss part
    # rel diff 214.68
    t.create_tl_actor_node(bg3.timeline_object.SOUND, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_sound_event_key(31.74, sound_event_id = '90a31a12-9f32-47e1-899e-cdced0705f27', sound_object_index = 4),
        t.create_sound_event_key(31.80, sound_event_id = '025fa6be-55ec-43fe-af6a-03b746163d72', sound_object_index = 4),
        t.create_sound_event_key(32.41, sound_event_id = 'ffbbbd57-5c31-444d-bc3a-c3d14df0be53', sound_object_index = 4),
        t.create_sound_event_key(34.83, sound_event_id = 'ffbbbd57-5c31-444d-bc3a-c3d14df0be53', sound_object_index = 4),
        t.create_sound_event_key(37.61, sound_event_id = 'ffbbbd57-5c31-444d-bc3a-c3d14df0be53', sound_object_index = 4),
        t.create_sound_event_key(39.28, sound_event_id = '5dac329f-b08a-412d-84bc-86fc1aecae45', sound_object_index = 4),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.SOUND, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_sound_event_key(23.7, sound_event_id = '3a82ed81-3970-461a-91dc-4687caa05cce', sound_object_index = 1),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.SOUND, bg3.SPEAKER_DURGE, '0.0', phase_duration, (
        t.create_sound_event_key(31.8, sound_event_id = '3dcf9fdd-8a5e-4a6b-b72b-75590f2d04c2', sound_object_index = 4),
        t.create_sound_event_key(33.51, sound_event_id = 'ffbbbd57-5c31-444d-bc3a-c3d14df0be53', sound_object_index = 4),
        t.create_sound_event_key(36.03, sound_event_id = 'ffbbbd57-5c31-444d-bc3a-c3d14df0be53', sound_object_index = 4),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.SOUND, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_sound_event_key(46.08, sound_type = 4),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.SOUND, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_sound_event_key(23.92, sound_event_id = '3a82ed81-3970-461a-91dc-4687caa05cce', sound_object_index = 2),
    ), is_snapped_to_end = True)

    # Physics
    t.create_tl_actor_node(bg3.timeline_object.PHYSICS, bg3.SPEAKER_DURGE, '0.0', phase_duration, (
        t.create_value_key(time = 0.0, interpolation_type = 3, value_name = 'InverseKinematics', value = False),
        t.create_value_key(time = '22.75', interpolation_type = 3),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.PHYSICS, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_value_key(time = 0.0, interpolation_type = 3, value_name = 'InverseKinematics', value = False),
        t.create_value_key(time = '22.75', interpolation_type = 3),
    ), is_snapped_to_end = True)
    # t.create_tl_actor_node(bg3.timeline_object.PHYSICS, bg3.SPEAKER_DURGE, '0.0', phase_duration, (
    #     t.create_value_key(time = 24.55, interpolation_type = 3),
    # ), is_snapped_to_end = True)
    # t.create_tl_actor_node(bg3.timeline_object.PHYSICS, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
    #     t.create_value_key(time = 24.55, interpolation_type = 3),
    # ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.HANDS_IK, bg3.SPEAKER_DURGE, '0.0', phase_duration, (), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.HANDS_IK, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (), is_snapped_to_end = True)

    t.create_tl_animation(
        bg3.SPEAKER_DURGE,
        '0.0', '13.65',
        '0a5b7810-3652-4465-876c-f6947aa618cf',
        'a2dae3f2-e3c9-4fc7-b8ac-82abf4a153b0',
        fade_in = 0.0,
        fade_out = 1.53)
    t.create_tl_animation(
        bg3.SPEAKER_SHADOWHEART,
        '0.0', '13.65',
        'd3cb3816-2562-6bbc-2e32-6e956c325718',
        'c8dad77b-5b76-44fe-bfeb-61d676ede3f6',
        fade_in = 0.0,
        fade_out = 1.53)

    t.create_tl_transform(bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = -8.0),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 0.0),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 0.395),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = (0.0, 0.0, 0.0, 1.0)),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 1),
        ),
        (),
    ), is_snapped_to_end = True)

    t.create_tl_transform(bg3.SPEAKER_DURGE, '0.0', '24.55', (
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = -8.0),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 0.0),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = -0.395),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = (0.0, 1.0, 0.0, 0.0)),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 1),
        ),
        (),
    ), is_snapped_to_end = True)


    # Camera shot 1
    t.create_tl_shot('d35b098e-8c34-45ee-9dde-21adfd2410a9', '0.0', '2.0')
    t.create_tl_camera_fov('d35b098e-8c34-45ee-9dde-21adfd2410a9', '0.0', '2.0', (
        t.create_value_key(time = 0.0, value_name = 'FoV', value = 25.0, interpolation_type = 2),
        #t.create_value_key(time = 0.0, value_name = 'FoV', value = 75.0, interpolation_type = 2),
    ))
    t.create_tl_transform('d35b098e-8c34-45ee-9dde-21adfd2410a9', '0.0', '2.0', (
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = -6.5),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 1.4),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 0.2),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = bg3.euler_to_quaternion(-117.0, 10.0, 0.0, sequence = 'yxz')),
        ),
        (),
        (),
    ))

    # Camera shot 2
    t.create_tl_shot('d35b098e-8c34-45ee-9dde-21adfd2410a9', '2.0', '4.2')
    t.create_tl_camera_fov('d35b098e-8c34-45ee-9dde-21adfd2410a9', '2.0', '4.2', (
        t.create_value_key(time = 2.0, value_name = 'FoV', value = 35.0, interpolation_type = 2),
        #t.create_value_key(time = 0.0, value_name = 'FoV', value = 75.0, interpolation_type = 2),
    ))
    t.create_tl_transform('d35b098e-8c34-45ee-9dde-21adfd2410a9', '2.0', '4.2', (
        (
            t.create_value_key(time = 2.0, interpolation_type = 5, value = -6.5),
        ),
        (
            t.create_value_key(time = 2.0, interpolation_type = 5, value = 1.4),
        ),
        (
            t.create_value_key(time = 2.0, interpolation_type = 5, value = -1.0),
        ),
        (
            t.create_value_key(time = 2.0, interpolation_type = 5, value = bg3.euler_to_quaternion(-62.0, 7.0, 0.0, sequence = 'yxz')),
        ),
        (),
        (),
    ))

    # Camera shot 3
    t.create_tl_shot('d35b098e-8c34-45ee-9dde-21adfd2410a9', '4.2', '8.74')
    t.create_tl_camera_fov('d35b098e-8c34-45ee-9dde-21adfd2410a9', '4.2', '8.74', (
        t.create_value_key(time = '4.2', value_name = 'FoV', value = 30.0, interpolation_type = 2),
    ))
    t.create_tl_transform('d35b098e-8c34-45ee-9dde-21adfd2410a9', '4.2', '8.74', (
        (
            t.create_value_key(time = '4.2', interpolation_type = 5, value = -6.0),
        ),
        (
            t.create_value_key(time = '4.2', interpolation_type = 5, value = 1.3),
        ),
        (
            t.create_value_key(time = '4.2', interpolation_type = 5, value = -0.6),
        ),
        (
            t.create_value_key(time = '4.2', interpolation_type = 5, value = bg3.euler_to_quaternion(-74.0, 10.0, 0.0, sequence = 'yxz')),
        ),
        (),
        (),
    ))

    # Camera shot 4
    t.create_tl_shot('d35b098e-8c34-45ee-9dde-21adfd2410a9', '8.74', '12.07')
    t.create_tl_camera_fov('d35b098e-8c34-45ee-9dde-21adfd2410a9', '8.74', '12.07', (
        t.create_value_key(time = '8.74', value_name = 'FoV', value = 25.0, interpolation_type = 2),
    ))
    t.create_tl_transform('d35b098e-8c34-45ee-9dde-21adfd2410a9', '8.74', '12.07', (
        (
            t.create_value_key(time = '8.74', interpolation_type = 5, value = -10.0),
        ),
        (
            t.create_value_key(time = '8.74', interpolation_type = 5, value = 1.4),
        ),
        (
            t.create_value_key(time = '8.74', interpolation_type = 5, value = -0.1),
        ),
        (
            t.create_value_key(time = '8.74', interpolation_type = 5, value = bg3.euler_to_quaternion(90.0, 10.0, 0.0, sequence = 'yxz')),
        ),
        (),
        (),
    ))

    # Camera shot 5
    t.create_tl_shot('d35b098e-8c34-45ee-9dde-21adfd2410a9', '12.07', '16.97')
    t.create_tl_camera_fov('d35b098e-8c34-45ee-9dde-21adfd2410a9', '12.07', '16.97', (
        t.create_value_key(time = '12.07', value_name = 'FoV', value = 35.0, interpolation_type = 2),
    ))
    t.create_tl_transform('d35b098e-8c34-45ee-9dde-21adfd2410a9', '12.07', '16.97', (
        (
            t.create_value_key(time = '12.07', interpolation_type = 5, value = -8.9),
        ),
        (
            t.create_value_key(time = '12.07', interpolation_type = 5, value = 1.3),
        ),
        (
            t.create_value_key(time = '12.07', interpolation_type = 5, value = 0.4),
        ),
        (
            t.create_value_key(time = '12.07', interpolation_type = 5, value = bg3.euler_to_quaternion(115.0, 10.0, 0.0, sequence = 'yxz')),
        ),
        (),
        (),
    ))

    t.create_tl_animation(
        bg3.SPEAKER_DURGE,
        '12.12', '22.75',
        '0a5b7810-3652-4465-876c-f6947aa618cf',
        'a2dae3f2-e3c9-4fc7-b8ac-82abf4a153b0',
        fade_in = 0.0,
        fade_out = 0.0,
        animation_play_start_offset = 8.0)
    t.create_tl_animation(
        bg3.SPEAKER_SHADOWHEART,
        '12.12', '22.75',
        'd3cb3816-2562-6bbc-2e32-6e956c325718',
        'c8dad77b-5b76-44fe-bfeb-61d676ede3f6',
        fade_in = 0.0,
        fade_out = 0.0,
        animation_play_start_offset = 8.0)

    # Camera shot 6
    t.create_tl_shot('d35b098e-8c34-45ee-9dde-21adfd2410a9', '16.97', '22.75')
    t.create_tl_camera_fov('d35b098e-8c34-45ee-9dde-21adfd2410a9', '16.97', '22.75', (
        t.create_value_key(time = '16.97', value_name = 'FoV', value = 35.0, interpolation_type = 2),
    ))
    t.create_tl_transform('d35b098e-8c34-45ee-9dde-21adfd2410a9', '16.97', '22.75', (
        (
            t.create_value_key(time = '16.97', interpolation_type = 5, value = -7.1),
        ),
        (
            t.create_value_key(time = '16.97', interpolation_type = 5, value = 1.35),
        ),
        (
            t.create_value_key(time = '16.97', interpolation_type = 5, value = 0.2),
        ),
        (
            t.create_value_key(time = '16.97', interpolation_type = 5, value = bg3.euler_to_quaternion(-117.0, 10.0, 0.0, sequence = 'yxz')),
        ),
        (),
        (),
    ))


    # Camera shot 7
    t.create_tl_shot('a6db4283-ef38-4472-827c-fffd0ac04a28', '22.75', '27.59')
    t.create_tl_camera_fov('a6db4283-ef38-4472-827c-fffd0ac04a28', '22.75', '27.59', (
        t.create_value_key(time = 0.0, value_name = 'FoV', value = 30.0, interpolation_type = 2),
    ))
    t.create_tl_transform('a6db4283-ef38-4472-827c-fffd0ac04a28', '22.75', '27.59', (
        (
            t.create_value_key(time = '22.75', interpolation_type = 5, value = -7.1),
        ),
        (
            t.create_value_key(time = '22.75', interpolation_type = 5, value = 1.3),
        ),
        (
            t.create_value_key(time = '22.75', interpolation_type = 5, value = -1.2),
        ),
        (
            t.create_value_key(time = '22.75', interpolation_type = 5, value = bg3.euler_to_quaternion(-44.0, 10.0, 0.0, sequence = 'yxz')),
        ),
        (),
        (),
    ))

    t.create_tl_transform(bg3.SPEAKER_DURGE, '22.75', phase_duration, (
        (
            t.create_value_key(time = '22.75', interpolation_type = 5, value = -8.0),
        ),
        (
            t.create_value_key(time = '22.75', interpolation_type = 5, value = 0.0),
        ),
        (
            t.create_value_key(time = '22.75', interpolation_type = 5, value = -0.83),
        ),
        (
            t.create_value_key(time = '22.75', interpolation_type = 5, value = (0.0, 1.0, 0.0, 0.0)),
        ),
        (
            t.create_value_key(time = '22.75', interpolation_type = 5, value = 1),
        ),
        (),
    ), is_snapped_to_end = True)
    t.create_tl_transform(bg3.SPEAKER_SHADOWHEART, '22.75', phase_duration, (
        (
            t.create_value_key(time = '22.75', interpolation_type = 5, value = -8.0),
        ),
        (
            t.create_value_key(time = '22.75', interpolation_type = 5, value = 0.0),
        ),
        (
            t.create_value_key(time = '22.75', interpolation_type = 5, value = 0.38),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = (0.0, 0.0, 0.0, 1.0)),
        ),
        (
            t.create_value_key(time = '22.75', interpolation_type = 5, value = 1),
        ),
        (),
    ), is_snapped_to_end = True)

    t.create_tl_animation(
        bg3.SPEAKER_SHADOWHEART, '22.75', phase_duration,
        'da93b30d-478a-45c6-3eb4-5425669432a4',
        '66ce0c11-1cdb-4573-818c-a91cde00f79f',
        animation_play_start_offset = 4.8,
        fade_in = 0.0,
        fade_out = 0.0,
        is_snapped_to_end = True)
    t.create_tl_animation(
        bg3.SPEAKER_DURGE, '22.75', phase_duration,
        '216e84fd-0597-4a94-ab2a-56d4b07e6140',
        '57fa3dc0-184f-4b43-93fd-86e5496448a9',
        animation_play_start_offset = 4.8,
        fade_in = 0.0,
        fade_out = 0.0,
        is_snapped_to_end = True)

    # Camera shot 8
    t.create_tl_shot('a6db4283-ef38-4472-827c-fffd0ac04a28', '25.89', '32.48')
    t.create_tl_camera_fov('a6db4283-ef38-4472-827c-fffd0ac04a28', '25.89', '32.48', (
        t.create_value_key(time = 29.39, value_name = 'FoV', value = 22.0, interpolation_type = 2),
    ))
    t.create_tl_transform('a6db4283-ef38-4472-827c-fffd0ac04a28', '25.89', '32.48', (
        (
            t.create_value_key(time = 25.89, interpolation_type = 5, value = -7.1),
        ),
        (
            t.create_value_key(time = 25.89, interpolation_type = 5, value = 1.3),
        ),
        (
            t.create_value_key(time = 25.89, interpolation_type = 5, value = -0.9),
        ),
        (
            t.create_value_key(time = 25.89, interpolation_type = 5, value = bg3.euler_to_quaternion(-65.0, 10.0, 0.0, sequence = 'yxz')),
        ),
        (),
        (),
    ))

    t.create_tl_voice(
        bg3.SPEAKER_SHADOWHEART, '28.367', '30.24',
        short_body_reaction_node_uuid,
        fade_in = 0.0,
        fade_out = 0.0)

    """
    92.01 to 122.9 = 30.89
    26.09+

    - 74.06

    104.82 -> 30.76

    """
    t.create_tl_animation(
        bg3.SPEAKER_SHADOWHEART, '30.76', '36.62',
        'c26b9b0a-20cc-44a4-a499-18d6d78abec5',
        '536f3ddd-33e5-4b9d-a20a-b7109f6bbc76',
        animation_slot = 1,
        animation_play_start_offset = 7,
        fade_in = 1.5,
        fade_out = 0.8
    )
    t.create_tl_animation(
        bg3.SPEAKER_DURGE, '31.08', '40.8',
        'c26b9b0a-20cc-44a4-a499-18d6d78abec5',
        '90070425-bce3-4bef-b8d7-ca38a676b5cb',
        animation_slot = 1,
        animation_play_start_offset = 6.63,
        fade_in = 1.5,
        fade_out = 1.5
    )
    t.create_tl_animation(
        bg3.SPEAKER_SHADOWHEART, '36.62', '40.8',
        'c26b9b0a-20cc-44a4-a499-18d6d78abec5',
        '536f3ddd-33e5-4b9d-a20a-b7109f6bbc76',
        animation_slot = 1,
        animation_play_start_offset = 12.04,
        fade_in = 1.0,
        fade_out = 1.5
    )

    # Camera shot 9
    t.create_tl_shot('a6db4283-ef38-4472-827c-fffd0ac04a28', '32.48', '35.68', is_snapped_to_end = True)
    t.create_tl_camera_fov('a6db4283-ef38-4472-827c-fffd0ac04a28', '32.48', '45.28', (
        t.create_value_key(time = 0.0, value_name = 'FoV', value = 25.0, interpolation_type = 2),
    ))
    t.create_tl_transform('a6db4283-ef38-4472-827c-fffd0ac04a28', '32.48', '45.28', (
        (
            t.create_value_key(time = 32.48, interpolation_type = 5, value = -9.0),
        ),
        (
            t.create_value_key(time = 32.48, interpolation_type = 5, value = 1.2),
        ),
        (
            t.create_value_key(time = 32.48, interpolation_type = 5, value = -0.6),
        ),
        (
            t.create_value_key(time = 32.48, interpolation_type = 5, value = bg3.euler_to_quaternion(86.0, 4.0, 0.0, sequence = 'yxz')),
        ),
        (),
        (),
    ))

    # Camera shot 10
    t.create_tl_shot('a6db4283-ef38-4472-827c-fffd0ac04a28', '35.68', '45.28', is_snapped_to_end = True)
    t.create_tl_camera_fov('a6db4283-ef38-4472-827c-fffd0ac04a28', '35.68', '45.28', (
        t.create_value_key(time = 0.0, value_name = 'FoV', value = 25.0, interpolation_type = 2),
    ))
    t.create_tl_transform('a6db4283-ef38-4472-827c-fffd0ac04a28', '35.68', '45.28', (
        (
            t.create_value_key(time = 35.68, interpolation_type = 5, value = -8.5),
        ),
        (
            t.create_value_key(time = 35.68, interpolation_type = 5, value = 1.2),
        ),
        (
            t.create_value_key(time = 35.68, interpolation_type = 5, value = -0.9),
        ),
        (
            t.create_value_key(time = 35.68, interpolation_type = 5, value = bg3.euler_to_quaternion(56.0, 4.0, 0.0, sequence = 'yxz')),
        ),
        (),
        (),
    ))

    # Camera shot 11
    t.create_tl_shot('a6db4283-ef38-4472-827c-fffd0ac04a28', '45.28', phase_duration, is_snapped_to_end = True)
    t.create_tl_camera_fov('a6db4283-ef38-4472-827c-fffd0ac04a28', '45.28', phase_duration, (
        t.create_value_key(time = 45.28, value_name = 'FoV', value = 35.0, interpolation_type = 2),
    ))
    t.create_tl_transform('a6db4283-ef38-4472-827c-fffd0ac04a28', '45.28', phase_duration, (
        (
            t.create_value_key(time = 45.28, interpolation_type = 5, value = -9.0),
        ),
        (
            t.create_value_key(time = 45.28, interpolation_type = 5, value = 1.5),
        ),
        (
            t.create_value_key(time = 45.28, interpolation_type = 5, value = -0.5),
        ),
        (
            t.create_value_key(time = 45.28, interpolation_type = 5, value = bg3.euler_to_quaternion(64.0, 0.0, 0.0, sequence = 'yxz')),
        ),
        (),
        (),
    ))


#################################################################################################
# Dragonborns
#################################################################################################

def create_scene_shadowheart_reaction_dragonborn() -> None:

    # d = bg3.dialog_object(files.get_file('Gustav', 'Mods/GustavDev/Story/DialogsBinary/Act3/LowerCity/BhaalTemple/LOW_BhaalTemple_PostBattleDarkUrge_Resistance.lsf'))
    # t = bg3.timeline_object(files.get_file('Gustav', 'Public/GustavDev/Timeline/Generated/LOW_BhaalTemple_PostBattleDarkUrge_Resistance.lsf'), d)

    ab = game_assets.get_modded_dialog_asset_bundle('LOW_BhaalTemple_PostBattleDarkUrge_Resistance')
    d = bg3.dialog_object(ab.dialog)
    t = bg3.timeline_object(ab.timeline, d)

    slot_idx_durge = d.get_speaker_slot_index(bg3.SPEAKER_DURGE)

    d.create_standard_dialog_node(
        dragonborn_reaction_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [just_keep_safe_out_there_node_uuid],
        bg3.text_content('hd896e304g5fc4g41e7g807cg524360fee6a9', 1),
        checkflags = (
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_DRAGONBORN, True, slot_idx_durge),
            )),
        ))

    # d = 1.8
    phase_duration = '48.28'
    t.create_new_phase(dragonborn_reaction_node_uuid, phase_duration)

    t.create_tl_actor_node(bg3.timeline_object.ATTITUDE, bg3.SPEAKER_DURGE, '0.0', phase_duration, (
        t.create_attitude_key(12.15, bg3.ATTITUDE_DIAG_Pose_Stand_R_Forward_01, bg3.ATTITUDE_DIAG_T_Pose),
        t.create_attitude_key(28.81, 'a2bd89b1-8ab9-4231-ac4b-e593d75aa083', bg3.ATTITUDE_DIAG_T_Pose),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.ATTITUDE, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_attitude_key(0.0, bg3.ATTITUDE_DIAG_Pose_Stand_L_Forward_01, bg3.ATTITUDE_DIAG_T_Pose),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.EMOTION, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_emotion_key(0.0, 32),
        t.create_emotion_key(6.13, 32, variation = 2),
        t.create_emotion_key(7.34, 32),
        t.create_emotion_key(15.63, 32, variation = 1),
        t.create_emotion_key(20.58, 32),
        t.create_emotion_key(44.85 - 4.26, 32, variation = 1, is_sustained = False),
        t.create_emotion_key(51.97 - 4.26, 32)
        #t.create_emotion_key(26.0, 2)
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.EMOTION, bg3.SPEAKER_DURGE, '0.0', phase_duration, (
        t.create_emotion_key(0.0, 32, variation = 1),
        t.create_emotion_key(3.51, 32),
        t.create_emotion_key(6.08, 32, variation = 1),
        t.create_emotion_key(6.56, 32),
        t.create_emotion_key(8.26, 32, variation = 2),
        t.create_emotion_key(11.26, 32, variation = 1),
        t.create_emotion_key(22.03, 32),
        t.create_emotion_key(40.14 - 4.26, 256),
        t.create_emotion_key(44.85 - 4.26, 32),
    ), is_snapped_to_end = True)

    t.create_tl_actor_node(bg3.timeline_object.LOOK_AT, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_look_at_key(
            0.0,
            target = bg3.SPEAKER_DURGE,
            bone = 'Head_M',
            turn_mode = 3,
            turn_speed_multiplier = 0.3,
            head_turn_speed_multiplier = 0.3,
            weight = 0,
            safe_zone_angle = 80,
            head_safe_zone_angle = 80,
            reset = True,
            look_at_mode = 1,
            eye_look_at_bone = 'Head_M'),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.LOOK_AT, bg3.SPEAKER_DURGE, '0.0', phase_duration, (
        t.create_look_at_key(
            0.0,
            target = bg3.SPEAKER_SHADOWHEART,
            bone = 'Head_M',
            turn_mode = 3,
            turn_speed_multiplier = 0.3,
            head_turn_speed_multiplier = 0.3,
            weight = 0,
            safe_zone_angle = 80,
            head_safe_zone_angle = 80,
            reset = True,
            look_at_mode = 1,
            eye_look_at_bone = 'Head_M'),
    ), is_snapped_to_end = True)

    t.create_tl_material(bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, '156a2490-d796-402c-b7fc-e00c032042c1', (), (
        t.create_value_key(time = 0.0, value = True),
    ), is_snapped_to_end = True, is_continuous = True)

    # Hide helmets
    t.create_tl_show_armor(bg3.SPEAKER_DURGE, '0.0', phase_duration, (
        (
            t.create_value_key(time = 0.0, value = False, interpolation_type = 0),
            t.create_value_key(time = phase_duration, interpolation_type = 0)
        ),
        (), (), (), (), (), (), (), (), (), ()
    ))
    t.create_tl_show_armor(bg3.SPEAKER_SHADOWHEART, '0.0',  phase_duration, (
        (
            t.create_value_key(time = 0.0, value = False, interpolation_type = 0),
            t.create_value_key(time = phase_duration, interpolation_type = 0)
        ),
        (), (), (), (), (), (), (), (), (), ()
    ))

    # Hide weapons
    t.create_tl_actor_node(bg3.timeline_object.SHOW_WEAPON, bg3.SPEAKER_DURGE, '0.0', phase_duration, (
        t.create_value_key(time = 0.0, value_name = 'ShowWeapon', value = False, interpolation_type = 3),
        t.create_value_key(time = phase_duration, interpolation_type = 3),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.SHOW_WEAPON, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_value_key(time = 0.0, value_name = 'ShowWeapon', value = False, interpolation_type = 3),
        t.create_value_key(time = phase_duration, interpolation_type = 3),
    ), is_snapped_to_end = True)

    # Show Durge
    t.create_tl_actor_node(bg3.timeline_object.SHOW_VISUAL, bg3.SPEAKER_DURGE, '0.0', phase_duration, (
        t.create_value_key(time = 0.0, interpolation_type = 3),
    ), is_snapped_to_end = True)

    # Kiss part
    t.create_tl_actor_node(bg3.timeline_object.SOUND, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_sound_event_key('34.06', sound_event_id = 'ffbbbd57-5c31-444d-bc3a-c3d14df0be53', sound_object_index = 4),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.SOUND, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_sound_event_key('31.66', sound_event_id = '90a31a12-9f32-47e1-899e-cdced0705f27', sound_object_index = 4),
        t.create_sound_event_key('31.66', sound_event_id = '025fa6be-55ec-43fe-af6a-03b746163d72', sound_object_index = 4),
        t.create_sound_event_key('32.27', sound_event_id = 'ffbbbd57-5c31-444d-bc3a-c3d14df0be53', sound_object_index = 4),
        t.create_sound_event_key('35.97', sound_event_id = 'ffbbbd57-5c31-444d-bc3a-c3d14df0be53', sound_object_index = 4),
        t.create_sound_event_key('37.63', sound_event_id = '5dac329f-b08a-412d-84bc-86fc1aecae45', sound_object_index = 4),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.SOUND, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_sound_event_key(25.3, sound_event_id = '3a82ed81-3970-461a-91dc-4687caa05cce', sound_object_index = 1),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.SOUND, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_sound_event_key(26.76, sound_event_id = '3a82ed81-3970-461a-91dc-4687caa05cce', sound_object_index = 2),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.SOUND, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (), is_snapped_to_end = True)

    # Physics
    t.create_tl_actor_node(bg3.timeline_object.PHYSICS, bg3.SPEAKER_DURGE, '0.0', phase_duration, (
        t.create_value_key(time = 0.0, interpolation_type = 3, value_name = 'InverseKinematics', value = False),
        t.create_value_key(time = '22.75', interpolation_type = 3),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.PHYSICS, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_value_key(time = 0.0, interpolation_type = 3, value_name = 'InverseKinematics', value = False),
        t.create_value_key(time = '22.75', interpolation_type = 3),
    ), is_snapped_to_end = True)
    # t.create_tl_actor_node(bg3.timeline_object.PHYSICS, bg3.SPEAKER_DURGE, '0.0', phase_duration, (
    #     t.create_value_key(time = 24.55, interpolation_type = 3),
    # ), is_snapped_to_end = True)
    # t.create_tl_actor_node(bg3.timeline_object.PHYSICS, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
    #     t.create_value_key(time = 24.55, interpolation_type = 3),
    # ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.HANDS_IK, bg3.SPEAKER_DURGE, '0.0', phase_duration, (), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.HANDS_IK, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (), is_snapped_to_end = True)

    t.create_tl_animation(
        bg3.SPEAKER_DURGE,
        '0.0', '13.06',
        '84117bdc-71dd-47a2-9cba-039df0b1890d',
        'a2dae3f2-e3c9-4fc7-b8ac-82abf4a153b0',
        fade_in = 0.0,
        fade_out = 0.94)
    t.create_tl_animation(
        bg3.SPEAKER_SHADOWHEART,
        '0.0', '13.06',
        '57523fff-f67e-c3d5-59a4-b45a84d3eaec',
        'c8dad77b-5b76-44fe-bfeb-61d676ede3f6',
        fade_in = 0.0,
        fade_out = 0.94)

    t.create_tl_transform(bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = -8.0),
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

    t.create_tl_transform(bg3.SPEAKER_DURGE, '0.0', '24.55', (
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = -8.0),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 0.0),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = -0.79),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = (0.0, 1.0, 0.0, 0.0)),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 1),
        ),
        (),
    ), is_snapped_to_end = True)


    # Camera shot 2
    t.create_tl_shot('d35b098e-8c34-45ee-9dde-21adfd2410a9', '0.0', '4.2')
    t.create_tl_camera_fov('d35b098e-8c34-45ee-9dde-21adfd2410a9', '0.0', '4.2', (
        t.create_value_key(time = 0.0, value_name = 'FoV', value = 35.0, interpolation_type = 2),
    ))
    t.create_tl_transform('d35b098e-8c34-45ee-9dde-21adfd2410a9', '0.0', '4.2', (
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = -6.5),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 1.8),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = -1.0),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = bg3.euler_to_quaternion(-62.0, 0.0, 0.0, sequence = 'yxz')),
        ),
        (),
        (),
    ))

    # Camera shot 3
    t.create_tl_shot('d35b098e-8c34-45ee-9dde-21adfd2410a9', '4.2', '8.74')
    t.create_tl_camera_fov('d35b098e-8c34-45ee-9dde-21adfd2410a9', '4.2', '8.74', (
        t.create_value_key(time = '4.2', value_name = 'FoV', value = 30.0, interpolation_type = 2),
    ))
    t.create_tl_transform('d35b098e-8c34-45ee-9dde-21adfd2410a9', '4.2', '8.74', (
        (
            t.create_value_key(time = '4.2', interpolation_type = 5, value = -6.0),
        ),
        (
            t.create_value_key(time = '4.2', interpolation_type = 5, value = 2.0),
        ),
        (
            t.create_value_key(time = '4.2', interpolation_type = 5, value = -0.6),
        ),
        (
            t.create_value_key(time = '4.2', interpolation_type = 5, value = bg3.euler_to_quaternion(-74.0, 10.0, 0.0, sequence = 'yxz')),
        ),
        (),
        (),
    ))

    # Camera shot 4
    t.create_tl_shot('d35b098e-8c34-45ee-9dde-21adfd2410a9', '8.74', '12.07')
    t.create_tl_camera_fov('d35b098e-8c34-45ee-9dde-21adfd2410a9', '8.74', '12.07', (
        t.create_value_key(time = '8.74', value_name = 'FoV', value = 25.0, interpolation_type = 2),
    ))
    t.create_tl_transform('d35b098e-8c34-45ee-9dde-21adfd2410a9', '8.74', '12.07', (
        (
            t.create_value_key(time = '8.74', interpolation_type = 5, value = -10.0),
        ),
        (
            t.create_value_key(time = '8.74', interpolation_type = 5, value = 1.8),
        ),
        (
            t.create_value_key(time = '8.74', interpolation_type = 5, value = -0.1),
        ),
        (
            t.create_value_key(time = '8.74', interpolation_type = 5, value = bg3.euler_to_quaternion(90.0, 0.0, 0.0, sequence = 'yxz')),
        ),
        (),
        (),
    ))


    t.create_tl_animation(
        bg3.SPEAKER_DURGE,
        '12.12', '22.75',
        '84117bdc-71dd-47a2-9cba-039df0b1890d',
        'a2dae3f2-e3c9-4fc7-b8ac-82abf4a153b0',
        fade_in = 0.0,
        fade_out = 0.0,
        animation_play_start_offset = 6.29)
    t.create_tl_animation(
        bg3.SPEAKER_SHADOWHEART,
        '12.12', '22.75',
        '57523fff-f67e-c3d5-59a4-b45a84d3eaec',
        'c8dad77b-5b76-44fe-bfeb-61d676ede3f6',
        fade_in = 0.0,
        fade_out = 0.0,
        animation_play_start_offset = 6.29)

    # Camera shot 5
    t.create_tl_shot('d35b098e-8c34-45ee-9dde-21adfd2410a9', '12.07', '16.97')
    t.create_tl_camera_fov('d35b098e-8c34-45ee-9dde-21adfd2410a9', '12.07', '16.97', (
        t.create_value_key(time = '12.07', value_name = 'FoV', value = 35.0, interpolation_type = 2),
    ))
    t.create_tl_transform('d35b098e-8c34-45ee-9dde-21adfd2410a9', '12.07', '16.97', (
        (
            t.create_value_key(time = '12.07', interpolation_type = 5, value = -8.9),
        ),
        (
            t.create_value_key(time = '12.07', interpolation_type = 5, value = 1.8),
        ),
        (
            t.create_value_key(time = '12.07', interpolation_type = 5, value = 0.4),
        ),
        (
            t.create_value_key(time = '12.07', interpolation_type = 5, value = bg3.euler_to_quaternion(115.0, 10.0, 0.0, sequence = 'yxz')),
        ),
        (),
        (),
    ))

    # Camera shot 6
    t.create_tl_shot('d35b098e-8c34-45ee-9dde-21adfd2410a9', '16.97', '22.75')
    t.create_tl_camera_fov('d35b098e-8c34-45ee-9dde-21adfd2410a9', '16.97', '22.75', (
        t.create_value_key(time = '16.97', value_name = 'FoV', value = 35.0, interpolation_type = 2),
    ))
    t.create_tl_transform('d35b098e-8c34-45ee-9dde-21adfd2410a9', '16.97', '22.75', (
        (
            t.create_value_key(time = '16.97', interpolation_type = 5, value = -7.1),
        ),
        (
            t.create_value_key(time = '16.97', interpolation_type = 5, value = 1.75),
        ),
        (
            t.create_value_key(time = '16.97', interpolation_type = 5, value = 0.2),
        ),
        (
            t.create_value_key(time = '16.97', interpolation_type = 5, value = bg3.euler_to_quaternion(-117.0, 0.0, 0.0, sequence = 'yxz')),
        ),
        (),
        (),
    ))

    # Camera shot 10
    t.create_tl_shot('a6db4283-ef38-4472-827c-fffd0ac04a28', '22.75', '27.59')
    t.create_tl_camera_fov('a6db4283-ef38-4472-827c-fffd0ac04a28', '22.75', '27.59', (
        t.create_value_key(time = 0.0, value_name = 'FoV', value = 30.0, interpolation_type = 2),
    ))
    t.create_tl_transform('a6db4283-ef38-4472-827c-fffd0ac04a28', '22.75', '27.59', (
        (
            t.create_value_key(time = '22.75', interpolation_type = 5, value = -7.1),
        ),
        (
            t.create_value_key(time = '22.75', interpolation_type = 5, value = 1.9),
        ),
        (
            t.create_value_key(time = '22.75', interpolation_type = 5, value = -1.2),
        ),
        (
            t.create_value_key(time = '22.75', interpolation_type = 5, value = bg3.euler_to_quaternion(-44.0, 10.0, 0.0, sequence = 'yxz')),
        ),
        (),
        (),
    ))

    t.create_tl_transform(bg3.SPEAKER_DURGE, '22.75', phase_duration, (
        (
            t.create_value_key(time = '22.75', interpolation_type = 5, value = -8.0),
        ),
        (
            t.create_value_key(time = '22.75', interpolation_type = 5, value = 0.0),
        ),
        (
            t.create_value_key(time = '22.75', interpolation_type = 5, value = -0.83),
        ),
        (
            t.create_value_key(time = '22.75', interpolation_type = 5, value = (0.0, 1.0, 0.0, 0.0)),
        ),
        (
            t.create_value_key(time = '22.75', interpolation_type = 5, value = 1),
        ),
        (),
    ), is_snapped_to_end = True)

    t.create_tl_animation(
        bg3.SPEAKER_SHADOWHEART, '22.75', '27.59',
        'c4853a60-b6f2-0141-6e8e-554f013828cf',
        '66ce0c11-1cdb-4573-818c-a91cde00f79f',
        animation_play_start_offset = 3.1,
        fade_in = 0.0,
        fade_out = 0.0
    )
    t.create_tl_animation(
        bg3.SPEAKER_DURGE, '22.75', '27.59',
        'eadb7e47-a9df-423c-92b7-a8cd04bf8197',
        '57fa3dc0-184f-4b43-93fd-86e5496448a9',
        animation_play_start_offset = 3.1,
        fade_in = 1.5,
        fade_out = 0.0
    )

    # Camera shot 11
    t.create_tl_shot('a6db4283-ef38-4472-827c-fffd0ac04a28', '27.59', '34.18')
    t.create_tl_camera_fov('a6db4283-ef38-4472-827c-fffd0ac04a28', '27.59', '34.18', (
        t.create_value_key(time = 29.39, value_name = 'FoV', value = 22.0, interpolation_type = 2),
    ))
    t.create_tl_transform('a6db4283-ef38-4472-827c-fffd0ac04a28', '27.59', '34.18', (
        (
            t.create_value_key(time = '27.59', interpolation_type = 5, value = -7.1),
        ),
        (
            t.create_value_key(time = '27.59', interpolation_type = 5, value = 1.9),
        ),
        (
            t.create_value_key(time = '27.59', interpolation_type = 5, value = -0.9),
        ),
        (
            t.create_value_key(time = '27.59', interpolation_type = 5, value = bg3.euler_to_quaternion(-65.0, 10.0, 0.0, sequence = 'yxz')),
        ),
        (),
        (),
    ))

    t.create_tl_animation(
        bg3.SPEAKER_SHADOWHEART, '27.59', '48.28',
        'c4853a60-b6f2-0141-6e8e-554f013828cf',
        '66ce0c11-1cdb-4573-818c-a91cde00f79f',
        animation_play_start_offset = 10.61,
        fade_in = 0.0,
        fade_out = 1.7
    )
    t.create_tl_animation(
        bg3.SPEAKER_DURGE, '27.59', '48.28',
        'eadb7e47-a9df-423c-92b7-a8cd04bf8197',
        '57fa3dc0-184f-4b43-93fd-86e5496448a9',
        animation_play_start_offset = 10.61,
        fade_in = 0.0,
        fade_out = 1.0
    )

    t.create_tl_voice(
        bg3.SPEAKER_SHADOWHEART, '28.067', '29.94',
        dragonborn_reaction_node_uuid,
        fade_in = 0.0,
        fade_out = 0.0)

    # Camera shot 12
    t.create_tl_shot('a6db4283-ef38-4472-827c-fffd0ac04a28', '34.18', '46.98', is_snapped_to_end = True)
    t.create_tl_camera_fov('a6db4283-ef38-4472-827c-fffd0ac04a28', '34.18', '46.98', (
        t.create_value_key(time = 0.0, value_name = 'FoV', value = 25.0, interpolation_type = 2),
    ))
    t.create_tl_transform('a6db4283-ef38-4472-827c-fffd0ac04a28', '34.18', '46.98', (
        (
            t.create_value_key(time = '34.18', interpolation_type = 5, value = -9.0),
        ),
        (
            t.create_value_key(time = '34.18', interpolation_type = 5, value = 1.8),
        ),
        (
            t.create_value_key(time = '34.18', interpolation_type = 5, value = -0.6),
        ),
        (
            t.create_value_key(time = '34.18', interpolation_type = 5, value = bg3.euler_to_quaternion(86.0, 4.0, 0.0, sequence = 'yxz')),
        ),
        (),
        (),
    ))


    t.create_tl_animation(
        bg3.SPEAKER_SHADOWHEART, '30.61', '39.1',
        'c26b9b0a-20cc-44a4-a499-18d6d78abec5',
        '536f3ddd-33e5-4b9d-a20a-b7109f6bbc76',
        animation_slot = 1,
        animation_play_start_offset = 6,
        fade_in = 1.5,
        fade_out = 1.8
    )
    t.create_tl_animation(
        bg3.SPEAKER_DURGE, '30.61', '39.1',
        'c26b9b0a-20cc-44a4-a499-18d6d78abec5',
        '90070425-bce3-4bef-b8d7-ca38a676b5cb',
        animation_slot = 1,
        animation_play_start_offset = 6,
        fade_in = 1.5,
        fade_out = 1.8
    )

    # Camera shot 13
    # t.create_tl_shot('a6db4283-ef38-4472-827c-fffd0ac04a28', '53.04', '53.22', is_snapped_to_end = True)
    # t.create_tl_camera_fov('a6db4283-ef38-4472-827c-fffd0ac04a28', '41.49', '53.22', (
    #     t.create_value_key(time = '41.49', value_name = 'FoV', value = 30.0, interpolation_type = 2),
    # ))
    # t.create_tl_transform('a6db4283-ef38-4472-827c-fffd0ac04a28', '41.49', '53.22', (
    #     (
    #         t.create_value_key(time = '41.49', interpolation_type = 5, value = -7.1),
    #     ),
    #     (
    #         t.create_value_key(time = '41.49', interpolation_type = 5, value = 1.75),
    #     ),
    #     (
    #         t.create_value_key(time = '41.49', interpolation_type = 5, value = -1.1),
    #     ),
    #     (
    #         t.create_value_key(time = '41.49', interpolation_type = 5, value = bg3.euler_to_quaternion(-60.0, 0.0, 0.0, sequence = 'yxz')),
    #     ),
    #     (),
    #     (),
    # ))

    # Camera shot 14
    t.create_tl_shot('a6db4283-ef38-4472-827c-fffd0ac04a28', '46.98', phase_duration, is_snapped_to_end = True)
    t.create_tl_camera_fov('a6db4283-ef38-4472-827c-fffd0ac04a28', '46.98', phase_duration, (
        t.create_value_key(time = '46.98', value_name = 'FoV', value = 32.0, interpolation_type = 2),
    ))
    t.create_tl_transform('a6db4283-ef38-4472-827c-fffd0ac04a28', '46.98', phase_duration, (
        (
            t.create_value_key(time = '46.98', interpolation_type = 5, value = -8.5),
        ),
        (
            t.create_value_key(time = '46.98', interpolation_type = 5, value = 1.75),
        ),
        (
            t.create_value_key(time = '46.98', interpolation_type = 5, value = -0.5),
        ),
        (
            t.create_value_key(time = '46.98', interpolation_type = 5, value = bg3.euler_to_quaternion(45.0, 0.0, 0.0, sequence = 'yxz')),
        ),
        (),
        (),
    ))


bg3.add_build_procedure('create_scene_shadowheart_cries_when_durge_dies', create_scene_shadowheart_cries_when_durge_dies)
bg3.add_build_procedure('create_scene_shadowheart_reaction_body_type_1', create_scene_shadowheart_reaction_body_type_1)
bg3.add_build_procedure('create_scene_shadowheart_reaction_body_type_2', create_scene_shadowheart_reaction_body_type_2)
bg3.add_build_procedure('create_scene_shadowheart_reaction_body_type_2_gith', create_scene_shadowheart_reaction_body_type_2_gith)
bg3.add_build_procedure('create_scene_shadowheart_reaction_body_type_3', create_scene_shadowheart_reaction_body_type_3)
bg3.add_build_procedure('create_scene_shadowheart_reaction_body_type_4', create_scene_shadowheart_reaction_body_type_4)
bg3.add_build_procedure('create_scene_shadowheart_reaction_dwarf', create_scene_shadowheart_reaction_dwarf)
bg3.add_build_procedure('create_scene_shadowheart_reaction_short_races', create_scene_shadowheart_reaction_short_races)
bg3.add_build_procedure('create_scene_shadowheart_reaction_dragonborn', create_scene_shadowheart_reaction_dragonborn)

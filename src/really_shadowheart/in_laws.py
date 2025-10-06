from __future__ import annotations

import bg3moddinglib as bg3

from .context import game_assets
from .flags import *


def create_father_blessing() -> None:
    # d = bg3.dialog_object(files.get_file('Gustav', 'Mods/GustavDev/Story/DialogsBinary/Camp/CAMP_ShadowheartFather.lsf'))
    # t = bg3.timeline_object(files.get_file('Gustav', 'Public/GustavDev/Timeline/Generated/CAMP_ShadowheartFather.lsf'), d)

    ab = game_assets.get_modded_dialog_asset_bundle('CAMP_ShadowheartFather')
    d = bg3.dialog_object(ab.dialog)
    t = bg3.timeline_object(ab.timeline, d)

    t.edit_tl_shot('6abff845-8bde-4dd9-8c25-3b4b330decf6', camera_uuid = 'fd554d55-be9b-46a1-933f-cdf092edd3fa')

    speaker_idx_arnell = d.get_speaker_slot_index(bg3.SPEAKER_ARNELL)
    speaker_idx_tav = d.get_speaker_slot_index(bg3.SPEAKER_PLAYER)

    im_starting_to_feel_like_my_old_self_node_uuid = '1b359f97-0956-d5b2-eb98-70e9c04d537e' # existing node
    as_i_am_node_uuid = 'ae294ef8-462f-3e25-0602-ea06c5b1e9aa'
    a_great_deal_of_damage_node_uuid = 'c1de0c29-e80e-62cc-850c-dbedaae22f00' # existing node
    you_are_more_than_a_friend_node_uuid = '2181cccc-b98e-883e-96f5-48f5b3f2a175' # existing node fd554d55-be9b-46a1-933f-cdf092edd3fa
    i_have_scant_energy_node_uuid = '5f3e36f4-de70-cfa4-f352-63bc57ade1aa' # existing node 83869b9f-cc18-49cf-a461-0901c0e990d3 96880158-7e0a-49b4-b531-2b9b56ef630f
    selunes_blessings_to_you = 'b61e5345-248c-bf9a-d812-c9e355156245' # existing node

    ask_for_arnell_blessing_node_uuid = 'e81436ee-279a-4daf-94a8-3d305dc1b5cd'
    alias_you_are_more_than_a_friend_node_uuid = '72bc185a-871d-4fd5-a5f8-8361c8d2b941'
    alias_i_have_scant_energy_node_uuid = '11bc692b-52ae-418e-9729-486fc8898b37'
    alias_selunes_blessings_to_you = '97bc91b2-8824-42dc-ad47-22bf491dd914'
    jump_back_node_uuid = 'e5618bb8-5fac-4965-85b7-965fc6f757b1'

    shadowheart_approval_arnell_plus_5 = bg3.reaction_object.create_new(game_assets.files, { bg3.SPEAKER_SHADOWHEART : 5 }, uuid = '0244a6ae-603f-4ab2-9253-c39adb90c135')

    d.add_dialog_flags(as_i_am_node_uuid, checkflags = (
        bg3.flag_group('Object', (
            bg3.flag(bg3.FLAG_ORI_State_PartneredWithShadowheart, False, speaker_idx_tav),
        )),
    ))
    d.set_dialog_flags(im_starting_to_feel_like_my_old_self_node_uuid, checkflags = (
        bg3.flag_group('Global', (
            bg3.flag(bg3.FLAG_NIGHT_Shadowheart_DaughterTears, True, None),
        )),
    ))
    d.set_dialog_flags(selunes_blessings_to_you, checkflags = (
        bg3.flag_group('Global', (
            bg3.flag(bg3.FLAG_NIGHT_Shadowheart_DaughterTears, True, None),
            bg3.flag(Parents_New_Clothes.uuid, True, None),
        )),
        bg3.flag_group('Object', (
            bg3.flag(Arnell_Blessed_Tav.uuid, True, speaker_idx_arnell),
        )),
    ))
    d.remove_root_node(selunes_blessings_to_you)
    idx = d.get_root_node_index(im_starting_to_feel_like_my_old_self_node_uuid)
    d.add_root_node(selunes_blessings_to_you, index = idx)

    d.create_standard_dialog_node(
        ask_for_arnell_blessing_node_uuid,
        bg3.SPEAKER_PLAYER,
        [alias_you_are_more_than_a_friend_node_uuid],
        bg3.text_content('h125217edg1082g4ad3g9b56g5b01a63b6b54', 1),
        constructor = bg3.dialog_object.QUESTION,
        approval_rating_uuid = shadowheart_approval_arnell_plus_5.uuid,
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(Arnell_Blessed_Tav.uuid, False, speaker_idx_arnell),
            )),
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_State_PartneredWithShadowheart, True, speaker_idx_tav),
            ))
        ),
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(Arnell_Blessed_Tav.uuid, True, speaker_idx_arnell),
            )),
        ))
    d.add_child_dialog_node(a_great_deal_of_damage_node_uuid, ask_for_arnell_blessing_node_uuid, 0)

    d.create_alias_dialog_node(
        alias_you_are_more_than_a_friend_node_uuid,
        you_are_more_than_a_friend_node_uuid,
        [alias_i_have_scant_energy_node_uuid])

    d.create_alias_dialog_node(
        alias_i_have_scant_energy_node_uuid,
        i_have_scant_energy_node_uuid,
        [alias_selunes_blessings_to_you])

    d.create_alias_dialog_node(
        alias_selunes_blessings_to_you,
        selunes_blessings_to_you,
        [jump_back_node_uuid])

    d.create_jump_dialog_node(jump_back_node_uuid, a_great_deal_of_damage_node_uuid, 2)

    # Arnell, please take a look at spare clothes in the camp chest. Take anything you and your wife like.
    d.create_standard_dialog_node(
        'd5ac6927-c1e3-430b-849b-c8e8404d66e4',
        bg3.SPEAKER_PLAYER,
        ['60010520-319e-4d94-b450-f20122f64449'],
        bg3.text_content('hd4092dd1g4eedg4d71g8f62gdd7bcbee39c5', 1),
        constructor = bg3.dialog_object.QUESTION,
        checkflags = (
            bg3.flag_group('Global', (
                bg3.flag(Parents_Change_Clothes.uuid, False, None),
                bg3.flag(Parents_New_Clothes.uuid, False, None),
            )),
        ),
        setflags = (
            bg3.flag_group('Global', (
                bg3.flag(Parents_Change_Clothes.uuid, True, None),
            )),
        ))
    d.add_child_dialog_node(a_great_deal_of_damage_node_uuid, 'd5ac6927-c1e3-430b-849b-c8e8404d66e4', 1)

    # Response to the above
    d.create_alias_dialog_node(
        '60010520-319e-4d94-b450-f20122f64449',
        selunes_blessings_to_you,
        [],
        end_node = True)


def create_mother_blessing() -> None:
    # d = bg3.dialog_object(files.get_file('Gustav', 'Mods/GustavDev/Story/DialogsBinary/Camp/CAMP_ShadowheartMother.lsf'))
    # t = bg3.timeline_object(files.get_file('Gustav', 'Public/GustavDev/Timeline/Generated/CAMP_ShadowheartMother.lsf'), d)

    ab = game_assets.get_modded_dialog_asset_bundle('CAMP_ShadowheartMother')
    d = bg3.dialog_object(ab.dialog)
    t = bg3.timeline_object(ab.timeline, d)

    t.edit_tl_shot('450e36f1-052c-476e-a6b0-0c8089593f80', camera_uuid = 'dfb96c7d-cab7-428d-8d7d-dc66f4a8ae68')

    speaker_idx_emmeline = d.get_speaker_slot_index(bg3.SPEAKER_EMMELINE)
    speaker_idx_tav = d.get_speaker_slot_index(bg3.SPEAKER_PLAYER)

    my_daughter_found_her_way_node_uuid = '9e700c80-98f1-abb3-04f8-9e5e6cfb1920' # existing node
    jump_over_blessing_line_node_uuid = '31d72b14-0c1c-bb6b-400a-3161ff02f1ec' # existing node
    i_think_things_will_be_better_node_uuid = 'e089901d-c67f-b6a7-fe22-1e2b62523fe3' # existing node af01c9d1-c36f-4d43-8b6d-91442def3526
    much_time_has_been_lost_but_no_more_node_uuid = '10199a18-2c5d-12e9-af66-ce2c57699835' # existing node
    more_than_a_friend_node_uuid = '84c53c31-04ae-7633-1665-d508a3516ded' # existing node dfb96c7d-cab7-428d-8d7d-dc66f4a8ae68 af01c9d1-c36f-4d43-8b6d-91442def3526
    moonmaidens_blessings_to_you_node_uuid = '9033ecc1-3339-a3ac-ab6b-f53fe59b0895' # existing node af01c9d1-c36f-4d43-8b6d-91442def3526

    ask_for_emmeline_blessing_node_uuid = '73491b02-79fb-4231-bd34-10764f378f8b'
    alias_more_than_a_friend_node_uuid = '4b729eb2-8704-4dec-a582-0f32abc5b2f6'
    alias_moonmaidens_blessings_to_you_node_uuid = '05a06dbf-0ae4-42d4-a613-aeccd7f379ab'
    jump_back_node_uuid = 'a97b0b42-c656-4c41-a0fa-b6a367b8d602'

    shadowheart_approval_emmeline_plus_5 = bg3.reaction_object.create_new(files, { bg3.SPEAKER_SHADOWHEART : 5 }, uuid = 'c1ad49b6-eda5-4f11-bc8f-a891e23a1e9f')

    d.add_dialog_flags(more_than_a_friend_node_uuid, setflags = (
        bg3.flag_group('Object', (
            bg3.flag(Emmeline_Blessed_Tav.uuid, True, speaker_idx_emmeline),
        )),
    ))
    d.set_dialog_flags(i_think_things_will_be_better_node_uuid, checkflags = (
        bg3.flag_group('Global', (
            bg3.flag(bg3.FLAG_NIGHT_Shadowheart_DaughterTears, True, None),
        )),
    ))
    d.set_dialog_flags(moonmaidens_blessings_to_you_node_uuid, checkflags = (
        bg3.flag_group('Global', (
            bg3.flag(bg3.FLAG_NIGHT_Shadowheart_DaughterTears, True, None),
            bg3.flag(Parents_New_Clothes.uuid, True, None),
        )),
        bg3.flag_group('Object', (
            bg3.flag(Emmeline_Blessed_Tav.uuid, True, speaker_idx_emmeline),
        )),
    ))
    d.remove_root_node(moonmaidens_blessings_to_you_node_uuid)
    idx = d.get_root_node_index(i_think_things_will_be_better_node_uuid)
    d.add_root_node(moonmaidens_blessings_to_you_node_uuid, index = idx)

    d.delete_all_children_dialog_nodes(my_daughter_found_her_way_node_uuid)
    d.add_child_dialog_node(my_daughter_found_her_way_node_uuid, jump_over_blessing_line_node_uuid)

    d.create_standard_dialog_node(
        ask_for_emmeline_blessing_node_uuid,
        bg3.SPEAKER_PLAYER,
        [alias_more_than_a_friend_node_uuid],
        bg3.text_content('h546e7566g6d98g4af1gb48fgeffb8d0a5de2', 1),
        constructor = bg3.dialog_object.QUESTION,
        approval_rating_uuid = shadowheart_approval_emmeline_plus_5.uuid,
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(Emmeline_Blessed_Tav.uuid, False, speaker_idx_emmeline),
            )),
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_State_PartneredWithShadowheart, True, speaker_idx_tav),
            ))
        ),
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(Emmeline_Blessed_Tav.uuid, True, speaker_idx_emmeline),
            )),
        ))
    d.add_child_dialog_node(much_time_has_been_lost_but_no_more_node_uuid, ask_for_emmeline_blessing_node_uuid, 0)

    d.create_alias_dialog_node(
        alias_more_than_a_friend_node_uuid,
        more_than_a_friend_node_uuid,
        [alias_moonmaidens_blessings_to_you_node_uuid])

    d.create_alias_dialog_node(
        alias_moonmaidens_blessings_to_you_node_uuid,
        moonmaidens_blessings_to_you_node_uuid,
        [jump_back_node_uuid])

    d.create_jump_dialog_node(jump_back_node_uuid, much_time_has_been_lost_but_no_more_node_uuid, 2)

    # Remove silly sharran insults
    d.delete_child_dialog_node('239ecc20-27cb-4cf7-b144-e3c0cb55fdcc', 'b8f89706-1717-bf03-79aa-092d686feee6')
    d.delete_child_dialog_node('10199a18-2c5d-12e9-af66-ce2c57699835', 'b818a107-9a77-0635-8089-f13c3c7c0598')

    # Emmeline, please take a look at spare clothes in the camp chest. Take anything you and your husband like.
    d.create_standard_dialog_node(
        '93db99f3-73d9-4bba-8e6c-e9f9198e25d9',
        bg3.SPEAKER_PLAYER,
        ['7a42de69-a9b0-4699-a2aa-e6dbeda2decd'],
        bg3.text_content('h2c5d201fgd8eag4bc1gb4a2gbf1158cce723', 1),
        constructor = bg3.dialog_object.QUESTION,
        checkflags = (
            bg3.flag_group('Global', (
                bg3.flag(Parents_Change_Clothes.uuid, False, None),
                bg3.flag(Parents_New_Clothes.uuid, False, None),
            )),
        ),
        setflags = (
            bg3.flag_group('Global', (
                bg3.flag(Parents_Change_Clothes.uuid, True, None),
            )),
        ))
    d.add_child_dialog_node(much_time_has_been_lost_but_no_more_node_uuid, '93db99f3-73d9-4bba-8e6c-e9f9198e25d9', 1)

    # Response to the above
    d.create_alias_dialog_node(
        '7a42de69-a9b0-4699-a2aa-e6dbeda2decd',
        moonmaidens_blessings_to_you_node_uuid,
        [],
        end_node = True)


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


def patch_shadowheart_father_conversation() -> None:
    # d = bg3.dialog_object(files.get_file('Gustav', 'Mods/GustavDev/Story/DialogsBinary/Camp/CAMP_ShadowheartFather.lsf'))
    # t = bg3.timeline_object(files.get_file('Gustav', 'Public/GustavDev/Timeline/Generated/CAMP_ShadowheartFather.lsf'), d)

    ab = game_assets.get_modded_dialog_asset_bundle('CAMP_ShadowheartFather')
    d = bg3.dialog_object(ab.dialog)
    t = bg3.timeline_object(ab.timeline, d)

    speaker_idx_arnell = d.get_speaker_slot_index(bg3.SPEAKER_ARNELL)
    speaker_idx_shadowheart = d.get_speaker_slot_index(bg3.SPEAKER_PLAYER) # that's right, these nodes are under the REALLY_SHADOWHEART tag

    first_time_met_root_node_uuid = 'b0ea6f07-ed37-40ac-b140-d57b655acc79'
    next_time_met_root_node_uuid = 'a04d4497-c24f-94ac-dc49-38e452518593'
    questions_countainer_node_uuid = '185a727b-9969-194c-9a7b-419d6db414ac'
    jump_back_next_time_met_node_uuid = '09426951-149b-4454-a1df-79719b8fe644'

    hug_your_father_node_uuid = '55465ca5-cd29-457d-b870-81e587308d26'
    hug_your_father_cinematic_node_uuid = '2a045921-1cc3-44dd-a68f-e18b1feb3f4a'
    please_take_a_look_at_spare_clothes_node_uuid = '8afa90be-01c9-4c80-a460-69251a9b8ef0'

    d.create_jump_dialog_node(jump_back_next_time_met_node_uuid, questions_countainer_node_uuid, 2)

    camera_visual_state_next_time_met_node_uuid = '51095229-4738-4095-9d27-1a4010d82527'
    d.create_cinematic_dialog_node(camera_visual_state_next_time_met_node_uuid, [jump_back_next_time_met_node_uuid])
    t.create_new_phase(camera_visual_state_next_time_met_node_uuid, '1.0')
    t.create_tl_actor_node(bg3.timeline_object.EMOTION, bg3.SPEAKER_PLAYER, '0.0', '1.0', (
        t.create_emotion_key(0.0, 2),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.EMOTION, bg3.SPEAKER_EMMELINE, '0.0', '1.0', (
        t.create_emotion_key(0.0, 2),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.ATTITUDE, bg3.SPEAKER_PLAYER, '0.0', '1.0', (
        t.create_attitude_key(0.0, bg3.ATTITUDE_DIAG_Pose_Stand_L_Forward_01, bg3.ATTITUDE_DIAG_T_Pose),
    ), is_snapped_to_end = True)
    t.create_tl_shot('7091f151-e3ed-495b-bcac-fd4b67077896', '0.0', '1.0', is_snapped_to_end = True)

    #
    # The following unblocks two conversations with Arnell, and allows Shadowheart to hug him and to ask more questions.
    #

    # The first conversation
    # Jenevelle. I still can't believe you freed us - that I'm standing here with you. I'd ask you to slap me so I know it's real, but I don't think I'm yet strong enough to bear it.
    d.set_dialog_flags(
        first_time_met_root_node_uuid,
        checkflags = (
            bg3.flag_group('Global', (
                bg3.flag(Parents_Long_Rested.uuid, False, None),
            )),
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_REALLY_SHADOWHEART, True, speaker_idx_shadowheart),
            )),
        ),
        setflags = ())

    # That name. I don't know how I feel about it.
    d.set_dialog_flags('b125a503-01c9-4102-90b1-2f19c037ae61', checkflags = ())

    # How is mother coping?
    d.set_dialog_flags('79429359-7135-44af-ea4a-6707246c6b20', checkflags = ())

    # They made me do things to you both, all those years. Please - I need to know.
    d.set_dialog_flags('8dca6afa-4da7-81d3-78af-bc6eb3469c0b', checkflags = ())

    # The second conversation
    d.set_dialog_flags(
        next_time_met_root_node_uuid,
        checkflags = (
            bg3.flag_group('Global', (
                bg3.flag(Parents_Long_Rested.uuid, True, None),
            )),
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_REALLY_SHADOWHEART, True, speaker_idx_shadowheart),
            )),
        ),
        setflags = ())
    d.set_dialog_flags('98431286-3a30-8326-b48b-25d51f5a2967', checkflags = ())
    d.set_dialog_flags('e7ef8506-e92c-d403-ac8f-afed2cc8b804', checkflags = ())
    d.set_dialog_flags('7a08df41-cfc1-a8f3-4918-d0ce12a6bf4b', checkflags = ())
    d.set_dialog_flags('ba348ef5-ede6-3913-25f9-91fef63c2388', checkflags = ())
    d.set_dialog_flags('3f072379-513c-be8f-863b-f2b9482678f7', checkflags = ())

    d.set_tagged_text('a93f4188-effd-0040-72b9-6dae71999415', bg3.text_content('h37557230gd8d3g4f9aga4c5gf62aa3431da5', 1))
    d.remove_dialog_attribute('a93f4188-effd-0040-72b9-6dae71999415', 'endnode')
    d.add_child_dialog_node('a93f4188-effd-0040-72b9-6dae71999415', 'f64b31f0-8cc1-430f-bc7d-d4bf172186c1')
    d.create_alias_dialog_node('f64b31f0-8cc1-430f-bc7d-d4bf172186c1', 'b61e5345-248c-bf9a-d812-c9e355156245', [], end_node = True)

    # Dad, please take a look at spare clothes in the camp chest. You and mom both need a wardrobe refresh.
    d.create_standard_dialog_node(
        please_take_a_look_at_spare_clothes_node_uuid,
        bg3.SPEAKER_PLAYER,
        ['f64b31f0-8cc1-430f-bc7d-d4bf172186c1'],
        bg3.text_content('hef65e31dgcdc2g47b4g9622gd3f1b9c9377e', 1),
        constructor = bg3.dialog_object.QUESTION,
        checkflags = (
            bg3.flag_group('Global', (
                bg3.flag(Parents_Change_Clothes.uuid, False, None),
                bg3.flag(Parents_New_Clothes.uuid, False, None),
            )),
        ),
        setflags = (
            bg3.flag_group('Global', (
                bg3.flag(Parents_Change_Clothes.uuid, True, None),
            )),
        ))
    d.add_child_dialog_node(questions_countainer_node_uuid, please_take_a_look_at_spare_clothes_node_uuid, 0)


    d.create_standard_dialog_node(
        hug_your_father_node_uuid,
        bg3.SPEAKER_PLAYER,
        [hug_your_father_cinematic_node_uuid],
        bg3.text_content('hb1bbbc3fg1b4cg4e71g9adcg847742345a11', 1),
        constructor = bg3.dialog_object.QUESTION,
        show_once = True)
    d.add_child_dialog_node(questions_countainer_node_uuid, hug_your_father_node_uuid, 0)

    # 62dc4211-3d45-4e20-b6bc-62e18087b085 A  -> A
    # 7091f151-e3ed-495b-bcac-fd4b67077896 A  -> SH
    # c38ee662-77b7-4728-9069-7f0e16484d6c SH -> A
    # fd554d55-be9b-46a1-933f-cdf092edd3fa SH -> A
    # 21f38a7e-227a-4a8c-b15d-7fdf9b250376 A  -> SH
    # 917bfa60-5513-469c-871c-6e423115979c A  -> A
    # 83869b9f-cc18-49cf-a461-0901c0e990d3 SH -> SH

    d.create_cinematic_dialog_node(hug_your_father_cinematic_node_uuid, [camera_visual_state_next_time_met_node_uuid])
    create_hug_timeline(
        hug_your_father_cinematic_node_uuid,
        t,
        bg3.SPEAKER_ARNELL,
        bg3.SPEAKER_PLAYER,
        'c38ee662-77b7-4728-9069-7f0e16484d6c',
        'fd554d55-be9b-46a1-933f-cdf092edd3fa',
        '21f38a7e-227a-4a8c-b15d-7fdf9b250376',
        '83869b9f-cc18-49cf-a461-0901c0e990d3')


def patch_shadowheart_mother_conversation() -> None:
    # d = bg3.dialog_object(files.get_file('Gustav', 'Mods/GustavDev/Story/DialogsBinary/Camp/CAMP_ShadowheartMother.lsf'))
    # t = bg3.timeline_object(files.get_file('Gustav', 'Public/GustavDev/Timeline/Generated/CAMP_ShadowheartMother.lsf'), d)

    ab = game_assets.get_modded_dialog_asset_bundle('CAMP_ShadowheartMother')
    d = bg3.dialog_object(ab.dialog)
    t = bg3.timeline_object(ab.timeline, d)

    speaker_idx_emmeline = d.get_speaker_slot_index(bg3.SPEAKER_EMMELINE)
    speaker_idx_shadowheart = d.get_speaker_slot_index(bg3.SPEAKER_PLAYER) # that's right, these nodes are under the REALLY_SHADOWHEART tag

    first_time_met_root_node_uuid = 'f5b88d43-4cbb-4f30-b6b2-a9f75f478ecf'
    next_time_met_root_node_uuid = '507c79c7-bcb4-e764-d21e-4dfe6451c7d2'
    jump_back_next_time_met_node_uuid = 'f9de8c06-354f-495a-83e9-a7d703180449'
    please_take_a_look_at_spare_clothes_node_uuid = '2a0efe96-1e7e-4c85-82e5-acd29131916a'

    hug_your_mother_node_uuid = '2269bc5b-011e-4b44-abd8-172f3d9f09a1'
    hug_your_mother_cinematic_node_uuid = '54507de4-524f-4ab1-ada7-4632a26de7fc'

    d.create_jump_dialog_node(jump_back_next_time_met_node_uuid, next_time_met_root_node_uuid, 2)

    # Shadowheart meets her mother
    # A simple visual state node to swicth camera and jump back to the root node
    camera_visual_state_next_time_met_node_uuid = '90e191ae-3519-4886-a27c-e3f7e22141eb'
    d.create_cinematic_dialog_node(camera_visual_state_next_time_met_node_uuid, [jump_back_next_time_met_node_uuid])
    t.create_new_phase(camera_visual_state_next_time_met_node_uuid, '1.0')
    t.create_tl_actor_node(bg3.timeline_object.EMOTION, bg3.SPEAKER_PLAYER, '0.0', '1.0', (
        t.create_emotion_key(0.0, 2),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.EMOTION, bg3.SPEAKER_EMMELINE, '0.0', '1.0', (
        t.create_emotion_key(0.0, 2),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.ATTITUDE, bg3.SPEAKER_PLAYER, '0.0', '1.0', (
        t.create_attitude_key(0.0, bg3.ATTITUDE_DIAG_Pose_Stand_L_Forward_01, bg3.ATTITUDE_DIAG_T_Pose),
    ), is_snapped_to_end = True)
    t.create_tl_shot('ee9b4766-8a6a-463c-8402-342a2a18da5c', '0.0', '1.0', is_snapped_to_end = True)

    #
    # The following unblocks two conversations with Emmeline, and allows Shadowheart to hug her and to ask more questions.
    #

    # The first conversation
    d.set_dialog_flags(
        first_time_met_root_node_uuid,
        checkflags = (
            bg3.flag_group('Global', (
                bg3.flag(Parents_Long_Rested.uuid, False, None),
            )),
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_REALLY_SHADOWHEART, True, speaker_idx_shadowheart),
            )),
        ),
        setflags = ())

    d.set_dialog_flags('512afac7-9a75-ec39-9a41-cab31b24ae89', checkflags = ())

    # The second conversation
    d.set_dialog_flags(
        next_time_met_root_node_uuid,
        checkflags = (
            bg3.flag_group('Global', (
                bg3.flag(Parents_Long_Rested.uuid, True, None),
            )),
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_REALLY_SHADOWHEART, True, speaker_idx_shadowheart),
            )),
        ),
        setflags = ())

    # Mom, please take a look at spare clothes in the camp chest. You and dad both need a wardrobe refresh.
    d.create_standard_dialog_node(
        please_take_a_look_at_spare_clothes_node_uuid,
        bg3.SPEAKER_PLAYER,
        ['2371802d-44b5-4652-bce1-c74d07e8840b'],
        bg3.text_content('h7721fd74g9dc2g4582gb2dagf2d24e9c1d0d', 1),
        constructor = bg3.dialog_object.QUESTION,
        checkflags = (
            bg3.flag_group('Global', (
                bg3.flag(Parents_Change_Clothes.uuid, False, None),
                bg3.flag(Parents_New_Clothes.uuid, False, None),
            )),
        ),
        setflags = (
            bg3.flag_group('Global', (
                bg3.flag(Parents_Change_Clothes.uuid, True, None),
            )),
        ))
    d.add_child_dialog_node(next_time_met_root_node_uuid, please_take_a_look_at_spare_clothes_node_uuid, 0)

    # What comes now?
    d.set_dialog_flags('94385072-8c73-3194-02c2-1175302ac75e', checkflags = ())

    # Are you feeling any better now?
    d.set_dialog_flags('645683ad-d6ba-f2ae-a6bf-d60a572fc63d', checkflags = ())

    # How do you feel?
    d.set_dialog_flags('83a1f37e-e8ee-0975-631a-08d74b5593ab', checkflags = ())

    # I love you, Mom. We'll talk more later.
    d.set_tagged_text('c889e56c-d7ba-e174-1b60-b4aa03831f1f', bg3.text_content('h33808f4bgb870g4fb2ga349g1e07c902ac97', 1))
    d.remove_dialog_attribute('c889e56c-d7ba-e174-1b60-b4aa03831f1f', 'endnode')
    d.add_child_dialog_node('c889e56c-d7ba-e174-1b60-b4aa03831f1f', '2371802d-44b5-4652-bce1-c74d07e8840b')
    d.create_alias_dialog_node('2371802d-44b5-4652-bce1-c74d07e8840b', '9033ecc1-3339-a3ac-ab6b-f53fe59b0895', [], end_node = True)

    d.create_standard_dialog_node(
        hug_your_mother_node_uuid,
        bg3.SPEAKER_PLAYER,
        [hug_your_mother_cinematic_node_uuid],
        bg3.text_content('hf2a5e82ag0a76g41d3g8567g66b82c583fa9', 1),
        constructor = bg3.dialog_object.QUESTION,
        show_once = True)
    d.add_child_dialog_node(next_time_met_root_node_uuid, hug_your_mother_node_uuid, 0)

    d.create_cinematic_dialog_node(hug_your_mother_cinematic_node_uuid, [camera_visual_state_next_time_met_node_uuid])
    # create_hug_timeline(
    #     hug_your_mother_cinematic_node_uuid,
    #     t,
    #     bg3.SPEAKER_EMMELINE,
    #     bg3.SPEAKER_PLAYER,
    #     'ee9b4766-8a6a-463c-8402-342a2a18da5c',
    #     '69a75b81-3fda-4daf-965f-7c07017f8e39',
    #     'af01c9d1-c36f-4d43-8b6d-91442def3526',
    #     'bb303f77-d07a-4d46-8525-41c8fcb3e2b7')

    # dfb96c7d-cab7-428d-8d7d-dc66f4a8ae68 M -> M
    # af01c9d1-c36f-4d43-8b6d-91442def3526 S -> M
    # ee9b4766-8a6a-463c-8402-342a2a18da5c M -> S
    # 69a75b81-3fda-4daf-965f-7c07017f8e39 S -> S
    # bb303f77-d07a-4d46-8525-41c8fcb3e2b7 M -> S
    # c1f7d129-55e1-4a3f-b272-242551bec6e4 S -> M
    create_hug_timeline(
        hug_your_mother_cinematic_node_uuid,
        t,
        bg3.SPEAKER_EMMELINE,
        bg3.SPEAKER_PLAYER,
        'bb303f77-d07a-4d46-8525-41c8fcb3e2b7',
        #'69a75b81-3fda-4daf-965f-7c07017f8e39',
        'c1f7d129-55e1-4a3f-b272-242551bec6e4',
        'ee9b4766-8a6a-463c-8402-342a2a18da5c',
        'af01c9d1-c36f-4d43-8b6d-91442def3526')


def patch_parents_visuals() -> None:
    gf = game_assets.files.get_file('Gustav', 'Public/GustavDev/Content/[PAK]_CharacterVisuals/_merged.lsf', mod_specific = True)

    children = gf.xml.find('./region[@id="CharacterVisualBank"]/node[@id="CharacterVisualBank"]/children')
    if children is None:
        raise RuntimeError("failed to patch parents visuals")
    resources = children.findall('./node[@id="Resource"]')
    arnell_visual_res = None
    emmeline_visual_res = None
    for resource in resources:
        if bg3.get_required_bg3_attribute(resource, 'Name') == 'S_LOW_ShadowheartFather_c12d561f-beae-4ef6-917e-0bec2f829449':
            arnell_visual_res = resource
        elif bg3.get_required_bg3_attribute(resource, 'Name') == 'S_LOW_ShadowheartMother_d085272a-f1d0-4ff8-a498-80728030f83e':
            emmeline_visual_res = resource
        else:
            children.remove(resource)
    if arnell_visual_res is None or emmeline_visual_res is None:
        raise RuntimeError("failed to patch parents visuals")
    bg3.set_bg3_attribute(arnell_visual_res, 'ShowEquipmentVisuals', 'True')
    bg3.set_bg3_attribute(emmeline_visual_res, 'ShowEquipmentVisuals', 'True')

    arnell_visual_res_children = arnell_visual_res.find('./children')
    if arnell_visual_res_children is None:
        raise RuntimeError("failed to patch parents visuals")
    arnell_visual_res_slots = arnell_visual_res_children.findall('./node[@id="Slots"]')
    for slot in arnell_visual_res_slots:
        slot_name = bg3.get_required_bg3_attribute(slot, 'Slot')
        if slot_name == 'Body' or slot_name == 'Footwear':
            arnell_visual_res_children.remove(slot)
    arnell_visual_res_children.append(bg3.et.fromstring(''.join([
        '<node id="Slots">',
        '<attribute id="Bone" type="FixedString" value="" />',
        '<attribute id="Slot" type="FixedString" value="Underwear" />',
        '<attribute id="VisualResource" type="FixedString" value="341f3344-a56c-3c54-8b97-65c1d86fc71e" />',
        '</node>'])))

    emmeline_visual_res_children = emmeline_visual_res.find('./children')
    if emmeline_visual_res_children is None:
        raise RuntimeError("failed to patch parents visuals")
    emmeline_visual_res_slots = emmeline_visual_res_children.findall('./node[@id="Slots"]')
    for slot in emmeline_visual_res_slots:
        slot_name = bg3.get_required_bg3_attribute(slot, 'Slot')
        if slot_name == 'Body' or slot_name == 'Footwear':
            emmeline_visual_res_children.remove(slot)
    emmeline_visual_res_children.append(bg3.et.fromstring(''.join([
        '<node id="Slots">',
        '<attribute id="Bone" type="FixedString" value="" />',
        '<attribute id="Slot" type="FixedString" value="Underwear" />',
        '<attribute id="VisualResource" type="FixedString" value="69d9e1e0-7548-00a4-15ef-a52622f9ceb1" />',
        '</node>'])))


bg3.add_build_procedure('create_father_blessing', create_father_blessing)
bg3.add_build_procedure('create_mother_blessing', create_mother_blessing)
bg3.add_build_procedure('patch_shadowheart_father_conversation', patch_shadowheart_father_conversation)
bg3.add_build_procedure('patch_shadowheart_mother_conversation', patch_shadowheart_mother_conversation)
bg3.add_build_procedure('patch_parents_visuals', patch_parents_visuals)
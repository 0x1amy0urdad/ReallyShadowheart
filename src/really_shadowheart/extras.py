from __future__ import annotations

import bg3moddinglib as bg3

from .context import game_assets
from .dialog_overrides import add_dialog_dependency, get_dialog_uuid
from .flags import *


def create_obfuscate_text_content() -> None:
    content = {
        # Obfuscate region
        "hddc41f9ag5022g431ag831cgc37e5af1cc72": (1, "&lt;i&gt;Tell her about your Master Sophia who taught you everything. Recall the pain you felt when she died.&lt;/i&gt;"),
        "hef879f48gf239g4f67g934cg234e684f2571": (1, "&lt;i&gt;Share your memories about Jarell, about his best years as a faithful warrior of Selûne, and the darkness that swallowed him afterwards...&lt;/i&gt;"),
        "hbadfd58fg48e6g48f1g8cd6g540840681696": (1, "&lt;i&gt;Take a deep breath, and tell her about your deepest fear of failing your friends; tell her about the heavy burden of responsibility, and hard choices you had to make.&lt;/i&gt;"),
        "h41e16b9cg1017g419bga093ge2ec19add985": (1, "Do you think my deeds made this world better... am I the person my Master Sophia wanted me to be?"),
        "h4f7de021g4443g4f22g94b7g2bd8275f99ed": (1, "Thank you for being my light and my strength. I am happy you opened your heart to me and allowed me to be at your side. You're my starlight, Shadowheart."),
        "h207ba395gb926g44beg8e54gdcd644853feb": (1, "&lt;i&gt;Say nothing, and kiss her.&lt;/i&gt;"),
    }
    loca = bg3.loca_object(files.add_new_file(files.get_loca_relative_path()))
    loca.add_lines(content)


def add_obfuscate_lines_act_1() -> None:
    ab = game_assets.get_modded_dialog_asset_bundle('CAMP_GoblinHuntCelebration_SD_ROM_NightWithShadowheart')
    d = bg3.dialog_object(ab.dialog)
    t = bg3.timeline_object(ab.timeline, d)

    something_about_you_node_uuid = '101101c0-aa11-6f0e-9bed-5d1ca1de8cf5' # existing node
    tav_questions_container_node_uuid = '8d631757-453c-43bf-9a60-a15c1e2894e9'

    d.create_standard_dialog_node(
        tav_questions_container_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        d.get_children_nodes_uuids(something_about_you_node_uuid),
        None)
    d.delete_all_children_dialog_nodes(something_about_you_node_uuid)
    d.add_child_dialog_node(something_about_you_node_uuid, tav_questions_container_node_uuid)

    jump_back_node_uuid = 'ab3b2a7b-78a5-42cc-b3d2-d14d7789f9c3'
    tell_about_sophia_node_uuid = '054ffda5-5361-4388-80a6-314ec401b620'
    tell_about_jarell_node_uuid = 'c03b76f1-a828-46df-b15b-65a918b853b5'
    tell_about_fear_node_uuid = '74d141fb-41ff-4320-b8dd-2b0c965c7207'
    i_can_respect_loyalty_node_uuid = '4a78f07b-39d4-4a70-b8f3-93b4b69c165c'
    it_must_be_catastrophic_node_uuid = 'a8ebcdee-c5bb-46cb-a978-3501a98a8966'
    i_can_sympathize_node_uuid = '6850e135-18da-48f0-925b-bb4c68994731'

    index = len(d.get_children_nodes_uuids(tav_questions_container_node_uuid)) - 2
    if index < 0:
        index = 0
    d.add_child_dialog_node(tav_questions_container_node_uuid, tell_about_fear_node_uuid, index)
    d.add_child_dialog_node(tav_questions_container_node_uuid, tell_about_jarell_node_uuid, index)
    d.add_child_dialog_node(tav_questions_container_node_uuid, tell_about_sophia_node_uuid, index)

    # Tell her about Sophia who taught you everything. Recall the pain you felt when she died.
    d.create_standard_dialog_node(
        tell_about_sophia_node_uuid,
        bg3.SPEAKER_PLAYER,
        [i_can_respect_loyalty_node_uuid],
        bg3.text_content('hddc41f9ag5022g431ag831cgc37e5af1cc72', 1),
        constructor = bg3.dialog_object.QUESTION,
        show_once = True)

    # Share your memories about Jarell, about his best years as a paladin of Selune, and the darkness that swallowed him afterwards...
    d.create_standard_dialog_node(
        tell_about_jarell_node_uuid,
        bg3.SPEAKER_PLAYER,
        [it_must_be_catastrophic_node_uuid],
        bg3.text_content('hef879f48gf239g4f67g934cg234e684f2571', 1),
        constructor = bg3.dialog_object.QUESTION,
        show_once = True)

    # Take a deep breath, and tell her about your deepest fear of being someone else's puppet; tell her about your desire to be the master of your own life.
    d.create_standard_dialog_node(
        tell_about_fear_node_uuid,
        bg3.SPEAKER_PLAYER,
        [i_can_sympathize_node_uuid],
        bg3.text_content('hbadfd58fg48e6g48f1g8cd6g540840681696', 1),
        constructor = bg3.dialog_object.QUESTION,
        show_once = True)
    
    d.create_jump_dialog_node(jump_back_node_uuid, tav_questions_container_node_uuid, 2)

    # I can respect that sort of loyalty. It's not all that removed from what was instilled in me...
    d.create_standard_dialog_node(
        i_can_respect_loyalty_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [jump_back_node_uuid],
        bg3.text_content('h9f19ca8eg86d2g4e82g8ebcg9c0bd151a21f', 2))
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '5.28',
        i_can_respect_loyalty_node_uuid,
        (('5.28', '10b1eac2-98ce-4f2f-8973-efcc0b8851e4'), (None, '4aacad72-14db-414c-a9ef-6a3d993e726f')),
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 4, None), (2.98, 64, 2)),
        },
        disable_mocap = True,
        phase_duration = '5.5')
    t.create_tl_actor_node(bg3.timeline_object.LOOK_AT, bg3.SPEAKER_SHADOWHEART, '0.0', '5.5', (
        t.create_look_at_key(
            0.0,
            target = bg3.SPEAKER_PLAYER,
            bone = 'Head_M',
            turn_mode = 3,
            turn_speed_multiplier = 0.05,
            head_turn_speed_multiplier = 0.05,
            weight = 0.15,
            head_safe_zone_angle = 80,
            offset = (0.65, 0.05, 0.0),
            reset = True,
            is_eye_look_at_enabled = True,
            eye_look_at_target_id = bg3.SPEAKER_PLAYER,
            eye_look_at_bone = 'Head_M'),
    ), is_snapped_to_end = True)
    # t.create_tl_actor_node(bg3.timeline_object.LOOK_AT, bg3.SPEAKER_PLAYER, 0.0, 5.5, (
    #     t.create_look_at_key(
    #         0.0,
    #         target = bg3.SPEAKER_SHADOWHEART,
    #         bone = 'Head_M',
    #         turn_mode = 3,
    #         turn_speed_multiplier = 0.05,
    #         head_turn_speed_multiplier = 0.05,
    #         weight = 0.15,
    #         head_safe_zone_angle = 80,
    #         offset = (0.5, 0.0, 1.0),
    #         reset = True,
    #         is_eye_look_at_enabled = True,
    #         eye_look_at_target_id = bg3.SPEAKER_PLAYER,
    #         eye_look_at_bone = 'Head_M'),
    # ))
    t.create_tl_animation(
        bg3.SPEAKER_SHADOWHEART, '0.0', '5.5',
        '8b783e47-f654-1744-08f3-8a5dc27716f7',
        'e422e20b-e9cd-4bfd-8328-7d3d491c628d',
        animation_play_start_offset = 7.0,
        fade_in = 0.0,
        fade_out = 0.0,
        offset_type = 5,
        enable_root_motion = True,
        continuous = True,
        is_snapped_to_end = True)

    # I'm not entirely without sympathy, I should say. To fall out with someone you revered... it must be catastrophic.
    d.create_standard_dialog_node(
        it_must_be_catastrophic_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [jump_back_node_uuid],
        bg3.text_content('hca472913g51b9g4d7egb6ffg728620fe0440', 1))
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '9.22',
        it_must_be_catastrophic_node_uuid,
        (('9.22', '10b1eac2-98ce-4f2f-8973-efcc0b8851e4'), (None, '4aacad72-14db-414c-a9ef-6a3d993e726f')),
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 4, None), (1.0, 2048, None), (2.2, 4, None), (4.3, 16, None), (5.3, 1024, None), (7.5, 2048, None)),
        },
        phase_duration = '9.5',
        disable_mocap = True)
    t.create_tl_actor_node(bg3.timeline_object.LOOK_AT, bg3.SPEAKER_SHADOWHEART, '0.0', '9.5', (
        t.create_look_at_key(
            0.0,
            target = bg3.SPEAKER_PLAYER,
            bone = 'Head_M',
            turn_mode = 3,
            turn_speed_multiplier = 0.05,
            head_turn_speed_multiplier = 0.05,
            weight = 0.15,
            head_safe_zone_angle = 80,
            offset = (0.65, 0.05, 0.0),
            reset = True,
            is_eye_look_at_enabled = True,
            eye_look_at_target_id = bg3.SPEAKER_PLAYER,
            eye_look_at_bone = 'Head_M'),
    ), is_snapped_to_end = True)
    # t.create_tl_actor_node(bg3.timeline_object.LOOK_AT, bg3.SPEAKER_PLAYER, 0.0, 9.5, (
    #     t.create_look_at_key(
    #         0.0,
    #         target = bg3.SPEAKER_SHADOWHEART,
    #         bone = 'Head_M',
    #         turn_mode = 3,
    #         turn_speed_multiplier = 0.05,
    #         head_turn_speed_multiplier = 0.05,
    #         weight = 0.15,
    #         head_safe_zone_angle = 80,
    #         offset = (0.5, 0.0, 1.0),
    #         reset = True,
    #         is_eye_look_at_enabled = True,
    #         eye_look_at_target_id = bg3.SPEAKER_PLAYER,
    #         eye_look_at_bone = 'Head_M'),
    # ))
    t.create_tl_animation(
        bg3.SPEAKER_SHADOWHEART, '0.0', '9.5',
        '8b783e47-f654-1744-08f3-8a5dc27716f7',
        'e422e20b-e9cd-4bfd-8328-7d3d491c628d',
        animation_play_start_offset = 7.0,
        fade_in = 0.0,
        fade_out = 0.0,
        offset_type = 5,
        enable_root_motion = True,
        continuous = True)

    # I can sympathise, truly.
    d.create_standard_dialog_node(
        i_can_sympathize_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [jump_back_node_uuid],
        bg3.text_content('h6f270a53gbf03g419ag9f55ge0fee516d305', 1))
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '2.63',
        i_can_sympathize_node_uuid,
        (('2.63', '10b1eac2-98ce-4f2f-8973-efcc0b8851e4'), (None, '4aacad72-14db-414c-a9ef-6a3d993e726f')),
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.2, 64, 2), (1.9, 4, None)),
        },
        phase_duration = '3.1',
        disable_mocap = True)
    t.create_tl_actor_node(bg3.timeline_object.LOOK_AT, bg3.SPEAKER_SHADOWHEART, '0.0', '3.1', (
        t.create_look_at_key(
            0.0,
            target = bg3.SPEAKER_PLAYER,
            bone = 'Head_M',
            turn_mode = 3,
            turn_speed_multiplier = 0.05,
            head_turn_speed_multiplier = 0.05,
            weight = 0.15,
            head_safe_zone_angle = 80,
            offset = (0.65, 0.05, 0.0),
            reset = True,
            is_eye_look_at_enabled = True,
            eye_look_at_target_id = bg3.SPEAKER_PLAYER,
            eye_look_at_bone = 'Head_M'),
    ), is_snapped_to_end = True)
    # t.create_tl_actor_node(bg3.timeline_object.LOOK_AT, bg3.SPEAKER_PLAYER, 0.0, 3.1, (
    #     t.create_look_at_key(
    #         0.0,
    #         target = bg3.SPEAKER_SHADOWHEART,
    #         bone = 'Head_M',
    #         turn_mode = 3,
    #         turn_speed_multiplier = 0.05,
    #         head_turn_speed_multiplier = 0.05,
    #         weight = 0.15,
    #         head_safe_zone_angle = 80,
    #         offset = (0.5, 0.0, 1.0),
    #         reset = True,
    #         is_eye_look_at_enabled = True,
    #         eye_look_at_target_id = bg3.SPEAKER_PLAYER,
    #         eye_look_at_bone = 'Head_M'),
    # ))
    t.create_tl_animation(
        bg3.SPEAKER_SHADOWHEART, '0.0', '3.1',
        '8b783e47-f654-1744-08f3-8a5dc27716f7',
        'e422e20b-e9cd-4bfd-8328-7d3d491c628d',
        animation_play_start_offset = 7.0,
        fade_in = 0.0,
        fade_out = 0.0,
        offset_type = 5,
        enable_root_motion = True,
        continuous = True,
        is_snapped_to_end = True)


def add_obfuscate_lines_act_3() -> None:
    # h41e16b9cg1017g419bga093ge2ec19add985": (1, "Do you think all that I did was my own free will... that I am not a puppet of any master anymore?"
    # "hc71b8f5bg8cc5g457aga817gc180cef540d0#2": "Not just that - you did what no one else was capable of. Thank you.<br>"

    ab = game_assets.get_modded_dialog_asset_bundle('ShadowHeart_InParty2_Nested_DefaultChapter')
    d = bg3.dialog_object(ab.dialog)
    t = bg3.timeline_object(ab.timeline, d)

    slot_idx_shadowheart = d.get_speaker_slot_index(bg3.SPEAKER_SHADOWHEART)
    slot_idx_tav = d.get_speaker_slot_index(bg3.SPEAKER_PLAYER)

    of_course_node_uuid = '23749c85-4289-4965-a7db-1909f5cb63a2' # existing node

    my_own_free_will_selune_saved_node_uuid = '0bce2f35-f000-4aa4-b715-917b3809a8e9'
    my_own_free_will_selune_killed_node_uuid = 'eeec3a97-8d57-4403-99de-08ec3ecb675b'
    my_own_free_will_shar_saved_node_uuid = 'e437342c-3ba7-485e-ba5a-da73f8313f03'
    not_just_that_node_uuid = '201d626f-9fe9-463a-9adf-5cc71f91a6de'
    youre_my_starlight_node_uuid = '2cd267b2-fd2c-4961-9d1a-242a9cbc4d31'
    say_nothing_node_uuid = '075a85db-4610-4433-ac6e-9f0953e1d4c5'
    kiss_her_node_uuid = '8067d989-e249-4c6d-8a0c-3f5d490c46eb'
    come_here_node_uuid = 'afef2ff1-4bff-4825-bf00-b5537e5f5f33'
    nested_kiss_node_uuid = '351729d6-0060-471e-822b-8bb01240750d'
    jump_back_node_uuid = 'e0f2f5c2-082a-48bf-979c-64e5f2f19fd8'

    d.create_jump_dialog_node(jump_back_node_uuid, of_course_node_uuid, 2)
    d.add_child_dialog_node(of_course_node_uuid, my_own_free_will_selune_saved_node_uuid, 0)
    d.add_child_dialog_node(of_course_node_uuid, my_own_free_will_selune_killed_node_uuid, 0)
    d.add_child_dialog_node(of_course_node_uuid, my_own_free_will_shar_saved_node_uuid, 0)

    # Do you think all that I did was my own free will... that I am not a puppet of any master anymore?
    d.create_standard_dialog_node(
        my_own_free_will_selune_saved_node_uuid,
        bg3.SPEAKER_PLAYER,
        [not_just_that_node_uuid],
        bg3.text_content('h41e16b9cg1017g419bga093ge2ec19add985', 1),
        checkflags = (
            bg3.flag_group('Global', (
                bg3.flag(bg3.FLAG_ORI_Shadowheart_State_RejectShar_SavedParents, True, None),
                bg3.flag(bg3.FLAG_ORI_Shadowheart_State_RejectShar_KilledParents, False, None),
                bg3.flag(bg3.FLAG_ORI_Shadowheart_State_Shar_SavedParents, False, None),
            )),
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_State_PartneredWithShadowheart, True, slot_idx_tav),
            ))
        ),
        constructor = bg3.dialog_object.QUESTION,
        show_once = True)

    d.create_alias_dialog_node(
        my_own_free_will_selune_killed_node_uuid,
        my_own_free_will_selune_saved_node_uuid,
        [not_just_that_node_uuid],
        checkflags = (
            bg3.flag_group('Global', (
                bg3.flag(bg3.FLAG_ORI_Shadowheart_State_RejectShar_SavedParents, False, None),
                bg3.flag(bg3.FLAG_ORI_Shadowheart_State_RejectShar_KilledParents, True, None),
                bg3.flag(bg3.FLAG_ORI_Shadowheart_State_Shar_SavedParents, False, None),
            )),
        ),
        show_once = True)
    d.create_alias_dialog_node(
        my_own_free_will_shar_saved_node_uuid,
        my_own_free_will_selune_saved_node_uuid,
        [not_just_that_node_uuid],
        checkflags = (
            bg3.flag_group('Global', (
                bg3.flag(bg3.FLAG_ORI_Shadowheart_State_RejectShar_SavedParents, False, None),
                bg3.flag(bg3.FLAG_ORI_Shadowheart_State_RejectShar_KilledParents, False, None),
                bg3.flag(bg3.FLAG_ORI_Shadowheart_State_Shar_SavedParents, True, None),
            )),
        ),
        show_once = True)

    # Not just that - you did what no one else was capable of. Thank you.
    d.create_standard_dialog_node(
        not_just_that_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [youre_my_starlight_node_uuid, say_nothing_node_uuid],
        bg3.text_content('hc71b8f5bg8cc5g457aga817gc180cef540d0', 2))
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '6.73',
        not_just_that_node_uuid,
        (('6.73', '7b067edd-f53f-49e1-95bc-0986e6e2ca2f'), (None, 'e08db860-1e62-4271-bf4e-d51602468573')),
        phase_duration = '7.1',
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 4, None), (2.5, 2, None), (5.7, 2, 1), (6.5, 2, None)),
            bg3.SPEAKER_PLAYER: ((0.0, 2, None),),
        })

    # Thank you for being my light and my strength. I am happy you opened your heart to me and allowed me to be at your side. You're my starlight, Shadowheart.
    d.create_standard_dialog_node(
        youre_my_starlight_node_uuid,
        bg3.SPEAKER_PLAYER,
        [come_here_node_uuid],
        bg3.text_content('h4f7de021g4443g4f22g94b7g2bd8275f99ed', 1),
        constructor = bg3.dialog_object.QUESTION)

    # Say nothing, and kiss her.
    d.create_standard_dialog_node(
        say_nothing_node_uuid,
        bg3.SPEAKER_PLAYER,
        [kiss_her_node_uuid],
        bg3.text_content('h207ba395gb926g44beg8e54gdcd644853feb', 1),
        constructor = bg3.dialog_object.QUESTION)

    plus_5_approval = bg3.reaction_object.create_new(game_assets.files, {bg3.SPEAKER_SHADOWHEART: 5})
    d.create_standard_dialog_node(
        come_here_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [kiss_her_node_uuid],
        bg3.text_content('h2c35be55g4742g47abgbdccg534dfa831e3e', 1),
        approval_rating_uuid = plus_5_approval.uuid)
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '0.842',
        come_here_node_uuid,
        ((None, 'd76eaab3-040b-4871-9c1d-4a8624f37cd2'),),
        fade_in = 0.0,
        fade_out = 0.0,
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 2, None),),
            bg3.SPEAKER_PLAYER: ((0.0, 2, None), ),
        })

    d.create_standard_dialog_node(
        kiss_her_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [nested_kiss_node_uuid],
        None,
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(ORI_ShadowheartKiss_VersionA.uuid, False, slot_idx_shadowheart),
            )),
            bg3.flag_group('Object', (
                bg3.flag(ORI_ShadowheartKiss_VersionB.uuid, False, slot_idx_shadowheart),
            )),
            bg3.flag_group('Object', (
                bg3.flag(ORI_ShadowheartKiss_VersionC.uuid, True, slot_idx_shadowheart),
            )),
            bg3.flag_group('Object', (
                bg3.flag(ORI_ShadowheartKiss_VersionD.uuid, False, slot_idx_shadowheart),
            )),
            bg3.flag_group('Object', (
                bg3.flag(ORI_ShadowheartKiss_VersionE.uuid, False, slot_idx_shadowheart),
            )),
            bg3.flag_group('Object', (
                bg3.flag(ORI_ShadowheartKiss_VersionF.uuid, False, slot_idx_shadowheart),
            )),
            bg3.flag_group('Object', (
                bg3.flag(ORI_ShadowheartKiss_LoveYou.uuid, False, slot_idx_shadowheart),
            )),
        ))

    kiss_nested_dialog_uuid = get_dialog_uuid('ShadowHeart_InParty2_Nested_ShadowheartKiss')
    d.create_nested_dialog_node(
        nested_kiss_node_uuid,
        kiss_nested_dialog_uuid,
        [jump_back_node_uuid],
        speaker_count = 7)
    add_dialog_dependency(ab, kiss_nested_dialog_uuid)


bg3.add_build_procedure('add_obfuscate_lines_act_1', add_obfuscate_lines_act_1, 'obfuscate')
bg3.add_build_procedure('add_obfuscate_lines_act_3', add_obfuscate_lines_act_3, 'obfuscate')
bg3.add_build_procedure('create_obfuscate_text_content', create_obfuscate_text_content, 'obfuscate')
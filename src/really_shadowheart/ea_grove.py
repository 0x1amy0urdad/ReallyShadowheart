from __future__ import annotations

import bg3moddinglib as bg3

from .context import game_assets
from .flags import *

def create_reaction_to_sazza() -> None:

    #################################################################################################
    # DEN_CapturedGoblin_GuardsAvenge
    #################################################################################################

    ab = game_assets.get_modded_dialog_asset_bundle('DEN_CapturedGoblin_GuardsAvenge')
    d = bg3.dialog_object(ab.dialog)

    speaker_idx_tav = d.get_speaker_slot_index(bg3.SPEAKER_PLAYER)

    d.add_dialog_flags('051fceb8-b9c1-4b0a-1bed-f82d0d74f565', setflags = (
        bg3.flag_group('Object', (
            bg3.flag(Reflection_Event_Sazza.uuid, True, speaker_idx_tav),
            bg3.flag(Reflection_Available_Sazza.uuid, True, speaker_idx_tav),
        )),
    ))

    #################################################################################################
    # Dialog: DEN_CapturedGoblin.lsf
    #################################################################################################

    ab = game_assets.get_modded_dialog_asset_bundle('DEN_CapturedGoblin')
    d = bg3.dialog_object(ab.dialog)

    speaker_idx_tav = d.get_speaker_slot_index(bg3.SPEAKER_PLAYER)

    promised_help_nodes = [
        '59ab03d8-98af-7faa-f921-0f08a80ce7bc',
        '5e19808d-dca3-1594-ec5f-376630cfddb3',
        '30788c83-098a-9906-81ab-01545269f18e',
        'e6730fd2-75c4-61b0-7b6f-1515dfd0d8d2',
    ]

    for node in promised_help_nodes:
        d.add_dialog_flags(node, setflags = (
            bg3.flag_group('Object', (
                bg3.flag(Reflection_Event_Sazza.uuid, True, speaker_idx_tav),
                bg3.flag(Reflection_Available_Sazza.uuid, True, speaker_idx_tav),
                bg3.flag(Tav_Promised_Help_Sazza.uuid, True, speaker_idx_tav),
            )),
        ))

    #################################################################################################
    # Dialog: ShadowHeart_InParty2.lsf
    #################################################################################################

    ab = game_assets.get_modded_dialog_asset_bundle('ShadowHeart_InParty')
    d = bg3.dialog_object(ab.dialog)

    speaker_idx_tav = d.get_speaker_slot_index(bg3.SPEAKER_PLAYER)

    topical_greetings_node_uuid = 'dfec2c3c-2397-ff26-ef9e-09ad12d81b9f' # existing root node

    saving_sazza_reflection_node_uuid = 'd5d4621a-4111-4714-a34c-03dcc26759a3'

    # reused node from putrid bog reflection
    nested_dialog_node_uuid = 'e2e11f4c-de6a-41af-9d83-623c2abdbdac'

    d.create_standard_dialog_node(
        saving_sazza_reflection_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [nested_dialog_node_uuid],
        None,
        checkflags = (
            bg3.flag_group('Global', (
                bg3.flag(ReallyShadowheart_Ext_V2_0_0_0.uuid, True, None),
            )),
            bg3.flag_group('Object', (
                bg3.flag(Reflection_Event_Sazza.uuid, True, speaker_idx_tav),
            )),
        ),
        constructor = bg3.dialog_object.GREETING,
        root = True)
    d.add_root_node_before(topical_greetings_node_uuid, saving_sazza_reflection_node_uuid)


    #################################################################################################
    # Dialog: ShadowHeart_InParty2_Nested_DefaultChapter.lsf
    #################################################################################################

    ab = game_assets.get_modded_dialog_asset_bundle('ShadowHeart_InParty2_Nested_DefaultChapter')
    d = bg3.dialog_object(ab.dialog)
    t = bg3.timeline_object(ab.timeline, d)

    speaker_idx_tav = d.get_speaker_slot_index(bg3.SPEAKER_PLAYER)

    sazza_reflection_greeting_root_node_uuid = '3fd2753d-ce7f-44b4-972f-901a3bc5cee4'
    do_you_think_helpin_goblin_good_idea_node_uuid = '189c0d7e-6e12-4323-ba0e-fdd47febb02c'

    im_not_in_the_habit_of_helping_vermin_node_uuid = 'b680ea50-c760-48e1-9b77-cd55ea888060'
    this_could_very_well_end_badly_node_uuid = 'c20642fd-6064-4d98-a49b-40ea4be1354d'
    and_yet_you_still_helped_it_escape_node_uuid = '7a0804e4-b3a5-4435-82c0-65ea19be9f50'
    sazza_remembers_what_we_did_node_uuid = '0f16e5aa-3929-4e4b-8b24-83494d83d1d4'
    if_youre_going_to_let_our_fates_depend_on_hope_node_uuid = '4be2a132-bb0f-40c6-8f08-f3acea600619'

    shooting_caged_prisoners_node_uuid = '84e58da6-ac8e-41fc-9748-bf7af4e8e04b'
    winning_display_of_archery_node_uuid = 'e57cb2b1-bb3a-43f5-8d37-49505156c4ef'
    good_riddance_node_uuid = '839f6cdb-ac8f-452b-a4fc-ca6eabe2b32a'
    come_on_node_uuid = '12797b27-bb3b-4afb-927b-26c8d0c9553b'
    didnt_feel_right_node_uuid = '2d27de4a-69ba-4255-b48a-d313c04a937a'
    dont_mourn_vermin_node_uuid = 'bd002db0-d9ec-4879-a09b-61eb188a1aa2'

    seek_help_from_a_goblin_healer_node_uuid = '4b235e1f-8398-4146-977f-cef61cd9a629'
    we_cant_afford_to_ignore_any_options_node_uuid = '9a8a7961-d5c2-4c4b-a8b2-b18dd34aadd9'
    youre_right_node_uuid = '242ce9fa-e54c-490e-949d-ba36cf23f2ba'
    gut_creature_stole_something_node_uuid = '765fed0e-47a2-49be-9239-8a9ff513e8e2'
    sounds_risky_node_uuid = 'be60d6d4-8b92-4deb-9fae-a258613096f5'
    well_need_to_take_some_risks_node_uuid = '838208e8-d09d-4543-861d-82dcabcd5fe7'

    d.add_child_dialog_node(bg3.SHADOWHEART_THOUGHTS_QUESTION_BANK_NODE_UUID, seek_help_from_a_goblin_healer_node_uuid, 0)
    d.add_child_dialog_node(bg3.SHADOWHEART_THOUGHTS_QUESTION_BANK_NODE_UUID, shooting_caged_prisoners_node_uuid, 0)
    d.add_child_dialog_node(bg3.SHADOWHEART_THOUGHTS_QUESTION_BANK_NODE_UUID, do_you_think_helpin_goblin_good_idea_node_uuid, 0)

    reaction_minus_3 = bg3.reaction_object.create_new(game_assets.files, { bg3.SPEAKER_SHADOWHEART: -3 }, uuid = '32c525be-9709-4df2-8c91-4b30bd30c8f2')
    reaction_minus_1 = bg3.reaction_object.create_new(game_assets.files, { bg3.SPEAKER_SHADOWHEART: -1 }, uuid = 'd3fae4be-5d14-437d-bdb0-fb558a3604a8')
    reaction_plus_1 = bg3.reaction_object.create_new(game_assets.files, { bg3.SPEAKER_SHADOWHEART: 1 }, uuid = '12595958-e020-4927-8059-c27f3f9e0319')

    d.create_standard_dialog_node(
        sazza_reflection_greeting_root_node_uuid,
        bg3.SPEAKER_PLAYER,
        [im_not_in_the_habit_of_helping_vermin_node_uuid, winning_display_of_archery_node_uuid],
        None,
        checkflags = (
            bg3.flag_group('Global', (
                bg3.flag(ReallyShadowheart_Ext_V2_0_0_0.uuid, True, None),
            )),
            bg3.flag_group('Object', (
                bg3.flag(Reflection_Event_Sazza.uuid, True, speaker_idx_tav),
            )),
        ),
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(Reflection_Event_Sazza.uuid, False, speaker_idx_tav),
            )),
        ),
        root = True,
        constructor = bg3.dialog_object.GREETING)
    d.add_root_node(sazza_reflection_greeting_root_node_uuid, 0)

    # Saving Sazza

    # Do you think helping that goblin was a good idea?
    d.create_standard_dialog_node(
        do_you_think_helpin_goblin_good_idea_node_uuid,
        bg3.SPEAKER_PLAYER,
        [im_not_in_the_habit_of_helping_vermin_node_uuid],
        bg3.text_content('hfe0694dbg0061g4175gb808g7dd1e6216e92', 1),
        constructor = bg3.dialog_object.QUESTION,
        checkflags = (
            bg3.flag_group(bg3.flag_group.OBJECT, (
                bg3.flag(Reflection_Available_Sazza.uuid, True, speaker_idx_tav),
                bg3.flag(Tav_Promised_Help_Sazza.uuid, True, speaker_idx_tav),
            )),
            bg3.flag_group(bg3.flag_group.GLOBAL, (
                bg3.flag(ReallyShadowheart_Ext_V2_0_0_0.uuid, True, None),
                bg3.flag(bg3.FLAG_GOB_Orpheus_State_HadVoiceOfAbsoluteEvent, False, None),
            )),
        ))

    # I'm not in the habit of helping vermin. I expect it to return and bite.
    d.create_standard_dialog_node(
        im_not_in_the_habit_of_helping_vermin_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [
            this_could_very_well_end_badly_node_uuid,
            sazza_remembers_what_we_did_node_uuid,
        ],
        bg3.text_content('h0e2f4915g5089g422dg9f54g6970c718af3a', 1),
        constructor = bg3.dialog_object.ANSWER,
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(Tav_Promised_Help_Sazza.uuid, True, speaker_idx_tav),
            )),
        ))
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '4.63',
        im_not_in_the_habit_of_helping_vermin_node_uuid,
        (('4.63', '7b067edd-f53f-49e1-95bc-0986e6e2ca2f'), (None, 'e08db860-1e62-4271-bf4e-d51602468573')),
        phase_duration = '5.0',
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 16, None), (1.84, 4, None), (2.74, 128, 1),)
        },
        attitudes = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_R_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, None),),
            bg3.SPEAKER_PLAYER: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_L_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, None),),
        })

    # This could very well end badly.
    d.create_standard_dialog_node(
        this_could_very_well_end_badly_node_uuid,
        bg3.SPEAKER_PLAYER,
        [and_yet_you_still_helped_it_escape_node_uuid],
        bg3.text_content('h8e40d0e4g5682g4becg9b95ga8ed381c9e67', 1),
        constructor = bg3.dialog_object.QUESTION)

    # And yet you still helped it escape. That grimy little creature had better be grateful.
    d.create_standard_dialog_node(
        and_yet_you_still_helped_it_escape_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [],
        bg3.text_content('h9346cf34g96cdg4d26ga327gfe3474d6dc61', 1),
        constructor = bg3.dialog_object.ANSWER,
        end_node = True)
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '5.37',
        and_yet_you_still_helped_it_escape_node_uuid,
        (('5.4', 'e7f21f15-f386-40f4-bb0f-2f9f42249ad1'), (None, 'e08db860-1e62-4271-bf4e-d51602468573')),
        phase_duration = '5.8',
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 4, 2), (2.69, 8, None),)
        },
        attitudes = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_R_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, None),),
            bg3.SPEAKER_PLAYER: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_L_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, None),),
        })

    # Let's just hope Sazza remembers what we did for her.
    d.create_standard_dialog_node(
        sazza_remembers_what_we_did_node_uuid,
        bg3.SPEAKER_PLAYER,
        [if_youre_going_to_let_our_fates_depend_on_hope_node_uuid],
        bg3.text_content('hd5ab5d0ageff6g4d15g9fd1ge2b89983638b', 1),
        approval_rating_uuid = reaction_minus_3.uuid,
        constructor = bg3.dialog_object.QUESTION)

    # If you are going to let our fates depend on hope, I might need to reconsider our alliance.
    d.create_standard_dialog_node(
        if_youre_going_to_let_our_fates_depend_on_hope_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [],
        bg3.text_content('h88e88827gffb4g454aga0b5g8540c1dc16de', 1),
        constructor = bg3.dialog_object.ANSWER,
        end_node = True)
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '6.22',
        if_youre_going_to_let_our_fates_depend_on_hope_node_uuid,
        (('6.3', 'e7f21f15-f386-40f4-bb0f-2f9f42249ad1'), (None, 'e08db860-1e62-4271-bf4e-d51602468573')),
        phase_duration = '6.7',
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 4, 1), (3.31, 8, None),)
        },
        attitudes = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_R_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, None),),
            bg3.SPEAKER_PLAYER: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_L_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, None),),
        })

    # Sazza was shot
    
    # Tieflings are not above shooting caged prisoners. Good to know.
    d.create_standard_dialog_node(
        shooting_caged_prisoners_node_uuid,
        bg3.SPEAKER_PLAYER,
        [winning_display_of_archery_node_uuid],
        bg3.text_content('hd128b7ffg3b6cg4d62ga6e5g3ce3e56b74d8', 1),
        constructor = bg3.dialog_object.QUESTION,
        checkflags = (
            bg3.flag_group(bg3.flag_group.OBJECT, (
                bg3.flag(Reflection_Available_Sazza.uuid, True, speaker_idx_tav),
            )),
            bg3.flag_group(bg3.flag_group.GLOBAL, (
                bg3.flag(bg3.FLAG_DEN_CapturedGoblin_State_PlayerWatchedGoblinExecution, True, None),
                bg3.flag(ReallyShadowheart_Ext_V2_0_0_0.uuid, True, None),
                bg3.flag(bg3.FLAG_GOB_Orpheus_State_HadVoiceOfAbsoluteEvent, False, None),
            )),
        ))

    # Hardly a winning display of archery, but it did the job.
    d.create_standard_dialog_node(
        winning_display_of_archery_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [good_riddance_node_uuid, didnt_feel_right_node_uuid],
        bg3.text_content('h4bef1930gfbb0g4788g8ac7ge04d4cfce547', 1),
        checkflags = (
            bg3.flag_group(bg3.flag_group.GLOBAL, (
                bg3.flag(bg3.FLAG_DEN_CapturedGoblin_State_PlayerWatchedGoblinExecution, True, None),
            )),
        ),
        constructor = bg3.dialog_object.ANSWER)
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '3.63',
        winning_display_of_archery_node_uuid,
        (('3.63', '7b067edd-f53f-49e1-95bc-0986e6e2ca2f'), (None, 'e08db860-1e62-4271-bf4e-d51602468573')),
        phase_duration = '4.0',
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 4, 1), (2.41, 1, None), (3.15, 4, None))
        },
        attitudes = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_R_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, None),),
            bg3.SPEAKER_PLAYER: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_L_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, None),),
        })

    # Good riddance.
    d.create_standard_dialog_node(
        good_riddance_node_uuid,
        bg3.SPEAKER_PLAYER,
        [come_on_node_uuid],
        bg3.text_content('h1f2acbeagf732g4949gb6edgfc1b26afa0a5', 1),
        constructor = bg3.dialog_object.QUESTION)

    # That's the best end any goblin can expect. Come on.
    d.create_standard_dialog_node(
        come_on_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [],
        bg3.text_content('hff5ccb73g7abbg4ebagbbf7gcadf1ce59ad8', 1),
        constructor = bg3.dialog_object.ANSWER,
        end_node = True)
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '4.01',
        come_on_node_uuid,
        (('4.1', 'e7f21f15-f386-40f4-bb0f-2f9f42249ad1'), (None, 'e08db860-1e62-4271-bf4e-d51602468573')),
        phase_duration = '4.4',
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 4, None), (1.36, 8, None), (2.91, 1, None))
        },
        attitudes = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_R_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, None),),
            bg3.SPEAKER_PLAYER: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_L_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, None),),
        })

    # Letting her die like that didn't feel right.
    d.create_standard_dialog_node(
        didnt_feel_right_node_uuid,
        bg3.SPEAKER_PLAYER,
        [dont_mourn_vermin_node_uuid],
        bg3.text_content('h5cf6685agca2bg46a7gb37cg20057becaebc', 1),
        constructor = bg3.dialog_object.QUESTION)

    # Goblins live fast, die bloody and drag others to the grave with them. Don't mourn vermin.
    d.create_standard_dialog_node(
        dont_mourn_vermin_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [],
        bg3.text_content('ha453e1e4g722ag4698gacc6g61d0bf4209d1', 1),
        constructor = bg3.dialog_object.ANSWER,
        approval_rating_uuid = reaction_plus_1.uuid,
        end_node = True)
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '6.39',
        dont_mourn_vermin_node_uuid,
        (('6.4', 'e7f21f15-f386-40f4-bb0f-2f9f42249ad1'), (None, 'e08db860-1e62-4271-bf4e-d51602468573')),
        phase_duration = '6.7',
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 4, None), (1.46, 8, None), (2.26, 2048, None), (3.48, 8, 1))
        },
        attitudes = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_R_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, None),),
            bg3.SPEAKER_PLAYER: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_L_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, None),),
        })

    # Gut goblin healer

    # I can't believe we're going to seek help from a goblin healer.
    d.create_standard_dialog_node(
        seek_help_from_a_goblin_healer_node_uuid,
        bg3.SPEAKER_PLAYER,
        [we_cant_afford_to_ignore_any_options_node_uuid],
        bg3.text_content('hbf96955egebb7g46edgb7b2g5b84f10db31a', 1),
        constructor = bg3.dialog_object.QUESTION,
        checkflags = (
            bg3.flag_group(bg3.flag_group.GLOBAL, (
                bg3.flag(bg3.FLAG_DEN_CapturedGoblin_Knows_Priestess, True, None),
                bg3.flag(ReallyShadowheart_Ext_V2_0_0_0.uuid, True, None),
                bg3.flag(bg3.FLAG_GOB_Orpheus_State_HadVoiceOfAbsoluteEvent, False, None),
            )),
        ))

    # Goblins aren't exactly renowned healers, but we can't afford to ignore any options.
    d.create_standard_dialog_node(
        we_cant_afford_to_ignore_any_options_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [youre_right_node_uuid, sounds_risky_node_uuid],
        bg3.text_content('hbef39624gc5dfg437egab2dg0071f327c9c2', 1),
        checkflags = (
            bg3.flag_group(bg3.flag_group.GLOBAL, (
                bg3.flag(bg3.FLAG_DEN_CapturedGoblin_State_PlayerWatchedGoblinExecution, False, None),
            )),
        ),
        constructor = bg3.dialog_object.ANSWER)
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '6.11',
        we_cant_afford_to_ignore_any_options_node_uuid,
        (('6.11', '7b067edd-f53f-49e1-95bc-0986e6e2ca2f'), (None, 'e08db860-1e62-4271-bf4e-d51602468573')),
        phase_duration = '6.4',
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 4, None), (3.85, 4, 1),)
        },
        attitudes = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_R_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, None),),
            bg3.SPEAKER_PLAYER: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_L_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, None),),
        })

    # You're right. We have to investigate all leads, no matter how unsavoury.
    d.create_standard_dialog_node(
        youre_right_node_uuid,
        bg3.SPEAKER_PLAYER,
        [gut_creature_stole_something_node_uuid],
        bg3.text_content('h03da7606g9062g4298ga35fgcbff2e1896f5', 1),
        constructor = bg3.dialog_object.QUESTION)

    # Perhaps this Gut creature stole something that could be useful. A scroll, a potion, a cranial extractor.
    d.create_standard_dialog_node(
        gut_creature_stole_something_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [],
        bg3.text_content('h5635d1dcgc5d5g448agb628gc055e30f3e2f', 1),
        constructor = bg3.dialog_object.ANSWER,
        end_node = True)
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '8.09',
        gut_creature_stole_something_node_uuid,
        (('8.0', 'e7f21f15-f386-40f4-bb0f-2f9f42249ad1'), (None, 'e08db860-1e62-4271-bf4e-d51602468573')),
        phase_duration = '8.09',
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 4, 2), (1.1, 4, 1), (1.97, 16, None), (2.86, 4, 1), (4.0, 16, None), (5.3, 4, None), (6.81, 2, 1))
        },
        attitudes = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_R_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, None),),
            bg3.SPEAKER_PLAYER: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_L_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, None),),
        })

    # Venturing into a goblin camp? Sounds risky, to put it mildly.
    d.create_standard_dialog_node(
        sounds_risky_node_uuid,
        bg3.SPEAKER_PLAYER,
        [well_need_to_take_some_risks_node_uuid],
        bg3.text_content('ha0d49ec1gbbaag4a7bga816gf133eaaae6b0', 1),
        approval_rating_uuid = reaction_minus_1.uuid,
        constructor = bg3.dialog_object.QUESTION)

    # We'll need to take some risks if we want to cure ourselves. Come on.
    d.create_standard_dialog_node(
        well_need_to_take_some_risks_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [],
        bg3.text_content('h8e3e63a6g50ffg4b8bgb124g4b9a2c18731d', 1),
        constructor = bg3.dialog_object.ANSWER,
        end_node = True)
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '3.92',
        well_need_to_take_some_risks_node_uuid,
        (('3.95', 'e7f21f15-f386-40f4-bb0f-2f9f42249ad1'), (None, 'e08db860-1e62-4271-bf4e-d51602468573')),
        phase_duration = '4.1',
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 4, None), (3.32, 1, None))
        },
        attitudes = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_R_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, None),),
            bg3.SPEAKER_PLAYER: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_L_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, None),),
        })


def create_reaction_arabella_death() -> None:
    #################################################################################################
    # DEN_ShadowDruid_SnakesCourt
    #################################################################################################

    ab = game_assets.get_modded_dialog_asset_bundle('DEN_ShadowDruid_SnakesCourt')
    d = bg3.dialog_object(ab.dialog)

    speaker_idx_tav = d.get_speaker_slot_index(bg3.SPEAKER_PLAYER)

    arabella_death_node_uuid = 'adfdfb63-2be6-09da-83e4-3a053f7cd15b'

    arabella_freed_approval_uuid = '6a5bbc5f-fd8b-45cb-ba9d-339e10c94773'

    d.set_approval_rating('87ea6c04-1804-bfcd-24b4-f8b750c0f1ec', arabella_freed_approval_uuid)
    d.set_approval_rating('30bd0321-120c-c700-e8b2-5ab9769649da', arabella_freed_approval_uuid)
    d.set_approval_rating('35a2a015-55e9-eeed-8117-adc1f4ec3274', arabella_freed_approval_uuid)
    d.set_approval_rating('807d76a6-d832-5e15-e323-175314ca5d50', arabella_freed_approval_uuid)
    d.set_approval_rating('89e12728-f29f-906c-e215-5777f8723e32', arabella_freed_approval_uuid)
    d.set_approval_rating('afd2dcc0-b863-d69b-ea46-5a6853960fca', arabella_freed_approval_uuid)

    d.add_dialog_flags(arabella_death_node_uuid, setflags = (
        bg3.flag_group('Object', (
            bg3.flag(Reflection_Event_Arabella_Death.uuid, True, speaker_idx_tav),
            bg3.flag(Reflection_Available_Arabella_Death.uuid, True, speaker_idx_tav),
        )),
    ))

    #################################################################################################
    # Dialog: ShadowHeart_InParty2.lsf
    #################################################################################################

    ab = game_assets.get_modded_dialog_asset_bundle('ShadowHeart_InParty')
    d = bg3.dialog_object(ab.dialog)

    speaker_idx_tav = d.get_speaker_slot_index(bg3.SPEAKER_PLAYER)

    topical_greetings_node_uuid = 'dfec2c3c-2397-ff26-ef9e-09ad12d81b9f' # existing root node

    arabella_death_reflection_node_uuid = '9c841ff1-797e-4341-ae62-b0e6e7e10d4a'

    # reused node from putrid bog reflection
    nested_dialog_node_uuid = 'e2e11f4c-de6a-41af-9d83-623c2abdbdac'

    d.create_standard_dialog_node(
        arabella_death_reflection_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [nested_dialog_node_uuid],
        None,
        checkflags = (
            bg3.flag_group('Global', (
                bg3.flag(ReallyShadowheart_Ext_V2_0_0_0.uuid, True, None),
            )),
            bg3.flag_group('Object', (
                bg3.flag(Reflection_Event_Arabella_Death.uuid, True, speaker_idx_tav),
            )),
        ),
        constructor = bg3.dialog_object.GREETING,
        root = True)
    d.add_root_node_before(topical_greetings_node_uuid, arabella_death_reflection_node_uuid)

    #################################################################################################
    # Dialog: ShadowHeart_InParty2_Nested_DefaultChapter.lsf
    #################################################################################################

    ab = game_assets.get_modded_dialog_asset_bundle('ShadowHeart_InParty2_Nested_DefaultChapter')
    d = bg3.dialog_object(ab.dialog)
    t = bg3.timeline_object(ab.timeline, d)

    speaker_idx_tav = d.get_speaker_slot_index(bg3.SPEAKER_PLAYER)

    reaction_minus_1 = bg3.reaction_object.create_new(game_assets.files, { bg3.SPEAKER_SHADOWHEART: -1 }, uuid = '23b20348-5c90-4223-b67e-61f713eddbd7')
    reaction_plus_1 = bg3.reaction_object.create_new(game_assets.files, { bg3.SPEAKER_SHADOWHEART: 1 }, uuid = '52ec5b57-14c1-4a8e-b0bf-360d793c6210')

    druid_this_harsh_node_uuid = 'd0d815f3-8ba3-4c6e-9237-a77d3178430e'
    arabella_death_reflection_greeting_root_node_uuid = '58be4a78-e8f4-4ab1-98eb-6dbd2c53027d'

    lets_find_that_healer_node_uuid = '379f53ed-9e21-4fc1-bfb4-57672159ea02'
    lets_get_in_and_out_of_this_place_node_uuid = 'ddc97103-1f41-4ba7-bb21-e9bd9203ac0d'
    jump_lets_find_that_healer_node_uuid = '4ddfb0f5-0efe-4590-b8aa-379e1c717c3f'

    im_not_dealing_with_child_killers_healer_node_uuid = 'e6e1ce75-9b21-4ac8-b054-463005a1100c'
    im_not_dealing_with_child_killers_node_uuid = '35829aa0-3a5e-4eae-848f-809e06e6a09d'
    principles_wont_save_us_node_uuid = '4dc3c763-5bb3-4cdb-8c5f-d164f7fa75a9'

    but_you_held_back_node_uuid = '5c68a323-a005-4f81-a7cc-4be5c035d610'
    i_didnt_know_that_was_going_to_happen_node_uuid = '5f8b06d3-c22c-4840-b173-564d0f3bc060'

    im_surprised_you_care_node_uuid = '7e6d9a5c-f4e4-4183-867b-4f8b6041f496'
    do_you_truly_think_im_that_callous_node_uuid = '14e31d99-cb65-4fc3-b090-4c87e0fb2905'

    she_tried_to_steal_node_uuid = 'd53c03e7-3085-4133-9e58-15cc23de865d'
    quite_a_price_node_uuid = '931c71e9-8836-4449-a798-b259c986fa7b'

    we_shouldve_done_something_node_uuid = '0589b60f-c0d9-47ce-8e7f-29bff51e883c'
    maybe_shed_still_be_dead_node_uuid = '4c20f0ec-99f6-416a-885c-a880df989aa7'
    we_cant_help_everyone_node_uuid = 'a80f8d13-c0dd-4811-b2ab-45602b994e98'

    what_will_her_parents_say_node_uuid = '6d6c8096-c085-4f81-b2f1-63b783c4322c'
    i_said_we_shouldnt_get_involved_node_uuid = '525a51f9-d37c-4420-9c92-99a7095674df'
    perhaps_we_shouldnt_have_node_uuid = 'fb129e7d-73c6-4364-884f-b04610f745b1'

    i_shouldve_just_attacked_node_uuid = 'bed67b73-186b-451a-8cc4-d121cc078319'
    then_wed_have_had_a_fight_node_uuid = 'c04104d4-5fe4-4cf8-babe-8f3df446db26'

    d.create_standard_dialog_node(
        arabella_death_reflection_greeting_root_node_uuid,
        bg3.SPEAKER_PLAYER,
        [lets_find_that_healer_node_uuid, lets_get_in_and_out_of_this_place_node_uuid],
        None,
        checkflags = (
            bg3.flag_group('Global', (
                bg3.flag(ReallyShadowheart_Ext_V2_0_0_0.uuid, True, None),
            )),
            bg3.flag_group('Object', (
                bg3.flag(Reflection_Event_Arabella_Death.uuid, True, speaker_idx_tav),
            )),
        ),
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(Reflection_Event_Arabella_Death.uuid, False, speaker_idx_tav),
            )),
        ),
        root = True,
        constructor = bg3.dialog_object.GREETING)
    d.add_root_node(arabella_death_reflection_greeting_root_node_uuid, 0)

    d.add_child_dialog_node(bg3.SHADOWHEART_THOUGHTS_QUESTION_BANK_NODE_UUID, druid_this_harsh_node_uuid, 0)

    # I didn't expect to find a viper's nest at the heart of the druid grove.
    d.create_standard_dialog_node(
        druid_this_harsh_node_uuid,
        bg3.SPEAKER_PLAYER,
        [lets_find_that_healer_node_uuid, lets_get_in_and_out_of_this_place_node_uuid],
        bg3.text_content('hfbe84835g4054g4839g8131g7e08e7c89383', 1),
        constructor = bg3.dialog_object.QUESTION,
        checkflags = (
            bg3.flag_group(bg3.flag_group.OBJECT, (
                bg3.flag(Reflection_Available_Arabella_Death.uuid, True, speaker_idx_tav),
            )),
            bg3.flag_group(bg3.flag_group.GLOBAL, (
                bg3.flag(ReallyShadowheart_Ext_V2_0_0_0.uuid, True, None),
                bg3.flag(bg3.FLAG_VISITEDREGION_SCL_Main_A_ACT_2, False, None),
                bg3.flag(bg3.DEN_AttackOnDen_State_DenVictory, False, None),
                bg3.flag(bg3.DEN_AttackOnDen_State_RaiderVictory, False, None),
                bg3.flag(bg3.DEN_Lockdown_State_Active, False, None),
            )),
        ))

    # These druids have a child's death on their hands... let's find that healer before any vipers decide to bare their fangs at <i>us.</i>
    d.create_standard_dialog_node(
        lets_find_that_healer_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [
            im_not_dealing_with_child_killers_healer_node_uuid,
            im_not_dealing_with_child_killers_node_uuid,
            but_you_held_back_node_uuid,
            im_surprised_you_care_node_uuid,
            she_tried_to_steal_node_uuid,
            we_shouldve_done_something_node_uuid,
            i_shouldve_just_attacked_node_uuid,
            what_will_her_parents_say_node_uuid,
        ],
        bg3.text_content('h48577497gd530g4cf3g9a0agca7fb6f5e450', 1),
        checkflags = (
            bg3.flag_group(bg3.flag_group.GLOBAL, (
                bg3.flag(bg3.FLAG_DEN_Apprentice_Knows_HeardAboutNettie, True, None),
            )),
        ),
        constructor = bg3.dialog_object.ANSWER)
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '7.27',
        lets_find_that_healer_node_uuid,
        (('7.3', '7b067edd-f53f-49e1-95bc-0986e6e2ca2f'), (None, 'e08db860-1e62-4271-bf4e-d51602468573')),
        phase_duration = '7.5',
        performance_fade = 2.5,
        fade_in = 1.5,
        fade_out = 1.0,
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 8, None), (1.63, 128, None), (3.93, 64, 2), (6.86, 128, None))
        },
        attitudes = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_R_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, None),),
            bg3.SPEAKER_PLAYER: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_L_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, None),),
        })

    # They killed a child, for that...? Let's get in and out of this place before any vipers decide to bare their fangs at us.
    d.create_standard_dialog_node(
        lets_get_in_and_out_of_this_place_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [jump_lets_find_that_healer_node_uuid],
        bg3.text_content('h48e97518ga03bg4506gb6d2g0694acd3cf4a', 1),
        checkflags = (
            bg3.flag_group(bg3.flag_group.GLOBAL, (
                bg3.flag(bg3.FLAG_DEN_Apprentice_Knows_HeardAboutNettie, False, None),
            )),
        ),
        constructor = bg3.dialog_object.ANSWER)
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '7.23',
        lets_get_in_and_out_of_this_place_node_uuid,
        (('7.3', '7b067edd-f53f-49e1-95bc-0986e6e2ca2f'), (None, 'e08db860-1e62-4271-bf4e-d51602468573')),
        phase_duration = '7.5',
        performance_fade = 2.5,
        fade_in = 1.5,
        fade_out = 1.0,
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 128, None), (0.81, 64, 2), (1.64, 32, None), (3.73, 64, 2), (6.97, 128, None))
        },
        attitudes = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_R_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, None),),
            bg3.SPEAKER_PLAYER: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_L_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, None),),
        })
    d.create_jump_dialog_node(jump_lets_find_that_healer_node_uuid, lets_find_that_healer_node_uuid, 2)

    # I'm not dealing with child-killers, even if they do have a healer.
    d.create_standard_dialog_node(
        im_not_dealing_with_child_killers_healer_node_uuid,
        bg3.SPEAKER_PLAYER,
        [principles_wont_save_us_node_uuid],
        bg3.text_content('h81035637g46d0g49ebgba34g354840f54aa8', 1),
        constructor = bg3.dialog_object.QUESTION,
        approval_rating_uuid = reaction_plus_1.uuid,
        checkflags = (
            bg3.flag_group(bg3.flag_group.GLOBAL, (
                bg3.flag(bg3.FLAG_DEN_Apprentice_Knows_HeardAboutNettie, True, None),
            )),
        ))

    # I'm not dealing with child-killers. Doesn't matter if they can help us or not.
    d.create_standard_dialog_node(
        im_not_dealing_with_child_killers_node_uuid,
        bg3.SPEAKER_PLAYER,
        [principles_wont_save_us_node_uuid],
        bg3.text_content('h97820e55gb731g4d21ga969ge213b0d23b8c', 1),
        constructor = bg3.dialog_object.QUESTION,
        approval_rating_uuid = reaction_plus_1.uuid,
        checkflags = (
            bg3.flag_group(bg3.flag_group.GLOBAL, (
                bg3.flag(bg3.FLAG_DEN_Apprentice_Knows_HeardAboutNettie, False, None),
            )),
        ))

    # Principles won't save us. Not this time. Just... bite your tongue, for now.<br>
    d.create_standard_dialog_node(
        principles_wont_save_us_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [],
        bg3.text_content('h61e41c7agbabbg44cdgbc86g5e8f5ebd7a5d', 1),
        end_node = True,
        constructor = bg3.dialog_object.ANSWER)
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '6.68',
        principles_wont_save_us_node_uuid,
        (('6.7', '7b067edd-f53f-49e1-95bc-0986e6e2ca2f'), (None, 'e08db860-1e62-4271-bf4e-d51602468573')),
        phase_duration = '7.0',
        performance_fade = 2.5,
        fade_in = 1.0,
        fade_out = 0.0,
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 32, None), (2.2, 64, 2), (3.64, 4, None), (4.11, 2048, 2), (4.84, 4, None))
        },
        attitudes = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_R_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, None),),
            bg3.SPEAKER_PLAYER: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_L_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, None),),
        })

    # We could've stopped this but you held back. The child's death is on you as well.
    d.create_standard_dialog_node(
        but_you_held_back_node_uuid,
        bg3.SPEAKER_PLAYER,
        [i_didnt_know_that_was_going_to_happen_node_uuid],
        bg3.text_content('h147c2a41g1b77g46a9gb35agdf188ca07c55', 1),
        constructor = bg3.dialog_object.QUESTION,
        approval_rating_uuid = reaction_minus_1.uuid,
        checkflags = (
            bg3.flag_group('Dialog', (
                bg3.flag('e78abad6-c3ac-4cfd-950b-adef28ab68c2', True, speaker_idx_tav), # DEN_ShadowDruid_SnakesCourt_SHWarnsAgainstCombat
            )),
        ))

    # I didn't know that was going to happen. Don't pretend picking a fight would've saved that little girl.
    d.create_standard_dialog_node(
        i_didnt_know_that_was_going_to_happen_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [],
        bg3.text_content('h05b65d73g0834g49d4ga83cgd939bfc73812', 1),
        end_node = True,
        constructor = bg3.dialog_object.ANSWER)
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '5.92',
        i_didnt_know_that_was_going_to_happen_node_uuid,
        (('6.0', '7b067edd-f53f-49e1-95bc-0986e6e2ca2f'), (None, 'e08db860-1e62-4271-bf4e-d51602468573')),
        phase_duration = '6.2',
        performance_fade = 2.5,
        fade_in = 1.0,
        fade_out = 0.0,
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 8, 1), (0.45, 8, 2), (3.15, 32, None), (5.02, 32, 1))
        },
        attitudes = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_R_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, None),),
            bg3.SPEAKER_PLAYER: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_L_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, None),),
        })

    # I'm surprised you care. That little girl was nobody to you.
    d.create_standard_dialog_node(
        im_surprised_you_care_node_uuid,
        bg3.SPEAKER_PLAYER,
        [do_you_truly_think_im_that_callous_node_uuid],
        bg3.text_content('h681c54d6g5871g4a04g9744g891caf7f1ff2', 1),
        approval_rating_uuid = reaction_minus_1.uuid,
        constructor = bg3.dialog_object.QUESTION)

    # Do you truly think I'm that callous? A young life snuffed out isn't easily shrugged off.
    d.create_standard_dialog_node(
        do_you_truly_think_im_that_callous_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [],
        bg3.text_content('h618b0c1cg15dfg4326g94b5g2848146e8651', 1),
        end_node = True,
        constructor = bg3.dialog_object.ANSWER)
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '6.02',
        do_you_truly_think_im_that_callous_node_uuid,
        (('6.0', '7b067edd-f53f-49e1-95bc-0986e6e2ca2f'), (None, 'e08db860-1e62-4271-bf4e-d51602468573')),
        phase_duration = '6.2',
        performance_fade = 2.5,
        fade_in = 1.0,
        fade_out = 0.0,
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.17, 8, 1), (1.65, 64, 2), (2.89, 32, None))
        },
        attitudes = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_R_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, None),),
            bg3.SPEAKER_PLAYER: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_L_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, None),),
        })

    # She tried to steal something precious to the druids - and paid the price.
    d.create_standard_dialog_node(
        she_tried_to_steal_node_uuid,
        bg3.SPEAKER_PLAYER,
        [quite_a_price_node_uuid],
        bg3.text_content('hb12bfeaagab56g44fdga150g16a6349f918f', 1),
        constructor = bg3.dialog_object.QUESTION,
        checkflags = (
            bg3.flag_group(bg3.flag_group.GLOBAL, (
                bg3.flag('91fbeb01-b3cf-d5a1-9ec1-0f2bcae4a14c', True, None), # DEN_DruidLeader_Event_ToldCrime
            )),
        ))

    # Quite a price. Let's behave ourselves around here - or at least let's not get caught.
    d.create_standard_dialog_node(
        quite_a_price_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [],
        bg3.text_content('hfeddd024ga270g43aaga668g5e7308b4caa6', 1),
        end_node = True,
        constructor = bg3.dialog_object.ANSWER)
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '7.44',
        quite_a_price_node_uuid,
        (('7.5', '7b067edd-f53f-49e1-95bc-0986e6e2ca2f'), (None, 'e08db860-1e62-4271-bf4e-d51602468573')),
        phase_duration = '7.7',
        performance_fade = 2.5,
        fade_in = 1.0,
        fade_out = 0.0,
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.27, 8, None), (2.8, 1, None), (5.25, 64, None), (6.25, 4, None))
        },
        attitudes = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_R_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, None),),
            bg3.SPEAKER_PLAYER: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_L_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, None),),
        })

    # We should have done something. Maybe we could have saved her.
    d.create_standard_dialog_node(
        we_shouldve_done_something_node_uuid,
        bg3.SPEAKER_PLAYER,
        [maybe_shed_still_be_dead_node_uuid],
        bg3.text_content('h5b7cadb0gf39dg4ceega647gcf122dea26d3', 1),
        constructor = bg3.dialog_object.QUESTION,
        checkflags = (
            bg3.flag_group(bg3.flag_group.GLOBAL, (
                bg3.flag('e73a3a99-89a5-29d7-f67a-1bded34c3a71', False, None), # DEN_ShadowDruid_Knows_AlmostAttackedSnakeCourt
            )),
        ))

    # Maybe. Or maybe she'd still be dead, and we'd be left fighting this lot.
    d.create_standard_dialog_node(
        maybe_shed_still_be_dead_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [we_cant_help_everyone_node_uuid],
        bg3.text_content('h883e659agedadg40deg82bag93ba71b57670', 1),
        constructor = bg3.dialog_object.ANSWER)
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '5.59',
        maybe_shed_still_be_dead_node_uuid,
        ((None, '7b067edd-f53f-49e1-95bc-0986e6e2ca2f'),),
        phase_duration = '5.8',
        performance_fade = 2.5,
        fade_in = 1.5,
        fade_out = 1.0,
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.25, 64, 2), (2.15, 4, None), (4.21, 8, None))
        },
        attitudes = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_R_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, None),),
            bg3.SPEAKER_PLAYER: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_L_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, None),),
        })

    # We... can't help everyone. Even if we want to.
    d.create_standard_dialog_node(
        we_cant_help_everyone_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [],
        bg3.text_content('hc8eb0375g5bb3g4485gb85age566d286a2fe', 1),
        end_node = True,
        constructor = bg3.dialog_object.ANSWER)
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '5.82',
        we_cant_help_everyone_node_uuid,
        (('5.9', '7b067edd-f53f-49e1-95bc-0986e6e2ca2f'), (None, 'e08db860-1e62-4271-bf4e-d51602468573')),
        phase_duration = '6.0',
        performance_fade = 2.5,
        fade_in = 1.5,
        fade_out = 0.0,
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.37, 32, None), (3.79, 64, 2))
        },
        attitudes = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_R_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, None),),
            bg3.SPEAKER_PLAYER: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_L_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, None),),
        })

    # I should have just attacked while I had the chance.
    d.create_standard_dialog_node(
        i_shouldve_just_attacked_node_uuid,
        bg3.SPEAKER_PLAYER,
        [then_wed_have_had_a_fight_node_uuid],
        bg3.text_content('h379b2d76gfb12g4851g845bgb2998b4a7581', 1),
        constructor = bg3.dialog_object.QUESTION,
        checkflags = (
            bg3.flag_group(bg3.flag_group.GLOBAL, (
                bg3.flag('e73a3a99-89a5-29d7-f67a-1bded34c3a71', True, None), # DEN_ShadowDruid_Knows_AlmostAttackedSnakeCourt
            )),
        ))

    # Then we'd have had a fight on our hands, and no hope of assistance from these druids.
    d.create_standard_dialog_node(
        then_wed_have_had_a_fight_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [we_cant_help_everyone_node_uuid],
        bg3.text_content('h45cd6ab6gd39ag458fgb29fg3416fbcbbc75', 1),
        constructor = bg3.dialog_object.ANSWER)
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '5.59',
        then_wed_have_had_a_fight_node_uuid,
        (('5.6', 'e7f21f15-f386-40f4-bb0f-2f9f42249ad1'),),
        phase_duration = '5.8',
        performance_fade = 2.5,
        fade_in = 1.5,
        fade_out = 1.0,
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.25, 64, 2), (2.15, 4, None), (4.21, 8, None))
        },
        attitudes = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_R_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, None),),
            bg3.SPEAKER_PLAYER: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_L_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, None),),
        })

    # What will her parents say? We told them we'd help.
    d.create_standard_dialog_node(
        what_will_her_parents_say_node_uuid,
        bg3.SPEAKER_PLAYER,
        [i_said_we_shouldnt_get_involved_node_uuid, perhaps_we_shouldnt_have_node_uuid],
        bg3.text_content('h9c9ef589g432cg41b8g80a4g6ca8bcf03740', 1),
        constructor = bg3.dialog_object.QUESTION,
        checkflags = (
            bg3.flag_group('Global', (
                bg3.flag('f22fc759-6072-4c9a-13a9-9b80ff5e384d', False, None), # DEN_GuardedEntrance_State_ParentsKnowDeath
            )),
            bg3.flag_group('User', (
                bg3.flag('c4fa8c89-2dca-664a-51c8-07f7d0def82d', True, speaker_idx_tav), # DEN_GuardedEntrance_State_OfferedHelpParents
            )),
        ))

    # 'We'? I said we shouldn't get involved.
    d.create_standard_dialog_node(
        i_said_we_shouldnt_get_involved_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [we_cant_help_everyone_node_uuid],
        bg3.text_content('h9788f3f4gbad4g4ac0g9daegba50efe40bfd', 1),
        constructor = bg3.dialog_object.ANSWER)
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '5.56',
        i_said_we_shouldnt_get_involved_node_uuid,
        ((None, '7b067edd-f53f-49e1-95bc-0986e6e2ca2f'),),
        phase_duration = '5.8',
        performance_fade = 2.5,
        fade_in = 1.5,
        fade_out = 1.0,
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.23, 8, None), (1.33, 64, None), (2.43, 64, 2))
        },
        attitudes = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_R_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, None),),
            bg3.SPEAKER_PLAYER: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_L_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, None),),
        })

    # Perhaps we shouldn't have.
    d.create_standard_dialog_node(
        perhaps_we_shouldnt_have_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [we_cant_help_everyone_node_uuid],
        bg3.text_content('h01e05477g6a6eg46cfgb791g1d0e4b9dc29a', 1),
        constructor = bg3.dialog_object.ANSWER)
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '1.95',
        perhaps_we_shouldnt_have_node_uuid,
        ((None, '7b067edd-f53f-49e1-95bc-0986e6e2ca2f'),),
        phase_duration = '2.1',
        performance_fade = 2.5,
        fade_in = 1.0,
        fade_out = 0.5,
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 4, None),)
        },
        attitudes = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_R_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, None),),
            bg3.SPEAKER_PLAYER: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_L_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, None),),
        })


def create_nettie_reaction() -> None:
    #################################################################################################
    # Dialog: DEN_Apprentice_Cyanide.lsf
    #################################################################################################

    ab = game_assets.get_modded_dialog_asset_bundle('DEN_Apprentice_Cyanide')
    d = bg3.dialog_object(ab.dialog)

    speaker_idx_tav = d.get_speaker_slot_index(bg3.SPEAKER_PLAYER)
    speaker_idx_shadowheart = d.get_speaker_slot_index(bg3.SPEAKER_SHADOWHEART)
    speaker_idx_karlach = d.get_speaker_slot_index(bg3.SPEAKER_KARLACH)
    speaker_idx_laezel = d.get_speaker_slot_index(bg3.SPEAKER_LAEZEL)
    speaker_idx_astarion = d.get_speaker_slot_index(bg3.SPEAKER_ASTARION)
    speaker_idx_gale = d.get_speaker_slot_index(bg3.SPEAKER_GALE)
    speaker_idx_wyll = d.get_speaker_slot_index(bg3.SPEAKER_WYLL)

    nettie_dialog_nodes_uuids = [
        '3785e625-4c3b-2d86-44b7-9ed7c7e6f534',
        '6e66be36-d45f-0505-9832-b8a99abd6b4a',
        '7d6bc8a2-ccd3-0e65-2500-7a320b77c692',
        '7e709ac2-8404-6e90-ebbf-d612de50cd83',
        '7fcd4e0b-a2cd-e0b9-3cbf-46d9b7db4a62',
        'b63ec106-afaf-977f-f639-700295eee78e',
        'dad8597c-863b-9ad4-62cf-5d9097dc95e3',
        'e5c46fef-838e-1275-b4f6-5d301ca9dc93',
    ]

    for nettie_dialog_node_uuid in nettie_dialog_nodes_uuids:
        d.add_dialog_flags(nettie_dialog_node_uuid, setflags = (
            bg3.flag_group('Object', (
                bg3.flag(Reflection_Event_Nettie.uuid, True, speaker_idx_tav),
                bg3.flag(Reflection_Available_Nettie.uuid, True, speaker_idx_tav)
            )),
        ))

    companion_inclusion_node_uuid = 'ec8bbe67-10dc-5205-982c-7656e31f5aef' # existing node
    you_dont_have_to_be_here_for_this_node_uuid = 'cf2b908b-7ba1-5490-0a49-349450737a8a' # existing node
    no_companions_are_in_dialogue_node_uuid = '5732a32d-4597-1850-8ae2-03e780daefff' # existing node
    shadowheart_is_in_dialogue_node_uuid = '0ad3f8d8-8bc2-4272-aca6-008c85be0541'
    karlach_is_in_dialogue_node_uuid = 'f57d6750-c13d-4c40-ae74-21c9a40a05ff'
    laezel_is_in_dialogue_node_uuid = '4d489be4-df08-4674-8f39-bf2b09e7b376'
    astarion_is_in_dialogue_node_uuid = 'ad7960c4-202a-46ef-8565-a97310d34bdb'
    gale_is_in_dialogue_node_uuid = '996635e9-545f-4353-835d-f5a2a1e353d4'
    wyll_is_in_dialogue_node_uuid = '56f0c52e-7a80-43ad-a408-a252e947bdc0'

    d.delete_all_children_dialog_nodes(companion_inclusion_node_uuid)
    d.add_child_dialog_node(companion_inclusion_node_uuid, shadowheart_is_in_dialogue_node_uuid)
    d.add_child_dialog_node(companion_inclusion_node_uuid, karlach_is_in_dialogue_node_uuid)
    d.add_child_dialog_node(companion_inclusion_node_uuid, laezel_is_in_dialogue_node_uuid)
    d.add_child_dialog_node(companion_inclusion_node_uuid, astarion_is_in_dialogue_node_uuid)
    d.add_child_dialog_node(companion_inclusion_node_uuid, gale_is_in_dialogue_node_uuid)
    d.add_child_dialog_node(companion_inclusion_node_uuid, wyll_is_in_dialogue_node_uuid)
    d.add_child_dialog_node(companion_inclusion_node_uuid, no_companions_are_in_dialogue_node_uuid)

    d.set_dialog_flags(you_dont_have_to_be_here_for_this_node_uuid, setflags = (), checkflags = ())

    d.create_standard_dialog_node(
        shadowheart_is_in_dialogue_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [you_dont_have_to_be_here_for_this_node_uuid],
        None,
        checkflags = (
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_AVATAR, False, speaker_idx_shadowheart),
                bg3.flag(bg3.TAG_REALLY_SHADOWHEART, True, speaker_idx_shadowheart)
            )),
        ))
    d.create_standard_dialog_node(
        karlach_is_in_dialogue_node_uuid,
        bg3.SPEAKER_KARLACH,
        [you_dont_have_to_be_here_for_this_node_uuid],
        None,
        checkflags = (
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_AVATAR, False, speaker_idx_karlach),
                bg3.flag(bg3.TAG_REALLY_KARLACH, True, speaker_idx_karlach)
            )),
        ))
    d.create_standard_dialog_node(
        laezel_is_in_dialogue_node_uuid,
        bg3.SPEAKER_LAEZEL,
        [you_dont_have_to_be_here_for_this_node_uuid],
        None,
        checkflags = (
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_AVATAR, False, speaker_idx_laezel),
                bg3.flag(bg3.TAG_REALLY_SHADOWHEART, True, speaker_idx_laezel)
            )),
        ))
    d.create_standard_dialog_node(
        astarion_is_in_dialogue_node_uuid,
        bg3.SPEAKER_ASTARION,
        [you_dont_have_to_be_here_for_this_node_uuid],
        None,
        checkflags = (
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_AVATAR, False, speaker_idx_astarion),
                bg3.flag(bg3.TAG_REALLY_SHADOWHEART, True, speaker_idx_astarion)
            )),
        ))
    d.create_standard_dialog_node(
        gale_is_in_dialogue_node_uuid,
        bg3.SPEAKER_GALE,
        [you_dont_have_to_be_here_for_this_node_uuid],
        None,
        checkflags = (
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_AVATAR, False, speaker_idx_gale),
                bg3.flag(bg3.TAG_REALLY_SHADOWHEART, True, speaker_idx_gale)
            )),
        ))
    d.create_standard_dialog_node(
        wyll_is_in_dialogue_node_uuid,
        bg3.SPEAKER_WYLL,
        [you_dont_have_to_be_here_for_this_node_uuid],
        None,
        checkflags = (
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_AVATAR, False, speaker_idx_wyll),
                bg3.flag(bg3.TAG_REALLY_SHADOWHEART, True, speaker_idx_wyll)
            )),
        ))


    #################################################################################################
    # Dialog: ShadowHeart_InParty2.lsf
    #################################################################################################

    ab = game_assets.get_modded_dialog_asset_bundle('ShadowHeart_InParty')
    d = bg3.dialog_object(ab.dialog)

    speaker_idx_tav = d.get_speaker_slot_index(bg3.SPEAKER_PLAYER)

    topical_greetings_node_uuid = 'dfec2c3c-2397-ff26-ef9e-09ad12d81b9f' # existing root node

    nettie_reflection_node_uuid = 'ac10f7ca-112e-4dbd-a0a6-9a145f1be46d'

    # reused node from putrid bog reflection
    nested_dialog_node_uuid = 'e2e11f4c-de6a-41af-9d83-623c2abdbdac'

    d.create_standard_dialog_node(
        nettie_reflection_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [nested_dialog_node_uuid],
        None,
        checkflags = (
            bg3.flag_group('Global', (
                bg3.flag(ReallyShadowheart_Ext_V2_0_0_0.uuid, True, None),
            )),
            bg3.flag_group('Object', (
                bg3.flag(Reflection_Event_Nettie.uuid, True, speaker_idx_tav),
            )),
        ),
        constructor = bg3.dialog_object.GREETING,
        root = True)
    d.add_root_node_before(topical_greetings_node_uuid, nettie_reflection_node_uuid)


    #################################################################################################
    # Dialog: ShadowHeart_InParty2_Nested_DefaultChapter.lsf
    #################################################################################################

    ab = game_assets.get_modded_dialog_asset_bundle('ShadowHeart_InParty2_Nested_DefaultChapter')
    d = bg3.dialog_object(ab.dialog)
    t = bg3.timeline_object(ab.timeline, d)

    speaker_idx_tav = d.get_speaker_slot_index(bg3.SPEAKER_PLAYER)

    nettie_reflection_greeting_root_node_uuid = '27bb70b1-53a3-460b-88ec-fe68de4a9a8d'

    if_i_ever_trust_idea_node_uuid = 'f5d189c0-0b6b-4ec0-a5e3-e8de84dcf731'
    all_we_got_is_poison_node_uuid = '2283a11a-0f1a-4ef5-b716-31855bc18ab0'
    blind_honesty_is_always_a_bad_idea_node_uuid = '13c28b13-25d3-4d1d-9b1d-3b6c513327c7'
    telling_the_wrong_person_node_uuid = '77464a4f-eb48-40e3-a395-6470a3ec5fb1'
    angry_mob_to_get_to_us_node_uuid = '3640d9f5-db51-441a-837b-00a8ff0970e3'
    how_do_you_expect_to_find_help_node_uuid = '47d87103-a605-40ba-b645-428437d93def'
    more_than_one_way_to_get_what_you_want_node_uuid = '94ef3827-57e4-472b-85b0-9a5f661eb8bc'
    this_got_us_a_free_vial_of_poison_node_uuid = '26f7a66d-1a63-4f09-9732-f385f56b72b6'
    poison_as_a_last_resort_node_uuid = 'c649addd-4699-49b4-ac87-ad0922587e18'
    as_a_very_last_resort_yes_node_uuid = '6c48f3cc-e80d-4e60-8112-c92d9614d584'
    pleasant_notions_are_in_short_supply_node_uuid = '6dbb7e84-8111-417b-9750-114f35eccd58'
    cowardly_more_like_node_uuid = '5f82e175-c174-4ae3-891f-2421f93da2ac'
    if_you_turn_into_a_monster_node_uuid = '8070adbd-12c2-451f-afe8-659da020e146'

    d.add_child_dialog_node(bg3.SHADOWHEART_THOUGHTS_QUESTION_BANK_NODE_UUID, all_we_got_is_poison_node_uuid, 0)
    d.add_child_dialog_node(bg3.SHADOWHEART_THOUGHTS_QUESTION_BANK_NODE_UUID, if_i_ever_trust_idea_node_uuid, 0)

    d.create_standard_dialog_node(
        nettie_reflection_greeting_root_node_uuid,
        bg3.SPEAKER_PLAYER,
        [blind_honesty_is_always_a_bad_idea_node_uuid, poison_as_a_last_resort_node_uuid],
        None,
        checkflags = (
            bg3.flag_group('Global', (
                bg3.flag(ReallyShadowheart_Ext_V2_0_0_0.uuid, True, None),
            )),
            bg3.flag_group('Object', (
                bg3.flag(Reflection_Event_Nettie.uuid, True, speaker_idx_tav),
            )),
        ),
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(Reflection_Event_Nettie.uuid, False, speaker_idx_tav),
            )),
        ),
        root = True,
        constructor = bg3.dialog_object.GREETING)
    d.add_root_node(nettie_reflection_greeting_root_node_uuid, 0)

    # If I'm ever going to trust a druid again, please remind me of Nettie.
    d.create_standard_dialog_node(
        if_i_ever_trust_idea_node_uuid,
        bg3.SPEAKER_PLAYER,
        [blind_honesty_is_always_a_bad_idea_node_uuid],
        bg3.text_content('hf3690a21g7aa9g4989g833eg7e134e2f536d', 1),
        constructor = bg3.dialog_object.QUESTION,
        checkflags = (
            bg3.flag_group(bg3.flag_group.OBJECT, (
                bg3.flag(Reflection_Available_Nettie.uuid, True, speaker_idx_tav),
                bg3.flag(bg3.FLAG_DEN_Apprentice_State_Cyanide_ShortPath, False, speaker_idx_tav)
            )),
            bg3.flag_group(bg3.flag_group.GLOBAL, (
                bg3.flag(ReallyShadowheart_Ext_V2_0_0_0.uuid, True, None),
                bg3.flag(bg3.FLAG_VISITEDREGION_SCL_Main_A_ACT_2, False, None),
                bg3.flag(bg3.DEN_AttackOnDen_State_DenVictory, False, None),
                bg3.flag(bg3.DEN_AttackOnDen_State_RaiderVictory, False, None),
                bg3.flag(bg3.DEN_Lockdown_State_Active, False, None),
            )),
        ))

    # We went to the grove looking for a cure, but all we got is poison.
    d.create_standard_dialog_node(
        all_we_got_is_poison_node_uuid,
        bg3.SPEAKER_PLAYER,
        [poison_as_a_last_resort_node_uuid],
        bg3.text_content('h4c03c093gef02g4258gbcf8g09ac9c185339', 1),
        checkflags = (
            bg3.flag_group(bg3.flag_group.OBJECT, (
                bg3.flag(Reflection_Available_Nettie.uuid, True, speaker_idx_tav),
                bg3.flag(bg3.FLAG_DEN_Apprentice_State_Cyanide_ShortPath, True, speaker_idx_tav),
                bg3.flag(bg3.FLAG_DEN_Apprentice_Event_GiveWyvenPoison, True, speaker_idx_tav),
            )),
            bg3.flag_group(bg3.flag_group.GLOBAL, (
                bg3.flag(ReallyShadowheart_Ext_V2_0_0_0.uuid, True, None),
                bg3.flag(bg3.FLAG_VISITEDREGION_SCL_Main_A_ACT_2, False, None),
                bg3.flag(bg3.DEN_AttackOnDen_State_DenVictory, False, None),
                bg3.flag(bg3.DEN_AttackOnDen_State_RaiderVictory, False, None),
                bg3.flag(bg3.DEN_Lockdown_State_Active, False, None),
            )),
        ),
        constructor = bg3.dialog_object.QUESTION)

    # Blind honesty is always a bad idea. We should keep quiet in future.
    d.create_standard_dialog_node(
        blind_honesty_is_always_a_bad_idea_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [
            telling_the_wrong_person_node_uuid,
            this_got_us_a_free_vial_of_poison_node_uuid,
            how_do_you_expect_to_find_help_node_uuid,
        ],
        bg3.text_content('hd4ed454cg32c2g44fbgaf16g3476e0bf9222', 1),
        checkflags = (
            bg3.flag_group(bg3.flag_group.OBJECT, (
                bg3.flag(bg3.FLAG_DEN_Apprentice_State_Cyanide_ShortPath, False, speaker_idx_tav),
            )),
        ))
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '5.31',
        blind_honesty_is_always_a_bad_idea_node_uuid,
        (('5.4', '7b067edd-f53f-49e1-95bc-0986e6e2ca2f'), (None, 'e08db860-1e62-4271-bf4e-d51602468573')),
        phase_duration = '5.6',
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 8, None), (1.33, 64, None), (2.28, 4, None), (3.21, 8, None))
        },
        attitudes = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_R_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, None),),
            bg3.SPEAKER_PLAYER: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_L_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, None),),
        })    

    # Agreed. Telling the wrong person about our little problem could prove fatal.
    d.create_standard_dialog_node(
        telling_the_wrong_person_node_uuid,
        bg3.SPEAKER_PLAYER,
        [angry_mob_to_get_to_us_node_uuid],
        bg3.text_content('h0ec85cefg0f8fg49c2g9716g1f566b7fdae7', 1),
        constructor = bg3.dialog_object.QUESTION)

    # Indeed. Wouldn't want a frightened and angry mob to get to us before the tadpole did, would we?
    d.create_standard_dialog_node(
        angry_mob_to_get_to_us_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [],
        bg3.text_content('h248d4b24g6f9fg4e0fgacc8g0000aad80dbf', 1),
        end_node = True)
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '6.64',
        angry_mob_to_get_to_us_node_uuid,
        (('6.64', 'e7f21f15-f386-40f4-bb0f-2f9f42249ad1'), (None, 'e08db860-1e62-4271-bf4e-d51602468573')),
        phase_duration = '6.95',
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 4, 1), (2.28, 128, 1), (5.2, 64, None),)
        },
        attitudes = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_R_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, None),),
            bg3.SPEAKER_PLAYER: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_L_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, None),),
        })    

    reaction_minus_3 = bg3.reaction_object.create_new(game_assets.files, { bg3.SPEAKER_SHADOWHEART: -3 }, uuid = '52a3c67a-4700-402a-8c66-38f89ca676e1')
    # How do you expect to find help if we don't tell anyone what the problem is?
    d.create_standard_dialog_node(
        how_do_you_expect_to_find_help_node_uuid,
        bg3.SPEAKER_PLAYER,
        [more_than_one_way_to_get_what_you_want_node_uuid],
        bg3.text_content('h7b65f7afgc1a1g4523ga3a3g56257996f45b', 1),
        constructor = bg3.dialog_object.QUESTION,
        approval_rating_uuid = reaction_minus_3.uuid)

    # There's more than one way to get what you want. Spilling secrets leads to spilled blood.
    d.create_standard_dialog_node(
        more_than_one_way_to_get_what_you_want_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [],
        bg3.text_content('h8c00c1adg411fg4190gb0bcg5746da9da979', 1),
        end_node = True)
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '5.98',
        more_than_one_way_to_get_what_you_want_node_uuid,
        (('5.98', 'e7f21f15-f386-40f4-bb0f-2f9f42249ad1'), (None, 'e08db860-1e62-4271-bf4e-d51602468573')),
        phase_duration = '6.4',
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 64, None), (2.65, 8, None), (4.4, 128, 1),)
        },
        attitudes = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_R_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, None),),
            bg3.SPEAKER_PLAYER: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_L_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, None),),
        })

    # Well, at least this got us a free vial of poison.
    d.create_standard_dialog_node(
        this_got_us_a_free_vial_of_poison_node_uuid,
        bg3.SPEAKER_PLAYER,
        [poison_as_a_last_resort_node_uuid],
        bg3.text_content('hd76b0332g14a4g40aag923ag09f88731c4ab', 1),
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_DEN_Apprentice_Event_GiveWyvenPoison, True, speaker_idx_tav),
            )),
        ),
        constructor = bg3.dialog_object.QUESTION)

    # Poison as a last resort - sensible.
    d.create_standard_dialog_node(
        poison_as_a_last_resort_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [as_a_very_last_resort_yes_node_uuid, cowardly_more_like_node_uuid],
        bg3.text_content('hcbad04f2g314bg479ag88b1g23befb081253', 1))
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '2.93',
        poison_as_a_last_resort_node_uuid,
        (('2.93', 'e7f21f15-f386-40f4-bb0f-2f9f42249ad1'), (None, 'e08db860-1e62-4271-bf4e-d51602468573')),
        phase_duration = '3.3',
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 4, None), (2.06, 64, None))
        },
        attitudes = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_R_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, None),),
            bg3.SPEAKER_PLAYER: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_L_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, None),),
        })

    # As a very last resort, yes. But not a pleasant notion all the same.
    d.create_standard_dialog_node(
        as_a_very_last_resort_yes_node_uuid,
        bg3.SPEAKER_PLAYER,
        [pleasant_notions_are_in_short_supply_node_uuid],
        bg3.text_content('h3d2fa92eg5accg4a1fgae8bgc7d33e163578', 1),
        constructor = bg3.dialog_object.QUESTION)

    # Pleasant notions are in short supply. I'll take a quick exit if I need to.
    d.create_standard_dialog_node(
        pleasant_notions_are_in_short_supply_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [],
        bg3.text_content('he076d76cg0fbcg4d50ga7e4g2ba631d8fc91', 1),
        end_node = True)
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '4.88',
        pleasant_notions_are_in_short_supply_node_uuid,
        (('4.9', 'e7f21f15-f386-40f4-bb0f-2f9f42249ad1'), (None, 'e08db860-1e62-4271-bf4e-d51602468573')),
        phase_duration = '5.3',
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 4, 2), (2.77, 32, None), (4.07, 8, None))
        },
        attitudes = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_R_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, None),),
            bg3.SPEAKER_PLAYER: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_L_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, None),),
        })

    reaction_minus_5 = bg3.reaction_object.create_new(game_assets.files, { bg3.SPEAKER_SHADOWHEART: -5 }, uuid = '1e7d8a7f-18c9-4434-b943-ce15a75e7dd9')

    # Sensible? Cowardly, more like. I haven't survived this long just to take my own life.
    d.create_standard_dialog_node(
        cowardly_more_like_node_uuid,
        bg3.SPEAKER_PLAYER,
        [if_you_turn_into_a_monster_node_uuid],
        bg3.text_content('h735fa879g5937g4f39ga162g0e4d6aca9f67', 1),
        constructor = bg3.dialog_object.QUESTION,
        approval_rating_uuid = reaction_minus_5.uuid)

    # If you turn into a monster, it'll already be taken.
    d.create_standard_dialog_node(
        if_you_turn_into_a_monster_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [],
        bg3.text_content('h1e227150g264fg4c4dg90a6g55d8894b6c5c', 1),
        end_node = True)
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '3.32',
        if_you_turn_into_a_monster_node_uuid,
        (('3.4', 'e7f21f15-f386-40f4-bb0f-2f9f42249ad1'), (None, 'e08db860-1e62-4271-bf4e-d51602468573')),
        phase_duration = '3.5',
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 4, None), (1.91, 4, 2))
        },
        attitudes = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_R_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, None),),
            bg3.SPEAKER_PLAYER: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_L_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, None),),
        })


bg3.add_build_procedure('create_reaction_to_saving_sazza', create_reaction_to_sazza)
bg3.add_build_procedure('create_reaction_arabella_death', create_reaction_arabella_death)
bg3.add_build_procedure('create_nettie_reaction', create_nettie_reaction)

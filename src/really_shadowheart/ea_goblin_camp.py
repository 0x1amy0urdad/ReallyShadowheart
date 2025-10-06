from __future__ import annotations

import bg3moddinglib as bg3

from .context import game_assets
from .flags import *

def create_goblin_camp_reaction() -> None:
    #################################################################################################
    # Dialog: ShadowHeart_InParty2.lsf
    #################################################################################################

    ab = game_assets.get_modded_dialog_asset_bundle('ShadowHeart_InParty')
    d = bg3.dialog_object(ab.dialog)

    speaker_idx_tav = d.get_speaker_slot_index(bg3.SPEAKER_PLAYER)

    topical_greetings_node_uuid = 'dfec2c3c-2397-ff26-ef9e-09ad12d81b9f' # existing root node

    goblin_camp_reflection_node_uuid = '739c4698-2626-4412-a71f-5142a165081e'

    # reused node from putrid bog reflection
    nested_dialog_node_uuid = 'e2e11f4c-de6a-41af-9d83-623c2abdbdac'

    d.create_standard_dialog_node(
        goblin_camp_reflection_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [nested_dialog_node_uuid],
        None,
        checkflags = (
            bg3.flag_group('Global', (
                bg3.flag(ReallyShadowheart_Ext_V2_0_0_0.uuid, True, None),
            )),
            bg3.flag_group('Object', (
                bg3.flag(Reflection_Event_Goblin_Camp.uuid, True, speaker_idx_tav),
            )),
        ),
        constructor = bg3.dialog_object.GREETING,
        root = True)
    d.add_root_node_before(topical_greetings_node_uuid, goblin_camp_reflection_node_uuid)

    #################################################################################################
    # Dialog: ShadowHeart_InParty2_Nested_DefaultChapter.lsf
    #################################################################################################

    ab = game_assets.get_modded_dialog_asset_bundle('ShadowHeart_InParty2_Nested_DefaultChapter')
    d = bg3.dialog_object(ab.dialog)
    t = bg3.timeline_object(ab.timeline, d)

    speaker_idx_tav = d.get_speaker_slot_index(bg3.SPEAKER_PLAYER)

    goblin_camp_reflection_greeting_root_node_uuid = '22ad21f9-fb1b-45e6-ac88-ec8c49cd28ae'
    judging_by_the_stench_node_uuid = 'ac0de771-e517-4fde-9820-2f35c90f3598'
    a_lot_of_goblins_around_here_node_uuid = 'f33dbb7b-bd04-45d4-99ab-6d5a131eda83'
    keep_things_discreet_node_uuid = 'eb9a0018-64b6-4620-9e2b-4516cdf57c13'
    fighting_our_way_out_node_uuid = '4aa8c46d-b070-4014-9482-e75941f72740'
    numbers_arent_everything_node_uuid = '04a9136a-29ff-48b2-bac0-12d12d1b7ac8'
    lets_not_be_rash_node_uuid = '5a8a4dc4-c5d6-46f6-bb88-6794cf01ee4e'
    take_out_their_leaders_node_uuid = '916d5582-b492-4db2-a02a-edf63642b019'
    enough_dark_corners_node_uuid = '281b6fc2-55a2-4996-8d97-d633b91f9511'
    blade_thirsts_node_uuid = '532dd387-678c-4f07-b5b7-64ecea371290'
    do_me_a_favour_node_uuid = '20cff777-a3ee-4401-ac1e-461b3a0e440d'
    i_dont_like_this_node_uuid = '61204584-a6f0-4d1c-8034-13dea2b23058'
    save_your_moralizing_node_uuid = 'e0ca88da-6179-4cdd-83fb-42e4ca0805c2'
    im_not_worried_node_uuid = '08d793f0-c88d-4f2a-b299-c1ca2d328721'
    fair_enough_node_uuid = '993da4d6-6986-4840-98d0-85b45e3b4825'
    being_riled_node_uuid = 'e029682c-ea2d-4350-b501-96a06c565187'
    mind_that_temper_node_uuid = '10ac88f4-2e42-41eb-bbf2-81d3c3f2b94c'

    d.create_standard_dialog_node(
        goblin_camp_reflection_greeting_root_node_uuid,
        bg3.SPEAKER_PLAYER,
        [a_lot_of_goblins_around_here_node_uuid],
        None,
        checkflags = (
            bg3.flag_group('Global', (
                bg3.flag(ReallyShadowheart_Ext_V2_0_0_0.uuid, True, None),
            )),
            bg3.flag_group('Object', (
                bg3.flag(Reflection_Event_Goblin_Camp.uuid, True, speaker_idx_tav),
            )),
        ),
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(Reflection_Event_Goblin_Camp.uuid, False, speaker_idx_tav),
            )),
        ),
        root = True,
        constructor = bg3.dialog_object.GREETING)
    d.add_root_node(goblin_camp_reflection_greeting_root_node_uuid, 0)

    # Judging by the stench, there are far more goblins than meets the eye.
    d.create_standard_dialog_node(
        judging_by_the_stench_node_uuid,
        bg3.SPEAKER_PLAYER,
        [a_lot_of_goblins_around_here_node_uuid],
        bg3.text_content('h3c811d37gd130g437cgb628g857e2fd18a2b', 1),
        checkflags = (
            bg3.flag_group(bg3.flag_group.OBJECT, (
                bg3.flag(Reflection_Available_Goblin_Camp.uuid, True, speaker_idx_tav),
            )),
            bg3.flag_group(bg3.flag_group.GLOBAL, (
                bg3.flag(ReallyShadowheart_Ext_V2_0_0_0.uuid, True, None),
                bg3.flag(bg3.GOB_State_LeadersAreDead, False, None),
                bg3.flag(bg3.DEN_AttackOnDen_State_DenVictory, False, None),
                bg3.flag(bg3.DEN_AttackOnDen_State_RaiderVictory, False, None),
                bg3.flag(bg3.DEN_Lockdown_State_Active, False, None),
                bg3.flag(bg3.FLAG_VISITEDREGION_SCL_Main_A_ACT_2, False, None),
            )),
        ),
        constructor = bg3.dialog_object.QUESTION)
    d.add_child_dialog_node(bg3.SHADOWHEART_THOUGHTS_QUESTION_BANK_NODE_UUID, judging_by_the_stench_node_uuid, 0)

    # A lot of goblins around here - best not to rile them.
    d.create_standard_dialog_node(
        a_lot_of_goblins_around_here_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [
            keep_things_discreet_node_uuid,
            numbers_arent_everything_node_uuid,
            take_out_their_leaders_node_uuid,
            blade_thirsts_node_uuid,
            i_dont_like_this_node_uuid,
            im_not_worried_node_uuid,
            being_riled_node_uuid,
        ],
        bg3.text_content('h9261acafg3f67g4babg9548g6b0baff8a232', 1))
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '4.78',
        a_lot_of_goblins_around_here_node_uuid,
        (('4.8', 'e7f21f15-f386-40f4-bb0f-2f9f42249ad1'), (None, 'e08db860-1e62-4271-bf4e-d51602468573')),
        phase_duration = '5.1',
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 16, None), (2.69, 1024, 1))
        },
        attitudes = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_R_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, None),),
            bg3.SPEAKER_PLAYER: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_L_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, None),),
        })    

    # Indeed. Let's keep things discreet for now.
    d.create_standard_dialog_node(
        keep_things_discreet_node_uuid,
        bg3.SPEAKER_PLAYER,
        [fighting_our_way_out_node_uuid],
        bg3.text_content('h8b4160c3ge0f9g458bg883cg74eede808efc', 1),
        constructor = bg3.dialog_object.QUESTION)
    # If there's trouble, we can always try fighting our way out. Let's at least look around first.
    d.create_standard_dialog_node(
        fighting_our_way_out_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [],
        bg3.text_content('h333dd578g7305g4788ga608g05b2261fc9a9', 1),
        end_node = True)
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '5.95',
        fighting_our_way_out_node_uuid,
        (('6.0', '7b067edd-f53f-49e1-95bc-0986e6e2ca2f'), (None, 'e08db860-1e62-4271-bf4e-d51602468573')),
        phase_duration = '6.2',
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 2048, None), (1.46, 16, None), (4.15, 4, 2))
        },
        attitudes = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_R_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, None),),
            bg3.SPEAKER_PLAYER: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_L_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, None),),
        })

    # We could take them on. Numbers aren't everything.
    d.create_standard_dialog_node(
        numbers_arent_everything_node_uuid,
        bg3.SPEAKER_PLAYER,
        [lets_not_be_rash_node_uuid],
        bg3.text_content('h8d83d0aag5f12g4945g8c72ge7997846e38a', 1),
        constructor = bg3.dialog_object.QUESTION)
    # Not everything, but something. Let's not be rash.
    d.create_standard_dialog_node(
        lets_not_be_rash_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [],
        bg3.text_content('h9c3da78cgf31bg4ce7g8b8cgb4d3880e87e4', 1),
        end_node = True)
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '4.96',
        lets_not_be_rash_node_uuid,
        (('5.0', '7b067edd-f53f-49e1-95bc-0986e6e2ca2f'), (None, 'e08db860-1e62-4271-bf4e-d51602468573')),
        phase_duration = '5.2',
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 4, 1), (1.98, 1, None), (3.38, 8, None))
        },
        attitudes = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_R_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, None),),
            bg3.SPEAKER_PLAYER: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_L_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, None),),
        })

    # We only need to take out their leaders anyway. No point in making things harder on ourselves.
    d.create_standard_dialog_node(
        take_out_their_leaders_node_uuid,
        bg3.SPEAKER_PLAYER,
        [enough_dark_corners_node_uuid],
        bg3.text_content('h1f259c06g38f0g44c9g81eeg2690864189ac', 1),
        constructor = bg3.dialog_object.QUESTION)
    # True. I imagine there's enough dark corners here to accomplish that without much trouble.
    d.create_standard_dialog_node(
        enough_dark_corners_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [],
        bg3.text_content('h89a3e500gb1aag4b14gba63g97606af3c642', 1),
        end_node = True)
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '6.01',
        enough_dark_corners_node_uuid,
        (('6.01', '7b067edd-f53f-49e1-95bc-0986e6e2ca2f'), (None, 'e08db860-1e62-4271-bf4e-d51602468573')),
        phase_duration = '6.2',
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 4, 1), (1.98, 1, None), (3.38, 8, None))
        },
        attitudes = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_R_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, None),),
            bg3.SPEAKER_PLAYER: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_L_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, None),),
        })

    reaction_minus_1 = bg3.reaction_object.create_new(game_assets.files, { bg3.SPEAKER_SHADOWHEART: -1 }, uuid = '3dd10b0f-fcfa-4443-8975-c1e6d863d42e')
    # My blade thirsts for their blood.
    d.create_standard_dialog_node(
        blade_thirsts_node_uuid,
        bg3.SPEAKER_PLAYER,
        [do_me_a_favour_node_uuid],
        bg3.text_content('hc5086a21gdd61g4fccg9ccag33d010647a2f', 1),
        approval_rating_uuid = reaction_minus_1.uuid,
        constructor = bg3.dialog_object.QUESTION)
    # Do me a favour and keep your blade tucked where it belongs.
    d.create_standard_dialog_node(
        do_me_a_favour_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [],
        bg3.text_content('h5d81f247g90bdg474aga7b0g76e990a01e1e', 1),
        end_node = True)
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '3.61',
        do_me_a_favour_node_uuid,
        (('3.61', '7b067edd-f53f-49e1-95bc-0986e6e2ca2f'), (None, 'e08db860-1e62-4271-bf4e-d51602468573')),
        phase_duration = '3.8',
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 2, None), (1.37, 128, None))
        },
        attitudes = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, bg3.ATTITUDE_DIAG_Pose_Crossed_01, bg3.ATTITUDE_DIAG_T_Pose, None),),
            bg3.SPEAKER_PLAYER: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_L_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, None),),
        })

    # I don't like this - walking through a camp of wicked creatures.
    d.create_standard_dialog_node(
        i_dont_like_this_node_uuid,
        bg3.SPEAKER_PLAYER,
        [save_your_moralizing_node_uuid],
        bg3.text_content('h74b9c7fbg9b00g4293g9f92gadeee6361b1f', 1),
        approval_rating_uuid = reaction_minus_1.uuid,
        checkflags = (
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_CLERIC_GOOD, True, speaker_idx_tav),
            )),
        ),
        constructor = bg3.dialog_object.QUESTION)
    # Save your moralizing. I'm sure your generous god will forgive you.
    d.create_standard_dialog_node(
        save_your_moralizing_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [],
        bg3.text_content('hf24faf2dg1655g4bdagb5e2g045c601d90c3', 1),
        end_node = True)
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '4.73',
        save_your_moralizing_node_uuid,
        (('4.75', '7b067edd-f53f-49e1-95bc-0986e6e2ca2f'), (None, 'e08db860-1e62-4271-bf4e-d51602468573')),
        phase_duration = '5.0',
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 64, 2), (2.54, 1024, 1))
        },
        attitudes = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, bg3.ATTITUDE_DIAG_Pose_Crossed_01, bg3.ATTITUDE_DIAG_T_Pose, None),),
            bg3.SPEAKER_PLAYER: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_L_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, None),),
        })

    # I'm not worried. I've outsmarted plenty of goblins before.
    d.create_standard_dialog_node(
        im_not_worried_node_uuid,
        bg3.SPEAKER_PLAYER,
        [fair_enough_node_uuid],
        bg3.text_content('hccb4dd99g8dc0g4e46gb56ag13184fc0c599', 1),
        constructor = bg3.dialog_object.QUESTION)
    # Fair enough. I suppose they're not known for their brains.
    d.create_standard_dialog_node(
        fair_enough_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [],
        bg3.text_content('h06d17aa7g54a2g4274gaf15g5783fd8db1e4', 1),
        end_node = True)
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '3.14',
        fair_enough_node_uuid,
        (('3.15', '7b067edd-f53f-49e1-95bc-0986e6e2ca2f'), (None, 'e08db860-1e62-4271-bf4e-d51602468573')),
        phase_duration = '3.5',
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 64, None), (1.39, 4, None))
        },
        attitudes = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_R_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, None),),
            bg3.SPEAKER_PLAYER: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_L_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, None),),
        })

    # Being riled is the least that these creatures deserve.
    d.create_standard_dialog_node(
        being_riled_node_uuid,
        bg3.SPEAKER_PLAYER,
        [mind_that_temper_node_uuid],
        bg3.text_content('h627b2b02g1572g4901gaab4g13e068fefa18', 1),
        constructor = bg3.dialog_object.QUESTION)
    # I'd mind that temper, unless you want to fight this entire camp on your lonesome.
    d.create_standard_dialog_node(
        mind_that_temper_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [],
        bg3.text_content('h0550e7b2g5ba8g4b69ga2e5gfcabac1e3723', 1),
        end_node = True)
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '5.05',
        mind_that_temper_node_uuid,
        (('5.05', '7b067edd-f53f-49e1-95bc-0986e6e2ca2f'), (None, 'e08db860-1e62-4271-bf4e-d51602468573')),
        phase_duration = '5.35',
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 8, None), (2.0, 64, None))
        },
        attitudes = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_R_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, None),),
            bg3.SPEAKER_PLAYER: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_L_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, None),),
        })

bg3.add_build_procedure('create_goblin_camp_reaction', create_goblin_camp_reaction)

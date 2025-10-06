from __future__ import annotations

import bg3moddinglib as bg3

from .context import game_assets
from .flags import *

def create_tadpole_reaction() -> None:
    #################################################################################################
    # Dialog: ShadowHeart_InParty2.lsf
    #################################################################################################

    ab = game_assets.get_modded_dialog_asset_bundle('ShadowHeart_InParty')
    d = bg3.dialog_object(ab.dialog)

    speaker_idx_tav = d.get_speaker_slot_index(bg3.SPEAKER_PLAYER)

    topical_greetings_node_uuid = 'dfec2c3c-2397-ff26-ef9e-09ad12d81b9f' # existing root node

    tadpole_reflection_node_uuid = '8c725bb0-9fb5-4632-91e2-6135696e4063'

    # reused node from putrid bog reflection
    nested_dialog_node_uuid = 'e2e11f4c-de6a-41af-9d83-623c2abdbdac'

    d.create_standard_dialog_node(
        tadpole_reflection_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [nested_dialog_node_uuid],
        None,
        checkflags = (
            bg3.flag_group('Global', (
                bg3.flag(ReallyShadowheart_Ext_V2_0_0_0.uuid, True, None),
            )),
            bg3.flag_group('Object', (
                bg3.flag(Reflection_Event_Tadpole.uuid, True, speaker_idx_tav),
            )),
        ),
        constructor = bg3.dialog_object.GREETING,
        root = True)
    d.add_root_node_before(topical_greetings_node_uuid, tadpole_reflection_node_uuid)

    #################################################################################################
    # Dialog: ShadowHeart_InParty2_Nested_DefaultChapter.lsf
    #################################################################################################

    ab = game_assets.get_modded_dialog_asset_bundle('ShadowHeart_InParty2_Nested_DefaultChapter')
    d = bg3.dialog_object(ab.dialog)
    t = bg3.timeline_object(ab.timeline, d)

    speaker_idx_tav = d.get_speaker_slot_index(bg3.SPEAKER_PLAYER)

    tadpole_reflection_greeting_root_node_uuid = '4c476bf6-ef98-4379-9f13-02c7b2034f85'
    another_tadpole_node_uuid = '9a61a1d7-0d24-4de9-8a34-bdb5549e2ab7'
    not_sentimental_creatures_node_uuid = '798671fa-a9bd-47fa-aeeb-5c7ca8d0d854'
    all_the_more_reason_to_find_a_cure_node_uuid = '7901c2d3-f83b-4bf3-9ded-7b677dee0aaa'
    once_mines_out_node_uuid = 'a05985b5-5ddf-460e-bda7-3a35449dd750'
    it_was_curious_node_uuid = '375b540c-ecf4-409a-96c3-86bf0d96c8f8'
    theres_something_more_node_uuid = '4cfda2f1-b316-4e81-9fc8-bed9579d4b38'
    he_was_just_like_us_node_uuid = '270dd30e-ea12-45e7-a9e2-fab98dcd80c7'
    his_faith_in_the_absolute_node_uuid = '29b434e4-267c-4b15-8501-d3a2f1f37ca6'
    ill_be_glad_never_see_node_uuid = '3324e41f-29c3-49cb-bbd9-eceadf05845d'
    nor_i_node_uuid = '4695d25a-ed25-46d6-a993-7092fa411555'

    d.create_standard_dialog_node(
        tadpole_reflection_greeting_root_node_uuid,
        bg3.SPEAKER_PLAYER,
        [not_sentimental_creatures_node_uuid],
        None,
        checkflags = (
            bg3.flag_group('Global', (
                bg3.flag(ReallyShadowheart_Ext_V2_0_0_0.uuid, True, None),
            )),
            bg3.flag_group('Object', (
                bg3.flag(Reflection_Event_Tadpole.uuid, True, speaker_idx_tav),
            )),
        ),
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(Reflection_Event_Tadpole.uuid, False, speaker_idx_tav),
            )),
        ),
        root = True,
        constructor = bg3.dialog_object.GREETING)
    d.add_root_node(tadpole_reflection_greeting_root_node_uuid, 0)

    # Another day, another tadpole... What do you think about it?
    d.create_standard_dialog_node(
        another_tadpole_node_uuid,
        bg3.SPEAKER_PLAYER,
        [not_sentimental_creatures_node_uuid],
        bg3.text_content('hf49b812fg1f2eg46c2gb455ge345905c1677', 1),
        checkflags = (
            bg3.flag_group(bg3.flag_group.OBJECT, (
                bg3.flag(Reflection_Available_Tadpole.uuid, True, speaker_idx_tav),
            )),
            bg3.flag_group(bg3.flag_group.GLOBAL, (
                bg3.flag(ReallyShadowheart_Ext_V2_0_0_0.uuid, True, None),
                bg3.flag(bg3.FLAG_GOB_Orpheus_State_HadVoiceOfAbsoluteEvent, False, None),
            )),
        ),
        constructor = bg3.dialog_object.QUESTION)
    d.add_child_dialog_node(bg3.SHADOWHEART_THOUGHTS_QUESTION_BANK_NODE_UUID, another_tadpole_node_uuid, 0)

    # That tadpole wasted no time in abandoning its host. Not sentimental creatures, clearly.
    d.create_standard_dialog_node(
        not_sentimental_creatures_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [
            all_the_more_reason_to_find_a_cure_node_uuid,
            it_was_curious_node_uuid,
            ill_be_glad_never_see_node_uuid,
        ],
        bg3.text_content('h831e43bagcbc4g4cc8g8417g003c5595ba38', 1))
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '6.01',
        not_sentimental_creatures_node_uuid,
        (('6.1', '7b067edd-f53f-49e1-95bc-0986e6e2ca2f'), (None, 'e08db860-1e62-4271-bf4e-d51602468573')),
        phase_duration = '6.4',
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 32, None), (3.73, 1024, None))
        },
        attitudes = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_R_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, None),),
            bg3.SPEAKER_PLAYER: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_L_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, None),),
        })

    # These things live on even if we don't. All the more reason to find a cure.
    d.create_standard_dialog_node(
        all_the_more_reason_to_find_a_cure_node_uuid,
        bg3.SPEAKER_PLAYER,
        [once_mines_out_node_uuid],
        bg3.text_content('h856a7435gdde6g4c5ag8b26g95f10a46248a', 1),
        constructor = bg3.dialog_object.QUESTION)

    # Indeed. Once mine's out, I'm going to drop it in a lit brazier and watch it sizzle.
    d.create_standard_dialog_node(
        once_mines_out_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [],
        bg3.text_content('hcf09cbebg1f84g4297g9a44gd31ca6f4c688', 1),
        end_node = True)
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '6.01',
        once_mines_out_node_uuid,
        (('6.1', '7b067edd-f53f-49e1-95bc-0986e6e2ca2f'), (None, 'e08db860-1e62-4271-bf4e-d51602468573')),
        phase_duration = '6.4',
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 32, None), (3.73, 1024, None))
        },
        attitudes = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_R_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, None),),
            bg3.SPEAKER_PLAYER: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_L_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, None),),
        })

    # It was curious. Before he died, the host seemed oblivious to his tadpole.
    d.create_standard_dialog_node(
        it_was_curious_node_uuid,
        bg3.SPEAKER_PLAYER,
        [theres_something_more_node_uuid],
        bg3.text_content('h9662455dg33f3g4b04gac47g9c9068cf8465', 1),
        constructor = bg3.dialog_object.QUESTION)

    # Being delirious with pain will do that. But there's something more, I think.
    d.create_standard_dialog_node(
        theres_something_more_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [his_faith_in_the_absolute_node_uuid, he_was_just_like_us_node_uuid],
        bg3.text_content('hae77f3d2ge432g4d84gb48bg4a257f0af68b', 1))
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '4.61',
        theres_something_more_node_uuid,
        ((None, '7b067edd-f53f-49e1-95bc-0986e6e2ca2f'),),
        phase_duration = '4.91',
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 4, None), (3.37, 4, 2))
        },
        attitudes = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_R_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, None),),
            bg3.SPEAKER_PLAYER: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_L_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, None),),
        })

    # He was just like us, except for his faith in this 'Absolute'. There must be something to that.
    d.create_standard_dialog_node(
        he_was_just_like_us_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [],
        bg3.text_content('hf4a25891g8e13g424fgbe6dg6a4b404ed0d8', 1),
        end_node = True,
        checkflags = (
            bg3.flag_group('Global', (
                bg3.flag(bg3.FLAG_GLO_Absolute_Knows_Name, False, None),
            )),
        ))
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '6.18',
        he_was_just_like_us_node_uuid,
        (('6.18', 'e7f21f15-f386-40f4-bb0f-2f9f42249ad1'), (None, 'e08db860-1e62-4271-bf4e-d51602468573')),
        phase_duration = '6.5',
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 4, None), (3.16, 8, None))
        },
        attitudes = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_R_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, None),),
            bg3.SPEAKER_PLAYER: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_L_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, None),),
        })

    # His faith in the Absolute can't be a coincidence. The cult must be connected to all this somehow.
    d.create_standard_dialog_node(
        his_faith_in_the_absolute_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [],
        bg3.text_content('h65486df9g6439g4564gb7d4gab25a15a14a2', 1),
        end_node = True,
        checkflags = (
            bg3.flag_group('Global', (
                bg3.flag(bg3.FLAG_GLO_Absolute_Knows_Name, True, None),
            )),
        ))
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '6.18',
        his_faith_in_the_absolute_node_uuid,
        (('6.18', 'e7f21f15-f386-40f4-bb0f-2f9f42249ad1'), (None, 'e08db860-1e62-4271-bf4e-d51602468573')),
        phase_duration = '6.5',
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 8, None), (4.5, 4, None))
        },
        attitudes = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_R_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, None),),
            bg3.SPEAKER_PLAYER: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_L_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, None),),
        })

    # I'll be glad if I never have to see something like that again.
    d.create_standard_dialog_node(
        ill_be_glad_never_see_node_uuid,
        bg3.SPEAKER_PLAYER,
        [nor_i_node_uuid],
        bg3.text_content('h5edf3529g1778g487egac48g4e93a5dabb7e', 1),
        constructor = bg3.dialog_object.QUESTION)

    # Nor I. All the more reason to get these things out while we're still alive.
    d.create_standard_dialog_node(
        nor_i_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [],
        bg3.text_content('h4b384021g8fe1g4d0ag9b9fgd9d8d8b1b64a', 1),
        end_node = True,
        checkflags = (
            bg3.flag_group('Global', (
                bg3.flag(bg3.FLAG_GLO_Absolute_Knows_Name, True, None),
            )),
        ))
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '4.76',
        nor_i_node_uuid,
        (('4.76', 'e7f21f15-f386-40f4-bb0f-2f9f42249ad1'), (None, 'e08db860-1e62-4271-bf4e-d51602468573')),
        phase_duration = '5.0',
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 4, None), (3.0, 8, None))
        },
        attitudes = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_R_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, None),),
            bg3.SPEAKER_PLAYER: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_L_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, None),),
        })


def create_bugbear_ogre_reaction() -> None:
    #################################################################################################
    # Dialog: ShadowHeart_InParty2.lsf
    #################################################################################################

    ab = game_assets.get_modded_dialog_asset_bundle('ShadowHeart_InParty')
    d = bg3.dialog_object(ab.dialog)

    speaker_idx_tav = d.get_speaker_slot_index(bg3.SPEAKER_PLAYER)

    topical_greetings_node_uuid = 'dfec2c3c-2397-ff26-ef9e-09ad12d81b9f' # existing root node

    bugbear_ogre_reflection_node_uuid = 'cfdef77e-4346-4036-8464-de5ce97fe5ee'

    # reused node from putrid bog reflection
    nested_dialog_node_uuid = 'e2e11f4c-de6a-41af-9d83-623c2abdbdac'

    d.create_standard_dialog_node(
        bugbear_ogre_reflection_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [nested_dialog_node_uuid],
        None,
        checkflags = (
            bg3.flag_group('Global', (
                bg3.flag(ReallyShadowheart_Ext_V2_0_0_0.uuid, True, None),
            )),
            bg3.flag_group('Object', (
                bg3.flag(Reflection_Event_Bugbear_Love.uuid, True, speaker_idx_tav),
            )),
        ),
        constructor = bg3.dialog_object.GREETING,
        root = True)
    d.add_root_node_before(topical_greetings_node_uuid, bugbear_ogre_reflection_node_uuid)

    #################################################################################################
    # Dialog: ShadowHeart_InParty2_Nested_DefaultChapter.lsf
    #################################################################################################

    ab = game_assets.get_modded_dialog_asset_bundle('ShadowHeart_InParty2_Nested_DefaultChapter')
    d = bg3.dialog_object(ab.dialog)
    t = bg3.timeline_object(ab.timeline, d)

    speaker_idx_tav = d.get_speaker_slot_index(bg3.SPEAKER_PLAYER)

    
    bugbear_reflection_greeting_root_node_uuid = 'c3526856-b896-4093-9a2c-93e4365bc47a'
    you_dont_seem_impressed_node_uuid = '78614cb8-fbc6-460c-95d8-abbb0a8ee577'
    that_was_unnecessary_node_uuid = 'ba530c21-e43c-4eef-bfa6-b1f2e56349d6'
    more_smoothly_node_uuid = '7aff20c2-8aa3-4eaf-80ce-c12b5e104f41'
    those_creatures_would_agree_node_uuid = '5f8f9422-cc65-4440-b332-2f828cb90ad0'
    potential_threat_node_uuid = 'e872ecb1-f5e9-4e2b-a4c7-e7d7415a5b95'
    made_potential_threat_into_a_certain_one_node_uuid = '004c758a-ddc3-4a0b-9cf2-76b6e19b31ea'
    such_a_rare_sight_node_uuid = '050981fd-b283-42a8-976b-04c3d8c9fb17'
    very_unhealthy_node_uuid = 'ad2f40b9-0fe6-49b1-8515-bf0dc006ea2c'

    d.create_standard_dialog_node(
        bugbear_reflection_greeting_root_node_uuid,
        bg3.SPEAKER_PLAYER,
        [that_was_unnecessary_node_uuid],
        None,
        checkflags = (
            bg3.flag_group('Global', (
                bg3.flag(ReallyShadowheart_Ext_V2_0_0_0.uuid, True, None),
            )),
            bg3.flag_group('Object', (
                bg3.flag(Reflection_Event_Bugbear_Love.uuid, True, speaker_idx_tav),
            )),
        ),
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(Reflection_Event_Bugbear_Love.uuid, False, speaker_idx_tav),
            )),
        ),
        root = True,
        constructor = bg3.dialog_object.GREETING)
    d.add_root_node(bugbear_reflection_greeting_root_node_uuid, 0)

    # When I opened the barn door, I didn't expect to see that.
    d.create_standard_dialog_node(
        you_dont_seem_impressed_node_uuid,
        bg3.SPEAKER_PLAYER,
        [that_was_unnecessary_node_uuid],
        bg3.text_content('he87e92c1g8accg4a03g845fgdb5b0e8080aa', 1),
        checkflags = (
            bg3.flag_group(bg3.flag_group.OBJECT, (
                bg3.flag(Reflection_Available_Bugbear_Love.uuid, True, speaker_idx_tav),
            )),
            bg3.flag_group(bg3.flag_group.GLOBAL, (
                bg3.flag(ReallyShadowheart_Ext_V2_0_0_0.uuid, True, None),
                bg3.flag(bg3.FLAG_VISITEDREGION_CRE_Main_A, False, None),
                bg3.flag(bg3.FLAG_VISITEDREGION_SCL_Main_A_ACT_2, False, None),
            )),
        ),
        constructor = bg3.dialog_object.QUESTION)
    d.add_child_dialog_node(bg3.SHADOWHEART_THOUGHTS_QUESTION_BANK_NODE_UUID, you_dont_seem_impressed_node_uuid, 0)

    # Well that was unnecessary. Were you jealous of them or something?
    d.create_standard_dialog_node(
        that_was_unnecessary_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [more_smoothly_node_uuid, potential_threat_node_uuid, such_a_rare_sight_node_uuid],
        bg3.text_content('hbf861642g0d92g4352gad62g4287fd50647a', 1))
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '3.8',
        that_was_unnecessary_node_uuid,
        (('3.8', 'e7f21f15-f386-40f4-bb0f-2f9f42249ad1'), (None, 'e08db860-1e62-4271-bf4e-d51602468573')),
        phase_duration = '4.2',
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.2, 1024, 1), (2.51, 4, None))
        },
        attitudes = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, bg3.ATTITUDE_DIAG_Pose_Crossed_01, bg3.ATTITUDE_DIAG_T_Pose, None),),
            bg3.SPEAKER_PLAYER: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_L_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, None),),
        })

    # Things could have gone more smoothly, yes.
    d.create_standard_dialog_node(
        more_smoothly_node_uuid,
        bg3.SPEAKER_PLAYER,
        [those_creatures_would_agree_node_uuid],
        bg3.text_content('h4cb3264fg5f97g4c96g8552g9b5a2213d005', 1),
        constructor = bg3.dialog_object.QUESTION)

    # I'm sure those creatures would agree with you on that. 
    d.create_standard_dialog_node(
        those_creatures_would_agree_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [],
        bg3.text_content('h83c8b7f5g7292g4c84g8addg588ee713f5aa', 1),
        end_node = True)
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '2.55',
        those_creatures_would_agree_node_uuid,
        (('2.8', '7b067edd-f53f-49e1-95bc-0986e6e2ca2f'), (None, 'e08db860-1e62-4271-bf4e-d51602468573')),
        phase_duration = '2.9',
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 8, None), (1.5, 4, None))
        },
        attitudes = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_R_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, None),),
            bg3.SPEAKER_PLAYER: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_L_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, None),),
        })


    reaction_minus_1 = bg3.reaction_object.create_new(game_assets.files, { bg3.SPEAKER_SHADOWHEART: -1 }, uuid = 'fe45b697-352d-4e80-a7c6-083e9182a1ec')
    # It would have been foolish to ignore a potential threat.
    d.create_standard_dialog_node(
        potential_threat_node_uuid,
        bg3.SPEAKER_PLAYER,
        [made_potential_threat_into_a_certain_one_node_uuid],
        bg3.text_content('h927af267gfab5g4691g9bbdg32d2b405bfb8', 1),
        approval_rating_uuid = reaction_minus_1.uuid,
        constructor = bg3.dialog_object.QUESTION)

    # You made a potential threat into a certain one. We don't need to pick every fight.
    d.create_standard_dialog_node(
        made_potential_threat_into_a_certain_one_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [],
        bg3.text_content('hb3c79bdcg467cg4776gb804g7a8aa9832db7', 1),
        end_node = True)
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '4.98',
        made_potential_threat_into_a_certain_one_node_uuid,
        (('5.1', '7b067edd-f53f-49e1-95bc-0986e6e2ca2f'), (None, 'e08db860-1e62-4271-bf4e-d51602468573')),
        phase_duration = '5.3',
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.2, 8, None), (2.08, 8, 2), (3.45, 8, 1), (4.28, 8, None))
        },
        attitudes = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_R_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, None),),
            bg3.SPEAKER_PLAYER: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_L_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, None),),
        })

    # We're lucky to have witnessed such a rare sight. A little curiosity is healthy.
    d.create_standard_dialog_node(
        such_a_rare_sight_node_uuid,
        bg3.SPEAKER_PLAYER,
        [very_unhealthy_node_uuid],
        bg3.text_content('hd3f708efg982bg4a07gbd98gd0fcf63c983d', 1),
        constructor = bg3.dialog_object.QUESTION)

    # Your curiosity could've turned very unhealthy if that fight hadn't gone our way.
    d.create_standard_dialog_node(
        very_unhealthy_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [],
        bg3.text_content('hc728d156g3656g4640g8dbbgd777c2be4e79', 1),
        approval_rating_uuid = reaction_minus_1.uuid,
        end_node = True)
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '4.7',
        very_unhealthy_node_uuid,
        (('5.0', '7b067edd-f53f-49e1-95bc-0986e6e2ca2f'), (None, 'e08db860-1e62-4271-bf4e-d51602468573')),
        phase_duration = '5.1',
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 8, None), (2.0, 8, 1), (2.74, 8, 2), (4.17, 8, None))
        },
        attitudes = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_R_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, None),),
            bg3.SPEAKER_PLAYER: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_L_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, None),),
        })

bg3.add_build_procedure('create_tadpole_reaction', create_tadpole_reaction)
bg3.add_build_procedure('create_bugbear_ogre_reaction', create_bugbear_ogre_reaction)

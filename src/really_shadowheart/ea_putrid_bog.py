from __future__ import annotations

import bg3moddinglib as bg3

from .context import game_assets
from .dialog_overrides import add_dialog_dependency, get_dialog_uuid
from .flags import *

#################################################################################################
# Encounter with Gandrel in the putrid bog, this adds protected/betrayed flags to dialog nodes
#################################################################################################

#################################################################################################
# Dialog: HAG_GurHunter_OM_Astarion_COM.lsf
#################################################################################################

def create_conversation_gur_monster_hunter_putrid_bog() -> None:

    # d = bg3.dialog_object(files.get_file('Gustav', 'Mods/Gustav/Story/DialogsBinary/Companions/Origin_Moments/HAG_GurHunter_OM_Astarion_COM.lsf'))
    ab = game_assets.get_modded_dialog_asset_bundle('HAG_GurHunter_OM_Astarion_COM')
    d = bg3.dialog_object(ab.dialog)

    speaker_idx_tav = d.get_speaker_slot_index(bg3.SPEAKER_PLAYER)

    protected_nodes_uuids = [
        'dfa4762d-2100-ae80-5ac3-629e4464f365',
        'd0a16028-f670-d9d2-9c1f-0de5fd26ab07',
        'af0ed688-ef1a-889a-20f8-7ad55a5da244',
        'f985ad20-ff14-60b4-f7df-3d61486f0dea',
        'c0801fdd-e892-02cc-1699-d5ba15e35ffa',
        '6836ff29-ee6c-2ae2-c776-8f1cf51445e8',
        '6a62689b-808c-9857-d533-3ea53adb9d58',
        '24ae4154-9ea3-6dc3-0cb6-713325e5b008',
        '0e357a0b-bb60-c257-4d6a-b6257f891d6f'
    ]

    betrayed_nodes_uuids = [
        '6e7f7075-77ca-92f0-12fd-76693cac464d',
        '44d6bbae-099d-0bf8-640d-af099034e006',
    ]

    for node_uuid in protected_nodes_uuids:
        d.set_dialog_flags(node_uuid, setflags=(
            bg3.flag_group(bg3.flag_group.GLOBAL, (
                bg3.flag(Tav_Protected_Astarion.uuid, True, speaker_idx_tav),
                bg3.flag(Tav_Betrayed_Astarion.uuid, False, speaker_idx_tav),
                bg3.flag(Reflection_Available_Gur_Hunter.uuid, True, speaker_idx_tav),
                bg3.flag(Reflection_Event_Gur_Hunter.uuid, True, speaker_idx_tav),
            )),
        ))

    for node_uuid in betrayed_nodes_uuids:
        d.set_dialog_flags(node_uuid, setflags=(
            bg3.flag_group(bg3.flag_group.GLOBAL, (
                bg3.flag(Tav_Protected_Astarion.uuid, False, speaker_idx_tav),
                bg3.flag(Tav_Betrayed_Astarion.uuid, True, speaker_idx_tav),
                bg3.flag(Reflection_Available_Gur_Hunter.uuid, True, speaker_idx_tav),
                bg3.flag(Reflection_Event_Gur_Hunter.uuid, True, speaker_idx_tav),
            )),
        ))


    #################################################################################################
    # Dialog: HAG_GurHunter.lsf
    #################################################################################################

    # d = bg3.dialog_object(files.get_file('Gustav', 'Mods/Gustav/Story/DialogsBinary/Act1/Swamp/HAG_GurHunter.lsf'))
    ab = game_assets.get_modded_dialog_asset_bundle('HAG_GurHunter')
    d = bg3.dialog_object(ab.dialog)

    speaker_idx_tav = d.get_speaker_slot_index(bg3.SPEAKER_PLAYER)

    protected_nodes_uuids = [
        '46b4329d-6ad9-0731-92a4-04f476976020',
        '75c501e8-f14e-50fe-345a-5215a96b41f9',
        '67f1947a-1ab7-c258-0154-c281e044dce6',
        'd5038649-4a25-e499-a298-40880a5fb433',
        'fe4cdf90-da1a-fbd9-d4df-f3b0df3f4925',
        '7d6a00cb-51c6-98ef-8b25-4f5b12430d44'
    ]

    betrayed_nodes_uuids = [
        '22ea2855-1463-001b-e0aa-334962d5af64',
        '6433cf07-496a-e117-b4bb-64c28f2d26cb'
    ]

    for node_uuid in protected_nodes_uuids:
        d.set_dialog_flags(node_uuid, setflags=(
            bg3.flag_group(bg3.flag_group.OBJECT, (
                bg3.flag(Tav_Protected_Astarion.uuid, True, speaker_idx_tav),
                bg3.flag(Tav_Betrayed_Astarion.uuid, False, speaker_idx_tav),
                bg3.flag(Reflection_Available_Gur_Hunter.uuid, True, speaker_idx_tav),
                bg3.flag(Reflection_Event_Gur_Hunter.uuid, True, speaker_idx_tav),
            )),
        ))

    for node_uuid in betrayed_nodes_uuids:
        d.set_dialog_flags(node_uuid, setflags=(
            bg3.flag_group(bg3.flag_group.OBJECT, (
                bg3.flag(Tav_Protected_Astarion.uuid, False, speaker_idx_tav),
                bg3.flag(Tav_Betrayed_Astarion.uuid, True, speaker_idx_tav),
                bg3.flag(Reflection_Available_Gur_Hunter.uuid, True, speaker_idx_tav),
                bg3.flag(Reflection_Event_Gur_Hunter.uuid, True, speaker_idx_tav),
            )),
        ))

    #################################################################################################
    # Dialog: ShadowHeart_InParty2.lsf
    #################################################################################################

    ab = game_assets.get_modded_dialog_asset_bundle('ShadowHeart_InParty')
    d = bg3.dialog_object(ab.dialog)

    speaker_idx_tav = d.get_speaker_slot_index(bg3.SPEAKER_PLAYER)

    topical_greetings_node_uuid = 'dfec2c3c-2397-ff26-ef9e-09ad12d81b9f' # existing root node

    gur_putrid_bog_reflection_node_uuid = 'ee271dc6-27cb-4439-baca-33963c21001e'
    nested_dialog_node_uuid = 'e2e11f4c-de6a-41af-9d83-623c2abdbdac'
    end_node_uuid = '533b79ed-15dc-4cac-804b-fd7edd64673e'
    jump_to_question_bank_node_uuid = '09e3d4bf-262f-4f6c-9d1b-6089edf6e0e8'
    d.create_standard_dialog_node(
        gur_putrid_bog_reflection_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [nested_dialog_node_uuid],
        None,
        checkflags = (
            bg3.flag_group('Global', (
                bg3.flag(ReallyShadowheart_Ext_V2_0_0_0.uuid, True, None),
            )),
            bg3.flag_group('Object', (
                bg3.flag(Reflection_Event_Gur_Hunter.uuid, True, speaker_idx_tav),
            )),
        ),
        constructor = bg3.dialog_object.GREETING,
        root = True)
    d.add_root_node_before(topical_greetings_node_uuid, gur_putrid_bog_reflection_node_uuid)

    nested_dialog_uuid = get_dialog_uuid('ShadowHeart_InParty2_Nested_DefaultChapter')
    d.create_nested_dialog_node(
        nested_dialog_node_uuid,
        nested_dialog_uuid,
        [end_node_uuid, jump_to_question_bank_node_uuid],
        speaker_count = 7)
    add_dialog_dependency(ab, nested_dialog_node_uuid)
    d.create_standard_dialog_node(
        end_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [],
        None,
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_Shadowheart_InParty_State_EndDialog, True, speaker_idx_tav),
            )),
        ),
        end_node = True)
    d.create_jump_dialog_node(jump_to_question_bank_node_uuid, bg3.SHADOWHEART_QUESTION_BANK_ROOT_NODE_UUID, 2)


    #################################################################################################
    # Dialog: ShadowHeart_InParty2_Nested_DefaultChapter.lsf
    #################################################################################################

    # d = bg3.dialog_object(files.get_file('Gustav', 'Mods/GustavDev/Story/DialogsBinary/Companions/ShadowHeart_InParty2_Nested_DefaultChapter.lsf'))
    # t = bg3.timeline_object(files.get_file('Gustav', 'Public/GustavDev/Timeline/Generated/ShadowHeart_InParty2_Nested_DefaultChapter.lsf'), d)

    ab = game_assets.get_modded_dialog_asset_bundle('ShadowHeart_InParty2_Nested_DefaultChapter')
    d = bg3.dialog_object(ab.dialog)
    t = bg3.timeline_object(ab.timeline, d)

    speaker_idx_tav = d.get_speaker_slot_index(bg3.SPEAKER_PLAYER)
    speaker_idx_shadowheart = d.get_speaker_slot_index(bg3.SPEAKER_SHADOWHEART)

    gur_hunter_reflection_greeting_root_node_uuid = '5cedd2d3-9bf3-404a-b093-02f351a22c02'
    what_do_you_make_of_our_encounter_node_uuid = '4654bc7c-ac9a-4351-aa74-9370075aac6a'

    im_a_little_surprised_node_uuid = '79071ea4-3722-4a1d-9856-07e8487524bb'
    hes_one_of_us_node_uuid = '8540671a-9877-4e44-8370-e8e82aeb1796'
    how_adorable_node_uuid = '568c8ed8-939a-443c-8548-f22e7034e709'
    youre_as_loyal_as_a_pup_and_twice_as_handsome_node_uuid = 'b5672ea7-9093-e82d-5b87-bee7b48bbdf6'
    youre_as_loyal_as_a_pup_and_twice_as_pretty_node_uuid = '80965aba-cc3d-45d0-bac0-30d6d30034c5'
    youre_as_loyal_as_a_pup_and_twice_as_charming_node_uuid = '28f07d7b-f8a5-4eae-9af4-dba6261edc58'
    he_knows_too_much_node_uuid = 'b6c92aa7-6b07-7a52-a553-9a283b30bc32'
    very_strategic_of_you_node_uuid = '95445707-07c8-af8b-7d3b-3980eb4ffcce'
    i_hope_i_dont_come_to_regret_node_uuid = '4aead3ff-33fb-484a-bbf5-0d9fea92d42c'
    you_can_always_rid_yourself_of_that_regret_node_uuid = '7b189788-4a3c-44dd-8b2f-225bf9088127'

    vampire_spawn_or_not_node_uuid = 'bb73eb24-1254-4157-be22-28f1af2af0a4'
    it_was_the_sensible_choice_node_uuid = 'd7260432-ba24-4717-9c0e-b9794be66767'
    quite_harsh_of_you_node_uuid = '60c1a039-a937-49ea-9d48-c0b116be778d'
    what_would_you_have_done_node_uuid = '93f7d010-ff5f-2a3d-6017-164bf82324bc'
    i_can_maintain_deniability_node_uuid = '40f7b676-2126-72d2-7f48-c2b5b921e44e'
    at_risk_of_fracturing_node_uuid = 'aa49f595-23f3-e121-4fbe-51ea6f57cb1a'
    you_dont_approve_node_uuid = '48918991-fc56-4de7-9b99-17992a3c330b'
    i_havent_decided_yet_node_uuid = 'add5d880-72f6-48d4-b5c9-0c1da7ae9909'
    i_just_hope_node_uuid = '14863dc8-18c4-c3e2-02d6-85bfcc2c2d8e'

    d.create_standard_dialog_node(
        gur_hunter_reflection_greeting_root_node_uuid,
        bg3.SPEAKER_PLAYER,
        [im_a_little_surprised_node_uuid, vampire_spawn_or_not_node_uuid],
        None,
        checkflags = (
            bg3.flag_group('Global', (
                bg3.flag(ReallyShadowheart_Ext_V2_0_0_0.uuid, True, None),
            )),
            bg3.flag_group('Object', (
                bg3.flag(Reflection_Event_Gur_Hunter.uuid, True, speaker_idx_tav),
            )),
        ),
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(Reflection_Event_Gur_Hunter.uuid, False, speaker_idx_tav),
            )),
        ),
        root = True,
        constructor = bg3.dialog_object.GREETING)
    d.add_root_node(gur_hunter_reflection_greeting_root_node_uuid, 0)

    d.add_child_dialog_node(bg3.SHADOWHEART_THOUGHTS_QUESTION_BANK_NODE_UUID, what_do_you_make_of_our_encounter_node_uuid, 0)

    # What do you make of our encounter with the Gur monster hunter?
    d.create_standard_dialog_node(
        what_do_you_make_of_our_encounter_node_uuid,
        bg3.SPEAKER_PLAYER,
        [im_a_little_surprised_node_uuid, vampire_spawn_or_not_node_uuid],
        bg3.text_content('h8b4751f2g4391g412dg8f63gc05bf8c67056', 1),
        constructor = bg3.dialog_object.QUESTION,
        checkflags = (
            bg3.flag_group(bg3.flag_group.OBJECT, (
                bg3.flag(Reflection_Available_Gur_Hunter.uuid, True, speaker_idx_tav),
            )),
            bg3.flag_group(bg3.flag_group.GLOBAL, (
                bg3.flag(ReallyShadowheart_Ext_V2_0_0_0.uuid, True, None),
                bg3.flag(bg3.FLAG_VISITEDREGION_SCL_Main_A_ACT_2, False, None),
            )),
        ))

    # d76eaab3-040b-4871-9c1d-4a8624f37cd2 Shadowheart
    # 0e8837db-4344-48d0-9175-12262c73806b Shadowheart
    # b4155335-5e08-4d85-8ccd-ddebf5507447 Shadowheart -> Tav
    # a5043f00-72f3-49fe-a24f-fce1e268d896 Shadowheart -> Tav
    # e08db860-1e62-4271-bf4e-d51602468573 Shadowheart -> Tav
    # e7f21f15-f386-40f4-bb0f-2f9f42249ad1 Tav -> Shadowheart
    # 7b067edd-f53f-49e1-95bc-0986e6e2ca2f Tav -> Shadowheart

    # Vampire spawn or not, I didn't think you'd just surrender Astarion like that.
    d.create_standard_dialog_node(
        vampire_spawn_or_not_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [it_was_the_sensible_choice_node_uuid, what_would_you_have_done_node_uuid, you_dont_approve_node_uuid],
        bg3.text_content('h1ab20829g3b5ag4bd4g8cb8gf2a2d129d9d5', 1),
        constructor = bg3.dialog_object.ANSWER,
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(Tav_Protected_Astarion.uuid, False, speaker_idx_tav),
                bg3.flag(Tav_Betrayed_Astarion.uuid, True, speaker_idx_tav),
            )),
        ))
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '4.93',
        vampire_spawn_or_not_node_uuid,
        (('4.93', 'e7f21f15-f386-40f4-bb0f-2f9f42249ad1'), (None, 'e08db860-1e62-4271-bf4e-d51602468573')),
        phase_duration = '5.3',
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 4, 2), (1.33, 4, None), (3.41, 64, None)),
            bg3.SPEAKER_PLAYER: ((0.0, 1, None),)
        },
        attitudes = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_R_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, None),),
            bg3.SPEAKER_PLAYER: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_L_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, None),),
        })

    # It was the sensible choice. We've enough dangerous parasites in our midst already.
    d.create_standard_dialog_node(
        it_was_the_sensible_choice_node_uuid,
        bg3.SPEAKER_PLAYER,
        [quite_harsh_of_you_node_uuid],
        bg3.text_content('h4a382af4g128bg427dg8534g0d70b37f629b', 1),
        constructor=bg3.dialog_object.QUESTION)

    # Quite harsh of you. I can't say I entirely disagree, but still... quite harsh.
    d.create_standard_dialog_node(
        quite_harsh_of_you_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [],
        bg3.text_content('hb29103d5gb3e9g4917ga0bagda2d1225c7d2', 1),
        constructor = bg3.dialog_object.ANSWER,
        end_node = True)
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '6.43',
        quite_harsh_of_you_node_uuid,
        (('6.43', '7b067edd-f53f-49e1-95bc-0986e6e2ca2f'), (None, 'e08db860-1e62-4271-bf4e-d51602468573')),
        phase_duration = '6.8',
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 4, 2), (0.65, 64, None), (1.18, 4, None), (1.94, 1024, None), (4.23, 64, None), (5.27, 4, 2)),
            bg3.SPEAKER_PLAYER: ((0.0, 1, None),)
        },
        attitudes = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_R_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, None),),
            bg3.SPEAKER_PLAYER: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_L_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, None),),
        })

    # What would you have done?
    d.create_standard_dialog_node(
        what_would_you_have_done_node_uuid,
        bg3.SPEAKER_PLAYER,
        [i_can_maintain_deniability_node_uuid],
        bg3.text_content('h60393557ge940g4f75gae59g969fde0c36e7', 1),
        constructor=bg3.dialog_object.QUESTION)

    # That'd be telling, wouldn't it? If he escapes and comes seeking vengeance, I can maintain deniability.
    d.create_standard_dialog_node(
        i_can_maintain_deniability_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [at_risk_of_fracturing_node_uuid],
        bg3.text_content('h99f44e71gc3d2g497dg9fe5ge2fc5c4b675e', 1),
        constructor = bg3.dialog_object.ANSWER)
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '6.88',
        i_can_maintain_deniability_node_uuid,
        ((None, '7b067edd-f53f-49e1-95bc-0986e6e2ca2f'),),
        phase_duration = '7.2',
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 1024, None), (2.45, 64, None), (4.78, 4, None)),
            bg3.SPEAKER_PLAYER: ((0.0, 1, None),)
        },
        attitudes = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_R_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, None),),
            bg3.SPEAKER_PLAYER: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_L_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, None),),
        })

    # If our group's at risk of fracturing, I'll have to do what's best for myself, naturally.
    d.create_standard_dialog_node(
        at_risk_of_fracturing_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [],
        bg3.text_content('hd54b5683gb8a9g4232g8f71gf21b8d96397e', 1),
        constructor = bg3.dialog_object.ANSWER,
        end_node = True)
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '3.88',
        at_risk_of_fracturing_node_uuid,
        (('3.9', '0e8837db-4344-48d0-9175-12262c73806b'), (None, 'e08db860-1e62-4271-bf4e-d51602468573')),
        phase_duration = '4.2',
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 4, 2), (1.55, 2048, None), (3.33, 4, 1)),
            bg3.SPEAKER_PLAYER: ((0.0, 1, None),)
        },
        attitudes = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_R_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, None),),
            bg3.SPEAKER_PLAYER: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_L_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, None),),
        })

    # I take it you don't approve?
    d.create_standard_dialog_node(
        you_dont_approve_node_uuid,
        bg3.SPEAKER_PLAYER,
        [i_havent_decided_yet_node_uuid],
        bg3.text_content('h99103040gfa01g4119g923egaf4365f8d6d6', 1),
        constructor=bg3.dialog_object.QUESTION)

    # I haven't decided yet. Seems prudent, on one hand, but on the other... he was one of us.
    d.create_standard_dialog_node(
        i_havent_decided_yet_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [i_just_hope_node_uuid],
        bg3.text_content('haad868c6gd546g4dcdgaeecg15bab803e58d', 1),
        constructor = bg3.dialog_object.ANSWER)
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '6.1',
        i_havent_decided_yet_node_uuid,
        ((None, '7b067edd-f53f-49e1-95bc-0986e6e2ca2f'),),
        phase_duration = '6.5',
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 4, 2), (1.92, 4, None), (3.89, 4, 1), (5.44, 4, None)),
            bg3.SPEAKER_PLAYER: ((0.0, 1, None),)
        },
        attitudes = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_R_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, None),),
            bg3.SPEAKER_PLAYER: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_L_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, None),),
        })

    # I just hope you don't find it as easy to cut ties with me, if the opportunity presents itself.
    d.create_standard_dialog_node(
        i_just_hope_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [],
        bg3.text_content('hf066fcc5g3d75g4716g9a70gea598ae4b2ae', 1),
        constructor = bg3.dialog_object.ANSWER,
        end_node = True)
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '4.94',
        i_just_hope_node_uuid,
        (('5.0', '0e8837db-4344-48d0-9175-12262c73806b'), (None, 'e08db860-1e62-4271-bf4e-d51602468573')),
        phase_duration = '5.4',
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 4, None), (1.14, 2048, None), (2.61, 64, None), (3.02, 4, 2), (4.39, 8, None)),
            bg3.SPEAKER_PLAYER: ((0.0, 1, None),)
        },
        attitudes = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_R_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, None),),
            bg3.SPEAKER_PLAYER: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_L_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, None),),
        })

    # Speaking truthfully, I'm a little surprised you chose to shield Astarion.
    d.create_standard_dialog_node(
        im_a_little_surprised_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [hes_one_of_us_node_uuid, he_knows_too_much_node_uuid, '4aead3ff-33fb-484a-bbf5-0d9fea92d42c'],
        bg3.text_content('hb3033ad0gf4d6g41d7gba68gab137658a56a', 1),
        constructor = bg3.dialog_object.ANSWER,
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(Tav_Protected_Astarion.uuid, True, speaker_idx_tav),
                bg3.flag(Tav_Betrayed_Astarion.uuid, False, speaker_idx_tav),
            )),
        ))
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '4.461',
        im_a_little_surprised_node_uuid,
        (('4.5', '7b067edd-f53f-49e1-95bc-0986e6e2ca2f'), (None, 'e08db860-1e62-4271-bf4e-d51602468573')),
        phase_duration = '4.8',
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 4, None), (1.89, 4, 1), (3.19, 4, None)),
            bg3.SPEAKER_PLAYER: ((0.0, 1, None),)
        },
        attitudes = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_R_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, None),),
            bg3.SPEAKER_PLAYER: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_L_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, None),),
        })

    reaction_plus_1 = bg3.reaction_object.create_new(game_assets.files, { bg3.SPEAKER_SHADOWHEART: 1 }, uuid = '3d0fecb6-049f-4014-a374-701171dbd765')

    # He's one of us. I wasn't about to just betray him.
    d.create_standard_dialog_node(
        hes_one_of_us_node_uuid,
        bg3.SPEAKER_PLAYER,
        [how_adorable_node_uuid],
        bg3.text_content('hfc1897b2g015ag4589gbe29gff4cf74aff01', 1),
        constructor=bg3.dialog_object.QUESTION)

    # How adorable. Such camaraderie at such a bargain rate.
    d.create_standard_dialog_node(
        how_adorable_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [
            youre_as_loyal_as_a_pup_and_twice_as_handsome_node_uuid,
            youre_as_loyal_as_a_pup_and_twice_as_pretty_node_uuid,
            youre_as_loyal_as_a_pup_and_twice_as_charming_node_uuid
        ],
        bg3.text_content('h56359b73gb29ag4f19gbcd0gcd15a66d30f6', 1),
        constructor=bg3.dialog_object.ANSWER)
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '4.368',
        how_adorable_node_uuid,
        ((None, 'e7f21f15-f386-40f4-bb0f-2f9f42249ad1'),),
        phase_duration = '4.6',
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.5, 16, None), (1.77, 16, 1), (2.83, 32, None), (3.79, 2048, None))
        },
        attitudes = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_R_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, None),),
            bg3.SPEAKER_PLAYER: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_L_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, None),),
        })


    # You're as loyal as a pup and twice as handsome.
    d.create_standard_dialog_node(
        youre_as_loyal_as_a_pup_and_twice_as_handsome_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [],
        bg3.text_content('h18a8a0c7g2147g42beg8a5fgdedc6b33b731', 1),
        checkflags = (
            bg3.flag_group('Tag', (
                (bg3.flag(bg3.TAG_MALE, True, speaker_idx_tav)),
            )),
        ),
        constructor=bg3.dialog_object.ANSWER,
        approval_rating_uuid = reaction_plus_1.uuid,
        end_node=True)
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '3.224',
        youre_as_loyal_as_a_pup_and_twice_as_handsome_node_uuid,
        (('3.5', 'd76eaab3-040b-4871-9c1d-4a8624f37cd2'), (None, 'b4155335-5e08-4d85-8ccd-ddebf5507447')),
        phase_duration = '3.8',
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.61, 16, None), (1.2, 4, None), (2.06, 16, None), (2.95, 64, None)),
            bg3.SPEAKER_PLAYER: ((0.0, 64, None),)
        },
        attitudes = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_R_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, None),),
            bg3.SPEAKER_PLAYER: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_L_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, None),),
        })


    # You're as loyal as a pup and twice as pretty.
    d.create_standard_dialog_node(
        youre_as_loyal_as_a_pup_and_twice_as_pretty_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [],
        bg3.text_content('haab6ee84g0a04g403dga445g5d9e7088377b', 1),
        checkflags = (
            bg3.flag_group('Tag', (
                (bg3.flag(bg3.TAG_FEMALE, True, speaker_idx_tav)),
            )),
        ),
        constructor=bg3.dialog_object.ANSWER,
        approval_rating_uuid = reaction_plus_1.uuid,
        end_node=True)
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '3.379',
        youre_as_loyal_as_a_pup_and_twice_as_pretty_node_uuid,
        (('3.5', 'd76eaab3-040b-4871-9c1d-4a8624f37cd2'), (None, 'b4155335-5e08-4d85-8ccd-ddebf5507447')),
        phase_duration = '3.8',
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.61, 16, None), (1.2, 4, None), (2.06, 16, None), (2.95, 64, None)),
            bg3.SPEAKER_PLAYER: ((0.0, 64, None),)
        },
        attitudes = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_R_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, None),),
            bg3.SPEAKER_PLAYER: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_L_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, None),),
        })


    # You're as loyal as a pup and twice as charming.
    d.create_standard_dialog_node(
        youre_as_loyal_as_a_pup_and_twice_as_charming_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [],
        bg3.text_content('h3ce42409g98f5g4c9bgaf28ge161d5015c0a', 1),
        constructor=bg3.dialog_object.ANSWER,
        approval_rating_uuid = reaction_plus_1.uuid,
        end_node=True)
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '3.306',
        youre_as_loyal_as_a_pup_and_twice_as_charming_node_uuid,
        (('3.5', 'd76eaab3-040b-4871-9c1d-4a8624f37cd2'), (None, 'b4155335-5e08-4d85-8ccd-ddebf5507447')),
        phase_duration = '3.8',
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.61, 16, None), (1.2, 4, None), (2.06, 16, None), (2.95, 64, None)),
            bg3.SPEAKER_PLAYER: ((0.0, 64, None),)
        },
        attitudes = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_R_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, None),),
            bg3.SPEAKER_PLAYER: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_L_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, None),),
        })


    # He knows too much - safer to keep him with us than risk him exposing our condition.
    d.create_standard_dialog_node(
        he_knows_too_much_node_uuid,
        bg3.SPEAKER_PLAYER,
        [very_strategic_of_you_node_uuid],
        bg3.text_content('hc1913f71g45e1g4388g9a08gbbef9784d018', 1),
        constructor=bg3.dialog_object.QUESTION)

    # Very strategic of you, actually. Hopefully keeping him in our midst proves to be the lesser risk.
    d.create_standard_dialog_node(
        very_strategic_of_you_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [],
        bg3.text_content('hf78f63ffg0e44g4359ga02cg205cb18ab600', 1),
        constructor=bg3.dialog_object.ANSWER,
        end_node=True)
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '6.510',
        very_strategic_of_you_node_uuid,
        (('6.6', '0e8837db-4344-48d0-9175-12262c73806b'), (None, 'a5043f00-72f3-49fe-a24f-fce1e268d896')),
        phase_duration = '7.0',
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.4, 16, None), (1.51, 4, None), (2.8, 4, 1), (4.66, 16, None)),
            bg3.SPEAKER_PLAYER: ((0.0, 16, None),)
        },
        attitudes = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_R_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, None),),
            bg3.SPEAKER_PLAYER: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_L_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, None),),
        })


    # I just hope I don't come to regret standing by him.
    d.create_standard_dialog_node(
        i_hope_i_dont_come_to_regret_node_uuid,
        bg3.SPEAKER_PLAYER,
        [you_can_always_rid_yourself_of_that_regret_node_uuid],
        bg3.text_content('hbe191947g233fg4ef7gb172g415bdd40ba49', 1),
        constructor=bg3.dialog_object.QUESTION)

    # Well you can always rid yourself of that regret with a well-place thrust of a dagger... if it comes to that, of course.
    d.create_standard_dialog_node(
        you_can_always_rid_yourself_of_that_regret_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [],
        bg3.text_content('h2351244eg25b9g4136ga0e4gec799138c580', 1),
        constructor=bg3.dialog_object.ANSWER,
        end_node=True)
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '6.789',
        you_can_always_rid_yourself_of_that_regret_node_uuid,
        (('6.8', '0e8837db-4344-48d0-9175-12262c73806b'), (None, 'a5043f00-72f3-49fe-a24f-fce1e268d896')),
        phase_duration = '7.2',
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.89, 16, None), (2.03, 16, 1), (2.93, 16, None), (3.65, 4, None), (4.94, 16, None), (6.15, 4, None)),
            bg3.SPEAKER_PLAYER: ((0.0, 4, None),)
        },
        attitudes = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_R_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, None),),
            bg3.SPEAKER_PLAYER: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_L_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, None),),
        })


bg3.add_build_procedure('create_conversation_gur_monster_hunter_putrid_bog', create_conversation_gur_monster_hunter_putrid_bog)

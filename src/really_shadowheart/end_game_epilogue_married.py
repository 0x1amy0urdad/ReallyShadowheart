from __future__ import annotations

import bg3moddinglib as bg3

from .context import game_assets
from .flags import *

def create_conversation_epilogue_married_couple() -> None:

    # d = bg3.dialog_object(files.get_file('Gustav', 'Mods/GustavDev/Story/DialogsBinary/Act3/EndGame/Epilogue/EPI_Epilogue_Shadowheart.lsf'))
    # t = bg3.timeline_object(files.get_file('Gustav', 'Public/GustavDev/Timeline/Generated/EPI_Epilogue_Shadowheart.lsf'), d)

    ab = game_assets.get_modded_dialog_asset_bundle('EPI_Epilogue_Shadowheart')
    d = bg3.dialog_object(ab.dialog)
    t = bg3.timeline_object(ab.timeline, d)

    slot_idx_tav = d.get_speaker_slot_index(bg3.SPEAKER_PLAYER)

    #########################################
    # Dialog: EPI_Epilogue_Shadowheart.lsf
    #########################################

    leaves_stuck_to_my_backside_node_uuid = '089d2852-7fca-44bc-8f99-7f8e4b72844e'
    back_to_cosy_cottage_node_uuid = 'cd1b875b-88b5-4d2f-9a18-ac10859fb794'
    must_i_node_uuid = '468a5596-9336-4257-8729-fbc514d5c0c5'
    take_parents_with_us_node_uuid = '5528d293-1f94-4a42-8123-be96a368daee'
    grandchildren_node_uuid = 'dfd3c34d-bf19-4757-b7af-947a211ddfc4'
    i_can_picture_the_look_node_uuid = 'f51489c6-aa4e-4fc5-9829-0d570927b26d'
    do_you_really_mean_that_node_uuid = '8abe32a0-accc-4e41-9a7c-2223af5e28c4'
    do_you_really_mean_that_female_node_uuid = 'ff185999-5803-4d54-beb2-3b48696ca281'
    i_suppose_i_do_node_uuid = 'e617406c-507b-4c5d-83f4-b06f3aa0bbd9'
    youd_never_ask_node_uuid = 'bfb830dd-c95b-4335-ae38-0e5b5fdc5fe1'
    we_are_expecting_node_uuid = '3f3bcaf2-a919-4f4c-a1cf-a93ba6f3b10a'
    lathander_heard_our_prayers_node_uuid = '974ee5f8-86f5-4e83-9e9c-50659b48f934'
    yes_perhaps_node_uuid = '689d5c5b-b3e4-46ea-a48e-6032c277555a'
    pay_no_attnetion_node_uuid = 'f8d67cda-5f71-4742-a147-d2a3893a16dd'
    parents_would_step_in_node_uuid = '484cef77-5d60-4f5e-a821-53539a8dc877'
    children_source_of_trouble_node_uuid = 'c1c246ca-fb4d-4353-bfc5-484a077090bc'
    sort_of_trouble_i_live_for_node_uuid = '47077824-d907-4219-ada0-040056c79ebe'
    happy_tear_node_uuid = '72d5f1d1-8c7e-40c7-a265-4f4fbbe642eb'
    keep_that_secret_node_uuid = '193fffb8-fecf-43f4-a3c2-aef23a5bbcf8'
    bypass_node_uuid = 'fc393ad8-b6d1-45a6-bace-35f020594445'
    kiss_reaction_node_uuid = 'ae4e4d40-150b-46a7-8545-ab2bc518441f'
    jump_back_1_node_uuid = 'd6011a52-e32f-4ec3-8175-49c1a5501abf'
    jump_back_2_node_uuid = 'd91a8d4d-0a24-4072-8a0d-57c5982e10b0'
    terribly_boring_selune_path_node_uuid = 'a99e4543-abe2-a3a1-6f3e-2cc8b929ccae'
    terribly_boring_shar_redemption_path_node_uuid = 'b7f2c5d6-ad15-1ac1-fa8c-ff8f7ec38727'
    enjoying_yourself_i_hope_node_uuid = '615d70fe-8832-1404-be8a-ab9194b877bb'

    

    d.add_dialog_flags(terribly_boring_selune_path_node_uuid, setflags = (
        bg3.flag_group("Local", (
            bg3.flag(Tav_Shadowheart_Epilogue_Convesation_Happened.uuid, True, None),
        )),
    ))

    d.add_dialog_flags(terribly_boring_shar_redemption_path_node_uuid, setflags = (
        bg3.flag_group("Local", (
            bg3.flag(Tav_Shadowheart_Epilogue_Convesation_Happened.uuid, True, None),
        )),
    ))

    # You must be keen to get back to our cosy cottage, don't you?
    d.create_standard_dialog_node(
        back_to_cosy_cottage_node_uuid,
        bg3.SPEAKER_PLAYER,
        [must_i_node_uuid],
        bg3.text_content('h9e23c5abg5a55g46c6g949fg4c089b18300f', 1),
        constructor = bg3.dialog_object.QUESTION,
        show_once = True,
        checkflags = (
            bg3.flag_group(bg3.flag_group.GLOBAL, (
                bg3.flag(Shadowheart_Tav_State_Married.uuid, True),
                bg3.flag(bg3.FLAG_ORI_Shadowheart_State_RetiredToFarmWithAvatar, True)
            )),
            bg3.flag_group(bg3.flag_group.LOCAL, (
                bg3.flag(Tav_Shadowheart_Marriage_Mentioned.uuid, False, None),
            )),
        ))

    # Must I? Honestly, I'm still not used to being married - it's almost a surprise... But a very pleasant surprise.
    d.create_standard_dialog_node(
        must_i_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [jump_back_2_node_uuid, jump_back_1_node_uuid],
        bg3.text_content('h78c89a38g324bg4a2cg9a76g58d634b668bf', 1),
        constructor=bg3.dialog_object.ANSWER,
        setflags=(
            bg3.flag_group(bg3.flag_group.LOCAL, (
                bg3.flag(Tav_Shadowheart_Marriage_Mentioned.uuid, True, None),
            )),
        ))
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '13.176',
        must_i_node_uuid,
        (
            ('2.2', '901e76eb-f5a5-4b6d-a16a-49930a7e2497'),
            ('8.1', '76b27274-bab6-4ba3-8e87-33441167316f'),
            ('11.1', '8f2ba008-2c99-4b20-a361-aaba89d33b33'),
            ('13.2', '76b27274-bab6-4ba3-8e87-33441167316f'),
            (None, '54f58265-8a27-4025-acd5-bbcba02063a7')
        ),
        emotions = {
            bg3.SPEAKER_SHADOWHEART: [(0.0, 64, None), (10.0, 2, 2)],
            bg3.SPEAKER_PLAYER: [(0.0, 1, None), (0.5, 64, 2), (8.4, 64, 1), (13, 2, None)]
        },
        attitudes = {
            bg3.SPEAKER_PLAYER: (
                (8.5, 'fd6ca738-c675-4249-8755-07d0d7027251', bg3.ATTITUDE_DIAG_T_Pose, None),
                (11.5, bg3.ATTITUDE_DIAG_Pose_Stand_L_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, None),
            ),
        },
        phase_duration='13.5'
    )

    # We should take your parents with us to the next party, if Withers calls us again.
    d.create_standard_dialog_node(
        take_parents_with_us_node_uuid,
        bg3.SPEAKER_PLAYER,
        [grandchildren_node_uuid],
        bg3.text_content('heb4bc4d7g7624g48b7g8200g7c599b41938f', 1),
        constructor=bg3.dialog_object.QUESTION,
        show_once=True,
        checkflags=(
            bg3.flag_group(bg3.flag_group.GLOBAL, (
                bg3.flag(Shadowheart_Tav_State_Married.uuid, True),
                bg3.flag(bg3.FLAG_ORI_Shadowheart_State_RetiredToFarmWithAvatar, True)
            )),
            bg3.flag_group(bg3.flag_group.LOCAL, (
                bg3.flag(Tav_Shadowheart_Marriage_Mentioned.uuid, True, None),
                bg3.flag(Tav_Shadowheart_Grandchildren_Mentioned.uuid, False, None),
            )),
        ))


    # Who knows? Perhaps they'll have grandchildren before long.
    d.create_standard_dialog_node(
        grandchildren_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [i_can_picture_the_look_node_uuid],
        bg3.text_content('h7a5a8a24gd159g4acag8e08ge118c911b003', 1),
        constructor=bg3.dialog_object.ANSWER,
        setflags = (
            bg3.flag_group("Local", (
                bg3.flag(Tav_Shadowheart_Grandchildren_Mentioned.uuid, True, None),
            )),
        ))

    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '4.64',
        grandchildren_node_uuid,
        ((None, '76b27274-bab6-4ba3-8e87-33441167316f'),),
        emotions = {
            bg3.SPEAKER_SHADOWHEART: [(0.0, 2, None), (3.3, 4, 2)],
            bg3.SPEAKER_PLAYER: [(0.0, 1, None), (3.5, 64, 2)]
        },
        phase_duration = '4.8'
    )

    # I can picture the look on my parent's faces already...
    d.create_standard_dialog_node(
        i_can_picture_the_look_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [
            pay_no_attnetion_node_uuid,
            do_you_really_mean_that_node_uuid,
            we_are_expecting_node_uuid,
            lathander_heard_our_prayers_node_uuid
        ],
        bg3.text_content('hc15d705ag42afg485cg937dg0e717d80f5d3', 1),
        constructor=bg3.dialog_object.ANSWER)

    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '3.98',
        i_can_picture_the_look_node_uuid,
        (
            ('3.98', '76b27274-bab6-4ba3-8e87-33441167316f'),
            (None, '17f67174-5546-433b-b54d-aaec87981b68'),
        ),
        emotions = {
            bg3.SPEAKER_SHADOWHEART: [(0.0, 2, 2), (1.75, 2, 1)],
            bg3.SPEAKER_PLAYER: [(0.0, 64, None), (3.1, 64, 2)]
        },
        phase_duration = '4.2'
    )

    # Wait, are we... expecting? Do you really mean that?
    d.create_standard_dialog_node(
        do_you_really_mean_that_node_uuid,
        bg3.SPEAKER_PLAYER,
        [i_suppose_i_do_node_uuid],
        bg3.text_content('h6af6d9f8gede1g482fg8cc6g0cecb08e0cfa', 1),
        # checkflags = (
        #     bg3.flag_group('Tag', (
        #         bg3.flag(bg3.TAG_FEMALE, False, slot_idx_tav),
        #     )),
        # ),
        constructor=bg3.dialog_object.QUESTION)

    # # 
    # d.create_standard_dialog_node(
    #     do_you_really_mean_that_female_node_uuid,
    #     bg3.SPEAKER_PLAYER,
    #     [i_suppose_i_do_node_uuid],
    #     bg3.text_content('h6ac59daag1832g4d71g9853g0b23ad51eae0', 1),
    #     checkflags = (
    #         bg3.flag_group('Tag', (
    #             bg3.flag(bg3.TAG_FEMALE, True, slot_idx_tav),
    #         )),
    #     ),
    #     constructor=bg3.dialog_object.QUESTION)

    # I suppose I do, don't I?
    d.create_standard_dialog_node(
        i_suppose_i_do_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [youd_never_ask_node_uuid],
        bg3.text_content('hbd47e60bgd882g43f6g8f65g9782c9e4733e', 1),
        constructor=bg3.dialog_object.ANSWER)

    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '2.42',
        i_suppose_i_do_node_uuid,
        (
            (None, '76b27274-bab6-4ba3-8e87-33441167316f'),
        ),
        emotions = {
            bg3.SPEAKER_SHADOWHEART: [(0.0, 2, None),],
            bg3.SPEAKER_PLAYER: [(0.0, 64, None),]
        }
    )

    # I was starting to think you'd never ask...
    d.create_standard_dialog_node(
        youd_never_ask_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [keep_that_secret_node_uuid],
        bg3.text_content('ha5ade060g70b9g4725g8f26g3f6232f11ecf', 1),
        constructor=bg3.dialog_object.ANSWER)

    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '4.274',
        youd_never_ask_node_uuid,
        (
            ('4.274', '76b27274-bab6-4ba3-8e87-33441167316f'),
            (None, '54f58265-8a27-4025-acd5-bbcba02063a7')
        ),
        emotions = {
            bg3.SPEAKER_SHADOWHEART: [(0.0, 2, None),],
            bg3.SPEAKER_PLAYER: [(0.0, 64, None),]
        },
        phase_duration='4.4'
    )

    # Did you just say that we are expecting?!
    d.create_standard_dialog_node(
        we_are_expecting_node_uuid,
        bg3.SPEAKER_PLAYER,
        [yes_perhaps_node_uuid],
        bg3.text_content('haadd3e89g0eeeg4514g9cf2g3a73b36b9f98', 1),
        checkflags = (
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_FEMALE, False, slot_idx_tav),
            )),
        ),
        constructor=bg3.dialog_object.QUESTION)

    # Did you just say Lathander heard our prayers? Am I an expectant spouse now?
    d.create_standard_dialog_node(
        lathander_heard_our_prayers_node_uuid,
        bg3.SPEAKER_PLAYER,
        [yes_perhaps_node_uuid],
        bg3.text_content('h8e6de288g61c0g4ff3g8e6dga6505c33e960', 1),
        checkflags = (
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_FEMALE, True, slot_idx_tav),
            )),
        ),
        constructor=bg3.dialog_object.QUESTION)

    # Yes, perhaps...
    d.create_standard_dialog_node(
        yes_perhaps_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [youd_never_ask_node_uuid],
        bg3.text_content('hf3b62768ga426g4abcgab78g7a68c5557c9a', 1),
        constructor=bg3.dialog_object.ANSWER)

    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '2.08',
        yes_perhaps_node_uuid,
        (
            (None, '76b27274-bab6-4ba3-8e87-33441167316f'),
        ),
        emotions = {
            bg3.SPEAKER_SHADOWHEART: [(0.15, 16, None), (0.71, 2, None),],
            bg3.SPEAKER_PLAYER: [(0.4, 16, None),]
        },
        phase_duration='2.54'
    )

    # d.create_standard_dialog_node(
    #     bypass_node_uuid,
    #     bg3.SPEAKER_SHADOWHEART,
    #     [happy_tear_node_uuid, children_source_of_trouble_node_uuid],
    #     None,
    #     checkflags = (
    #         bg3.flag_group('Tag', (
    #             bg3.flag(bg3.TAG_FEMALE, True, slot_idx_tav),
    #         )),
    #     ),
    #     constructor=bg3.dialog_object.ANSWER)

    # Let's keep that our special secret. Oh you know what I mean...
    d.create_standard_dialog_node(
        keep_that_secret_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [happy_tear_node_uuid, parents_would_step_in_node_uuid],
        bg3.text_content('h198df115g788ag4de4g9ccfg5c8e82bc10f8', 1),
        constructor=bg3.dialog_object.ANSWER)

    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '6.864',
        keep_that_secret_node_uuid,
        (
            ('3.0', '54f58265-8a27-4025-acd5-bbcba02063a7'),
            (None, '8f2ba008-2c99-4b20-a361-aaba89d33b33')
        ),
        emotions = {
            bg3.SPEAKER_SHADOWHEART: [(0.38, 64, 1), (2.28, 64, None)],
            bg3.SPEAKER_PLAYER: [(0.4, 1, None), (3.4, 64, 1)]
        },
        phase_duration='7.0'
    )

    # Pay no attention to that and move on to other matters.
    d.create_standard_dialog_node(
        pay_no_attnetion_node_uuid,
        bg3.SPEAKER_PLAYER,
        [jump_back_2_node_uuid, jump_back_1_node_uuid],
        bg3.text_content('hcb948f33g2863g49d1g8074g267265978b66', 1),
        constructor=bg3.dialog_object.QUESTION)


    # I do hope your parents would step in and help us with our new troubles...
    d.create_standard_dialog_node(
        parents_would_step_in_node_uuid,
        bg3.SPEAKER_PLAYER,
        [sort_of_trouble_i_live_for_node_uuid],
        bg3.text_content('hab27fa75ge385g4d81g8b81gca48789e9a7b', 1),
        # checkflags = (
        #     bg3.flag_group('Tag', (
        #         bg3.flag(bg3.TAG_FEMALE, False, slot_idx_tav),
        #     )),
        # ),
        constructor=bg3.dialog_object.QUESTION)

    # # Children are source of trouble, do you know that?
    # d.create_standard_dialog_node(
    #     children_source_of_trouble_node_uuid,
    #     bg3.SPEAKER_PLAYER,
    #     [sort_of_trouble_i_live_for_node_uuid],
    #     bg3.text_content('h460ba56dgd453g4e9cgbd11g1a7133b34cbe', 1),
    #     checkflags = (
    #         bg3.flag_group('Tag', (
    #             bg3.flag(bg3.TAG_FEMALE, True, slot_idx_tav),
    #         )),
    #     ),
    #     constructor=bg3.dialog_object.QUESTION)
    

    # That's the sort of trouble I live for.
    d.create_standard_dialog_node(
        sort_of_trouble_i_live_for_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [jump_back_2_node_uuid, jump_back_1_node_uuid],
        bg3.text_content('h52748d9eg7edcg4ec7gb7f4g3420366ec3d4', 1),
        constructor=bg3.dialog_object.ANSWER)

    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '3.33',
        sort_of_trouble_i_live_for_node_uuid,
        (
            ('4.274', '76b27274-bab6-4ba3-8e87-33441167316f'),
            (None, '54f58265-8a27-4025-acd5-bbcba02063a7')
        ),
        emotions = {
            bg3.SPEAKER_SHADOWHEART: [(0.0, 2, None),],
            bg3.SPEAKER_PLAYER: [(0.0, 64, None),]
        },
        phase_duration='4.4'
    )

    #
    # Kiss her aliases
    #
    kiss_alias_1_node_uuid = '7de84819-2995-4b1e-9d35-338aeb3361fa'
    kiss_alias_2_node_uuid = 'cebf54f6-3acb-480c-bcff-942bdda1fa99'
    kiss_alias_3_node_uuid = '63b8b360-e0c6-4f50-806a-fc469ff69df0'
    kiss_alias_4_node_uuid = '2ef6f9ce-0028-4a28-9aae-dbbcdbcb2e78'
    kiss_alias_5_node_uuid = 'e47d5f79-0ee2-4430-b26d-1662bcc378ba'
    kiss_alias_6_node_uuid = 'bc3c8c7a-0c5c-4f89-ab21-08338fe7ed74'
    kiss_alias_7_node_uuid = 'ef099d90-1b67-4f51-9b10-64a1178aaf97'

    # &lt;i&gt;Shed a happy tear and kiss her.&lt;/i&gt;
    d.create_standard_dialog_node(
        happy_tear_node_uuid,
        bg3.SPEAKER_PLAYER,
        [
            kiss_alias_1_node_uuid,
            kiss_alias_2_node_uuid,
            kiss_alias_3_node_uuid,
            kiss_alias_4_node_uuid,
            kiss_alias_5_node_uuid,
            kiss_alias_6_node_uuid,
            kiss_alias_7_node_uuid,
        ],
        bg3.text_content('hfee6d489g9f92g4b08gad5egcde430d9f6e3', 1),
        constructor=bg3.dialog_object.QUESTION)

    d.create_alias_dialog_node(
        kiss_alias_1_node_uuid,
        '4796b7ea-7658-f03b-05cc-12b642f405f7',
        [kiss_reaction_node_uuid],
        show_once = True,
        checkflags = (
            bg3.flag_group("Tag", (
                bg3.flag(bg3.TAG_FULL_CEREMORPH, True, slot_idx_tav),
                bg3.flag(bg3.TAG_HUMANOID_MONSTER, False, slot_idx_tav)
            )),
        ))
    d.create_alias_dialog_node(
        kiss_alias_2_node_uuid,
        'c88b5996-c5cc-a63e-a513-c23a4aab4467',
        [kiss_reaction_node_uuid],
        show_once = True,
        checkflags = (
            bg3.flag_group("Tag", (
                bg3.flag(bg3.TAG_DWARF, True, slot_idx_tav),
            )),
        ))
    d.create_alias_dialog_node(
        kiss_alias_3_node_uuid,
        'a04825f1-271d-431a-139a-9dd9c6c4cbdf',
        [kiss_reaction_node_uuid],
        show_once = True,
        checkflags = (
            bg3.flag_group("Tag", (
                bg3.flag(bg3.TAG_SHORT, True, slot_idx_tav),
            )),
        ))
    d.create_alias_dialog_node(
        kiss_alias_4_node_uuid,
        '4b585ded-a7a5-f03f-6257-3d4f9766a4c9',
        [kiss_reaction_node_uuid],
        show_once = True,
        checkflags = (
            bg3.flag_group("Tag", (
                bg3.flag(bg3.TAG_DRAGONBORN, True, slot_idx_tav),
            )),
        ))
    d.create_alias_dialog_node(
        kiss_alias_5_node_uuid,
        'b1903548-474e-8d56-12e2-3f8a63507d37',
        [kiss_reaction_node_uuid],
        show_once = True,
        checkflags = (
            bg3.flag_group("Tag", (
                bg3.flag(bg3.TAG_BODYTYPE_STRONG, True, slot_idx_tav),
            )),
        ))
    d.create_alias_dialog_node(
        kiss_alias_6_node_uuid,
        'f5a83bc1-ce3c-37a5-5710-cc95bfb9b67c',
        [kiss_reaction_node_uuid],
        show_once = True,
        checkflags = (
            bg3.flag_group("Tag", (
                bg3.flag(bg3.TAG_FEMALE, True, slot_idx_tav),
            )),
        ))
    d.create_alias_dialog_node(
        kiss_alias_7_node_uuid,
        'bafd964e-833f-4dd3-a908-3e13262cda96',
        [kiss_reaction_node_uuid],
        show_once = True)

    d.create_alias_dialog_node(
        kiss_reaction_node_uuid,
        'c263d617-d4dc-23bf-67c3-ef6c2085b878',
        [jump_back_2_node_uuid, jump_back_1_node_uuid],
        show_once = True)

    d.create_standard_dialog_node(
        jump_back_1_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        ['cfb979f0-d79b-4068-92cb-03be41d0c7a8'],
        None,
        checkflags = (
            bg3.flag_group("Local", (
                bg3.flag(Tav_Shadowheart_Epilogue_Convesation_Happened.uuid, False, None),
            )),
        ))

    d.create_standard_dialog_node(
        jump_back_2_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        ['d7733481-fd3d-46a4-b9b8-69e2182ce46c'],
        None,
        checkflags = (
            bg3.flag_group("Local", (
                bg3.flag(Tav_Shadowheart_Epilogue_Convesation_Happened.uuid, True, None),
            )),
        ))

    d.create_jump_dialog_node('cfb979f0-d79b-4068-92cb-03be41d0c7a8', leaves_stuck_to_my_backside_node_uuid, 2)
    d.create_jump_dialog_node('d7733481-fd3d-46a4-b9b8-69e2182ce46c', enjoying_yourself_i_hope_node_uuid, 2)

    d.add_child_dialog_node(leaves_stuck_to_my_backside_node_uuid, take_parents_with_us_node_uuid, 0)
    d.add_child_dialog_node(leaves_stuck_to_my_backside_node_uuid, back_to_cosy_cottage_node_uuid, 0)

    d.add_child_dialog_node(enjoying_yourself_i_hope_node_uuid, take_parents_with_us_node_uuid, 0)
    d.add_child_dialog_node(enjoying_yourself_i_hope_node_uuid, back_to_cosy_cottage_node_uuid, 0)


bg3.add_build_procedure('create_conversation_epilogue_married_couple', create_conversation_epilogue_married_couple)

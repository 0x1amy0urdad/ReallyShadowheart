from __future__ import annotations

import bg3moddinglib as bg3

from .context import get_context
from .flags import *

def create_conversation_epilogue_married_couple() -> None:
    game_assets = get_context().assets

    ab = game_assets.get_modded_dialog_asset_bundle('EPI_Epilogue_Shadowheart')
    d = bg3.dialog_object(ab.dialog)
    t = bg3.timeline_object(ab.timeline, d)

    speaker_idx_tav = d.get_speaker_slot_index(bg3.SPEAKER_PLAYER)
    speaker_idx_shadowheart = d.get_speaker_slot_index(bg3.SPEAKER_SHADOWHEART)

    #########################################
    # Dialog: EPI_Epilogue_Shadowheart.lsf
    #########################################

    leaves_stuck_to_my_backside_node_uuid = '089d2852-7fca-44bc-8f99-7f8e4b72844e' # existing node, 1st dialog
    enjoying_yourself_i_hope_node_uuid = '615d70fe-8832-1404-be8a-ab9194b877bb' # existing node, 2nd dialog
    checking_in_on_me_sweet_of_you_node = '644c0b9a-0166-eba8-5e8d-68a877676095' # existing node, 3rd and all other dialogs
    lets_make_tonight_count_node_uuid = '58da3ab8-9234-7b0d-7c93-973c8fe5d23a' # existing node

    back_to_cosy_cottage_node_uuid = 'cd1b875b-88b5-4d2f-9a18-ac10859fb794'
    must_i_node_uuid = '468a5596-9336-4257-8729-fbc514d5c0c5'
    take_parents_with_us_node_uuid = '5528d293-1f94-4a42-8123-be96a368daee'
    grandchildren_node_uuid = 'dfd3c34d-bf19-4757-b7af-947a211ddfc4'
    i_can_picture_the_look_node_uuid = 'f51489c6-aa4e-4fc5-9829-0d570927b26d'
    do_you_really_mean_that_node_uuid = '8abe32a0-accc-4e41-9a7c-2223af5e28c4'
    i_suppose_i_do_node_uuid = 'e617406c-507b-4c5d-83f4-b06f3aa0bbd9'
    youd_never_ask_node_uuid = 'bfb830dd-c95b-4335-ae38-0e5b5fdc5fe1'
    we_are_expecting_node_uuid = '3f3bcaf2-a919-4f4c-a1cf-a93ba6f3b10a'
    lathander_heard_our_prayers_node_uuid = '974ee5f8-86f5-4e83-9e9c-50659b48f934'
    yes_perhaps_node_uuid = '689d5c5b-b3e4-46ea-a48e-6032c277555a'
    pay_no_attnetion_node_uuid = 'f8d67cda-5f71-4742-a147-d2a3893a16dd'
    parents_would_step_in_node_uuid = '484cef77-5d60-4f5e-a821-53539a8dc877'
    sort_of_trouble_i_live_for_node_uuid = '47077824-d907-4219-ada0-040056c79ebe'
    happy_tear_node_uuid = '72d5f1d1-8c7e-40c7-a265-4f4fbbe642eb'
    keep_that_secret_node_uuid = '193fffb8-fecf-43f4-a3c2-aef23a5bbcf8'
    kiss_reaction_node_uuid = 'ae4e4d40-150b-46a7-8545-ab2bc518441f'
    jump_to_i_hope_we_wont_seem_terribly_boring_node_uuid = 'a280f866-06ac-4265-aa84-aa2c4aeb770a'
    jump_back_1_node_uuid = 'd6011a52-e32f-4ec3-8175-49c1a5501abf'
    jump_back_2_node_uuid = 'd91a8d4d-0a24-4072-8a0d-57c5982e10b0'
    jump_back_3_node_uuid = '39227ad1-7bc4-4542-8215-08a0490a501f'


    # a07c619a-ef51-4627-bea0-dc25333a8ae3 Shadowheart
    # 515ddf53-051a-462f-a59e-c408ef0bc1f3 Tav

    # 76b27274-bab6-4ba3-8e87-33441167316f Shadowheart -> Shadowheart
    # 54f58265-8a27-4025-acd5-bbcba02063a7 Shadowheart -> Shadowheart
    # 17f67174-5546-433b-b54d-aaec87981b68 Tav         -> Shadowheart
    # 901e76eb-f5a5-4b6d-a16a-49930a7e2497 Shadowheart -> Tav
    # 8f2ba008-2c99-4b20-a361-aaba89d33b33 Tav         -> Tav
    # 5ca301a6-46e0-474f-9577-c4506b1017d8 Shadowheart -> Tav
    # 40dfb377-ca20-4e0e-8ff1-2eb954797090 Shadowheart -> Tav
    # ea49f57e-ef64-4f7f-82bd-811e31e6cb62 Tav         -> Shadowheart
    # f307f27b-f965-49c6-b9ff-9a704b45b41f Tav         -> Shadowheart
    # ce7ab405-861d-412b-8d69-97269c440501 Tav         -> Shadowheart
    # 70178311-1d50-4d78-b894-e8141e505361 free
    # 2eb0f72d-b6bb-4388-80c3-e9b2f17a7572 free

    d.add_dialog_flags(leaves_stuck_to_my_backside_node_uuid, setflags = (
        bg3.flag_group("Local", (
            bg3.flag(Tav_Shadowheart_Epilogue_Convesation_1.uuid, True, None),
            bg3.flag(Tav_Shadowheart_Epilogue_Convesation_2.uuid, False, None),
            bg3.flag(Tav_Shadowheart_Epilogue_Convesation_3.uuid, False, None),
            bg3.flag(Tav_Shadowheart_Epilogue_Convesation_Voice.uuid, False, None),
        )),
    ))

    d.add_dialog_flags(enjoying_yourself_i_hope_node_uuid, setflags = (
        bg3.flag_group("Local", (
            bg3.flag(Tav_Shadowheart_Epilogue_Convesation_1.uuid, False, None),
            bg3.flag(Tav_Shadowheart_Epilogue_Convesation_2.uuid, True, None),
            bg3.flag(Tav_Shadowheart_Epilogue_Convesation_3.uuid, False, None),
            bg3.flag(Tav_Shadowheart_Epilogue_Convesation_Voice.uuid, False, None),
        )),
    ))

    d.add_dialog_flags(checking_in_on_me_sweet_of_you_node, setflags = (
        bg3.flag_group("Local", (
            bg3.flag(Tav_Shadowheart_Epilogue_Convesation_1.uuid, False, None),
            bg3.flag(Tav_Shadowheart_Epilogue_Convesation_2.uuid, False, None),
            bg3.flag(Tav_Shadowheart_Epilogue_Convesation_3.uuid, True, None),
            bg3.flag(Tav_Shadowheart_Epilogue_Convesation_Voice.uuid, False, None),
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
        [jump_back_3_node_uuid, jump_back_2_node_uuid, jump_back_1_node_uuid],
        bg3.text_content('h78c89a38g324bg4a2cg9a76g58d634b668bf', 1),
        constructor=bg3.dialog_object.ANSWER,
        setflags=(
            bg3.flag_group(bg3.flag_group.LOCAL, (
                bg3.flag(Tav_Shadowheart_Marriage_Mentioned.uuid, True, None),
            )),
        ))
    # BUG: anumation hold
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '13.1',
        must_i_node_uuid,
        (
            ('2.2', '901e76eb-f5a5-4b6d-a16a-49930a7e2497'),
            ('8.1', '76b27274-bab6-4ba3-8e87-33441167316f'),
            ('11.1', '8f2ba008-2c99-4b20-a361-aaba89d33b33'),
            ('13.0', '76b27274-bab6-4ba3-8e87-33441167316f'),
            (None, '8f2ba008-2c99-4b20-a361-aaba89d33b33')
        ),
        fade_in = 0.0,
        fade_out = 1.0,
        performance_fade = 1.0,
        emotions = {
            bg3.SPEAKER_SHADOWHEART: [(0.0, 64, None), (10.0, 2, 2)],
            bg3.SPEAKER_PLAYER: [(0.0, 1, None), (0.5, 64, 2), (8.4, 64, 1), (13, 2, None)]
        },
        attitudes = {
            bg3.SPEAKER_PLAYER: (
                (8.5, 'fd6ca738-c675-4249-8755-07d0d7027251', bg3.ATTITUDE_DIAG_T_Pose, None),
                (11.5, bg3.ATTITUDE_DIAG_Pose_Stand_L_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, None),
            ),
            bg3.SPEAKER_SHADOWHEART: (
                (0.0, bg3.ATTITUDE_DIAG_Pose_Stand_R_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, None),
            )
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
        '4.17',
        grandchildren_node_uuid,
        ((None, 'ea49f57e-ef64-4f7f-82bd-811e31e6cb62'),),
        emotions = {
            bg3.SPEAKER_SHADOWHEART: [(0.0, 2, None), (3.3, 4, 2)],
            bg3.SPEAKER_PLAYER: [(0.0, 1, None), (3.5, 64, 2)]
        },
        phase_duration = '4.8',
        fade_in = 0.7,
        fade_out = 0.7,
        performance_fade = 1.0,
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

    # BUG: anumation hold
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '3.16',
        i_can_picture_the_look_node_uuid,
        (
            ('3.2', '17f67174-5546-433b-b54d-aaec87981b68'),
            (None, '8f2ba008-2c99-4b20-a361-aaba89d33b33'),
        ),
        emotions = {
            bg3.SPEAKER_SHADOWHEART: [(0.0, 2, 2), (1.75, 2, 1)],
            bg3.SPEAKER_PLAYER: [(0.0, 64, None), (3.1, 64, 2)]
        },
        fade_in = 0.7,
        fade_out = 0.7,
        performance_fade = 1.0,
        phase_duration = '3.8'
    )

    # Wait, are we... expecting? Do you really mean that?
    d.create_standard_dialog_node(
        do_you_really_mean_that_node_uuid,
        bg3.SPEAKER_PLAYER,
        [i_suppose_i_do_node_uuid],
        bg3.text_content('h6af6d9f8gede1g482fg8cc6g0cecb08e0cfa', 1),
        constructor=bg3.dialog_object.QUESTION)

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
            (None, '54f58265-8a27-4025-acd5-bbcba02063a7'),
        ),
        emotions = {
            bg3.SPEAKER_SHADOWHEART: [(0.0, 2, None),],
            bg3.SPEAKER_PLAYER: [(0.0, 64, None),]
        },
        fade_out = 0.5,
        performance_fade = 1.0,
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
            (None, '54f58265-8a27-4025-acd5-bbcba02063a7'),
        ),
        emotions = {
            bg3.SPEAKER_SHADOWHEART: [(0.0, 2, None),],
            bg3.SPEAKER_PLAYER: [(0.0, 64, None),]
        },
        phase_duration='4.4',
        fade_in = 0.5,
        fade_out = 0.5,
        performance_fade = 1.0,
    )

    # Did you just say that we are expecting?!
    d.create_standard_dialog_node(
        we_are_expecting_node_uuid,
        bg3.SPEAKER_PLAYER,
        [yes_perhaps_node_uuid],
        bg3.text_content('haadd3e89g0eeeg4514g9cf2g3a73b36b9f98', 1),
        checkflags = (
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_FEMALE, False, speaker_idx_tav),
            )),
        ),
        constructor=bg3.dialog_object.QUESTION)

    # Did you just say Selûne blessed us with a baby?
    d.create_standard_dialog_node(
        lathander_heard_our_prayers_node_uuid,
        bg3.SPEAKER_PLAYER,
        [yes_perhaps_node_uuid],
        bg3.text_content('h8e6de288g61c0g4ff3g8e6dga6505c33e960', 1),
        checkflags = (
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_FEMALE, True, speaker_idx_tav),
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
        '1.5',
        yes_perhaps_node_uuid,
        (
            (None, '54f58265-8a27-4025-acd5-bbcba02063a7'),
        ),
        emotions = {
            bg3.SPEAKER_SHADOWHEART: [(0.15, 16, None), (0.71, 2, None),],
            bg3.SPEAKER_PLAYER: [(0.4, 16, None),]
        },
        phase_duration='2.08',
        fade_out = 0.5,
        performance_fade = 1.0,
    )

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
            ('3.0', 'ce7ab405-861d-412b-8d69-97269c440501'),
            (None, '8f2ba008-2c99-4b20-a361-aaba89d33b33')
        ),
        emotions = {
            bg3.SPEAKER_SHADOWHEART: [(0.38, 64, 1), (2.28, 64, None)],
            bg3.SPEAKER_PLAYER: [(0.4, 1, None), (3.4, 64, 1)]
        },
        fade_in = 0.5,
        fade_out = 0.5,
        performance_fade = 1.0,    )

    # Pay no attention to that and move on to other matters.
    d.create_standard_dialog_node(
        pay_no_attnetion_node_uuid,
        bg3.SPEAKER_PLAYER,
        [jump_back_3_node_uuid, jump_back_2_node_uuid, jump_back_1_node_uuid],
        bg3.text_content('hcb948f33g2863g49d1g8074g267265978b66', 1),
        constructor=bg3.dialog_object.QUESTION)


    # I do hope your parents would step in and help us with our new troubles...
    d.create_standard_dialog_node(
        parents_would_step_in_node_uuid,
        bg3.SPEAKER_PLAYER,
        [sort_of_trouble_i_live_for_node_uuid],
        bg3.text_content('hab27fa75ge385g4d81g8b81gca48789e9a7b', 1),
        constructor=bg3.dialog_object.QUESTION)

    # That's the sort of trouble I live for.
    d.create_standard_dialog_node(
        sort_of_trouble_i_live_for_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        #[jump_back_3_node_uuid, jump_back_2_node_uuid, jump_back_1_node_uuid],
        [jump_to_i_hope_we_wont_seem_terribly_boring_node_uuid],
        bg3.text_content('h52748d9eg7edcg4ec7gb7f4g3420366ec3d4', 1),
        constructor=bg3.dialog_object.ANSWER)

    # BUG: anumation hold
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '2.823',
        sort_of_trouble_i_live_for_node_uuid,
        (
            ('2.8', '76b27274-bab6-4ba3-8e87-33441167316f'),
            (None, '8f2ba008-2c99-4b20-a361-aaba89d33b33')
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
                bg3.flag(bg3.TAG_FULL_CEREMORPH, True, speaker_idx_tav),
                bg3.flag(bg3.TAG_HUMANOID_MONSTER, False, speaker_idx_tav)
            )),
        ))
    d.create_alias_dialog_node(
        kiss_alias_2_node_uuid,
        'c88b5996-c5cc-a63e-a513-c23a4aab4467',
        [kiss_reaction_node_uuid],
        show_once = True,
        checkflags = (
            bg3.flag_group("Tag", (
                bg3.flag(bg3.TAG_DWARF, True, speaker_idx_tav),
            )),
        ))
    d.create_alias_dialog_node(
        kiss_alias_3_node_uuid,
        'a04825f1-271d-431a-139a-9dd9c6c4cbdf',
        [kiss_reaction_node_uuid],
        show_once = True,
        checkflags = (
            bg3.flag_group("Tag", (
                bg3.flag(bg3.TAG_SHORT, True, speaker_idx_tav),
            )),
        ))
    d.create_alias_dialog_node(
        kiss_alias_4_node_uuid,
        '4b585ded-a7a5-f03f-6257-3d4f9766a4c9',
        [kiss_reaction_node_uuid],
        show_once = True,
        checkflags = (
            bg3.flag_group("Tag", (
                bg3.flag(bg3.TAG_DRAGONBORN, True, speaker_idx_tav),
            )),
        ))
    d.create_alias_dialog_node(
        kiss_alias_5_node_uuid,
        'b1903548-474e-8d56-12e2-3f8a63507d37',
        [kiss_reaction_node_uuid],
        show_once = True,
        checkflags = (
            bg3.flag_group("Tag", (
                bg3.flag(bg3.TAG_BODYTYPE_STRONG, True, speaker_idx_tav),
            )),
        ))
    d.create_alias_dialog_node(
        kiss_alias_6_node_uuid,
        'f5a83bc1-ce3c-37a5-5710-cc95bfb9b67c',
        [kiss_reaction_node_uuid],
        show_once = True,
        checkflags = (
            bg3.flag_group("Tag", (
                bg3.flag(bg3.TAG_FEMALE, True, speaker_idx_tav),
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
        # [jump_back_3_node_uuid, jump_back_2_node_uuid, jump_back_1_node_uuid],
        [jump_to_i_hope_we_wont_seem_terribly_boring_node_uuid],
        show_once = True)

    d.create_standard_dialog_node(
        jump_back_1_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        ['cfb979f0-d79b-4068-92cb-03be41d0c7a8'],
        None,
        checkflags = (
            bg3.flag_group("Local", (
                bg3.flag(Tav_Shadowheart_Epilogue_Convesation_1.uuid, True, None),
            )),
        ))
    d.create_jump_dialog_node('cfb979f0-d79b-4068-92cb-03be41d0c7a8', leaves_stuck_to_my_backside_node_uuid, 2)

    d.create_standard_dialog_node(
        jump_back_2_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        ['d7733481-fd3d-46a4-b9b8-69e2182ce46c'],
        None,
        checkflags = (
            bg3.flag_group("Local", (
                bg3.flag(Tav_Shadowheart_Epilogue_Convesation_2.uuid, True, None),
            )),
        ))
    d.create_jump_dialog_node('d7733481-fd3d-46a4-b9b8-69e2182ce46c', lets_make_tonight_count_node_uuid, 2)

    d.create_standard_dialog_node(
        jump_back_3_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        ['6bf96554-7910-4a77-a12e-61631e28e2a5'],
        None,
        checkflags = (
            bg3.flag_group("Local", (
                bg3.flag(Tav_Shadowheart_Epilogue_Convesation_3.uuid, True, None),
            )),
        ))
    d.create_jump_dialog_node('6bf96554-7910-4a77-a12e-61631e28e2a5', lets_make_tonight_count_node_uuid, 2)

    a_little_wine_might_help_node_uuid = '68c17cf4-4787-c998-9912-98250d2d9db3' # existing node
    save_it_for_when_were_alone_node_uuid = '5186866e-ebfd-4f6c-9362-d76374656f49' # existing node
    oh_ive_noticed_node_uuid = '31dd1a85-b883-078d-89a1-ebf3a8cec461' # existing node
    youre_sweet_but_dont_worry_node_uuid = 'eddc67a7-f651-bf00-b24c-29c9de569793' # existing node

    partnered_dont_worry_node_uuid = '0d90dbb4-c1e2-62db-355c-b364f28a057b' # existing node
    partnered_i_can_pinch_you_node_uuid = '712b4a7a-d3ed-eaf8-b03d-22d1338ebd7c' # existing node
    partnered_your_backside_node_uuid = '335e9909-f4c3-fadf-9839-292a74494498' # existing node
    partnered_just_say_the_word_node_uuid = '7f16cdaa-ec53-fcfe-dd34-40752573e131' # existing node
    i_hope_we_wont_seem_terribly_boring_node_uuid = 'a99e4543-abe2-a3a1-6f3e-2cc8b929ccae' # existing node

    married_i_can_pinch_you_node_uuid = 'e5fe2199-5c5e-4a6b-a861-f3bd349895ee'
    married_your_backside_node_uuid = '6ab38560-2ac2-419a-a75e-2ed380a246e7'
    married_laezel_your_backside_node_uuid = '0fd0ad19-bd34-4046-b093-4b2c8d094bb7'
    married_dont_worry_node_uuid = '18054adf-6668-4109-a239-a82e5916d087'
    married_just_say_the_word_node_uuid = '26d93d2e-ef17-4352-9c6a-409392a254cb'
    married_more_tav_lines_node_uuid = '5ce6d378-88c2-42e5-9366-7f6bce38b9bf'

    alias_a_little_wine_might_help_node_uuid = '29bcfbb7-eda9-4b43-ae94-44222a67ace8'
    alias_save_it_for_when_were_alone_node_uuid = 'a98323b1-4187-4547-a180-5cb76ffd1938'
    alias_oh_ive_noticed_node_uuid = '7dda1491-05c3-40cf-8d40-fe96691cd01c'
    alias_youre_sweet_but_dont_worry_node_uuid = 'a2eccc8b-bff2-4c5a-8605-1a5064d9a51b'
    alias_i_hope_we_wont_seem_terribly_boring_node_uuid = 'd913b6df-3b51-44b1-9a4a-c95f623e61e9'

    d.create_jump_dialog_node(jump_to_i_hope_we_wont_seem_terribly_boring_node_uuid, alias_i_hope_we_wont_seem_terribly_boring_node_uuid, 1)

    d.create_alias_dialog_node(
        alias_i_hope_we_wont_seem_terribly_boring_node_uuid,
        i_hope_we_wont_seem_terribly_boring_node_uuid,
        ['66c000e4-effe-45d4-9d05-cfb57dfed60c'])
    d.create_jump_dialog_node('66c000e4-effe-45d4-9d05-cfb57dfed60c', i_hope_we_wont_seem_terribly_boring_node_uuid, 2)

    d.create_standard_dialog_node(
        married_dont_worry_node_uuid,
        bg3.SPEAKER_PLAYER,
        [alias_a_little_wine_might_help_node_uuid],
        bg3.text_content('ha9fc5aefg4d72g4e4egb23fg5049c715481b', 1),
        constructor = bg3.dialog_object.QUESTION,
        checkflags = (
            bg3.flag_group('Global', (
                bg3.flag(Shadowheart_Tav_State_Married.uuid, True, None),
            )),
        ))
    d.create_alias_dialog_node(
        alias_a_little_wine_might_help_node_uuid,
        a_little_wine_might_help_node_uuid,
        [alias_i_hope_we_wont_seem_terribly_boring_node_uuid])

    d.create_standard_dialog_node(
        married_i_can_pinch_you_node_uuid,
        bg3.SPEAKER_PLAYER,
        [alias_save_it_for_when_were_alone_node_uuid],
        bg3.text_content('h6ff170ccgf810g4670g8836g885e42840666', 1),
        constructor = bg3.dialog_object.QUESTION,
        checkflags = (
            bg3.flag_group('Global', (
                bg3.flag(Shadowheart_Tav_State_Married.uuid, True, None),
            )),
        ))
    d.create_alias_dialog_node(
        alias_save_it_for_when_were_alone_node_uuid,
        save_it_for_when_were_alone_node_uuid,
        [married_more_tav_lines_node_uuid])

    d.create_standard_dialog_node(
        married_your_backside_node_uuid,
        bg3.SPEAKER_PLAYER,
        [alias_oh_ive_noticed_node_uuid],
        bg3.text_content('h0a7a540bg05c9g4031gbb9ag598001638a28', 2),
        constructor = bg3.dialog_object.QUESTION,
        checkflags = (
            bg3.flag_group('Global', (
                bg3.flag(Shadowheart_Tav_State_Married.uuid, True, None),
            )),
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_REALLY_LAEZEL, False, speaker_idx_tav),
            )),
        ))
    d.create_alias_dialog_node(
        alias_oh_ive_noticed_node_uuid,
        oh_ive_noticed_node_uuid,
        [married_more_tav_lines_node_uuid])

    d.create_standard_dialog_node(
        married_laezel_your_backside_node_uuid,
        bg3.SPEAKER_PLAYER,
        [alias_oh_ive_noticed_node_uuid],
        bg3.text_content('h994ca233g57f7g494dg9cbeg91240f44cc49', 1),
        constructor = bg3.dialog_object.QUESTION,
        checkflags = (
            bg3.flag_group('Global', (
                bg3.flag(Shadowheart_Tav_State_Married.uuid, True, None),
            )),
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_REALLY_LAEZEL, True, speaker_idx_tav),
            )),
        ))
    

    d.create_standard_dialog_node(
        married_just_say_the_word_node_uuid,
        bg3.SPEAKER_PLAYER,
        [alias_youre_sweet_but_dont_worry_node_uuid],
        bg3.text_content('h15f569beg6392g437cg96bbg957d65dc54de', 2),
        constructor = bg3.dialog_object.QUESTION,
        checkflags = (
            bg3.flag_group('Global', (
                bg3.flag(Shadowheart_Tav_State_Married.uuid, True, None),
            )),
        ))
    d.create_alias_dialog_node(
        alias_youre_sweet_but_dont_worry_node_uuid,
        youre_sweet_but_dont_worry_node_uuid,
        [alias_i_hope_we_wont_seem_terribly_boring_node_uuid])

    d.create_standard_dialog_node(
        married_more_tav_lines_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [
            married_dont_worry_node_uuid,
            married_just_say_the_word_node_uuid,
        ],
        None,
    )

    d.add_dialog_flags(partnered_dont_worry_node_uuid, checkflags = (
        bg3.flag_group('Global', (
            bg3.flag(Shadowheart_Tav_State_Married.uuid, False, None),
        )),
    ))
    d.add_dialog_flags(partnered_i_can_pinch_you_node_uuid, checkflags = (
        bg3.flag_group('Global', (
            bg3.flag(Shadowheart_Tav_State_Married.uuid, False, None),
        )),
    ))
    d.add_dialog_flags(partnered_your_backside_node_uuid, checkflags = (
        bg3.flag_group('Global', (
            bg3.flag(Shadowheart_Tav_State_Married.uuid, False, None),
        )),
    ))
    d.add_dialog_flags(partnered_just_say_the_word_node_uuid, checkflags = (
        bg3.flag_group('Global', (
            bg3.flag(Shadowheart_Tav_State_Married.uuid, False, None),
        )),
    ))


    d.add_child_dialog_node(leaves_stuck_to_my_backside_node_uuid, married_your_backside_node_uuid, 0)
    d.add_child_dialog_node(leaves_stuck_to_my_backside_node_uuid, married_laezel_your_backside_node_uuid, 0)
    d.add_child_dialog_node(leaves_stuck_to_my_backside_node_uuid, married_i_can_pinch_you_node_uuid, 0)
    d.add_child_dialog_node(leaves_stuck_to_my_backside_node_uuid, take_parents_with_us_node_uuid, 0)
    d.add_child_dialog_node(leaves_stuck_to_my_backside_node_uuid, back_to_cosy_cottage_node_uuid, 0)

    # d.add_child_dialog_node(enjoying_yourself_i_hope_node_uuid, take_parents_with_us_node_uuid, 0)
    # d.add_child_dialog_node(enjoying_yourself_i_hope_node_uuid, back_to_cosy_cottage_node_uuid, 0)

    d.add_child_dialog_node(lets_make_tonight_count_node_uuid, take_parents_with_us_node_uuid, 0)
    d.add_child_dialog_node(lets_make_tonight_count_node_uuid, back_to_cosy_cottage_node_uuid, 0)

    #
    # Dad jokes
    #

    first_dad_joke_node_uuid = '5d4fb810-7e87-5535-5763-fd8aee629de4' # existing node
    leave_node_uuid = 'f38f2c4c-ae9d-8826-dc82-a1405a3a079f' # existing node/question
    not_with_that_sort_of_attitude_i_dont_node_uuid = '8b60add9-43d9-b994-4b77-1cce05db0cb9' # existing node
    hmm_let_me_see_node_uuid = '73ee0c50-90d8-785b-a5b7-7068db449011' # existing node

    more_terrible_jokes_to_share_node_uuid = '6d97e6f9-884e-20f4-f4ca-e01a8af70d66'
    more_hilarious_jokes_for_me_node_uuid = 'f36d9dd0-a4dd-88e3-4fc4-1e1e401aeae3'

    leave_joke_node_uuid = '72ab8c7d-5b0a-445b-802c-0e7edb493664'
    jump_to_dad_joke_node_uuid = 'f5356ccb-9a13-49af-8038-5117c379878e'
    leave2_node_uuid = '80022157-87f2-45d0-801b-0dd95a1e1ae4' # on the 2nd conversation and later
    leave3_node_uuid = '4144d45c-fe4d-46cf-96e0-cf34b27b4285' # on the 3rd conversation and later

    d.set_dialog_flags(leave_node_uuid, checkflags = (
        bg3.flag_group("Global", (
            bg3.flag(Shadowheart_Tav_State_Married.uuid, False, None),
        )),
    ))

    d.create_standard_dialog_node(
        leave2_node_uuid,
        bg3.SPEAKER_PLAYER,
        [],
        bg3.text_content('h6097a567g01cbg4809gafdag8fe5d42c1bb6', 1),
        constructor = bg3.dialog_object.QUESTION,
        end_node = True,
        checkflags = (
            bg3.flag_group("Local", (
                bg3.flag(Tav_Shadowheart_Epilogue_Convesation_3.uuid, False, None),
            )),
            bg3.flag_group("Global", (
                bg3.flag(Shadowheart_Tav_State_Married.uuid, True, None),
            )),
        ))

    d.create_standard_dialog_node(
        leave_joke_node_uuid,
        bg3.SPEAKER_PLAYER,
        [jump_to_dad_joke_node_uuid],
        bg3.text_content('h6097a567g01cbg4809gafdag8fe5d42c1bb6', 1),
        constructor = bg3.dialog_object.QUESTION,
        checkflags = (
            bg3.flag_group("Local", (
                bg3.flag(Tav_Shadowheart_Epilogue_Convesation_3.uuid, True, None),
            )),
            bg3.flag_group("Object", (
                bg3.flag(bg3.FLAG_EPI_Epilogue_Shadowheart_State_ToldDadJoke, False, speaker_idx_tav),
            )),
            bg3.flag_group("Global", (
                bg3.flag(Shadowheart_Tav_State_Married.uuid, True, None),
            )),
        ))
    d.create_jump_dialog_node(jump_to_dad_joke_node_uuid, first_dad_joke_node_uuid, 1)

    d.create_standard_dialog_node(
        leave3_node_uuid,
        bg3.SPEAKER_PLAYER,
        [],
        bg3.text_content('h6097a567g01cbg4809gafdag8fe5d42c1bb6', 1),
        constructor = bg3.dialog_object.QUESTION,
        end_node = True,
        checkflags = (
            bg3.flag_group("Local", (
                bg3.flag(Tav_Shadowheart_Epilogue_Convesation_3.uuid, True, None),
            )),
            bg3.flag_group("Object", (
                bg3.flag(bg3.FLAG_EPI_Epilogue_Shadowheart_State_ToldDadJoke, True, speaker_idx_tav),
            )),
            bg3.flag_group("Global", (
                bg3.flag(Shadowheart_Tav_State_Married.uuid, True, None),
            )),
        ))

    d.create_standard_dialog_node(
        more_terrible_jokes_to_share_node_uuid,
        bg3.SPEAKER_PLAYER,
        [not_with_that_sort_of_attitude_i_dont_node_uuid],
        bg3.text_content('h3d6b35f5gd073g4db3gbc74g63a5e62d55bb', 1),
        constructor = bg3.dialog_object.QUESTION,
        checkflags = (
            bg3.flag_group("Object", (
                bg3.flag(bg3.FLAG_EPI_Epilogue_Shadowheart_State_ToldDadJoke, True, speaker_idx_tav),
                bg3.flag(bg3.FLAG_EPI_Epilogue_Shadowheart_State_ToldSecondJoke, False, speaker_idx_tav),
            )),
            bg3.flag_group("Global", (
                bg3.flag(Shadowheart_Tav_State_Married.uuid, True, None),
            )),
            bg3.flag_group("Local", (
                bg3.flag(Tav_Shadowheart_Epilogue_Convesation_3.uuid, True, None),
            )),
        ),
        setflags = (
            bg3.flag_group("Object", (
                bg3.flag(bg3.FLAG_EPI_Epilogue_Shadowheart_State_ToldSecondJoke, True, speaker_idx_tav),
            )),
        ))
    d.create_standard_dialog_node(
        more_hilarious_jokes_for_me_node_uuid,
        bg3.SPEAKER_PLAYER,
        [hmm_let_me_see_node_uuid],
        bg3.text_content('h6a109bc3g1736g4a98g96bbg4265810e48ef', 1),
        constructor = bg3.dialog_object.QUESTION,
        checkflags = (
            bg3.flag_group("Object", (
                bg3.flag(bg3.FLAG_EPI_Epilogue_Shadowheart_State_ToldDadJoke, True, speaker_idx_tav),
                bg3.flag(bg3.FLAG_EPI_Epilogue_Shadowheart_State_ToldSecondJoke, False, speaker_idx_tav),
            )),
            bg3.flag_group("Global", (
                bg3.flag(Shadowheart_Tav_State_Married.uuid, True, None),
            )),
            bg3.flag_group("Local", (
                bg3.flag(Tav_Shadowheart_Epilogue_Convesation_3.uuid, True, None),
            )),
        ),
        setflags = (
            bg3.flag_group("Object", (
                bg3.flag(bg3.FLAG_EPI_Epilogue_Shadowheart_State_ToldSecondJoke, True, speaker_idx_tav),
            )),
        ))

    d.add_child_dialog_node(lets_make_tonight_count_node_uuid, more_terrible_jokes_to_share_node_uuid, 2)
    d.add_child_dialog_node(lets_make_tonight_count_node_uuid, more_hilarious_jokes_for_me_node_uuid, 2)
    d.add_child_dialog_node(lets_make_tonight_count_node_uuid, leave2_node_uuid)
    d.add_child_dialog_node(lets_make_tonight_count_node_uuid, leave_joke_node_uuid)
    d.add_child_dialog_node(lets_make_tonight_count_node_uuid, leave3_node_uuid)

    # Fix the flag
    # That joke was as funny as night orchids are poisonous.
    d.set_dialog_flags('4ac0bc72-40a5-e4da-638d-0ff976c5052b', checkflags = (
        bg3.flag_group("Global", (
            bg3.flag(bg3.FLAG_ORI_Shadowheart_State_NightsongPoint_GaveNightOrchid, True, None),
        )),
    ))

    # delete jump node in "Why thank you." 2a1c16bc-4f1a-7201-a45a-bc73c1014e47
    d.delete_dialog_node('34a81567-5606-942e-5170-309d2aaa28be')
    d.create_standard_dialog_node(
        '34a81567-5606-942e-5170-309d2aaa28be',
        bg3.SPEAKER_SHADOWHEART,
        ['063e75ba-eaa5-4b22-aef7-e4e4b47bb3cd', '41009498-69b1-486d-85c6-dabd530a0302'],
        None)
    d.create_standard_dialog_node(
        '063e75ba-eaa5-4b22-aef7-e4e4b47bb3cd',
        bg3.SPEAKER_SHADOWHEART,
        ['ec04113e-9cce-46f9-8d5a-dbd543365da5'],
        None,
        checkflags = (
            bg3.flag_group("Global", (
                bg3.flag(Shadowheart_Tav_State_Married.uuid, False, None),
            )),
        ))
    d.create_standard_dialog_node(
        '41009498-69b1-486d-85c6-dabd530a0302',
        bg3.SPEAKER_SHADOWHEART,
        ['3bf05175-1a9b-42f4-b56e-44e624371d8d'],
        None,
        checkflags = (
            bg3.flag_group("Global", (
                bg3.flag(Shadowheart_Tav_State_Married.uuid, True, None),
            )),
        ))
    d.create_jump_dialog_node('ec04113e-9cce-46f9-8d5a-dbd543365da5', '9877659d-1e2c-f4db-3822-f80804b0633f', 2)
    d.create_jump_dialog_node('3bf05175-1a9b-42f4-b56e-44e624371d8d', lets_make_tonight_count_node_uuid, 2)

    #
    # Extra dialogs
    #
    as_i_am_node_uuid = '68c0b864-3bf1-8892-6c02-f401260bf1f6' # existing node
    im_so_happy_to_be_with_you_node_uuid = '9cf5c4ff-3967-4c28-8428-dd605228dc54'
    alias_as_i_am_node_uuid = 'b27460e4-f165-41ca-a65f-c55e528ecc48'

    d.create_standard_dialog_node(
        im_so_happy_to_be_with_you_node_uuid,
        bg3.SPEAKER_PLAYER,
        [alias_as_i_am_node_uuid],
        bg3.text_content('h527425b6g1174g4464g8c4agee5e5c11dec8', 1),
        constructor = bg3.dialog_object.QUESTION,
        show_once = True,
        checkflags = (
            bg3.flag_group("Global", (
                bg3.flag(Shadowheart_Tav_State_Married.uuid, True, None),
            )),
        ))
    d.create_alias_dialog_node(alias_as_i_am_node_uuid, as_i_am_node_uuid, [])
    d.add_child_dialog_node(lets_make_tonight_count_node_uuid, im_so_happy_to_be_with_you_node_uuid, 2)

    #
    # God's favourite princess line
    #
    oh_hush_node_uuid = '96e1e145-b69b-2178-16ad-b50da1466c2d' # existing node
    of_course_i_do_node_uuid = 'bbd423f9-3291-8ff6-d4f8-35af16fb68f8' # existing node
    id_rather_just_be_alone_with_you_node_uuid = '7103bba0-d5da-403f-a52a-508904d6028e'
    alias_oh_hush_node_uuid = 'dc9ceefd-4de4-41b4-a787-e3232b784a78'
    whatever_you_say_i_love_hearing_it_node_uuid = '9c9b19f2-8636-4dbf-9851-4c25402ec2e3'
    demand_she_prove_her_point_node_uuid = '045ac801-c5ac-4b64-aaad-94e9e7d6cd07'
    gods_fav_princess_jump_back_node_uuid = '36e3802f-355c-4392-bf9f-2feb04f2be21'
    married_jump_back_node_uuid = '3d6c2699-1da9-4d5d-be94-78d915693900'
    not_married_jump_back_node_uuid = 'ba6137d5-bf54-4556-a11f-9c5180511945'
    non_maried_jump_target_node_uuid = '58e15bfc-bc7b-4833-cce3-23aedeedcc38'

    # I'd rather just be alone with you, honestly.
    d.create_standard_dialog_node(
        id_rather_just_be_alone_with_you_node_uuid,
        bg3.SPEAKER_PLAYER,
        [alias_oh_hush_node_uuid],
        bg3.text_content('h65ab510eg1a24g4e56g91a2g157b08ade6a1', 1),
        constructor = bg3.dialog_object.QUESTION,
        show_once = True,
        checkflags = (
            bg3.flag_group("Global", (
                bg3.flag(Shadowheart_Tav_State_Married.uuid, True, None),
            )),
            bg3.flag_group("Local", (
                bg3.flag(Tav_Shadowheart_Epilogue_Convesation_Voice.uuid, False, None),
                bg3.flag(Tav_Shadowheart_Epilogue_Convesation_3.uuid, True, None),
            )),
        ),
        setflags = (
            bg3.flag_group("Local", (
                bg3.flag(Tav_Shadowheart_Epilogue_Convesation_Voice.uuid, True, None),
            )),
        ))
    d.create_alias_dialog_node(alias_oh_hush_node_uuid, oh_hush_node_uuid, [])
    d.add_child_dialog_node(lets_make_tonight_count_node_uuid, id_rather_just_be_alone_with_you_node_uuid, 2)

    # Whatever you say, I love hearing it. I bet you like it too.
    d.create_standard_dialog_node(
        whatever_you_say_i_love_hearing_it_node_uuid,
        bg3.SPEAKER_PLAYER,
        [of_course_i_do_node_uuid],
        bg3.text_content('h19109ca4g50aeg4fbfgb8c7gb3c5c346c4be', 1),
        constructor = bg3.dialog_object.QUESTION,
        show_once = True,
        checkflags = (
            bg3.flag_group("Local", (
                bg3.flag(Tav_Shadowheart_Epilogue_Convesation_3.uuid, True, None),
            )),
            bg3.flag_group("Local", (
                bg3.flag(Tav_Shadowheart_Epilogue_Convesation_Voice.uuid, True, None),
            )),
        ),
        setflags = (
            bg3.flag_group("Local", (
                bg3.flag(Tav_Shadowheart_Epilogue_Convesation_Voice.uuid, False, None),
            )),
        ))
    d.add_child_dialog_node(lets_make_tonight_count_node_uuid, whatever_you_say_i_love_hearing_it_node_uuid, 3)

    # Demand she prove her point, and whisper a phrase for her to repeat.
    d.create_standard_dialog_node(
        demand_she_prove_her_point_node_uuid,
        bg3.SPEAKER_PLAYER,
        ['a3a7ba8a-d172-f342-ae0b-c073f4564b52'], # ... what the Hells does <i>that </i>mean?
        bg3.text_content('hc7ab8b3egd132g4c90gb643ga4306bacf4c2', 1),
        constructor = bg3.dialog_object.QUESTION,
        checkflags = (
            bg3.flag_group('Global', (
                bg3.flag(Shadowheart_Tav_State_Married.uuid, True, None),
            )),
        ))
    d.add_child_dialog_node(of_course_i_do_node_uuid, demand_she_prove_her_point_node_uuid)

    # This suppresses the "If you say so" line.
    d.add_dialog_flags('aa33612c-b49e-a42e-d6c8-272612a3f4f5', checkflags = (
        bg3.flag_group("Global", (
            bg3.flag(Shadowheart_Tav_State_Married.uuid, False, None),
        )),
    ))
    d.add_dialog_flags('9c0d2117-aaf5-90eb-de54-8f22a2de42c8', checkflags = (
        bg3.flag_group("Global", (
            bg3.flag(Shadowheart_Tav_State_Married.uuid, False, None),
        )),
    ))

    d.create_standard_dialog_node(
        gods_fav_princess_jump_back_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [married_jump_back_node_uuid, not_married_jump_back_node_uuid],
        None)
    d.create_standard_dialog_node(
        married_jump_back_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        ['8a49f9c8-0f0c-4533-8bbd-5c9a63ee2042'],
        None,
        checkflags = (
            bg3.flag_group("Global", (
                bg3.flag(Shadowheart_Tav_State_Married.uuid, True, None),
            )),
        ))
    d.create_jump_dialog_node('8a49f9c8-0f0c-4533-8bbd-5c9a63ee2042', lets_make_tonight_count_node_uuid, 2)
    d.create_standard_dialog_node(
        not_married_jump_back_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        ['127c6a12-ee52-4943-841d-9c8856bc6da4'],
        None,
        checkflags = (
            bg3.flag_group("Global", (
                bg3.flag(Shadowheart_Tav_State_Married.uuid, False, None),
            )),
        ))
    d.create_jump_dialog_node('127c6a12-ee52-4943-841d-9c8856bc6da4', non_maried_jump_target_node_uuid, 2)

    d.delete_dialog_node('842a614d-ca39-6cef-bff7-6a41f509c22d')
    d.delete_dialog_node('2f8ea3c6-8323-71d0-2ac8-62d2cce69cd9')
    d.delete_dialog_node('49179b10-af0f-afb1-b748-d9680112af1c')
    d.delete_dialog_node('b11faaed-a854-b841-6df0-1b5d1d53b1e6')

    nodes = (
        'ddf0ead2-afbf-7c93-f9be-54817563a9a1', # Ugh, the latrine's overflowing again - watch your step... oh I truly hope you're not speaking from experience.
        '0369b381-839c-4a9f-de5a-db18142a7acc', # Congratulations - I think I've sprained my tongue.
        '547a8dec-b696-5933-8010-6c4347be08bd', # Another time perhaps. Some undefined time in the far, distant future.
        'e3516cd6-5afc-4cad-6b85-8c854ea98034', # Mad as a sack of shaken geese, clearly. No wonder they got rid of her.
        'c0b3e9a6-3410-7d2b-6454-efb62f9d0ac2', # Some strange githyanki adage, I assume? I'm not sure I want to know...
    )
    for node in nodes:
        d.delete_all_children_dialog_nodes(node)
        d.add_child_dialog_node(node, gods_fav_princess_jump_back_node_uuid)

    # Spoilsport.
    # And proud of it.
    d.delete_all_children_dialog_nodes('dda562b8-f17c-69df-562b-6f548f9151bd')
    d.add_child_dialog_node('dda562b8-f17c-69df-562b-6f548f9151bd', '547a8dec-b696-5933-8010-6c4347be08bd')

    #
    # Fix emotions for:
    # Ugh, the latrine's overflowing again - watch your step... oh I truly hope you're not speaking from experience.
    # ddf0ead2-afbf-7c93-f9be-54817563a9a1
    #
    tl_phase = t.use_existing_phase(195)
    t.remove_effect_component('91b27e63-035b-8e34-a6aa-1d8297d69e2f')
    t.create_tl_actor_node(bg3.timeline_object.EMOTION, bg3.SPEAKER_SHADOWHEART, '0.0', tl_phase.duration, (
        t.create_emotion_key('0.0', 2, variation = 1),
        t.create_emotion_key('0.7', 1),
        t.create_emotion_key('4.86', 2, variation = 24),
        t.create_emotion_key('5.5', 2, variation = 2),
    ), is_snapped_to_end = True)

    # The last words of an infamous githyanki heretic, publicly executed generations ago by Vlaakith LXXIV.
    d.add_dialog_flags('7e2c202f-59dc-8836-d8b1-75d96eda603e', checkflags = (
        bg3.flag_group('Tag', (
            bg3.flag(bg3.TAG_REALLY_GITHYANKI, True, speaker_idx_tav),
        )),
    ))
    # Some strange githyanki adage, I assume? I'm not sure I want to know...
    d.add_dialog_flags('c0b3e9a6-3410-7d2b-6454-efb62f9d0ac2', checkflags = (
        bg3.flag_group('Tag', (
            bg3.flag(bg3.TAG_REALLY_GITHYANKI, True, speaker_idx_tav),
        )),
    ))

    alias_mad_as_a_sack_of_shaken_geese_node_uuid = 'c20019da-9fbb-43ee-bc4b-20db173bd3ca'
    mad_as_a_sack_of_shaken_geese_node_uuid = 'e3516cd6-5afc-4cad-6b85-8c854ea98034'
    d.create_alias_dialog_node(alias_mad_as_a_sack_of_shaken_geese_node_uuid, mad_as_a_sack_of_shaken_geese_node_uuid, [gods_fav_princess_jump_back_node_uuid])

    # ... I may be a hater and a gatekeeper, but I'm also god's favourite princess, and the most interesting girl in the world.
    d.add_child_dialog_node('ee2a2492-e168-2704-989a-036549b3df67', alias_mad_as_a_sack_of_shaken_geese_node_uuid)


bg3.add_build_procedure('create_conversation_epilogue_married_couple', create_conversation_epilogue_married_couple)

from __future__ import annotations

import bg3moddinglib as bg3

from .context import get_context
from .flags import *

# 9752ba41-f69d-4ef9-a29c-346f23265fb6 ShadowHeart_InParty2_Nested_BackgroundChapter
# It's just... something I have to live with.

def create_wound_ea_conversation() -> None:
    game_assets = get_context().assets
    files = get_context().files

    # ShadowHeart_InParty2
    # d76eaab3-040b-4871-9c1d-4a8624f37cd2 SH  -> SH
    # 0e8837db-4344-48d0-9175-12262c73806b SH  -> SH
    # 8942c483-83c9-4974-9f47-87cd1dd10828 Tav -> SH
    # b188e5c9-4ec1-456f-8408-b4a5da405cc5 Tav -> SH
    # 2b1dd4ed-5f01-46a2-a244-ac074d0feff0 Tav -> Tav
    # 95a53513-08ce-4d80-ae74-e306b51db565 Tav -> Tav
    # cde43894-62c3-4f23-8ea7-b772f9357697 Tav -> Tav
    # fd96b957-6a74-4f97-a035-eb9641c48242 SH  -> Tav

    # ShadowHeart_InParty2_Nested_BackgroundChapter
    # 489a3caa-497c-4dc9-9f4b-53f205d6d151 SH  -> SH
    # 0755706f-fbcd-4db8-85e5-d291c585e198 SH  -> SH
    # 98b9055b-78f8-4cc0-ad53-bcebff8543ae SH  -> Tav
    # d8e110c4-0021-4090-8280-10c376d66c20 SH  -> Tav
    # 0971d30b-bb12-4a62-9902-f931a83a215a SH  -> Tav
    # 71ac7742-ee0d-4b00-bbcd-59b14886f948 Tav -> SH
    # 1b4df08f-3658-4848-88ed-1fc81b688707 Tav -> SH
    # 7ca6622e-dabf-450d-9ddc-e75ebdb466b4 Tav -> SH
    # b25baf48-5c46-4a49-8984-8029a65e674d Tav -> Tav
    # 8353acff-3330-421a-a5fb-1472576ca21c Tav -> Tav


    ################################################################################################
    # Dialog: ShadowHeart_InParty2_Nested_BackgroundChapter.lsf
    ################################################################################################
    ab = game_assets.get_modded_dialog_asset_bundle('ShadowHeart_InParty2_Nested_BackgroundChapter')
    d = bg3.dialog_object(ab.dialog)
    t = bg3.timeline_object(ab.timeline, d)

    just_an_old_wound_node_uuid = 'eedfc924-72a2-4a35-ad6c-fd3a097cd936'
    something_i_have_to_live_with_node_uuid = '26a99bb5-3b32-4b61-ba17-cb88f9509952'

    why_do_you_think_it_happened_node_uuid = '33fa8da4-7bd8-4f6e-a927-563aee841d23'
    i_dont_know_node_uuid = '4e067f08-d978-4bff-9513-49c4003f0029'
    another_mystery_node_uuid = 'aea549ca-4c6f-4d21-9de9-8d2193b12751'
    is_it_dangerous_node_uuid = '865d5884-78b7-4183-b983-f791a5642763'
    very_node_uuid = '12041565-41e4-439e-9a40-b2e60a02562b'
    save_your_life_node_uuid = '054aa12a-1d68-406c-8f8b-9965e70db6df'
    i_dont_like_the_look_of_it_node_uuid = 'ab1fec87-c523-4af9-8c30-28d388bfe443'
    afraid_ill_turn_on_you_node_uuid = '94aeab03-e28d-4fa7-861e-dddc63b98162'
    ill_give_you_fair_warning_node_uuid = '69f05d18-b20b-42d1-b629-7540d9e892c6'
    i_didnt_have_odd_magical_flares_node_uuid = '911ea7b5-f71f-4038-815c-a7c838da069b'
    what_are_you_suggesting_exactly_node_uuid = '1fa45e43-b3a1-4df8-abc5-91a8f7a9b871'
    whatever_minor_difference_node_uuid = 'a24761d1-7ebb-4df3-8d9f-75fb23e5fca9'
    did_tadpole_cause_this_node_uuid = 'd1cb9dc3-482e-4449-a11e-f9f6d0c530b4'
    its_nothing_to_do_with_the_tadpoles_node_uuid = 'c75ad676-2a8b-4376-b0b5-463ba666b640'
    are_you_sure_its_not_connected_to_tadpoles_node_uuid = 'c4abfbf1-d67f-4f61-8d22-86e27fa63f48'

    how_badly_does_it_hurt_node_uuid = '61eef984-a851-4a5e-9af0-100472703fb2' # existing node
    turn_to_other_matters_node_uuid = '1367d18d-d748-444c-820f-7b30d9edf4e7' # existing node

    speaker_idx_shadowheart = d.get_speaker_slot_index(bg3.SPEAKER_SHADOWHEART)
    speaker_idx_tav = d.get_speaker_slot_index(bg3.SPEAKER_PLAYER)

    reaction_minus_2 = bg3.reaction_object.create_new(files, { bg3.SPEAKER_SHADOWHEART: -2 })
    reaction_minus_3 = bg3.reaction_object.create_new(files, { bg3.SPEAKER_SHADOWHEART: -3 })

    

    # # It's just an old wound that hurts me from time to time. Nothing to be concerned about.
    # d.create_standard_dialog_node(
    #     just_an_old_wound_node_uuid,
    #     bg3.SPEAKER_SHADOWHEART,
    #     [something_i_have_to_live_with_node_uuid],
    #     bg3.text_content('h3362a74ag82ccg4d3fgab28gbec49d35b203', 1),
    #     checkflags = (
    #         bg3.flag_group('Global', (
    #             bg3.flag(bg3.FLAG_ShadowHeart_InParty_Knows_SharWorshipper, False, None),
    #             bg3.flag(Really_Shadowheart_Softened_Version.uuid, False, None),
    #             bg3.flag(ReallyShadowheart_Ext_V2_0_0_0.uuid, True, None)
    #         )),
    #     ),
    #     setflags = (
    #         bg3.flag_group('Object', (
    #             bg3.flag(Shadowheart_Wound_Flare_Event_Mentioned_Tadpole.uuid, False, speaker_idx_tav),
    #             bg3.flag(Shadowheart_Wound_Flare_Event_Tav_Asked_About_Tadpole.uuid, False, speaker_idx_tav),
    #         )),
    #     ))
    # t.create_simple_dialog_answer_phase(
    #     bg3.SPEAKER_SHADOWHEART,
    #     '6.242',
    #     just_an_old_wound_node_uuid,
    #     ((None, '71ac7742-ee0d-4b00-bbcd-59b14886f948'),),
    #     emotions = {
    #         bg3.SPEAKER_SHADOWHEART: (('0.0', 64, None), ('1.32', 4, None), ('2.67', 4, 2), ('3.43', 4, None)),
    #     },
    #     performance_fade = 1.0,
    #     fade_in = 1.0,
    #     fade_out = 1.0)

    # # It's just... something I have to live with.
    # d.create_standard_dialog_node(
    #     something_i_have_to_live_with_node_uuid,
    #     bg3.SPEAKER_SHADOWHEART,
    #     [
    #         how_badly_does_it_hurt_node_uuid,
    #         did_tadpole_cause_this_node_uuid,
    #         are_you_sure_its_not_connected_to_tadpoles_node_uuid,
    #         why_do_you_think_it_happened_node_uuid,
    #         is_it_dangerous_node_uuid,
    #         i_dont_like_the_look_of_it_node_uuid,
    #         i_didnt_have_odd_magical_flares_node_uuid,
    #         turn_to_other_matters_node_uuid,
    #     ],
    #     bg3.text_content('h1e4eef49g7443g4635gac98g251fd5903087', 1))
    # t.create_simple_dialog_answer_phase(
    #     bg3.SPEAKER_SHADOWHEART,
    #     '3.179',
    #     something_i_have_to_live_with_node_uuid,
    #     (('3.1', '489a3caa-497c-4dc9-9f4b-53f205d6d151'), (None, '98b9055b-78f8-4cc0-ad53-bcebff8543ae')),
    #     emotions = {
    #         bg3.SPEAKER_SHADOWHEART: (('0.16', 64, None), ('1.32', 4, None), ('2.67', 4, 2), ('3.43', 4, None)),
    #     })

    # # Are you sure it's not connected to the tadpoles?
    # d.create_standard_dialog_node(
    #     are_you_sure_its_not_connected_to_tadpoles_node_uuid,
    #     bg3.SPEAKER_PLAYER,
    #     [
    #         '66ddbdda-e826-436e-9aca-07b19c95ac9d', # Positive. You can trust me on that.
    #         '09aee876-a353-47a1-854e-9e91ef4d175c', # I'm sure. 
    #     ],
    #     bg3.text_content('hebc1920fga154g421cg8c0dg82bbd511db5f', 1),
    #     constructor = bg3.dialog_object.QUESTION,
    #     # checkflags = (
    #     #     bg3.flag_group('Object', (
    #     #         bg3.flag(Shadowheart_Wound_Flare_Event_Tav_Asked_About_Tadpole.uuid, True, speaker_idx_tav),
    #     #     )),
    #     # ),
    #     show_once = True)


    # # Why do you think it happened right at that moment?
    # d.create_standard_dialog_node(
    #     why_do_you_think_it_happened_node_uuid,
    #     bg3.SPEAKER_PLAYER,
    #     [i_dont_know_node_uuid],
    #     bg3.text_content('hd7a3991bgf469g4ac5gaba9g205578c38b73', 1),
    #     constructor = bg3.dialog_object.QUESTION,
    #     # checkflags = (
    #     #     bg3.flag_group('Object', (
    #     #         bg3.flag(Shadowheart_Wound_Flare_Event_Mentioned_Tadpole.uuid, False, speaker_idx_tav),
    #     #     )),
    #     # ),
    #     show_once = True)

    # # I... I don't know. Something to do with the tadpole, who's to say?
    # d.create_standard_dialog_node(
    #     i_dont_know_node_uuid,
    #     bg3.SPEAKER_SHADOWHEART,
    #     [another_mystery_node_uuid],
    #     bg3.text_content('h0a662297g6e99g41e8g817ag7800e6b0a35c', 1),
    #     setflags = (
    #         bg3.flag_group('Object', (
    #             bg3.flag(Shadowheart_Wound_Flare_Event_Mentioned_Tadpole.uuid, True, speaker_idx_tav),
    #         )),
    #     ))
    # t.create_simple_dialog_answer_phase(
    #     bg3.SPEAKER_SHADOWHEART,
    #     '4.499',
    #     i_dont_know_node_uuid,
    #     ((None, '489a3caa-497c-4dc9-9f4b-53f205d6d151'),),
    #     emotions = {
    #         bg3.SPEAKER_SHADOWHEART: (('0.16', 64, None), ('1.32', 4, None), ('2.67', 4, 2), ('3.43', 4, None)),
    #     })

    # # Another mystery to add to the pile.
    # d.create_standard_dialog_node(
    #     another_mystery_node_uuid,
    #     bg3.SPEAKER_SHADOWHEART,
    #     [
    #         how_badly_does_it_hurt_node_uuid,
    #         did_tadpole_cause_this_node_uuid,
    #         are_you_sure_its_not_connected_to_tadpoles_node_uuid,
    #         why_do_you_think_it_happened_node_uuid,
    #         is_it_dangerous_node_uuid,
    #         i_dont_like_the_look_of_it_node_uuid,
    #         i_didnt_have_odd_magical_flares_node_uuid,
    #         turn_to_other_matters_node_uuid,
    #     ],
    #     bg3.text_content('h48e80bb6g3326g4b65ga010g32f31682cf4d', 1))
    # t.create_simple_dialog_answer_phase(
    #     bg3.SPEAKER_SHADOWHEART,
    #     '2.2',
    #     another_mystery_node_uuid,
    #     (('2.1', '0755706f-fbcd-4db8-85e5-d291c585e198'), (None, '0971d30b-bb12-4a62-9902-f931a83a215a')),
    #     fade_in = 0.0,
    #     fade_out = 1.0,
    #     performance_fade = 1.0,
    #     emotions = {
    #         bg3.SPEAKER_SHADOWHEART: (('0.2', 64, None), ('1.85', 4, 2)),
    #     })

    # I'm worried it could hurt me. How dangerous is it?
    d.create_standard_dialog_node(
        is_it_dangerous_node_uuid,
        bg3.SPEAKER_PLAYER,
        [very_node_uuid],
        bg3.text_content('h7fc2d5d7g33e5g4811g9541gcb3a9dbbdc4f', 1),
        constructor = bg3.dialog_object.QUESTION,
        show_once = True,
        checkflags = (
            bg3.flag_group('Global', (
                bg3.flag(Really_Shadowheart_Softened_Version.uuid, False, None),
                bg3.flag(ReallyShadowheart_Ext_V2_0_0_0.uuid, True, None)
            )),
        ))

    # Very. It wanted to lash out at you.
    d.create_standard_dialog_node(
        very_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [save_your_life_node_uuid],
        bg3.text_content('hb8aaf34bg3c83g4c68ga568g5a0d9d859271', 1),
        approval_rating_uuid = reaction_minus_3.uuid)
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '3.136',
        very_node_uuid,
        ((None, '489a3caa-497c-4dc9-9f4b-53f205d6d151'),),
        emotions = {
            bg3.SPEAKER_SHADOWHEART: (('0.28', 2, None), ('1.01', 4, 2)),
        })

    # Luckily I was there to stop it and save your life. Anything else?
    d.create_standard_dialog_node(
        save_your_life_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [],
        bg3.text_content('h84687a07g722eg4891ga3fcg981bb6daafd2', 1))
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '4.045',
        save_your_life_node_uuid,
        (('3.95', '489a3caa-497c-4dc9-9f4b-53f205d6d151'), (None, 'd8e110c4-0021-4090-8280-10c376d66c20')),
        emotions = {
            bg3.SPEAKER_SHADOWHEART: (('0.24', 64, None), ('3.07', 4, 2)),
        },
        fade_in = 1.5,
        fade_out = 0.0,
        performance_fade = 1.5)

    # I don't like the look of it. I'll keep an eye on you, just in case.
    d.create_standard_dialog_node(
        i_dont_like_the_look_of_it_node_uuid,
        bg3.SPEAKER_PLAYER,
        [afraid_ill_turn_on_you_node_uuid],
        bg3.text_content('ha4c29745g1474g400fgb120g867c851ba716', 1),
        constructor = bg3.dialog_object.QUESTION,
        show_once = True,
        checkflags = (
            bg3.flag_group('Global', (
                bg3.flag(Really_Shadowheart_Softened_Version.uuid, False, None),
                bg3.flag(ReallyShadowheart_Ext_V2_0_0_0.uuid, True, None)
            )),
        ))

    # Why, afraid I'll turn on you? 
    d.create_standard_dialog_node(
        afraid_ill_turn_on_you_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [ill_give_you_fair_warning_node_uuid],
        bg3.text_content('h80047ff5gfb98g4429gb75ag13ad83321d99', 1))
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '2.212',
        afraid_ill_turn_on_you_node_uuid,
        ((None, '0755706f-fbcd-4db8-85e5-d291c585e198'),),
        emotions = {
            bg3.SPEAKER_SHADOWHEART: (('0.16', 64, None), ('1.53', 4, None)),
        })

    # Don't worry. I'll give you fair warning when it comes to that.
    d.create_standard_dialog_node(
        ill_give_you_fair_warning_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [],
        bg3.text_content('hc138cb58gef9fg4c8bg945egc36a6d2e8f72', 1))
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '3.890',
        ill_give_you_fair_warning_node_uuid,
        (('3.8', '489a3caa-497c-4dc9-9f4b-53f205d6d151'), (None, 'd8e110c4-0021-4090-8280-10c376d66c20')),
        emotions = {
            bg3.SPEAKER_SHADOWHEART: (('0.13', 64, None), ('1.82', 8, None)),
        })

    # Hmmm. I didn't have odd magical flares since I was infected.
    d.create_standard_dialog_node(
        i_didnt_have_odd_magical_flares_node_uuid,
        bg3.SPEAKER_PLAYER,
        [what_are_you_suggesting_exactly_node_uuid],
        bg3.text_content('hce38ab83ga0afg4fdfg95c1gb4c3fa8fe151', 1),
        constructor = bg3.dialog_object.QUESTION,
        show_once = True,
        checkflags = (
            bg3.flag_group('Global', (
                bg3.flag(Really_Shadowheart_Softened_Version.uuid, False, None),
                bg3.flag(ReallyShadowheart_Ext_V2_0_0_0.uuid, True, None)
            )),
        ))

    # What are you suggesting exactly? That my tadpole's worse than yours or something?
    d.create_standard_dialog_node(
        what_are_you_suggesting_exactly_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [whatever_minor_difference_node_uuid],
        bg3.text_content('h664f3719g4019g4fcfg9b0fg67576b6311b8', 1),
        approval_rating_uuid = reaction_minus_2.uuid,
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(Shadowheart_Wound_Flare_Event_Mentioned_Tadpole.uuid, True, speaker_idx_tav),
            )),
        ))
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '4.530',
        what_are_you_suggesting_exactly_node_uuid,
        ((None, '1b4df08f-3658-4848-88ed-1fc81b688707'),),
        emotions = {
            bg3.SPEAKER_SHADOWHEART: (('0.22', 8, None), ('2.41', 4, 2), ('3.38', 64, 1)),
        })

    # Whatever minor difference you think you've noticed will hardly matter if we don't find a cure. Keep focused.
    d.create_standard_dialog_node(
        whatever_minor_difference_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [],
        bg3.text_content('h387cc5e3gc467g4b25g8e85gdbaf99e4d4db', 1))
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '6.893',
        whatever_minor_difference_node_uuid,
        (('6.7', '0755706f-fbcd-4db8-85e5-d291c585e198'), (None, '0971d30b-bb12-4a62-9902-f931a83a215a')),
        emotions = {
            bg3.SPEAKER_SHADOWHEART: (('0.27', 64, None), ('1.39', 4, None), ('3.77', 8, 1), ('5.9', 8, 3)),
        })

    d.add_child_dialog_node('9752ba41-f69d-4ef9-a29c-346f23265fb6', i_didnt_have_odd_magical_flares_node_uuid, 0)
    d.add_child_dialog_node('9752ba41-f69d-4ef9-a29c-346f23265fb6', i_dont_like_the_look_of_it_node_uuid, 0)
    d.add_child_dialog_node('9752ba41-f69d-4ef9-a29c-346f23265fb6', is_it_dangerous_node_uuid, 0)

    # jump_node_uuid = '5248901e-a344-4c33-8195-f1716c4e5c94'
    # d.create_jump_dialog_node(jump_node_uuid, just_an_old_wound_node_uuid, 1)

    # d.add_child_dialog_node('3b98b584-0171-4432-9948-12b24e5cece2', jump_node_uuid, 0)
    # d.add_child_dialog_node('4ee7f57d-ce1d-faef-9c79-4924bade288a', just_an_old_wound_node_uuid, 0)


bg3.add_build_procedure('create_wound_ea_conversation', create_wound_ea_conversation)

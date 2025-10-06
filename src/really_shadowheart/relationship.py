from __future__ import annotations

import bg3moddinglib as bg3

from .context import game_assets
from .dialog_overrides import add_dialog_dependency, get_dialog_uuid
from .flags import *


of_course_node_uuid = '23749c85-4289-4965-a7db-1909f5cb63a2' # existing node

def patch_relationship_conversations() -> None:
    ################################################################################################
    # Dialog: ShadowHeart_InParty2_Nested_DefaultChapter.lsf
    # New response to "Admit it - you've never had a relationship quite like this one, have you?"
    ################################################################################################

    # d = bg3.dialog_object(files.get_file('Gustav', 'Mods/GustavDev/Story/DialogsBinary/Companions/ShadowHeart_InParty2_Nested_DefaultChapter.lsf'))
    # t = bg3.timeline_object(files.get_file('Gustav', 'Public/GustavDev/Timeline/Generated/ShadowHeart_InParty2_Nested_DefaultChapter.lsf'), d)

    ab = game_assets.get_modded_dialog_asset_bundle('ShadowHeart_InParty2_Nested_DefaultChapter')
    d = bg3.dialog_object(ab.dialog)
    t = bg3.timeline_object(ab.timeline, d)

    # speaker slot indexes
    slot_idx_shadowheart = d.get_speaker_slot_index(bg3.SPEAKER_SHADOWHEART)
    slot_idx_tav = d.get_speaker_slot_index(bg3.SPEAKER_PLAYER)

    shadowheart_enemy_of_shar_true = bg3.flag_group('Global', (bg3.flag(Shadowheart_Turned_Away_From_Shar.uuid, True, None),))
    shadowheart_enemy_of_shar_false = bg3.flag_group('Global', (bg3.flag(Shadowheart_Turned_Away_From_Shar.uuid, False, None),))

    admit_it_node_uuid = '1768e8f4-7100-448d-8422-dd41ded1014d'
    even_if_i_could_remember_node_uuid = '067285cc-d3e7-4190-b785-7d4a61bad7d3'
    the_way_i_was_raised_node_uuid = '1921ef97-3e74-4194-88a9-94d4b4c10fb1'
    a_lots_changed_node_uuid = 'cd6593a9-b021-4721-b370-7f68e934ded4'
    i_sougth_to_confide_node_uuid = 'aa276109-e497-4c76-97f7-3b42c43fd47e'

    # The way I was raised, the way I was trained... well, it was positively encouraged, to get to know each other. Even from the memories I can recall, there's stories I could tell you...
    d.create_standard_dialog_node(
        the_way_i_was_raised_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [a_lots_changed_node_uuid],
        bg3.text_content('h58d907fbg3657g4f4egbca2g4542dd67e653', 3, '5b255972-c650-4464-a852-b0be05d4872f'),
        checkflags=(shadowheart_enemy_of_shar_true,)
    )
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '15.948',
        the_way_i_was_raised_node_uuid,
        (
            ('9.948', '7b067edd-f53f-49e1-95bc-0986e6e2ca2f'),
            (None,  '0e8837db-4344-48d0-9175-12262c73806b'),
        ),
        emotions={
            bg3.SPEAKER_SHADOWHEART: ((0.0, 1024, 1), (2.765, 1024, None), (6.046, 1024, 2), (9.948, 1024, 3), (13.3, 1024, 1)),
            bg3.SPEAKER_PLAYER: ((0.0, 1024, None),)
        }
    )

    # A lot's changed since then. More than I ever thought was possible.
    d.create_standard_dialog_node(
        a_lots_changed_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [i_sougth_to_confide_node_uuid],
        bg3.text_content('h0d2027f1g386eg45bbg8a6ag7ab77f651a6c', 1, '6727877f-b790-4b32-9896-53e5dd621b28')
    )
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '4.334',
        a_lots_changed_node_uuid,
        ((None, '7b067edd-f53f-49e1-95bc-0986e6e2ca2f'),),
        emotions={
            bg3.SPEAKER_SHADOWHEART: ((0.0, 16, None), (2.14, 2, None), (3.4, 2, 1)),
            bg3.SPEAKER_PLAYER: ((0.0, 1, None),)
        }
    )

    # It's difficult to put into words... I can't remember the last time I sought to confide in someone like this - maybe I never have, for all I know. But now it just feels... right.
    d.create_standard_dialog_node(
        i_sougth_to_confide_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [],
        bg3.text_content('h9b00b4fbgd0e0g4bbcgadc0gdbea99682ab5', 1)
    )
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '14.938',
        i_sougth_to_confide_node_uuid,
        (
            ('2.538', 'b4155335-5e08-4d85-8ccd-ddebf5507447'),
            (None,  '7b067edd-f53f-49e1-95bc-0986e6e2ca2f')
        ),
        emotions={
            bg3.SPEAKER_SHADOWHEART: ((0.0, 16, None), (4.14, 16, 1), (8.34, 16, 2), (11.8, 2, None)),
            bg3.SPEAKER_PLAYER: ((0.0, 64, None), (0.5, 1, None), (1.55, 64, None))
        }
    )

    d.set_dialog_flags(even_if_i_could_remember_node_uuid, checkflags=[shadowheart_enemy_of_shar_false])
    d.add_child_dialog_node(admit_it_node_uuid, the_way_i_was_raised_node_uuid, 0)

    ################################################################################################
    # The following replaces 'Of course' with 'I'm all ears'.
    ################################################################################################

    # '74ebad47-6406-491b-bca9-57811fbe17c3' Shar path 'of course' node
    of_course_but_node_uuid = '74ebad47-6406-491b-bca9-57811fbe17c3' # existing node
    im_all_ears_node_uuid = '3250b885-192c-4feb-93bd-e36be3c1362b'
    jump_to_of_course_node_uuid = '7cf8a483-3d1b-4972-a2d7-cc37f0d217d5' # existing node

    lover_conversation_event_flag = '22c04792-d5fc-4285-b45d-95c7df986e47'

    d.create_standard_dialog_node(
        im_all_ears_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [jump_to_of_course_node_uuid],
        bg3.text_content('he88e5a7ag2d50g4665gb852gd09d30a20fea', 1),
        constructor = bg3.dialog_object.GREETING,
        root = True,
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(lover_conversation_event_flag, True, slot_idx_tav),
            )),
        ),
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(lover_conversation_event_flag, False, slot_idx_tav),
            )),
        ))
    t.create_new_voice_phase_from_another(
        of_course_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        '2.03',
        im_all_ears_node_uuid,
        skip_tl_nodes = ('TLShot',),
        phase_duration = '2.3',
        emotions = {
            bg3.SPEAKER_SHADOWHEART: [(0.0, 2, None),],
        })
    t.create_tl_shot(
        'd76eaab3-040b-4871-9c1d-4a8624f37cd2',
        '0.0',
        '2.0')
    t.create_tl_shot(
        'e08db860-1e62-4271-bf4e-d51602468573',
        '2.0',
        '2.3',
        is_snapped_to_end = True)

    # d.delete_dialog_node('da8bcbbb-7d69-4ac0-94f6-dd7b7be3174c')
    # d.create_jump_dialog_node('da8bcbbb-7d69-4ac0-94f6-dd7b7be3174c', im_all_ears_node_uuid, 2)

    # d.delete_dialog_node('7cf8a483-3d1b-4972-a2d7-cc37f0d217d5')
    # d.create_jump_dialog_node('7cf8a483-3d1b-4972-a2d7-cc37f0d217d5', im_all_ears_node_uuid, 2)

    insert_at_index = d.get_root_node_index(of_course_node_uuid)
    d.remove_root_node(of_course_node_uuid)
    d.add_root_node(im_all_ears_node_uuid, index = insert_at_index)


    ################################################################################################
    # Fix flags on the "Of course - but remember. Lady Shar comes first." line
    ################################################################################################
    d.set_dialog_flags(of_course_but_node_uuid, checkflags = (
        bg3.flag_group('Global', (
            bg3.flag(Shadowheart_Turned_Away_From_Shar.uuid, False, None),
        )),
        bg3.flag_group('Object', (
            bg3.flag(lover_conversation_event_flag, True, slot_idx_tav),
        )),
    ))


    ################################################################################################
    # It'll make for quite a bedtime tale for the children, if you ever get me in a family way.
    # Shadowheart will only say that line if her approval of Tav is >= 60
    ################################################################################################

    d.set_dialog_flags('639cab1b-8130-44b5-8f37-73502e1c33b2', checkflags = (
        bg3.flag_group('Object', (
            bg3.flag(bg3.FLAG_ORI_State_PartneredWithShadowheart, True, slot_idx_tav),
            bg3.flag(bg3.FLAG_Approval_AtLeast_60_For_Sp2, True, slot_idx_shadowheart),
        )),
        bg3.flag_group('Global', (
            bg3.flag(Shadowheart_Turned_Away_From_Shar.uuid, True, None),
        ))
    ))
    d.set_dialog_flags('f6f5ea4d-1c9e-46c7-9c7f-2a881c042032', checkflags = (
        bg3.flag_group('Global', (
            bg3.flag(Shadowheart_Turned_Away_From_Shar.uuid, True, None),
        )),
    ))
    d.create_standard_dialog_node(
        '4c3bff11-b11b-4961-a9ed-8113a71192c8',
        bg3.SPEAKER_SHADOWHEART,
        ['12a98b7f-d3f5-46e6-b273-574254d88f1d'],
        None,
        checkflags = (
            bg3.flag_group('Global', (
                bg3.flag(Shadowheart_Turned_Away_From_Shar.uuid, False, None),
            )),
        ))
    d.create_jump_dialog_node('12a98b7f-d3f5-46e6-b273-574254d88f1d', '9f7d4510-e658-4b23-b066-4fe117fbba7b', 2)
    d.add_child_dialog_node('0524e061-c351-4bed-b6d8-f89067c3de10', '4c3bff11-b11b-4961-a9ed-8113a71192c8')


    ################################################################################################
    # I want to end things between us.
    # This is to prevent accidental break up
    ################################################################################################

    i_want_to_end_things_node_uuid = '8bf568b9-62fa-4c6f-9166-736af8cc150c' # existing node

    your_loss_then_node_uuid = 'df636441-eb0c-494a-81c8-2331a9e813a4'
    just_like_that_node_uuid = 'b7e53d90-9daf-4a5b-8731-60ee57d5942c'
    i_was_mistaken_node_uuid = 'c00bbcb8-d431-47f6-acde-a1c8556c8125'
    oopsie_node_uuid = '02f366cb-d265-49c9-b038-a963d11400e2'
    end_this_now_node_uuid = '9ca5e811-1b05-4877-8c02-8a0091e845ac'
    i_dont_know_what_you_mean_node_uuid = '78d68f1f-b6c8-4622-8633-278f356d8a01'
    gather_your_thoughts_node_uuid = 'bd9f27aa-59e1-477a-a35c-3e877eeeb107'

    reaction_minus_10 = bg3.reaction_object.create_new(files, { bg3.SPEAKER_SHADOWHEART : -10 }, uuid = 'fc7711e6-e5d6-47bb-ae00-669228590930')

    # Your loss then. If you're struck down in the battles to come, remember that you refused Lady Shar's shield.
    d.create_standard_dialog_node(
        your_loss_then_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [],
        bg3.text_content('h1322d131g42c6g4541g98ceg89f14f931e67', 2),
        checkflags = (
            bg3.flag_group('Global', (
                bg3.flag(Shadowheart_Turned_Away_From_Shar.uuid, False, None),
            )),
        ),
        setflags = (
             bg3.flag_group('Object', (
                 bg3.flag(bg3.FLAG_ORI_State_PartneredWithShadowheart, False, slot_idx_tav),
                 bg3.flag(bg3.FLAG_ORI_State_WasPartneredWithShadowheart, True, slot_idx_tav),
             )),
        ),
        end_node = True)
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '7.5',
        your_loss_then_node_uuid,
        (('7.8', '7b067edd-f53f-49e1-95bc-0986e6e2ca2f'), (None, 'e08db860-1e62-4271-bf4e-d51602468573')),
        phase_duration = '8.0',
        emotions={
            bg3.SPEAKER_SHADOWHEART: ((0.0, 128, None), (2.06, 4, 3)),
            bg3.SPEAKER_PLAYER: ((0.0, 64, None),)
        })


    # Just like that...? I thought we had something special. Something lasting.
    d.create_standard_dialog_node(
        just_like_that_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [oopsie_node_uuid, end_this_now_node_uuid],
        bg3.text_content('h656ea716g6c7fg4810g9a40g7a4faf11bd91', 1),
        checkflags = (
            bg3.flag_group('Global', (
                bg3.flag(Shadowheart_Turned_Away_From_Shar.uuid, True, None),
            )),
        ))
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '6.75',
        just_like_that_node_uuid,
        (('6.75', '7b067edd-f53f-49e1-95bc-0986e6e2ca2f'), (None, 'e08db860-1e62-4271-bf4e-d51602468573')),
        phase_duration = '6.8',
        emotions={
            bg3.SPEAKER_SHADOWHEART: ((0.0, 16, 1), (2.78, 16, 2), (4.33, 32, None), (5.91, 2048, None)),
            bg3.SPEAKER_PLAYER: ((0.0, 64, None),)
        })

    # Oopsie, my love... I accidentally clicked the wrong option in the dialog.
    d.create_standard_dialog_node(
         oopsie_node_uuid,
         bg3.SPEAKER_PLAYER,
         [i_dont_know_what_you_mean_node_uuid],
         bg3.text_content('h7df66cf3g43c8g4d4dg9581ga29d9779951b', 1),
         constructor = bg3.dialog_object.QUESTION)

    # I realized we are too poor of a match. It'd be better to end this now.
    d.create_standard_dialog_node(
         end_this_now_node_uuid,
         bg3.SPEAKER_PLAYER,
         [i_was_mistaken_node_uuid],
         bg3.text_content('hd6147aa7g76feg48a5g8c11g3f734c02a5a4', 1),
         setflags = (
             bg3.flag_group('Object', (
                 bg3.flag(bg3.FLAG_ORI_State_PartneredWithShadowheart, False, slot_idx_tav),
                 bg3.flag(bg3.FLAG_ORI_State_WasPartneredWithShadowheart, True, slot_idx_tav),
             )),
         ),
         constructor = bg3.dialog_object.QUESTION)

    # # I don't know what you mean.
    # d.create_standard_dialog_node(
    #     i_dont_know_what_you_mean_node_uuid,
    #     bg3.SPEAKER_SHADOWHEART,
    #     [gather_your_thoughts_node_uuid],
    #     bg3.text_content('hefb7aa04g56a6g46edg94f7g4d84e3dcc77e', 1))
    # t.create_simple_dialog_answer_phase(
    #     bg3.SPEAKER_SHADOWHEART,
    #     1.64,
    #     i_dont_know_what_you_mean_node_uuid,
    #     ((None, '0e8837db-4344-48d0-9175-12262c73806b'),),
    #     phase_duration = 2.0,
    #     emotions = {
    #         bg3.SPEAKER_SHADOWHEART: ((0.0, 32, None),)
    #     })

    # I don't know what you're talking about. I suspect <i>you </i>don't know what you're talking about.
    d.create_standard_dialog_node(
        i_dont_know_what_you_mean_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [gather_your_thoughts_node_uuid],
        bg3.text_content('h7228d91fg9ab8g4854g91b0g54dda6e78438', 1))
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '4.84',
        i_dont_know_what_you_mean_node_uuid,
        ((None, '0e8837db-4344-48d0-9175-12262c73806b'),),
        phase_duration = '4.9',
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 64, None), (1.95, 4, None), (3.89, 64, None)),
            bg3.SPEAKER_PLAYER: ((0.0, 64, None),),
        })


    # Gather your thoughts. Then perhaps we can talk some more.
    d.create_standard_dialog_node(
        gather_your_thoughts_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [],
        bg3.text_content('h316517e1g18b2g41f3g91deg1900c4cdb48a', 1),
        end_node = True
    )
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '4.21',
        gather_your_thoughts_node_uuid,
        (('4.21', 'd76eaab3-040b-4871-9c1d-4a8624f37cd2'), (None, 'e08db860-1e62-4271-bf4e-d51602468573')),
        phase_duration = '4.3',
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 8, None),),
            bg3.SPEAKER_PLAYER: ((0.0, 64, None),),
        })


    # Clearly I was mistaken. But at least it's a mistake I won't make twice.
    d.create_standard_dialog_node(
        i_was_mistaken_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [],
        bg3.text_content('hc4496b0eg4c3eg43e4g8597g1b40e9dd0395', 1),
        end_node = True,
        approval_rating_uuid = reaction_minus_10.uuid)
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '5.29',
        i_was_mistaken_node_uuid,
        (('5.29', '0e8837db-4344-48d0-9175-12262c73806b'), (None, 'e08db860-1e62-4271-bf4e-d51602468573')),
        phase_duration = '5.4',
        emotions={
            bg3.SPEAKER_SHADOWHEART: ((0.0, 2048, 1), (0.21, 128, None), (3.12, 128, 1),),
            bg3.SPEAKER_PLAYER: ((0.0, 64, None),)
        })


    d.set_dialog_flags(i_want_to_end_things_node_uuid, setflags = ())
    d.delete_all_children_dialog_nodes(i_want_to_end_things_node_uuid)
    d.add_child_dialog_node(i_want_to_end_things_node_uuid, your_loss_then_node_uuid)
    d.add_child_dialog_node(i_want_to_end_things_node_uuid, just_like_that_node_uuid)

    ################################################################################################
    # How are you faring?
    # Modded answers to this question.
    ################################################################################################

    how_are_you_node_uuid = 'd6882eaf-132e-440e-8416-4b2fa547506a' # existing node
    how_are_you_faring_node_uuid = '0a72a161-8baa-483e-baf2-afa6f93ca8f0' # existing node
    always_good_when_im_with_you_node_uuid = '204d7c3a-fe80-4dd7-a3ff-5b149033a43b' # existing node
    always_good_when_im_with_you_scl_node_uuid = '98004b3e-1268-4450-9a44-a6bd6399a978' # existing node

    # Always good, when I'm with you.
    alias_to_always_good_when_im_with_you_act1_node_uuid = '9145fd6e-06b6-42c7-b2b9-4e763b2d5b6c'
    d.create_alias_dialog_node(
        alias_to_always_good_when_im_with_you_act1_node_uuid,
        always_good_when_im_with_you_node_uuid,
        [],
        checkflags = (
            bg3.flag_group('Global', (
                bg3.flag(bg3.FLAG_CURRENTREGION_SCL_Main_A, False, None),
                bg3.flag(bg3.FLAG_VISITEDREGION_INT_Main_A_ACT_3, False, None),
            )),
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_State_DatingShadowheart, True, slot_idx_tav),
                bg3.flag(bg3.FLAG_Approval_AtLeast_40_For_Sp2, True, slot_idx_shadowheart),
            ))
        ),
        end_node = True)

    # Always good, when I'm with you - even in perilous lands such as these.
    alias_to_always_good_when_im_with_you_act2_node_uuid = 'e7da318a-7626-4a71-bdd5-7c7a5d55f321'
    d.create_alias_dialog_node(
        alias_to_always_good_when_im_with_you_act2_node_uuid,
        always_good_when_im_with_you_scl_node_uuid,
        [],
        checkflags = (
            bg3.flag_group('Global', (
                bg3.flag(bg3.FLAG_CURRENTREGION_SCL_Main_A, True, None),
            )),
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_State_DatingShadowheart, True, slot_idx_tav),
                bg3.flag(bg3.FLAG_Approval_AtLeast_40_For_Sp2, True, slot_idx_shadowheart),
            ))
        ),
        end_node = True)

    # Always good, when I'm with you.
    alias_to_always_good_when_im_with_you_act3_node_uuid = '7707aece-560a-4841-9871-808edef8c087'
    d.create_alias_dialog_node(
        alias_to_always_good_when_im_with_you_act3_node_uuid,
        always_good_when_im_with_you_node_uuid,
        [],
        checkflags = (
            bg3.flag_group('Global', (
                bg3.flag(bg3.FLAG_VISITEDREGION_INT_Main_A_ACT_3, True, None),
            )),
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_State_PartneredWithShadowheart, True, slot_idx_tav),
                bg3.flag(bg3.FLAG_Approval_AtLeast_40_For_Sp2, True, slot_idx_shadowheart),
            )),
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_REALLY_DARK_URGE, False, slot_idx_tav),
            ))
        ),
        end_node = True)

    # Always good, when I'm with you.
    alias_to_always_good_when_im_with_you_act3_durge_node_uuid = 'a81b2164-28bb-4984-bdd6-aa7b17117eae'
    d.create_alias_dialog_node(
        alias_to_always_good_when_im_with_you_act3_durge_node_uuid,
        always_good_when_im_with_you_node_uuid,
        [],
        checkflags = (
            bg3.flag_group('Global', (
                bg3.flag(bg3.FLAG_VISITEDREGION_INT_Main_A_ACT_3, True, None),
                bg3.flag(bg3.FLAG_ORI_DarkUrge_State_BhaalAccepted, False, None),
            )),
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_State_PartneredWithShadowheart, True, slot_idx_tav),
                bg3.flag(bg3.FLAG_Approval_AtLeast_40_For_Sp2, True, slot_idx_shadowheart),
            )),
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_REALLY_DARK_URGE, True, slot_idx_tav),
            ))
        ),
        end_node = True)

    # I'm fine.
    im_fine_node_uuid = 'c0a7709f-b5b9-4273-bec4-46936806c9ac'
    d.create_standard_dialog_node(
        im_fine_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [],
        bg3.text_content('h0e667597gc7c0g47ebg9e53g790f7da74b3f', 1),
        end_node = True)
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '1.25',
        im_fine_node_uuid,
        (('1.2', 'e7f21f15-f386-40f4-bb0f-2f9f42249ad1'), (None, 'a5043f00-72f3-49fe-a24f-fce1e268d896')),
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 1, None),),
            bg3.SPEAKER_PLAYER: ((0.0, 1, None),)
        })


    d.delete_all_children_dialog_nodes(how_are_you_faring_node_uuid)
    d.add_child_dialog_node(how_are_you_faring_node_uuid, alias_to_always_good_when_im_with_you_act1_node_uuid)
    d.add_child_dialog_node(how_are_you_faring_node_uuid, alias_to_always_good_when_im_with_you_act2_node_uuid)
    d.add_child_dialog_node(how_are_you_faring_node_uuid, alias_to_always_good_when_im_with_you_act3_node_uuid)
    d.add_child_dialog_node(how_are_you_faring_node_uuid, alias_to_always_good_when_im_with_you_act3_durge_node_uuid)
    d.add_child_dialog_node(how_are_you_faring_node_uuid, im_fine_node_uuid)


    # rehearsal_node_uuid = '4669348d-640c-4d09-9b2b-cc9862e3f626'
    # every_day_is_an_adventure_node_uuid = '0bc3d936-8a92-4f4e-bc51-26658a78c35b'
    # did_you_want_something_node_uuid = 'f7e507b8-80f0-4f29-ba83-94f872db1329'

    # d.create_standard_dialog_node(
    #     rehearsal_node_uuid,
    #     bg3.SPEAKER_PLAYER,
    #     [every_day_is_an_adventure_node_uuid],
    #     bg3.text_content('h8ce2f791g872eg4e96g9fc9g28bf3bf54a34', 1),
    #     constructor = bg3.dialog_object.QUESTION)

    # 7b067edd-f53f-49e1-95bc-0986e6e2ca2f
    #d.add_child_dialog_node(of_course_node_uuid, rehearsal_node_uuid, 0)

    #fallback_node_uuid = '8747037f-084c-4e25-a039-c798ac3f7864'
    #d.create_jump_dialog_node(fallback_node_uuid, how_are_you_node_uuid, 2)


    i_wanted_to_tell_something_node_uuid = '2a96a513-cab2-4cef-992a-77563f54e7de'
    i_wanted_to_tell_something_durge_node_uuid = '633941f0-0e2a-441f-860b-b38a1ec9d458'
    alls_well_i_hope_node_uuid = '7c7211ec-93be-4ae4-9115-aca10e2ba0c4'
    confession_v1_node_uuid = 'b12ca2d7-59b4-4f9d-a03e-189f37f6f1ee'
    confession_v2_node_uuid = 'ce74c73b-d2b6-4b47-9187-92729ac3dd9b'
    confession_durge_node_uuid = 'ec205b47-a89b-43f6-8928-77d824e940df'
    confession_bard_node_uuid = '06acc6da-bf3f-43f0-8637-1ee1f672b593'
    confession_rogue_node_uuid = '753aaf81-6b74-48c7-a86b-d597f36c9cd0'
    happiest_man_alive_node_uuid = '8f4933c3-a292-4be5-91dd-13b777bd6197'
    happiest_woman_alive_node_uuid = 'b9888f30-2618-46d9-b755-6f86a5cfb1df'
    i_love_you_node_uuid = '5c8b5016-86ae-4a69-af9c-036f091c5a8b'
    my_love_node_uuid = '0d8503d8-9a85-40b2-8211-5882ed1f9bb5'
    first_confession_reaction_node_uuid = '92f6ac2c-5e84-4ea8-8939-e65ff32ed9b5'
    come_here_node_uuid = '0efd0066-4d38-4797-b51c-4fad103cba3d'
    i_know_node_uuid = '4c21339a-95ed-46a6-9f85-21f3edb90d5a'
    i_know_but_its_nice_to_hear_node_uuid = '35939093-8f24-4487-ae25-2d98426182fe'
    nested_confession_kiss_node_uuid = '3192580f-34ca-4a9b-88b3-1e292b2f594e'
    nested_kiss_node_uuid = 'ebae4805-558c-44ce-b24a-186b823f34a4'
    love_you_too_node_uuid = '8ed5d2bf-e8a7-4c33-87d6-4ab4bce9b438'
    say_nothing_node_uuid = '784b3e44-5261-4f9d-baa1-c2a501eaf3f0'
    return_back_node_uuid = 'bb3642b9-5d09-48cf-97ca-fc2bf4f48c31'

    d.add_child_dialog_node(of_course_node_uuid, i_wanted_to_tell_something_node_uuid, 0)
    d.add_child_dialog_node(of_course_node_uuid, i_wanted_to_tell_something_durge_node_uuid, 0)
    d.add_child_dialog_node(of_course_node_uuid, happiest_man_alive_node_uuid, 0)
    d.add_child_dialog_node(of_course_node_uuid, happiest_woman_alive_node_uuid, 0)
    d.add_child_dialog_node(of_course_node_uuid, i_love_you_node_uuid, 0)

    # There's something I wanted to tell you. Something that was on my mind since I met you.
    d.create_standard_dialog_node(
        i_wanted_to_tell_something_node_uuid,
        bg3.SPEAKER_PLAYER,
        [alls_well_i_hope_node_uuid],
        bg3.text_content('h862a65d3g8f8fg46b7gb8afga7dc2ad11479', 1),
        constructor = bg3.dialog_object.QUESTION,
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(Cheated_On_Shadowheart.uuid, False, slot_idx_tav),
                bg3.flag(bg3.FLAG_ORI_State_PartneredWithShadowheart, True, slot_idx_tav),
                bg3.flag(Shadowheart_More_Sandcastles.uuid, True, slot_idx_shadowheart),
                bg3.flag(Tav_Love_Confession.uuid, False, slot_idx_shadowheart),
                bg3.flag(Tav_Said_Love_You.uuid, False, slot_idx_shadowheart),
            )),
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_REALLY_DARK_URGE, False, slot_idx_tav),
            )),        
            bg3.flag_group('Global', (
                bg3.flag(bg3.FLAG_GLO_CAMP_State_NightMode, True, None),
            )),
        ),
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(Tav_Love_Confession.uuid, True, slot_idx_shadowheart),
                bg3.flag(Tav_Said_Love_You.uuid, True, slot_idx_shadowheart),
            )),
        ))

    # There's something I wanted to tell you. Something that was on my mind since I met you.
    d.create_standard_dialog_node(
        i_wanted_to_tell_something_durge_node_uuid,
        bg3.SPEAKER_PLAYER,
        [alls_well_i_hope_node_uuid],
        bg3.text_content('h862a65d3g8f8fg46b7gb8afga7dc2ad11479', 1),
        constructor = bg3.dialog_object.QUESTION,
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(Cheated_On_Shadowheart.uuid, False, slot_idx_tav),
                bg3.flag(bg3.FLAG_ORI_State_PartneredWithShadowheart, True, slot_idx_tav),
                bg3.flag(Shadowheart_More_Sandcastles.uuid, True, slot_idx_shadowheart),
                bg3.flag(Tav_Love_Confession.uuid, False, slot_idx_shadowheart),
                bg3.flag(Tav_Said_Love_You.uuid, False, slot_idx_shadowheart),
            )),
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_REALLY_DARK_URGE, True, slot_idx_tav),
            )),
            bg3.flag_group('Global', (
                bg3.flag(bg3.FLAG_ORI_DarkUrge_State_BhaalResisted, True, None),
                bg3.flag(bg3.FLAG_GLO_CAMP_State_NightMode, True, None),
            )),
        ),
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(Tav_Love_Confession.uuid, True, slot_idx_shadowheart),
                bg3.flag(Tav_Said_Love_You.uuid, True, slot_idx_shadowheart),
            )),
        ))

    # All's well I hope...?
    d.create_standard_dialog_node(
        alls_well_i_hope_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [
            confession_durge_node_uuid,
            confession_bard_node_uuid,
            confession_rogue_node_uuid,
            confession_v1_node_uuid,
            confession_v2_node_uuid
        ],
        bg3.text_content('hd07291d2g217dg47fdg8fd3ga02a235f6b7b', 1))
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '1.375',
        alls_well_i_hope_node_uuid,
        (('2.4', 'd76eaab3-040b-4871-9c1d-4a8624f37cd2'), (None, 'e08db860-1e62-4271-bf4e-d51602468573')),
        phase_duration = '2.5',
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 1024, 0), ),
            bg3.SPEAKER_PLAYER: ((0.0, 32, 1), ),
        })

    confession_approval = bg3.reaction_object.create_new(files, { bg3.SPEAKER_SHADOWHEART : 10 }, uuid = 'bb28ec6c-502a-4fad-902a-7fbe200bf64a')
    love_you_too_approval = bg3.reaction_object.create_new(files, { bg3.SPEAKER_SHADOWHEART : 10 }, uuid = 'd5b42139-675f-4048-b418-54cb7865cf97')

    # Since the time I first saw you in that pod... I changed... no, you changed me. My life has a new meaning: you.
    d.create_standard_dialog_node(
        confession_v1_node_uuid,
        bg3.SPEAKER_PLAYER,
        [i_know_node_uuid, first_confession_reaction_node_uuid],
        bg3.text_content('h82e6c111g7e35g4b7fgba0egec25bbbe117a', 1),
        checkflags = (
            bg3.flag_group('Global', (
                bg3.flag(bg3.FLAG_GLO_Shadowheart_State_RecruitedInTutorial, True, None),
            )),
        ),
        constructor = bg3.dialog_object.QUESTION)

    # We are thrown together by dire circumstances, yet the brief time we shared was more precious than all my years.
    d.create_standard_dialog_node(
        confession_v2_node_uuid,
        bg3.SPEAKER_PLAYER,
        [i_know_node_uuid, first_confession_reaction_node_uuid],
        bg3.text_content('h4d23cd12ga6fdg4485ga129g9ffda516643f', 1),
        constructor = bg3.dialog_object.QUESTION)

    # I can't remember much of myself, and what I remember is like a crimson mist. Until I met you. I am no Bhaal's Chosen anymore. I am yours.
    d.create_standard_dialog_node(
        confession_durge_node_uuid,
        bg3.SPEAKER_PLAYER,
        [i_know_node_uuid, first_confession_reaction_node_uuid],
        bg3.text_content('hd386265bgaf96g421bga57eg8d9ffdeeb899', 1),
        constructor = bg3.dialog_object.QUESTION,
        checkflags = (
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_REALLY_DARK_URGE, True, slot_idx_tav),
            )),
        ))

    # Read a long, emotional, and sad love poem that you wrote for her.
    d.create_standard_dialog_node(
        confession_bard_node_uuid,
        bg3.SPEAKER_PLAYER,
        [i_know_node_uuid, first_confession_reaction_node_uuid],
        bg3.text_content('h2058154fgca15g4c4dg81a9g331986e63a86', 1),
        constructor = bg3.dialog_object.QUESTION,
        checkflags = (
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_BARD, True, slot_idx_tav),
            )),
        ))

    # I sneaked into the most protected vaults, stole countless treasures... only to find that my heart is stolen too. By you.
    d.create_standard_dialog_node(
        confession_rogue_node_uuid,
        bg3.SPEAKER_PLAYER,
        [i_know_node_uuid, first_confession_reaction_node_uuid],
        bg3.text_content('h7ecf542bgf7c8g410dga109gb838c82a324e', 1),
        constructor = bg3.dialog_object.QUESTION,
        checkflags = (
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_ROGUE, True, slot_idx_tav),
            )),
        ))


    # When I woke up this morning, I listened to your gentle snores for a while. I am the happiest man alive. I love you.
    d.create_standard_dialog_node(
        happiest_man_alive_node_uuid,
        bg3.SPEAKER_PLAYER,
        [i_know_node_uuid, my_love_node_uuid],
        bg3.text_content('hb23e9145g96dcg4946g85e2ga984fb7ac751', 1),
        constructor = bg3.dialog_object.QUESTION,
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(Cheated_On_Shadowheart.uuid, False, slot_idx_tav),
                bg3.flag(bg3.FLAG_ORI_State_PartneredWithShadowheart, True, slot_idx_tav),
                bg3.flag(Shadowheart_More_Sandcastles.uuid, True, slot_idx_shadowheart),
                bg3.flag(Tav_Love_Confession.uuid, True, slot_idx_shadowheart),
                bg3.flag(Shadowheart_Tav_Slept_Together.uuid, True, slot_idx_tav),
                bg3.flag(Cuddles_Love_You.uuid, False, slot_idx_shadowheart),
                bg3.flag(Tav_Said_Love_You.uuid, False, slot_idx_shadowheart),
            )),
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_MALE, True, slot_idx_tav),
            )),
        ),
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(Cuddles_Love_You.uuid, True, slot_idx_shadowheart),
                bg3.flag(Tav_Said_Love_You.uuid, True, slot_idx_shadowheart),
            )),
        ))

    # When I woke up this morning, I listened to your gentle snores for a while. I am the happiest woman alive. I love you.
    d.create_standard_dialog_node(
        happiest_woman_alive_node_uuid,
        bg3.SPEAKER_PLAYER,
        [i_know_node_uuid, my_love_node_uuid],
        bg3.text_content('h35801df6g8e05g4eefga058g983fa676324d', 1),
        constructor = bg3.dialog_object.QUESTION,
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(Cheated_On_Shadowheart.uuid, False, slot_idx_tav),
                bg3.flag(bg3.FLAG_ORI_State_PartneredWithShadowheart, True, slot_idx_tav),
                bg3.flag(Shadowheart_More_Sandcastles.uuid, True, slot_idx_shadowheart),
                bg3.flag(Tav_Love_Confession.uuid, True, slot_idx_shadowheart),
                bg3.flag(Shadowheart_Tav_Slept_Together.uuid, True, slot_idx_tav),
                bg3.flag(Cuddles_Love_You.uuid, False, slot_idx_shadowheart),
                bg3.flag(Tav_Said_Love_You.uuid, False, slot_idx_shadowheart),
            )),
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_FEMALE, True, slot_idx_tav),
            )),
        ),
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(Cuddles_Love_You.uuid, True, slot_idx_shadowheart),
                bg3.flag(Tav_Said_Love_You.uuid, True, slot_idx_shadowheart),
            )),
        ))

    # I love you.
    d.create_standard_dialog_node(
        i_love_you_node_uuid,
        bg3.SPEAKER_PLAYER,
        [i_know_node_uuid, my_love_node_uuid],
        bg3.text_content('h10588bf1gd0c4g4b91g90cdg7442250d8d4a', 1),
        constructor = bg3.dialog_object.QUESTION,
        show_once = True,
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(Cheated_On_Shadowheart.uuid, False, slot_idx_tav),
                bg3.flag(bg3.FLAG_ORI_State_PartneredWithShadowheart, True, slot_idx_tav),
                bg3.flag(Tav_Love_Confession.uuid, True, slot_idx_shadowheart),
                bg3.flag(Shadowheart_Tav_Slept_Together.uuid, True, slot_idx_tav),
                bg3.flag(Cuddles_Love_You.uuid, True, slot_idx_shadowheart),
                bg3.flag(Tav_Said_Love_You.uuid, False, slot_idx_shadowheart),
            )),
        ),
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(Tav_Said_Love_You.uuid, True, slot_idx_shadowheart),
            )),
        ))

    # My love...
    d.create_standard_dialog_node(
        my_love_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [come_here_node_uuid],
        bg3.text_content('h8ba27ee6g443bg49cag82eagf508a23378d5', 1))
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        #0.765,
        '2.5',
        my_love_node_uuid,
        (('1.1', 'e7f21f15-f386-40f4-bb0f-2f9f42249ad1'), (None, 'e08db860-1e62-4271-bf4e-d51602468573')),
        phase_duration = '2.5',
        fade_in = 0.0,
        fade_out = 0.0,
        performance_fade = 0.0,
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 2, None),),
            bg3.SPEAKER_PLAYER: ((0.0, 2, None), (1.4, 2, 1), (1.9, 2, None)),
        })

    # Follow up after "My love"
    # Come here...
    d.create_standard_dialog_node(
        come_here_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [nested_kiss_node_uuid],
        bg3.text_content('h2c35be55g4742g47abgbdccg534dfa831e3e', 1),
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(ORI_ShadowheartKiss_VersionA.uuid, False, slot_idx_shadowheart),
            )),
            bg3.flag_group('Object', (
                bg3.flag(ORI_ShadowheartKiss_VersionB.uuid, False, slot_idx_shadowheart),
            )),
            bg3.flag_group('Object', (
                bg3.flag(ORI_ShadowheartKiss_VersionC.uuid, False, slot_idx_shadowheart),
            )),
            bg3.flag_group('Object', (
                bg3.flag(ORI_ShadowheartKiss_VersionD.uuid, True, slot_idx_shadowheart),
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
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        #0.842,
        '1.5',
        come_here_node_uuid,
        ((None, 'e7f21f15-f386-40f4-bb0f-2f9f42249ad1'),),
        #((None, 'd76eaab3-040b-4871-9c1d-4a8624f37cd2'),),
        phase_duration = '1.5',
        performance_fade = 0.0,
        fade_in = 0.0,
        fade_out = 0.0,
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 2, None),),
            bg3.SPEAKER_PLAYER: ((0.0, 2, None), ),
        })

    # Reaction to the 1st love confession.
    # Come here...
    d.create_standard_dialog_node(
        first_confession_reaction_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [nested_confession_kiss_node_uuid],
        bg3.text_content('h2c35be55g4742g47abgbdccg534dfa831e3e', 1),
        approval_rating_uuid = confession_approval.uuid,
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(ORI_ShadowheartKiss_VersionA.uuid, False, slot_idx_shadowheart),
            )),
            bg3.flag_group('Object', (
                bg3.flag(ORI_ShadowheartKiss_VersionB.uuid, False, slot_idx_shadowheart),
            )),
            bg3.flag_group('Object', (
                bg3.flag(ORI_ShadowheartKiss_VersionC.uuid, False, slot_idx_shadowheart),
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
                bg3.flag(ORI_ShadowheartKiss_LoveYou.uuid, True, slot_idx_shadowheart),
            )),
        ))
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        #0.842,
        '2.0',
        first_confession_reaction_node_uuid,
        ((None, 'd76eaab3-040b-4871-9c1d-4a8624f37cd2'),),
        fade_in = 0.8,
        fade_out = 0,
        performance_fade = 1.0,
        phase_duration = '2.0',
        voice_delay = '0.5',
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 2, None),),
            bg3.SPEAKER_PLAYER: ((0.0, 2, None), ),
        })


    # I know. But it's nice to hear you say it.
    d.create_standard_dialog_node(
        i_know_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [],
        bg3.text_content('hb3cef858g5973g4601gb5a3gfb6772f115ec', 1),
        end_node = True,
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(Shadowheart_Has_Doubts_About_Tav.uuid, True, slot_idx_tav),
            )),
        ))
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '4.136',
        i_know_node_uuid,
        (('4.0', 'd76eaab3-040b-4871-9c1d-4a8624f37cd2'), (None, 'a5043f00-72f3-49fe-a24f-fce1e268d896')),
        phase_duration = '4.136',
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 64, None), (2.2, 2, None), (4.0, 1, None)),
            bg3.SPEAKER_PLAYER: ((0.0, 64, None), ),
        })

    nested_dialog_uuid = get_dialog_uuid('ShadowHeart_InParty2_Nested_ShadowheartKiss')
    d.create_nested_dialog_node(
        nested_confession_kiss_node_uuid,
        nested_dialog_uuid,
        [love_you_too_node_uuid, say_nothing_node_uuid],
        speaker_count = 7)

    d.create_nested_dialog_node(
        nested_kiss_node_uuid,
        nested_dialog_uuid,
        [return_back_node_uuid],
        speaker_count = 7)
    
    add_dialog_dependency(ab, nested_dialog_uuid)

    d.create_jump_dialog_node(return_back_node_uuid, of_course_node_uuid, 2)

    # Love you too...
    d.create_standard_dialog_node(
        love_you_too_node_uuid,
        bg3.SPEAKER_PLAYER,
        [i_know_but_its_nice_to_hear_node_uuid],
        bg3.text_content('h91c7ed29gaec4g4388g8655g77ae1647ebe7', 1),
        approval_rating_uuid = love_you_too_approval.uuid,
        constructor = bg3.dialog_object.QUESTION)

    # Say nothing.
    d.create_standard_dialog_node(
        say_nothing_node_uuid,
        bg3.SPEAKER_PLAYER,
        [],
        bg3.text_content('h2b8d754egf05bg4f89g8ae0gacf81a83ad38', 1),
        end_node = True,
        constructor = bg3.dialog_object.QUESTION)

    # I know. But it's nice to hear you say it.
    d.create_standard_dialog_node(
        i_know_but_its_nice_to_hear_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [],
        bg3.text_content('hb3cef858g5973g4601gb5a3gfb6772f115ec', 1),
        end_node = True)
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '4.136',
        i_know_but_its_nice_to_hear_node_uuid,
        (('4.2', 'd76eaab3-040b-4871-9c1d-4a8624f37cd2'), (None, 'a5043f00-72f3-49fe-a24f-fce1e268d896')),
        phase_duration = '4.3',
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 64, None), (2.2, 2, None), (3.5, 2, 1)),
            bg3.SPEAKER_PLAYER: ((0.0, 64, None), ),
        })


def create_reactions_to_creep_debacle() -> None:
    # d = bg3.dialog_object(files.get_file('Gustav', 'Mods/GustavDev/Story/DialogsBinary/Companions/ShadowHeart_InParty2.lsf'))
    # t = bg3.timeline_object(files.get_file('Gustav', 'Public/GustavDev/Timeline/Generated/ShadowHeart_InParty2.lsf'), d)

    ab = game_assets.get_modded_dialog_asset_bundle('ShadowHeart_InParty')
    d = bg3.dialog_object(ab.dialog)
    t = bg3.timeline_object(ab.timeline, d)

    slot_idx_shadowheart = d.get_speaker_slot_index(bg3.SPEAKER_SHADOWHEART)
    slot_idx_tav = d.get_speaker_slot_index(bg3.SPEAKER_PLAYER)


    creep_knocked_out_reaction_node_uuid = '7194d2ec-fd40-4888-9b24-7c430417cf97'
    ignore_her_node_uuid = '33036e4f-3a70-40a5-824a-ffb7fe395e43'
    he_had_it_coming_node_uuid = 'c14d2b72-749b-462d-b705-617b46d9f15b'
    hed_be_lying_dead_node_uuid = 'a9396667-637f-4320-8ff5-dbb1b60ee57d'
    im_sorry_node_uuid = '66f7836d-1c6c-4b9e-b014-ff6e71adb112'
    nothing_more_to_be_said2_node_uuid = '21814299-a4b8-4e22-9654-0ed4d96c8361'
    youre_reading_too_much_into_node_uuid = '17b244a9-201e-4807-9e23-5ed72f8ef3d9'
    i_suppose_youre_right_node_uuid = '8f6410b9-a4c6-4c59-9363-388f9854788f'
    what_i_did_was_uncalled_for_node_uuid = '8ae90184-8428-4d47-9e3c-c2aaa7b0a89f'
    you_mean_the_world_to_me_node_uuid = '0e219df0-cfc5-414c-8355-8b812fed33e5'
    say_nothing_node_uuid = 'e2b5f493-0609-4f7f-8ef9-3875d45f1cb1'
    you_should_get_some_rest_node_uuid = 'faa14348-4019-4695-83ec-22c76680c4a4'
    hug_her_nested_dialog_node_uuid = '28ef0358-1240-4dd7-ab70-6fb624c0803c'
    exit_node_uuid = 'ad648da3-0bc1-48fc-8cea-05e38bd4e353'

    creep_peacefully_removed_reaction1_node_uuid = 'cc7b671e-75cc-45f2-a24d-74bc80cbe590'
    creep_peacefully_removed_reaction2_node_uuid = '521c9faa-30db-4620-b664-8e60bb6a42be'
    #no_loss_to_our_little_venture_node_uuid = 'a0280a58-7f11-4cac-a8a8-2bbc04a2172b'

    #
    # Reaction to Tav kicking creep's ass
    #
    # Hells, was that really necessary? Keep your hands to yourself.
    d.create_standard_dialog_node(
        creep_knocked_out_reaction_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [ignore_her_node_uuid, he_had_it_coming_node_uuid, hed_be_lying_dead_node_uuid, im_sorry_node_uuid],
        bg3.text_content('hdd530817g57ffg457fg853bg5665b8ba9d29', 1),
        constructor = bg3.dialog_object.GREETING,
        root = True,
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(Halsins_Ass_Kicked.uuid, True, slot_idx_tav),
            )),
        ),
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(Halsins_Ass_Kicked.uuid, False, slot_idx_tav),
            )),
        ))
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '6.38',
        creep_knocked_out_reaction_node_uuid,
        (('6.4', '8942c483-83c9-4974-9f47-87cd1dd10828'), (None, '95a53513-08ce-4d80-ae74-e306b51db565')),
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 16, 1), (0.67, 8, 1), (2.55, 128, 2), (3.67, 16, None), (4.51, 8, 1)),
        },
        phase_duration = '6.5')

    shadowheart_approval_plus_6 = bg3.reaction_object.create_new(files, { bg3.SPEAKER_SHADOWHEART : 6 }, uuid = 'c8f23ca0-bd9b-4aca-a8c3-fe5893f4069f')
    shadowheart_approval_minus_10 = bg3.reaction_object.create_new(files, { bg3.SPEAKER_SHADOWHEART : -10 }, uuid = '22a809cb-5892-44d5-9b69-c47115fc939a')
    shadowheart_approval_minus_20 = bg3.reaction_object.create_new(files, { bg3.SPEAKER_SHADOWHEART : -20 }, uuid = '9d91c838-9287-46b1-8729-94a27542e869')

    # You're sure it was necessary, but you don't want to argue. Ignore her.
    d.create_standard_dialog_node(
        ignore_her_node_uuid,
        bg3.SPEAKER_PLAYER,
        [],
        bg3.text_content('hc9d4a3begd325g43c3gbad9gba9afff1194e', 1),
        approval_rating_uuid = shadowheart_approval_minus_20.uuid,
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(Shadowheart_Has_Doubts_About_Tav.uuid, True, slot_idx_tav),
            )),
        ),
        end_node = True,
        constructor = bg3.dialog_object.QUESTION)

    # Yes, that was necessary. He had it coming. How dared he speak to me like that? He's lucky to be alive.
    d.create_standard_dialog_node(
        he_had_it_coming_node_uuid,
        bg3.SPEAKER_PLAYER,
        [nothing_more_to_be_said2_node_uuid],
        bg3.text_content('ha1b09cc8g23b1g4d8fg99fbg86cb2dfea5f2', 1),
        approval_rating_uuid = shadowheart_approval_minus_10.uuid,
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(Shadowheart_Has_Doubts_About_Tav.uuid, True, slot_idx_tav),
            )),
        ),
        constructor = bg3.dialog_object.QUESTION)

    # I taught him a good lesson. Had he as much as touched you, he'd be lying dead now.
    d.create_standard_dialog_node(
        hed_be_lying_dead_node_uuid,
        bg3.SPEAKER_PLAYER,
        [nothing_more_to_be_said2_node_uuid],
        bg3.text_content('hbc4712f9g33ceg470fgaa3bg4d7e0cfa2828', 1),
        approval_rating_uuid = shadowheart_approval_minus_10.uuid,
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(Shadowheart_Has_Doubts_About_Tav.uuid, True, slot_idx_tav),
            )),
        ),
        constructor = bg3.dialog_object.QUESTION)

    # I'm sorry, I really am. I lost my head the moment he said &lt;i&gt;that&lt;/i&gt;. He treated us like his toys, and our bond like a passing indulgence.
    d.create_standard_dialog_node(
        im_sorry_node_uuid,
        bg3.SPEAKER_PLAYER,
        [youre_reading_too_much_into_node_uuid],
        bg3.text_content('h91f8224eg4917g4f31g91d5gc01933960797', 1),
        approval_rating_uuid = shadowheart_approval_plus_6.uuid,
        constructor = bg3.dialog_object.QUESTION)

    # Oh... I see. Well in that case, I suppose there's nothing more to be said on the matter.
    d.create_standard_dialog_node(
        nothing_more_to_be_said2_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [],
        bg3.text_content('h51e0aa30g444dg42fbga21fgd6339b3ad12c', 1),
        end_node = True)
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '7.27',
        nothing_more_to_be_said2_node_uuid,
        ((None, 'd76eaab3-040b-4871-9c1d-4a8624f37cd2'),),
        phase_duration = '7.3',
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 2048, None), (3.68, 4, None), (5.55, 16, None),),
            bg3.SPEAKER_PLAYER: ((0.0, 1, None),),
        },
        attitudes = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_R_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, 3),),
            bg3.SPEAKER_PLAYER: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_L_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, 3),)
        })

    # Normally, I'd tell you you're just reading too much into things. But, well...
    d.create_standard_dialog_node(
        youre_reading_too_much_into_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [i_suppose_youre_right_node_uuid],
        bg3.text_content('h0fd636a0g2cfag44adgbc80ga1c3e537ca5c', 1))
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '8.95',
        youre_reading_too_much_into_node_uuid,
        (
            ('5.5', 'd76eaab3-040b-4871-9c1d-4a8624f37cd2'),
            ('7.9', '95a53513-08ce-4d80-ae74-e306b51db565'),
            (None, 'd76eaab3-040b-4871-9c1d-4a8624f37cd2')
        ),
        phase_duration = '9.5',
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 4, None), (5.02, 16, 1), (6.8, 256, 25), (7.13, 2048, 2), (7.68, 2048, None)),
            bg3.SPEAKER_PLAYER: ((0.0, 2048, None),),
        },
        attitudes = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_R_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, 3),),
            bg3.SPEAKER_PLAYER: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_L_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, 3),)
        })

    # I suppose you're right. On both counts.
    d.create_standard_dialog_node(
        i_suppose_youre_right_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [what_i_did_was_uncalled_for_node_uuid, you_mean_the_world_to_me_node_uuid, say_nothing_node_uuid],
        bg3.text_content('h1d948c45g9286g4881ga6fegb4be459ce4b0', 1))
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '2.95',
        i_suppose_youre_right_node_uuid,
        (('3.4', '8942c483-83c9-4974-9f47-87cd1dd10828'), (None, '95a53513-08ce-4d80-ae74-e306b51db565')),
        phase_duration = '3.5',
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 2048, None), (1.2, 4, None), (2.2, 2, None)),
            bg3.SPEAKER_PLAYER: ((0.0, 2048, None),),
        },
        attitudes = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_R_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, 3),),
            bg3.SPEAKER_PLAYER: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_L_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, 3),)
        })

    # What I did was uncalled for. It won't happen again.
    d.create_standard_dialog_node(
        what_i_did_was_uncalled_for_node_uuid,
        bg3.SPEAKER_PLAYER,
        [you_should_get_some_rest_node_uuid],
        bg3.text_content('h6d35fcc7g133cg47b9gad16g9dbdc0e3d5ce', 1),
        constructor = bg3.dialog_object.QUESTION)

    # I want you to know, you mean the world for me.
    d.create_standard_dialog_node(
        you_mean_the_world_to_me_node_uuid,
        bg3.SPEAKER_PLAYER,
        [you_should_get_some_rest_node_uuid],
        bg3.text_content('h72247b7dg8cadg42b2gba2bgc722a51e01be', 1),
        constructor = bg3.dialog_object.QUESTION)

    # You feel embarassed by your own actions. You can't find the right words to say, so you just hug her.
    d.create_standard_dialog_node(
        say_nothing_node_uuid,
        bg3.SPEAKER_PLAYER,
        [hug_her_nested_dialog_node_uuid],
        bg3.text_content('h9dda2c14geaafg4a47gb232gb1dcd163d524', 1),
        constructor = bg3.dialog_object.QUESTION)

    # You should get some rest. We've got hard times ahead.
    d.create_standard_dialog_node(
        you_should_get_some_rest_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [],
        bg3.text_content('h423eb0ddg04eeg4e3bga2a0g2186a8f528d3', 1),
        end_node = True)
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '4.14',
        you_should_get_some_rest_node_uuid,
        ((None, 'd76eaab3-040b-4871-9c1d-4a8624f37cd2'),),
        phase_duration = '4.4',
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 64, None), (2.73, 4, None),),
            bg3.SPEAKER_PLAYER: ((0.0, 1, None),),
        },
        attitudes = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_R_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, 3),),
            bg3.SPEAKER_PLAYER: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_L_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, 3),)
        })

    nested_dialog_uuid = get_dialog_uuid('ShadowHeart_InParty2_Nested_ShadowheartHug')
    d.create_nested_dialog_node(
        hug_her_nested_dialog_node_uuid,
        nested_dialog_uuid,
        [exit_node_uuid],
        speaker_count = 2)
    add_dialog_dependency(ab, nested_dialog_uuid)

    d.create_standard_dialog_node(
        exit_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [],
        None,
        end_node = True)

    #
    # Reaction to Tav asking creep to leave peacefully
    #
    # Halsin's gone ...
    d.create_standard_dialog_node(
        creep_peacefully_removed_reaction1_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [creep_peacefully_removed_reaction2_node_uuid],
        bg3.text_content('h50379f60g5177g4986g89cage72e87dab0c9', 1),
        constructor = bg3.dialog_object.GREETING,
        root = True,
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(Creep_Ran_Away.uuid, True, slot_idx_tav),
            )),
        ),
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(Creep_Ran_Away.uuid, False, slot_idx_tav),
            )),
        ))
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '2.0',
        creep_peacefully_removed_reaction1_node_uuid,
        ((None, '8942c483-83c9-4974-9f47-87cd1dd10828'),),
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 1024, None),),
        },
        phase_duration = '2.4')

    # Huh. That was... actually rather comforting. Thank you.
    d.create_standard_dialog_node(
        creep_peacefully_removed_reaction2_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        ['3fb3ee71-b5a7-432c-a121-7b274df88c7c'],
        bg3.text_content('h29c33fefg63fbg4e8ag8975g40ddb8876780', 1))
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '6.38',
        creep_peacefully_removed_reaction2_node_uuid,
        (('6.4', 'd76eaab3-040b-4871-9c1d-4a8624f37cd2'), (None, '95a53513-08ce-4d80-ae74-e306b51db565')),
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 1024, None), (1.0, 2, None), (4.5, 2, 1)),
        },
        phase_duration = '6.8')
    d.create_jump_dialog_node('3fb3ee71-b5a7-432c-a121-7b274df88c7c', bg3.SHADOWHEART_QUESTION_BANK_ROOT_NODE_UUID, 2)

    d.add_root_node(creep_peacefully_removed_reaction1_node_uuid, index = 0)
    d.add_root_node(creep_knocked_out_reaction_node_uuid, index = 0)


    # No loss to our little venture, either way.
    # d.create_standard_dialog_node(
    #     no_loss_to_our_little_venture_node_uuid,
    #     bg3.SPEAKER_SHADOWHEART,
    #     [sleep_together_entry_point_node_uuid],
    #     bg3.text_content('h02d316a4g8e5dg4df2gb987g4fdb2003db8d', 1))
    # t.create_simple_dialog_answer_phase(
    #     bg3.SPEAKER_SHADOWHEART,
    #     2.2,
    #     no_loss_to_our_little_venture_node_uuid,
    #     ((2.2, 'd76eaab3-040b-4871-9c1d-4a8624f37cd2'), (None, '95a53513-08ce-4d80-ae74-e306b51db565')),
    #     emotions = {
    #         bg3.SPEAKER_SHADOWHEART: ((0.5, 2, None),),
    #     },
    #     phase_duration = 2.5)


def create_romance_events() -> None:
    ############################################################################################
    # Dialog: ShadowHeart_InParty2.lsf
    ############################################################################################

    # d = bg3.dialog_object(files.get_file('Gustav', 'Mods/GustavDev/Story/DialogsBinary/Companions/ShadowHeart_InParty2.lsf'))
    # t = bg3.timeline_object(files.get_file('Gustav', 'Public/GustavDev/Timeline/Generated/ShadowHeart_InParty2.lsf'), d)

    ab = game_assets.get_modded_dialog_asset_bundle('ShadowHeart_InParty')
    d = bg3.dialog_object(ab.dialog)
    t = bg3.timeline_object(ab.timeline, d)

    slot_idx_shadowheart = d.get_speaker_slot_index(bg3.SPEAKER_SHADOWHEART)
    slot_idx_tav = d.get_speaker_slot_index(bg3.SPEAKER_PLAYER)


    kiss1_entry_node_uuid = 'bb420881-2621-4c12-a95a-820731c2a823'
    kiss2_entry_node_uuid = 'b1c72050-bd56-4240-a812-3d5afe4b4cc2'
    kiss3_entry_node_uuid = 'dbdc428e-59f0-4690-b8c5-ab62852fa53a'
    kiss_nested_node_uuid = '3a5bf5f3-ea78-498f-b92f-49b19b370d5e'
    off_you_go_node_uuid = '45d27e9e-ed36-4fad-b95f-7d049e7f13a0'
    kiss_her_node_uuid = 'e258e122-c225-4a6c-a9ac-8c026f53a04f'
    kiss_her_nested_node_uuid = 'df118ca4-a813-4c72-a2f1-84c8b83454bf'
    resist_kissing_her_node_uuid = '878c72df-549a-4103-9efe-62aef1d61683'
    cant_resist_kissing_her_node_uuid = 'a19fd891-c600-406f-b924-bcc4bfbf0f6d'
    strong_and_silent_node_uuid = '28f1552c-6c9d-4f2c-88a0-3b2988076305'
    arm_on_hips_node_uuid = '2f3b1cf2-5ca1-4611-a00a-e68bf494adbd'
    a_shame_node_uuid = 'd048c792-9a95-4386-a51a-bcca1d11e7f3'

    i_wondered_if_youdve_kissed_me_node_uuid = 'd541de7f-d41b-4b2d-b502-61e5170b734d'
    i_wanted_you_to_kiss_me_node_uuid = 'bab79f05-4349-4209-94c3-acb7fc747971'
    you_were_going_to_kiss_me_node_uuid = '8bd9214d-6444-47e9-bb0a-77a118c34cf1'
    it_was_on_my_mind_all_night_node_uuid = 'bea9d792-f118-495d-88ff-cb846e95e367'

    d.create_standard_dialog_node(
        kiss1_entry_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [kiss_nested_node_uuid],
        None,
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(ORI_ShadowheartKiss_VersionC.uuid, True, slot_idx_shadowheart),
            )),
        ),
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(Shadowheart_Usolicited_Kiss_1.uuid, True, slot_idx_shadowheart),
                bg3.flag(bg3.FLAG_ORI_State_PartneredWithShadowheart, True, slot_idx_tav)
            )),
        ))

    d.create_standard_dialog_node(
        kiss2_entry_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [kiss_nested_node_uuid],
        None,
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(ORI_ShadowheartKiss_VersionD.uuid, True, slot_idx_shadowheart),
            )),
        ),
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(Shadowheart_Usolicited_Kiss_2.uuid, True, slot_idx_shadowheart),
                bg3.flag(bg3.FLAG_ORI_State_PartneredWithShadowheart, True, slot_idx_tav)
            )),
        ))

    d.create_standard_dialog_node(
        kiss3_entry_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [kiss_nested_node_uuid],
        None,
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(ORI_ShadowheartKiss_VersionE.uuid, True, slot_idx_shadowheart),
            )),
        ),
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(Shadowheart_Usolicited_Kiss_3.uuid, True, slot_idx_shadowheart),
                bg3.flag(bg3.FLAG_ORI_State_PartneredWithShadowheart, True, slot_idx_tav)
            )),
        ))

    kiss_nested_dialog_uuid = get_dialog_uuid('ShadowHeart_InParty2_Nested_ShadowheartKiss')
    d.create_nested_dialog_node(
        kiss_nested_node_uuid,
        kiss_nested_dialog_uuid,
        [off_you_go_node_uuid],
        speaker_count = 2)
    add_dialog_dependency(ab, kiss_nested_dialog_uuid)

    # Just that. Off you go.
    # Much better. Now off you go.
    d.create_standard_dialog_node(
        off_you_go_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [],
        [
            bg3.text_content('h9d952bcdgb6ceg451egac14g59f4691463c1', 1, 'dcd18e04-e6f7-4368-be09-571c14e9a760', custom_sequence_id = 'dcd18e04-e6f7-4368-be09-571c14e9a760'),
            bg3.text_content('h1a75465dg3588g46dcg86bag4db0fc101dea', 1, '35f90a90-3f1a-4831-8818-54bdf1b3eaa9', custom_sequence_id = '35f90a90-3f1a-4831-8818-54bdf1b3eaa9'),
        ],
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(Shadowheart_Usolicited_Kiss_1.uuid, False, slot_idx_shadowheart),
                bg3.flag(Shadowheart_Usolicited_Kiss_2.uuid, False, slot_idx_shadowheart),
                bg3.flag(Shadowheart_Usolicited_Kiss_3.uuid, False, slot_idx_shadowheart),
            )),
        ),
        end_node = True)
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '4.4',
        off_you_go_node_uuid,
        ((None, '8942c483-83c9-4974-9f47-87cd1dd10828'),),
        line_index = 0,
        phase_duration = '4.8',
        emotions = {
            bg3.SPEAKER_SHADOWHEART : ((0.0, 2, 2), (1.36, 2, 1), (3.56, 64, 1)),
        })
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '4.65',
        off_you_go_node_uuid,
        ((None, '0e8837db-4344-48d0-9175-12262c73806b'),),
        phase_duration = '4.8',
        line_index = 1,
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 64, 24), (0.4, 2, None)),
            bg3.SPEAKER_PLAYER: ((0.0, 2, None),)
        })


    # I wondered if you'd have kissed me, if you could.
    d.create_standard_dialog_node(
        i_wondered_if_youdve_kissed_me_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [resist_kissing_her_node_uuid, kiss_her_node_uuid],
        bg3.text_content('had4aeb47g123cg49b3g9477g2912df10f5ff', 1),
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(Shadowheart_Daytime_Kiss_1.uuid, True, slot_idx_shadowheart),
                bg3.flag(bg3.FLAG_ORI_State_PartneredWithShadowheart, True, slot_idx_tav)
            )),
        ))
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '3.43',
        i_wondered_if_youdve_kissed_me_node_uuid,
        (('3.6', '0e8837db-4344-48d0-9175-12262c73806b'), (None, '95a53513-08ce-4d80-ae74-e306b51db565')),
        phase_duration = '3.7',
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 16, None), (1.47, 64, None), (2.72, 4, None)),
            bg3.SPEAKER_PLAYER: ((0.0, 16, None),)
        })

    # I thought you were going to kiss me. I wanted you to kiss me.
    d.create_standard_dialog_node(
        i_wanted_you_to_kiss_me_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [resist_kissing_her_node_uuid, kiss_her_node_uuid],
        bg3.text_content('ha41235a2gf772g4beeg8556g01fd0e097f92', 1),
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(Shadowheart_Daytime_Kiss_2.uuid, True, slot_idx_shadowheart),
                bg3.flag(bg3.FLAG_ORI_State_PartneredWithShadowheart, True, slot_idx_tav)
            )),
        ))
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '5.33',
        i_wanted_you_to_kiss_me_node_uuid,
        (('5.4', '0e8837db-4344-48d0-9175-12262c73806b'), (None, '95a53513-08ce-4d80-ae74-e306b51db565')),
        phase_duration = '5.6',
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 64, None), (1.1, 4, None), (2.89, 16, None), (4.51, 64, None)),
            bg3.SPEAKER_PLAYER: ((0.0, 16, None),)
        })

    # I thought you were going to kiss me. I was almost sure of it.
    d.create_standard_dialog_node(
        you_were_going_to_kiss_me_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [resist_kissing_her_node_uuid, kiss_her_node_uuid],
        bg3.text_content('hcc20e6degd72cg4369g900fgf826e5630fb8', 1),
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(Shadowheart_Daytime_Kiss_3.uuid, True, slot_idx_shadowheart),
                bg3.flag(bg3.FLAG_ORI_State_PartneredWithShadowheart, True, slot_idx_tav)
            )),
        ))
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '5.15',
        you_were_going_to_kiss_me_node_uuid,
        (('5.15', '0e8837db-4344-48d0-9175-12262c73806b'), (None, '95a53513-08ce-4d80-ae74-e306b51db565')),
        phase_duration = '5.4',
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 16, None), (1.42, 4, None), (2.87, 64, None)),
            bg3.SPEAKER_PLAYER: ((0.0, 16, None),)
        })

    # I wondered if you'd have kissed me, if you could. It was on my mind all night.
    d.create_standard_dialog_node(
        it_was_on_my_mind_all_night_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [kiss_her_node_uuid, resist_kissing_her_node_uuid],
        bg3.text_content('hc1f152f8g206eg46adg9724g0dabebe2af8c', 1),
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(Shadowheart_Morning_Kiss.uuid, True, slot_idx_shadowheart),
                bg3.flag(bg3.FLAG_ORI_State_PartneredWithShadowheart, True, slot_idx_tav)
            )),
        ))
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '6.48',
        it_was_on_my_mind_all_night_node_uuid,
        (('6.7', '0e8837db-4344-48d0-9175-12262c73806b'), (None, '95a53513-08ce-4d80-ae74-e306b51db565')),
        phase_duration = '6.8',
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 64, None), (1.07, 4, None), (2.23, 16, None)),
            bg3.SPEAKER_PLAYER: ((0.0, 16, None),)
        })

    # Play the strong, silent type.
    d.create_roll_dialog_node(
        resist_kissing_her_node_uuid,
        bg3.SPEAKER_PLAYER,
        bg3.SPEAKER_PLAYER,
        bg3.dialog_object.ABILITY_CHARISMA,
        bg3.dialog_object.SKILL_PERFORMANCE,
        #bg3.DC_Act3_VeryEasy,
        bg3.DC_Act3_Impossible,
        cant_resist_kissing_her_node_uuid,
        kiss_her_nested_node_uuid,
        bg3.text_content('h1329b6fcg3af2g4116gb1f0g724131178f2e', 1),
        #advantage = 1,
        advantage = 2,
        advantage_reason = ('h817752ecg4935g4a31g9ea7g35c3b014b249', 1),
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(ORI_ShadowheartKiss_StartRandom.uuid, True, slot_idx_shadowheart),
            )),
        ))        

    # *You succeeded... and you failed! Hmmm, at least you tried.*
    d.create_standard_dialog_node(
        cant_resist_kissing_her_node_uuid,
        bg3.SPEAKER_NARRATOR,
        [kiss_her_nested_node_uuid],
        bg3.text_content('he112f6b7gfd35g4cabg97dag817ab8be7767', 1),
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(ORI_ShadowheartKiss_StartRandom.uuid, True, slot_idx_shadowheart),
            )),
        ))
    t.create_new_phase(cant_resist_kissing_her_node_uuid, '7.2')
    t.create_tl_actor_node(bg3.timeline_object.EMOTION, bg3.SPEAKER_PLAYER, '0.0', '7.2', (
        t.create_emotion_key(0.0, 256),
        t.create_emotion_key(2.5, 1),
        t.create_emotion_key(5.9, 2)
    ), is_snapped_to_end = True)
    t.create_tl_voice(bg3.SPEAKER_NARRATOR, '0.0', '6.965', cant_resist_kissing_her_node_uuid, is_snapped_to_end = True)
    t.create_tl_shot('95a53513-08ce-4d80-ae74-e306b51db565', '0.0', '7.2', is_snapped_to_end = True)

    # Kiss her.
    d.create_standard_dialog_node(
        kiss_her_node_uuid,
        bg3.SPEAKER_PLAYER,
        [kiss_her_nested_node_uuid],
        bg3.text_content('hc41af286gefabg4061gbe97g5786d98267ac', 1),
        constructor = bg3.dialog_object.QUESTION,
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(ORI_ShadowheartKiss_StartRandom.uuid, True, slot_idx_shadowheart),
            )),
        ))

    d.create_nested_dialog_node(
        kiss_her_nested_node_uuid,
        kiss_nested_dialog_uuid,
        [a_shame_node_uuid],
        speaker_count = 2)

    # I hope there'll be more of those to come, before dawn creeps up on us.
    # Almost a shame we're with company - I'd be tempted to let you whisk me away someplace quiet.
    d.create_standard_dialog_node(
        a_shame_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [],
        [
            bg3.text_content('he571361ag7eb9g4eb7g9347g223c94c8e069', 1, 'bba4dea6-fc91-49b5-b0b6-a4b694373aa5', custom_sequence_id = 'bba4dea6-fc91-49b5-b0b6-a4b694373aa5'),
            bg3.text_content('h59fb8bd0gbdd2g4833g9e60g969c88a43346', 2, '7da24dc8-e149-4c19-ab76-9b3039e41cd1', custom_sequence_id = '7da24dc8-e149-4c19-ab76-9b3039e41cd1'),
        ],
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(Shadowheart_Daytime_Kiss_1.uuid, False, slot_idx_shadowheart),
                bg3.flag(Shadowheart_Daytime_Kiss_2.uuid, False, slot_idx_shadowheart),
                bg3.flag(Shadowheart_Daytime_Kiss_3.uuid, False, slot_idx_shadowheart),
                bg3.flag(Shadowheart_Morning_Kiss.uuid, False, slot_idx_shadowheart),
            )),
        ),
        end_node = True)
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '4.81',
        a_shame_node_uuid,
        ((None, '8942c483-83c9-4974-9f47-87cd1dd10828'),),
        line_index = 0,
        phase_duration = '5.2',
        emotions = {
            bg3.SPEAKER_SHADOWHEART : ((0.0, 2, None), (1.74, 64, None), (3.18, 4, None)),
        })
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '7.26',
        a_shame_node_uuid,
        ((None, '0e8837db-4344-48d0-9175-12262c73806b'),),
        phase_duration = '7.7',
        line_index = 1,
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 2, 1), (3.98, 64, 1), (5.14, 2, None)),
            bg3.SPEAKER_PLAYER: ((0.0, 2, None),)
        })

    #
    # Put occasional kisses just above the partenered greetings
    #

    approval_80_greetings_male_node_uuid = '80fc8153-9363-4c6f-a3bc-ec5e81cbc08a'
    #approval_80_greetings_female_node_uuid = '8d8076e7-1bf1-4a91-95f2-469986a6a5bb'
    every_day_is_an_adventure_node_uuid = '0bc3d936-8a92-4f4e-bc51-26658a78c35b'
    existing_partnered_greetings_node_uuid = '4c2f28c3-4a1b-370a-73f8-d2bfcea53e9d'

    index = d.get_root_node_index(existing_partnered_greetings_node_uuid)
    try:
        index_male = d.get_root_node_index(approval_80_greetings_male_node_uuid)
    except:
        index_male = 999999
    try:
        index_female = d.get_root_node_index(every_day_is_an_adventure_node_uuid)
    except:
        index_female = 999999

    if index_male < index:
        index = index_male
    if index_female < index:
        index = index_female

    d.add_root_node(kiss1_entry_node_uuid, index = index)
    d.add_root_node(kiss2_entry_node_uuid, index = index)
    d.add_root_node(kiss3_entry_node_uuid, index = index)
    d.add_root_node(i_wondered_if_youdve_kissed_me_node_uuid, index = index)
    d.add_root_node(i_wanted_you_to_kiss_me_node_uuid, index = index)
    d.add_root_node(you_were_going_to_kiss_me_node_uuid, index = index)
    d.add_root_node(it_was_on_my_mind_all_night_node_uuid, index = index)

    t.create_narrator_timeline_actor_data()


def create_sharran_kiss() -> None:
    # d = bg3.dialog_object(files.get_file('Gustav', 'Mods/GustavDev/Story/DialogsBinary/Companions/ShadowHeart_InParty2_Nested_DefaultChapter.lsf'))
    # t = bg3.timeline_object(files.get_file('Gustav', 'Public/GustavDev/Timeline/Generated/ShadowHeart_InParty2_Nested_DefaultChapter.lsf'), d)

    ab = game_assets.get_modded_dialog_asset_bundle('ShadowHeart_InParty2_Nested_DefaultChapter')
    d = bg3.dialog_object(ab.dialog)
    t = bg3.timeline_object(ab.timeline, d)

    # speaker slot indexes
    slot_idx_shadowheart = d.get_speaker_slot_index(bg3.SPEAKER_SHADOWHEART)
    slot_idx_tav = d.get_speaker_slot_index(bg3.SPEAKER_PLAYER)

    tav_kiss_node_uuid = '5752078a-349c-4ba7-b8de-3e9341cb0c9c' # existing node
    karlach_kiss_node_uuid = '1a4e47d3-7dbc-468c-a8c9-3b858912a680' # existing node
    kiss_node_uuid = '5e26cf5f-ff2f-4ab8-8281-e8462d1c8655' # existing node

    i_want_to_kiss_you_node_uuid = 'eaca3a74-3383-4cc1-8db3-81f3c2fa4e96'
    karlach_i_want_to_kiss_you_node_uuid = 'c3a94db0-ebea-456c-9f36-00a9f1e5f732'
    i_know_you_do_node_uuid = 'e02f555a-e88c-4156-93f1-0f4f5f20fd80'
    before_shar_romance_crd_node_uuid = 'da77cd27-c867-40f7-b30e-78e9e577606b'
    after_shar_romance_crd_node_uuid = 'de2dde5e-4ca0-4c07-a0e3-7f81bc838313'
    one_kiss_per_long_rest_node_uuid = '764753ca-6461-4ea1-9f30-9bfc6737eaba'
    blasphemy_kiss_roll_node_uuid = 'fd1779ec-8feb-48a9-9ac3-a02923c14fe9'
    blasphemy_kiss_hard_roll_node_uuid = 'bf2ec1df-39a2-432a-be94-0defff549fd4'
    blasphemy_kiss_very_hard_roll_node_uuid = '8a795253-86fb-42af-93df-137f8e213d91'
    bite_me_roll_node_uuid = 'c2afe4d4-902b-4c28-a4ca-eb380187d7d9'
    bite_me_hard_roll_node_uuid = 'bb2fb7b6-ff64-49ad-b244-602cd17163ef'
    bite_me_very_hard_roll_node_uuid = '900355c0-4f4d-4cb9-8376-b7b0f7bad2b7'
    losing_my_mind_roll_node_uuid = 'd753cb50-4a83-44d2-8e32-55d901b0880c'
    losing_my_mind_hard_roll_node_uuid = 'e3c7c794-d25e-47ad-9f29-8ddabe1e529c'
    losing_my_mind_very_hard_roll_node_uuid = '69947c65-e5a8-412d-bc64-d28d16443782'
    darkness_possess_me_roll_node_uuid = '3a97f02c-b47f-48a3-95d4-afe70b0d5fb3'
    darkness_possess_me_hard_roll_node_uuid = '46c702b8-760f-4ee5-9c43-f3f8649f4138'
    darkness_possess_me_very_hard_roll_node_uuid = 'e15d49bf-60a6-4caf-a2e6-d2f4d9efb90e'
    let_the_matter_drop_node_uuid = 'a753cffb-2d2b-4ece-a54a-948245031c9e'

    i_dont_know_what_to_say_node_uuid = '9f3bfaff-7cd2-45af-8d3d-fad0b0815250'
    i_ll_give_you_all_node_uuid = '09a64826-8a9f-47f1-bc8f-6b73b0a2577a'
    i_love_you_node_uuid = 'eba5b7ef-cf05-4a36-977d-bf48306cf746'
    say_nothing_node_uuid = 'b53d675b-d8e3-4443-882a-0e7366ec4ff4'
    ability_check_kiss_node_uuid = '8eea4e04-fdc7-4d4d-b1c9-4771bcba34fa'
    blasphemy_kiss_node_uuid = 'a109176e-8c92-471a-aeee-402b841b00cb'

    d.set_dialog_flags(tav_kiss_node_uuid, checkflags = (
        bg3.flag_group('Object', (
            bg3.flag(bg3.FLAG_ORI_State_PartneredWithShadowheart, True, slot_idx_tav),
        )),
        bg3.flag_group('Global', (
            bg3.flag(Shadowheart_Turned_Away_From_Shar.uuid, True, None),
        )),
        bg3.flag_group('Tag', (
            bg3.flag(bg3.TAG_REALLY_SHADOWHEART, True, slot_idx_shadowheart),
            bg3.flag(bg3.TAG_REALLY_KARLACH, False, slot_idx_tav),
        ))
    ))

    d.set_dialog_flags(karlach_kiss_node_uuid, checkflags = (
        bg3.flag_group('Global', (
            bg3.flag(bg3.FLAG_GLO_ForgingOfTheHeart_State_KarlachSecondUpgrade, True, None),
            bg3.flag(Shadowheart_Turned_Away_From_Shar.uuid, True, None),
        )),
        bg3.flag_group('Object', (
            bg3.flag(bg3.FLAG_ORI_State_PartneredWithShadowheart, True, slot_idx_tav),
        )),
        bg3.flag_group('Tag', (
            bg3.flag(bg3.TAG_REALLY_SHADOWHEART, True, slot_idx_shadowheart),
            bg3.flag(bg3.TAG_REALLY_KARLACH, True, slot_idx_tav),
        ))
    ))

    # I want to kiss you.
    d.create_standard_dialog_node(
        i_want_to_kiss_you_node_uuid,
        bg3.SPEAKER_PLAYER,
        [one_kiss_per_long_rest_node_uuid, i_know_you_do_node_uuid],
        bg3.text_content('hda03b2b0ga7d1g4114gad9cg678ae8cc2f03', 1),
        constructor = bg3.dialog_object.QUESTION,
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_State_PartneredWithShadowheart, True, slot_idx_tav),
            )),
            bg3.flag_group('Global', (
                bg3.flag(Shadowheart_Turned_Away_From_Shar.uuid, False, None),
            )),
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_REALLY_SHADOWHEART, True, slot_idx_shadowheart),
                bg3.flag(bg3.TAG_REALLY_KARLACH, False, slot_idx_tav),
            ))
        ))

    # I want to kiss you.
    d.create_standard_dialog_node(
        karlach_i_want_to_kiss_you_node_uuid,
        bg3.SPEAKER_PLAYER,
        [one_kiss_per_long_rest_node_uuid, i_know_you_do_node_uuid],
        bg3.text_content('hda03b2b0ga7d1g4114gad9cg678ae8cc2f03', 1),
        constructor = bg3.dialog_object.QUESTION,
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_State_PartneredWithShadowheart, True, slot_idx_tav),
            )),
            bg3.flag_group('Global', (
                bg3.flag(bg3.FLAG_GLO_ForgingOfTheHeart_State_KarlachSecondUpgrade, True, None),
                bg3.flag(Shadowheart_Turned_Away_From_Shar.uuid, False, None),
            )),
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_REALLY_SHADOWHEART, True, slot_idx_shadowheart),
                bg3.flag(bg3.TAG_REALLY_KARLACH, True, slot_idx_tav),
            ))
        ))

    d.create_standard_dialog_node(
        one_kiss_per_long_rest_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [kiss_node_uuid],
        None,
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(DJ_Shadowheart_Kissed_Tav.uuid, False, slot_idx_shadowheart),
            )),
        ),
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(DJ_Shadowheart_Kissed_Tav.uuid, True, slot_idx_shadowheart),
            )),
        ))

    # I know you do... but I'm not going to let you. Not just yet...
    d.create_standard_dialog_node(
        i_know_you_do_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [before_shar_romance_crd_node_uuid, after_shar_romance_crd_node_uuid],
        bg3.text_content('h3fe8f895geca6g4da4gae1cgeaa948690a75', 1))
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '9.04',
        i_know_you_do_node_uuid,
        (('9.3', '7b067edd-f53f-49e1-95bc-0986e6e2ca2f'), (None, 'e08db860-1e62-4271-bf4e-d51602468573')),
        phase_duration = '9.5',
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 2, 4), (2.86, 64, 1), (5.49, 2, 23), (7.86, 2, None)),
            bg3.SPEAKER_PLAYER: ((0.0, 32, None),)
        })

    d.create_standard_dialog_node(
        before_shar_romance_crd_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [],
        None,
        checkflags = (
            bg3.flag_group('Global', (
                bg3.flag(Nightfall_Point_Shar_Romance.uuid, False, None),
            )),
        ),
        end_node = True)

    d.create_standard_dialog_node(
        after_shar_romance_crd_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [
            blasphemy_kiss_roll_node_uuid,
            blasphemy_kiss_hard_roll_node_uuid,
            blasphemy_kiss_very_hard_roll_node_uuid,
            bite_me_roll_node_uuid,
            bite_me_hard_roll_node_uuid,
            bite_me_very_hard_roll_node_uuid,
            losing_my_mind_roll_node_uuid,
            losing_my_mind_hard_roll_node_uuid,
            losing_my_mind_very_hard_roll_node_uuid,
            darkness_possess_me_roll_node_uuid,
            darkness_possess_me_hard_roll_node_uuid,
            darkness_possess_me_very_hard_roll_node_uuid,
            let_the_matter_drop_node_uuid
        ],
        None)


    d.create_standard_dialog_node(
        let_the_matter_drop_node_uuid,
        bg3.SPEAKER_PLAYER,
        [],
        bg3.text_content('h69eb305dgbd0ag4076ga6aag321a13ad1524', 2),
        constructor = bg3.dialog_object.QUESTION,
        end_node = True)

    # I will commit an act of blasphemy against my goddess in exchange for a single kiss.
    d.create_roll_dialog_node(
        blasphemy_kiss_roll_node_uuid,
        bg3.SPEAKER_PLAYER,
        bg3.SPEAKER_SHADOWHEART,
        bg3.dialog_object.ABILITY_WISDOM,
        bg3.dialog_object.SKILL_RELIGION,
        bg3.DC_Act3_Medium,
        blasphemy_kiss_node_uuid,
        i_dont_know_what_to_say_node_uuid,
        bg3.text_content('h4911fe70ge9e4g4a26g8245g2ac23f6ccbd6', 1),
        advantage = 1,
        advantage_reason = 'he7d56031g63c2g4a69gacdcg1151b2bfc3b1',
        show_once = True,
        checkflags = (
            bg3.flag_group('Tag', (
                bg3.flag(bg3.GOD_SELUNE, True, slot_idx_tav),
            )),
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_Approval_AtLeast_80_For_Sp2, True, slot_idx_shadowheart),
                bg3.flag(bg3.FLAG_ORI_State_PartneredWithShadowheart, True, slot_idx_tav)
            )),
        ))

    # I will commit an act of blasphemy against my goddess in exchange for a single kiss.
    d.create_roll_dialog_node(
        blasphemy_kiss_hard_roll_node_uuid,
        bg3.SPEAKER_PLAYER,
        bg3.SPEAKER_SHADOWHEART,
        bg3.dialog_object.ABILITY_WISDOM,
        bg3.dialog_object.SKILL_RELIGION,
        bg3.DC_Act3_Challenging,
        ability_check_kiss_node_uuid,
        i_dont_know_what_to_say_node_uuid,
        bg3.text_content('h4911fe70ge9e4g4a26g8245g2ac23f6ccbd6', 1),
        advantage = 1,
        advantage_reason = 'he7d56031g63c2g4a69gacdcg1151b2bfc3b1', 
        show_once = True,
        checkflags = (
            bg3.flag_group('Tag', (
                bg3.flag(bg3.GOD_SELUNE, True, slot_idx_tav),
            )),
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_Approval_AtLeast_60_For_Sp2, True, slot_idx_shadowheart),
                bg3.flag(bg3.FLAG_Approval_AtLeast_80_For_Sp2, False, slot_idx_shadowheart),
                bg3.flag(bg3.FLAG_ORI_State_PartneredWithShadowheart, True, slot_idx_tav)
            )),
        ))

    # I will commit an act of blasphemy against my goddess in exchange for a single kiss.
    d.create_roll_dialog_node(
        blasphemy_kiss_very_hard_roll_node_uuid,
        bg3.SPEAKER_PLAYER,
        bg3.SPEAKER_SHADOWHEART,
        bg3.dialog_object.ABILITY_WISDOM,
        bg3.dialog_object.SKILL_RELIGION,
        bg3.DC_Act3_Hard,
        ability_check_kiss_node_uuid,
        i_dont_know_what_to_say_node_uuid,
        bg3.text_content('h4911fe70ge9e4g4a26g8245g2ac23f6ccbd6', 1),
        advantage = 1,
        advantage_reason = 'he7d56031g63c2g4a69gacdcg1151b2bfc3b1', 
        show_once = True,
        checkflags = (
            bg3.flag_group('Tag', (
                bg3.flag(bg3.GOD_SELUNE, True, slot_idx_tav),
            )),
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_Approval_AtLeast_40_For_Sp2, True, slot_idx_shadowheart),
                bg3.flag(bg3.FLAG_Approval_AtLeast_60_For_Sp2, False, slot_idx_shadowheart),
                bg3.flag(bg3.FLAG_ORI_State_PartneredWithShadowheart, True, slot_idx_tav)
            )),
        ))

    # Don't kiss me. Bite me. Make it hurt.
    d.create_roll_dialog_node(
        bite_me_roll_node_uuid,
        bg3.SPEAKER_PLAYER,
        bg3.SPEAKER_SHADOWHEART,
        bg3.dialog_object.ABILITY_CHARISMA,
        bg3.dialog_object.SKILL_PERSUASION,
        bg3.DC_Act3_Challenging,
        ability_check_kiss_node_uuid,
        i_dont_know_what_to_say_node_uuid,
        bg3.text_content('h298e5b95g05c2g47e9ga0efg88498c299f74', 1),
        advantage = 1,
        advantage_reason = 'he7d56031g63c2g4a69gacdcg1151b2bfc3b1', 
        show_once = True,
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_Approval_AtLeast_80_For_Sp2, True, slot_idx_shadowheart),
                bg3.flag(bg3.FLAG_ORI_State_PartneredWithShadowheart, True, slot_idx_tav)
            )),
        ))

    # Don't kiss me. Bite me. Make it hurt.
    d.create_roll_dialog_node(
        bite_me_hard_roll_node_uuid,
        bg3.SPEAKER_PLAYER,
        bg3.SPEAKER_SHADOWHEART,
        bg3.dialog_object.ABILITY_CHARISMA,
        bg3.dialog_object.SKILL_PERSUASION,
        bg3.DC_Act3_Hard,
        ability_check_kiss_node_uuid,
        i_dont_know_what_to_say_node_uuid,
        bg3.text_content('h298e5b95g05c2g47e9ga0efg88498c299f74', 1),
        advantage = 1,
        advantage_reason = 'he7d56031g63c2g4a69gacdcg1151b2bfc3b1', 
        show_once = True,
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_Approval_AtLeast_60_For_Sp2, True, slot_idx_shadowheart),
                bg3.flag(bg3.FLAG_Approval_AtLeast_80_For_Sp2, False, slot_idx_shadowheart),
                bg3.flag(bg3.FLAG_ORI_State_PartneredWithShadowheart, True, slot_idx_tav)
            )),
        ))

    # Don't kiss me. Bite me. Make it hurt.
    d.create_roll_dialog_node(
        bite_me_very_hard_roll_node_uuid,
        bg3.SPEAKER_PLAYER,
        bg3.SPEAKER_SHADOWHEART,
        bg3.dialog_object.ABILITY_CHARISMA,
        bg3.dialog_object.SKILL_PERSUASION,
        bg3.DC_Act3_VeryHard,
        ability_check_kiss_node_uuid,
        i_dont_know_what_to_say_node_uuid,
        bg3.text_content('h298e5b95g05c2g47e9ga0efg88498c299f74', 1),
        advantage = 1,
        advantage_reason = 'he7d56031g63c2g4a69gacdcg1151b2bfc3b1', 
        show_once = True,
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_Approval_AtLeast_40_For_Sp2, True, slot_idx_shadowheart),
                bg3.flag(bg3.FLAG_Approval_AtLeast_60_For_Sp2, False, slot_idx_shadowheart),
                bg3.flag(bg3.FLAG_ORI_State_PartneredWithShadowheart, True, slot_idx_tav)
            )),
        ))

    # How much loss would warrant me another kiss? I am losing my mind because of you.
    d.create_roll_dialog_node(
        losing_my_mind_roll_node_uuid,
        bg3.SPEAKER_PLAYER,
        bg3.SPEAKER_SHADOWHEART,
        bg3.dialog_object.ABILITY_INTELLIGENCE,
        bg3.dialog_object.SKILL_INSIGHT,
        bg3.DC_Act3_Challenging,
        ability_check_kiss_node_uuid,
        i_dont_know_what_to_say_node_uuid,
        bg3.text_content('h35785161gf2dag4d3cg8db5g2015f81e18ff', 1),
        advantage = 1,
        advantage_reason = 'he7d56031g63c2g4a69gacdcg1151b2bfc3b1', 
        show_once = True,
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_Approval_AtLeast_80_For_Sp2, True, slot_idx_shadowheart),
                bg3.flag(bg3.FLAG_ORI_State_PartneredWithShadowheart, True, slot_idx_tav)
            )),
        ))

    # How much loss would warrant me another kiss? I am losing my mind because of you.
    d.create_roll_dialog_node(
        losing_my_mind_hard_roll_node_uuid,
        bg3.SPEAKER_PLAYER,
        bg3.SPEAKER_SHADOWHEART,
        bg3.dialog_object.ABILITY_INTELLIGENCE,
        bg3.dialog_object.SKILL_INSIGHT,
        bg3.DC_Act3_Hard,
        ability_check_kiss_node_uuid,
        i_dont_know_what_to_say_node_uuid,
        bg3.text_content('h35785161gf2dag4d3cg8db5g2015f81e18ff', 1),
        advantage = 1,
        advantage_reason = 'he7d56031g63c2g4a69gacdcg1151b2bfc3b1', 
        show_once = True,
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_Approval_AtLeast_60_For_Sp2, True, slot_idx_shadowheart),
                bg3.flag(bg3.FLAG_Approval_AtLeast_80_For_Sp2, False, slot_idx_shadowheart),
                bg3.flag(bg3.FLAG_ORI_State_PartneredWithShadowheart, True, slot_idx_tav)
            )),
        ))

    # How much loss would warrant me another kiss? I am losing my mind because of you.
    d.create_roll_dialog_node(
        losing_my_mind_very_hard_roll_node_uuid,
        bg3.SPEAKER_PLAYER,
        bg3.SPEAKER_SHADOWHEART,
        bg3.dialog_object.ABILITY_INTELLIGENCE,
        bg3.dialog_object.SKILL_INSIGHT,
        bg3.DC_Act3_VeryHard,
        ability_check_kiss_node_uuid,
        i_dont_know_what_to_say_node_uuid,
        bg3.text_content('h35785161gf2dag4d3cg8db5g2015f81e18ff', 1),
        advantage = 1,
        advantage_reason = 'he7d56031g63c2g4a69gacdcg1151b2bfc3b1', 
        show_once = True,
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_Approval_AtLeast_40_For_Sp2, True, slot_idx_shadowheart),
                bg3.flag(bg3.FLAG_Approval_AtLeast_60_For_Sp2, False, slot_idx_shadowheart),
                bg3.flag(bg3.FLAG_ORI_State_PartneredWithShadowheart, True, slot_idx_tav)
            )),
        ))

    # I felt a divine touch the last time you kissed me. Kiss me again, let the darkness possess me.
    d.create_roll_dialog_node(
        darkness_possess_me_roll_node_uuid,
        bg3.SPEAKER_PLAYER,
        bg3.SPEAKER_SHADOWHEART,
        bg3.dialog_object.ABILITY_WISDOM,
        bg3.dialog_object.SKILL_RELIGION,
        bg3.DC_Act3_Challenging,
        ability_check_kiss_node_uuid,
        i_dont_know_what_to_say_node_uuid,
        bg3.text_content('h772fe651g90b6g4806g9c2dgca7e8b7128dd', 1),
        advantage = 1,
        advantage_reason = 'he7d56031g63c2g4a69gacdcg1151b2bfc3b1', 
        show_once = True,
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_Approval_AtLeast_80_For_Sp2, True, slot_idx_shadowheart),
                bg3.flag(bg3.FLAG_ORI_State_PartneredWithShadowheart, True, slot_idx_tav)
            )),
        ))

    # I felt a divine touch the last time you kissed me. Kiss me again, let the darkness possess me.
    d.create_roll_dialog_node(
        darkness_possess_me_hard_roll_node_uuid,
        bg3.SPEAKER_PLAYER,
        bg3.SPEAKER_SHADOWHEART,
        bg3.dialog_object.ABILITY_WISDOM,
        bg3.dialog_object.SKILL_RELIGION,
        bg3.DC_Act3_Hard,
        ability_check_kiss_node_uuid,
        i_dont_know_what_to_say_node_uuid,
        bg3.text_content('h772fe651g90b6g4806g9c2dgca7e8b7128dd', 1),
        advantage = 1,
        advantage_reason = 'he7d56031g63c2g4a69gacdcg1151b2bfc3b1', 
        show_once = True,
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_Approval_AtLeast_60_For_Sp2, True, slot_idx_shadowheart),
                bg3.flag(bg3.FLAG_Approval_AtLeast_80_For_Sp2, False, slot_idx_shadowheart),
                bg3.flag(bg3.FLAG_ORI_State_PartneredWithShadowheart, True, slot_idx_tav)
            )),
        ))

    # I felt a divine touch the last time you kissed me. Kiss me again, let the darkness possess me.
    d.create_roll_dialog_node(
        darkness_possess_me_very_hard_roll_node_uuid,
        bg3.SPEAKER_PLAYER,
        bg3.SPEAKER_SHADOWHEART,
        bg3.dialog_object.ABILITY_WISDOM,
        bg3.dialog_object.SKILL_RELIGION,
        bg3.DC_Act3_VeryHard,
        ability_check_kiss_node_uuid,
        i_dont_know_what_to_say_node_uuid,
        bg3.text_content('h772fe651g90b6g4806g9c2dgca7e8b7128dd', 1),
        advantage = 1,
        advantage_reason = 'he7d56031g63c2g4a69gacdcg1151b2bfc3b1', 
        show_once = True,
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_Approval_AtLeast_40_For_Sp2, True, slot_idx_shadowheart),
                bg3.flag(bg3.FLAG_Approval_AtLeast_60_For_Sp2, False, slot_idx_shadowheart),
                bg3.flag(bg3.FLAG_ORI_State_PartneredWithShadowheart, True, slot_idx_tav)
            )),
        ))

    # # I don't know what to say... we're already together as much as Lady Shar allows. Is that not enough for you?
    # d.create_standard_dialog_node(
    #     i_dont_know_what_to_say_node_uuid,
    #     bg3.SPEAKER_SHADOWHEART,
    #     [i_love_you_node_uuid, say_nothing_node_uuid],
    #     bg3.text_content('had60c5eegcd40g45d5ga5fagd7afc188c576', 1))
    # t.create_simple_dialog_answer_phase(
    #     bg3.SPEAKER_SHADOWHEART,
    #     '10.75',
    #     i_dont_know_what_to_say_node_uuid,
    #     (
    #         ('7.3', 'e7f21f15-f386-40f4-bb0f-2f9f42249ad1'),
    #         ('10.75', '0e8837db-4344-48d0-9175-12262c73806b'),
    #         (None, 'e08db860-1e62-4271-bf4e-d51602468573')),
    #     phase_duration = '11.0',
    #     emotions = {
    #         bg3.SPEAKER_SHADOWHEART: ((0.0, 32, None), (3.38, 16, None), (7.41, 32, None)),
    #         bg3.SPEAKER_PLAYER: ((0.0, 32, None),)
    #     })

    # I don't know what to say... we're already together as much as Lady Shar allows. Is that not enough for you?
    d.create_standard_dialog_node(
        i_dont_know_what_to_say_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [i_love_you_node_uuid, say_nothing_node_uuid],
        bg3.text_content('had60c5eegcd40g45d5ga5fagd7afc188c576', 1))
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '10.75',
        i_dont_know_what_to_say_node_uuid,
        (
            ('7.3', 'e7f21f15-f386-40f4-bb0f-2f9f42249ad1'),
            ('10.75', '0e8837db-4344-48d0-9175-12262c73806b'),
            (None, 'e08db860-1e62-4271-bf4e-d51602468573')),
        phase_duration = '11.0',
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 32, None), (3.38, 16, None), (7.41, 32, None)),
            bg3.SPEAKER_PLAYER: ((0.0, 32, None),)
        })

    # I &lt;i&gt;love&lt;/i&gt; you.
    d.create_standard_dialog_node(
        i_love_you_node_uuid,
        bg3.SPEAKER_PLAYER,
        [i_ll_give_you_all_node_uuid],
        bg3.text_content('h95ce0b4bgf7dcg4218g9d40g1a7101bf3551', 1),
        constructor = bg3.dialog_object.QUESTION,
        setflags = (
            bg3.flag_group('Global', (
                bg3.flag(Nightfall_Point_Love_You.uuid, True, None),
            )),
        )
    )

    # Sigh and say nothing.
    d.create_standard_dialog_node(
        say_nothing_node_uuid,
        bg3.SPEAKER_PLAYER,
        [],
        bg3.text_content('h0d817f23g8ef3g4a75g8f69gdc6f6c6af9c4', 1),
        constructor = bg3.dialog_object.QUESTION,
        end_node = True,
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_Shadowheart_InParty_State_EndDialog, True, slot_idx_tav),
            )),
        ))

    # I'll give you all that I can. Just don't call it love.
    d.create_standard_dialog_node(
        i_ll_give_you_all_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [],
        bg3.text_content('hb3fd7d74gccf8g4046g9817g08eb029f6804', 1),
        end_node = True,
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_Shadowheart_InParty_State_EndDialog, True, slot_idx_tav),
            )),
        ))
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '6.68',
        i_ll_give_you_all_node_uuid,
        (
            ('3.5', '7b067edd-f53f-49e1-95bc-0986e6e2ca2f'),
            ('6.7', '0e8837db-4344-48d0-9175-12262c73806b'),
            (None, 'e08db860-1e62-4271-bf4e-d51602468573')
        ),
        phase_duration = '6.9',
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 16, None), (3.38, 32, 1),),
            bg3.SPEAKER_PLAYER: ((0.0, 32, None),)
        })

    d.create_alias_dialog_node(
        blasphemy_kiss_node_uuid,
        kiss_node_uuid,
        ['47eaa218-721a-446a-94fc-62895c1ce704'],
        setflags = (
            bg3.flag_group('Global', (
                bg3.flag(Nightfall_Point_Selune_Blasphemy_Kiss.uuid, True, None),
            )),
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_Kiss_StartRandom, True, slot_idx_shadowheart),
            )),
        ))
    d.create_alias_dialog_node(
        ability_check_kiss_node_uuid,
        kiss_node_uuid,
        ['47eaa218-721a-446a-94fc-62895c1ce704'],
        setflags = (
            bg3.flag_group('Global', (
                bg3.flag(Nightfall_Point_Ability_Check_Kiss.uuid, True, None),
            )),
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_Kiss_StartRandom, True, slot_idx_shadowheart),
            )),
        ))
    kiss_nested_dialog_uuid = get_dialog_uuid('ShadowHeart_InParty2_Nested_ShadowheartKiss')
    d.create_nested_dialog_node(
        '47eaa218-721a-446a-94fc-62895c1ce704',
        kiss_nested_dialog_uuid,
        ['e648f02f-eab4-4000-8656-a5fd9b32a85d'],
        speaker_count = 2)
    add_dialog_dependency(ab, kiss_nested_dialog_uuid)
    d.create_standard_dialog_node(
        'e648f02f-eab4-4000-8656-a5fd9b32a85d',
        bg3.SPEAKER_SHADOWHEART,
        [],
        None,
        end_node = True,
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_Shadowheart_InParty_State_EndDialog, True, slot_idx_tav),
            )),
        ))
    
    d.add_child_dialog_node(of_course_node_uuid, karlach_i_want_to_kiss_you_node_uuid, 0)
    d.add_child_dialog_node(of_course_node_uuid, i_want_to_kiss_you_node_uuid, 0)


def create_entry_point_to_partnered_dialog() -> None:
    ############################################################################################
    # Dialog: ShadowHeart_InParty2.lsf
    ############################################################################################

    # d = bg3.dialog_object(files.get_file('Gustav', 'Mods/GustavDev/Story/DialogsBinary/Companions/ShadowHeart_InParty2.lsf'))
    # t = bg3.timeline_object(files.get_file('Gustav', 'Public/GustavDev/Timeline/Generated/ShadowHeart_InParty2.lsf'), d)

    ab = game_assets.get_modded_dialog_asset_bundle('ShadowHeart_InParty')
    d = bg3.dialog_object(ab.dialog)
    t = bg3.timeline_object(ab.timeline, d)

    speaker_idx_tav = d.get_speaker_slot_index(bg3.SPEAKER_PLAYER)
    speaker_idx_shadowheart = d.get_speaker_slot_index(bg3.SPEAKER_SHADOWHEART)

    # This replaces
    # "I wanted to talk about our relationship."
    # with
    # "I want to talk about us."
    children_uuids = d.get_children_nodes_uuids(bg3.SHADOWHEART_QUESTION_BANK_ROOT_NODE_UUID)
    insertion_index = 0
    i_want_to_talk_about_our_relationship_node_uuid = '5fd62d4b-a8b1-23bc-8582-fc20d5e5f04e' # existing node
    i_want_to_talk_about_us_node_uuid = '6e6b1d74-1791-4ba7-be66-f2ef6f02b1d4'
    high_approval_node_uuid = '3808f6f9-3f51-41ff-b50b-bb9384869824'
    low_approval_node_uuid = '482f3a97-ae59-4187-8b34-866bdd89721f'
    lets_talk_later_node_uuid = '3d33af78-b36c-4425-bb6e-722a28349f84'

    nested_node_uuid = d.get_children_nodes_uuids(i_want_to_talk_about_our_relationship_node_uuid)[0]

    for child_uuid in children_uuids:
        if child_uuid == i_want_to_talk_about_our_relationship_node_uuid:
            break
        insertion_index += 1

    d.delete_child_dialog_node(bg3.SHADOWHEART_QUESTION_BANK_ROOT_NODE_UUID, i_want_to_talk_about_our_relationship_node_uuid)
    d.add_child_dialog_node(bg3.SHADOWHEART_QUESTION_BANK_ROOT_NODE_UUID, i_want_to_talk_about_us_node_uuid, insertion_index)

    # I want to talk about us.
    d.create_standard_dialog_node(
        i_want_to_talk_about_us_node_uuid,
        bg3.SPEAKER_PLAYER,
        [high_approval_node_uuid, low_approval_node_uuid],
        bg3.text_content('h1e8574a0gb5d2g48abg95a9gbe6264723760', 1),
        constructor = bg3.dialog_object.QUESTION,
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_State_PartneredWithShadowheart, True, speaker_idx_tav),
            )),
        ))

    d.create_standard_dialog_node(
        high_approval_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [nested_node_uuid],
        None,
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_Approval_AtLeast_40_For_Sp2, True, speaker_idx_shadowheart),
            )),
        ),
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_Shadowheart_InParty_Event_PartneredStart, True, speaker_idx_tav),
            )),
        ))

    # In need of attention, I take it?
    d.create_standard_dialog_node(
        low_approval_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [lets_talk_later_node_uuid],
        bg3.text_content('hdcf8e090g9bbeg4352ga4b7g955471d143c4', 3))
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '2.49',
        low_approval_node_uuid,
        ((None, '0e8837db-4344-48d0-9175-12262c73806b'),),
        phase_duration = '2.8',
        performance_fade = 2.0,
        fade_in = 0.0,
        fade_out = 2.0,
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 4, None), (1.01, 4, 2)),
            bg3.SPEAKER_PLAYER: ((0.0, 1, None),),
        },
        attitudes = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_R_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, 3),),
            bg3.SPEAKER_PLAYER: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_L_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, 3),)
        })

    # Let's talk later.
    d.create_standard_dialog_node(
        lets_talk_later_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [],
        bg3.text_content('h51521c18g21c4g40d4g80c8gf426407abe71', 1),
        end_node = True)
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '2.58',
        lets_talk_later_node_uuid,
        #((None, 'd76eaab3-040b-4871-9c1d-4a8624f37cd2'),),
        ((None, '0e8837db-4344-48d0-9175-12262c73806b'),),
        phase_duration = '2.8',
        performance_fade = 2.0,
        fade_in = 2.0,
        fade_out = 0.0,
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 1, None),),
            bg3.SPEAKER_PLAYER: ((0.0, 1, None),),
        },
        attitudes = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_R_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, 3),),
            bg3.SPEAKER_PLAYER: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_L_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, 3),)
        })


def create_incubus_reaction() -> None:
    # d = bg3.dialog_object(files.get_file('Gustav', 'Mods/GustavDev/Story/DialogsBinary/Act3/LowerCity/HouseOfHope/LOW_HouseOfHope_ROM_Incubus.lsf'))
    # t = bg3.timeline_object(files.get_file('Gustav', 'Public/GustavDev/Timeline/Generated/LOW_HouseOfHope_ROM_Incubus.lsf'), d)

    ab = game_assets.get_modded_dialog_asset_bundle('LOW_HouseOfHope_ROM_Incubus')
    d = bg3.dialog_object(ab.dialog)
    t = bg3.timeline_object(ab.timeline, d)

    speaker_idx_tav = d.get_speaker_slot_index(bg3.SPEAKER_PLAYER)
    speaker_idx_shadowheart = d.get_speaker_slot_index(bg3.SPEAKER_SHADOWHEART)
    speaker_idx_wyll = d.get_speaker_slot_index(bg3.SPEAKER_WYLL)

    #######################################################################################
    # This prevents companions from being raped by Haarlep
    #######################################################################################
    entry_point1_node_uuid = '21ec9eb6-089a-614a-76f2-e47a8656c23f'
    entry_point2_node_uuid = '6ee38606-dba6-6fd0-13ac-d2be06c77004'
    d.add_dialog_flags(entry_point1_node_uuid, checkflags = (
        bg3.flag_group('Tag', (
            bg3.flag(bg3.TAG_AVATAR, True, speaker_idx_tav),
        )),
    ))
    d.add_dialog_flags(entry_point2_node_uuid, checkflags = (
        bg3.flag_group('Tag', (
            bg3.flag(bg3.TAG_AVATAR, True, speaker_idx_tav),
        )),
    ))


    # careful_node_uuid = 'fe95d8f1-22a9-4474-abea-c7c479cae7fa' # existing node
    # on_the_bed_lie_back_node_uuid = '99a01ef7-e195-0fab-0c9b-d66a866d8c4e' # existing node

    #######################################################################################
    # Approval ratings
    #######################################################################################
    off_with_your_clothes_node_uuid = 'b25bbddb-d0d5-43e0-a117-6b461efc8499' # existing node
    remove_your_garments_node_uuid = '4e04836e-d21b-a81c-44ca-9cfc5f163968' # existing node
    i_have_dreamed_of_lying_with_raphael_node_uuid = '255d4b69-c8dc-3412-829d-15af6b8ce3f1' # existing node
    stay_as_a_man_node_uuid = 'a11c3090-a209-74c4-fd65-f1311bf3ef40' # existing node
    feminine_form_to_my_taste_node_uuid = '5ceb0938-5bac-d1ee-5d47-16650df6a77f' # existing node
    it_matters_not_to_me_node_uuid = 'e7184318-9ac8-6efe-2fb7-638f6fa2a639' # existing node
    lie_down_node_uuid = '094d3acc-153d-4058-7bf5-e889bedae4d7' # existing node

    ive_had_enough_of_your_sick_game_node_uuid = '83a982fa-e386-e059-12cd-6dbc5fba8d79'  # existing node

    approval_remove_your_garments = bg3.reaction_object.create_new(files, {
        bg3.SPEAKER_SHADOWHEART: -10,
        bg3.SPEAKER_KARLACH: -10,
        bg3.SPEAKER_LAEZEL: -10,
        bg3.SPEAKER_ASTARION: -10,
        bg3.SPEAKER_GALE: -10,
        bg3.SPEAKER_WYLL: -10,
        bg3.SPEAKER_MINTHARA: -10,
        bg3.SPEAKER_JAHEIRA: -10,
        bg3.SPEAKER_MINSC: -10
    })
    d.set_approval_rating(remove_your_garments_node_uuid, approval_remove_your_garments.uuid)

    approval_dreamed_of_lying_with_raphael = bg3.reaction_object.create_new(files, {
        bg3.SPEAKER_SHADOWHEART: -10,
        bg3.SPEAKER_KARLACH: -10,
        bg3.SPEAKER_LAEZEL: -10,
        bg3.SPEAKER_ASTARION: -10,
        bg3.SPEAKER_GALE: -10,
        bg3.SPEAKER_WYLL: -10,
        bg3.SPEAKER_MINTHARA: -10,
        bg3.SPEAKER_JAHEIRA: -10,
        bg3.SPEAKER_MINSC: -10
    })
    d.set_approval_rating(i_have_dreamed_of_lying_with_raphael_node_uuid, approval_dreamed_of_lying_with_raphael.uuid)

    approval_lie_down = bg3.reaction_object.create_new(files, {
        bg3.SPEAKER_SHADOWHEART: -10,
        bg3.SPEAKER_KARLACH: -10,
        bg3.SPEAKER_LAEZEL: -10,
        bg3.SPEAKER_ASTARION: -10,
        bg3.SPEAKER_GALE: -10,
        bg3.SPEAKER_WYLL: -10,
        bg3.SPEAKER_MINTHARA: -10,
        bg3.SPEAKER_JAHEIRA: -10,
        bg3.SPEAKER_MINSC: -10
    })
    d.set_approval_rating(lie_down_node_uuid, approval_lie_down.uuid)

    approval_shadowheart_minus_10 = bg3.reaction_object.create_new(files, {
        bg3.SPEAKER_SHADOWHEART: -10
    })
    d.set_approval_rating(stay_as_a_man_node_uuid, approval_shadowheart_minus_10.uuid)
    d.set_approval_rating(feminine_form_to_my_taste_node_uuid, approval_shadowheart_minus_10.uuid)
    d.set_approval_rating(it_matters_not_to_me_node_uuid, approval_shadowheart_minus_10.uuid)

    approval_shadowheart_plus_10 = bg3.reaction_object.create_new(files, {
        bg3.SPEAKER_SHADOWHEART: 10
    })
    d.set_approval_rating(ive_had_enough_of_your_sick_game_node_uuid, approval_shadowheart_plus_10.uuid)

    #######################################################################################
    # Reaction to "Off with your clothes."
    #######################################################################################
    begin_inclusion1_node_uuid = '20693232-97a0-4205-92c7-05dc62351e40'
    alias_careful_node_uuid = 'eac4f292-f466-4d6a-aa24-28cfaad6f54f'
    end_inclusion1_node_uuid = 'd98db7bf-00c6-4b52-b1c0-25d8aed955d3'
    not_partnered_node_uuid = '499223ba-d14a-4aa3-8ad1-9c18858bb22c'
    children_nodes = d.get_children_nodes_uuids(off_with_your_clothes_node_uuid)
    d.create_standard_dialog_node(
        begin_inclusion1_node_uuid,
        bg3.SPEAKER_PLAYER,
        [alias_careful_node_uuid],
        None,
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_State_PartneredWithShadowheart, True, speaker_idx_tav),
            )),
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_REALLY_SHADOWHEART, True, speaker_idx_shadowheart),
            )),
        ),
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_Inclusion_ShadowHeart, True, speaker_idx_tav),
            )),
        ))
    # Careful. I doubt Raphael's associates dispense pleasures of the flesh out of charity. There's bound to be a catch.
    d.create_standard_dialog_node(
        alias_careful_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [end_inclusion1_node_uuid],
        bg3.text_content('hb86710e0g0e84g48ebg955egef0ec35c6789', 2))
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '8.01',
        alias_careful_node_uuid,
        (),
        phase_duration = '8.4',
        fade_in = 0.0,
        fade_out = 1.0,
        performance_fade = 1.0,
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 16, None), (1.09, 128, None), (3.37, 4, None), (6.255, 32, None)),
            bg3.SPEAKER_PLAYER: ((0.0, 128, None),)
        })
    t.create_tl_actor_node(bg3.timeline_object.LOOK_AT, bg3.SPEAKER_SHADOWHEART, '0.0', '8.4', (
        t.create_look_at_key(
            0.0,
            target = bg3.SPEAKER_PLAYER,
            bone = 'Head_M',
            turn_mode = 3,
            turn_speed_multiplier = 0.3,
            head_turn_speed_multiplier = 0.1,
            weight = 0.0,
            #reset = True,
            eye_look_at_bone = 'Head_M',
            safe_zone_angle = 80.0,
            head_safe_zone_angle = 80.0
        ),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.LOOK_AT, bg3.SPEAKER_PLAYER, '0.0', '8.4', (
        t.create_look_at_key(
            8.0,
            target = bg3.SPEAKER_HAARLEP,
            bone = 'Head_M',
            turn_mode = 3,
            turn_speed_multiplier = 0.3,
            head_turn_speed_multiplier = 0.1,
            weight = 0.0,
            reset = True,
            eye_look_at_bone = 'Head_M',
            safe_zone_angle = 80.0,
            head_safe_zone_angle = 80.0
        ),
    ), is_snapped_to_end = True)
    t.create_tl_shot('6a582f7f-3398-423b-a51d-dc922e6bf53f', '0.0', '8.2', is_snapped_to_end = True)
    t.create_tl_shot('6fdc46a6-dbe7-405d-b6e4-6347403b9364', '8.2', '8.4', is_snapped_to_end = True)
    d.create_standard_dialog_node(
        end_inclusion1_node_uuid,
        bg3.SPEAKER_PLAYER,
        children_nodes,
        None,
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_Inclusion_End_ShadowHeart, True, speaker_idx_tav),
            )),
        ))
    d.create_standard_dialog_node(
        not_partnered_node_uuid,
        bg3.SPEAKER_PLAYER,
        children_nodes,
        None)
    d.delete_all_children_dialog_nodes(off_with_your_clothes_node_uuid)
    d.add_child_dialog_node(off_with_your_clothes_node_uuid, begin_inclusion1_node_uuid)
    d.add_child_dialog_node(off_with_your_clothes_node_uuid, not_partnered_node_uuid)


    #######################################################################################
    # Reaction to "I'll admit. I have dreamed of lying with Raphael. Undiluted and raw."
    #######################################################################################
    raph_begin_inclusion_node_uuid = '8a350312-9e81-4078-8ffd-86dbf62fc36d'
    i_knew_there_was_something_untrustworthy_node_uuid = 'a0666ab9-1bd3-4d90-a133-b7914e1b484e'
    lets_talk_later_node_uuid = '530d28e0-c3c2-494b-9bda-33c3beccc2a0'
    raph_end_inclusion_node_uuid = '8b92c2ae-230f-494d-8c87-d2de2aefe338'
    raph_bypass_node_uuid = '1923344e-b115-4a6f-80a6-f5df6f77dc25'
    children_nodes = d.get_children_nodes_uuids(i_have_dreamed_of_lying_with_raphael_node_uuid)

    d.create_standard_dialog_node(
        raph_begin_inclusion_node_uuid,
        bg3.SPEAKER_PLAYER,
        [i_knew_there_was_something_untrustworthy_node_uuid],
        None,
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_State_PartneredWithShadowheart, True, speaker_idx_tav),
            )),
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_REALLY_SHADOWHEART, True, speaker_idx_shadowheart),
            )),
            bg3.flag_group('Global', (
                bg3.flag(Shadowheart_Turned_Away_From_Shar.uuid, True, None),
            ))
        ),
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_Inclusion_ShadowHeart, True, speaker_idx_tav),
            )),
        ))

    # I knew there was something untrustworthy about you.
    d.create_standard_dialog_node(
        i_knew_there_was_something_untrustworthy_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [lets_talk_later_node_uuid],
        bg3.text_content('h47af3b65g0733g403bg8d10g65fe729ad919', 1))
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '3.21',
        i_knew_there_was_something_untrustworthy_node_uuid,
        (),
        phase_duration = '3.5',
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 128, None), (1.4, 128, 1)),
        })
    t.create_tl_actor_node(bg3.timeline_object.LOOK_AT, bg3.SPEAKER_SHADOWHEART, '0.0', '3.5', (
        t.create_look_at_key(
            0.0,
            target = bg3.SPEAKER_PLAYER,
            bone = 'Head_M',
            turn_mode = 3,
            turn_speed_multiplier = 0.3,
            head_turn_speed_multiplier = 0.1,
            weight = 0.0,
            #reset = True,
            eye_look_at_bone = 'Head_M',
            safe_zone_angle = 80.0,
            head_safe_zone_angle = 80.0
        ),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.LOOK_AT, bg3.SPEAKER_PLAYER, '0.0', '3.5', (
        t.create_look_at_key(
            3.0,
            target = bg3.SPEAKER_HAARLEP,
            bone = 'Head_M',
            turn_mode = 3,
            turn_speed_multiplier = 0.3,
            head_turn_speed_multiplier = 0.1,
            weight = 0.0,
            reset = True,
            eye_look_at_bone = 'Head_M',
            safe_zone_angle = 80.0,
            head_safe_zone_angle = 80.0
        ),
    ), is_snapped_to_end = True)
    t.create_tl_shot('6a582f7f-3398-423b-a51d-dc922e6bf53f', '0.0', '3.5', is_snapped_to_end = True)

    # Let's talk later.
    d.create_standard_dialog_node(
        lets_talk_later_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [raph_end_inclusion_node_uuid],
        bg3.text_content('h51521c18g21c4g40d4g80c8gf426407abe71', 1))
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '2.58',
        lets_talk_later_node_uuid,
        (),
        phase_duration = '3.0',
        fade_in = 1.0,
        fade_out = 0.0,
        performance_fade = 1.0,
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 128, 1), (1.0, 128, None)),
        })
    t.create_tl_actor_node(bg3.timeline_object.LOOK_AT, bg3.SPEAKER_SHADOWHEART, '0.0', '3.0', (
        t.create_look_at_key(
            0.0,
            target = bg3.SPEAKER_PLAYER,
            bone = 'Head_M',
            turn_mode = 3,
            turn_speed_multiplier = 0.3,
            head_turn_speed_multiplier = 0.1,
            weight = 0.0,
            reset = True,
            eye_look_at_bone = 'Head_M',
            safe_zone_angle = 80.0,
            head_safe_zone_angle = 80.0
        ),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.LOOK_AT, bg3.SPEAKER_PLAYER, '0.0', '3.0', (
        t.create_look_at_key(
            2.5,
            target = bg3.SPEAKER_HAARLEP,
            bone = 'Head_M',
            turn_mode = 3,
            turn_speed_multiplier = 0.3,
            head_turn_speed_multiplier = 0.1,
            weight = 0.0,
            reset = True,
            eye_look_at_bone = 'Head_M',
            safe_zone_angle = 80.0,
            head_safe_zone_angle = 80.0
        ),
    ), is_snapped_to_end = True)
    t.create_tl_shot('6a582f7f-3398-423b-a51d-dc922e6bf53f', '0.0', '3.0', is_snapped_to_end = True)

    d.create_standard_dialog_node(
        raph_end_inclusion_node_uuid,
        bg3.SPEAKER_PLAYER,
        children_nodes,
        None,
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_Inclusion_End_ShadowHeart, True, speaker_idx_tav),
            )),
        ))
    d.create_standard_dialog_node(
        raph_bypass_node_uuid,
        bg3.SPEAKER_PLAYER,
        children_nodes,
        None)

    d.delete_all_children_dialog_nodes(i_have_dreamed_of_lying_with_raphael_node_uuid)
    d.add_child_dialog_node(i_have_dreamed_of_lying_with_raphael_node_uuid, raph_begin_inclusion_node_uuid)
    d.add_child_dialog_node(i_have_dreamed_of_lying_with_raphael_node_uuid, raph_bypass_node_uuid)


    #######################################################################################
    # Reaction to "Stay as a man, if you please."
    #######################################################################################

    man_begin_inclusion_node_uuid = '5745f230-da9a-4f46-a2e6-ad3075ae7f6b'
    alias_i_knew_there_was_something_untrustworthy_node_uuid = 'a9ce2e1a-8f89-4710-a068-fdae883e47d5'
    alias_lets_talk_later_node_uuid = '50878147-3193-4e90-bbe1-aa89011ae4af'
    man_end_inclusion_node_uuid = '36dd69a6-5097-4c7c-ab7a-e686bb5c609b'
    man_bypass_node_uuid = '41af74ff-65b1-40ed-a12c-3aa4b87204d0'
    children_nodes = d.get_children_nodes_uuids(stay_as_a_man_node_uuid)

    d.create_standard_dialog_node(
        man_begin_inclusion_node_uuid,
        bg3.SPEAKER_PLAYER,
        [alias_i_knew_there_was_something_untrustworthy_node_uuid],
        None,
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_State_PartneredWithShadowheart, True, speaker_idx_tav),
            )),
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_REALLY_SHADOWHEART, True, speaker_idx_shadowheart),
            )),
            bg3.flag_group('Global', (
                bg3.flag(Shadowheart_Turned_Away_From_Shar.uuid, True, None),
            ))
        ),
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_Inclusion_ShadowHeart, True, speaker_idx_tav),
            )),
        ))
    d.create_alias_dialog_node(
        alias_i_knew_there_was_something_untrustworthy_node_uuid,
        i_knew_there_was_something_untrustworthy_node_uuid,
        [alias_lets_talk_later_node_uuid])
    d.create_alias_dialog_node(
        alias_lets_talk_later_node_uuid,
        lets_talk_later_node_uuid,
        [man_end_inclusion_node_uuid])
    d.create_standard_dialog_node(
        man_end_inclusion_node_uuid,
        bg3.SPEAKER_PLAYER,
        children_nodes,
        None,
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_Inclusion_End_ShadowHeart, True, speaker_idx_tav),
            )),
        ))
    d.create_standard_dialog_node(
        man_bypass_node_uuid,
        bg3.SPEAKER_PLAYER,
        children_nodes,
        None)

    d.delete_all_children_dialog_nodes(stay_as_a_man_node_uuid)
    d.add_child_dialog_node(stay_as_a_man_node_uuid, man_begin_inclusion_node_uuid)
    d.add_child_dialog_node(stay_as_a_man_node_uuid, man_bypass_node_uuid)


    #######################################################################################
    # Reaction to "The feminine form is more to my taste.""
    #######################################################################################

    duchess_begin_inclusion_node_uuid = '31982629-4b9c-42c2-88f9-8aca894daefc'
    alias_i_knew_there_was_something_untrustworthy_node_uuid = 'f768beb5-e1da-4167-92af-fc98c4fa737b'
    alias_lets_talk_later_node_uuid = '1d45216f-8560-4519-8c0a-f2cee0271df8'
    duchess_end_inclusion_node_uuid = '666d51d1-3b48-412b-9a78-e2661979bddf'
    duchess_bypass_node_uuid = '97b7bb5e-8ab3-45d1-9b85-6626d7694b70'
    children_nodes = d.get_children_nodes_uuids(feminine_form_to_my_taste_node_uuid)

    d.create_standard_dialog_node(
        duchess_begin_inclusion_node_uuid,
        bg3.SPEAKER_PLAYER,
        [alias_i_knew_there_was_something_untrustworthy_node_uuid],
        None,
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_State_PartneredWithShadowheart, True, speaker_idx_tav),
            )),
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_REALLY_SHADOWHEART, True, speaker_idx_shadowheart),
            )),
            bg3.flag_group('Global', (
                bg3.flag(Shadowheart_Turned_Away_From_Shar.uuid, True, None),
            ))
        ),
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_Inclusion_ShadowHeart, True, speaker_idx_tav),
            )),
        ))
    d.create_alias_dialog_node(
        alias_i_knew_there_was_something_untrustworthy_node_uuid,
        i_knew_there_was_something_untrustworthy_node_uuid,
        [alias_lets_talk_later_node_uuid],
        approval_rating_uuid = approval_shadowheart_minus_10.uuid)
    d.create_alias_dialog_node(
        alias_lets_talk_later_node_uuid,
        lets_talk_later_node_uuid,
        [duchess_end_inclusion_node_uuid])
    d.create_standard_dialog_node(
        duchess_end_inclusion_node_uuid,
        bg3.SPEAKER_PLAYER,
        children_nodes,
        None,
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_Inclusion_End_ShadowHeart, True, speaker_idx_tav),
            )),
        ))
    d.create_standard_dialog_node(
        duchess_bypass_node_uuid,
        bg3.SPEAKER_PLAYER,
        children_nodes,
        None)

    d.delete_all_children_dialog_nodes(feminine_form_to_my_taste_node_uuid)
    d.add_child_dialog_node(feminine_form_to_my_taste_node_uuid, duchess_begin_inclusion_node_uuid)
    d.add_child_dialog_node(feminine_form_to_my_taste_node_uuid, duchess_bypass_node_uuid)


    #######################################################################################
    # Reaction to "It matters not to me."
    #######################################################################################

    matters_not_begin_inclusion_node_uuid = '8cff2eec-2933-4554-8938-7061da32df86'
    alias_i_knew_there_was_something_untrustworthy_node_uuid = 'e2011a20-2d8e-485a-88e4-f3df8290c535'
    alias_lets_talk_later_node_uuid = '5317dc25-28e4-4d12-801d-a78a800381cd'
    matters_not_end_inclusion_node_uuid = '20069866-826f-4f2e-9b98-9a3ba703c438'
    matters_not_bypass_node_uuid = 'b0289652-e9b8-4bc5-aff3-c5a3a813d90c'
    children_nodes = d.get_children_nodes_uuids(it_matters_not_to_me_node_uuid)

    d.create_standard_dialog_node(
        matters_not_begin_inclusion_node_uuid,
        bg3.SPEAKER_PLAYER,
        [alias_i_knew_there_was_something_untrustworthy_node_uuid],
        None,
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_State_PartneredWithShadowheart, True, speaker_idx_tav),
            )),
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_REALLY_SHADOWHEART, True, speaker_idx_shadowheart),
            )),
            bg3.flag_group('Global', (
                bg3.flag(Shadowheart_Turned_Away_From_Shar.uuid, True, None),
            ))
        ),
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_Inclusion_ShadowHeart, True, speaker_idx_tav),
            )),
        ))
    d.create_alias_dialog_node(
        alias_i_knew_there_was_something_untrustworthy_node_uuid,
        i_knew_there_was_something_untrustworthy_node_uuid,
        [alias_lets_talk_later_node_uuid],
        approval_rating_uuid = approval_shadowheart_minus_10.uuid)
    d.create_alias_dialog_node(
        alias_lets_talk_later_node_uuid,
        lets_talk_later_node_uuid,
        [matters_not_end_inclusion_node_uuid])
    d.create_standard_dialog_node(
        matters_not_end_inclusion_node_uuid,
        bg3.SPEAKER_PLAYER,
        children_nodes,
        None,
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_Inclusion_End_ShadowHeart, True, speaker_idx_tav),
            )),
        ))
    d.create_standard_dialog_node(
        matters_not_bypass_node_uuid,
        bg3.SPEAKER_PLAYER,
        children_nodes,
        None)

    d.delete_all_children_dialog_nodes(it_matters_not_to_me_node_uuid)
    d.add_child_dialog_node(it_matters_not_to_me_node_uuid, matters_not_begin_inclusion_node_uuid)
    d.add_child_dialog_node(it_matters_not_to_me_node_uuid, matters_not_bypass_node_uuid)


    #######################################################################################
    # Reaction to "Lie down."
    #######################################################################################
    lie_down_reaction_fork = 'ea6d425c-5500-45f2-956c-018d4673c78b' # existing node
    lie_down_begin_inclusion_node_uuid = '445797f9-ec13-494e-868c-95fe66d68c14' # existing node
    lie_down_end_inclusion_node_uuid = '70e955a5-548b-4306-943f-af4037e9c8dd' # existing node
    halsin_inclusion_node_uuid = 'fce23778-6ce4-486d-a91f-e2c5142e8e32' # existing node
    cinematic_flow_continuation_node_uuid = '17b90d80-8f8b-6588-99e8-a63dce29cfdb'
    new_begin_inclusion_node_uuid = '9609d267-a300-4eb3-bb7f-5f57e730a3b1'
    what_are_you_doing_stop_node_uuid = '9aef130b-c7a2-40e6-83b2-5d8e4f179807'
    new_end_inclusion_node_uuid = '51966933-b39c-4901-badc-85c5cb3d6e5c'

    shadowheart_state_of_mind_node_uuid = '922e0824-bb41-4a92-8406-11b40bb35083'
    tav_state_of_mind_node_uuid = 'bdace965-af2e-4383-a9dd-e8f804a4eecc'
    halsin_fork_node_uuid = '90058954-2cad-43fb-bf51-ba14b77a22ae'
    i_deserve_so_much_more_node_uuid = '377f4862-7e0d-4d07-9080-d0955bf2a2e9'
    she_will_cope_she_will_stay_node_uuid = 'edc8d288-9bd4-4a27-bf67-4af178fb4b0f'
    i_need_to_get_out_of_this_node_uuid = 'a3d51cfb-d781-44f1-925d-0086554a95ff'
    jump_to_fight_node_uuid = '570d7203-a64e-4e5b-a399-e440ca18e132'
    you_will_make_a_pretty_feast_node_uuid = 'ba4631ea-e477-3b41-d4b4-7d06ce21231b' # existing node

    d.delete_child_dialog_node(lie_down_reaction_fork, lie_down_begin_inclusion_node_uuid)
    d.add_child_dialog_node(lie_down_reaction_fork, new_begin_inclusion_node_uuid, 0)
    d.create_standard_dialog_node(
        new_begin_inclusion_node_uuid,
        bg3.SPEAKER_PLAYER,
        [shadowheart_state_of_mind_node_uuid],
        None,
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_State_PartneredWithShadowheart, True, speaker_idx_tav),
            )),
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_REALLY_SHADOWHEART, True, speaker_idx_shadowheart),
            )),
        ),
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_Inclusion_ShadowHeart, True, speaker_idx_tav),
            )),
        ))
    d.create_standard_dialog_node(
        shadowheart_state_of_mind_node_uuid,
        bg3.SPEAKER_PLAYER,
        [what_are_you_doing_stop_node_uuid, new_end_inclusion_node_uuid],
        None)
    # What are you doing? Stop!
    d.create_standard_dialog_node(
        what_are_you_doing_stop_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [new_end_inclusion_node_uuid],
        bg3.text_content('hbf059a07ga169g4d73g9bb3g047e8ed389fb', 1),
        checkflags = (
            bg3.flag_group('Global', (
                bg3.flag(Shadowheart_Turned_Away_From_Shar.uuid, True, None),
            )),
        ))
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '3.17',
        what_are_you_doing_stop_node_uuid,
        (),
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 16, 1), (1.6, 8, 1), (3.35, 32, 2)),
        },
        phase_duration = '3.7')
    t.create_tl_actor_node(bg3.timeline_object.SHOW_VISUAL, bg3.SPEAKER_SHADOWHEART, '0.0', '3.5', (
        t.create_value_key(time = 0.0, interpolation_type = 3, value_name = 'ShowVisual', value = True),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.LOOK_AT, bg3.SPEAKER_SHADOWHEART, '0.0', '3.5', (
        t.create_look_at_key(
            0.0,
            target = bg3.SPEAKER_PLAYER,
            bone = 'Head_M',
            turn_mode = 3,
            turn_speed_multiplier = 0.3,
            head_turn_speed_multiplier = 0.1,
            weight = 0.0,
            #reset = True,
            eye_look_at_bone = 'Head_M',
            safe_zone_angle = 80.0,
            head_safe_zone_angle = 80.0
        ),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.LOOK_AT, bg3.SPEAKER_PLAYER, '0.0', '3.5', (
        t.create_look_at_key(
            3.0,
            target = bg3.SPEAKER_HAARLEP,
            bone = 'Head_M',
            turn_mode = 3,
            turn_speed_multiplier = 0.3,
            head_turn_speed_multiplier = 0.1,
            weight = 0.0,
            reset = True,
            eye_look_at_bone = 'Head_M',
            safe_zone_angle = 80.0,
            head_safe_zone_angle = 80.0
        ),
    ), is_snapped_to_end = True)
    t.create_tl_shot('6a582f7f-3398-423b-a51d-dc922e6bf53f', '0.0', '3.3', is_snapped_to_end = True)
    t.create_tl_shot('d2bb86ec-fd6f-4e93-8060-37c28f10a69e', '3.3', '3.7', is_snapped_to_end = True)

    d.create_standard_dialog_node(
        new_end_inclusion_node_uuid,
        bg3.SPEAKER_PLAYER,
        [halsin_fork_node_uuid],
        None,
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_Inclusion_End_ShadowHeart, True, speaker_idx_tav),
            )),
        ))
    d.create_standard_dialog_node(
        halsin_fork_node_uuid,
        bg3.SPEAKER_PLAYER,
        [tav_state_of_mind_node_uuid, halsin_inclusion_node_uuid],
        None)
    d.create_standard_dialog_node(
        tav_state_of_mind_node_uuid,
        bg3.SPEAKER_PLAYER,
        [i_deserve_so_much_more_node_uuid, she_will_cope_she_will_stay_node_uuid, i_need_to_get_out_of_this_node_uuid],
        None,
        checkflags = (
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_REALLY_SHADOWHEART, True, speaker_idx_shadowheart),
            )),
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_State_PartneredWithShadowheart, True, speaker_idx_tav),
            )),
            bg3.flag_group('Global', (
                bg3.flag(Shadowheart_Turned_Away_From_Shar.uuid, True, None),
            )),
        ))
    # She has never truly understood me. I deserve so much more than just her.
    d.create_standard_dialog_node(
        i_deserve_so_much_more_node_uuid,
        bg3.SPEAKER_PLAYER,
        [cinematic_flow_continuation_node_uuid],
        bg3.text_content('h4497715fg0105g43a9g8748g5f50dfa0cd30', 1),
        constructor = bg3.dialog_object.QUESTION)
    # She has nowhere else to go. She will cope, and she will stay with me.
    d.create_standard_dialog_node(
        she_will_cope_she_will_stay_node_uuid,
        bg3.SPEAKER_PLAYER,
        [cinematic_flow_continuation_node_uuid],
        bg3.text_content('hd8ceefa0g516eg4ad8gbbdeg509ecf2134f0', 1),
        constructor = bg3.dialog_object.QUESTION)
    # What am I doing? Had I lost my mind? I need to fight this ... thing.
    d.create_standard_dialog_node(
        i_need_to_get_out_of_this_node_uuid,
        bg3.SPEAKER_PLAYER,
        [jump_to_fight_node_uuid],
        bg3.text_content('hc36d812dgb030g48d9gb8ffg307186503100', 1),
        constructor = bg3.dialog_object.QUESTION,
        approval_rating_uuid = approval_shadowheart_plus_10.uuid)
    d.create_jump_dialog_node(jump_to_fight_node_uuid, you_will_make_a_pretty_feast_node_uuid, 1)

    d.delete_all_children_dialog_nodes(lie_down_begin_inclusion_node_uuid)
    d.add_child_dialog_node(lie_down_begin_inclusion_node_uuid, what_are_you_doing_stop_node_uuid)


    #######################################################################################
    # Wyll's reaction
    # Not to sound like a second-rate writer, but - are you sure this is a good idea?
    #######################################################################################
    begin_wyll_inclusion_node_uuid = '6f892b35-808e-43e0-85ba-0a3ea922ebd8'
    are_you_sure_this_is_a_good_idea_node_uuid = 'd470fe04-00c1-414b-a4bb-9f919bf6b7e0'
    end_wyll_inclusion_node_uuid = '5d68e214-0a4f-40ee-9c4f-a2ca958240b5'
    wyll_not_in_party_node_uuid = '2b169935-4875-4aa7-bae0-c4e62f705f97'
    children_nodes = d.get_children_nodes_uuids(remove_your_garments_node_uuid)
    d.create_standard_dialog_node(
        begin_wyll_inclusion_node_uuid,
        bg3.SPEAKER_PLAYER,
        [are_you_sure_this_is_a_good_idea_node_uuid],
        None,
        checkflags = (
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_REALLY_WYLL, True, speaker_idx_wyll),
            )),
        ),
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_Inclusion_Wyll, True, speaker_idx_tav),
            )),
        ))
    d.create_standard_dialog_node(
        are_you_sure_this_is_a_good_idea_node_uuid,
        bg3.SPEAKER_WYLL,
        [end_wyll_inclusion_node_uuid],
        bg3.text_content('h09542ad5gb843g48c6gb5c2g341603998f6f', 1)
    )
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_WYLL,
        '5.5',
        are_you_sure_this_is_a_good_idea_node_uuid,
        (),
        phase_duration = '5.5')
    t.create_tl_shot('48dbf93b-b5ad-4a3f-80e3-5d46e1cca9d5', '0.0', '5.5', is_snapped_to_end = True)
    d.create_standard_dialog_node(
        end_wyll_inclusion_node_uuid,
        bg3.SPEAKER_PLAYER,
        children_nodes,
        None,
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_Inclusion_End_Wyll, True, speaker_idx_tav),
            )),
        ))
    d.create_standard_dialog_node(
        wyll_not_in_party_node_uuid,
        bg3.SPEAKER_PLAYER,
        children_nodes,
        None)
    d.delete_all_children_dialog_nodes(remove_your_garments_node_uuid)
    d.add_child_dialog_node(remove_your_garments_node_uuid, begin_wyll_inclusion_node_uuid)
    d.add_child_dialog_node(remove_your_garments_node_uuid, wyll_not_in_party_node_uuid)



    #######################################################################################
    # This creates consequences for Tav on Shadowheart's selunite and sharran paths
    # No consequences if Shadowheart is on her mother superior path
    #######################################################################################

    every_touch_a_lie_of_true_love_safe_node_uuid = '774159bc-7e13-dbca-9747-af012830d6ee' # existing node
    safe_branch_next_node_uuid = d.get_children_nodes_uuids(every_touch_a_lie_of_true_love_safe_node_uuid)[0]
    this_is_the_end_unsafe_node_uuid = '97509bc5-59b2-1fd8-5a8d-c49ec89b304f' # existing node
    devote_yourself_to_pleasure_eternal_node_uuid = '7ebf1786-f9c3-d27c-b911-9ffd2f820cc3' # existing node

    safe_branch_breakup_fork_node_uuid = '5b29bd9a-b34b-41bc-b68a-01c185de9bb9'
    safe_branch_selunite_node_uuid = 'f7f8e6a6-60b2-4bae-acf6-cce10e420150'
    safe_branch_sharran_node_uuid = '59f31452-8baf-4ac5-b81d-963067ac3c88'
    unsafe_branch_breakup_fork_node_uuid = '0e904de3-811a-400c-b711-dd5359f1464e'
    unsafe_branch_selunite_node_uuid = '84036534-bd56-4774-a724-5b9fd27e62b8'
    unsafe_branch_sharran_node_uuid = 'e57dc97b-cb3f-4daa-bdf4-00ccbe4d4fea'

    #tav_question_container_node_uuid = '2781af1c-74c9-46fa-85a4-6ee550c86a63'
    shadowheart_reacts_fork_node_uuid = 'b0b21a06-dd0e-4438-aaa8-a9552ad86a5c'

    d.create_standard_dialog_node(
        safe_branch_breakup_fork_node_uuid,
        bg3.SPEAKER_PLAYER,
        [safe_branch_selunite_node_uuid, safe_branch_sharran_node_uuid, safe_branch_next_node_uuid],
        None)
    d.create_standard_dialog_node(
        safe_branch_selunite_node_uuid,
        bg3.SPEAKER_PLAYER,
        [safe_branch_next_node_uuid],
        None,
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_State_PartneredWithShadowheart, True, speaker_idx_tav),
            )),
            bg3.flag_group('Global', (
                bg3.flag(Shadowheart_Turned_Away_From_Shar.uuid, True, None),
            )),
        ),
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_State_PartneredWithShadowheart, False, speaker_idx_tav),
                bg3.flag(bg3.FLAG_ORI_State_WasPartneredWithShadowheart, True, speaker_idx_tav),
                bg3.flag(bg3.FLAG_ORI_State_HandledBreakupWithShadowheart, False, speaker_idx_tav),
                bg3.flag(Shadowheart_Has_Doubts_About_Tav.uuid, False, speaker_idx_tav),
                bg3.flag(Tav_Played_With_Incubus.uuid, True, speaker_idx_tav),
            )),
        ))
    d.create_standard_dialog_node(
        safe_branch_sharran_node_uuid,
        bg3.SPEAKER_PLAYER,
        [safe_branch_next_node_uuid],
        None,
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_State_PartneredWithShadowheart, True, speaker_idx_tav),
            )),
            bg3.flag_group('Global', (
                bg3.flag(bg3.FLAG_ORI_Shadowheart_State_Shar_KilledParents, False, None),
            )),
        ),
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(Shadowheart_Has_Doubts_About_Tav.uuid, True, speaker_idx_tav),
                bg3.flag(Tav_Played_With_Incubus.uuid, True, speaker_idx_tav),
            )),
        )
    )
    d.delete_all_children_dialog_nodes(every_touch_a_lie_of_true_love_safe_node_uuid)
    d.add_child_dialog_node(every_touch_a_lie_of_true_love_safe_node_uuid, safe_branch_breakup_fork_node_uuid)

    d.create_standard_dialog_node(
        unsafe_branch_breakup_fork_node_uuid,
        bg3.SPEAKER_PLAYER,
        [unsafe_branch_selunite_node_uuid, unsafe_branch_sharran_node_uuid, devote_yourself_to_pleasure_eternal_node_uuid],
        None)
    d.create_standard_dialog_node(
        unsafe_branch_selunite_node_uuid,
        bg3.SPEAKER_PLAYER,
        [shadowheart_reacts_fork_node_uuid],
        None,
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_State_PartneredWithShadowheart, True, speaker_idx_tav),
            )),
            bg3.flag_group('Global', (
                bg3.flag(Shadowheart_Turned_Away_From_Shar.uuid, True, None),
            )),
        ),
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_State_PartneredWithShadowheart, False, speaker_idx_tav),
                bg3.flag(bg3.FLAG_ORI_State_WasPartneredWithShadowheart, True, speaker_idx_tav),
                bg3.flag(bg3.FLAG_ORI_State_HandledBreakupWithShadowheart, False, speaker_idx_tav),
                bg3.flag(Shadowheart_Has_Doubts_About_Tav.uuid, False, speaker_idx_tav),
                bg3.flag(Tav_Played_With_Incubus.uuid, True, speaker_idx_tav),
            )),
        )
    )
    d.create_standard_dialog_node(
        unsafe_branch_sharran_node_uuid,
        bg3.SPEAKER_PLAYER,
        [shadowheart_reacts_fork_node_uuid],
        None,
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_State_PartneredWithShadowheart, True, speaker_idx_tav),
            )),
            bg3.flag_group('Global', (
                bg3.flag(bg3.FLAG_ORI_Shadowheart_State_Shar_KilledParents, False, None),
            )),
        ),
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(Shadowheart_Has_Doubts_About_Tav.uuid, True, speaker_idx_tav),
                bg3.flag(Tav_Played_With_Incubus.uuid, True, speaker_idx_tav),
            )),
        )
    )
    d.delete_all_children_dialog_nodes(this_is_the_end_unsafe_node_uuid)
    d.add_child_dialog_node(this_is_the_end_unsafe_node_uuid, unsafe_branch_breakup_fork_node_uuid)


    #######################################################################################
    # Shadowheart reacts to what's happening on the bed
    #######################################################################################
    shadowheart_reacts_selune_path_node_uuid = 'f823fd53-ac09-473a-b006-8ff30cf25d94'
    shadowheart_reacts_shar_path_node_uuid = '24593148-6f03-43a1-b8ea-b57816b366ee'

    d.create_standard_dialog_node(
        shadowheart_reacts_fork_node_uuid,
        bg3.SPEAKER_PLAYER,
        [shadowheart_reacts_selune_path_node_uuid, shadowheart_reacts_shar_path_node_uuid, devote_yourself_to_pleasure_eternal_node_uuid],
        None)

    # Shadowheart reacts, Selune path
    d.create_cinematic_dialog_node(
        shadowheart_reacts_selune_path_node_uuid,
        [devote_yourself_to_pleasure_eternal_node_uuid],
        checkflags = (
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_REALLY_SHADOWHEART, True, speaker_idx_shadowheart),
            )),
            bg3.flag_group('Global', (
                bg3.flag(Shadowheart_Turned_Away_From_Shar.uuid, True, None),
            )),
        ))
    t.create_new_phase(shadowheart_reacts_selune_path_node_uuid, '3.0')
    t.create_tl_actor_node(bg3.timeline_object.SHOW_VISUAL, bg3.SPEAKER_SHADOWHEART, '0.0', '3.0', (
        t.create_value_key(time = 0.0, interpolation_type = 3, value_name = 'ShowVisual', value = True),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.ATTITUDE, bg3.SPEAKER_SHADOWHEART, '0.0', '3.0', (
        t.create_attitude_key(1.2, bg3.ATTITUDE_DIAG_Pose_Shocked_L_01, bg3.ATTITUDE_DIAG_T_Pose),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.EMOTION, bg3.SPEAKER_SHADOWHEART, '0.0', '3.0', (
        t.create_emotion_key(0.0, 32),
        t.create_emotion_key(1.4, 32, variation = 1, is_sustained = False),
    ))
    t.create_tl_camera_fov('6a582f7f-3398-423b-a51d-dc922e6bf53f', '0.0', '3.0', (
        t.create_value_key(time = 0.0, value_name = 'FoV', value = 25.0),
        t.create_value_key(time = 3.0, value_name = 'FoV', value = 20.0),
    ))
    t.create_tl_shot('6a582f7f-3398-423b-a51d-dc922e6bf53f', '0.0', '3.0')


    # Shadowheart reacts, Shar path
    d.create_cinematic_dialog_node(
        shadowheart_reacts_shar_path_node_uuid,
        [devote_yourself_to_pleasure_eternal_node_uuid],
        checkflags = (
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_REALLY_SHADOWHEART, True, speaker_idx_shadowheart),
            )),
        ))
    t.create_new_phase(shadowheart_reacts_shar_path_node_uuid, '3.0')
    t.create_tl_actor_node(bg3.timeline_object.SHOW_VISUAL, bg3.SPEAKER_SHADOWHEART, '0.0', '3.0', (
        t.create_value_key(time = 0.0, interpolation_type = 3, value_name = 'ShowVisual', value = True),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.ATTITUDE, bg3.SPEAKER_SHADOWHEART, '0.0', '3.0', (
        t.create_attitude_key(1.2, bg3.ATTITUDE_DIAG_Pose_Crossed_01, bg3.ATTITUDE_DIAG_T_Pose),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.EMOTION, bg3.SPEAKER_SHADOWHEART, '0.0', '3.0', (
        t.create_emotion_key(0.0, 8, variation = 1),
        t.create_emotion_key(1.4, 8, variation = 2, is_sustained = False),
    ))
    t.create_tl_camera_fov('6a582f7f-3398-423b-a51d-dc922e6bf53f', '0.0', '3.0', (
        t.create_value_key(time = 0.0, value_name = 'FoV', value = 25.0),
        t.create_value_key(time = 3.0, value_name = 'FoV', value = 20.0),
    ))
    t.create_tl_shot('6a582f7f-3398-423b-a51d-dc922e6bf53f', '0.0', '3.0')

    #######################################################################################
    # Tav will have to succeed a skill check to keep their soul
    #######################################################################################
    devote_yourself_to_pleasure_eternal_node_uuid = '7ebf1786-f9c3-d27c-b911-9ffd2f820cc3' # existing node
    a_brilliant_choice_node_uuid = 'd583ad81-412d-3f9a-c564-bef99f479575' # existing node
    indeed_they_are_node_uuid = 'e6d4cadb-5c3b-a984-71e8-0dacce6cd20c' # existing node
    you_can_have_my_body_but_not_my_mind_node_uuid = '0ac9fd92-818b-61c0-5a39-cfadc1c75ff6' # existing node
    i_will_only_share_my_body_node_uuid = 'ab4b3725-a634-42f9-bbb4-00020b9ffc87'

    d.create_roll_dialog_node(
        i_will_only_share_my_body_node_uuid,
        bg3.SPEAKER_PLAYER,
        bg3.SPEAKER_PLAYER,
        bg3.dialog_object.ABILITY_WISDOM,
        '',
        bg3.DC_Act3_Hard,
        a_brilliant_choice_node_uuid,
        indeed_they_are_node_uuid,
        bg3.text_content('haea72441gdfe6g41fcga75bg97af9661125e', 1))

    d.delete_child_dialog_node(devote_yourself_to_pleasure_eternal_node_uuid, you_can_have_my_body_but_not_my_mind_node_uuid)
    d.add_child_dialog_node(devote_yourself_to_pleasure_eternal_node_uuid, i_will_only_share_my_body_node_uuid, 0)

    # This changes the outcome of failing the constitution check: incubus consumes Tav's soul.
    # Try to cool your desires, and push the creature away.
    try_as_you_will_every_part_melts_node_uuid = '7343d2ee-f38b-fc72-ca4b-50800df9514d' # existing node
    d.delete_all_children_dialog_nodes(try_as_you_will_every_part_melts_node_uuid)
    d.add_child_dialog_node(try_as_you_will_every_part_melts_node_uuid, indeed_they_are_node_uuid)


    #######################################################################################
    # Tav will have to succeed a skill check to keep their soul
    # Safe romance option is ON
    #######################################################################################
    safe_romance_visual_node_uuid = 'fe434edb-15d4-37a8-af96-ede506c06275'
    you_can_have_my_body_but_not_my_mind_safe_node_uuid = '1d8f2af1-5bfb-7a9e-3dfc-bd4e602a7dee' # eixsting node
    roll_you_can_have_my_body_but_not_my_mind_safe_node_uuid = 'c6b2de40-1577-4b8a-b9a7-0b623c1b9452'
    you_force_your_eyes_open_node_uuid = '9f6fbdcc-2fa4-e8a8-b39c-e38e6df67ad7' # existing node
    incubus_laps_eevry_part_of_your_soul_node_uuid = '0b6936d4-a288-1cb4-1da5-2705452b765a' # existing node
    pleasuring_thousands_id_rather_die_safe_node_uuid = 'f921daa7-0b12-a934-6e91-ef065be19532'

    d.create_roll_dialog_node(
        roll_you_can_have_my_body_but_not_my_mind_safe_node_uuid,
        bg3.SPEAKER_PLAYER,
        bg3.SPEAKER_PLAYER,
        bg3.dialog_object.ABILITY_WISDOM,
        bg3.dialog_object.SKILL_SURVIVAL,
        bg3.DC_Act3_Hard,
        you_force_your_eyes_open_node_uuid,
        incubus_laps_eevry_part_of_your_soul_node_uuid,
        bg3.text_content('hce84b81ega726g4456g88eag4bc0681104bc', 1))

    d.delete_child_dialog_node(safe_romance_visual_node_uuid, you_can_have_my_body_but_not_my_mind_safe_node_uuid)
    d.add_child_dialog_node(safe_romance_visual_node_uuid, roll_you_can_have_my_body_but_not_my_mind_safe_node_uuid, 4)
    d.delete_child_dialog_node(safe_romance_visual_node_uuid, pleasuring_thousands_id_rather_die_safe_node_uuid)


def create_post_incubus_breakup() -> None:
    # d = bg3.dialog_object(files.get_file('Gustav', 'Mods/GustavDev/Story/DialogsBinary/Companions/ShadowHeart_InParty2.lsf'))
    # t = bg3.timeline_object(files.get_file('Gustav', 'Public/GustavDev/Timeline/Generated/ShadowHeart_InParty2.lsf'), d)

    ab = game_assets.get_modded_dialog_asset_bundle('ShadowHeart_InParty')
    d = bg3.dialog_object(ab.dialog)
    t = bg3.timeline_object(ab.timeline, d)

    speaker_idx_tav = d.get_speaker_slot_index(bg3.SPEAKER_PLAYER)
    speaker_idx_shadowheart = d.get_speaker_slot_index(bg3.SPEAKER_SHADOWHEART)

    post_incubus_reaction_start_node_uuid = '31910643-2244-47b4-b28e-4ccc8b7dc681'
    i_am_sorry_node_uuid = '730c9215-a8b0-441e-944b-18aeba1514dd'
    we_need_to_talk_node_uuid = '896e03d8-0ec3-497a-aaad-78e073190a7b'
    why_do_you_look_node_uuid = 'e76b8013-7b85-4c4a-b25d-b6a208a02120'
    theres_no_we_node_uuid = '4e300238-8e9e-4071-b606-a19230a50e4d'
    youd_be_wise_to_forget_me_node_uuid = '00d79623-35fa-4300-826a-6afb299736eb'
    you_finally_showed_yourself_node_uuid = 'c419fc9b-c179-42bc-846b-53da4b861ad6'
    keep_away_from_me_node_uuid = 'b4d5883e-c877-4433-89cc-c78cb1838ac1'

    # Cameras looking at Shadowheart
    # 8942c483-83c9-4974-9f47-87cd1dd10828
    # d76eaab3-040b-4871-9c1d-4a8624f37cd2

    # What do you want?
    d.create_standard_dialog_node(
        post_incubus_reaction_start_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [i_am_sorry_node_uuid, we_need_to_talk_node_uuid, why_do_you_look_node_uuid],
        bg3.text_content('hfe6f29f1gb2a4g4d56g9928g6189f20f8142', 1),
        constructor = bg3.dialog_object.GREETING,
        root = True,
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_State_PartneredWithShadowheart, False, speaker_idx_tav),
                bg3.flag(bg3.FLAG_ORI_State_WasPartneredWithShadowheart, True, speaker_idx_tav),
                bg3.flag(bg3.FLAG_ORI_State_HandledBreakupWithShadowheart, False, speaker_idx_tav),
                bg3.flag(Tav_Played_With_Incubus.uuid, True, speaker_idx_tav),
                bg3.flag(Shadowheart_Approval_Set_To_Zero.uuid, True, speaker_idx_tav)
            )),
        ))
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '1.01',
        post_incubus_reaction_start_node_uuid,
        (('1.1', '0e8837db-4344-48d0-9175-12262c73806b'), (None, '95a53513-08ce-4d80-ae74-e306b51db565')),
        phase_duration = '1.2',
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 128, 1),),
            bg3.SPEAKER_PLAYER: ((0.0, 8, None),)
        })

    # I am sorry you had to watch all that happened between me and Haarlep. Let's just forget we've ever been there, shall we?
    d.create_standard_dialog_node(
        i_am_sorry_node_uuid,
        bg3.SPEAKER_PLAYER,
        [theres_no_we_node_uuid],
        bg3.text_content('h58b582d2gb6ceg428dga83eg173f46859af9', 1),
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(Shadowheart_Saw_Tav_Played_With_Incubus.uuid, True, speaker_idx_tav),
            )),
        ),
        constructor = bg3.dialog_object.QUESTION)
    # So, about that little incident with the incubus. We...
    d.create_standard_dialog_node(
        we_need_to_talk_node_uuid,
        bg3.SPEAKER_PLAYER,
        [theres_no_we_node_uuid],
        bg3.text_content('hcd1956bag717cg4d73gbc9egfa85c62cf3b2', 1),
        constructor = bg3.dialog_object.QUESTION)
    # What is that look on your face? Is something wrong?
    d.create_standard_dialog_node(
        why_do_you_look_node_uuid,
        bg3.SPEAKER_PLAYER,
        [you_finally_showed_yourself_node_uuid],
        bg3.text_content('hf48e5c20g24d7g4ad8g8adag3c98a1515653', 1),
        constructor = bg3.dialog_object.QUESTION)

    # There is no 'we'. Not anymore.
    d.create_standard_dialog_node(
        theres_no_we_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [youd_be_wise_to_forget_me_node_uuid],
        bg3.text_content('h6dc58f69gea0eg4dc8ga62ega1a743640d1f', 1))
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '3.37',
        theres_no_we_node_uuid,
        (('3.5', 'd76eaab3-040b-4871-9c1d-4a8624f37cd2'), (None, '95a53513-08ce-4d80-ae74-e306b51db565')),
        phase_duration = '5.0',
        fade_in = 0.0,
        fade_out = 2.0,
        performance_fade = 2.0,
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 8, 2), (1.93, 8, 3)),
            bg3.SPEAKER_PLAYER: ((0.0, 1, 0), (4.0, 8, 2))
        })
    t.create_tl_actor_node(bg3.timeline_object.LOOK_AT, bg3.SPEAKER_SHADOWHEART, '0.0', '5.0', (
        t.create_look_at_key(
            0.0,
            target = bg3.SPEAKER_PLAYER,
            bone = 'Head_M',
            turn_mode = 3,
            turn_speed_multiplier = 0.3,
            head_turn_speed_multiplier = 0.1,
            weight = 1.0,
            eye_look_at_bone = 'Head_M'
        ),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.LOOK_AT, bg3.SPEAKER_PLAYER, '0.0', '5.0', (
        t.create_look_at_key(
            0.0,
            target = bg3.SPEAKER_SHADOWHEART,
            bone = 'Head_M',
            turn_mode = 3,
            turn_speed_multiplier = 0.3,
            head_turn_speed_multiplier = 0.1,
            weight = 1.0,
            eye_look_at_bone = 'Head_M'
        ),
        t.create_look_at_key(
            4.3,
            target = bg3.SPEAKER_SHADOWHEART,
            bone = 'Head_M',
            turn_mode = 3,
            turn_speed_multiplier = 0.3,
            head_turn_speed_multiplier = 0.1,
            weight = 1.0,
            offset = (0.0, -8.0, 0.0),
            eye_look_at_bone = 'Head_M'
        ),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.ATTITUDE, bg3.SPEAKER_PLAYER, '0.0', '5.0', (
        t.create_attitude_key(3.7, bg3.ATTITUDE_DIAG_Pose_Confused_L_01, bg3.ATTITUDE_DIAG_T_Pose),
    ), is_snapped_to_end = True)
    

    # You finally showed yourself - I thought you might try and avoid me.
    d.create_standard_dialog_node(
        you_finally_showed_yourself_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [youd_be_wise_to_forget_me_node_uuid],
        bg3.text_content('hfd85464cg1480g417dgbf3ag3f8fea9ec234', 1))
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '4.28',
        you_finally_showed_yourself_node_uuid,
        (('4.5', 'd76eaab3-040b-4871-9c1d-4a8624f37cd2'), (None, '95a53513-08ce-4d80-ae74-e306b51db565')),
        phase_duration = '5.5',
        fade_in = 0.0,
        fade_out = 2.0,
        performance_fade = 2.0,
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 8, None), (2.5, 8, 1), (4.0, 8, 3)),
            bg3.SPEAKER_PLAYER: ((0.0, 1, 0), (4.9, 8, None))
        })
    t.create_tl_actor_node(bg3.timeline_object.LOOK_AT, bg3.SPEAKER_SHADOWHEART, '0.0', '5.5', (
        t.create_look_at_key(
            0.0,
            target = bg3.SPEAKER_PLAYER,
            bone = 'Head_M',
            turn_mode = 3,
            turn_speed_multiplier = 0.3,
            head_turn_speed_multiplier = 0.1,
            weight = 1.0,
            eye_look_at_bone = 'Head_M'
        ),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.LOOK_AT, bg3.SPEAKER_PLAYER, '0.0', '5.5', (
        t.create_look_at_key(
            0.0,
            target = bg3.SPEAKER_SHADOWHEART,
            bone = 'Head_M',
            turn_mode = 3,
            turn_speed_multiplier = 0.3,
            head_turn_speed_multiplier = 0.1,
            weight = 1.0,
            eye_look_at_bone = 'Head_M'
        ),
        t.create_look_at_key(
            4.9,
            target = bg3.SPEAKER_SHADOWHEART,
            bone = 'Head_M',
            turn_mode = 3,
            turn_speed_multiplier = 0.3,
            head_turn_speed_multiplier = 0.1,
            weight = 1.0,
            offset = (0.0, -8.0, 0.0),
            eye_look_at_bone = 'Head_M'
        ),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.ATTITUDE, bg3.SPEAKER_PLAYER, '0.0', '5.5', (
        t.create_attitude_key(4.7, '7afbcfa6-55cb-4272-ba5b-d905175e4317', bg3.ATTITUDE_DIAG_T_Pose),
    ), is_snapped_to_end = True)

    # You would be wise to forget me. I can only hope I one day forget you.
    d.create_standard_dialog_node(
        youd_be_wise_to_forget_me_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [keep_away_from_me_node_uuid],
        bg3.text_content('hd71c095eg2810g42beg80f8g7002fcb6a4c6', 2))
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '5.73',
        youd_be_wise_to_forget_me_node_uuid,
        (('6.0', 'd76eaab3-040b-4871-9c1d-4a8624f37cd2'), (None, '95a53513-08ce-4d80-ae74-e306b51db565')),
        phase_duration = '8.0',
        fade_in = 2.0,
        fade_out = 0.0,
        performance_fade = 2.0,
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 8, 1), (2.81, 8, 2)),
            bg3.SPEAKER_PLAYER: ((0.0, 128, 0),)
        },
        attitudes = {
            bg3.SPEAKER_PLAYER: (
                (6.5, bg3.ATTITUDE_DIAG_Pose_Crossed_01, bg3.ATTITUDE_DIAG_T_Pose, None),
            )
        })

    # The sooner we part ways, the better. Until then, keep away from me.
    d.create_standard_dialog_node(
        keep_away_from_me_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [],
        bg3.text_content('h2d480978gaaabg44c2gb35fgcd02da44ec86', 1),
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_State_HandledBreakupWithShadowheart, True, speaker_idx_tav),
            )),
        ),
        end_node = True)
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '5.41',
        keep_away_from_me_node_uuid,
        ((None, 'd76eaab3-040b-4871-9c1d-4a8624f37cd2'),),
        phase_duration = '5.8',
        fade_in = 0.0,
        fade_out = 0.0,
        performance_fade = 0.0,
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 4, None), (2.61, 16, None), (4.19, 128, None)),
            bg3.SPEAKER_PLAYER: ((0.0, 128, 0),)
        },
        attitudes = {
            bg3.SPEAKER_PLAYER: (
                (0.0, bg3.ATTITUDE_DIAG_Pose_Stand_L_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, None),
            )
        })

    d.add_root_node(post_incubus_reaction_start_node_uuid, index = 0)


def create_intimate_followups() -> None:
    ################################################################################################
    # Dialog: ShadowHeart_InParty2_Nested_DefaultChapter.lsf
    ################################################################################################

    ab = game_assets.get_modded_dialog_asset_bundle('ShadowHeart_InParty2_Nested_DefaultChapter')
    d = bg3.dialog_object(ab.dialog)

    # speaker slot indexes
    speaker_idx_shadowheart = d.get_speaker_slot_index(bg3.SPEAKER_SHADOWHEART)
    speaker_idx_tav = d.get_speaker_slot_index(bg3.SPEAKER_PLAYER)

    of_course_node_uuid = '23749c85-4289-4965-a7db-1909f5cb63a2' # existing node
    about_our_night_together_node_uuid = 'fd4f6e5f-c41b-4ada-9cb2-0455a8211625'
    about_what_we_did_before_node_uuid = 'c631e115-5959-40bf-931d-3fafb86bd52e'
    nested_romance_node_uuid = '03baebb7-4fed-468c-b277-99e7fa2cf56c'

    # About our night together, at the beach...
    d.create_standard_dialog_node(
        about_our_night_together_node_uuid,
        bg3.SPEAKER_PLAYER,
        [nested_romance_node_uuid],
        bg3.text_content('h2f8c39d4gf90dg4dc5gaa22gfa31ee1c4740', 1),
        constructor = bg3.dialog_object.QUESTION,
        show_once = True,
        checkflags = (
            bg3.flag_group('Global', (
                bg3.flag(bg3.FLAG_NIGHT_Shadowheart_Skinnydipping, True, None),
                bg3.flag(bg3.FLAG_ORI_Shadowheart_State_PostSkinnydipping_Discussed, True, None),
                bg3.flag(Shadowheart_Turned_Away_From_Shar.uuid, True, None),
                bg3.flag(bg3.FLAG_ORI_Shadowheart_State_AbortedSkinnydipping, False, None),
            )),
            bg3.flag_group('Object', (
                bg3.flag(Shadowheart_Has_Doubts_About_Tav.uuid, False, speaker_idx_tav),
            )),
        ),
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(Skinny_Dipping_Recurrent_Conversation.uuid, True, speaker_idx_tav),
            )),
        ))

    nested_dialog_uuid = get_dialog_uuid('ShadowHeart_InParty2_Nested_Romance')
    d.create_nested_dialog_node(
        nested_romance_node_uuid,
        nested_dialog_uuid,
        ['690a3b4c-1954-4dc8-bbfb-8d797b1105c9'],
        speaker_count = 2
    )
    d.create_jump_dialog_node('690a3b4c-1954-4dc8-bbfb-8d797b1105c9', of_course_node_uuid, 2)


    # About what we did before. The Nightfall ritual...
    d.create_standard_dialog_node(
        about_what_we_did_before_node_uuid,
        bg3.SPEAKER_PLAYER,
        [nested_romance_node_uuid],
        bg3.text_content('h2afbd894g7427g4791g9ec5g8c61963fd591', 1),
        constructor = bg3.dialog_object.QUESTION,
        show_once = True,
        checkflags = (
            bg3.flag_group('Global', (
                bg3.flag(bg3.FLAG_NIGHT_Shadowheart_NightfallRitual, True, None),
                bg3.flag(bg3.FLAG_NIGHT_Shadowheart_Skinnydipping, False, None),
                bg3.flag(bg3.FLAG_ORI_Shadowheart_State_PostNightfall_Discussed, True, None),
                bg3.flag(Shadowheart_Turned_Away_From_Shar.uuid, False, None),
                bg3.flag(bg3.FLAG_ORI_Shadowheart_State_AbortedNightfall, False, None),
            )),
            bg3.flag_group('Object', (
                bg3.flag(Nightfall_Cant_Happen_Again.uuid, False, speaker_idx_tav),
            )),
        ),
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_Shadowheart_InParty_Event_NightfallQuestionStart, True, speaker_idx_tav),
            )),
        ))

    d.add_child_dialog_node(of_course_node_uuid, about_what_we_did_before_node_uuid, 0)
    d.add_child_dialog_node(of_course_node_uuid, about_our_night_together_node_uuid, 0)


    ################################################################################################
    # Dialog: ShadowHeart_InParty2_Nested_Romance.lsf
    ################################################################################################

    ab = game_assets.get_modded_dialog_asset_bundle('ShadowHeart_InParty2_Nested_Romance')
    d = bg3.dialog_object(ab.dialog)
    t = bg3.timeline_object(ab.timeline, d)

    # Reaction -10 if Tav says they didn't like the night they spent with her
    reaction_minus_10 = bg3.reaction_object.create_new(game_assets.files, { bg3.SPEAKER_SHADOWHEART: -10 }, uuid = '7c381bd5-0ea7-4832-a175-8898313f6715')

    im_not_sure_we_should_do_that_again_node_uuid = 'f340ef8f-42c9-47bd-9613-93d18a692ba4' # existing node
    i_think_it_mightve_been_a_mistake_node_uuid = '337e0839-651b-4364-a0d4-fa26f301ffbb'   # existing node

    alls_well_i_hope_node_uuid = '03e84b46-bb3c-49da-9525-f7f8e29c0a9b'

    # This hides an option to tell her it was a mistake if they discussed this matter previously
    # and adds -10 disapproval
    d.add_dialog_flags(
        im_not_sure_we_should_do_that_again_node_uuid,
        checkflags = (
            bg3.flag_group('Global', (
                bg3.flag(bg3.FLAG_ORI_Shadowheart_State_PostSkinnydipping_Discussed, False, None),
            )),
        ))
    d.set_dialog_attribute(im_not_sure_we_should_do_that_again_node_uuid, 'ApprovalRatingID', reaction_minus_10.uuid, attribute_type = 'guid')
    d.add_dialog_flags(
        i_think_it_mightve_been_a_mistake_node_uuid,
        checkflags = (
            bg3.flag_group('Global', (
                bg3.flag(bg3.FLAG_ORI_Shadowheart_State_PostSkinnydipping_Discussed, False, None),
            )),
        ))
    d.set_dialog_attribute(i_think_it_mightve_been_a_mistake_node_uuid, 'ApprovalRatingID', reaction_minus_10.uuid, attribute_type = 'guid')

    i_really_needed_that_node_uuid = '56891e48-ff30-4b99-91aa-3aebbbcb8a12'
    im_glad_i_feel_the_same_way_node_uuid = '605d9bc5-253e-4cfd-badf-2a677c33101e' # existing node
    youll_need_plenty_of_practice_node_uuid = 'd35b52b1-f77b-40fe-ab6a-29e97bca2594' # existing node
    well_see_node_uuid = '301d7363-48c0-414e-8624-03cdea7e989d' # existing node
    im_still_finding_sand_node_uuid = '35233704-6b10-441f-b3b7-7262029366c6' # existing node
    love_to_help_you_wash_node_uuid = '2100ee84-789c-40f8-b098-4e48994fa97e'
    you_dont_waste_time_node_uuid = 'de00b84f-bb16-4e75-bfd4-a355c1c620cc'
    perhaps_well_see_node_uuid = 'a02476cc-535b-4ffc-8b19-986fb9464842' # existing node

    # h8a068db5gfd71g4b2dg91f5g959e9654c0b7
    # You don't waste time, do you?

    # All's well I hope...?
    d.create_standard_dialog_node(
        alls_well_i_hope_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [
            i_really_needed_that_node_uuid,
            youll_need_plenty_of_practice_node_uuid,
            well_see_node_uuid
        ],
        bg3.text_content('hd07291d2g217dg47fdg8fd3ga02a235f6b7b', 1),
        constructor = bg3.dialog_object.GREETING,
        root = True,
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(Skinny_Dipping_Recurrent_Conversation.uuid, True, speaker_idx_tav),
            )),
        ),
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(Skinny_Dipping_Recurrent_Conversation.uuid, False, speaker_idx_tav),
            )),
        ))
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '1.375',
        alls_well_i_hope_node_uuid,
        (('1.9', 'd76eaab3-040b-4871-9c1d-4a8624f37cd2'), (None, 'e08db860-1e62-4271-bf4e-d51602468573')),
        phase_duration = '2.0',
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 64, None), (1.2, 4, None)),
            bg3.SPEAKER_PLAYER: ((0.0, 2, None),),
        })
    d.add_root_node(alls_well_i_hope_node_uuid)

    # It was wonderful. I really needed that...
    d.create_standard_dialog_node(
        i_really_needed_that_node_uuid,
        bg3.SPEAKER_PLAYER,
        [im_glad_i_feel_the_same_way_node_uuid],
        bg3.text_content('h17919bb2g242dg4852ga6degae6eaee08d11', 1),
        constructor = bg3.dialog_object.QUESTION)

    # I'd love to help you wash all that sand out of your hair.
    d.create_standard_dialog_node(
        love_to_help_you_wash_node_uuid,
        bg3.SPEAKER_PLAYER,
        [you_dont_waste_time_node_uuid],
        bg3.text_content('h2a7a961bg5a07g4adbgbab8g56db98e84814', 1),
        constructor = bg3.dialog_object.QUESTION)

    # You don't waste time, do you?
    d.create_standard_dialog_node(
        you_dont_waste_time_node_uuid,
        bg3.SPEAKER_PLAYER,
        [perhaps_well_see_node_uuid],
        bg3.text_content('h93d2e7aeg716eg463fga1dag2f1110664d35', 1))
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '1.71',
        you_dont_waste_time_node_uuid,
        (('1.71', 'd76eaab3-040b-4871-9c1d-4a8624f37cd2'), (None, 'e08db860-1e62-4271-bf4e-d51602468573')),
        phase_duration = '4.2',
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 64, 0), (0.8, 64, 1)),
            bg3.SPEAKER_PLAYER: ((1.7, 64, None), (2.5, 62, 2), (3.2, 2, 1))
        },
        attitudes = {
            bg3.SPEAKER_PLAYER: (
                (0.0, bg3.ATTITUDE_DIAG_Pose_Stand_L_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, 3),                
                (1.72, bg3.ATTITUDE_DIAG_Pose_Hips_01, bg3.ATTITUDE_DIAG_T_Pose, 3),)
        })    

    d.add_child_dialog_node(im_still_finding_sand_node_uuid, love_to_help_you_wash_node_uuid)

    #
    # Nightfall romance discussion
    #
    this_cant_happen_again_node_uuid = 'e5aa9b18-b568-4f27-b367-95f2bb4ac638'
    d.add_dialog_flags(this_cant_happen_again_node_uuid, setflags = (
        bg3.flag_group('Object', (
            bg3.flag(Nightfall_Cant_Happen_Again.uuid, True, speaker_idx_tav),
        )),
    ))
    d.set_dialog_attribute(this_cant_happen_again_node_uuid, 'ApprovalRatingID', reaction_minus_10.uuid, attribute_type = 'guid')


def create_post_dj_romance_conversation() -> None:
    ############################################################################################
    # Dialog: ShadowHeart_InParty2.lsf
    ############################################################################################

    ab = game_assets.get_modded_dialog_asset_bundle('ShadowHeart_InParty')
    d = bg3.dialog_object(ab.dialog)
    t = bg3.timeline_object(ab.timeline, d)

    speaker_idx_shadowheart = d.get_speaker_slot_index(bg3.SPEAKER_SHADOWHEART)
    speaker_idx_tav = d.get_speaker_slot_index(bg3.SPEAKER_PLAYER)

    sorry_was_lost_in_thought_node_uuid = 'c6359e1e-f7f4-4cec-8ede-d03a70a3a7eb'
    creep_partnered_node_uuid = '80787b2a-43f1-4a63-b454-975cd890820d'
    jump_to_question_bank_node_uuid = 'eeea5c5c-5cd1-4ab3-bf4b-d43678e52c9b'
    tav_post_dj_romance_questions_node_uuid = '63adaefc-8450-46f9-802d-b24018653393'
    all_that_happened_in_the_cloister_node_uuid = 'a3f3628e-8e29-4d43-b131-7acd2992562d'
    more_than_i_thought_would_be_possible_node_uuid = 'edd63e07-9d59-4977-9c6d-47d3b105e73c'
    i_still_cant_believe_node_uuid = '1c964c1a-3579-4226-af13-ee944d697975'
    maybe_i_shouldnt_be_entirely_shocked_node_uuid = '17bb2834-9cea-4c53-a21a-37bac9d1e847'
    i_just_wanted_to_remind_you_node_uuid = '8a95c964-50ad-45f7-a873-f105fc70e0da'
    youve_done_more_to_help_me_node_uuid = 'a9ea394c-abb8-4253-9397-deee0971ef97'
    i_thought_my_faith_node_uuid = '9b56d385-1f37-442f-b47d-85e072280d8d'
    kiss_her_node_uuid = '2a9ba87b-ff10-47f1-8d21-44d7b48d275a'
    now_and_always_node_uuid = '8d29104a-6dca-4f0d-8a06-e279c9780dde'
    cannot_be_any_other_way_node_uuid = 'b13ee1b0-5d96-4151-bf15-2eb000fbcc56'
    yes_i_love_you_node_uuid = 'b82ed493-b442-45ef-a291-45c48a872307'
    kiss_node_uuid = '2372a454-1c1d-47b7-b632-06b25de2d168'
    kiss_nested_node_uuid = '2fc9117e-7733-4e42-a6bb-e490fea8d425'
    kiss_reaction_node_uuid = 'c63520d1-5038-4c80-a5e7-5cbd9e671bf8'

    """
    cameras
    d76eaab3-040b-4871-9c1d-4a8624f37cd2 SH  -> SH
    0e8837db-4344-48d0-9175-12262c73806b SH  -> SH
    8942c483-83c9-4974-9f47-87cd1dd10828 Tav -> SH
    2b1dd4ed-5f01-46a2-a244-ac074d0feff0 Tav -> Tav
    95a53513-08ce-4d80-ae74-e306b51db565 Tav -> Tav
    cde43894-62c3-4f23-8ea7-b772f9357697 Tav -> Tav
    fd96b957-6a74-4f97-a035-eb9641c48242 SH  -> Tav
    b188e5c9-4ec1-456f-8408-b4a5da405cc5 Tav -> SH
    """

    # Sorry. Was lost in thought... something the matter?
    d.create_standard_dialog_node(
        sorry_was_lost_in_thought_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [
            creep_partnered_node_uuid,
            tav_post_dj_romance_questions_node_uuid,
        ],
        bg3.text_content('h5c168822g2c25g4c30g8758g256b3becc53b', 1),
        constructor = bg3.dialog_object.GREETING,
        root = True,
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(Shadowheart_Post_DJ_Romance.uuid, True, speaker_idx_tav),
            )),
        ),
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(Shadowheart_Post_DJ_Romance.uuid, False, speaker_idx_tav),
            )),
        ))
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '4.2',
        sorry_was_lost_in_thought_node_uuid,
        (('4.3', '0e8837db-4344-48d0-9175-12262c73806b'), (None, 'fd96b957-6a74-4f97-a035-eb9641c48242')),
        phase_duration = '4.7',
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 16, None), (1.63, 16, 1), (3.06, 4, None)),
            bg3.SPEAKER_PLAYER: ((0.0, 4, None),)
        })

    d.add_root_node_after('36f63b74-8cc6-4766-87ad-7247d092e6db', sorry_was_lost_in_thought_node_uuid)

    d.create_standard_dialog_node(
        creep_partnered_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [jump_to_question_bank_node_uuid],
        None,
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(Shadowheart_Lost_Faith_In_Tav.uuid, True, speaker_idx_tav),
            )),
        ),
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(Shadowheart_Rejects_Proposal.uuid, True, speaker_idx_shadowheart),
            )),
        ))

    d.create_jump_dialog_node(jump_to_question_bank_node_uuid, bg3.SHADOWHEART_QUESTION_BANK_ROOT_NODE_UUID, 2)

    d.create_standard_dialog_node(
        tav_post_dj_romance_questions_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [
            all_that_happened_in_the_cloister_node_uuid,
            i_still_cant_believe_node_uuid,
            i_just_wanted_to_remind_you_node_uuid,
            kiss_her_node_uuid
        ],
        None)

    # All that happened in the cloister, does it mean anything for what you and I share?
    d.create_standard_dialog_node(
        all_that_happened_in_the_cloister_node_uuid,
        bg3.SPEAKER_PLAYER,
        [more_than_i_thought_would_be_possible_node_uuid],
        bg3.text_content('hca13afeag937fg43d6gbb06gff8f0a675b45', 1),
        constructor = bg3.dialog_object.QUESTION)

    # I still can't believe you turned away from Shar. What comes next for us?
    d.create_standard_dialog_node(
        i_still_cant_believe_node_uuid,
        bg3.SPEAKER_PLAYER,
        [maybe_i_shouldnt_be_entirely_shocked_node_uuid],
        bg3.text_content('hfc1c1a85g0853g4dcbgb29bg0957807df0e1', 1),
        constructor = bg3.dialog_object.QUESTION,
        checkflags = (
            bg3.flag_group('Tag', (
                bg3.flag(bg3.GOD_SELUNE, True, speaker_idx_tav),
            )),
        ))

    # I just wanted to remind you, I'm here for you, if you need me.
    d.create_standard_dialog_node(
        i_just_wanted_to_remind_you_node_uuid,
        bg3.SPEAKER_PLAYER,
        [youve_done_more_to_help_me_node_uuid],
        bg3.text_content('h2dc007d7ga4cdg4d87g9113g9940966c49d8', 1),
        constructor = bg3.dialog_object.QUESTION)

    # Kiss her
    d.create_standard_dialog_node(
        kiss_her_node_uuid,
        bg3.SPEAKER_PLAYER,
        [kiss_node_uuid],
        bg3.text_content('hc41af286gefabg4061gbe97g5786d98267ac', 1),
        constructor = bg3.dialog_object.QUESTION)

    # More than I thought would be possible, considering the short time we had...
    d.create_standard_dialog_node(
        more_than_i_thought_would_be_possible_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [i_thought_my_faith_node_uuid],
        bg3.text_content('h6e79dfd8g6ec8g439fgb01fg4b1a1bb51327', 1))
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '4.32',
        more_than_i_thought_would_be_possible_node_uuid,
        ((None, 'b188e5c9-4ec1-456f-8408-b4a5da405cc5'),),
        phase_duration = '4.6',
        emotions = { bg3.SPEAKER_SHADOWHEART: ((0.0, 32, None), (3.3, 4, None)) })

    # Maybe I shouldn't be entirely shocked - I did fall for a Selunite, after all.
    d.create_standard_dialog_node(
        maybe_i_shouldnt_be_entirely_shocked_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [i_thought_my_faith_node_uuid],
        bg3.text_content('h9de02247gfc21g49c6g9d8bgbfd39e6edef9', 1))
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '6.32',
        maybe_i_shouldnt_be_entirely_shocked_node_uuid,
        ((None, 'b188e5c9-4ec1-456f-8408-b4a5da405cc5'),),
        phase_duration = '6.7',
        emotions = { bg3.SPEAKER_SHADOWHEART: ((0.0, 2048, None),) })

    # I suppose I do, don't I? You've done more to help me than my faith has in recent times, if I'm honest. Thank you.
    d.create_standard_dialog_node(
        youve_done_more_to_help_me_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [i_thought_my_faith_node_uuid],
        bg3.text_content('h1d16f85egfc30g49d3ga767g1f643acb0d5d', 1))
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '10.97',
        youve_done_more_to_help_me_node_uuid,
        ((None, 'b188e5c9-4ec1-456f-8408-b4a5da405cc5'),),
        phase_duration = '11.3',
        emotions = { bg3.SPEAKER_SHADOWHEART: ((0.0, 64, None), (1.7, 2, None), (4.71, 64, None), (10.2, 2, None)) })

    # I thought my faith was the most important thing in my life - I couldn't have been more wrong.
    d.create_standard_dialog_node(
        i_thought_my_faith_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [now_and_always_node_uuid],
        bg3.text_content('h0a2ce1f6gad2fg4e76g8c9age7490daf36b9', 1))
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '6.2',
        i_thought_my_faith_node_uuid,
        ((None, 'd76eaab3-040b-4871-9c1d-4a8624f37cd2'),),
        phase_duration = '6.7',
        emotions = { bg3.SPEAKER_SHADOWHEART: ((0.0, 16, None), (3.756, 256, None), (4.556, 16, None)) })

    # I've squandered too much time already. I want to be with you. Now and always. Do you want the same?
    d.create_standard_dialog_node(
        now_and_always_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [cannot_be_any_other_way_node_uuid, yes_i_love_you_node_uuid],
        bg3.text_content('h84af1273g4437g4b86gb1aag53e0b065deda', 1))
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '12.83',
        now_and_always_node_uuid,
        (('12.9', '0e8837db-4344-48d0-9175-12262c73806b'), (None, 'fd96b957-6a74-4f97-a035-eb9641c48242')),
        phase_duration = '12.99',
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 16, None), (10.49, 64, None)),
            bg3.SPEAKER_PLAYER: ((0.0, 64, None),)
        })

    # Of course, it cannot be any other way.
    d.create_standard_dialog_node(
        cannot_be_any_other_way_node_uuid,
        bg3.SPEAKER_PLAYER,
        [kiss_node_uuid],
        bg3.text_content('h620ae1d5g1041g4969gb2e0g56f9b5e9d1ae', 1),
        constructor = bg3.dialog_object.QUESTION)

    # Yes, I do. I love you.
    d.create_standard_dialog_node(
        yes_i_love_you_node_uuid,
        bg3.SPEAKER_PLAYER,
        [kiss_node_uuid],
        bg3.text_content('hbbfbc3ceg2938g41a2gaaf6gc5bb605da6f7', 1),
        constructor = bg3.dialog_object.QUESTION)

    d.create_standard_dialog_node(
        kiss_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [kiss_nested_node_uuid],
        None,
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(ORI_ShadowheartKiss_VersionB.uuid, True, speaker_idx_shadowheart),
            )),
        ))
    kiss_nested_dialog_uuid = get_dialog_uuid('ShadowHeart_InParty2_Nested_ShadowheartKiss')
    d.create_nested_dialog_node(
        kiss_nested_node_uuid,
        kiss_nested_dialog_uuid,
        [kiss_reaction_node_uuid],
        speaker_count = 2)
    add_dialog_dependency(ab, kiss_nested_dialog_uuid)

    # Hard to imagine there was a time when I didn't have you to hold me.
    d.create_standard_dialog_node(
        kiss_reaction_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [],
        bg3.text_content('h714be156g6df0g4027gae01g55e7dc00a214', 1),
        setflags = (
            bg3.flag_group('Global', (
                bg3.flag(Shadowheart_Post_DJ_Now_And_Always.uuid, True, None),
            )),
        ),
        end_node = True)
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '3.3',
        kiss_reaction_node_uuid,
        ((None, 'd76eaab3-040b-4871-9c1d-4a8624f37cd2'),),
        phase_duration = '3.5',
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 2, 2), (1.4, 2, None)),
            bg3.SPEAKER_PLAYER: ((0.0, 2, None),)
        })


def patch_post_shadowfell_conversation() -> None:
    ab = game_assets.get_modded_dialog_asset_bundle('ShadowHeart_InParty2_Nested_ShadowCurseChapter')
    d = bg3.dialog_object(ab.dialog)
    t = bg3.timeline_object(ab.timeline, d)

    speaker_idx_tav = d.get_speaker_slot_index(bg3.SPEAKER_PLAYER)

    ###########################################################################
    # This adds a new Tav's response
    ###########################################################################

    now_and_always_node_uuid = '59ded4e3-b27c-48e9-9925-5f6e05c50907' # existing node
    shows_what_i_know_node_uuid = '27bcc860-5695-41b3-856d-dc96915e3afc' # existing node
    i_love_you_node_uuid = '0024209d-b950-4613-a798-b3edebdf5f5a'
    are_you_trying_to_make_me_blush_node_uuid = 'f8416b9f-a60d-4ba8-b78b-f73f6e7c9639'

    # Yes. I ... love you.
    d.create_standard_dialog_node(
        i_love_you_node_uuid,
        bg3.SPEAKER_PLAYER,
        [are_you_trying_to_make_me_blush_node_uuid],
        bg3.text_content('h18ffbc26g6b50g4068g8b32g273ff82086a0', 1),
        constructor = bg3.dialog_object.QUESTION,
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_State_PartneredWithShadowheart, True, speaker_idx_tav),
            )),
        ))

    # Are you trying to make me blush? I think it might just be working...
    d.create_standard_dialog_node(
        are_you_trying_to_make_me_blush_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [shows_what_i_know_node_uuid],
        bg3.text_content('h28718517g8121g4ad6gac91g8a63b8b9e512', 2))
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '6.91',
        are_you_trying_to_make_me_blush_node_uuid,
        (('6.91', 'ff50ec8e-d4ad-4e67-acb4-567576ba65bb'), (None, '82528b8d-561a-4888-b311-a048fef73338')),
        phase_duration = '8.0',
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 2, 23), (1.04, 64, 1), (4.26, 2, None), (6.09, 2, 1)),
            bg3.SPEAKER_PLAYER: ((6.91, 64, 1),)
        },
        attitudes = {
            bg3.SPEAKER_PLAYER: (
                ('6.92', bg3.ATTITUDE_DIAG_Pose_Confused_L_01, bg3.ATTITUDE_DIAG_T_Pose, None),
                ('8.0', bg3.ATTITUDE_DIAG_Pose_Stand_R_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, None),
            ),
        })

    d.add_child_dialog_node(now_and_always_node_uuid, i_love_you_node_uuid, 0)


bg3.add_build_procedure('patch_relationship_conversations', patch_relationship_conversations)
bg3.add_build_procedure('create_romance_events', create_romance_events)
bg3.add_build_procedure('create_reactions_to_creep_debacle', create_reactions_to_creep_debacle)
bg3.add_build_procedure('create_sharran_kiss', create_sharran_kiss)
bg3.add_build_procedure('create_entry_point_to_partnered_dialog', create_entry_point_to_partnered_dialog)
bg3.add_build_procedure('create_incubus_reaction', create_incubus_reaction)
bg3.add_build_procedure('create_post_incubus_breakup', create_post_incubus_breakup)
bg3.add_build_procedure('create_intimate_followups', create_intimate_followups)
bg3.add_build_procedure('create_post_dj_romance_conversation', create_post_dj_romance_conversation)
bg3.add_build_procedure('patch_post_shadowfell_conversation', patch_post_shadowfell_conversation)
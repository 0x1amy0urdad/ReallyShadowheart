from __future__ import annotations

import bg3moddinglib as bg3

from .context import game_assets
from .flags import *

from decimal import Decimal


just_stay_close_node_uuid = '8635f1ad-1af0-4d82-ace2-91396cb78ca6'
i_can_manage_node_uuid = 'c2680c2a-995e-4d2e-b465-1a7c825ca194'
more_the_drowning_node_uuid = '77e9165b-abc3-4b18-8921-6a65f36c47b7'
before_i_lose_my_nerve_node_uuid = '689f045d-23c9-4dff-b123-09a38a74c890'
what_wait_node_uuid = '2fd16a3c-9b67-4740-987b-048871cc31c3'
hermit_crab_node_uuid = '6ffac790-d38d-477c-9e47-394ff0919fad'
oh_hells_thats_cold_node_uuid = '4146b802-39f4-4856-b506-84370c7929e6'
my_feet_arent_touching_the_bottom_anymore_node_uuid = '94b7f8a7-531a-48ad-b369-2998e2115580'
tav_you_can_hold_onto_me_node_uuid = '5f932b4d-cd31-4a51-9024-e4bc9228e2ce'
tav_splash_her_playfully_node_uuid = '7b9b650a-b5dd-4239-9b5d-57d3d7e721a4'
you_didnt_need_to_wait_to_hold_me_node_uuid = 'c80a7c86-7c58-4f74-ba39-9d6e7456d74a'
shadowheart_splashes_tav_node_uuid = 'f94c267f-8961-4066-a2b3-6b108452b9f6'
you_pest_node_uuid = '2ef94465-c7ba-42a2-99bb-4a45ac407426'
come_here_node_uuid = '186aff51-a9ed-4dfe-a2aa-147bf5d40a0f'
flag_setter_node_uuid = '629f35e0-a7cd-4cfe-82f0-6bc9a26c7f0e'
thank_you_i_needed_that_node_uuid = 'a8c1641e-adee-4923-9ca9-beeb21cd0113'
i_dont_want_to_go_back_node_uuid = '6c5746e0-9304-48a4-9f39-e1660639d6da'

ACTOR_HERMIT_CRAB = '7105d35c-f0a9-4862-957f-e7ef8bde91a9'

##########################################################################################################
# Skinny dipping cutscene: more opportunities to slip away, fix for the black hair bug, etc
##########################################################################################################

def patch_act3_romance_conversations() -> None:

    ##########################################################################################################
    # Dialog: ShadowHeart_InParty2.lsf
    # This is a fix for the missed discussion about the night at the beach.
    # Vanilla game checks FLAG_ORI_State_WasPartneredWithShadowheart
    # The correct flag is FLAG_ORI_State_PartneredWithShadowheart
    ##########################################################################################################

    #d = bg3.dialog_object(files.get_file('Gustav', 'Mods/GustavDev/Story/DialogsBinary/Companions/ShadowHeart_InParty2.lsf'))

    ab = game_assets.get_modded_dialog_asset_bundle('ShadowHeart_InParty')
    d = bg3.dialog_object(ab.dialog)


    speaker_idx_tav = d.get_speaker_slot_index(bg3.SPEAKER_PLAYER)

    about_our_night_at_the_beach_node_uuid = 'b3bd2cbe-b758-11d7-038f-2966141bf7f9'

    d.set_dialog_flags(
        about_our_night_at_the_beach_node_uuid,
        checkflags = (
            bg3.flag_group('Global', (
                bg3.flag(bg3.FLAG_NIGHT_Shadowheart_Skinnydipping, True, None),
                bg3.flag(bg3.FLAG_ORI_Shadowheart_State_PostSkinnydipping_Discussed, False, None),
                bg3.flag(bg3.FLAG_ORI_Shadowheart_State_PostSkinnyDipping_DiscussionAvailable, True, None)
            )),
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_State_PartneredWithShadowheart, True, speaker_idx_tav),
            )),
        ))


    ##########################################################################################################
    # Dialog: ShadowHeart_InParty2_Nested_DefaultChapter.lsf
    # Adds a new line in Shadowheart's dialog. At night time in camp, if Shadowheart told Tav that
    # she hopes they'll have more opportunities to slip away,
    # Tav can ask Shadowheart to make more sandcastles.
    # This replays the skinny dipping cutscene with edits.
    ##########################################################################################################

    # d = bg3.dialog_object(files.get_file('Gustav', 'Mods/GustavDev/Story/DialogsBinary/Companions/ShadowHeart_InParty2_Nested_DefaultChapter.lsf'))
    # t = bg3.timeline_object(files.get_file('Gustav', 'Public/GustavDev/Timeline/Generated/ShadowHeart_InParty2_Nested_DefaultChapter.lsf'), d)

    ab = game_assets.get_modded_dialog_asset_bundle('ShadowHeart_InParty2_Nested_DefaultChapter')
    d = bg3.dialog_object(ab.dialog)
    t = bg3.timeline_object(ab.timeline, d)

    slot_idx_shadowheart = d.get_speaker_slot_index(bg3.SPEAKER_SHADOWHEART)
    slot_idx_tav = d.get_speaker_slot_index(bg3.SPEAKER_PLAYER)

    of_course_node_uuid = '23749c85-4289-4965-a7db-1909f5cb63a2' # existing node

    another_swim_lesson_node_uuid = 'ff663060-bb62-48d8-928d-5253b65da04b'
    another_swim_lesson2_node_uuid = '18b0de17-5427-4e75-9f94-2791b36311f7'
    took_the_words_node_uuid = 'dca8eede-5035-4977-bca7-cf8a08c1efb4'
    wait_until_others_asleep_node_uuid = '738a3386-1a00-4324-afe6-95cb236c127a'
    not_right_now_node_uuid = '62e11af0-bd3b-4f5a-8851-ca91dae393b4'

    # Others seem quite tired, they'll be asleep soon. Don't you think we could seize the opportunity?
    d.create_standard_dialog_node(
        another_swim_lesson_node_uuid,
        bg3.SPEAKER_PLAYER,
        [took_the_words_node_uuid, not_right_now_node_uuid],
        bg3.text_content('h06a5cd66g501bg402bgb1e3g41bd32d9ca18', 1),
        constructor=bg3.dialog_object.QUESTION,
        checkflags=(
            bg3.flag_group('Global', (
                bg3.flag(Shadowheart_Turned_Away_From_Shar.uuid, True, None),
                bg3.flag(bg3.FLAG_GLO_CAMP_State_NightMode, True, None),
            )),
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_State_PartneredWithShadowheart, True, slot_idx_tav),
                bg3.flag(Snuck_Away_To_Make_Sandcastles.uuid, False, slot_idx_shadowheart),
                bg3.flag(Shadowheart_More_Sandcastles.uuid, True, slot_idx_shadowheart),
                bg3.flag(Shadowheart_LongRest_Before_More_Sandcastles.uuid, True, slot_idx_shadowheart),
                bg3.flag(Shadowheart_More_Sandcastles_Replied.uuid, False, slot_idx_shadowheart),                     
            )),
        ))

    # This seems to be a perfect night to build a few sandcastles, don't you think?
    d.create_standard_dialog_node(
        another_swim_lesson2_node_uuid,
        bg3.SPEAKER_PLAYER,
        [took_the_words_node_uuid, not_right_now_node_uuid],
        bg3.text_content('hec9703c4g433cg4352gbfb1g5804f86ec900', 1),
        constructor=bg3.dialog_object.QUESTION,
        checkflags=(
            bg3.flag_group('Global', (
                bg3.flag(Shadowheart_Turned_Away_From_Shar.uuid, True, None),
                bg3.flag(bg3.FLAG_GLO_CAMP_State_NightMode, True, None),
            )),
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_State_PartneredWithShadowheart, True, slot_idx_tav),
                bg3.flag(Snuck_Away_To_Make_Sandcastles.uuid, True, slot_idx_shadowheart),
                bg3.flag(Shadowheart_More_Sandcastles.uuid, True, slot_idx_shadowheart),
                bg3.flag(Shadowheart_LongRest_Before_More_Sandcastles.uuid, True, slot_idx_shadowheart),
                bg3.flag(Shadowheart_More_Sandcastles_Replied.uuid, False, slot_idx_shadowheart),                     
            )),
        ))
    # This adds more opportunities to make sand castles
    d.add_child_dialog_node(of_course_node_uuid, another_swim_lesson_node_uuid, 0)
    d.add_child_dialog_node(of_course_node_uuid, another_swim_lesson2_node_uuid, 0)

    # You took the words right out of my mouth.
    d.create_standard_dialog_node(
        took_the_words_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [wait_until_others_asleep_node_uuid],
        bg3.text_content('hc89bd245g631dg480ag9218g7d20f8f9422c', 1, '72bb47ca-818d-49ca-b8c6-aed90ed59a6a'),
        checkflags=(
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_Approval_AtLeast_60_For_Sp2, True, slot_idx_shadowheart),
                bg3.flag(Shadowheart_Has_Doubts_About_Tav.uuid, False, slot_idx_tav),
            )),
        )
    )
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '2.71',
        took_the_words_node_uuid,
        ((None, '7b067edd-f53f-49e1-95bc-0986e6e2ca2f'),),
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 2, 1), (1.0, 2, 2)),
            bg3.SPEAKER_PLAYER: ((0.0, 2, None),)
        }
    )

    # Wait until the others are asleep, then come with me... Get some rest while you can.
    d.create_standard_dialog_node(
        wait_until_others_asleep_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [],
        bg3.text_content('h40c1c09egd7bcg4575g8a9dgd8ee7a05e75d', 1, '5ca4af10-9855-40f2-8abe-d846c0f4d9b0'),
        setflags=(
            bg3.flag_group('Object', (
                bg3.flag(Shadowheart_More_Sandcastles_Tonight.uuid, True, slot_idx_shadowheart),
                bg3.flag(Shadowheart_More_Sandcastles_Replied.uuid, True, slot_idx_shadowheart),
            )),
        ),
        end_node=True
    )
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '6.506',
        wait_until_others_asleep_node_uuid,
        (
            ('4.506', 'd76eaab3-040b-4871-9c1d-4a8624f37cd2'),
            (None,  'b4155335-5e08-4d85-8ccd-ddebf5507447'),
        ),
        emotions={
            bg3.SPEAKER_SHADOWHEART: ((0.0, 2, None), (1.33, 2, 1), (3.1, 2, None), (4.0, 2, 1)),
            bg3.SPEAKER_PLAYER: ((0.0, 2, None),)
        }
    )

    # Perhaps... not right now. As tempting as you make it sound.
    d.create_standard_dialog_node(
        not_right_now_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [],
        bg3.text_content('h2df9f309g5badg4c17gb9efgff4360cabd70', 1, '0d7304c8-681a-4b1e-b5e9-5476d52fa095'),
        setflags=(
            bg3.flag_group('Object', (
                bg3.flag(Shadowheart_More_Sandcastles_Replied.uuid, True, slot_idx_shadowheart),
            )),
        ),
        end_node=True
    )
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '4.883',
        not_right_now_node_uuid,
        (
            ('4.383', '7b067edd-f53f-49e1-95bc-0986e6e2ca2f'),
            (None,  'b4155335-5e08-4d85-8ccd-ddebf5507447'),
        ),
        emotions={
            bg3.SPEAKER_SHADOWHEART: ((0.0, 1024, 1), (0.94, 1024, None), (2.86, 1024, 2)),
            bg3.SPEAKER_PLAYER: ((0.0, 1024, 2),)
        }
    )


    ##########################################################################################################
    # Dialog: ShadowHeart_InParty2_Nested_Romance.lsf
    # Set the custom flag that enables replays of the skinny dipping cutscene
    # Flags are set in Shadowheart's answers after the first night at the beach
    ##########################################################################################################

    # d = bg3.dialog_object(files.get_file('Gustav', 'Mods/GustavDev/Story/DialogsBinary/Companions/ShadowHeart_InParty2_Nested_Romance.lsf'))

    ab = game_assets.get_modded_dialog_asset_bundle('ShadowHeart_InParty2_Nested_Romance')
    d = bg3.dialog_object(ab.dialog)

    slot_idx_shadowheart = d.get_speaker_slot_index(bg3.SPEAKER_SHADOWHEART)
    slot_idx_tav = d.get_speaker_slot_index(bg3.SPEAKER_PLAYER)

    make_sand_castles_node_uuid = '08c8b4f5-79df-4b9b-9e11-2e2c0cf06a3d' # existing node
    alias_make_sand_castles_node_uuid = '23793ec5-4624-4beb-a13a-d8ebb276fe6e'

    # But of course they will. I hope we'll have more opportunities to slip away... and make sand castles.
    d.add_dialog_flags(make_sand_castles_node_uuid, setflags = (
        bg3.flag_group('Object', (
            bg3.flag(Shadowheart_More_Sandcastles.uuid, True, slot_idx_shadowheart),
            bg3.flag(Snuck_Away_To_Make_Sandcastles.uuid, True, slot_idx_shadowheart),
            bg3.flag(Shadowheart_LongRest_Before_More_Sandcastles.uuid, False, slot_idx_shadowheart),
        )),
    ))
    d.create_alias_dialog_node(
        alias_make_sand_castles_node_uuid,
        make_sand_castles_node_uuid,
        [],
        end_node = True,
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(Shadowheart_More_Sandcastles.uuid, True, slot_idx_shadowheart),
            )),
        ))
    d.add_child_dialog_node('20e7daab-9901-4496-a44f-8a692af16f2a', alias_make_sand_castles_node_uuid, 0)

    im_glad_we_have_each_other_node_uuid = '277288c2-302f-4e53-9e3d-02974e7ac352' # existing node
    alias_im_glad_we_have_each_other_node_uuid = '31fcc31f-32b3-44c7-8d32-f6a8f56845c4'

    # I suppose it doesn't. I'm glad we have each other. And I hope we'll have more opportunities to slip away.
    d.add_dialog_flags(im_glad_we_have_each_other_node_uuid, setflags = (
        bg3.flag_group('Object', (
            bg3.flag(Shadowheart_More_Sandcastles.uuid, True, slot_idx_shadowheart),
            bg3.flag(Shadowheart_LongRest_Before_More_Sandcastles.uuid, False, slot_idx_shadowheart),
        )),
    ))
    d.create_alias_dialog_node(
        alias_im_glad_we_have_each_other_node_uuid,
        im_glad_we_have_each_other_node_uuid,
        [],
        end_node = True,
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(Shadowheart_More_Sandcastles.uuid, True, slot_idx_shadowheart),
            )),
        ))
    d.add_child_dialog_node('7e9c736b-8fba-4320-9db7-fa733621874d', alias_im_glad_we_have_each_other_node_uuid, 0)

    perhaps_well_see_node_uuid = 'a02476cc-535b-4ffc-8b19-986fb9464842' # existing node
    alias_perhaps_well_see_node_uuid = '0ed5178e-7dfd-40ae-9fb9-95da1b35cb4c'

    # Perhaps. We'll see.
    d.add_dialog_flags(perhaps_well_see_node_uuid, setflags = (
        bg3.flag_group('Object', (
            bg3.flag(Shadowheart_More_Sandcastles.uuid, True, slot_idx_shadowheart),
            bg3.flag(Shadowheart_LongRest_Before_More_Sandcastles.uuid, False, slot_idx_shadowheart),
        )),
    ))
    d.create_alias_dialog_node(
        alias_perhaps_well_see_node_uuid,
        perhaps_well_see_node_uuid,
        [],
        end_node = True,
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(Shadowheart_More_Sandcastles.uuid, True, slot_idx_shadowheart),
            )),
        ))
    d.add_child_dialog_node('b2c22c96-8272-4793-9cb5-9e6eb97ac978', alias_perhaps_well_see_node_uuid, 0)


    # Oh. I'm sorry you feel that way... I don't.
    d.add_dialog_flags('ce072faa-0aa6-404a-aeaa-27fb3d226b5d', setflags = (
        bg3.flag_group('Object', (
            bg3.flag(Shadowheart_Has_Doubts_About_Tav.uuid, True, slot_idx_tav),
        )),
    ))


def patch_skinny_dipping_scene() -> None:

    ##########################################################################################################
    # Dialog: CAMP_Shadowheart_SkinnyDipping_SD_ROM.lsf
    # Removed dialog options that let Tav walk away if this isn't the first time they swim with Shadowheart
    ##########################################################################################################

    # d = bg3.dialog_object(files.get_file('Gustav', 'Mods/GustavDev/Story/DialogsBinary/Camp/SoloDreams/CAMP_Shadowheart_SkinnyDipping_SD_ROM.lsf'))
    # t = bg3.timeline_object(files.get_file('Gustav', 'Public/GustavDev/Timeline/Generated/CAMP_Shadowheart_SkinnyDipping_SD_ROM.lsf'), d)

    ab = game_assets.get_modded_dialog_asset_bundle('CAMP_Shadowheart_SkinnyDipping_SD_ROM')
    d = bg3.dialog_object(ab.dialog)


    slot_idx_shadowheart = d.get_speaker_slot_index(bg3.SPEAKER_SHADOWHEART)
    slot_idx_tav = d.get_speaker_slot_index(bg3.SPEAKER_PLAYER)

    dialog_nodes = [
        # Suppress nodes for the 2nd run of the unsafe cutscene as they don't make sense anymore
        'a36d3365-38ba-8a0a-e249-8491cf394f2c', # What?
        '0403b053-4b6c-9cfb-7b95-007c6024509b', # I never said I was coming in with you.
        '955c8afa-d714-09e6-2541-a409d7919304', # I didn't bring anything to swim in.
        'bbd5a13c-fa69-58c4-e0d8-1b65c3dc908d', # There's easier ways to get me naked, you know.
        'd2205284-8cbe-0cba-be5a-6693eb699a5a', # Forget it. Let's head back.
        'c0230403-b3a9-2203-baff-7102710154c7', # Actually, I've changed my mind. I'm heading back to camp.

        # Suppress nodes for the 2nd run of the safe cutscene as they don't make sense anymore
        'c70dbc9c-5afe-909b-7514-6480a9c2c79c', # What?
        'a00730b5-70c7-13ab-9263-239d28168c29', # I never said I was coming in with you.
        'd53947d8-21fc-df12-a0f0-c43c4d080911', # I didn't bring anything to swim in.
        '5e5a9953-4814-8853-b8ee-833e25b05af8', # Forget it. Let's head back.
    ]
    for dialog_node in dialog_nodes:
        d.set_dialog_flags(
            dialog_node,
            checkflags = (
                bg3.flag_group('Object', (
                    bg3.flag(Shadowheart_More_Sandcastles.uuid, False, slot_idx_shadowheart),
                )),
            ),
        )

    aborted_sd_dialog_nodes = [
        '37f2f70f-2be2-df93-a613-d45b1aa1db31', # Alias to 97859427-f401-6a21-bd0c-e855f36c7d1d
        '45b93976-c611-89c0-9546-41fb7996be5a', # Yes. A silent one, if you have any sense.
        '97859427-f401-6a21-bd0c-e855f36c7d1d'  # Oh. If you insist...
    ]
    for dialog_node in aborted_sd_dialog_nodes:
        d.set_dialog_flags(
            dialog_node,
            setflags = (
                bg3.flag_group('Global', (
                    bg3.flag(bg3.FLAG_ORI_Shadowheart_State_AbortedSkinnydipping, True, None),
                )),
                bg3.flag_group('Object', (
                    bg3.flag(Shadowheart_Has_Doubts_About_Tav.uuid, True, slot_idx_tav),
                )),
            ))


    ###########################################################################
    # Timeline: CAMP_Shadowheart_SkinnyDipping_SD_ROM.lsf
    # Delay camera transform when Tav & Shadowheart are kissing on the beach
    ###########################################################################

    # now_dont_you_dare_stop_node_uuid = '209a6af4-1a79-cbe3-665e-63c03a31db0c'
    # phase = t.use_existing_phase(now_dont_you_dare_stop_node_uuid)

    # transform_t1 = phase.duration - 4.45
    # transform_t2 = phase.duration - 2.25

    # transform_channels = (
    #     (
    #         t.create_value_key(time=transform_t1, interpolation_type=5, value=-0.9371941),
    #         t.create_value_key(time=transform_t2, interpolation_type=5, value=-0.9421899),
    #     ),
    #     (
    #         t.create_value_key(time=transform_t1, interpolation_type=5, value=0.2273747),
    #         t.create_value_key(time=transform_t2, interpolation_type=5, value=0.2277535),
    #     ),
    #     (
    #         t.create_value_key(time=transform_t1, interpolation_type=5, value=-6.752407),
    #         t.create_value_key(time=transform_t2, interpolation_type=5, value=-6.757811),
    #     ),
    #     (
    #         t.create_value_key(time=transform_t1, interpolation_type=5, value=(0.013664621, 0.3343945, -0.00484906, 0.94232166)),
    #         t.create_value_key(time=transform_t2, interpolation_type=5, value=(0.22784422, -0.33852422, -0.084851965, -0.90900415)),
    #     ),
    #     (),
    #     ())

    # t.edit_tl_transform('98020265-3ead-4cc4-9c99-3ff011567e38', channels=transform_channels)

    # t.update_duration()

    ###########################################################################
    # Timeline: CAMP_Shadowheart_SkinnyDipping_SD_ROM.lsf
    # Fix Shadowheart black hair bug: keep her slippers on her feet
    # Fixed in hotfix 28
    ###########################################################################

    # How does this work? Hair color changes to black if she is nude.
    # Wearing camp shoes somehow prevents hair color from turning black.
    # So, all TLShowArmor nodes that control visual state of Shadowheart equipment are patched to keep her slippers on.
    # TLShowArmor's channel 6 (zero-based index) controls camp footwear.
    # The following code sets the 6th channel to True for each TLShowArmor with actor uuid set to Shadowheart.

    # This bug is fixed as of Patch 7 Hotfix 28
    #show_armor_components = t.find_effect_components(effect_component_type=bg3.timeline_object.SHOW_ARMOR, actor=bg3.SPEAKER_SHADOWHEART)
    #for effect_component in show_armor_components:
    #    channels = effect_component.find("./children/node[@id='Channels']/children")
    #    if channels is not None and hasattr(channels, '__len__') and len(channels) == 11:
    #        key = channels[6].find("./children/node[@id='Keys']/children/node[@id='Key']/attribute[@id='Value']")
    #        if key is not None:
    #            key.set('value', 'True')


###############################################################################
# All right. Just stay close...
# original start time: 70.60
# duration:            8.64
# end time:            79.24
###############################################################################

def create_just_stay_close_timeline(d: bg3.dialog_object, t: bg3.timeline_object) -> None:
    #phase_duration = 31.34
    phase_duration = '31.64'
    t.create_new_phase(just_stay_close_node_uuid, phase_duration)

    camera1 = '0f34b216-08ed-4dd8-acd4-7cdb783f80ed'
    camera2 = '76e352cd-bd60-40e6-afb9-2dd21e1c0512'
    #camera2 = '6ab16d55-663c-4005-a4e8-283e8266cd02'

    t.create_tl_actor_node(bg3.timeline_object.SHOW_VISUAL, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        t.create_value_key(time = '0.0', interpolation_type = 3, value_name = 'ShowVisual', value = True),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.SHOW_VISUAL, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_value_key(time = '0.0', interpolation_type = 3, value_name = 'ShowVisual', value = True),
    ), is_snapped_to_end = True)
    t.create_tl_non_actor_node(bg3.timeline_object.SWITCH_STAGE, '0.0', phase_duration, (
        t.create_switch_stage_event_key('0.0', event_uuid = 'dffc3db7-d7bb-4965-8569-ef8edbe30b1e', force_transform_update = True),
    ))
    t.create_tl_non_actor_node(bg3.timeline_object.SWITCH_LOCATION, '0.0', phase_duration, ())
    t.create_tl_actor_node(bg3.timeline_object.EMOTION, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_emotion_key('0.2', 32),
        t.create_emotion_key('2.92', 32, variation = 2)
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(
        bg3.timeline_object.LOOK_AT,
        bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration,
        (
            t.create_look_at_key(
                1.35,
                bone = 'Head_M',
                turn_mode = 3,
                turn_speed_multiplier = 0.3,
                head_turn_speed_multiplier = 0.3,
                weight = 0,
                offset = (1.821, 0.869, 6.708),
                is_eye_look_at_enabled = True,
                eye_look_at_target_id = bg3.SPEAKER_PLAYER,
                eye_look_at_bone = 'Head_M'),
            t.create_look_at_key(
                3.26,
                bone = 'Head_M',
                turn_mode = 3,
                turn_speed_multiplier = 0.3,
                head_turn_speed_multiplier = 0.1,
                weight = 0,
                offset = (1.475, 0.869, 7.221),
                is_eye_look_at_enabled = True,
                eye_look_at_bone = 'Head_M',
                eye_look_at_offset = (0.139, 0.427, 8.181)),
            t.create_look_at_key(
                4.32,
                bone = 'Head_M',
                turn_mode = 3,
                turn_speed_multiplier = 0.3,
                head_turn_speed_multiplier = 0.3,
                weight = 0,
                safe_zone_angle = 80.0,
                head_safe_zone_angle = 80.0,
                offset = (-1.236, 0.0, 9.588),
                look_at_mode = 1,
                eye_look_at_bone = 'Head_M')
        ),
        is_snapped_to_end = True)
    t.create_tl_actor_node(
        bg3.timeline_object.LOOK_AT,
        bg3.SPEAKER_PLAYER, '0.0', phase_duration,
        (
            t.create_look_at_key(
                0.0,
                target = bg3.SPEAKER_SHADOWHEART,
                bone = 'Head_M',
                turn_mode = 3,
                turn_speed_multiplier = 0.3,
                head_turn_speed_multiplier = 0.1,
                weight = 0.0,
                offset = (-0.387, 0.0, 0.349),
                is_eye_look_at_enabled = True,
                eye_look_at_target_id = bg3.SPEAKER_SHADOWHEART,
                eye_look_at_bone = 'Head_M'),
        ),
        is_snapped_to_end = True)
    t.create_tl_show_armor(bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
        (),
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
        (),
        (),
        (),
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
    ), is_snapped_to_end = True)
    t.create_tl_show_armor(bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
        (),
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
        (),
        (),
        (),
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
    ), is_snapped_to_end = True)
    t.create_tl_voice(
        bg3.SPEAKER_SHADOWHEART, '0.0', '5.86',
        just_stay_close_node_uuid,
        performance_fade = 2.0,
        fade_in = 2.0,
        fade_out = 0.0,
        performance_drift_type = 2)
    t.create_tl_shot(camera1, '0.0', '4.32')

    t.create_tl_transform('2773773e-4ffd-44ae-92f0-5854bf0d6a62', '0.0', phase_duration, (
        (
            t.create_value_key(time = phase_duration, interpolation_type = 0, value = 7.852595),
        ),
        (
            t.create_value_key(time = phase_duration, interpolation_type = 0, value = -0.3154944),
        ),
        (
            t.create_value_key(time = phase_duration, interpolation_type = 0, value = 11.40912),
        ),
        (
            t.create_value_key(time = phase_duration, interpolation_type = 0, value = bg3.euler_to_quaternion(-178.68031, -4.61708, -0.02341, sequence = 'yxz')),
        ),
        (),
        ()
    ))
    t.create_tl_transform('c03290fc-a9d1-4b31-a318-8309540d53ba', '0.0', phase_duration, ())

    t.create_tl_camera_dof(
        camera2, '0.0', phase_duration,
        (
            (
                t.create_value_key(time = 9.53, interpolation_type = 0, value = 10.0),
            ),
            (
                t.create_value_key(time = 9.53, interpolation_type = 0, value = 20.0),
            ),
            (
                t.create_value_key(time = 9.53, interpolation_type = 0, value = 1.0),
            ),
            (
                t.create_value_key(time = 9.53, interpolation_type = 0, value = 1.0),
            ),
            (
                t.create_value_key(time = 9.53, interpolation_type = 0),
            ),
            (
                t.create_value_key(time = 9.53, interpolation_type = 0),
            ),
            (
                t.create_value_key(time = 9.53, interpolation_type = 0),
            ),
        ))

    t.create_tl_animation(
        bg3.SPEAKER_SHADOWHEART, '4.32', phase_duration,
        'e8e40c74-f89a-c00f-763e-ec95152aec53',
        'c117d3bf-4e9c-4255-84bd-9928b424f45c',
        fade_in = 0.0,
        fade_out = 0.0,
        offset_type = 2,
        enable_root_motion = True,
        target_transform = t.create_animation_target_transform(
            1.0, (2.618318, -0.7280912, 6.70607), bg3.euler_to_quaternion(103.63883, -1.85705, 2.27379, sequence='yxz')
        ))
    t.create_tl_animation(
        bg3.SPEAKER_PLAYER, '4.32', phase_duration,
        '6b48d6cd-8daa-43a8-bcf9-6b056eb96862',
        '668c02f3-f56c-40b1-bc43-37ecd964b6e5',
        fade_in = 0.0,
        fade_out = 0.0,
        offset_type = 2,
        enable_root_motion = True,
        target_transform = t.create_animation_target_transform(
            #1.0, (1.95, -0.75, 6.4), bg3.euler_to_quaternion(-177.9591, 0.0, 0.0, sequence='yxz')
            1.0, (2.1, -0.8, 6.25), bg3.euler_to_quaternion(-177.9591, 0.0, 0.0, sequence='yxz')
        ))

    #t.create_tl_transform(camera2, 4.32, 21.34, (
    t.create_tl_transform(camera2, '4.32', phase_duration, (
        (
            #t.create_value_key(time = 10.52, interpolation_type = 5, value = -0.4804078),
            t.create_value_key(time = 10.52, interpolation_type = 5, value = -1.0),
        ),
        (
            t.create_value_key(time = 10.52, interpolation_type = 5, value = -0.3),
        ),
        (
            t.create_value_key(time = 10.52, interpolation_type = 5, value = 1.75),
            t.create_value_key(time = 21.34, interpolation_type = 5, value = 0.75),
        ),
        (
            # t.create_value_key(time = 10.52, interpolation_type = 5, value = bg3.euler_to_quaternion(160.57563, 2.88036, -0.02204, sequence = 'yxz')),
            # t.create_value_key(time = 21.34, interpolation_type = 5, value = bg3.euler_to_quaternion(156.56495, 9.0, -0.02144, sequence = 'yxz')),
            t.create_value_key(time = 10.52, interpolation_type = 5, value = bg3.euler_to_quaternion(155, 2.88036, -0.02204, sequence = 'yxz')),
            t.create_value_key(time = 21.34, interpolation_type = 5, value = bg3.euler_to_quaternion(149, 9.0, -0.02144, sequence = 'yxz')),
        ),
        (),
        (
            t.create_frame_of_reference_key(4.32, 5, bg3.SPEAKER_PLAYER, 'Socket_DIAG_Camera', True, True),
        )
    ))
    t.create_tl_shot(camera2, '4.32', phase_duration)

    #t.create_tl_shot(camera2, 4.32, 21.34)
    # t.create_tl_transform(camera2, 21.34, phase_duration, (
    #     (
    #         t.create_value_key(time = 21.34, interpolation_type = 5, value = 3.5),
    #     ),
    #     (
    #         t.create_value_key(time = 21.34, interpolation_type = 5, value = -0.4),
    #     ),
    #     (
    #         t.create_value_key(time = 21.34, interpolation_type = 5, value = -6.5),
    #         t.create_value_key(time = phase_duration, interpolation_type = 5, value = -8.0),
    #     ),
    #     (
    #         t.create_value_key(time = 21.34, interpolation_type = 5, value = bg3.euler_to_quaternion(-36.0, 6.0, -0.02144, sequence = 'yxz')),
    #     ),
    #     (),
    #     (
    #         t.create_frame_of_reference_key(21.34, 5, bg3.SPEAKER_PLAYER, 'Socket_DIAG_Camera', True, True),
    #     )
    # ))
    # t.create_tl_shot(camera2, 21.34, phase_duration, is_snapped_to_end = True)


###############################################################################
# Wait - just give me a moment. I can manage. As long as you stay with me.
# original start time: 188.56
# duration:            
# end time:            204.8
###############################################################################

def create_i_can_manage_timeline(d: bg3.dialog_object, t: bg3.timeline_object) -> None:
    #phase_duration = 36.62
    phase_duration = '36.92'
    t.create_new_phase(i_can_manage_node_uuid, phase_duration)

    camera1 = '0f34b216-08ed-4dd8-acd4-7cdb783f80ed'
    camera2 = '76e352cd-bd60-40e6-afb9-2dd21e1c0512'

    t.create_tl_actor_node(bg3.timeline_object.SHOW_VISUAL, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        t.create_value_key(time = 0.0, interpolation_type = 3, value_name = 'ShowVisual', value = True),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.SHOW_VISUAL, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_value_key(time = 0.0, interpolation_type = 3, value_name = 'ShowVisual', value = True),
    ), is_snapped_to_end = True)
    t.create_tl_non_actor_node(bg3.timeline_object.SWITCH_STAGE, '0.0', phase_duration, (
        t.create_switch_stage_event_key(0.0, event_uuid = 'dffc3db7-d7bb-4965-8569-ef8edbe30b1e', force_transform_update = True),
    ))
    t.create_tl_non_actor_node(bg3.timeline_object.SWITCH_LOCATION, '0.0', phase_duration, ())
    t.create_tl_actor_node(bg3.timeline_object.EMOTION, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_emotion_key(0.0, 32),
        t.create_emotion_key(2.2, 16),
        t.create_emotion_key(4.0, 32),
        t.create_emotion_key(5.57, 64),
        t.create_emotion_key(7.66, 64, variation = 2)
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(
        bg3.timeline_object.LOOK_AT,
        bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration,
        (
            t.create_look_at_key(
                0.81,
                bone = 'Head_M',
                turn_mode = 3,
                turn_speed_multiplier = 0.3,
                head_turn_speed_multiplier = 0.3,
                weight = 0,
                offset = (1.821, 0.869, 6.708),
                is_eye_look_at_enabled = True,
                eye_look_at_target_id = bg3.SPEAKER_PLAYER,
                eye_look_at_bone = 'Head_M'),
            t.create_look_at_key(
                4.61,
                bone = 'Head_M',
                turn_mode = 3,
                turn_speed_multiplier = 0.3,
                head_turn_speed_multiplier = 0.1,
                weight = 0,
                offset = (1.475, 0.869, 7.221),
                is_eye_look_at_enabled = True,
                eye_look_at_bone = 'Head_M',
                eye_look_at_offset = (0.139, 0.427, 8.181)),
            t.create_look_at_key(
                6.99,
                bone = 'Head_M',
                turn_mode = 3,
                turn_speed_multiplier = 0.3,
                head_turn_speed_multiplier = 0.3,
                weight = 0,
                offset = (1.821, 0.869, 6.708),
                is_eye_look_at_enabled = True,
                eye_look_at_target_id = bg3.SPEAKER_PLAYER,
                eye_look_at_bone = 'Head_M'),
            t.create_look_at_key(
                11.06,
                bone = 'Head_M',
                turn_mode = 3,
                turn_speed_multiplier = 0.3,
                head_turn_speed_multiplier = 0.1,
                weight = 0,
                offset = (1.821, 0.869, 6.708),
                look_at_mode = 0,
                is_eye_look_at_enabled = True),
        ),
        is_snapped_to_end = True)
    t.create_tl_actor_node(
        bg3.timeline_object.LOOK_AT,
        bg3.SPEAKER_PLAYER, '0.0', phase_duration,
        (
            t.create_look_at_key(
                9.6,
                target = bg3.SPEAKER_SHADOWHEART,
                bone = 'Head_M',
                turn_mode = 3,
                turn_speed_multiplier = 0.3,
                head_turn_speed_multiplier = 0.1,
                weight = 0.0,
                offset = (-0.387, 0.0, 0.349),
                is_eye_look_at_enabled = True,
                eye_look_at_target_id = bg3.SPEAKER_SHADOWHEART,
                eye_look_at_bone = 'Head_M'),
        ),
        is_snapped_to_end = True)
    t.create_tl_show_armor(bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
        (),
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
        (),
        (),
        (),
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
    ), is_snapped_to_end = True)
    t.create_tl_show_armor(bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
        (),
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
        (),
        (),
        (),
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
    ), is_snapped_to_end = True)
    t.create_tl_voice(
        bg3.SPEAKER_SHADOWHEART, '1.44', '9.6',
        i_can_manage_node_uuid,
        performance_fade = 2.0,
        fade_in = 2.0,
        fade_out = 0.0,
        performance_drift_type = 2)
    t.create_tl_shot(camera1, '0.0', '9.6')

    t.create_tl_transform('2773773e-4ffd-44ae-92f0-5854bf0d6a62', '0.0', phase_duration, (
        (
            t.create_value_key(time = phase_duration, interpolation_type = 0, value = 7.852595),
        ),
        (
            t.create_value_key(time = phase_duration, interpolation_type = 0, value = -0.3154944),
        ),
        (
            t.create_value_key(time = phase_duration, interpolation_type = 0, value = 11.40912),
        ),
        (
            t.create_value_key(time = phase_duration, interpolation_type = 0, value = bg3.euler_to_quaternion(-178.68031, -4.61708, -0.02341, sequence = 'yxz')),
        ),
        (),
        ()
    ))
    t.create_tl_transform('c03290fc-a9d1-4b31-a318-8309540d53ba', '0.0', phase_duration, ())

    t.create_tl_camera_dof(
        camera2, '0.0', phase_duration,
        (
            (
                t.create_value_key(time = 10.47, interpolation_type = 0, value = 10.0),
            ),
            (
                t.create_value_key(time = 10.47, interpolation_type = 0, value = 20.0),
            ),
            (
                t.create_value_key(time = 10.47, interpolation_type = 0, value = 1.0),
            ),
            (
                t.create_value_key(time = 10.47, interpolation_type = 0, value = 1.0),
            ),
            (
                t.create_value_key(time = 10.47, interpolation_type = 0),
            ),
            (
                t.create_value_key(time = 10.47, interpolation_type = 0),
            ),
            (
                t.create_value_key(time = 10.47, interpolation_type = 0),
            ),
        ))

    t.create_tl_animation(
        bg3.SPEAKER_SHADOWHEART, '9.6', phase_duration,
        'e8e40c74-f89a-c00f-763e-ec95152aec53',
        'c117d3bf-4e9c-4255-84bd-9928b424f45c',
        fade_in = 0.0,
        fade_out = 0.0,
        offset_type = 2,
        enable_root_motion = True,
        target_transform = t.create_animation_target_transform(
            1.0, (2.618318, -0.7280912, 6.70607), bg3.euler_to_quaternion(103.63883, -1.85705, 2.27379, sequence='yxz')
        ))
    t.create_tl_animation(
        bg3.SPEAKER_PLAYER, '9.6', phase_duration,
        '6b48d6cd-8daa-43a8-bcf9-6b056eb96862',
        '668c02f3-f56c-40b1-bc43-37ecd964b6e5',
        fade_in = 0.0,
        fade_out = 0.0,
        offset_type = 2,
        enable_root_motion = True,
        target_transform = t.create_animation_target_transform(
            1.0, (2.1, -0.8, 6.25), bg3.euler_to_quaternion(-177.9591, 0.0, 0.0, sequence='yxz')
        ))

    t.create_tl_transform(camera2, '9.6', phase_duration, (
        (
            t.create_value_key(time = 10.52, interpolation_type = 5, value = -1.0),
        ),
        (
            t.create_value_key(time = 15.8, interpolation_type = 5, value = -0.3),
        ),
        (
            t.create_value_key(time = 15.8, interpolation_type = 5, value = 1.75),
            t.create_value_key(time = 26.62, interpolation_type = 5, value = 0.75),
        ),
        (
            t.create_value_key(time = 15.8, interpolation_type = 5, value = bg3.euler_to_quaternion(155, 2.88036, -0.02204, sequence = 'yxz')),
            t.create_value_key(time = 26.62, interpolation_type = 5, value = bg3.euler_to_quaternion(149, 9.0, -0.02144, sequence = 'yxz')),        
        ),
        (),
        (
            t.create_frame_of_reference_key(9.6, 5, bg3.SPEAKER_PLAYER, 'Socket_DIAG_Camera', True, True),
        )
    ))
    t.create_tl_shot(camera2, '9.6', phase_duration, is_snapped_to_end = True)

    # t.create_tl_shot(camera2, 9.6, 26.62)
    # t.create_tl_transform(camera2, 26.62, phase_duration, (
    #     (
    #         t.create_value_key(time = 26.62, interpolation_type = 5, value = 3.5),
    #     ),
    #     (
    #         t.create_value_key(time = 26.62, interpolation_type = 5, value = -0.4),
    #     ),
    #     (
    #         t.create_value_key(time = 26.62, interpolation_type = 5, value = -6.5),
    #         t.create_value_key(time = phase_duration, interpolation_type = 5, value = -8.0),
    #     ),
    #     (
    #         t.create_value_key(time = 26.62, interpolation_type = 5, value = bg3.euler_to_quaternion(-36.0, 6.0, -0.02144, sequence = 'yxz')),
    #     ),
    #     (),
    #     (
    #         t.create_frame_of_reference_key(26.62, 5, bg3.SPEAKER_PLAYER, 'Socket_DIAG_Camera', True, True),
    #     )
    # ))
    # t.create_tl_shot(camera2, 26.62, phase_duration, is_snapped_to_end = True)


###############################################################################
# More the drowning, and the things that could be hiding underwater, and the drowning, and the cold. Did I mention the drowning?
# Let's get on with it, before I lose my nerve.
# original start time: 480.71
# duration:            
# end time:            501.6938
###############################################################################

def create_more_the_drowning_timeline(d: bg3.dialog_object, t: bg3.timeline_object) -> None:
    phase_duration = '40.74'
    t.create_new_phase(more_the_drowning_node_uuid, phase_duration)

    camera1 = '0f34b216-08ed-4dd8-acd4-7cdb783f80ed'
    camera2 = '6ab16d55-663c-4005-a4e8-283e8266cd02'
    camera3 = '8fe7fd24-d40e-451c-9537-0b3fffb4f71c'
    camera4 = '76e352cd-bd60-40e6-afb9-2dd21e1c0512'

    t.create_tl_actor_node(bg3.timeline_object.SHOW_VISUAL, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        t.create_value_key(time = 0.0, interpolation_type = 3, value_name = 'ShowVisual', value = True),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.SHOW_VISUAL, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_value_key(time = 0.0, interpolation_type = 3, value_name = 'ShowVisual', value = True),
    ), is_snapped_to_end = True)
    t.create_tl_non_actor_node(bg3.timeline_object.SWITCH_STAGE, '0.0', phase_duration, (
        t.create_switch_stage_event_key(0.0, event_uuid = 'dffc3db7-d7bb-4965-8569-ef8edbe30b1e', force_transform_update = True),
    ))
    t.create_tl_non_actor_node(bg3.timeline_object.SWITCH_LOCATION, '0.0', phase_duration, ())
    t.create_tl_actor_node(bg3.timeline_object.EMOTION, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        t.create_emotion_key(8.34, 2),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.EMOTION, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_emotion_key(0.0, 64),
        t.create_emotion_key(0.81, 32, variation = 1),
        t.create_emotion_key(2.03, 64, variation = 2),
        t.create_emotion_key(4.21, 4),
        t.create_emotion_key(5.16, 2048, variation = 1),
        t.create_emotion_key(5.81, 64),
        t.create_emotion_key(10.66, 64, variation = 2),
        t.create_emotion_key(12.08, 32)
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(
        bg3.timeline_object.LOOK_AT,
        bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration,
        (
            t.create_look_at_key(
                0.88,
                bone = 'Head_M',
                turn_mode = 3,
                turn_speed_multiplier = 0.3,
                head_turn_speed_multiplier = 0.1,
                weight = 0.0,
                offset = (1.441, 1.081, 6.832),
                is_eye_look_at_enabled = True,
                eye_look_at_target_id = bg3.SPEAKER_PLAYER,
                eye_look_at_bone = 'Head_M'),
            t.create_look_at_key(
                6.23,
                bone = 'Head_M',
                turn_mode = 3,
                turn_speed_multiplier = 0.3,
                head_turn_speed_multiplier = 0.1,
                weight = 0.0,
                offset = (1.033, 0.869, 8.985),
                eye_look_at_bone = 'Head_M',
                eye_look_at_offset = (0.139, 0.427, 8.181)),
            t.create_look_at_key(
                9.0,
                bone = 'Head_M',
                turn_mode = 3,
                turn_speed_multiplier = 0.3,
                head_turn_speed_multiplier = 0.1,
                weight = 0.0,
                offset = (1.441, 1.081, 6.832),
                is_eye_look_at_enabled = True,
                eye_look_at_target_id = bg3.SPEAKER_PLAYER,
                eye_look_at_bone = 'Head_M'),
            t.create_look_at_key(
                12.93,
                bone = 'Head_M',
                turn_mode = 3,
                turn_speed_multiplier = 0.3,
                head_turn_speed_multiplier = 0.1,
                weight = 0.0,
                offset = (1.033, 0.869, 8.985),
                eye_look_at_bone = 'Head_M',
                eye_look_at_offset = (0.139, 0.427, 8.181)),
            t.create_look_at_key(
                17.24,
                turn_mode = 3,
                turn_speed_multiplier = 0.3,
                head_turn_speed_multiplier = 0.1,
                weight = 0.0,
                offset = (1.441, 1.081, 6.832),
                look_at_mode = 0,
                is_eye_look_at_enabled = True)
        ))
    t.create_tl_actor_node(
        bg3.timeline_object.LOOK_AT,
        bg3.SPEAKER_PLAYER, '0.0', phase_duration,
        (
            t.create_look_at_key(
                5.49,
                target = bg3.SPEAKER_SHADOWHEART,
                bone = 'Head_M',
                turn_mode = 3,
                turn_speed_multiplier = 0.3,
                head_turn_speed_multiplier = 0.1,
                weight = 0.0,
                offset = (-0.784, 0.0, 0.349),
                is_eye_look_at_enabled = True,
                eye_look_at_target_id = bg3.SPEAKER_SHADOWHEART,
                eye_look_at_bone = 'Head_M'),
        ))
    t.create_tl_show_armor(bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
        (),
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
        (),
        (),
        (),
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
    ), is_snapped_to_end = True)
    t.create_tl_show_armor(bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
        (),
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
        (),
        (),
        (),
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
    ), is_snapped_to_end = True)

    t.create_tl_camera_dof(
        camera4, '0.0', phase_duration,
        (
            (
                t.create_value_key(time = 0.0, interpolation_type = 0, value = 10.0),
            ),
            (
                t.create_value_key(time = 0.0, interpolation_type = 0, value = 20.0),
            ),
            (
                t.create_value_key(time = 0.0, interpolation_type = 0, value = 1.0),
            ),
            (
                t.create_value_key(time = 0.0, interpolation_type = 0, value = 1.0),
            ),
            (
                t.create_value_key(time = 0.0, interpolation_type = 0),
            ),
            (
                t.create_value_key(time = 0.0, interpolation_type = 0),
            ),
            (
                t.create_value_key(time = 0.0, interpolation_type = 0),
            ),
        ))

    t.create_tl_shot(camera1, '0.0', '7.99')
    t.create_tl_voice(
        bg3.SPEAKER_SHADOWHEART, '0.0', '8.45',
        more_the_drowning_node_uuid,
        performance_fade = 2.0,
        fade_in = 2.0,
        fade_out = 0.0)

    t.create_tl_animation(
        bg3.SPEAKER_PLAYER, '7.99', '13.72',
        '6b48d6cd-8daa-43a8-bcf9-6b056eb96862',
        '668c02f3-f56c-40b1-bc43-37ecd964b6e5',
        animation_play_start_offset = 4.08,
        fade_in = 0.0,
        fade_out = 0.0,
        enable_root_motion = True)
    t.create_tl_shot(camera2, '7.99', '10.18')

    t.create_tl_voice(
        bg3.SPEAKER_SHADOWHEART, '10.18', '13.72',
        before_i_lose_my_nerve_node_uuid,
        performance_fade = 2.0,
        fade_in = 2.0,
        fade_out = 0.0)
    t.create_tl_shot(camera3, '10.18', '13.72')

    t.create_tl_animation(
        bg3.SPEAKER_SHADOWHEART, '13.72', phase_duration,
        'e8e40c74-f89a-c00f-763e-ec95152aec53',
        'c117d3bf-4e9c-4255-84bd-9928b424f45c',
        fade_in = 0.0,
        fade_out = 0.0,
        offset_type = 2,
        enable_root_motion = True,
        target_transform = t.create_animation_target_transform(
            1.0, (2.618318, -0.7280912, 6.70607), bg3.euler_to_quaternion(103.63883, -1.85705, 2.27379, sequence='yxz')
        ))
    t.create_tl_animation(
        bg3.SPEAKER_PLAYER, '13.72', phase_duration,
        '6b48d6cd-8daa-43a8-bcf9-6b056eb96862',
        '668c02f3-f56c-40b1-bc43-37ecd964b6e5',
        fade_in = 0.0,
        fade_out = 0.0,
        offset_type = 2,
        enable_root_motion = True,
        target_transform = t.create_animation_target_transform(
            #1.0, (2.05, -0.75, 6.4), bg3.euler_to_quaternion(-177.9591, 0.0, 0.0, sequence='yxz')
            1.0, (2.1, -0.75, 6.25), bg3.euler_to_quaternion(-177.9591, 0.0, 0.0, sequence='yxz')
        ))

    camera4_u_turn_time = '28.5'
    t.create_tl_transform(camera4, '13.72', camera4_u_turn_time, (
        (
            t.create_value_key(time = 19.92, interpolation_type = 5, value = -0.4804078),
        ),
        (
            t.create_value_key(time = 19.92, interpolation_type = 5, value = -0.3),
        ),
        (
            t.create_value_key(time = 19.92, interpolation_type = 5, value = 1.5),
            t.create_value_key(time = camera4_u_turn_time, interpolation_type = 5, value = -0.25),
        ),
        (
            t.create_value_key(time = 19.92, interpolation_type = 5, value = bg3.euler_to_quaternion(160.57563, 2.88036, -0.02204, sequence = 'yxz')),
            t.create_value_key(time = camera4_u_turn_time, interpolation_type = 5, value = bg3.euler_to_quaternion(156.56495, 2.87884, -0.02144, sequence = 'yxz')),
        ),
        (),
        (
            t.create_frame_of_reference_key(13.72, 5, bg3.SPEAKER_PLAYER, 'Socket_DIAG_Camera', True, True),
        )
    ))
    t.create_tl_shot(camera4, '13.72', camera4_u_turn_time)

    t.create_tl_transform(camera4, camera4_u_turn_time, phase_duration, (
        (
            t.create_value_key(time = camera4_u_turn_time, interpolation_type = 5, value = 3.5),
        ),
        (
            t.create_value_key(time = camera4_u_turn_time, interpolation_type = 5, value = -0.4),
        ),
        (
            t.create_value_key(time = camera4_u_turn_time, interpolation_type = 5, value = -6.5),
            t.create_value_key(time = phase_duration, interpolation_type = 5, value = -8.0),
        ),
        (
            t.create_value_key(time = camera4_u_turn_time, interpolation_type = 5, value = bg3.euler_to_quaternion(-36.0, 6.0, -0.02144, sequence = 'yxz')),
        ),
        (),
        (
            t.create_frame_of_reference_key(camera4_u_turn_time, 5, bg3.SPEAKER_PLAYER, 'Socket_DIAG_Camera', True, True),
        )
    ))
    t.create_tl_shot(camera4, camera4_u_turn_time, phase_duration, is_snapped_to_end = True)


###############################################################################
# More the drowning, and the things that could be hiding underwater, and the drowning, and the cold. Did I mention the drowning?
# Let's get on with it, before I lose my nerve.
# original start time: 414.82
# duration:              6.87
# end time:            421.69
###############################################################################

def create_what_wait_timeline(d: bg3.dialog_object, t: bg3.timeline_object) -> None:
    phase_duration = '6.87'
    t.create_new_phase(what_wait_node_uuid, phase_duration)

    camera1 = '87366234-4354-4641-a782-4118a64c05e3'
    camera2 = '8d4b8136-f375-461c-a4d3-af20b94240e1'

    t.create_tl_actor_node(bg3.timeline_object.SHOW_VISUAL, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        t.create_value_key(time = 0.0, interpolation_type = 3, value_name = 'ShowVisual', value = True),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.SHOW_VISUAL, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_value_key(time = 0.0, interpolation_type = 3, value_name = 'ShowVisual', value = True),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.EMOTION, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_emotion_key(3.75, 64),
        t.create_emotion_key(4.13, 2),
        t.create_emotion_key(4.96, 2, variation = 1),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.EMOTION, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        t.create_emotion_key(0.46, 4),
        t.create_emotion_key(1.52, 2),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(
        bg3.timeline_object.LOOK_AT,
        bg3.SPEAKER_PLAYER, '0.0', phase_duration,
        (
            t.create_look_at_key(
                0.0,
                turn_mode = 3,
                turn_speed_multiplier = 0.3,
                head_turn_speed_multiplier = 0.3,
                weight = 0.0,
                look_at_mode = 0),
            t.create_look_at_key(
                0.4,
                target = bg3.SPEAKER_SHADOWHEART,
                bone = 'Head_M',
                turn_mode = 3,
                turn_speed_multiplier = 0.3,
                head_turn_speed_multiplier = 0.3,
                weight = 0.0,
                look_at_mode = 1,
                safe_zone_angle = 80.0,
                head_safe_zone_angle = 80.0,
                eye_look_at_bone = 'Head_M'),
            t.create_look_at_key(
                0.96,
                target = bg3.SPEAKER_SHADOWHEART,
                bone = 'Head_M',
                turn_mode = 3,
                turn_speed_multiplier = 0.3,
                head_turn_speed_multiplier = 0.3,
                weight = 0.0,
                safe_zone_angle = 80.0,
                head_safe_zone_angle = 80.0,
                offset = (-3.491, 0.0, 4.395),
                look_at_mode = 1,
                eye_look_at_bone = 'Head_M'),
            t.create_look_at_key(
                1.81,
                target = bg3.SPEAKER_SHADOWHEART,
                bone = 'Head_M',
                turn_mode = 3,
                turn_speed_multiplier = 0.3,
                head_turn_speed_multiplier = 0.3,
                weight = 0.0,
                safe_zone_angle = 80.0,
                head_safe_zone_angle = 80.0,
                offset = (-0.459, 0.0, 0.548),
                look_at_mode = 1,
                eye_look_at_bone = 'Head_M'),
            t.create_look_at_key(
                2.58,
                target = bg3.SPEAKER_SHADOWHEART,
                bone = 'Head_M',
                turn_mode = 3,
                turn_speed_multiplier = 0.3,
                head_turn_speed_multiplier = 0.3,
                weight = 0.0,
                safe_zone_angle = 80.0,
                head_safe_zone_angle = 80.0,
                offset = (-3.491, 0.0, 4.395),
                look_at_mode = 1,
                eye_look_at_bone = 'Head_M')
        ), is_snapped_to_end = True)
    t.create_tl_actor_node(
        bg3.timeline_object.LOOK_AT,
        bg3.SPEAKER_PLAYER, '0.0', phase_duration,
        (
            t.create_look_at_key(
                0.0,
                target = bg3.SPEAKER_PLAYER,
                bone = 'Head_M',
                turn_mode = 3,
                tracking_mode = 1,
                turn_speed_multiplier = 0.3,
                head_turn_speed_multiplier = 0.3,
                weight = 0.0,
                safe_zone_angle = 10.0,
                head_safe_zone_angle = 80.0,
                eye_look_at_bone = 'Head_M'),
        ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.SOUND, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        t.create_sound_event_key(2.69, sound_event_id = '10425fc2-f4d3-4ebc-8c60-356d4770750f') 
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.SOUND, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_sound_event_key(6.28352, sound_event_id = 'c0846db8-80be-4a01-926f-bc59cfd18866') 
    ), is_snapped_to_end = True)
    t.create_tl_non_actor_node(bg3.timeline_object.SWITCH_STAGE, '0.0', phase_duration, (
        t.create_switch_stage_event_key(0.0, event_uuid = 'dffc3db7-d7bb-4965-8569-ef8edbe30b1e', force_transform_update = True),
    ))
    t.create_tl_show_armor(bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
        (),
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
        (),
        (),
        (),
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
    ), is_snapped_to_end = True)
    t.create_tl_show_armor(bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
        (),
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
        (),
        (),
        (),
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
    ), is_snapped_to_end = True)
    t.create_tl_animation(
        bg3.SPEAKER_PLAYER, '0.0', '3.08',
        '69c24f7e-87da-e91d-6a31-cc51e2eea400',
        '668c02f3-f56c-40b1-bc43-37ecd964b6e5',
        animation_play_start_offset = 1.9667,
        fade_in = 0.0,
        fade_out = 0.0,
        offset_type = 2,
        enable_root_motion = True,
        continuous = True,
        target_transform = t.create_animation_target_transform(
            1.0, (1.867714, -0.780274, 6.250424), bg3.euler_to_quaternion(-168.2933, 0.0, 0.0,sequence = 'yxz')
        ))
    t.create_tl_animation(
        bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration,
        'ca67ef6a-869e-eb30-ab5f-7b92c50e47b9',
        'c117d3bf-4e9c-4255-84bd-9928b424f45c',
        animation_play_start_offset = 1.3333,
        fade_in = 0.0,
        fade_out = 0.0,
        offset_type = 2,
        enable_root_motion = True,
        continuous = True,
        is_snapped_to_end = True,
        target_transform = t.create_animation_target_transform(
            1.0, (2.5994427, -0.7280329, 6.85754), bg3.euler_to_quaternion(127.0942, 0.0, 0.0,sequence = 'yxz')
        ))

    t.create_tl_transform(camera1, '0.0', phase_duration, (
        (
            t.create_value_key(time = 0.0, interpolation_type = 3, value = 0.2230746),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 3, value = -0.2647269),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 3, value = -1.739825),
        ),
        (),
        (),
        (
            t.create_frame_of_reference_key(0.0, 0, bg3.SPEAKER_PLAYER, 'Socket_DIAG_Camera', True, True),
        ),
    ), is_snapped_to_end = True)
    t.create_tl_camera_dof(camera1, '0.0', phase_duration, (
        (
            t.create_value_key(time = 0.0, interpolation_type = 0, value = 1.45),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 0, value = 40.0),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 0, value = 1.0),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 0, value = 1.0),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 0),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 0),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 0),
        ),
    ))
    t.create_tl_camera_fov(camera1, '0.0', phase_duration, (
        t.create_value_key(time = 0.0, interpolation_type = 0, value_name = 'FoV', value = 24.0),
    ), is_snapped_to_end = True)

    t.create_tl_camera_look_at(camera1, '0.0', phase_duration, (
        t.create_tl_camera_look_at_key(0.0, bg3.SPEAKER_PLAYER, 'Head_M', (0.47, 0.35), damping_strength = 15.0)
    ), is_snapped_to_end = True)
    t.create_tl_shot(camera1, '0.0', '3.08')

    t.create_tl_transform(camera2, '0.0', phase_duration, (
        (
            t.create_value_key(time = 3.08, interpolation_type = 0, value = 1.183096),
            t.create_value_key(time = phase_duration, interpolation_type = 5, value = 1.263667),
        ),
        (
            t.create_value_key(time = 3.08, interpolation_type = 0, value = 0.6930529),
            t.create_value_key(time = phase_duration, interpolation_type = 5, value = 0.6893288),
        ),
        (
            t.create_value_key(time = 3.08, interpolation_type = 0, value = 7.859756),
            t.create_value_key(time = phase_duration, interpolation_type = 5, value = 8.127102),
        ),
        (
            t.create_value_key(time = 3.08, interpolation_type = 0, value = bg3.euler_to_quaternion(121.385, -5.047, 0.018, sequence = 'yxz')),
            t.create_value_key(time = phase_duration, interpolation_type = 5, value = bg3.euler_to_quaternion(130.784, -5.151, -0.015, sequence = 'yxz')),
        ),
        (),
        (),
    ))
    t.create_tl_camera_dof(camera2, '0.0', phase_duration, (
        (
            t.create_value_key(time = 3.08, interpolation_type = 0, value = 1.4),
        ),
        (
            t.create_value_key(time = 3.08, interpolation_type = 0, value = 40.0),
        ),
        (
            t.create_value_key(time = 3.08, interpolation_type = 0, value = 1.0),
        ),
        (
            t.create_value_key(time = 3.08, interpolation_type = 0, value = 1.0),
        ),
        (
            t.create_value_key(time = 3.08, interpolation_type = 0),
        ),
        (
            t.create_value_key(time = 3.08, interpolation_type = 0),
        ),
        (
            t.create_value_key(time = 3.08, interpolation_type = 0),
        ),
    ))
    t.create_tl_camera_fov(camera2, '0.0', phase_duration, (
        t.create_value_key(time = 3.08, interpolation_type = 0, value_name = 'FoV', value = 20.0),
    ), is_snapped_to_end = True)

    t.create_tl_animation(
        bg3.SPEAKER_PLAYER, '3.08', phase_duration,
        '69c24f7e-87da-e91d-6a31-cc51e2eea400',
        '668c02f3-f56c-40b1-bc43-37ecd964b6e5',
        animation_play_start_offset = 5.0467,
        fade_in = 0.0,
        fade_out = 0.0,
        offset_type = 2,
        enable_root_motion = True,
        continuous = True,
        is_snapped_to_end = True,
        target_transform = t.create_animation_target_transform(
            1.0, (1.5697, -0.7549, 7.303), bg3.euler_to_quaternion(-167.7856, -2.6211, -1.1995, sequence = 'yxz')))
    t.create_tl_shot(camera2, '3.08', phase_duration, is_snapped_to_end = True)
    t.create_tl_voice(
        bg3.SPEAKER_SHADOWHEART, '3.64', '6.69',
        what_wait_node_uuid,
        performance_fade = 2.0,
        fade_in = 2.0,
        fade_out = 0.0)


###############################################################################
# Hermit crab node
# original start time: 440.34
# duration:            6.7
# end time:            447.04
###############################################################################

def create_hermit_crab_timeline(d: bg3.dialog_object, t: bg3.timeline_object) -> None:
    phase_duration = '6.7'
    camera1 = '2773773e-4ffd-44ae-92f0-5854bf0d6a62'
    t.create_new_phase(hermit_crab_node_uuid, phase_duration)

    t.create_tl_actor_node(bg3.timeline_object.SHOW_VISUAL, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        t.create_value_key(time = 0.0, interpolation_type = 3, value_name = 'ShowVisual', value = True),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.SHOW_VISUAL, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_value_key(time = 0.0, interpolation_type = 3, value_name = 'ShowVisual', value = True),
    ), is_snapped_to_end = True)
    t.create_tl_non_actor_node(bg3.timeline_object.SWITCH_LOCATION, '0.0', phase_duration, (), is_snapped_to_end = True)
    t.create_tl_non_actor_node(bg3.timeline_object.SWITCH_STAGE, '0.0', phase_duration, (), is_snapped_to_end = True)
    #t.create_tl_actor_node(bg3.timeline_object.SHOW_VISUAL, 'cd43a0cf-dbe2-44c1-9655-ce9fc5386f40', 0.0, phase_duration, (), is_snapped_to_end = True)
    #t.create_tl_actor_node(bg3.timeline_object.SHOW_VISUAL, '2366c911-04c5-4a0a-ae96-eeb14c153931', 0.0, phase_duration, (), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.SHOW_VISUAL, ACTOR_HERMIT_CRAB, '0.0', phase_duration, (
        t.create_value_key(time = 0.0, interpolation_type = 3),
        t.create_value_key(time = 6.92, interpolation_type = 3, value_name = 'ShowVisual', value = False),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.SOUND, 'd8311b54-84be-4a8b-91f2-80c643dfc4fb', '0.0', phase_duration, (
        t.create_sound_event_key(0.0, sound_event_id = 'd7167dd1-7f06-47b8-846b-28880ddd9558'),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.PLAY_EFFECT, '260ee065-cb60-4d24-a77f-1b108023c4e9', '0.0', phase_duration, (), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.PLAY_EFFECT, 'f74b7ea5-4e09-4998-8d56-62290aeebccf', '0.0', phase_duration, (
        t.create_value_key(time = 0.0, interpolation_type = 3, value_name = 'PlayEffect', value = False),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.PLAY_EFFECT, '43870af9-59de-4762-828d-ae3f2b6bd220', '0.0', phase_duration, (
        t.create_value_key(time = 0.0, interpolation_type = 3, value_name = 'PlayEffect', value = False),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.PLAY_EFFECT, 'cbcc553f-5eb6-409a-856b-2cce6eac271e', '0.0', phase_duration, (), is_snapped_to_end = True)
    t.create_tl_animation(
        ACTOR_HERMIT_CRAB,
        '0.0', '6.92',
        'a5305f77-4ea9-f17d-0eb5-54efede733a7',
        '20259bf4-b466-4460-8510-a9eb96d6d691',
        animation_play_start_offset = 0.98,
        fade_in = 0.0,
        fade_out = 0.0,
        offset_type = 2,
        enable_root_motion = True,
        continuous = True,
        target_transform = t.create_animation_target_transform(1.0, (0.0, -0.129, 0.0), bg3.euler_to_quaternion(102.798, 8.511, 1.926, sequence = 'yxz')))
    t.create_tl_transform(
        'd8311b54-84be-4a8b-91f2-80c643dfc4fb', '0.0', phase_duration, (
            (
                t.create_value_key(time = 0.0, interpolation_type = 3, value = 0.0),
            ),
            (
                t.create_value_key(time = 0.0, interpolation_type = 3, value = 0.05),
            ),
            (
                t.create_value_key(time = 0.0, interpolation_type = 3, value = 0.0),
            ),
            (
                t.create_value_key(time = 0.0, interpolation_type = 3, value = bg3.euler_to_quaternion(0.0, 0.0, 0.0, sequence = 'yxz')),
            ),
            (
                t.create_value_key(time = 0.0, interpolation_type = 3, value = 0.2),
            ),
            (
                t.create_frame_of_reference_key(0.0, 3, ACTOR_HERMIT_CRAB, "", False, True),
            )
        ), continuous = True)
    t.create_tl_transform(
        ACTOR_HERMIT_CRAB, '0.0', '0.49', (
            (
                t.create_value_key(time = 0.0, interpolation_type = 3, value = 8.27),
            ),
            (
                t.create_value_key(time = 4.47, interpolation_type = 3, value = -0.37),
            ),
            (
                t.create_value_key(time = 4.47, interpolation_type = 3, value = 8.67),
            ),
            (
                t.create_value_key(time = 4.47, interpolation_type = 3, value = bg3.euler_to_quaternion(-176.88268, 0.0, 0.0, sequence = 'yxz')),
            ),
            (
                t.create_value_key(time = 4.47, interpolation_type = 3, value = 1.0),
            ),
            (),
        ))
    t.create_tl_transform(
        '76e352cd-bd60-40e6-afb9-2dd21e1c0512', '0.0', '2.22', (
            (),
            (),
            (
                t.create_value_key(time = 2.22, interpolation_type = 0, value = 0.15),
            ),
            (
                t.create_value_key(time = 2.22, interpolation_type = 0, value = bg3.euler_to_quaternion(156.564947, 2.878842, -0.021439, sequence = 'yxz')),
            ),
            (),
            ()
        ))
    t.create_tl_transform(
        'c03290fc-a9d1-4b31-a318-8309540d53ba', '0.0', '6.08', (
            (
                t.create_value_key(time = 0.0, interpolation_type = 0, value = 2.221755),
                t.create_value_key(time = 6.08, interpolation_type = 5, value = 2.819271),
            ),
            (
                t.create_value_key(time = 0.0, interpolation_type = 0, value = 0.9113636),
                t.create_value_key(time = 6.08, interpolation_type = 5, value = 0.9052609),
            ),
            (
                t.create_value_key(time = 0.0, interpolation_type = 0, value = 8.531829),
                t.create_value_key(time = 6.08, interpolation_type = 5, value = 8.352493),
            ),
            (
                t.create_value_key(time = 0.0, interpolation_type = 0, value = bg3.euler_to_quaternion(-172.95388208194757, 3.1201805749382183, -0.023195006150739453, sequence = 'yxz')),
                t.create_value_key(time = 1.7, interpolation_type = 0, value = bg3.euler_to_quaternion(-171.57931242330017, 4.438537538233648, -0.02315474275238145, sequence = 'yxz')),
                t.create_value_key(time = 6.08, interpolation_type = 0, value = bg3.euler_to_quaternion(-164.6996587747424, 4.139676187345997, 0.032837228010279274, sequence = 'yxz')),
            ),
            (),
            ()
        ))
    t.create_tl_transform(
        camera1, '0.0', phase_duration, (
            (
                t.create_value_key(time = 4.47, interpolation_type = 5, value = 8.240543),
                t.create_value_key(time = phase_duration, interpolation_type = 5, value = 8.240543),
            ),
            (
                t.create_value_key(time = 4.47, interpolation_type = 5, value = -0.3154944),
                t.create_value_key(time = phase_duration, interpolation_type = 5, value = -0.3154944),
            ),
            (
                t.create_value_key(time = 4.47, interpolation_type = 5, value = 11.41944),
                t.create_value_key(time = phase_duration, interpolation_type = 5, value = 11.41944),
            ),
            (
                t.create_value_key(time = 4.47, interpolation_type = 5, value = bg3.euler_to_quaternion(-176.33212516612303, -2.324291197723004, -0.023308336932487853, sequence = 'yxz')),
                t.create_value_key(time = phase_duration, interpolation_type = 5, value = bg3.euler_to_quaternion(-162.06552180366452, -2.318597681729297, -0.022221253575686526, sequence = 'yxz')),
            ),
            (),
            (),
        ), is_snapped_to_end = True)
    t.create_tl_camera_dof(
        camera1, '0.0', phase_duration, (
            (
                t.create_value_key(time = 0.0, interpolation_type = 0, value = 2.7),
            ),
            (
                t.create_value_key(time = 0.0, interpolation_type = 0, value = 50),
            ),
            (
                t.create_value_key(time = 0.0, interpolation_type = 0, value = 1),
            ),
            (
                t.create_value_key(time = 0.0, interpolation_type = 0, value = 1),
            ),
            (
                t.create_value_key(time = 0.0, interpolation_type = 0),
            ),
            (
                t.create_value_key(time = 0.0, interpolation_type = 0),
            ),
            (
                t.create_value_key(time = 0.0, interpolation_type = 0),
            ),
        ), is_snapped_to_end = True)
    t.create_tl_camera_fov(camera1, '0.0', phase_duration, (
        t.create_value_key(time = 0.0, interpolation_type = 2, value_name = 'FoV', value = 16.0),
    ), is_snapped_to_end = True)
    t.create_tl_shot(camera1, '0.0', phase_duration, is_snapped_to_end = True)


###############################################################################
# Oh Hells that's cold.
# original start time: 447.04
# duration:            7.76
# end time:            454.8
###############################################################################

def create_oh_hells_thats_cold_timeline(d: bg3.dialog_object, t: bg3.timeline_object) -> None:
    camera = '19c25796-250c-47f9-844f-b0a5b9796ee3'
    phase_duration = '6.4' #6.76
    t.create_new_phase(oh_hells_thats_cold_node_uuid, phase_duration)

    t.create_tl_actor_node(bg3.timeline_object.SHOW_VISUAL, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        t.create_value_key(time = 0.0, interpolation_type = 3, value_name = 'ShowVisual', value = True),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.SHOW_VISUAL, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_value_key(time = 0.0, interpolation_type = 3, value_name = 'ShowVisual', value = True),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.ATTITUDE, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.ATTITUDE, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.EMOTION, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_emotion_key(2.52, 64, variation = 2),  # 449.56
    ))
    t.create_tl_actor_node(bg3.timeline_object.EMOTION, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        t.create_emotion_key(7.25, 2),                   # 454.29
    ))
    t.create_tl_actor_node(bg3.timeline_object.LOOK_AT, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_look_at_key(
            0.0,
            turn_mode = 3,
            turn_speed_multiplier = 0.3,
            head_turn_speed_multiplier = 0.3,
            weight = 0,
            look_at_mode = 0
        ),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.LOOK_AT, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        t.create_look_at_key(
            0.0,
            turn_mode = 3,
            turn_speed_multiplier = 0.3,
            head_turn_speed_multiplier = 0.3,
            weight = 0,
            look_at_mode = 0
        ),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.SHOW_VISUAL, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.SHOW_VISUAL, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.SHOW_VISUAL, ACTOR_HERMIT_CRAB, '0.0', phase_duration, (
        t.create_value_key(time = 0.0, interpolation_type = 3, value_name = 'ShowVisual', value = False),
    ), is_snapped_to_end = True)
    t.create_tl_show_armor(bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
        (),
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
        (),
        (),
        (),
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
    ), is_snapped_to_end = True)
    t.create_tl_show_armor(bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
        (),
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
        (),
        (),
        (),
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.SOUND, '7835e997-e23c-45b2-b491-e5631e6587d6', '0.0', phase_duration, (
        t.create_sound_event_key(0.1, sound_event_id = '128d0631-04d1-4d41-9dfc-d57743acd91b'),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.PLAY_EFFECT, 'f74b7ea5-4e09-4998-8d56-62290aeebccf', '0.0', phase_duration, (
        t.create_value_key(time = 0.0, interpolation_type = 3),
    ))
    t.create_tl_actor_node(bg3.timeline_object.PLAY_EFFECT, '43870af9-59de-4762-828d-ae3f2b6bd220', '0.0', phase_duration, (
        t.create_value_key(time = 0.0, interpolation_type = 3),
    ))
    t.create_tl_splatter(bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_splatter_channel(0),
        t.create_splatter_channel(1),
        t.create_splatter_channel(2),
        t.create_splatter_channel(3, time = 0.0, value = 1.0)
    ), is_snapped_to_end = True)
    t.create_tl_splatter(bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        t.create_splatter_channel(0),
        t.create_splatter_channel(1),
        t.create_splatter_channel(2),
        t.create_splatter_channel(3, time = 0.0, value = 1.0)
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.SPRINGS, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.SPRINGS, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.PHYSICS, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_value_key(time = 0.0, value_name = 'InverseKinematics', value = False, interpolation_type = 3),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.PHYSICS, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_value_key(time = 0.0, value_name = 'InverseKinematics', value = False, interpolation_type = 3),
    ), is_snapped_to_end = True)
    t.create_tl_non_actor_node(bg3.timeline_object.SWITCH_LOCATION, '0.0', phase_duration, (), is_snapped_to_end = True)
    t.create_tl_non_actor_node(bg3.timeline_object.SWITCH_STAGE, '0.0', phase_duration, (
        t.create_switch_stage_event_key(0.0, event_uuid = '5cbe087e-8f9a-42d8-96e4-af0f200ce93e'),
    ), is_snapped_to_end = True)
    t.create_tl_animation(
        bg3.SPEAKER_PLAYER, '0.0', phase_duration,
        '4e6cc7d8-2c45-4c99-9314-dfd11c7d9cd7',
        '668c02f3-f56c-40b1-bc43-37ecd964b6e5',
        animation_play_start_offset = 0.75,
        fade_in = 0.0,
        fade_out = 0.0,
        offset_type = 5,
        enable_root_motion = True)
    t.create_tl_animation(
        bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration,
        '04cf151a-8ee6-824b-6a5f-4a2f928efa54',
        '753d2fcc-313c-4f58-8b1c-2139dd4cb4fb',
        animation_play_start_offset = 0.75,
        fade_in = 0.0,
        fade_out = 0.0,
        offset_type = 5,
        enable_root_motion = True)
    t.create_tl_transform(
        '43870af9-59de-4762-828d-ae3f2b6bd220', '0.0', phase_duration, (
            (
                t.create_value_key(time = 0.0, interpolation_type = 3, value = -3.1),
            ),
            (
                t.create_value_key(time = 0.0, interpolation_type = 3, value = -0.47),
            ),
            (
                t.create_value_key(time = 0.0, interpolation_type = 3, value = 15.34611),
            ),
            (
                t.create_value_key(time = 0.0, interpolation_type = 3, value = bg3.euler_to_quaternion(0.0, 0.0, 0.0, sequence = 'yxz')),
            ),
            (
                t.create_value_key(time = 0.0, interpolation_type = 3, value = 0.5),
            ),
            ()
        ), continuous = True)
    t.create_tl_transform(
        'f74b7ea5-4e09-4998-8d56-62290aeebccf', '0.0', phase_duration, (
            (
                t.create_value_key(time = 0.0, interpolation_type = 2, value = -1.7),
            ),
            (
                t.create_value_key(time = 0.0, interpolation_type = 2, value = -0.47),
            ),
            (
                t.create_value_key(time = 0.0, interpolation_type = 2, value = 15.34611),
            ),
            (
                t.create_value_key(time = 0.0, interpolation_type = 2, value = bg3.euler_to_quaternion(0.0, 0.0, 0.0, sequence = 'yxz')),
            ),
            (
                t.create_value_key(time = 0.0, interpolation_type = 2, value = 0.3),
            ),
            ()
        ), continuous = True)
    t.create_tl_transform(
        '40fb1d31-fbba-43d3-9f7e-a5fa4a70cb6e', '2.17', phase_duration, (
            (
                t.create_value_key(time = 4.72, interpolation_type = 2, value = -7.55371),
            ),
            (
                t.create_value_key(time = 4.72, interpolation_type = 2, value = -0.02595572),
            ),
            (
                t.create_value_key(time = 4.72, interpolation_type = 2, value = 39.42289),
            ),
            (
                t.create_value_key(time = 4.72, interpolation_type = 2, value = bg3.euler_to_quaternion(163.2708, -2.9055, 0.0224, sequence = 'yxz')),
            ),
            (),
            ()
        ))
    t.create_tl_transform('f481e268-7098-4acb-9c71-0fe83e9e20ec', '3.16', phase_duration, ())
    t.create_tl_transform('83656b91-c327-4d57-97b4-b2b9f6d0c45e', '3.16', phase_duration, ())
    t.create_tl_transform('a528493e-85a4-406f-a05b-a68abd459bb6', '3.16', phase_duration, ())

    t.create_tl_transform(
        camera, '0.0', phase_duration, (
            (
                t.create_value_key(time = 0.0, interpolation_type = 0, value = -8.491296),
                t.create_value_key(time = phase_duration, interpolation_type = 0, value = -7.955216),
            ),
            (
                t.create_value_key(time = 0.0, interpolation_type = 0, value = -0.2529699),
                t.create_value_key(time = phase_duration, interpolation_type = 0, value = -0.2388907),
            ),
            (
                t.create_value_key(time = 0.0, interpolation_type = 0, value = -4.08088),
                t.create_value_key(time = phase_duration, interpolation_type = 0, value = -2.530615),
            ),
            (
                t.create_value_key(time = 0.0, interpolation_type = 0, value = bg3.euler_to_quaternion(19.48, -1.1, 0.0, sequence = 'yxz')),
                t.create_value_key(time = 0.0, interpolation_type = 0, value = bg3.euler_to_quaternion(18.56, 0.4, 0.0, sequence = 'yxz')),
            ),
            (),
            ()
        ))
    t.create_tl_voice(
        bg3.SPEAKER_SHADOWHEART, '0.22', '3.59',
        oh_hells_thats_cold_node_uuid,
        performance_fade = 2.0,
        fade_in = 2.0,
        fade_out = 0.0,
        disable_mocap = True)

    t.create_tl_camera_dof(camera, '0.0', phase_duration, (
        (
            t.create_value_key(time = 0.0, interpolation_type = 0, value = 19.0)
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 0, value = 8.0)
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 0, value = 1.0)
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 0, value = 1.0)
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 0, value = 4.0)
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 0)
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 0, value = 3.0)
        ),
    ), is_snapped_to_end = True)
    t.create_tl_camera_fov(camera, '0.0', phase_duration, (
        t.create_value_key(time = 0.0, interpolation_type = 0, value_name = 'FoV', value = 16.0),
    ))
    t.create_tl_shot(camera, '0.0', phase_duration)


###############################################################################
# My feet aren't touching the bottom anymore - it's <i>terrifying</i>.
# Do people really enjoy this?
# original start time: 238.1
# duration:             11.68
# end time:            249.78
###############################################################################

def create_my_feet_arent_touching_the_bottom_anymore_timeline(d: bg3.dialog_object, t: bg3.timeline_object) -> None:
    camera1 = '72c1e5ae-0201-404f-b31d-ec190c10ef77'
    camera2 = '61fbaded-ffc1-48df-b4d0-46e6a85ff534'
    camera3 = 'aea0ef16-7853-444d-95a5-09a98fff41bf'

    phase_duration = '11.68'
    t.create_new_phase(my_feet_arent_touching_the_bottom_anymore_node_uuid, phase_duration)

    t.create_tl_non_actor_node(bg3.timeline_object.SWITCH_LOCATION, '0.0', phase_duration, (), is_snapped_to_end = True)
    t.create_tl_non_actor_node(bg3.timeline_object.SWITCH_STAGE, '0.0', phase_duration, (
        t.create_switch_stage_event_key(0.0, event_uuid = '5cbe087e-8f9a-42d8-96e4-af0f200ce93e'),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.SHOW_VISUAL, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        t.create_value_key(time = 0.0, interpolation_type = 3, value_name = 'ShowVisual', value = True),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.SHOW_VISUAL, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_value_key(time = 0.0, interpolation_type = 3, value_name = 'ShowVisual', value = True),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.EMOTION, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        t.create_emotion_key(8.87, 2),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.EMOTION, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_emotion_key(0.0, 2),
        t.create_emotion_key(6.75, 64, variation = 1),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.LOOK_AT, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        t.create_look_at_key(
            0.0,
            turn_mode = 3,
            turn_speed_multiplier = 0.3,
            head_turn_speed_multiplier = 0.3,
            weight = 0,
            look_at_mode = 0),
    ), is_snapped_to_end= True)
    t.create_tl_actor_node(bg3.timeline_object.LOOK_AT, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_look_at_key(
            0.0,
            turn_mode = 3,
            turn_speed_multiplier = 0.3,
            head_turn_speed_multiplier = 0.3,
            weight = 0,
            look_at_mode = 0),
    ), is_snapped_to_end= True)
    t.create_tl_actor_node(bg3.timeline_object.SOUND, '3552747d-5796-44af-9a51-5aee5865ebcb', '0.0', phase_duration, (
        t.create_sound_event_key(0.66, sound_event_id = 'a039744b-63f7-49cf-a618-0e2ca0fc7d95'),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.SOUND, 'dcf756ae-8126-47e3-bea2-43fa14cf847a', '0.0', phase_duration, (
        t.create_sound_event_key(6.51, sound_event_id = 'd06703ad-73ed-47d8-b04e-4fff2196c807'),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.SOUND, '7835e997-e23c-45b2-b491-e5631e6587d6', '0.0', phase_duration, (
        t.create_sound_event_key(0.25, sound_event_id = 'a039744b-63f7-49cf-a618-0e2ca0fc7d95'),
    ), is_snapped_to_end = True)
    t.create_tl_splatter(bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_splatter_channel(0),
        t.create_splatter_channel(1),
        t.create_splatter_channel(2),
        t.create_splatter_channel(3, time = 0.0, value = 1.0)
    ), is_snapped_to_end = True)
    t.create_tl_splatter(bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        t.create_splatter_channel(0),
        t.create_splatter_channel(1),
        t.create_splatter_channel(2),
        t.create_splatter_channel(3, time = 0.0, value = 1.0)
    ), is_snapped_to_end = True)
    t.create_tl_show_armor(bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
        (),
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
        (),
        (),
        (),
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
    ), is_snapped_to_end = True)
    t.create_tl_show_armor(bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
        (),
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
        (),
        (),
        (),
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
    ), is_snapped_to_end = True)

    # t.create_tl_transform(camera1, 0.0, phase_duration, (
    #     (
    #         t.create_value_key(time = 0.0, interpolation_type = 0, value = -6.814023),
    #         t.create_value_key(time = 6.38, interpolation_type = 0, value = -5.196828),
    #     ),
    #     (
    #         t.create_value_key(time = 0.0, interpolation_type = 0, value = 2.391685),
    #         t.create_value_key(time = 6.38, interpolation_type = 0, value = 2.391685),
    #     ),
    #     (
    #         t.create_value_key(time = 0.0, interpolation_type = 0, value = -10.68792),
    #         t.create_value_key(time = 6.38, interpolation_type = 0, value = -10.53476),
    #     ),
    #     (
    #         t.create_value_key(time = 0.0, interpolation_type = 0, value = bg3.euler_to_quaternion(-5.3858, 7.3339, 0.0, sequence = 'yxz')),
    #         t.create_value_key(time = 6.38, interpolation_type = 0, value = bg3.euler_to_quaternion(-5.3858, 7.3339, 0.0, sequence = 'yxz')),
    #     ),
    #     (),
    #     (),
    # ))
    # t.create_tl_camera_dof(camera1, 0.0, phase_duration, (
    #     (
    #         t.create_value_key(time = 0.0, interpolation_type = 0, value = 19.0),
    #     ),
    #     (
    #         t.create_value_key(time = 0.0, interpolation_type = 0, value = 4.0),
    #     ),
    #     (
    #         t.create_value_key(time = 0.0, interpolation_type = 0, value = 1.0),
    #     ),
    #     (),
    #     (),
    #     (),
    #     (),
    # ))

    t.create_tl_transform(camera1, '0.0', phase_duration, (
        (
            t.create_value_key(time = 0.0, interpolation_type = 0, value = -3.5),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 0, value = -0.3142635),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 0, value = 19.0),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 0, value = bg3.euler_to_quaternion(165.0, 4.87, 0.0, sequence = 'yxz')),
        ),
        (),
        (),
    ))
    t.create_tl_camera_fov(camera1, '0.0', phase_duration, (
        t.create_value_key(time = 0.0, interpolation_type = 2, value_name = 'FoV', value = 27.0),
    ), is_snapped_to_end = True)

    t.create_tl_transform(camera2, '0.0', phase_duration, (
        (
            t.create_value_key(time = 6.38, interpolation_type = 0, value = -4.547183),
        ),
        (
            t.create_value_key(time = 6.38, interpolation_type = 0, value = -0.3142635),
        ),
        (
            t.create_value_key(time = 6.38, interpolation_type = 0, value = 14.36134),
        ),
        (
            t.create_value_key(time = 6.38, interpolation_type = 0, value = bg3.euler_to_quaternion(52.08, 4.87, 0.0, sequence = 'yxz')),
        ),
        (),
        (),
    ))
    t.create_tl_camera_fov(camera2, '0.0', phase_duration, (
        t.create_value_key(time = 6.38, interpolation_type = 2, value_name = 'FoV', value = 20.0),
    ), is_snapped_to_end = True)
    
    t.create_tl_transform(camera3, '0.0', phase_duration, (
        (
            t.create_value_key(time = 9.06, interpolation_type = 0, value = 0.3738768),
        ),
        (
            t.create_value_key(time = 9.06, interpolation_type = 0, value = -0.3170906),
        ),
        (
            t.create_value_key(time = 9.06, interpolation_type = 0, value = 14.56228),
        ),
        (
            t.create_value_key(time = 9.06, interpolation_type = 0, value = bg3.euler_to_quaternion(-70.9322, 2.6929, 0.0, sequence = 'yxz')),
        ),
        (),
        (),
    ))
    t.create_tl_camera_dof(camera3, '0.0', phase_duration, (
        (
            t.create_value_key(time = 9.06, interpolation_type = 0, value = 4.0),
        ),
        (
            t.create_value_key(time = 9.06, interpolation_type = 0, value = 15.0),
        ),
        (
            t.create_value_key(time = 9.06, interpolation_type = 0, value = 1.0),
        ),
        (
            t.create_value_key(time = 9.06, interpolation_type = 0, value = 1.0),
        ),
        (
            t.create_value_key(time = 9.06, interpolation_type = 0),
        ),
        (
            t.create_value_key(time = 9.06, interpolation_type = 0),
        ),
        (
            t.create_value_key(time = 9.06, interpolation_type = 0),
        ),
    ))
    t.create_tl_camera_fov(camera3, '0.0', phase_duration, (
        t.create_value_key(time = 9.06, interpolation_type = 0, value_name = 'FoV', value = 26.0),
    ), is_snapped_to_end = True)

    t.create_tl_animation(
        bg3.SPEAKER_SHADOWHEART, '0.0', '6.38',
        '04cf151a-8ee6-824b-6a5f-4a2f928efa54',
        'c117d3bf-4e9c-4255-84bd-9928b424f45c',
        animation_play_start_offset = 0.97,
        fade_in = 0.0,
        fade_out = 0.0,
        offset_type = 5,
        enable_root_motion = True,
        hold_animation = True)
    t.create_tl_animation(
        bg3.SPEAKER_PLAYER, '0.0', '6.38',
        'cb5ce957-13ca-015f-381b-bbc5059b9ba8',
        '668c02f3-f56c-40b1-bc43-37ecd964b6e5',
        animation_play_start_offset = 0.97,
        fade_in = 0.0,
        fade_out = 0.0,
        offset_type = 5,
        enable_root_motion = True,
        hold_animation = True)

    t.create_tl_shot(camera1, '0.0', '6.38')

    t.create_tl_voice(
        bg3.SPEAKER_SHADOWHEART, '2.41', '9.67',
        my_feet_arent_touching_the_bottom_anymore_node_uuid,
        fade_in = 2.0,
        fade_out = 0.0,
        performance_fade = 2.0)

    t.create_tl_animation(
        bg3.SPEAKER_SHADOWHEART, '6.38', '9.06',
        '04cf151a-8ee6-824b-6a5f-4a2f928efa54',
        'c117d3bf-4e9c-4255-84bd-9928b424f45c',
        animation_play_start_offset = 0.97,
        fade_in = 0.0,
        fade_out = 0.0,
        offset_type = 5,
        enable_root_motion = True,
        hold_animation = True)
    t.create_tl_animation(
        bg3.SPEAKER_PLAYER, '6.38', '9.06',
        'cb5ce957-13ca-015f-381b-bbc5059b9ba8',
        '668c02f3-f56c-40b1-bc43-37ecd964b6e5',
        animation_play_start_offset = 0.97,
        fade_in = 0.0,
        fade_out = 0.0,
        offset_type = 5,
        enable_root_motion = True,
        hold_animation = True)
    t.create_tl_shot(camera2, '6.38', '9.06')

    t.create_tl_animation(
        bg3.SPEAKER_SHADOWHEART, '9.06', phase_duration,
        '91138e09-fa53-ad81-10ce-af1859302aba',
        'c117d3bf-4e9c-4255-84bd-9928b424f45c',
        fade_in = 0.0,
        fade_out = 0.0,
        enable_root_motion = True,
        is_snapped_to_end = True,
        continuous = True)
    t.create_tl_animation(
        bg3.SPEAKER_PLAYER, '9.06', phase_duration,
        '80ab7bf1-460b-4ad8-1934-cf52a6f60d13',
        '668c02f3-f56c-40b1-bc43-37ecd964b6e5',
        fade_in = 0.0,
        fade_out = 0.0,
        enable_root_motion = True,
        is_snapped_to_end = True,
        continuous = True)
    t.create_tl_shot(camera3, '9.06', phase_duration, is_snapped_to_end = True)


###############################################################################
# Shadowheart splashes Tav
# original start time: 454.8
# duration:            2.81
# end time:            456.61
###############################################################################

def create_shadowheart_splashes_tav_timeline(d: bg3.dialog_object, t: bg3.timeline_object) -> None:
    camera = 'e050452b-f066-4907-afc7-3ae180c02fb1'
    phase_duration = '2.9' #2.81 #1.6 #1.81
    t.create_new_phase(shadowheart_splashes_tav_node_uuid, phase_duration)

    t.create_tl_actor_node(bg3.timeline_object.SHOW_VISUAL, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        t.create_value_key(time = 0.0, interpolation_type = 3, value_name = 'ShowVisual', value = True),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.SHOW_VISUAL, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_value_key(time = 0.0, interpolation_type = 3, value_name = 'ShowVisual', value = True),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.ATTITUDE, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.ATTITUDE, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.EMOTION, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_emotion_key(2.62, 2),
    ))
    t.create_tl_actor_node(bg3.timeline_object.EMOTION, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        t.create_emotion_key(1.63, 64, variation = 23),
    ))
    t.create_tl_actor_node(bg3.timeline_object.LOOK_AT, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_look_at_key(
            0.0,
            turn_mode = 3,
            turn_speed_multiplier = 0.3,
            head_turn_speed_multiplier = 0.3,
            weight = 0,
            look_at_mode = 0
        ),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.LOOK_AT, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        t.create_look_at_key(
            0.0,
            turn_mode = 3,
            turn_speed_multiplier = 0.3,
            head_turn_speed_multiplier = 0.3,
            weight = 0,
            look_at_mode = 0
        ),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.SHOW_VISUAL, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.SHOW_VISUAL, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.SHOW_VISUAL, ACTOR_HERMIT_CRAB, '0.0', phase_duration, (
        t.create_value_key(time = 0.0, interpolation_type = 3, value_name = 'ShowVisual', value = False),
    ), is_snapped_to_end = True)
    t.create_tl_show_armor(bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
        (),
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
        (),
        (),
        (),
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
    ), is_snapped_to_end = True)
    t.create_tl_show_armor(bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
        (),
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
        (),
        (),
        (),
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
    ), is_snapped_to_end = True)

    t.create_tl_actor_node(bg3.timeline_object.PLAY_EFFECT, '260ee065-cb60-4d24-a77f-1b108023c4e9', '0.0', phase_duration, (
        t.create_value_key(time = 0.0, interpolation_type = 3, value_name = 'PlayEffect', value = False),
        t.create_value_key(time = 1.71, interpolation_type = 3),
    ))
    t.create_tl_actor_node(bg3.timeline_object.PLAY_EFFECT, 'cbcc553f-5eb6-409a-856b-2cce6eac271e', '0.0', phase_duration, (
        t.create_value_key(time = 0.0, interpolation_type = 3, value_name = 'PlayEffect', value = False),
        t.create_value_key(time = 1.28, interpolation_type = 3),
    ))
    t.create_tl_actor_node(bg3.timeline_object.SOUND, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_sound_event_key(1.2, sound_event_id = 'efb45f14-bd92-4966-afc3-35d212c71ef6', sound_object_index = 1),
    ))
    t.create_tl_actor_node(bg3.timeline_object.SPRINGS, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.SPRINGS, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.PHYSICS, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_value_key(time = 0.0, value_name = 'InverseKinematics', value = False, interpolation_type = 3),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.PHYSICS, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_value_key(time = 0.0, value_name = 'InverseKinematics', value = False, interpolation_type = 3),
    ), is_snapped_to_end = True)
    t.create_tl_non_actor_node(bg3.timeline_object.SWITCH_LOCATION, '0.0', phase_duration, (), is_snapped_to_end = True)
    t.create_tl_non_actor_node(bg3.timeline_object.SWITCH_STAGE, '0.0', phase_duration, (
        t.create_switch_stage_event_key(0.0, event_uuid = '5cbe087e-8f9a-42d8-96e4-af0f200ce93e'),
    ), is_snapped_to_end = True)

    t.create_tl_transform(
        '43870af9-59de-4762-828d-ae3f2b6bd220', '0.0', phase_duration, (
            (
                t.create_value_key(time = 0.0, interpolation_type = 3, value = -3.1),
            ),
            (
                t.create_value_key(time = 0.0, interpolation_type = 3, value = -0.47),
            ),
            (
                t.create_value_key(time = 0.0, interpolation_type = 3, value = 15.34611),
            ),
            (
                t.create_value_key(time = 0.0, interpolation_type = 3, value = bg3.euler_to_quaternion(0.0, 0.0, 0.0, sequence = 'yxz')),
            ),
            (
                t.create_value_key(time = 0.0, interpolation_type = 3, value = 0.5),
            ),
            ()
        ), continuous = True)
    t.create_tl_transform(
        'f74b7ea5-4e09-4998-8d56-62290aeebccf', '0.0', phase_duration, (
            (
                t.create_value_key(time = 0.0, interpolation_type = 2, value = -1.7),
            ),
            (
                t.create_value_key(time = 0.0, interpolation_type = 2, value = -0.47),
            ),
            (
                t.create_value_key(time = 0.0, interpolation_type = 2, value = 15.34611),
            ),
            (
                t.create_value_key(time = 0.0, interpolation_type = 2, value = bg3.euler_to_quaternion(0.0, 0.0, 0.0, sequence = 'yxz')),
            ),
            (
                t.create_value_key(time = 0.0, interpolation_type = 2, value = 0.3),
            ),
            ()
        ), continuous = True)
    t.create_tl_transform(
        '40fb1d31-fbba-43d3-9f7e-a5fa4a70cb6e', '0.0', '0.4', (
            (
                t.create_value_key(time = 0.0, interpolation_type = 2, value = -7.55371),
            ),
            (
                t.create_value_key(time = 0.0, interpolation_type = 2, value = -0.02595572),
            ),
            (
                t.create_value_key(time = 0.0, interpolation_type = 2, value = 39.42289),
            ),
            (
                t.create_value_key(time = 0.0, interpolation_type = 2, value = bg3.euler_to_quaternion(163.2708, -2.9055, 0.0224, sequence = 'yxz')),
            ),
            (),
            ()
        ))
    t.create_tl_transform(
        'cbcc553f-5eb6-409a-856b-2cce6eac271e', '0.0', phase_duration, (
            (
                t.create_value_key(time = 0.0, interpolation_type = 2, value = 0.0),
            ),
            (
                t.create_value_key(time = 0.0, interpolation_type = 2, value = 0.0),
            ),
            (
                t.create_value_key(time = 0.0, interpolation_type = 2, value = 0.0),
            ),
            (
                t.create_value_key(time = 0.0, interpolation_type = 2, value = bg3.euler_to_quaternion(0.0, 0.0, 0.0, sequence = 'yxz')),
            ),
            (
                t.create_value_key(time = 0.0, interpolation_type = 2, value = 1.0),
            ),
            (
                t.create_frame_of_reference_key(
                    0.0,
                    interpolation_type = 2,
                    target_uuid = '753d2fcc-313c-4f58-8b1c-2139dd4cb4fb',
                    target_bone = 'Dummy_R_HandFX',
                    one_frame_only = False,
                    keep_scale = True),
            )
        ))
    t.create_tl_transform(
        '260ee065-cb60-4d24-a77f-1b108023c4e9', '0.0', phase_duration, (
            (
                t.create_value_key(time = 0.0, interpolation_type = 2, value = 0.0),
            ),
            (
                t.create_value_key(time = 0.0, interpolation_type = 2, value = 0.0),
            ),
            (
                t.create_value_key(time = 0.0, interpolation_type = 2, value = 0.0),
            ),
            (
                t.create_value_key(time = 0.0, interpolation_type = 2, value = bg3.euler_to_quaternion(0.0, 0.0, 0.0, sequence = 'yxz')),
            ),
            (
                t.create_value_key(time = 0.0, interpolation_type = 2, value = 1.0),
            ),
            (
                t.create_frame_of_reference_key(
                    0.0,
                    interpolation_type = 2,
                    target_uuid = '753d2fcc-313c-4f58-8b1c-2139dd4cb4fb',
                    target_bone = 'Dummy_R_HandFX',
                    one_frame_only = False,
                    keep_scale = True),
            )
        ))

    t.create_tl_splatter(bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_splatter_channel(0),
        t.create_splatter_channel(1),
        t.create_splatter_channel(2),
        t.create_splatter_channel(3, time = 0.0, value = 1.0)
    ), is_snapped_to_end = True)
    t.create_tl_splatter(bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        t.create_splatter_channel(0),
        t.create_splatter_channel(1),
        t.create_splatter_channel(2),
        t.create_splatter_channel(3, time = 0.0, value = 1.0)
    ), is_snapped_to_end = True)

    t.create_tl_animation(
        bg3.SPEAKER_PLAYER, '0.0', phase_duration,
        '4e6cc7d8-2c45-4c99-9314-dfd11c7d9cd7',
        '668c02f3-f56c-40b1-bc43-37ecd964b6e5',
        animation_play_start_offset = 7.51,
        fade_in = 0.0,
        fade_out = 0.0,
        offset_type = 5,
        enable_root_motion = True)
    t.create_tl_animation(
        bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration,
        '04cf151a-8ee6-824b-6a5f-4a2f928efa54',
        '753d2fcc-313c-4f58-8b1c-2139dd4cb4fb',
        animation_play_start_offset = 7.51,
        fade_in = 0.0,
        fade_out = 0.0,
        offset_type = 5,
        enable_root_motion = True)

    t.create_tl_camera_dof(
        camera, '0.0', phase_duration, (
            (
                t.create_value_key(time = 0.0, interpolation_type = 0, value = 1.5)
            ),
            (
                t.create_value_key(time = 0.0, interpolation_type = 0, value = 30.0)
            ),
            (
                t.create_value_key(time = 0.0, interpolation_type = 0, value = 1.0)
            ),
            (
                t.create_value_key(time = 0.0, interpolation_type = 0, value = 1.0)
            ),
            (),
            (
                t.create_value_key(time = 0.0, interpolation_type = 0)
            ),
            (
                t.create_value_key(time = 0.0, interpolation_type = 0)
            )
        ), is_snapped_to_end = True)
    t.create_tl_transform(
        camera, '0.0', phase_duration, (
            (
                t.create_value_key(time = 0.0, interpolation_type = 0, value = -1.785417),
            ),
            (
                t.create_value_key(time = 0.0, interpolation_type = 0, value = -0.3957208),
            ),
            (
                t.create_value_key(time = 0.0, interpolation_type = 0, value = 15.13934),
            ),
            (
                t.create_value_key(time = 0.0, interpolation_type = 0, value = bg3.euler_to_quaternion(-65.3172, 1.8908, 0.0, sequence = 'yxz')),
            ),
            (),
            ()
        ))
    t.create_tl_shot(camera, '0.0', phase_duration)


###############################################################################
# Come here...
# original start time: 456.61
# duration:            10.28
# end time:            466.89
###############################################################################

def create_come_here_timeline(d: bg3.dialog_object, t: bg3.timeline_object) -> None:
    camera = '61fbaded-ffc1-48df-b4d0-46e6a85ff534'
    phase_duration = '10.28'
    t.create_new_phase(come_here_node_uuid, phase_duration)

    t.create_tl_actor_node(bg3.timeline_object.SHOW_VISUAL, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        t.create_value_key(time = 0.0, interpolation_type = 3, value_name = 'ShowVisual', value = True),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.SHOW_VISUAL, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_value_key(time = 0.0, interpolation_type = 3, value_name = 'ShowVisual', value = True),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.ATTITUDE, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.ATTITUDE, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.EMOTION, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_emotion_key(0.0, 2),
        t.create_emotion_key(2.82, 2, variation = 23),
        t.create_emotion_key(9.3, 2),
    ))
    t.create_tl_actor_node(bg3.timeline_object.EMOTION, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        t.create_emotion_key(0.0, 2),
        t.create_emotion_key(0.26, 2, variation = 1, is_sustained = False),
        t.create_emotion_key(9.3, 2),
    ))
    t.create_tl_actor_node(bg3.timeline_object.LOOK_AT, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_look_at_key(
            0.0,
            turn_mode = 3,
            turn_speed_multiplier = 0.3,
            head_turn_speed_multiplier = 0.3,
            weight = 0,
            look_at_mode = 0),
        t.create_look_at_key(
            0.69,
            target = bg3.SPEAKER_PLAYER,
            bone = 'Head_M',
            turn_mode = 3,
            turn_speed_multiplier = 0.3,
            head_turn_speed_multiplier = 0.28137,
            weight = 0,
            safe_zone_angle = 80,
            head_safe_zone_angle = 80,
            look_at_mode = 1,
            eye_look_at_bone = 'Head_M')
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.LOOK_AT, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        t.create_look_at_key(
            0.0,
            turn_mode = 3,
            turn_speed_multiplier = 0.3,
            head_turn_speed_multiplier = 0.3,
            weight = 0,
            look_at_mode = 0
        ),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.SHOW_VISUAL, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.SHOW_VISUAL, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.SHOW_VISUAL, ACTOR_HERMIT_CRAB, '0.0', phase_duration, (
        t.create_value_key(time = 0.0, interpolation_type = 3, value_name = 'ShowVisual', value = False),
    ), is_snapped_to_end = True)
    t.create_tl_show_armor(bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
        (),
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
        (),
        (),
        (),
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
    ), is_snapped_to_end = True)
    t.create_tl_show_armor(bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
        (),
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
        (),
        (),
        (),
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
    ), is_snapped_to_end = True)
    t.create_tl_non_actor_node(bg3.timeline_object.SWITCH_STAGE, '0.0', phase_duration, (
        t.create_switch_stage_event_key(0.0, event_uuid = '5cbe087e-8f9a-42d8-96e4-af0f200ce93e'),
    ), is_snapped_to_end = True)

    t.create_tl_splatter(bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_splatter_channel(0),
        t.create_splatter_channel(1),
        t.create_splatter_channel(2),
        t.create_splatter_channel(3, time = 0.0, value = 1.0)
    ), is_snapped_to_end = True)
    t.create_tl_splatter(bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        t.create_splatter_channel(0),
        t.create_splatter_channel(1),
        t.create_splatter_channel(2),
        t.create_splatter_channel(3, time = 0.0, value = 1.0)
    ), is_snapped_to_end = True)

    t.create_tl_animation(
        bg3.SPEAKER_PLAYER, '0.0', '6.93',
        '4e6cc7d8-2c45-4c99-9314-dfd11c7d9cd7',
        '668c02f3-f56c-40b1-bc43-37ecd964b6e5',
        animation_play_start_offset = 10.796139296,
        fade_in = 0.0,
        fade_out = 0.0,
        offset_type = 2,
        enable_root_motion = True,
        hold_animation = True,
        target_transform = t.create_animation_target_transform(
            1.0, (-3.337885, -1.695444, 15.36661), bg3.euler_to_quaternion(-116.80843, 0.0, 0.0, sequence = 'yxz')))
    t.create_tl_animation(
        bg3.SPEAKER_SHADOWHEART, '0.0', '6.93',
        '04cf151a-8ee6-824b-6a5f-4a2f928efa54',
        'c117d3bf-4e9c-4255-84bd-9928b424f45c',
        animation_play_start_offset = 10.8,
        fade_in = 0.0,
        fade_out = 0.0,
        offset_type = 2,
        enable_root_motion = True,
        hold_animation = True,
        target_transform = t.create_animation_target_transform(
            1.0, (-2.04316, -1.66016, 15.91005), bg3.euler_to_quaternion(54.31412, -0.0, 0.0, sequence = 'yxz')))

    t.create_tl_camera_dof(camera, '0.0', phase_duration, (
        (
            t.create_value_key(time = 4.13, interpolation_type = 5, value = 2.9),
            t.create_value_key(time = 7.46, interpolation_type = 5, value = 100.0),
        ),
        (
            t.create_value_key(time = 4.13, interpolation_type = 5, value = 30.0),
        ),
        (
            t.create_value_key(time = 4.13, interpolation_type = 5, value = 1.0),
        ),
        (
            t.create_value_key(time = 4.13, interpolation_type = 5, value = 1.0),
        ),
        (
            t.create_value_key(time = 4.13, interpolation_type = 5),
        ),
        (
            t.create_value_key(time = 4.13, interpolation_type = 5),
        ),
        (
            t.create_value_key(time = 4.13, interpolation_type = 5),
        ),
    ))
    t.create_tl_camera_fov(camera, '0.0', phase_duration, (
        t.create_value_key(time = 3.22, value_name = 'FoV', value = 20.0),
    ))
    t.create_tl_transform(
        camera, '0.0', phase_duration, (
            (
                t.create_value_key(time = 2.08, interpolation_type = 5, value = -4.398167),
                t.create_value_key(time = 11.26, interpolation_type = 5, value = -4.398167),
            ),
            (
                t.create_value_key(time = 2.08, interpolation_type = 5, value = -0.3142635),
                t.create_value_key(time = 11.26, interpolation_type = 5, value = -0.3872041),
            ),
            (
                t.create_value_key(time = 2.08, interpolation_type = 5, value = 14.18179),
                t.create_value_key(time = 11.26, interpolation_type = 5, value = 15.34189),
            ),
            (
                t.create_value_key(time = 2.08, interpolation_type = 5, value = bg3.euler_to_quaternion(44.97719, 4.69825, 0.0, sequence = 'yxz')),
                t.create_value_key(time = 11.26, interpolation_type = 5, value = bg3.euler_to_quaternion(42.05511, -30.0, 0.0, sequence = 'yxz')),
            ),
            (),
            (),
        ))
    t.create_tl_shot(camera, '0.0', phase_duration)
    t.create_tl_voice(
        bg3.SPEAKER_SHADOWHEART, '0.45', '4.01',
        come_here_node_uuid,
        performance_fade = 2.0,
        fade_in = 2.0,
        fade_out = 0.0,
        disable_mocap = True)
    t.create_tl_animation(
        bg3.SPEAKER_SHADOWHEART, '4.31', '8.95',
        'a0e37a8e-c619-4d0a-840a-061831fb0523',
        '8959c358-e0bc-4e9e-a4c0-04b761b2c6a7',
        animation_slot = 1,
        fade_in = 1.5,
        fade_out = 1.5)


###############################################################################
# Thank you, for being by my side through all of this. I'm glad we have each other.
# original start time: 465.56
# duration:            9.99
# end time:            475.55
###############################################################################

def create_thank_you_i_needed_that_timeline(d: bg3.dialog_object, t: bg3.timeline_object) -> None:
    camera1 = '6b181adf-04c5-467e-9fd1-9db5905a326b'
    #camera2 = '6ab16d55-663c-4005-a4e8-283e8266cd02'
    #camera3 = 'fabb9053-a022-4053-a536-acfbf68c1f58'
    phase_duration = '9.99'
    t.create_new_phase(thank_you_i_needed_that_node_uuid, phase_duration)

    t.create_tl_actor_node(bg3.timeline_object.SHOW_VISUAL, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        t.create_value_key(time = 0.0, interpolation_type = 3, value_name = 'ShowVisual', value = True),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.SHOW_VISUAL, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_value_key(time = 0.0, interpolation_type = 3, value_name = 'ShowVisual', value = True),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.ATTITUDE, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.ATTITUDE, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.EMOTION, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_emotion_key(0.0, 2),
        t.create_emotion_key(3.87, 64),
        t.create_emotion_key(6.35, 64, variation = 2),
    ))
    t.create_tl_actor_node(bg3.timeline_object.EMOTION, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        t.create_emotion_key(0.0, 64),
        t.create_emotion_key(3.9, 2, variation = 1),
    ))
    t.create_tl_actor_node(bg3.timeline_object.LOOK_AT, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_look_at_key(
            0.0,
            target = bg3.SPEAKER_PLAYER,
            bone = 'Head_M',
            turn_mode = 3,
            turn_speed_multiplier = 0.3,
            head_turn_speed_multiplier = 0.28137,
            weight = 0,
            safe_zone_angle = 80,
            head_safe_zone_angle = 80,
            look_at_mode = 1,
            eye_look_at_bone = 'Head_M'
        ),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.LOOK_AT, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        t.create_look_at_key(
            0.0,
            turn_mode = 3,
            turn_speed_multiplier = 0.3,
            head_turn_speed_multiplier = 0.3,
            weight = 0,
            look_at_mode = 0),
        t.create_look_at_key(
            3.5,
            target = bg3.SPEAKER_SHADOWHEART,
            bone = 'Head_M',
            turn_mode = 3,
            turn_speed_multiplier = 0.3,
            head_turn_speed_multiplier = 0.3,
            weight = 0,
            safe_zone_angle = 80,
            head_safe_zone_angle = 80,
            look_at_mode = 1,
            is_eye_look_at_enabled = True,
            offset = (-0.42, -0.324, 1.087),
            eye_look_at_target_id = bg3.SPEAKER_SHADOWHEART,
            eye_look_at_bone = 'Head_M')
    ), is_snapped_to_end = True)

    t.create_tl_non_actor_node(bg3.timeline_object.SWITCH_STAGE, '0.0', phase_duration, (
        t.create_switch_stage_event_key(0.0, event_uuid = 'af25308e-d885-4955-ad16-6ff483b71b2e', force_transform_update = True),
    ))

    t.create_tl_splatter(bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_splatter_channel(0),
        t.create_splatter_channel(1),
        t.create_splatter_channel(2),
        t.create_splatter_channel(3, time = 0.0, value = 1.0)
    ), is_snapped_to_end = True)
    t.create_tl_splatter(bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        t.create_splatter_channel(0),
        t.create_splatter_channel(1),
        t.create_splatter_channel(2),
        t.create_splatter_channel(3, time = 0.0, value = 1.0)
    ), is_snapped_to_end = True)

    t.create_tl_show_armor(bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
        (),
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
        (),
        (),
        (),
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
    ), is_snapped_to_end = True)
    t.create_tl_show_armor(bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
        (),
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
        (),
        (),
        (),
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
    ), is_snapped_to_end = True)

    t.create_tl_camera_dof(camera1, '0.0', '2.8', (
        (
            t.create_value_key(time = 0.0, interpolation_type = 0, value = 3.5),
            #t.create_value_key(time = phase_duration, interpolation_type = 0, value = 3.0),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 0, value = 10),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 0, value = 1),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 0, value = 1),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 0),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 0),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 0),
        ),
    ))
    t.create_tl_transform(camera1, '0.0', '2.8', (
        (
            t.create_value_key(time = 0.0, interpolation_type = 0, value = 5.185493),
            t.create_value_key(time = phase_duration, interpolation_type = 0, value = 4.939955), # 5.2 - 0.026 * t
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 0, value = -0.199504),
            t.create_value_key(time = phase_duration, interpolation_type = 0, value = -0.1611413), # -0.19 + 0.004 * t
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 0, value = 0.5636961),
            t.create_value_key(time = phase_duration, interpolation_type = 0, value = 0.3171002), # 0.564 - 0.0247 * t
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 0, value = bg3.euler_to_quaternion(-134.39075, -6.31982, -0.01643, sequence='yxz')),
            t.create_value_key(time = phase_duration, interpolation_type = 0, value = bg3.euler_to_quaternion(-136.51095, -5.23181, -0.017, sequence='yxz')),
        ),
        (),
        ()
    ))
    #t.create_tl_shot(camera1, 0.0, 8.64)
    
    t.create_tl_shot(camera1, '0.0', '2.8')

    t.create_tl_voice(
        bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration,
        thank_you_i_needed_that_node_uuid,
        performance_fade = 0,
        fade_in = 0,
        fade_out = 0)
    
    t.create_tl_animation(
        bg3.SPEAKER_PLAYER, '0.0', phase_duration,
        'f80782ef-051b-4925-9593-234073211158',
        '668c02f3-f56c-40b1-bc43-37ecd964b6e5',
        fade_in = 0,
        fade_out = 0,
        offset_type = 5,
        hold_animation = True,
        enable_root_motion = True)
    t.create_tl_animation(
        bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration,
        'e31d063a-ef85-f2a6-c354-acbb1f5489f9',
        'c117d3bf-4e9c-4255-84bd-9928b424f45c',
        animation_play_start_offset = 0.35,
        fade_in = 0,
        fade_out = 0,
        offset_type = 2,
        enable_root_motion = True,
        continuous = True,
        target_transform = t.create_animation_target_transform(
            1.0, (2.296675, -0.350525, -1.774567), (bg3.euler_to_quaternion(164.78118, 0, 0, sequence = 'yxz'))))


    t.create_tl_camera_dof(camera1, '2.8', '5.9', (
        (
            t.create_value_key(time = '2.8', interpolation_type = 0, value = 0.7),
        ),
        (
            t.create_value_key(time = '2.8', interpolation_type = 0, value = 25.0),
        ),
        (
            t.create_value_key(time = '2.8', interpolation_type = 0, value = 1),
        ),
        (
            t.create_value_key(time = '2.8', interpolation_type = 0, value = 1),
        ),
        (
            t.create_value_key(time = '2.8', interpolation_type = 0),
        ),
        (
            t.create_value_key(time = '2.8', interpolation_type = 0),
        ),
        (
            t.create_value_key(time = '2.8', interpolation_type = 0),
        ),
    ))
    t.create_tl_transform(camera1, '2.8', '5.9', (
        (
            t.create_value_key(time = 2.8, interpolation_type = 0, value = 3.0),
        ),
        (
            t.create_value_key(time = 2.8, interpolation_type = 0, value = 0.3),
        ),
        (
            t.create_value_key(time = 2.8, interpolation_type = 0, value = -1.2),
        ),
        (
            t.create_value_key(time = 2.8, interpolation_type = 0, value = bg3.euler_to_quaternion(-225.0, -8.0, 0, sequence='yxz')),
        ),
        (),
        ()
    ))
    t.create_tl_shot(camera1, '2.8', '5.9')

    # t.create_tl_camera_fov(camera1, 5.8, phase_duration, (
    #     t.create_value_key(time = 5.8, value_name = 'FoV', value = 16.0)
    # ), is_snapped_to_end = True)

    t.create_tl_camera_dof(camera1, '5.9', phase_duration, (
        (
            t.create_value_key(time = '5.9', interpolation_type = 0, value = 1.25),
        ),
        (
            t.create_value_key(time = '5.9', interpolation_type = 0, value = 10),
        ),
        (
            t.create_value_key(time = '5.9', interpolation_type = 0, value = 1),
        ),
        (
            t.create_value_key(time = '5.9', interpolation_type = 0, value = 1),
        ),
        (
            t.create_value_key(time = '5.9', interpolation_type = 0),
        ),
        (
            t.create_value_key(time = '5.9', interpolation_type = 0),
        ),
        (
            t.create_value_key(time = '5.9', interpolation_type = 0),
        ),
    ))
    t.create_tl_transform(camera1, '5.9', phase_duration, (
        (
            #t.create_value_key(time = 5.9, interpolation_type = 0, value = 2.5),
            t.create_value_key(time = 5.9, interpolation_type = 0, value = 2.8),
        ),
        (
            t.create_value_key(time = 5.9, interpolation_type = 0, value = 0.3),
        ),
        (
            t.create_value_key(time = 5.9, interpolation_type = 0, value = -0.7),
        ),
        (
            t.create_value_key(time = 5.9, interpolation_type = 0, value = bg3.euler_to_quaternion(-200.0, -3.0, 0, sequence='yxz')),
            #t.create_value_key(time = 6.9, interpolation_type = 0, value = bg3.euler_to_quaternion(-180.0, -3.0, 0, sequence='yxz')),
        ),
        (),
        ()
    ))
    t.create_tl_shot(camera1, '5.9', phase_duration, is_snapped_to_end = True)

    # t.create_tl_camera_look_at(camera3, 8.64, phase_duration, (
    #     t.create_tl_camera_look_at_key(8.64, bg3.SPEAKER_PLAYER, 'Head_M', (0.3, 0.4)),
    # ))
    # t.create_tl_transform(camera3, 8.64, phase_duration, (
    #     (
    #         t.create_value_key(time = 8.64, interpolation_type = 0, value = 1.974954),
    #     ),
    #     (
    #         t.create_value_key(time = 8.64, interpolation_type = 0, value = 0.4380218),
    #     ),
    #     (
    #         t.create_value_key(time = 8.64, interpolation_type = 0, value = -1.544251),
    #     ),
    #     (),
    #     (),
    #     ()
    # ))
    #t.create_tl_shot(camera2, 8.64, phase_duration)


###############################################################################
# I don't want to go back. Not just yet.
# original start time: 475.55
# duration:            5.16
# end time:            480.71
###############################################################################

def create_i_dont_want_to_go_back_timeline(d: bg3.dialog_object, t: bg3.timeline_object) -> None:
    camera1 = 'fabb9053-a022-4053-a536-acfbf68c1f58'
    camera2 = 'c8f70199-7776-47d0-82b1-061bfe800acf'
    phase_duration = '5.16'
    t.create_new_phase(i_dont_want_to_go_back_node_uuid, phase_duration)

    t.create_tl_actor_node(bg3.timeline_object.SHOW_VISUAL, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        t.create_value_key(time = 0.0, interpolation_type = 3, value_name = 'ShowVisual', value = True),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.SHOW_VISUAL, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_value_key(time = 0.0, interpolation_type = 3, value_name = 'ShowVisual', value = True),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.ATTITUDE, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.ATTITUDE, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.EMOTION, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_emotion_key(0.0, 64, variation = 2),
        t.create_emotion_key(2.13, 2)
    ))
    t.create_tl_actor_node(bg3.timeline_object.EMOTION, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        t.create_emotion_key(0.0, 2),
    ))
    t.create_tl_non_actor_node(bg3.timeline_object.SWITCH_STAGE, '0.0', phase_duration, (
        t.create_switch_stage_event_key(0.0, event_uuid = 'af25308e-d885-4955-ad16-6ff483b71b2e', force_transform_update = True),
    ))

    t.create_tl_show_armor(bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
        (),
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
        (),
        (),
        (),
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
    ), is_snapped_to_end = True)
    t.create_tl_show_armor(bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
        (),
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
        (),
        (),
        (),
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
    ), is_snapped_to_end = True)

    t.create_tl_camera_look_at(camera1, '0.0', phase_duration, (
        t.create_tl_camera_look_at_key(0.0, bg3.SPEAKER_PLAYER, 'Head_M', (0.3, 0.4)),
    ))
    t.create_tl_transform(camera1, '0.0', phase_duration, (
        (
            t.create_value_key(time = 0.0, interpolation_type = 0, value = 1.974954),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 0, value = 0.4380218),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 0, value = -1.544251),
        ),
        (
        ),
        (),
        ()
    ))
    t.create_tl_shot(camera1, '0.0', '1.63')

    t.create_tl_camera_dof(camera2, '0.0', phase_duration, (
        (
            t.create_value_key(time = 0.0, interpolation_type = 0, value = 1.3),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 0, value = 25.0),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 0, value = 1.0),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 0, value = 1.0),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 0),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 0),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 0),
        )))
    t.create_tl_transform(camera2, '0.0', phase_duration, (
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 3.748054),
            t.create_value_key(time = phase_duration, interpolation_type = 5, value = 3.748054),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 0.2109072),
            t.create_value_key(time = phase_duration, interpolation_type = 5, value = 0.2109072),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = -0.8475647),
            t.create_value_key(time = phase_duration, interpolation_type = 5, value = -0.8475647),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = bg3.euler_to_quaternion(-146.19542, -0.19286, -0.01939, sequence = 'yxz')),
            t.create_value_key(time = phase_duration, interpolation_type = 5, value = bg3.euler_to_quaternion(-149.00257, -1.16785, -0.02, sequence = 'yxz')),
        ),
        (),
        ()
    ))

    t.create_tl_animation(
        bg3.SPEAKER_PLAYER, '0.0', phase_duration,
        'f80782ef-051b-4925-9593-234073211158',
        '668c02f3-f56c-40b1-bc43-37ecd964b6e5',
        animation_play_start_offset = 9.99,
        fade_in = 0,
        fade_out = 0,
        offset_type = 2,
        enable_root_motion = True)
    t.create_tl_animation(
        bg3.SPEAKER_SHADOWHEART, '0.0', '1.63',
        'e31d063a-ef85-f2a6-c354-acbb1f5489f9',
        'c117d3bf-4e9c-4255-84bd-9928b424f45c',
        animation_play_start_offset = 10.34,
        fade_in = 0,
        fade_out = 0,
        offset_type = 2,
        enable_root_motion = True,
        continuous = True,
        target_transform = t.create_animation_target_transform(
            1.0, (2.296675, -0.350525, -1.774567), (bg3.euler_to_quaternion(164.78118, 0, 0, sequence = 'yxz'))))

    t.create_tl_voice(
        bg3.SPEAKER_SHADOWHEART, '0.98', phase_duration,
        i_dont_want_to_go_back_node_uuid,
        performance_fade = 2.0,
        fade_in = 0.0,
        fade_out = 0.0,
        is_snapped_to_end = True)

    t.create_tl_animation(
        bg3.SPEAKER_SHADOWHEART, '1.63', phase_duration,
        '3f4635fa-5acc-bed1-af7f-5fc5c8e6ea6b',
        'c117d3bf-4e9c-4255-84bd-9928b424f45c',
        animation_play_start_offset = 4.25,
        fade_in = 0.0,
        fade_out = 0.0,
        offset_type = 2,
        enable_root_motion = True,
        continuous = True,
        target_transform = t.create_animation_target_transform(
            1.0, (2.60073, -0.3614736, -1.699632), bg3.euler_to_quaternion(164.78118, 0, 0, sequence = 'yxz')))
    t.create_tl_shot(camera2, '1.63', phase_duration, is_snapped_to_end = True)


###############################################################################
# You know you didn't need to wait until I was in the water to hold me.
# original start time: 63.19
# duration:            7.41
# end time:            70.6
###############################################################################

def create_you_didnt_need_to_wait_to_hold_me_timeline(d: bg3.dialog_object, t: bg3.timeline_object) -> None:
    phase_duration = '7.41'
    t.create_new_phase(you_didnt_need_to_wait_to_hold_me_node_uuid, phase_duration)

    t.create_tl_actor_node(bg3.timeline_object.SHOW_VISUAL, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        t.create_value_key(time = 0.0, interpolation_type = 3, value_name = 'ShowVisual', value = True),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.SHOW_VISUAL, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_value_key(time = 0.0, interpolation_type = 3, value_name = 'ShowVisual', value = True),
    ), is_snapped_to_end = True)

    t.create_tl_show_armor(bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
        (),
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
        (),
        (),
        (),
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
    ), is_snapped_to_end = True)
    t.create_tl_show_armor(bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
        (),
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
        (),
        (),
        (),
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
    ), is_snapped_to_end = True)

    t.create_tl_voice(
        bg3.SPEAKER_SHADOWHEART, '0.0', '5.08',
        you_didnt_need_to_wait_to_hold_me_node_uuid,
        performance_fade = 2.0,
        fade_in = 2.0,
        fade_out = 0.0,
        disable_mocap = True)
    t.create_tl_actor_node(bg3.timeline_object.EMOTION, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_emotion_key(0.0, 2, variation = 1),
        t.create_emotion_key(2.19, 2)
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.EMOTION, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        t.create_emotion_key(0.0, 2),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.LOOK_AT, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_look_at_key(
            0.0,
            target = bg3.SPEAKER_PLAYER,
            bone = 'Head_M',
            turn_mode = 3,
            turn_speed_multiplier = 0.3,
            head_turn_speed_multiplier = 0.3,
            weight = 0.0,
            safe_zone_angle = 80.0,
            head_safe_zone_angle = 80.0,
            look_at_mode = 1,
            eye_look_at_bone = 'Head_M'),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.LOOK_AT, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        t.create_look_at_key(
            0.0,
            target = bg3.SPEAKER_SHADOWHEART,
            bone = 'Head_M',
            turn_mode = 3,
            turn_speed_multiplier = 0.3,
            head_turn_speed_multiplier = 0.3,
            weight = 0.0,
            safe_zone_angle = 80.0,
            head_safe_zone_angle = 80.0,
            look_at_mode = 1,
            eye_look_at_bone = 'Head_M'),
    ), is_snapped_to_end = True)
    t.create_tl_animation(
        bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration,
        '91138e09-fa53-ad81-10ce-af1859302aba',
        'c117d3bf-4e9c-4255-84bd-9928b424f45c',
        fade_in = 2.0,
        fade_out = 0.0,
        offset_type = 5,
        continuous = True)
    #t.create_tl_shot('8fe7fd24-d40e-451c-9537-0b3fffb4f71c', 0.0, 5.08, is_jcut_enabled = True, j_cut_length = 1)
    t.create_tl_shot('a5f853f2-73f1-48ba-ba50-f691ce793dff', '0.0', '5.08')
    t.create_tl_animation(
        bg3.SPEAKER_PLAYER, '0.0', phase_duration,
        '80ab7bf1-460b-4ad8-1934-cf52a6f60d13',
        '668c02f3-f56c-40b1-bc43-37ecd964b6e5',
        fade_in = 0.0,
        fade_out = 0.0,
        continuous = True,
        is_snapped_to_end = True)
    t.create_tl_shot('2565f85a-e2a2-41ba-8381-83b7865401f9', '5.08', phase_duration, is_snapped_to_end = True)


###############################################################################
# You pest!
# original start time: 233.23999
# duration:            4.86
# end time:            238.09999
###############################################################################

def create_you_pest_timeline_node_uuid(d: bg3.dialog_object, t: bg3.timeline_object) -> None:
    #phase_duration = 4.86
    phase_duration = '5.93'
    t.create_new_phase(you_pest_node_uuid, phase_duration)

    t.create_tl_actor_node(bg3.timeline_object.SHOW_VISUAL, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        t.create_value_key(time = 0.0, interpolation_type = 3, value_name = 'ShowVisual', value = True),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.SHOW_VISUAL, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_value_key(time = 0.0, interpolation_type = 3, value_name = 'ShowVisual', value = True),
    ), is_snapped_to_end = True)
    t.create_tl_non_actor_node(bg3.timeline_object.SWITCH_LOCATION, '0.0', phase_duration, (), is_snapped_to_end = True)
    t.create_tl_non_actor_node(bg3.timeline_object.SWITCH_STAGE, '0.0', phase_duration, (), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.EMOTION, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_emotion_key(1.12, 64, variation = 24),
        t.create_emotion_key(1.62, 2, variation = 2),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.EMOTION, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_emotion_key(0.51, 2, variation = 2),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.SOUND, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        t.create_sound_event_key(0.8, sound_event_id = 'efb45f14-bd92-4966-afc3-35d212c71ef6', sound_object_index = 1),
    ), is_snapped_to_end = True)

    t.create_tl_show_armor(bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
        (),
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
        (),
        (),
        (),
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
    ), is_snapped_to_end = True)
    t.create_tl_show_armor(bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
        (),
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
        (),
        (),
        (),
        (t.create_value_key(time = '0.0', interpolation_type = 2, value = False),),
    ), is_snapped_to_end = True)

    t.create_tl_transform('260ee065-cb60-4d24-a77f-1b108023c4e9', '0.0', phase_duration, (
        (
            t.create_value_key(time = 0.0, interpolation_type = 3, value = 0.0),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 3, value = 0.0),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 3, value = 0.0),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 3, value = bg3.euler_to_quaternion(0.0, 0.0, 0.0)),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 3, value = 1.0),
        ),
        (
            t.create_frame_of_reference_key(0.0, 3, bg3.SPEAKER_PLAYER, 'Dummy_R_HandFX', False, True),
        ),
    ), is_snapped_to_end = True)
    t.create_tl_transform('cbcc553f-5eb6-409a-856b-2cce6eac271e', '0.0', phase_duration, (
        (
            t.create_value_key(time = 0.0, interpolation_type = 3, value = 0.0),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 3, value = 0.0),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 3, value = 0.0),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 3, value = bg3.euler_to_quaternion(0.0, 0.0, 0.0)),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 3, value = 1.0),
        ),
        (
            t.create_frame_of_reference_key(0.0, 3, bg3.SPEAKER_SHADOWHEART, 'Shoulder_R', False, True),
        ),
    ), is_snapped_to_end = True)

    t.create_tl_actor_node(bg3.timeline_object.PLAY_EFFECT, '260ee065-cb60-4d24-a77f-1b108023c4e9', '0.0', phase_duration, (
        t.create_value_key(time = 0.0, interpolation_type = 3, value_name = 'PlayEffect', value = False),
        t.create_value_key(time = 0.99, interpolation_type = 3),
        t.create_value_key(time = 3.84, interpolation_type = 3, value_name = 'PlayEffect', value = False),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.PLAY_EFFECT, 'cbcc553f-5eb6-409a-856b-2cce6eac271e', '0.0', phase_duration, (
        t.create_value_key(time = 0.0, interpolation_type = 3, value_name = 'PlayEffect', value = False),
        t.create_value_key(time = 1.23, interpolation_type = 3),
        t.create_value_key(time = 3.84, interpolation_type = 3, value_name = 'PlayEffect', value = False),
    ), is_snapped_to_end = True)
    
    t.create_tl_animation(
        bg3.SPEAKER_PLAYER, '0.0', '1.12',
        '96303f5c-65b1-46b5-a834-49a810397408',
        '668c02f3-f56c-40b1-bc43-37ecd964b6e5',
        animation_play_start_offset = 6.47,
        fade_in = 0.0,
        fade_out = 0.0,
        offset_type = 2,
        hold_animation = True,
        target_transform = t.create_animation_target_transform(1.0, (-3.437586, -1.695445, 16.44739), bg3.euler_to_quaternion(-64.127, 0.0, 0.0, sequence = 'yxz')))

    #camera1 = '5c12c243-d1ef-469c-a0be-e98afa66b7ac'
    #camera1 = 'c4fb35c3-b143-4d11-bc4d-5af3968b87bd'
    camera2 = '3f975a3d-e59a-43d3-b1dc-06e3f0b18f77'
    camera3 = '6ab16d55-663c-4005-a4e8-283e8266cd02'

    #camera1 = 'e487f2ef-4cc7-4d27-ba8e-aa0a6dc03616'
    # t.create_tl_transform(camera1, 0.0, phase_duration, (
    #     (
    #         t.create_value_key(time = 0.8, interpolation_type = 5, value = -2.285081),
    #         t.create_value_key(time = 1.62, interpolation_type = 5, value = -2.285081),
    #     ),
    #     (
    #         t.create_value_key(time = 0.8, interpolation_type = 5, value = -0.5029444),
    #         t.create_value_key(time = 1.62, interpolation_type = 5, value = -0.5029444),
    #     ),
    #     (
    #         t.create_value_key(time = 0.8, interpolation_type = 5, value = 15.07436),
    #         t.create_value_key(time = 1.62, interpolation_type = 5, value = 15.07436),
    #     ),
    #     (
    #         t.create_value_key(time = 0.8, interpolation_type = 5, value = bg3.euler_to_quaternion(-38.732, -3.735, 0.0, sequence = 'yxz')),
    #         t.create_value_key(time = 0.8, interpolation_type = 5, value = bg3.euler_to_quaternion(-2.0, -8.777, 0.0, sequence = 'yxz')),
    #     ),
    #     (),
    #     (),
    # ), is_snapped_to_end = True)
    # t.create_tl_camera_fov(camera1, 0.0, phase_duration, (
    #     t.create_value_key(time = 0.0, interpolation_type = 0, value_name = 'FoV', value = 20.0),
    # ), is_snapped_to_end = True)

    camera1 = 'e050452b-f066-4907-afc7-3ae180c02fb1'
    t.create_tl_camera_dof(
        camera1, '0.0', '1.12', (
            (
                t.create_value_key(time = 0.0, interpolation_type = 0, value = 1.5)
            ),
            (
                t.create_value_key(time = 0.0, interpolation_type = 0, value = 30.0)
            ),
            (
                t.create_value_key(time = 0.0, interpolation_type = 0, value = 1.0)
            ),
            (
                t.create_value_key(time = 0.0, interpolation_type = 0, value = 1.0)
            ),
            (),
            (
                t.create_value_key(time = 0.0, interpolation_type = 0)
            ),
            (
                t.create_value_key(time = 0.0, interpolation_type = 0)
            )
        ), is_snapped_to_end = True)
    t.create_tl_transform(
        camera1, '0.0', '1.12', (
            (
                t.create_value_key(time = 0.0, interpolation_type = 0, value = -1.785417),
            ),
            (
                t.create_value_key(time = 0.0, interpolation_type = 0, value = -0.3957208),
            ),
            (
                t.create_value_key(time = 0.0, interpolation_type = 0, value = 15.13934),
            ),
            (
                t.create_value_key(time = 0.0, interpolation_type = 0, value = bg3.euler_to_quaternion(-65.3172, 1.8908, 0.0, sequence = 'yxz')),
            ),
            (),
            ()
        ))
    t.create_tl_shot(camera1, '0.0', '1.12')

    t.create_tl_animation(
        bg3.SPEAKER_SHADOWHEART, '1.12', '3.84',
        '0521b051-bdbf-39de-19cb-59fbb8cdfdd5',
        'c117d3bf-4e9c-4255-84bd-9928b424f45c',
        animation_play_start_offset = 7.36,
        fade_in = 0.0,
        fade_out = 0.0)
    t.create_tl_animation(
        bg3.SPEAKER_PLAYER, '1.12', phase_duration,
        '96303f5c-65b1-46b5-a834-49a810397408',
        '668c02f3-f56c-40b1-bc43-37ecd964b6e5',
        animation_play_start_offset = 7.36,
        fade_in = 0.0,
        fade_out = 0.0,
        offset_type = 2,
        hold_animation = True,
        is_snapped_to_end = True,
        target_transform = t.create_animation_target_transform(1.0, (-3.437586, -1.695445, 16.44739), bg3.euler_to_quaternion(-64.127, 0.0, 0.0, sequence = 'yxz')))

    t.create_tl_transform(camera2, '0.0', phase_duration, (
        (
            t.create_value_key(time = 0.0, interpolation_type = 0, value = -3.389717),
            t.create_value_key(time = 1.12, interpolation_type = 0, value = -3.389717),
            t.create_value_key(time = 1.41, interpolation_type = 5, value = -3.389716),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 0, value = -0.3848768),
            t.create_value_key(time = 1.12, interpolation_type = 0, value = -0.3848768),
            t.create_value_key(time = 1.41, interpolation_type = 5, value = -0.3625968),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 0, value = 15.53428),
            t.create_value_key(time = 1.12, interpolation_type = 0, value = 15.53428),
            t.create_value_key(time = 1.41, interpolation_type = 5, value = 15.53428),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 0, value = bg3.euler_to_quaternion(43.086, -1.042, 0.0, sequence = 'yxz')),
            t.create_value_key(time = 1.12, interpolation_type = 0, value = bg3.euler_to_quaternion(43.086, -1.042, 0.0, sequence = 'yxz')),
            t.create_value_key(time = 1.41, interpolation_type = 5, value = bg3.euler_to_quaternion(64.458, 2.865, 0.0, sequence = 'yxz')),
        ),
        (),
        (),
    ), is_snapped_to_end = True)
    t.create_tl_shot(camera2, '1.12', '3.84')

    t.create_tl_voice(
        bg3.SPEAKER_SHADOWHEART, '3.84', phase_duration,
        you_pest_node_uuid,
        performance_fade = 2.0,
        fade_in = 2.0,
        fade_out = 0.0,
        disable_mocap = True)
    t.create_tl_shot(camera3, '3.84', phase_duration, is_snapped_to_end = True)


def create_2nd_skinny_dipping_scene() -> None:
    ##########################################################################################################
    # Dialog: CAMP_Shadowheart_SkinnyDipping_SD_ROM.lsf
    # Removed dialog options that let Tav walk away if this isn't the first time they swim with Shadowheart
    ##########################################################################################################

    # d = bg3.dialog_object(files.get_file('Gustav', 'Mods/GustavDev/Story/DialogsBinary/Camp/SoloDreams/CAMP_Shadowheart_SkinnyDipping_SD_ROM.lsf'))
    # t = bg3.timeline_object(files.get_file('Gustav', 'Public/GustavDev/Timeline/Generated/CAMP_Shadowheart_SkinnyDipping_SD_ROM.lsf'), d)
    # s = bg3.scene_object(
    #     files.get_file('Gustav', 'Public/GustavDev/Timeline/Generated/CAMP_Shadowheart_SkinnyDipping_SD_ROM_Scene.lsf'),
    #     files.get_file('Gustav', 'Public/GustavDev/Timeline/Generated/CAMP_Shadowheart_SkinnyDipping_SD_ROM_Scene.lsx'))

    ab = game_assets.get_modded_dialog_asset_bundle('CAMP_Shadowheart_SkinnyDipping_SD_ROM')
    d = bg3.dialog_object(ab.dialog)
    t = bg3.timeline_object(ab.timeline, d)
    s = bg3.scene_object(ab.scene_lsf, ab.scene_lsx)

    s.set_light_radius('d3ff4672-e030-463f-b021-3b33b2b046a8', 7.0)
    s.set_light_radius('da58d5f1-361b-44a3-aea8-01fb1555b773', 9.0)

    s.set_direction_light_dims('2319741f-7238-4db9-afa7-377a7324cf7e', 'dffc3db7-d7bb-4965-8569-ef8edbe30b1e', (10.0, 5.0, 8.0))
    s.set_direction_light_dims('6078328c-10b4-439f-a371-bbfaa03ba48d', 'dffc3db7-d7bb-4965-8569-ef8edbe30b1e', (10.0, 5.0, 8.0))
    s.set_direction_light_dims('28ff6231-9e61-4efa-95d3-3d1c03a99f6f', 'dffc3db7-d7bb-4965-8569-ef8edbe30b1e', (10.0, 5.0, 8.0))
    s.set_direction_light_dims('cb6759ec-0463-467e-b20c-940df4221aef', 'dffc3db7-d7bb-4965-8569-ef8edbe30b1e', (10.0, 5.0, 8.0))

    speaker_idx_shadowheart = d.get_speaker_slot_index(bg3.SPEAKER_SHADOWHEART)

    # existing nodes
    tav_ori_yes_you_can_node_uuid = 'c7bba6a2-780f-4fb8-4e08-85ad1880a63c'
    tav_ori_we_dont_have_to_do_this_node_uuid = '958c12a3-f689-a840-d195-8b934658d64b'
    tav_ori_afraid_of_getting_wet_node_uuid = '390a676b-2b7d-a9d6-c22f-0d5c0c135f31'
    tav_ori_shrug_and_run_node_uuid = '8d6eb833-e4e2-6980-4ff3-5d95454d9ffc'

    ori_just_stay_close_node_uuid = '85c87d4f-7e3d-540a-b14c-934bcba31e32'
    ori_before_i_lose_my_nerve_node_uuid = '9a749a44-333a-73b0-c79d-6ae839b73fee'
    ori_i_can_manage_node_uuid = 'cd07e5eb-beca-52aa-d6f7-5369e29ee72a'
    ori_wait_what_node_uuid = '3c78e6db-d620-1c70-850e-2c181f3595df'
    #ori_oh_hells_thats_cold_node_uuid = 'd1d208f3-099a-a89e-1470-2f7fb8dd614b'
    #ori_i_dont_want_to_go_back_node_uuid = '8a5292c9-2dba-c31f-5a0d-9af6462e3c81'
    ori_karlach_no_2nd_upgrade_node_uuid = '133de80e-5f3d-8778-8898-5c459389bcb2'
    ori_dragonborn_just_a_pebble_node_uuid = 'c42aacc3-5eb9-baeb-8ae4-c911991ce8a7'
    ori_short_races_just_a_pebble_node_uuid = '0f0c1d31-6bd6-192a-e2ec-aa99b0acb6c9'
    ori_just_a_pebble_node_uuid = 'fda433c0-4613-8d30-6a06-df743a3cf3a8'

    second_sandcastles_entry_point_node_uuid = '347a3e6a-bfda-4797-8388-0e8b3d55b820'

    d.add_child_dialog_node(tav_ori_yes_you_can_node_uuid, just_stay_close_node_uuid, 0)
    d.add_child_dialog_node(tav_ori_we_dont_have_to_do_this_node_uuid, i_can_manage_node_uuid, 0)
    d.add_child_dialog_node(tav_ori_afraid_of_getting_wet_node_uuid, more_the_drowning_node_uuid, 0)
    #d.add_child_dialog_node(tav_ori_shrug_and_run_node_uuid, what_wait_node_uuid, 0)

    #d.add_child_dialog_node(ori_just_stay_close_node_uuid, second_sandcastles_entry_point_node_uuid, 0)
    #d.add_child_dialog_node(ori_before_lose_my_nerve_node_uuid, second_sandcastles_entry_point_node_uuid, 0)
    #d.add_child_dialog_node(ori_i_can_manage_node_uuid, second_sandcastles_entry_point_node_uuid, 0)

    d.add_child_dialog_node(ori_wait_what_node_uuid, second_sandcastles_entry_point_node_uuid, 0)

    # All right. Just stay close...
    d.create_standard_dialog_node(
        just_stay_close_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [hermit_crab_node_uuid],
        bg3.text_content('h2a36d8a7ge7f5g4243g9483g7a715faa3239', 2),
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(Shadowheart_More_Sandcastles.uuid, True, speaker_idx_shadowheart),
            )),
        ))
    create_just_stay_close_timeline(d, t)

    # Wait - just give me a moment. I can manage. As long as you stay with me.
    d.create_standard_dialog_node(
        i_can_manage_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [hermit_crab_node_uuid],
        bg3.text_content('hc5469384gcf5bg4680g84ffg3e9de10717b5', 2),
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(Shadowheart_More_Sandcastles.uuid, True, speaker_idx_shadowheart),
            )),
        ))
    create_i_can_manage_timeline(d, t)

    # More the drowning, and the things that could be hiding underwater, and the drowning, and the cold. Did I mention the drowning?
    d.create_standard_dialog_node(
        more_the_drowning_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [before_i_lose_my_nerve_node_uuid],
        bg3.text_content('h78c348deg47b5g40d1g88dage5ccb628dc7b', 3),
        group_id = more_the_drowning_node_uuid,
        group_index = 0,
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(Shadowheart_More_Sandcastles.uuid, True, speaker_idx_shadowheart),
            )),
        ))
    # Let's get on with it, before I lose my nerve.
    d.create_standard_dialog_node(
        before_i_lose_my_nerve_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [hermit_crab_node_uuid],
        bg3.text_content('h7f79ad66gcd8fg42dcg9754g792daac1258a', 2),
        group_id = more_the_drowning_node_uuid,
        group_index = 1)
    create_more_the_drowning_timeline(d, t)

    # What...? Wait!
    d.create_standard_dialog_node(
        what_wait_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [hermit_crab_node_uuid],
        bg3.text_content('h198bdddeg81f6g44e8gb556g2a14b27740d0', 3),
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(Shadowheart_More_Sandcastles.uuid, True, speaker_idx_shadowheart),
            )),
        ))
    create_what_wait_timeline(d, t)

    d.create_standard_dialog_node(
        second_sandcastles_entry_point_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [hermit_crab_node_uuid],
        None,
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(Shadowheart_More_Sandcastles.uuid, True, speaker_idx_shadowheart),
            )),
        ))

    d.create_cinematic_dialog_node(
        hermit_crab_node_uuid,
        #[ori_oh_hells_thats_cold_node_uuid])
        [oh_hells_thats_cold_node_uuid])
    create_hermit_crab_timeline(d, t)

    # Oh Hells that's cold.
    d.create_standard_dialog_node(
        oh_hells_thats_cold_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        #['31b1b69b-0fbb-35a1-7a0e-4b222b0c06ce'],
        [my_feet_arent_touching_the_bottom_anymore_node_uuid],
        bg3.text_content('h57b30a46g323fg41dcga8c6g5b6c93b0d27c', 3))
    create_oh_hells_thats_cold_timeline(d, t)

    # My feet aren't touching the bottom anymore - it's terrifying. Do people really enjoy this?
    d.create_standard_dialog_node(
        my_feet_arent_touching_the_bottom_anymore_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [tav_you_can_hold_onto_me_node_uuid, tav_splash_her_playfully_node_uuid],
        bg3.text_content('h3edcb705g95f8g4277ga3b5g0f95c69fef4e', 1))
    create_my_feet_arent_touching_the_bottom_anymore_timeline(d, t)

    # You can hold onto me if you're afraid.
    d.create_standard_dialog_node(
        tav_you_can_hold_onto_me_node_uuid,
        bg3.SPEAKER_PLAYER,
        [you_didnt_need_to_wait_to_hold_me_node_uuid],
        bg3.text_content('h618b18d2g8814g45e6ga781g9b98723959cd', 1),
        constructor = bg3.dialog_object.QUESTION)

    # Splash her, playfully.
    d.create_standard_dialog_node(
        tav_splash_her_playfully_node_uuid,
        bg3.SPEAKER_PLAYER,
        [you_pest_node_uuid],
        bg3.text_content('h9fb54eabgfdefg44d8gabdagc2fed1c5ccd0', 2),
        constructor = bg3.dialog_object.QUESTION)

    # You know you didn't need to wait until I was in the water to hold me.
    d.create_standard_dialog_node(
        you_didnt_need_to_wait_to_hold_me_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [shadowheart_splashes_tav_node_uuid],
        bg3.text_content('hc2fda58dg8913g48f8g9c78g69e5c20d1eb8', 1))
    create_you_didnt_need_to_wait_to_hold_me_timeline(d, t)

    # You pest!
    d.create_standard_dialog_node(
        you_pest_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [shadowheart_splashes_tav_node_uuid],
        bg3.text_content('h212aae05g276cg4136gaaeag84b2d33b797e', 1))
    create_you_pest_timeline_node_uuid(d, t)

    d.create_cinematic_dialog_node(
        shadowheart_splashes_tav_node_uuid,
        [come_here_node_uuid])
    create_shadowheart_splashes_tav_timeline(d, t)

    # Come here...
    d.create_standard_dialog_node(
        come_here_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [flag_setter_node_uuid],
        bg3.text_content('h2372ed03gcf94g4575gbc56gd748ae7b936c', 1))
    create_come_here_timeline(d, t)

    sandcastles_2_times_node_uuid = '19876cb6-bb76-46aa-9406-88fca8186244'
    sandcastles_3_times_node_uuid = '5acbcc72-68cb-4a82-aff0-97a9f32b2b64'
    sandcastles_4_times_node_uuid = '3c14040e-b403-47ce-aabd-15675bf0aa10'
    d.create_standard_dialog_node(
        flag_setter_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [
            sandcastles_2_times_node_uuid,
            sandcastles_3_times_node_uuid,
            sandcastles_4_times_node_uuid,
            thank_you_i_needed_that_node_uuid
        ],
        None)

    d.create_standard_dialog_node(
        sandcastles_2_times_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [thank_you_i_needed_that_node_uuid],
        None,
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(Tav_Shadowheart_Made_Sandcastles_Two_Times.uuid, False, speaker_idx_shadowheart),
            )),
        ),
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(Tav_Shadowheart_Made_Sandcastles_Two_Times.uuid, True, speaker_idx_shadowheart),
            )),
        ))

    d.create_standard_dialog_node(
        sandcastles_3_times_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [thank_you_i_needed_that_node_uuid],
        None,
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(Tav_Shadowheart_Made_Sandcastles_Three_Times.uuid, False, speaker_idx_shadowheart),
            )),
        ),
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(Tav_Shadowheart_Made_Sandcastles_Three_Times.uuid, True, speaker_idx_shadowheart),
            )),
        ))

    d.create_standard_dialog_node(
        sandcastles_4_times_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [thank_you_i_needed_that_node_uuid],
        None,
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(Tav_Shadowheart_Made_Sandcastles_Four_Times.uuid, False, speaker_idx_shadowheart),
            )),
        ),
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(Tav_Shadowheart_Made_Sandcastles_Four_Times.uuid, True, speaker_idx_shadowheart),
            )),
        ))

    # Thank you. I needed that. I needed to know I can face things without Shar.
    d.create_standard_dialog_node(
        thank_you_i_needed_that_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [i_dont_want_to_go_back_node_uuid],
        bg3.text_content('hc587df2bg3b3cg44d9gbb8bg04b93d8bec79', 1))
    create_thank_you_i_needed_that_timeline(d, t)

    # I don't want to go back. Not just yet.
    d.create_standard_dialog_node(
        i_dont_want_to_go_back_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [
            ori_karlach_no_2nd_upgrade_node_uuid,
            ori_dragonborn_just_a_pebble_node_uuid,
            ori_short_races_just_a_pebble_node_uuid,
            ori_just_a_pebble_node_uuid
        ],
        bg3.text_content('h8a823a11gb5f9g4e6fg82b4gad4ec7a48d0a', 2))    
    create_i_dont_want_to_go_back_timeline(d, t)


def create_act3_breakup_scene() -> None:
    # d = bg3.dialog_object(files.get_file('Gustav', 'Mods/GustavDev/Story/DialogsBinary/Camp/Camp_Relationship_Dialogs/CAMP_Shadowheart_CRD_SkinnyDippingRomance.lsf'))
    # t = bg3.timeline_object(files.get_file('Gustav', 'Public/GustavDev/Timeline/Generated/CAMP_Shadowheart_CRD_SkinnyDippingRomance.lsf'), d)

    ab = game_assets.get_modded_dialog_asset_bundle('CAMP_Shadowheart_CRD_SkinnyDippingRomance')
    d = bg3.dialog_object(ab.dialog)
    t = bg3.timeline_object(ab.timeline, d)

    speaker_idx_shadowheart = d.get_speaker_slot_index(bg3.SPEAKER_SHADOWHEART)
    speaker_idx_tav = d.get_speaker_slot_index(bg3.SPEAKER_PLAYER)

    didnt_ask_about_swimming_node_uuid = '9f0ed151-2761-4f1a-9d6c-4b3974fccdb4'

    you_know_we_had_the_beginnings_node_uuid = '917e4fa2-2df0-4705-adf1-7a85e0dcc157'
    it_might_sound_harsh_node_uuid = 'a1b43bd4-491c-4949-b33e-3e771576d3c2'
    too_many_to_list_node_uuid = '083e22a1-c59f-46c3-b11f-9a53f9f51a65'
    we_cant_pretend_node_uuid = '9a28972f-b0fa-4bb7-8d53-de587c593efd'
    theres_no_hard_feelings_node_uuid = '2e962a47-b40d-492d-a708-8660ae612f6d'
    though_for_a_while_node_uuid = '2d3d4d6b-b8bf-4c7d-9b42-aebfa8d26991'
    dont_worry_about_me_node_uuid = 'e116069a-c1d6-4ada-a5a5-5914a6356a34'

    i_felt_the_same_node_uuid = '0ac6b910-53dd-4044-9957-be74665ffbd3'
    what_are_you_talking_about_node_uuid = '97335e2d-4e0c-459e-9eb8-de0aaeea75e3'
    what_happened_node_uuid = '2a07ee82-3854-4fed-9282-ecce88c7f05b'
    but_why_node_uuid = '9fc4054b-aecc-438e-9906-331a816cf73d'

    # Cameras
    # d2ea7696-eded-4662-891e-78c7f1f0fc56 SH  -> SH
    # e5b0b581-0315-4fd8-887f-23714bd6c2d3 SH  -> Tav
    # d754c012-c3ab-424f-bb26-c838a3e866f3 Tav -> SH
    # 3b0a9e0a-0ed7-4443-a962-57cc14d147f6 Tav -> Tav

    # Break-up entry point
    # If Tav didn't offer help to save her parents and didn't ask about swimming, she will break up
    d.create_standard_dialog_node(
        didnt_ask_about_swimming_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [you_know_we_had_the_beginnings_node_uuid],
        None,
        constructor = bg3.dialog_object.GREETING,
        root = True,
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(Aylin_Told_Shadowheart_About_Parents.uuid, True, speaker_idx_shadowheart),
                bg3.flag(Tav_Promised_Help_Saving_Parents.uuid, False, speaker_idx_shadowheart),
            )),
            bg3.flag_group('Global', (
                bg3.flag(bg3.FLAG_ORI_Shadowheart_Knows_PersonalInfo, False),
            )),
        ))

    # You know, we had the beginnings of something special once... but it was not meant to be, I suppose. Perhaps happiness lies elsewhere, for both of us.
    d.create_standard_dialog_node(
        you_know_we_had_the_beginnings_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [
            i_felt_the_same_node_uuid,
            what_are_you_talking_about_node_uuid,
            what_happened_node_uuid,
            but_why_node_uuid
        ],
        bg3.text_content('h07ead16bg9785g4e6cga87egb482f54481b2', 2),
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_State_WasPartneredWithShadowheart, True, speaker_idx_tav),
                bg3.flag(bg3.FLAG_ORI_State_PartneredWithShadowheart, False, speaker_idx_tav)
            )),
        ))
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '12.61',
        you_know_we_had_the_beginnings_node_uuid,
        (('12.8', 'd754c012-c3ab-424f-bb26-c838a3e866f3'), (None, 'e5b0b581-0315-4fd8-887f-23714bd6c2d3')),
        phase_duration = '12.95',
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 16, None), (6.12, 32, None), (7.32, 64, 2), (9.76, 4, None), (10.65, 0, None), (12.0, 64, None)),
            bg3.SPEAKER_PLAYER: ((0.0, 1, None), (10.0, 32, None)),
        })

    # I felt the same. That little spark we shared, it is snuffed out now.
    d.create_standard_dialog_node(
        i_felt_the_same_node_uuid,
        bg3.SPEAKER_PLAYER,
        [theres_no_hard_feelings_node_uuid],
        bg3.text_content('h1240259dgc597g453cg8bacgb0fe544a5fdd', 1),
        constructor = bg3.dialog_object.QUESTION)

    # What are you talking about?
    d.create_standard_dialog_node(
        what_are_you_talking_about_node_uuid,
        bg3.SPEAKER_PLAYER,
        [it_might_sound_harsh_node_uuid],
        bg3.text_content('hb6e5b7a3ged7dg44d3g9dcegfcc3ca6d0347', 1),
        constructor = bg3.dialog_object.QUESTION)

    # What happened? What have I done to make you say that?
    d.create_standard_dialog_node(
        what_happened_node_uuid,
        bg3.SPEAKER_PLAYER,
        [too_many_to_list_node_uuid],
        bg3.text_content('h1c32e152gd4adg4b31gac89gb05243bae1ff', 1),
        constructor = bg3.dialog_object.QUESTION)

    # But why? I thought we're doing good together. Tell me what could I do for us...
    d.create_standard_dialog_node(
        but_why_node_uuid,
        bg3.SPEAKER_PLAYER,
        [we_cant_pretend_node_uuid],
        bg3.text_content('h875060d1g5ab3g49cag9993ge310a94ef55b', 1),
        constructor = bg3.dialog_object.QUESTION)

    # It might sound harsh, but we're desperate, thrown together by fate. We both might want to see things that aren't truly there.
    d.create_standard_dialog_node(
        it_might_sound_harsh_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [theres_no_hard_feelings_node_uuid],
        bg3.text_content('h9049c50ag5230g4404gbe25g5b93ea38da4b', 1))
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '8.76',
        it_might_sound_harsh_node_uuid,
        ((None, 'd2ea7696-eded-4662-891e-78c7f1f0fc56'),),
        phase_duration = '9.2',
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.1, 16, None), (2.21, 0, None), (3.7, 64, None), (6.06, 8, None)),
            bg3.SPEAKER_PLAYER: ((7.0, 8, None),),
        })

    # Too many to list. But the fact that you can't figure it out for yourself is very telling.
    d.create_standard_dialog_node(
        too_many_to_list_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [dont_worry_about_me_node_uuid],
        bg3.text_content('he00b142bg5b23g4455ga781g8f14c5e5f77b', 1))
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '5.39',
        too_many_to_list_node_uuid,
        ((None, 'd754c012-c3ab-424f-bb26-c838a3e866f3'),),
        phase_duration = '5.9',
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 128, None), (1.48, 4, None)),
            bg3.SPEAKER_PLAYER: ((0.0, 1, None),),
        })

    # Don't. We can't pretend to be someone we're not - either of us. It'll just end badly.
    d.create_standard_dialog_node(
        we_cant_pretend_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [theres_no_hard_feelings_node_uuid],
        bg3.text_content('h6d8757ccgc91eg4d61gb239g5399f29ff092', 1))
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '8.52',
        we_cant_pretend_node_uuid,
        ((None, 'd2ea7696-eded-4662-891e-78c7f1f0fc56'),),
        phase_duration = '9.1',
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 128, None), (1.61, 32, None), (5.68, 2048, 1), (6.18, 2048, 1)),
            bg3.SPEAKER_PLAYER: ((0.0, 1, None),),
        })

    # There's no hard feelings - genuinely. You deserve happiness, and I'm more than glad to remain with you to bear witness to it.
    d.create_standard_dialog_node(
        theres_no_hard_feelings_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [though_for_a_while_node_uuid],
        bg3.text_content('hb2ee4ec2g2cf0g456bg839eg0d5fa0a9083a', 3))
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '12.44',
        theres_no_hard_feelings_node_uuid,
        ((None, 'd754c012-c3ab-424f-bb26-c838a3e866f3'),),
        phase_duration = '12.9',
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 1024, 1), (1.58, 64, None), (3.83, 16, 1), (6.26, 64, None), (7.16, 2, None), (8.98, 64, 1), (10.9, 2, None)),
            bg3.SPEAKER_PLAYER: ((0.0, 1, None),),
        })

    # Though for a while, I thought I might have someone to share new memories with. Not to be, it seems...
    d.create_standard_dialog_node(
        though_for_a_while_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [],
        bg3.text_content('h78acffbfgbaa2g4fd9g8f1bgfd0fa7ef98f4', 3),
        end_node = True)
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '8.21',
        though_for_a_while_node_uuid,
        ((None, 'd2ea7696-eded-4662-891e-78c7f1f0fc56'),),
        phase_duration = '8.95',
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 16, None), (2.34, 4, None), (6.31, 32, None)),
            bg3.SPEAKER_PLAYER: ((0.0, 32, None),),
        })

    # And don't worry about me - I'll manage, one way or another. But I'll remember our little moments together fondly - they're amongst the few good memories I can lay claim to.
    d.create_standard_dialog_node(
        dont_worry_about_me_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [],
        bg3.text_content('h2be04f49ga18dg4007gad91gdf626fea1a86', 3),
        end_node = True)
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '13.71',
        dont_worry_about_me_node_uuid,
        ((None, 'd2ea7696-eded-4662-891e-78c7f1f0fc56'),),
        phase_duration = '14.4',
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 4, None), (1.0, 16, None), (2.85, 1024, 2), (5.94, 32, None), (7.12, 64, 2), (10.77, 64, None), (12.59, 2, None)),
            bg3.SPEAKER_PLAYER: ((0.0, 1, None),),
        })

    d.add_root_node(didnt_ask_about_swimming_node_uuid, index = 0)


def allow_character_customizations_in_skinny_dipping_cutscene() -> None:
    ################################################################################################
    # CAMP_Shadowheart_SkinnyDipping_SD_ROM
    ################################################################################################

    ab = game_assets.get_modded_dialog_asset_bundle('CAMP_Shadowheart_SkinnyDipping_SD_ROM')
    d = bg3.dialog_object(ab.dialog)
    t = bg3.timeline_object(ab.timeline, d)

    for effect_component in t.find_effect_components(effect_component_types = 'TLShapeShift', actor = bg3.SPEAKER_SHADOWHEART):
        t.remove_effect_component(effect_component)


bg3.add_build_procedure('patch_act3_romance_conversations', patch_act3_romance_conversations)
bg3.add_build_procedure('patch_skinny_dipping_scene', patch_skinny_dipping_scene)
bg3.add_build_procedure('create_2nd_skinny_dipping_scene', create_2nd_skinny_dipping_scene)
bg3.add_build_procedure('create_act3_breakup_scene', create_act3_breakup_scene)
# bg3.add_build_procedure('allow_character_customizations_in_skinny_dipping_cutscene', allow_character_customizations_in_skinny_dipping_cutscene)

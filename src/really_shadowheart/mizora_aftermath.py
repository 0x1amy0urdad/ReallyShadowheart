from __future__ import annotations

import bg3moddinglib as bg3

from .context import game_assets
from .flags import *

##########################################################################################
# After the night with Mizora
##########################################################################################

def patch_mizora_aftermath_scene() -> None:
    ##########################################################################################
    # Dialog: CAMP_MizoraMorningAfter_CFM_ROM.lsf'
    ##########################################################################################

    # d = bg3.dialog_object(files.get_file('Gustav', 'Mods/GustavDev/Story/DialogsBinary/Camp/Campfire_Moments/CAMP_MizoraMorningAfter_CFM_ROM.lsf'))
    # t = bg3.timeline_object(files.get_file('Gustav', 'Public/GustavDev/Timeline/Generated/CAMP_MizoraMorningAfter_CFM_ROM.lsf'), d)

    ab = game_assets.get_modded_dialog_asset_bundle('CAMP_MizoraMorningAfter_CFM_ROM')
    d = bg3.dialog_object(ab.dialog)
    t = bg3.timeline_object(ab.timeline, d)

    slot_idx_shadowheart = d.get_speaker_slot_index(bg3.SPEAKER_SHADOWHEART)
    slot_idx_tav = d.get_speaker_slot_index(bg3.SPEAKER_PLAYER)

    visual_state_hub_node_uuid = 'e1559f9b-6398-8697-5f45-1e537df5c7bc'
    i_regret_every_moment = '187d15c2-0373-e8a9-99c7-98178864b01f'
    pleasant_evening_i_trust_node_uuid = 'bdcdf773-ea22-ec72-53e1-09e6504948af'
    she_tempted_me_node_uuid = 'f52dcc59-bd36-4572-bd8a-8f2bbe0e1080'
    oh_you_were_tempted_node_uuid = '60d87989-9058-421f-87a6-8989dc5be876'
    you_saw_me_node_uuid = '7af74646-8520-4834-82e5-eb8e854b8272'
    i_hesitated_node_uuid = 'a38a6673-c160-4857-965a-5cbdd25ddac8'
    i_really_fell_for_you_node_uuid = '4413099c-dd54-4b82-b719-564dfc458d55'
    i_admit_it_node_uuid = '09507b62-542a-4e2a-879f-3e13f40afbe2'
    youre_handsome_node_uuid = '679cea8a-14bd-48e7-8852-1d0854a7ca5d'
    youre_pretty_node_uuid = '0124d131-eeb2-423c-919d-3c86ec954428'
    im_not_seeking_to_control_you_node_uuid = '2c756513-a11d-48c5-8fba-60586e2fec0c'
    you_can_do_better_node_uuid = '5d155a9d-7275-419f-9bd1-2e96123cccbe'
    easily_said_by_some_node_uuid = '5dbd4076-3882-47b4-adf1-1a2abb46eeae'
    you_dont_believe_me_node_uuid = '1d1df4e2-c0ec-4e80-822e-d74d4500a495'
    i_do_mean_it_node_uuid = '4f596b9c-7c24-45d5-b81d-a2c4929ae77d'
    opinions_easily_swayed_node_uuid = 'f9a4919a-8253-4ac4-8b22-4ba26e2180eb'
    we_need_allies_node_uuid = 'f8ebd0f6-41d2-40ef-8f16-d56c40722b9e'
    devil_has_our_interests_at_heart_node_uuid = 'f722fc52-eac3-4479-b968-54c4c0b09edd'
    turn_the_page_node_uuid = 'beeaa8a5-6c4b-42a0-8d5e-2ecbf76d4689'
    are_you_sarcastic_node_uuid = 'f6a5b4ed-76a0-4036-b499-882ea39cbe15'
    i_deserve_to_be_hated_node_uuid = 'f9bcd638-f8b9-41f8-add0-43e86189706f'
    dont_be_ridiculous_node_uuid = 'affa609f-9355-4491-841c-1e595db61121'
    what_kind_of_question_node_uuid = 'c9c4082e-a25a-4349-8b55-9abc528fde34'
    i_cant_trust_you_node_uuid = '6f97974f-1eb4-4b09-98e9-8e5c35dde499'
    theres_just_moments_node_uuid = 'dfae2ff2-c989-4701-8923-ca9609ec913f'

    # a template dialog uuid for cloning timeline phases
    shadowheart_answer_node_uuid = 'e8ed0318-95d4-6ab6-c185-5028b16d9b45'

    d.set_dialog_flags(i_regret_every_moment, setflags=(
        bg3.flag_group('Object', (
            bg3.flag(Tav_Regrets_Mizora_Romance.uuid, True, slot_idx_tav),
        )),    
    ))

    # This fixes a bug: Mizora has 2 lines, one per each Shadowheart's path.
    # In original game, Mizora uses Sharran line for Selune Shadowheart, and vice versa.
    # This corrects the flags.
    d.set_dialog_flags('8f60f1d8-0021-20b4-252d-0529ddf3daff', checkflags=(
        bg3.flag_group('Global', (
            bg3.flag(bg3.FLAG_ORI_Shadowheart_State_EnemyOfSharPath, True, None),
        )),
    ))

    d.set_dialog_flags('ed73923b-652a-effe-5682-ef9ec2d3ce8f', checkflags=(
        bg3.flag_group('Global', (
            bg3.flag(bg3.FLAG_ORI_Shadowheart_State_EnemyOfSharPath, False, None),
        )),
    ))

    # This creates a fork: Selunite Shadowheart is very dissappointed, while Sharran Shadowheart retains the "original" behavior
    d.set_dialog_flags(pleasant_evening_i_trust_node_uuid, checkflags=(
        bg3.flag_group('Global', (
            bg3.flag(bg3.FLAG_ORI_State_PartneredWithShadowheart, True, slot_idx_tav),
        )),
        bg3.flag_group('Global', (
            bg3.flag(Shadowheart_Turned_Away_From_Shar.uuid, False, None),
        )),
    ))

    # Changes for Selune path
    selune_pleasant_evening_i_trust_node_uuid = '7f9cdefa-07f0-40a6-b2ec-c32dfca9afe5'

    d.add_child_dialog_node(visual_state_hub_node_uuid, selune_pleasant_evening_i_trust_node_uuid, 0)

    # Pleasant evening, I trust? I tidied up my hair and had an early night... but you don't look like you had much sleep at all.
    d.create_standard_dialog_node(
        selune_pleasant_evening_i_trust_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [she_tempted_me_node_uuid, we_need_allies_node_uuid, i_deserve_to_be_hated_node_uuid],
        bg3.text_content('h87b01e28gd091g42fcg9687gd26699397a2e', 2),
        checkflags=(
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_State_PartneredWithShadowheart, True, slot_idx_tav),
            )),
            bg3.flag_group('Global', (
                bg3.flag(Shadowheart_Turned_Away_From_Shar.uuid, True, None),
            )),
        ))
    t.create_new_voice_phase_from_another(
        pleasant_evening_i_trust_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        '9.71',
        selune_pleasant_evening_i_trust_node_uuid,
        skip_tl_nodes = ('TLShot',),
        phase_duration = '10.0',
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 1024, None), (1.91, 2, None), (6.18, 4, 1), (8.38, 64, None), (9.85, 4, None)),
        },
        attitudes = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_R_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, 3),),
            bg3.SPEAKER_PLAYER: ((0.0, bg3.ATTITUDE_DIAG_Pose_Stand_L_Forward_01, bg3.ATTITUDE_DIAG_T_Pose, 3),)
        })

    comp_cams = ('81b6ede6-3f4b-4caf-910b-3dd142f0b98b', '26949517-f0f4-4689-ae37-b94fe68dfee9', 'd3e056d9-f660-4ab7-b766-6aaff02b7c78')
    t.create_tl_shot('d0630fdf-f2f2-4e18-926b-2cc4a1d78500', '0.0', '9.71', j_cut_length = 1, is_logic_enabled = True, companion_cameras = comp_cams)
    t.create_tl_shot('0a6eee54-6691-4483-87c9-1967d6c72a65', '9.71', '10.0')

    # Listen, Shadowheart. She's a half devil, she charmed me... she tempted me... It meant nothing, I swear.
    d.create_standard_dialog_node(
        she_tempted_me_node_uuid,
        bg3.SPEAKER_PLAYER,
        [oh_you_were_tempted_node_uuid],
        bg3.text_content('hee80ea70g5160g490agac63g98f23b7d0501', 1),
        constructor=bg3.dialog_object.QUESTION)

    # Oh you were tempted, were you? Interesting.
    d.create_standard_dialog_node(
        oh_you_were_tempted_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [you_saw_me_node_uuid, i_admit_it_node_uuid],
        bg3.text_content('h2cf340efg18e8g4923g8282g753fc6e2a8b9', 1))
    t.create_new_voice_phase_from_another(
        shadowheart_answer_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        '4.053',
        oh_you_were_tempted_node_uuid,
        skip_tl_nodes = ('TLShot',),
        phase_duration = '4.5',
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 1, None), (3.5, 1, 3))
        })
    t.create_tl_shot('d0630fdf-f2f2-4e18-926b-2cc4a1d78500', '0.0', '4.2', j_cut_length=1, is_logic_enabled=True, companion_cameras=comp_cams)
    t.create_tl_shot('0a6eee54-6691-4483-87c9-1967d6c72a65', '4.2', '4.5')

    # You saw me with Mizora that evening, did you? Why didn't you talk me out of it?
    d.create_standard_dialog_node(
        you_saw_me_node_uuid,
        bg3.SPEAKER_PLAYER,
        [i_hesitated_node_uuid],
        bg3.text_content('h63ebfa3egc78eg487cga031g3cbc4b395e4a', 1),
        constructor=bg3.dialog_object.QUESTION)

    # I hesitated? Probably because I was coming to realise what a poor match we are for each other.
    d.create_standard_dialog_node(
        i_hesitated_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [theres_just_moments_node_uuid],
        bg3.text_content('h0b36cc12gf68bg4543g91ddg329318005c48', 1))
    t.create_new_voice_phase_from_another(
        shadowheart_answer_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        '6.276',
        i_hesitated_node_uuid,
        skip_tl_nodes = ('TLShot',),
        phase_duration = '7.55',
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 1024, None), (4.35, 1, 3)),
            bg3.SPEAKER_PLAYER: ((0.0, 4, None), (6.6, 2048, None))
        })
    t.create_tl_shot('d0630fdf-f2f2-4e18-926b-2cc4a1d78500', '0.0', '6.3', j_cut_length=1, is_logic_enabled=True, companion_cameras=comp_cams)
    t.create_tl_shot('0a6eee54-6691-4483-87c9-1967d6c72a65', '6.3', '7.55')

    # I admit it, I was a fool and I regret what I've done. You must be hating me, and I absolutely deserve that.
    d.create_standard_dialog_node(
        i_admit_it_node_uuid,
        bg3.SPEAKER_PLAYER,
        [youre_pretty_node_uuid, youre_handsome_node_uuid, easily_said_by_some_node_uuid],
        bg3.text_content('h52c04688gf4a9g4178ga99eg7f58bfe6fae5', 1),
        constructor=bg3.dialog_object.QUESTION)

    # I deserve to be hated for what I did. All I can say, don't leave me... although I cannot give you a reason not to.
    d.create_standard_dialog_node(
        i_deserve_to_be_hated_node_uuid,
        bg3.SPEAKER_PLAYER,
        [youre_pretty_node_uuid, youre_handsome_node_uuid, easily_said_by_some_node_uuid],
        bg3.text_content('hed5250f0g98dag42efga79ag3b0d5fb8f44c', 1),
        constructor=bg3.dialog_object.QUESTION)

    # Don't be foolish - you're far too handsome to hate. I'll still pet you as much as you like.
    d.create_standard_dialog_node(
        youre_handsome_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [im_not_seeking_to_control_you_node_uuid],
        bg3.text_content('h1f7912b4g8b72g46ceg9e8bg8c9874f03472', 1),
        checkflags=(
            bg3.flag_group('Object', (
                bg3.flag(Tav_Regrets_Mizora_Romance.uuid, True, slot_idx_tav),
            )),
        ))
    t.create_new_voice_phase_from_another(
        shadowheart_answer_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        '8.684',
        youre_handsome_node_uuid,
        skip_tl_nodes = ('TLShot',),
        phase_duration = '9.0',
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 1024, None), (3.7, 2, None)),
            bg3.SPEAKER_PLAYER: ((0.0, 1, 3), (6.7, 2, None))
        })
    t.create_tl_shot('d0630fdf-f2f2-4e18-926b-2cc4a1d78500', '0.0', '5.5', j_cut_length=1, is_logic_enabled=True, companion_cameras=comp_cams)
    t.create_tl_shot('0a6eee54-6691-4483-87c9-1967d6c72a65', '5.5', '9.0')

    # Don't be foolish - you're far too pretty to hate. I'll still pet you as much as you like.
    d.create_standard_dialog_node(
        youre_pretty_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [im_not_seeking_to_control_you_node_uuid],
        bg3.text_content('hd9da4525g93d3g45e4g89b1g36bbc09cae31', 1),
        checkflags=(
            bg3.flag_group('Object', (
                bg3.flag(Tav_Regrets_Mizora_Romance.uuid, True, slot_idx_tav),
            )),
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_FEMALE, True, slot_idx_tav),
            )),
        ))
    t.create_new_voice_phase_from_another(
        shadowheart_answer_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        '7.891',
        youre_pretty_node_uuid,
        skip_tl_nodes = ('TLShot',),
        phase_duration = '8.2',
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 1024, None), (3.2, 2, None)),
            bg3.SPEAKER_PLAYER: ((0.0, 1, 3), (6.7, 2, None))
        })
    t.create_tl_shot('d0630fdf-f2f2-4e18-926b-2cc4a1d78500', '0.0', '5.0', j_cut_length=1, is_logic_enabled=True, companion_cameras=comp_cams)
    t.create_tl_shot('0a6eee54-6691-4483-87c9-1967d6c72a65', '5.0', '8.2')

    # I'm not seeking to control you. All I ask is a little... consideration.
    d.create_standard_dialog_node(
        im_not_seeking_to_control_you_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [you_can_do_better_node_uuid],
        bg3.text_content('h30b8b180gcc86g412cg9ff2g37a9462f42bb', 1))
    t.create_new_voice_phase_from_another(
        shadowheart_answer_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        '6.451',
        im_not_seeking_to_control_you_node_uuid,
        skip_tl_nodes = ('TLShot',),
        phase_duration = '6.8',
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 1024, None), (2.065, 1024, 1), (3.7, 1024, 2), (5.4, 1024, 3)),
        })
    t.create_tl_shot('d0630fdf-f2f2-4e18-926b-2cc4a1d78500', '0.0', '6.8', j_cut_length=1, is_logic_enabled=True, companion_cameras=comp_cams)

    # That said, you can certainly do better then her. I should know.
    d.create_standard_dialog_node(
        you_can_do_better_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [],
        bg3.text_content('h4fe9571fg5ee4g42ecg9be5g35bb1571ea9a', 1),
        end_node=True)
    t.create_new_voice_phase_from_another(
        shadowheart_answer_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        '4.9',
        you_can_do_better_node_uuid,
        skip_tl_nodes = ('TLShot',),
        phase_duration = '6.0',
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 1024, None), (3.7, 2, None), (5.2, 2, 2)),
        })
    t.create_tl_shot('d0630fdf-f2f2-4e18-926b-2cc4a1d78500', '0.0', '5.3', j_cut_length=1, is_logic_enabled=True, companion_cameras=comp_cams)

    # That's more easily said by some than others.
    d.create_standard_dialog_node(
        easily_said_by_some_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [you_dont_believe_me_node_uuid, i_do_mean_it_node_uuid],
        bg3.text_content('h67e7aaddgecc5g4a50gb5edg8a0ee697c294', 1),
        checkflags=(
            bg3.flag_group('Object', (
                bg3.flag(Tav_Regrets_Mizora_Romance.uuid, False, slot_idx_tav),
            )),
        ))
    t.create_new_voice_phase_from_another(
        shadowheart_answer_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        '2.392',
        easily_said_by_some_node_uuid,
        skip_tl_nodes = ('TLShot',),
        phase_duration = '3.3',
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 1024, None), (1.7, 1024, 1)),
        })
    t.create_tl_shot('d0630fdf-f2f2-4e18-926b-2cc4a1d78500', '0.0', '2.392')
    t.create_tl_shot('0a6eee54-6691-4483-87c9-1967d6c72a65', '2.392', '3.3')

    # I do mean it. I regret every moment I spent in the Hells with Mizora.
    d.create_standard_dialog_node(
        i_do_mean_it_node_uuid,
        bg3.SPEAKER_PLAYER,
        [opinions_easily_swayed_node_uuid],
        bg3.text_content('hfb28a99dg8cc8g4ad3g879bg6f843e2112d8', 1),
        constructor=bg3.dialog_object.QUESTION)

    # You don't believe me, do you?
    d.create_standard_dialog_node(
        you_dont_believe_me_node_uuid,
        bg3.SPEAKER_PLAYER,
        [opinions_easily_swayed_node_uuid],
        bg3.text_content('hfc18b96ege9ccg484ag946fg3aa2a789e477', 1),
        constructor=bg3.dialog_object.QUESTION)

    # Your opinions are easily swayed. Should I wait for them to change again?
    d.create_standard_dialog_node(
        opinions_easily_swayed_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [theres_just_moments_node_uuid],
        bg3.text_content('h18f5f39dg5473g4079g8077g8d57c8209978', 1))
    t.create_new_voice_phase_from_another(
        shadowheart_answer_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        '4.71',
        opinions_easily_swayed_node_uuid,
        skip_tl_nodes = ('TLShot',),
        phase_duration = '5.5',
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 4, None), (2.72, 4, 2)),
            bg3.SPEAKER_PLAYER: ((0.0, 1, 3), (5.0, 4, 2),)
        })
    t.create_tl_shot('d0630fdf-f2f2-4e18-926b-2cc4a1d78500', '0.0', '2.63')
    t.create_tl_shot('d0630fdf-f2f2-4e18-926b-2cc4a1d78500', '2.63', '4.8', j_cut_length=1, is_logic_enabled=True, companion_cameras=comp_cams)
    t.create_tl_shot('0a6eee54-6691-4483-87c9-1967d6c72a65', '4.8', '5.5')

    # We need allies for the fight to come. I tried to win Mizora's favor. I have no feelings for her.
    d.create_standard_dialog_node(
        we_need_allies_node_uuid,
        bg3.SPEAKER_PLAYER,
        [devil_has_our_interests_at_heart_node_uuid],
        bg3.text_content('h9188942ag8b41g4e68g894ag277ae309838f', 1),
        constructor=bg3.dialog_object.QUESTION)

    # "Perhaps you're right. Perhaps a devil has our best interests at heart and wants nothing in return.
    d.create_standard_dialog_node(
        devil_has_our_interests_at_heart_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [are_you_sarcastic_node_uuid, turn_the_page_node_uuid],
        bg3.text_content('h30e4ed58gc710g43e7g9eb7g5e8d33869649', 1))
    t.create_new_voice_phase_from_another(
        shadowheart_answer_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        '6.426',
        devil_has_our_interests_at_heart_node_uuid,
        skip_tl_nodes = ('TLShot',),
        phase_duration = '6.9',
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 4, None), (2.72, 4, 2)),
            bg3.SPEAKER_PLAYER: ((0.0, 1, 3), (5.0, 4, 2),)
        })
    t.create_tl_shot('d0630fdf-f2f2-4e18-926b-2cc4a1d78500', '0.0', '6.5', j_cut_length=1, is_logic_enabled=True, companion_cameras=comp_cams)
    t.create_tl_shot('0a6eee54-6691-4483-87c9-1967d6c72a65', '6.5', '6.9')

    # If we agree on that, we can turn the page now, shall we?
    d.create_standard_dialog_node(
        turn_the_page_node_uuid,
        bg3.SPEAKER_PLAYER,
        [dont_be_ridiculous_node_uuid],
        bg3.text_content('hbf3e9b58gce14g484bga545g9cfb5645c4cb', 1),
        constructor=bg3.dialog_object.QUESTION)

    # Are you being sarcastic now?
    d.create_standard_dialog_node(
        are_you_sarcastic_node_uuid,
        bg3.SPEAKER_PLAYER,
        [what_kind_of_question_node_uuid],
        bg3.text_content('h757179ffg608bg47e6gaf76gb55db99ca2c8', 1),
        constructor=bg3.dialog_object.QUESTION)

    # What? No, don't be ridiculous.
    d.create_standard_dialog_node(
        dont_be_ridiculous_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [i_cant_trust_you_node_uuid],
        bg3.text_content('hd7eb9710g6c5bg4382gbb6fg711122508d0b', 1))
    t.create_new_voice_phase_from_another(
        shadowheart_answer_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        '2.91',
        dont_be_ridiculous_node_uuid,
        skip_tl_nodes = ('TLShot',),
        phase_duration = '3.3',
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 1, 2), (1.72, 1, 3)),
        })
    t.create_tl_shot('d0630fdf-f2f2-4e18-926b-2cc4a1d78500', '0.0', '3.3')

    # What kind of question is that? Of course I am. Are you?
    d.create_standard_dialog_node(
        what_kind_of_question_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [i_cant_trust_you_node_uuid],
        bg3.text_content('h52f83b1ag8c8bg4561gaefeg1030db3594e3', 1))
    t.create_new_voice_phase_from_another(
        shadowheart_answer_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        '3.65',
        what_kind_of_question_node_uuid,
        skip_tl_nodes = ('TLShot',),
        phase_duration = '3.8',
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 32, None), (2.2, 1, 3)),
        })
    t.create_tl_shot('d0630fdf-f2f2-4e18-926b-2cc4a1d78500', '0.0', '3.8')

    # I can't trust you, can I?
    # You clearly can't be trusted.
    d.create_standard_dialog_node(
        i_cant_trust_you_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [theres_just_moments_node_uuid],
        bg3.text_content('hf13f4035g79ffg46f5g817eg966012bd471c', 1))
        #bg3.text_content('hb4a70fe4ga6b8g449ag9cbbg03f6c252b7fb', 1))
    t.create_new_voice_phase_from_another(
        shadowheart_answer_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        #1.97,
        '2.1',
        i_cant_trust_you_node_uuid,
        skip_tl_nodes = ('TLShot',),
        phase_duration = '5.0',
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 32, 0), (1.22, 2048, 0)),
            bg3.SPEAKER_PLAYER: ((0.0, 1, None), (2.9, 2048, 0))
        },
        attitudes = {
            bg3.SPEAKER_PLAYER: ((2.6, 'fd6ca738-c675-4249-8755-07d0d7027251', bg3.ATTITUDE_DIAG_T_Pose, None),),
        })
    t.create_tl_shot('d0630fdf-f2f2-4e18-926b-2cc4a1d78500', '0.0', '2.5', j_cut_length=1, is_logic_enabled=True, companion_cameras=comp_cams)
    t.create_tl_shot('0a6eee54-6691-4483-87c9-1967d6c72a65', '2.5', '5.0')


    # It's not like I've been keeping a list of charges to throw at you. There's just... moments.
    d.create_standard_dialog_node(
        theres_just_moments_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [i_really_fell_for_you_node_uuid],
        bg3.text_content('h1a0fb4f0g2d87g4c5cgbfd4g455259452c83', 1))
    t.create_new_voice_phase_from_another(
        shadowheart_answer_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        '6.52',
        theres_just_moments_node_uuid,
        skip_tl_nodes = ('TLShot',),
        phase_duration = '7.0',
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 1, 2), (1.72, 1, 3)),
        })
    t.create_tl_shot('d0630fdf-f2f2-4e18-926b-2cc4a1d78500', '0.0', '7.0', j_cut_length=1, is_logic_enabled=True, companion_cameras=comp_cams)


    # I really fell for you, you know. But then... You've changed, and not for the better. I can't be at such odds with you and be your lover. Not anymore.
    d.create_standard_dialog_node(
        i_really_fell_for_you_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [],
        bg3.text_content('h11a84dedgd2cbg46bfg8b92ga6c48d37a486', 1),
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(Shadowheart_Approval_Set_To_Zero.uuid, True, slot_idx_tav),
                bg3.flag(bg3.FLAG_ORI_State_WasPartneredWithShadowheart, True, slot_idx_tav),
                bg3.flag(bg3.FLAG_ORI_State_PartneredWithShadowheart, False, slot_idx_tav),
                bg3.flag(bg3.FLAG_ORI_State_HandledBreakupWithShadowheart, True, slot_idx_tav)
            )),
            bg3.flag_group('Global', (
                bg3.flag(bg3.FLAG_ORI_Shadowheart_State_PostSkinnydipping_Discussed, True, None),
            ))
        ),
        end_node=True)
    t.create_new_voice_phase_from_another(
        shadowheart_answer_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        '13.009',
        i_really_fell_for_you_node_uuid,
        skip_tl_nodes = ('TLShot',),
        phase_duration = '14.0',
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 64, None), (2.91, 32, 1), (6.18, 4, 1), (8.38, 64, None), (9.85, 4, None), (13.0, 2048, 0)),
            bg3.SPEAKER_PLAYER: ((0.0, 1, None), (7.2, 64, None))
        })
    t.create_tl_shot('d0630fdf-f2f2-4e18-926b-2cc4a1d78500', '0.0', '5.37', j_cut_length = 1, is_logic_enabled = True, companion_cameras = comp_cams)
    t.create_tl_shot('0a6eee54-6691-4483-87c9-1967d6c72a65', '5.37', '8.624')
    t.create_tl_shot('d0630fdf-f2f2-4e18-926b-2cc4a1d78500', '8.624', '14.0', j_cut_length = 1, is_logic_enabled = True, companion_cameras = comp_cams)


bg3.add_build_procedure('patch_mizora_aftermath_scene', patch_mizora_aftermath_scene)

from __future__ import annotations

import bg3moddinglib as bg3

from .context import game_assets
from .flags import *

def patch_dapper_drow_intimacy() -> None:
    ##############################################################################################
    # Dialog: WYR_DapperDrow_SiblingsThreeWay.lsf
    ##############################################################################################

    # e808c0d5-8c1a-186b-970f-9b13f49dd02c, hired brother, 1st time
    # a14d0f3c-41fa-b72d-72b3-b44769ba4b30, hired sister, 1st time
    # 580023b9-b5bf-4266-8c75-2a4424d3e761, hired both, 1st time
    # 8d2c44ef-3b93-e385-fde6-dd76d9c78806, hired both, again
    # 2d9df113-4ae2-96dc-f456-5d546a9b0c35, hired sister, again
    # b249b3f2-9427-5e27-57c1-ed9d2e3b6f02, hired brother, again

    # d = bg3.dialog_object(files.get_file('Gustav', 'Mods/GustavDev/Story/DialogsBinary/Act3/Wyrm/WYR_DapperDrow_Intimacy.lsf'))

    ab = game_assets.get_modded_dialog_asset_bundle('WYR_DapperDrow_Intimacy')
    d = bg3.dialog_object(ab.dialog)

    speaker_idx_tav = d.get_speaker_slot_index(bg3.SPEAKER_PLAYER)
    speaker_idx_shadowheart = d.get_speaker_slot_index(bg3.SPEAKER_SHADOWHEART)

    cheated_on_shadowheart_node_uuid = 'd439d6d9-9d2f-4221-8cb4-249f46fc747c'
    not_cheated_on_shadowheart_node_uuid = 'b0a2d593-9588-4602-ae9b-18a3d91d374d'
    end_cinematic_node_uuid = '7146fdf3-2ee8-6e25-8952-22b7e33882cd' # existing node
    
    hired_brother_1st_time_node_uuid = 'e808c0d5-8c1a-186b-970f-9b13f49dd02c'
    hired_sister_1st_time_node_uuid = 'a14d0f3c-41fa-b72d-72b3-b44769ba4b30'
    hired_both_1st_time_node_uuid = '580023b9-b5bf-4266-8c75-2a4424d3e761'
    hired_both_again_node_uuid = '8d2c44ef-3b93-e385-fde6-dd76d9c78806'
    hired_sister_again_node_uuid = '2d9df113-4ae2-96dc-f456-5d546a9b0c35'
    hired_brother_again_node_uuid = 'b249b3f2-9427-5e27-57c1-ed9d2e3b6f02'

    d.remove_dialog_attribute(end_cinematic_node_uuid, "endnode")
    d.add_child_dialog_node(end_cinematic_node_uuid, cheated_on_shadowheart_node_uuid)
    d.add_child_dialog_node(end_cinematic_node_uuid, not_cheated_on_shadowheart_node_uuid)

    d.create_standard_dialog_node(
        cheated_on_shadowheart_node_uuid,
        bg3.SPEAKER_PLAYER,
        [],
        None,
        constructor = bg3.dialog_object.ANSWER,
        end_node = True,
        checkflags = (
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_REALLY_SHADOWHEART, False, speaker_idx_shadowheart),
            )),
            bg3.flag_group('Global', (
                bg3.flag(Shadowheart_Turned_Away_From_Shar.uuid, True, None),
            ))
        ),
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(Cheated_On_Shadowheart.uuid, True, speaker_idx_tav),
                bg3.flag(Shadowheart_Has_Doubts_About_Tav.uuid, True, speaker_idx_tav)
            )),
        ))
    d.create_standard_dialog_node(
        not_cheated_on_shadowheart_node_uuid,
        bg3.SPEAKER_PLAYER,
        [],
        None,
        constructor = bg3.dialog_object.ANSWER,
        end_node = True)


def patch_sharess_caress() -> None:
    ##############################################################################################
    # Dialog: WYR_DapperDrow_SiblingsThreeWay.lsf
    ##############################################################################################

    # d = bg3.dialog_object(files.get_file('Gustav', 'Mods/GustavDev/Story/DialogsBinary/Act3/Wyrm/WYR_DapperDrow_SiblingsThreeWay.lsf'))
    # t = bg3.timeline_object(files.get_file('Gustav', 'Public/GustavDev/Timeline/Generated/WYR_DapperDrow_SiblingsThreeWay.lsf'), d)

    ab = game_assets.get_modded_dialog_asset_bundle('WYR_DapperDrow_SiblingsThreeWay')
    d = bg3.dialog_object(ab.dialog)
    t = bg3.timeline_object(ab.timeline, d)

    # speaker slot indexes
    slot_idx_shadowheart = d.get_speaker_slot_index(bg3.SPEAKER_SHADOWHEART)
    slot_idx_tav = d.get_speaker_slot_index(bg3.SPEAKER_PLAYER)
    slot_idx_the_creep = d.get_speaker_slot_index(bg3.SPEAKER_HALSIN)

    # flags
    # shadowheart_enemy_of_shar_true = bg3.flag_group('Global', (bg3.flag(Shadowheart_Turned_Away_From_Shar.uuid, True, None),))
    # shadowheart_chosen_of_shar_true = bg3.flag_group('Global', (bg3.flag(Shadowheart_Turned_Away_From_Shar.uuid, False, None),))
    # tav_partnered_true = bg3.flag_group('Object', (bg3.flag(bg3.FLAG_ORI_State_PartneredWithShadowheart, True, slot_idx_tav),))
    # tav_partnered_false = bg3.flag_group('Object', (bg3.flag(bg3.FLAG_ORI_State_PartneredWithShadowheart, False, slot_idx_tav),))
    # tav_brokenup_true = bg3.flag_group('Object', (bg3.flag(bg3.FLAG_ORI_State_WasPartneredWithShadowheart, True, slot_idx_tav),))
    # skinny_dipping_discussion_happened_true = bg3.flag_group('Global', (bg3.flag(bg3.FLAG_ORI_Shadowheart_State_PostSkinnydipping_Discussed, True, None),))
    # handled_breakup_true = bg3.flag_group('Object', (bg3.flag(bg3.FLAG_ORI_State_HandledBreakupWithShadowheart, True, slot_idx_tav),))
    # really_shadowheart_true = bg3.flag_group('Tag', (bg3.flag(bg3.TAG_REALLY_SHADOWHEART, True, slot_idx_shadowheart),))
    # shadowheart_goes_to_camp = bg3.flag_group('Object', (bg3.flag(bg3.FLAG_OriginRemoveFromPartyAfterDialog, True, slot_idx_shadowheart),))
    # tav_promise_true = bg3.flag_group('Object', (bg3.flag(Shadowheart_State_DontHireDapperDrowPromise.uuid, True, slot_idx_shadowheart),))
    # tav_promise_false = bg3.flag_group('Object', (bg3.flag(Shadowheart_State_DontHireDapperDrowPromise.uuid, False, slot_idx_shadowheart),))
    # tav_rejected_drow_3some_true = bg3.flag_group('Object', (bg3.flag(Shadowheart_State_RejectedDapperDrow3some.uuid, True, slot_idx_tav),))
    # tav_rejected_drow_3some_false = bg3.flag_group('Object', (bg3.flag(Shadowheart_State_RejectedDapperDrow3some.uuid, False, slot_idx_tav),))
    # tav_rejected_drow_true = bg3.flag_group('Object', (bg3.flag(Shadowheart_State_RejectedDapperDrow.uuid, True, slot_idx_tav),))
    # tav_rejected_drow_false = bg3.flag_group('Object', (bg3.flag(Shadowheart_State_RejectedDapperDrow.uuid, False, slot_idx_tav),))

    # dialog uuids, existing dialogs
    drow_question_bank_node_uuid = 'cb85e926-5003-ebf4-cc84-c661c0cf8c9c' # All questions are here
    id_like_you_all_to_myself_node_uuid = '42eabadc-bf51-6129-f4f7-e79718020fef'
    theres_an_idea_node_uuid = '4d6c4b25-54b3-d965-9b1d-4240b4d32c09'
    should_i_be_jelous_node_uuid = 'b7f42923-a360-e758-3504-43b90a2354de'
    i_feel_the_same_way_node_uuid = '37e7cf82-ed52-4b7d-b903-38237b6ab604'
    forget_i_said_node_uuid = '0b4912e4-fd26-7785-6e7a-ce1852138fb0'
    id_like_to_hire_both_node_uuid = '650c0d75-3e1a-06f2-63c1-09f4554b4adb'
    id_like_to_hire_my_lady_node_uuid = '49b95aec-c693-2332-1874-9aa1a65d37f4'
    i_want_to_hire_lad_node_uuid = '18138b2a-618f-28dc-7b62-90a7dfb46135'
    id_like_to_spend_time_lady_nym_node_uuid = 'fccddc42-f0a1-e4e0-18d2-4e2c68dbdd0a'
    halsin_interjection_node_uuid = 'be20dd65-bb29-9f58-1295-eb25179240b1'
    partner_reaction_hub_node_uuid = '8c62a0da-1341-e527-91d9-9fe9a960cd47'

    a_shame_but_either_node_uuid = '926123a4-a4ca-73b3-d10c-0575f89cd0d1'
    this_is_not_for_me_node_uuid = 'bd187d1e-469f-3844-3c4b-7041d1cbbf78'
    sorry_friend_node_uuid = 'a9c3b863-8f18-1009-8b39-9abfd2384220'

    #dialog uuids, new dialogs
    you_two_are_clueless_node_uuid = '20db1d33-7368-49c1-9ff0-b2fab43531bf'
    drows_were_rejected_node_uuid = 'a0bc6155-35b3-4d80-8f34-31144ea1be21'
    drows_reaction_jump_node_uuid = '76890f9d-2e58-4b66-b7d6-2f93723c8ec4'
    entry_point_node_uuid = '1248ea3a-a035-4944-80f2-b4d3a3752486'
    just_like_that_node_uuid = '1f836a58-db44-4b04-8f97-6a9a0361324a'
    deception_node_uuid = '20ae75a9-5abd-4b10-b233-3e867dbaf39d'
    persuasion_node_uuid = '2bd1be3b-7b34-4ef1-96e6-58a6813cf153'
    lets_drop_this_node_uuid = '7d411d40-89d2-4e4d-b773-8a6c05a22016'
    cut_you_loose_node_uuid = 'aa037df5-0825-4f52-8cbf-6783c29df1f3'
    dont_do_this_again_node_uuid = '5a598edd-3495-4240-84c7-3e2178f698a0'
    bad_liar_node_uuid = '91265082-8a28-4233-b22b-654c2a7656d6'
    best_leave_me_alone_node_uuid = 'f2e1df94-dc62-4981-849c-53bf84eed103'
    now_leave_me_alone_node_uuid = '194e0965-3a7a-4238-b2eb-e5e403e8a4c5'
    your_affections_drifted_node_uuid = '3258a7bb-a84a-44d9-be22-116089156432'
    i_am_free_node_uuid = '9fb11096-33d8-4c30-9eef-3fe7b142b46f'
    i_dont_want_to_lose_you_node_uuid = '56ba2b98-5d0a-4dbe-b5e4-081c85f5bd2c'
    better_if_we_were_friends_node_uuid = '3c5709f2-2586-49c8-b75b-d6cd97572db5'
    your_new_beau_node_uuid = '35a4a0c9-74c6-4f28-befd-686e3eaec7fb'
    spare_lover_node_uuid = '1bdb3c57-d180-47d1-8eb0-23c5cf08f0cc'
    way_to_end_things_node_uuid = '4b9bf0a2-4058-4a7e-8b6b-9649990fc814'
    what_do_you_mean_node_uuid = '7f30d6cf-1481-4db1-8510-3435005813b9'
    #arent_dear_friends_uuid = 'ceacb4b7-6db1-4952-8a00-e4fad3ec0e78'
    i_dont_have_to_explain_node_uuid = '91f4387b-9b01-491a-8a18-390143bc55cd'

    # Negative impact to approval rating
    #set_zero_approval_true = bg3.flag_group('Object', (bg3.flag(Shadowheart_Approval_Set_To_Zero.uuid, True, slot_idx_tav),))
    #set_neutral_approval_true = bg3.flag_group('Object', (bg3.flag(Shadowheart_Approval_Set_To_Neutral.uuid, True, slot_idx_tav),))
    #set_low_approval_true = bg3.flag_group('Object', (bg3.flag(Shadowheart_Approval_Set_To_Low.uuid, True, slot_idx_tav),))
    #set_very_low_approval_true = bg3.flag_group('Object', (bg3.flag(Shadowheart_Approval_Set_To_VeryLow.uuid, True, slot_idx_tav),))


    # Camera that looks at Shadowheart
    def create_shadowheart_tl_shot(tl_obj: bg3.timeline_object, start: str | bg3.dc.Decimal, end: str | bg3.dc.Decimal) -> None:
        tl_obj.create_tl_shot(
            '959c765e-cc11-4861-ba1c-ab711f1bffb2',
            start,
            end,
            is_snapped_to_end=True,
            is_logic_enabled=True,
            j_cut_length=1,
            companion_cameras=('81b6ede6-3f4b-4caf-910b-3dd142f0b98b', '26949517-f0f4-4689-ae37-b94fe68dfee9', 'd3e056d9-f660-4ab7-b766-6aaff02b7c78'))

    # This prevents Halsin's "more company" line in the drow siblings convo if Tav didn't start a secondary relationship with him.
    d.set_dialog_flags(halsin_interjection_node_uuid, checkflags = (
        bg3.flag_group('Tag', (
            bg3.flag(bg3.TAG_REALLY_HALSIN, True, slot_idx_the_creep),
        )),
        bg3.flag_group('Object', (
            bg3.flag(bg3.FLAG_ORI_State_PartneredWithHalsinSecondary, True, slot_idx_tav),
        )),
    ))

    # Selune Shadowheart always rejects 3some with drows

    # While it's a fascinating prospect, I'd like you all to myself...
    d.set_dialog_flags(id_like_you_all_to_myself_node_uuid, checkflags = (
        bg3.flag_group('Global', (
            bg3.flag(Shadowheart_Turned_Away_From_Shar.uuid, True, None),
        )),
        bg3.flag_group('Object', (
            bg3.flag(bg3.FLAG_ORI_State_PartneredWithShadowheart, True, slot_idx_tav),
        ))
    ))
    d.set_tagged_text(id_like_you_all_to_myself_node_uuid, bg3.text_content('h7b905a4fgda7dg4417g9c24g768f4ef486e4', 1))

    # Timeline: re-use the existing one, but change it a bit
    tl_shot = t.find_effect_component('d482b324-2af0-4148-9588-5c0430bce81a')
    end_time = float(bg3.get_required_bg3_attribute(tl_shot, 'EndTime'))
    end_time -= 1.7
    bg3.set_bg3_attribute(tl_shot, 'EndTime', str(end_time))
    tl_shot = t.find_effect_component('92581c30-236e-4cf8-94c0-98a20b45607f')
    bg3.set_bg3_attribute(tl_shot, 'StartTime', str(end_time))
    
    # Change camera: this camera looks at Nym, attached to Tav
    nym_cam = tl_shot.find("./children/node[@id='CameraContainer']")
    if nym_cam is None:
        raise RuntimeError('Malformed TLShot element')
    bg3.set_bg3_attribute(nym_cam, 'Object', '36b8f8c0-fb65-4088-8c56-aa911e642c5e')

    # Make Tav appear when camera switched back to Nym
    tl_show_visual = t.find_effect_component('b4bab808-d053-4bfc-8b2e-c77b1c46bdba')
    tl_show_visual_keys = tl_show_visual.findall('./children/node[@id="Keys"]/children/node[@id="Key"]')
    bg3.set_bg3_attribute(tl_show_visual_keys[1], 'Time', str(end_time))

    
    # Definitely, this isn't my cup of tea. You do you, and I go my way. Bye.
    everyone_but_creep = bg3.reaction_object.create_new(game_assets.files, {
        bg3.SPEAKER_SHADOWHEART: 1,
        bg3.SPEAKER_LAEZEL: 1,
        bg3.SPEAKER_KARLACH: 1,
        bg3.SPEAKER_GALE: 1,
        bg3.SPEAKER_WYLL: 1,
        bg3.SPEAKER_MINTHARA: 1,
        bg3.SPEAKER_ASTARION: 1,
        bg3.SPEAKER_MINSC: 1,
        bg3.SPEAKER_JAHEIRA: 1,
        bg3.SPEAKER_HALSIN: -5
    })
    d.create_standard_dialog_node(
        you_two_are_clueless_node_uuid,
        bg3.SPEAKER_PLAYER,
        [drows_reaction_jump_node_uuid],
        bg3.text_content('h8fd76834gff47g46a1ga97dgb43e95aa6962', 1),
        constructor = bg3.dialog_object.QUESTION,
        approval_rating_uuid = everyone_but_creep.uuid,
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(Shadowheart_State_RejectedDapperDrow3some.uuid, True, slot_idx_tav),
                bg3.flag(Shadowheart_State_RejectedDapperDrow.uuid, True, slot_idx_tav),
            )),
        ))
    d.create_jump_dialog_node(drows_reaction_jump_node_uuid, a_shame_but_either_node_uuid, 1)
    d.add_child_dialog_node(drow_question_bank_node_uuid, you_two_are_clueless_node_uuid, 0)

    # This is not for me.
    d.set_dialog_flags(this_is_not_for_me_node_uuid, setflags = (
        bg3.flag_group('Object', (
            bg3.flag(Shadowheart_State_RejectedDapperDrow3some.uuid, True, slot_idx_tav),
            bg3.flag(Shadowheart_State_RejectedDapperDrow.uuid, True, slot_idx_tav),
        )),
    ))

    # If drows were rejected, cut the whole conversation very short.
    d.create_alias_dialog_node(
        drows_were_rejected_node_uuid,
        sorry_friend_node_uuid,
        [],
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(Shadowheart_State_RejectedDapperDrow3some.uuid, True, slot_idx_tav),
                bg3.flag(Shadowheart_State_RejectedDapperDrow.uuid, True, slot_idx_tav),
            )),
        ),
        end_node = True)
    d.add_root_node(drows_were_rejected_node_uuid, index = 0)


    # Block the 3some option after the conversation
    d.set_dialog_flags(i_feel_the_same_way_node_uuid, setflags = (
        bg3.flag_group('Object', (
            bg3.flag(Shadowheart_State_RejectedDapperDrow3some.uuid, True, slot_idx_tav),
        )),
    ))
    d.set_dialog_flags(forget_i_said_node_uuid, setflags = (
        bg3.flag_group('Object', (
            bg3.flag(Shadowheart_State_RejectedDapperDrow3some.uuid, True, slot_idx_tav),
        )),
    ))

    # Allow hiring drow twins only if Tav didn't reject this idea
    d.set_dialog_flags(id_like_to_hire_both_node_uuid, checkflags = (
        bg3.flag_group('Object', (bg3.flag(Shadowheart_State_RejectedDapperDrow3some.uuid, False, slot_idx_tav),)),
    ))
    d.set_dialog_flags(id_like_to_hire_my_lady_node_uuid, checkflags = (
        bg3.flag_group('Object', (
            bg3.flag(Shadowheart_State_RejectedDapperDrow.uuid, False, slot_idx_tav),
        )),
    ))
    d.set_dialog_flags(i_want_to_hire_lad_node_uuid, checkflags = (
        bg3.flag_group('Object', (
            bg3.flag(Shadowheart_State_RejectedDapperDrow.uuid, False, slot_idx_tav),
        )),
    ))
    d.set_dialog_flags(id_like_to_spend_time_lady_nym_node_uuid, checkflags = (
        bg3.flag_group('Object', (
            bg3.flag(Shadowheart_State_RejectedDapperDrow.uuid, False, slot_idx_tav),
        )),
    ))

    # Shar Shadowheart always agrees to 3some with drows
    d.set_dialog_flags(theres_an_idea_node_uuid, checkflags = (
        bg3.flag_group('Global', (
            bg3.flag(Shadowheart_Turned_Away_From_Shar.uuid, False, None),
        )),
        bg3.flag_group('Object', (
            bg3.flag(bg3.FLAG_ORI_State_PartneredWithShadowheart, True, slot_idx_tav),
        ))
    ))

    # Shar Shadowheart doesn't mind Tav hiring drows without her
    d.set_dialog_flags(should_i_be_jelous_node_uuid, checkflags = (
        bg3.flag_group('Global', (
            bg3.flag(Shadowheart_Turned_Away_From_Shar.uuid, False, None),
        )),
        bg3.flag_group('Object', (
            bg3.flag(bg3.FLAG_ORI_State_PartneredWithShadowheart, True, slot_idx_tav),
        ))
    ))

    # Partners always react to hiring drow twins
    d.remove_dialog_attribute(partner_reaction_hub_node_uuid, 'transitionmode')
    #d.set_dialog_flags(partner_reaction_hub_node_uuid, checkflags=())

    # Put the entry point node into the conversation
    d.delete_child_dialog_node(partner_reaction_hub_node_uuid, should_i_be_jelous_node_uuid)
    d.add_child_dialog_node(partner_reaction_hub_node_uuid, entry_point_node_uuid, 0)

    # Entry point: a 3 way fork 
    d.create_standard_dialog_node(
        entry_point_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [
            just_like_that_node_uuid,
            your_affections_drifted_node_uuid,
            should_i_be_jelous_node_uuid],
        None,
        checkflags = (
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_REALLY_SHADOWHEART, True, slot_idx_shadowheart),
            )),
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_State_PartneredWithShadowheart, True, slot_idx_tav),
            ))
        ))

    # Just like that...? I thought we had something special. Something lasting.
    d.create_standard_dialog_node(
        just_like_that_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [deception_node_uuid, persuasion_node_uuid, lets_drop_this_node_uuid],
        bg3.text_content('h656ea716g6c7fg4810g9a40g7a4faf11bd91', 1),
        checkflags = (
            bg3.flag_group('Global', (
                bg3.flag(Shadowheart_Turned_Away_From_Shar.uuid, True, None),
            )),
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_State_PartneredWithShadowheart, True, slot_idx_tav),
                bg3.flag(Shadowheart_State_DontHireDapperDrowPromise.uuid, False, slot_idx_shadowheart),
            )),
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_REALLY_SHADOWHEART, True, slot_idx_shadowheart),
            )),
        ))
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '6.75',
        just_like_that_node_uuid,
        (),
        phase_duration = '7.05',
        look_at_player = bg3.SPEAKER_NYM_ORLYTH,
        emotions={
            bg3.SPEAKER_SHADOWHEART: ((0.0, 16, 1), (2.78, 16, 2), (4.33, 32, None), (5.91, 2048, None)),
            bg3.SPEAKER_PLAYER: ((0.0, 64, None),)
        })
    create_shadowheart_tl_shot(t, '0.0', '6.75')
    t.create_tl_shot('3b786a1e-3d4d-4d02-960f-8dd34901f1ec', '6.75', '7.05', is_snapped_to_end=True)

    # Forget I said anything. Let's drop this.
    d.create_standard_dialog_node(
        lets_drop_this_node_uuid,
        bg3.SPEAKER_PLAYER,
        [cut_you_loose_node_uuid],
        bg3.text_content('hfd18944dg9b68g4093ga62bg4718589a098a', 1),
        constructor = bg3.dialog_object.QUESTION,
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(Shadowheart_State_RejectedDapperDrow.uuid, True, slot_idx_tav),
            )),
        ))

    # Fine. But understand that I'll cut you loose the moment I have to.
    d.create_standard_dialog_node(
        cut_you_loose_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [],
        bg3.text_content('ha090154fg5825g4e2bg8e91g6f160fa5e992', 1),
        setflags=(
            bg3.flag_group('Object', (
                bg3.flag(Shadowheart_State_DontHireDapperDrowPromise.uuid, True, slot_idx_shadowheart),
            )),
        ),
        end_node=True)
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '3.97',
        cut_you_loose_node_uuid,
        (),
        look_at_player = bg3.SPEAKER_NYM_ORLYTH,
        emotions={
            bg3.SPEAKER_SHADOWHEART: ((0.12, 8, None), (1.5, 64, None), (3.26, 4, None)),
        })
    create_shadowheart_tl_shot(t, '0.0', '3.97')

    # I'm just trying to get you jealous, my love.
    d.create_roll_dialog_node(
        deception_node_uuid,
        bg3.SPEAKER_PLAYER,
        bg3.SPEAKER_SHADOWHEART,
        bg3.dialog_object.ABILITY_WISDOM,
        bg3.dialog_object.SKILL_DECEPTION,
        bg3.DC_Act3_Hard,
        dont_do_this_again_node_uuid,
        bad_liar_node_uuid,
        bg3.text_content('h5def25a4gf970g4dadgbb68gec13e203facc', 1))

    # At least you're honest. Don't do that again.
    d.create_standard_dialog_node(
        dont_do_this_again_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [],
        bg3.text_content('h6f3bfd2agf0d5g4e74g9420g1e59d78b5047', 1),
        setflags=(
            bg3.flag_group('Object', (
                bg3.flag(Shadowheart_State_DontHireDapperDrowPromise.uuid, True, slot_idx_shadowheart),
            )),
        ),
        end_node=True)
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '3.11',
        dont_do_this_again_node_uuid,
        (),
        look_at_player = bg3.SPEAKER_NYM_ORLYTH,
        emotions={
            bg3.SPEAKER_SHADOWHEART: ((0.0, 64, None), (0.65, 4, None), (1.79, 128, 1)),
        })
    create_shadowheart_tl_shot(t, '0.0', '3.11')

    # You're a bad liar... Don't treat me like an idiot, please!
    d.create_standard_dialog_node(
        bad_liar_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [best_leave_me_alone_node_uuid],
        bg3.text_content('hd86ce9a8g7a59g49ddgad72g6f87d1c370dd', 1),
        setflags=(
            bg3.flag_group('Object', (
                bg3.flag(Shadowheart_State_DontHireDapperDrowPromise.uuid, True, slot_idx_shadowheart),
                bg3.flag(Shadowheart_Approval_Set_To_Zero.uuid, True, slot_idx_tav),
            )),
        ))
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '5.338',
        bad_liar_node_uuid,
        (),
        emotions={
            bg3.SPEAKER_SHADOWHEART: ((0.0, 128, 1), (3.1, 32, None), (4.2, 2048, None)),
            bg3.SPEAKER_PLAYER: ((0.0, 128, None), (4.0, 64, 2))
        },
        phase_duration = '6.0',
        look_at_player = bg3.SPEAKER_NYM_ORLYTH)
    create_shadowheart_tl_shot(t, '0.0', '3.538')
    t.create_tl_shot('318bfab8-282a-47ed-abdc-78184e7a6c30', '3.538', '5.338', is_snapped_to_end=True)

    # Best if you leave me alone, for now.
    d.create_standard_dialog_node(
        best_leave_me_alone_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [],
        bg3.text_content('hb7c3b03bg7d22g41dag989dgae8d9c2223f4', 1),
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(Shadowheart_Has_Doubts_About_Tav.uuid, True, slot_idx_tav),
                bg3.flag(bg3.FLAG_OriginRemoveFromPartyAfterDialog, True, slot_idx_shadowheart),
            )),
        ),
        end_node=True)
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '3.54',
        best_leave_me_alone_node_uuid,
        (),
        look_at_player = bg3.SPEAKER_NYM_ORLYTH,
        emotions={
            bg3.SPEAKER_SHADOWHEART: ((0.0, 8, None), (2.2, 128, 1)),
        })
    create_shadowheart_tl_shot(t, '0.0', '3.54')

    # Surely you wouldn't mind if I had a bit of fun? I am my own person, after all.
    d.create_roll_dialog_node(
        persuasion_node_uuid,
        bg3.SPEAKER_PLAYER,
        bg3.SPEAKER_SHADOWHEART,
        bg3.dialog_object.ABILITY_CHARISMA,
        bg3.dialog_object.SKILL_PERSUASION,
        bg3.DC_Act3_Hard,
        spare_lover_node_uuid,
        way_to_end_things_node_uuid,
        bg3.text_content('h9a474f8dg36b3g4089gbf4aga01c55224234', 1))

    # In truth, I don't think I'd want to be your spare lover. I'd always want more of you than you'd have to spare. Better perhaps to bow out with dignity.
    d.create_standard_dialog_node(
        spare_lover_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [better_if_we_were_friends_node_uuid, i_dont_want_to_lose_you_node_uuid],
        bg3.text_content('hd3fd298bgb472g4e8bg8e74gaceeb20de6e1', 3),
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_State_PartneredWithShadowheart, False, slot_idx_tav),
                bg3.flag(bg3.FLAG_ORI_State_WasPartneredWithShadowheart, True, slot_idx_tav),
                bg3.flag(bg3.FLAG_ORI_State_HandledBreakupWithShadowheart, True, slot_idx_tav),
            )),
            bg3.flag_group('Global', (
                bg3.flag(bg3.FLAG_ORI_Shadowheart_State_PostSkinnydipping_Discussed, True, None),
            )),
        ))
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '13.06',
        spare_lover_node_uuid,
        (),
        emotions={
            bg3.SPEAKER_SHADOWHEART: ((0.0, 4, None), (1.82, 16, None), (3.56, 64, None), (5.29, 64, 1), (8.9, 1024, 2), (11.0, 64, None), (11.8, 2, None)),
            bg3.SPEAKER_PLAYER: ((0.0, 64, 1),)
        },
        phase_duration = '13.56',
        look_at_player = bg3.SPEAKER_NYM_ORLYTH)
    create_shadowheart_tl_shot(t, '0.0', '13.06')
    t.create_tl_shot('318bfab8-282a-47ed-abdc-78184e7a6c30', '13.06', '13.506', is_snapped_to_end=True)

    # Well that's one way to end things.
    d.create_standard_dialog_node(
        way_to_end_things_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [what_do_you_mean_node_uuid, i_am_free_node_uuid],
        bg3.text_content('h80ce62e6g2315g4255g902fg75e92b696ee3', 3),
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(Shadowheart_Approval_Set_To_Zero.uuid, True, slot_idx_tav),
                bg3.flag(bg3.FLAG_ORI_State_PartneredWithShadowheart, False, slot_idx_tav),
                bg3.flag(bg3.FLAG_ORI_State_WasPartneredWithShadowheart, True, slot_idx_tav),
            )),
            bg3.flag_group('Global', (
                bg3.flag(bg3.FLAG_ORI_Shadowheart_State_PostSkinnydipping_Discussed, True, None),
            )),
        ))
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '5.29',
        way_to_end_things_node_uuid,
        (),
        emotions={
            bg3.SPEAKER_SHADOWHEART: ((0.0, 16, None), (2.14, 4, 2), (3.35, 64, None), (4.01, 128, None)),
            bg3.SPEAKER_PLAYER: ((0.0, 64, 2),)
        },
        phase_duration = '5.79',
        look_at_player = bg3.SPEAKER_NYM_ORLYTH)
    create_shadowheart_tl_shot(t, '0.0', '5.29')
    t.create_tl_shot('318bfab8-282a-47ed-abdc-78184e7a6c30', '5.29', '5.79', is_snapped_to_end=True)

    # Wait, I don't want to lose you... I want to be with you...
    d.create_standard_dialog_node(
        i_dont_want_to_lose_you_node_uuid,
        bg3.SPEAKER_PLAYER,
        [your_new_beau_node_uuid],
        bg3.text_content('h4e692070gf12fg40e1g9b36ge64802670e20', 1),
        constructor = bg3.dialog_object.QUESTION,
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_State_PartneredWithShadowheart, False, slot_idx_tav),
                bg3.flag(bg3.FLAG_ORI_State_WasPartneredWithShadowheart, True, slot_idx_tav),
            )),
            bg3.flag_group('Global', (
                bg3.flag(bg3.FLAG_ORI_Shadowheart_State_PostSkinnydipping_Discussed, True, None),
            ))
        ))

    # Perhaps, you're right. It would be better for us if we were friends.
    d.create_standard_dialog_node(
        better_if_we_were_friends_node_uuid,
        bg3.SPEAKER_PLAYER,
        [best_leave_me_alone_node_uuid],
        bg3.text_content('h5de64a8eg404fg4151ga564g5956eab0a0f4', 1),
        constructor = bg3.dialog_object.QUESTION,
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_State_PartneredWithShadowheart, False, slot_idx_tav),
                bg3.flag(bg3.FLAG_ORI_State_WasPartneredWithShadowheart, True, slot_idx_tav),
            )),
            bg3.flag_group('Global', (
                bg3.flag(bg3.FLAG_ORI_Shadowheart_State_PostSkinnydipping_Discussed, True, None),
            ))
        ))

    # I am free to do whatever I want. Leave, if you have a problem with that.
    d.create_standard_dialog_node(
        i_am_free_node_uuid,
        bg3.SPEAKER_PLAYER,
        [now_leave_me_alone_node_uuid],
        bg3.text_content('hf070d2bag8b3cg4918ga17dg7f009caa75dc', 1),
        constructor = bg3.dialog_object.QUESTION,
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_State_PartneredWithShadowheart, False, slot_idx_tav),
                bg3.flag(bg3.FLAG_ORI_State_WasPartneredWithShadowheart, True, slot_idx_tav),
            )),
            bg3.flag_group('Global', (
                bg3.flag(bg3.FLAG_ORI_Shadowheart_State_PostSkinnydipping_Discussed, True, None),
            ))
        ))

    # What do you mean?
    d.create_standard_dialog_node(
        what_do_you_mean_node_uuid,
        bg3.SPEAKER_PLAYER,
        [i_dont_have_to_explain_node_uuid],
        bg3.text_content('h6d9862b7g728fg4822ga5f3g658e9bfc16d3', 1),
        constructor=bg3.dialog_object.QUESTION)

    # Oh don't be like that - you've made your bed, now go roll around in it with your new beau.
    d.create_standard_dialog_node(
        your_new_beau_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [],
        bg3.text_content('h45bb0963g86ccg4633gb227gb944064b9b0d', 3),
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_OriginRemoveFromPartyAfterDialog, True, slot_idx_shadowheart),
            )),
        ),
        end_node = True)
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '7.0',
        your_new_beau_node_uuid,
        (),
        look_at_player = bg3.SPEAKER_NYM_ORLYTH,
        emotions={
            bg3.SPEAKER_SHADOWHEART: ((0.0, 128, 1), (2.5, 16, None), (4.11, 1024, None), (6.2, 64, None))
        })
    create_shadowheart_tl_shot(t, '0.0', '7.0')

    # # Unused dialog node
    # # We aren't dear friends now, if that's what you're asking.
    # d.create_standard_dialog_node(
    #     arent_dear_friends_uuid,
    #     bg3.SPEAKER_SHADOWHEART,
    #     [best_leave_me_alone_uuid],
    #     bg3.text_content('hd08cebbdgc4acg409ag92a9gcaddaec78634', 1))
    # t.create_simple_dialog_answer_phase(
    #     bg3.SPEAKER_SHADOWHEART,
    #     '3.0',
    #     arent_dear_friends_uuid,
    #     (),
    #     emotions={
    #         bg3.SPEAKER_SHADOWHEART: ((0.0, 1024, None), (1.5, 4, None)),
    #         bg3.SPEAKER_PLAYER: ((3.3, 64, 2),)
    #     },
    #     phase_duration = '4.2')
    # create_shadowheart_tl_shot(t, '0.0', '3.0')
    # t.create_tl_shot('b6e5d011-7375-4baf-8c02-942f716ee78c', '3.0', '4.2', is_snapped_to_end=True)

    # I don't have to explain myself to you.
    d.create_standard_dialog_node(
        i_dont_have_to_explain_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [best_leave_me_alone_node_uuid],
        bg3.text_content('hee549e4ag5e19g41c5gb7d8g1ba58eb2d7b8', 1))
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '2.61',
        i_dont_have_to_explain_node_uuid,
        (),
        emotions={
            bg3.SPEAKER_SHADOWHEART: ((0.0, 1024, None), (1.5, 4, None)),
            bg3.SPEAKER_PLAYER: ((3.3, 64, 2),)
        },
        look_at_player = bg3.SPEAKER_NYM_ORLYTH,
        phase_duration = '3.2')
    create_shadowheart_tl_shot(t, '0.0', '2.7')
    t.create_tl_shot('b6e5d011-7375-4baf-8c02-942f716ee78c', '2.7', '3.2', is_snapped_to_end=True)

    # Now leave me alone.
    d.create_standard_dialog_node(
        now_leave_me_alone_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [],
        bg3.text_content('habcc14b2g5065g4b7dg8f22gc39494c34f5e', 1),
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_OriginRemoveFromPartyAfterDialog, True, slot_idx_shadowheart),
            )),
        ),
        end_node = True)
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '2.53',
        now_leave_me_alone_node_uuid,
        (),
        emotions={
            bg3.SPEAKER_SHADOWHEART: ((0.0, 8, None),)
        },
        look_at_player = bg3.SPEAKER_NYM_ORLYTH,
        phase_duration = '3.0')
    create_shadowheart_tl_shot(t, '0.0', '3.0')

    # So... I gather your affections have drifted elsewhere. Curious.
    d.create_standard_dialog_node(
        your_affections_drifted_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [i_am_free_node_uuid, i_dont_want_to_lose_you_node_uuid],
        bg3.text_content('h888d9f87g4fddg4df6g83c4g9e7307f9c7dc', 3),
        checkflags = (
            bg3.flag_group('Global', (
                bg3.flag(Shadowheart_Turned_Away_From_Shar.uuid, True, None),
            )),
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_REALLY_SHADOWHEART, True, slot_idx_shadowheart),
            )),
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_State_PartneredWithShadowheart, True, slot_idx_tav),
                bg3.flag(Shadowheart_State_DontHireDapperDrowPromise.uuid, True, slot_idx_shadowheart),
            )),
        ),
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(Shadowheart_Approval_Set_To_Zero.uuid, True, slot_idx_tav),
                bg3.flag(bg3.FLAG_ORI_State_HandledBreakupWithShadowheart, True, slot_idx_tav),
            )),
        ))
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '6.31',
        your_affections_drifted_node_uuid,
        (),
        look_at_player = bg3.SPEAKER_NYM_ORLYTH,
        emotions={
            bg3.SPEAKER_SHADOWHEART: ((0.0, 4, None), (3.35, 16, 1), (5.18, 4, None)),
            bg3.SPEAKER_PLAYER: ((0.0, 4, None),)
        },
        phase_duration = '7.0')
    create_shadowheart_tl_shot(t, '0.0', '6.31')
    t.create_tl_shot('318bfab8-282a-47ed-abdc-78184e7a6c30', '6.31', '7.0', is_snapped_to_end=True)


bg3.add_build_procedure('patch_sharess_caress', patch_sharess_caress)
bg3.add_build_procedure('patch_dapper_drow_intimacy', patch_dapper_drow_intimacy)

from __future__ import annotations

import bg3moddinglib as bg3

from .context import game_assets
from .flags import *

############################################################################
# This fixes all the shoehorned Halsin-related nonsense, including banter
############################################################################

def patch_creepy_druid() -> None:
    ############################################################################
    # Dialog: ShadowHeart_InParty2_Nested_DefaultChapter.lsf
    # If Shadowheart rejected Shar, she breaks up with Tav
    # if they are determined to sleep with Halsin.
    ############################################################################

    # d = bg3.dialog_object(files.get_file('Gustav', 'Mods/GustavDev/Story/DialogsBinary/Companions/ShadowHeart_InParty2_Nested_DefaultChapter.lsf'))
    # t = bg3.timeline_object(files.get_file('Gustav', 'Public/GustavDev/Timeline/Generated/ShadowHeart_InParty2_Nested_DefaultChapter.lsf'), d)

    ab = game_assets.get_modded_dialog_asset_bundle('ShadowHeart_InParty2_Nested_DefaultChapter')
    d = bg3.dialog_object(ab.dialog)
    t = bg3.timeline_object(ab.timeline, d)

    # speaker slots
    slot_idx_tav = d.get_speaker_slot_index(bg3.SPEAKER_PLAYER)
    slot_idx_shadowheart = d.get_speaker_slot_index(bg3.SPEAKER_SHADOWHEART)

    # dialog uuids
    # these will work for Sharran path only
    ori_willing_to_share_node_uuid = 'd068cdda-889c-48e4-862b-3f7582a2178a'        # ha4ef192dg5572g46a4g8650g392d3e528c46 "He's open-minded, and willing to share... as long as you are."
    ori_space_for_you_and_i_node_uuid = '6c42318e-a9f1-447b-bf53-0395e02ce610'     # hd659b6abge7f2g4246gbdfag871ce01df511 "He wants me. And I want him. I'm not sure if there's space for you and I."
    ori_not_quite_true_node_uuid = 'a72253d9-8bb4-4b6b-bbd8-645234a1d5e3'          # h1f8512c8gbf54g4320ga929ge622d5f05434 "But that's not quite true, is it? You <i>are </i>interested."   
    ori_cruel_to_deny_you_node_uuid = '196e514c-7dec-40d6-8315-24f66ee86f70'       # contains tav's follow up questions
    ori_im_glad_fanservice_node_uuid = 'afd7efc0-cff7-4ef5-8f46-665065b2041c'
    #ori_forget_it_wandering_eye_node_uuid = '1a331bb1-d9e2-4ad8-a625-6bc349eb9430' # hdddd3031g1a88g4096g97e7gc4c0527b20c8 "Forget it. Just my wandering eye. I'll tell him I'm not interested."

    # replacement nodes for Selune path
    new_willing_to_share_node_uuid = 'd8739c08-8abd-4d6c-80d0-af66e42d966f'
    new_space_for_you_and_i_node_uuid = 'd7f46d8d-e432-4599-99f2-9ae107b7b90a'
    fork_spare_lover_node_uuid = '888eaff2-da60-40b7-b2f2-1aad2cf23fc0'
    #new_forget_it_wandering_eye_node_uuid = '7f98e7dd-5724-4508-a57a-70e7023d74ae'

    # reactions to the new nodes
    breakup_reaction_node_uuid = '522b8845-5f52-4b19-b4fa-ffe92eeeff5d' # existing node, reposnse to new_space_for_you_and_i_node_uuid
    spare_lover_node_uuid = '2c250206-77c2-4feb-a73e-c80a6fe285b4' # response to new_willing_to_share_node_uuid
    want_be_with_you_node_uuid = 'cdbf6ef1-f01a-455e-ad95-016ce20741d4'
    your_new_beau_uuid = '69a6d3af-88d2-4298-b777-daaf3b68b430'
    new_memories_node_uuid = '122a341f-5c12-4944-89a0-d70e1262ef62'
    #thank_you_understanding_node_uuid = 'b3558b5e-8e65-467e-ba57-fd72b4050c7d'
    #almost_flattered_node_uuid = 'fac231c8-8200-445f-9b5f-5f43281017bc'
    fleeting_relationship_node_uuid = '7d7e27c7-87c4-4074-b9a7-d8f43b146aa0'
    i_suppose_it_was_node_uuid = 'b80794d3-eb9c-4cbd-b593-1efb50153d84'
    not_meant_to_be_node_uuid = 'd0bff72f-3e42-4adc-bec2-0ccabe6ac20b'

    # the parent node for all new nodes
    youre_talking_about_halsin_uuid = '3da75e80-d9eb-4ca1-9c0e-6cf8bd0938ac'

    # preserve the existing behavior if Shadowhart remained loyal to Shar
    d.set_dialog_flags(
        ori_willing_to_share_node_uuid,
        checkflags = (
            bg3.flag_group('Global', (
                bg3.flag(Shadowheart_Turned_Away_From_Shar.uuid, False, None),
            )),
        ),
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(Shadowheart_Lost_Faith_In_Tav.uuid, True, slot_idx_tav),
            )),
        ))
    d.set_dialog_flags(
        ori_space_for_you_and_i_node_uuid,
        checkflags = (
            bg3.flag_group('Global', (
                bg3.flag(Shadowheart_Turned_Away_From_Shar.uuid, False, None),
            )),
        ),
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(Shadowheart_Lost_Faith_In_Tav.uuid, True, slot_idx_tav),
            )),
        ))
    #d.set_dialog_flags(ori_forget_it_wandering_eye_node_uuid, checkflags=(shadowheart_chosen_of_shar_true,))

    # add new behavior if Shadowheart defied Shar
    d.add_child_dialog_node(youre_talking_about_halsin_uuid, new_willing_to_share_node_uuid)
    d.add_child_dialog_node(youre_talking_about_halsin_uuid, new_space_for_you_and_i_node_uuid)
    #d.add_child_dialog_node(youre_talking_about_halsin_uuid, new_forget_it_wandering_eye_node_uuid)

    # He wants me. And I want him. I'm not sure if there's space for you and I.
    d.create_standard_dialog_node(
        new_space_for_you_and_i_node_uuid,
        bg3.SPEAKER_PLAYER,
        [breakup_reaction_node_uuid],
        bg3.text_content('hd659b6abge7f2g4246gbdfag871ce01df511', 1),
        constructor=bg3.dialog_object.QUESTION,
        checkflags = (
            bg3.flag_group('Global', (
                bg3.flag(Shadowheart_Turned_Away_From_Shar.uuid, True, None),
            )),
        ),
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_State_PartneredWithShadowheart, False, slot_idx_tav),
                bg3.flag(bg3.FLAG_ORI_State_WasPartneredWithShadowheart, True, slot_idx_tav),
                bg3.flag(bg3.FLAG_CAMP_Halsin_CRD_Romance_PartnerAllowsHalsin, True, slot_idx_tav),
                bg3.flag(bg3.FLAG_ORI_State_HandledBreakupWithShadowheart, True, slot_idx_tav),
            )),
            bg3.flag_group('Global', (
                bg3.flag(bg3.FLAG_ORI_Shadowheart_State_PostSkinnydipping_Discussed, True, None),
            )),
        ))

    # He's open-minded, and willing to share... as long as you are.
    d.create_standard_dialog_node(
        new_willing_to_share_node_uuid,
        bg3.SPEAKER_PLAYER,
        [spare_lover_node_uuid],
        bg3.text_content('ha4ef192dg5572g46a4g8650g392d3e528c46', 1),
        constructor=bg3.dialog_object.QUESTION,
        checkflags = (
            bg3.flag_group('Global', (
                bg3.flag(Shadowheart_Turned_Away_From_Shar.uuid, True, None),
            )),
        ),
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_State_PartneredWithShadowheart, False, slot_idx_tav),
                bg3.flag(bg3.FLAG_ORI_State_WasPartneredWithShadowheart, True, slot_idx_tav),
                bg3.flag(bg3.FLAG_CAMP_Halsin_CRD_Romance_PartnerAllowsHalsin, True, slot_idx_tav),
                bg3.flag(bg3.FLAG_ORI_State_HandledBreakupWithShadowheart, True, slot_idx_tav),
            )),
            bg3.flag_group('Global', (
                bg3.flag(bg3.FLAG_ORI_Shadowheart_State_PostSkinnydipping_Discussed, True, None),
            )),
        ))

    # This removes the following question:
    # I'm glad you were so understanding.
    d.delete_child_dialog_node(ori_cruel_to_deny_you_node_uuid, ori_im_glad_fanservice_node_uuid)

    d.create_standard_dialog_node(
        fork_spare_lover_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [spare_lover_node_uuid],
        None,
        checkflags = (
            bg3.flag_group('Global', (
                bg3.flag(Shadowheart_Turned_Away_From_Shar.uuid, True, None),
            )),
        ),
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_State_PartneredWithShadowheart, False, slot_idx_tav),
                bg3.flag(bg3.FLAG_ORI_State_WasPartneredWithShadowheart, True, slot_idx_tav),
                bg3.flag(bg3.FLAG_CAMP_Halsin_CRD_Romance_PartnerAllowsHalsin, True, slot_idx_tav),
                bg3.flag(bg3.FLAG_ORI_State_HandledBreakupWithShadowheart, True, slot_idx_tav),
            )),
            bg3.flag_group('Global', (
                bg3.flag(bg3.FLAG_ORI_Shadowheart_State_PostSkinnydipping_Discussed, True, None),
            )),
        ))
    d.add_child_dialog_node(ori_not_quite_true_node_uuid, fork_spare_lover_node_uuid, 0)

    # # Forget it. Just my wandering eye. I'll tell him I'm not interested.
    # d.create_standard_dialog_node(
    #     new_forget_it_wandering_eye_node_uuid,
    #     bg3.SPEAKER_PLAYER,
    #     [almost_flattered_node_uuid],
    #     bg3.text_content('hdddd3031g1a88g4096g97e7gc4c0527b20c8', 1),
    #     constructor=bg3.dialog_object.QUESTION,
    #     setflags=(halsin_sharing_not_ok_true,),
    #     checkflags=(shadowheart_enemy_of_shar_true,))

    # In truth, I don't think I'd want to be your spare lover. I'd always want more of you than you'd have to spare. Better perhaps to bow out with dignity.
    d.create_standard_dialog_node(
        spare_lover_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [fleeting_relationship_node_uuid, want_be_with_you_node_uuid],
        bg3.text_content('hd3fd298bgb472g4e8bg8e74gaceeb20de6e1', 1))
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '13.06',
        spare_lover_node_uuid,
        (('13.06', '7b067edd-f53f-49e1-95bc-0986e6e2ca2f'), (None, 'b4155335-5e08-4d85-8ccd-ddebf5507447')),
        emotions={
            bg3.SPEAKER_SHADOWHEART: ((0.0, 4, None), (1.82, 16, None), (3.56, 32, None), (5.29, 64, 1), (8.9, 1024, 2), (11.0, 64, None), (11.8, 2, None)),
            bg3.SPEAKER_PLAYER: ((0.0, 64, 1),)
        },
        phase_duration='13.56')

    # Our relationship was... fleeting. I want to move on.
    d.create_standard_dialog_node(
        fleeting_relationship_node_uuid,
        bg3.SPEAKER_PLAYER,
        [i_suppose_it_was_node_uuid],
        bg3.text_content('hf278c5d2g81beg46abgaa45g649a20dfeb09', 1),
        constructor=bg3.dialog_object.QUESTION,
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_State_PartneredWithShadowheart, False, slot_idx_tav),
                bg3.flag(bg3.FLAG_ORI_State_WasPartneredWithShadowheart, True, slot_idx_tav),
                bg3.flag(bg3.FLAG_CAMP_Halsin_CRD_Romance_PartnerAllowsHalsin, True, slot_idx_tav),
                bg3.flag(bg3.FLAG_ORI_State_HandledBreakupWithShadowheart, True, slot_idx_tav),
            )),
            bg3.flag_group('Global', (
                bg3.flag(bg3.FLAG_ORI_Shadowheart_State_PostSkinnydipping_Discussed, True, None),
            )),
        ))

    # I suppose it was. And don't worry - I'm not going to toss your belongings into the campfire or anything.
    d.create_standard_dialog_node(
        i_suppose_it_was_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [not_meant_to_be_node_uuid],
        bg3.text_content('h11cbe8fcg20cdg498bgb7cbg47060b5530a6', 3))
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '8.31',
        i_suppose_it_was_node_uuid,
        ((None, '7b067edd-f53f-49e1-95bc-0986e6e2ca2f'),),
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 1024, 1), (2.98, 64, None), (4.73, 64, 1), (6.26, 4, 2)),
            bg3.SPEAKER_PLAYER: ((0.0, 4, None),)
        })

    # Maybe you and I are not meant to be, I don't know. I sense I'll have little time for distractions, moving forward. Especially ones that don't bear fruit.
    d.create_standard_dialog_node(
        not_meant_to_be_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [new_memories_node_uuid],
        bg3.text_content('h03a13c89ge885g4ebcgbc71gb2d502c80f3a', 1))
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '11.2',
        not_meant_to_be_node_uuid,
        ((None, '0e8837db-4344-48d0-9175-12262c73806b'),),
        emotions={
            bg3.SPEAKER_SHADOWHEART: ((0.0, 32, None), (4.76, 16, None), (9.05, 2048, None)),
            bg3.SPEAKER_PLAYER: ((0.0, 16, None),)
        })

    # I didn't realize your feel this way. I want to be with you... Forget I ever said anything.
    d.create_standard_dialog_node(
        want_be_with_you_node_uuid,
        bg3.SPEAKER_PLAYER,
        [your_new_beau_uuid],
        bg3.text_content('h9635e41bge285g4f12gb61bg13692d55fba6', 1),
        constructor = bg3.dialog_object.QUESTION)

    # Oh don't be like that - you've made your bed, now go roll around in it with your new beau.
    d.create_standard_dialog_node(
        your_new_beau_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [new_memories_node_uuid],
        bg3.text_content('h45bb0963g86ccg4633gb227gb944064b9b0d', 3))
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '7.0',
        your_new_beau_uuid,
        ((None, '7b067edd-f53f-49e1-95bc-0986e6e2ca2f'),),
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 128, 1), (2.5, 16, None), (4.11, 1024, None), (6.2, 64, None))
        })
    
    # Though for a while, I thought I might have someone to share new memories with. Not to be, it seems...
    d.create_standard_dialog_node(
        new_memories_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [],
        bg3.text_content('h78acffbfgbaa2g4fd9g8f1bgfd0fa7ef98f4', 3),
        end_node = True)
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '8.21',
        new_memories_node_uuid,
        ((None, '0e8837db-4344-48d0-9175-12262c73806b'),),
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 16, None), (2.34, 4, None), (6.31, 32, None),)
        })
    

    # # Thank you. I had a feeling you'd be understanding.
    # d.create_standard_dialog_node(
    #     thank_you_understanding_node_uuid,
    #     bg3.SPEAKER_SHADOWHEART,
    #     [],
    #     bg3.text_content('hc6d2bb77g1250g40e2gac71g74c4d0c686ff', 1),
    #     end_node=True)
    # t.create_simple_dialog_answer_phase(
    #     bg3.SPEAKER_SHADOWHEART,
    #     4.53,
    #     thank_you_understanding_node_uuid,
    #     ((None, '7b067edd-f53f-49e1-95bc-0986e6e2ca2f'),),
    #     emotions={
    #         bg3.SPEAKER_SHADOWHEART: ((0.0, 64, None), (2.48, 2, None)),
    #         bg3.SPEAKER_PLAYER: ((0.0, 2, None),)
    #     })

    # # I'm almost flattered. Almost.
    # d.create_standard_dialog_node(
    #     almost_flattered_node_uuid,
    #     bg3.SPEAKER_SHADOWHEART,
    #     [],
    #     bg3.text_content('he817ea29gb437g4509gaa6egf9f4acf255a0', 1),
    #     end_node=True)
    # t.create_simple_dialog_answer_phase(
    #     bg3.SPEAKER_SHADOWHEART,
    #     4.45,
    #     almost_flattered_node_uuid,
    #     ((None, '7b067edd-f53f-49e1-95bc-0986e6e2ca2f'),),
    #     emotions={
    #         bg3.SPEAKER_SHADOWHEART: ((0.0, 64, None), (1.84, 2, None)),
    #         bg3.SPEAKER_PLAYER: ((0.0, 1, None),)
    #     })


    #########################################################################
    # Dialog: Halsin_InParty_Nested_Polyamory.lsf
    #########################################################################

    #########################################################################
    # Selune Shadowheart doesn't want Tav to sleep with Halsin.
    # If Tav ignores her and does that, Shadowheart ends their relatinship
    #########################################################################

    # d = bg3.dialog_object(files.get_file('Gustav', 'Mods/GustavDev/Story/DialogsBinary/Companions/Halsin_InParty_Nested_Polyamory.lsf'))

    ab = game_assets.get_modded_dialog_asset_bundle('Halsin_InParty_Nested_Polyamory')
    d = bg3.dialog_object(ab.dialog)

    # speaker slots
    slot_idx_tav = d.get_speaker_slot_index(bg3.SPEAKER_PLAYER)

    existing_making_my_own_node_uuid = 'b73b4b91-7c1f-4b0a-975d-68a4e2ee3017'
    existing_answer_node_uuid = 'e86250d2-036a-4a13-9d4b-dae85d7193e6'
    new_selune_path_node_uuid = '389d34ce-0297-4f86-b6b5-12a2811e0f06'
    new_shar_path_node_uuid = 'bd6ee90c-8e29-48e4-a9a9-a045f6ea97e8'
    new_not_partnered_node_uuid = '5b616a0c-bedb-4b04-b858-5345c2438dee'

    d.create_standard_dialog_node(
        new_selune_path_node_uuid,
        bg3.SPEAKER_HALSIN,
        [existing_answer_node_uuid],
        None,
        checkflags = (
            bg3.flag_group('Global', (
                bg3.flag(Shadowheart_Turned_Away_From_Shar.uuid, True, None),
            )),
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_State_PartneredWithShadowheart, True, slot_idx_tav),
            ))
        ),
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_State_PartneredWithShadowheart, False, slot_idx_tav),
                bg3.flag(bg3.FLAG_ORI_State_WasPartneredWithShadowheart, True, slot_idx_tav),
                bg3.flag(Shadowheart_BreakUp_Notification_Start.uuid, True, slot_idx_tav),
            )),
            bg3.flag_group('Global', (
                bg3.flag(bg3.FLAG_ORI_Shadowheart_State_PostSkinnydipping_Discussed, True, None),
                bg3.flag(bg3.FLAG_ORI_Shadowheart_State_PostNightfall_Discussed, True, None),
            ))
        ))

    d.create_standard_dialog_node(
        new_shar_path_node_uuid,
        bg3.SPEAKER_HALSIN,
        [existing_answer_node_uuid],
        None,
        checkflags = (
            bg3.flag_group('Global', (
                bg3.flag(Shadowheart_Turned_Away_From_Shar.uuid, False, None),
            )),
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_State_PartneredWithShadowheart, True, slot_idx_tav),
            ))
        ),
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(Shadowheart_Lost_Faith_In_Tav.uuid, True, slot_idx_tav),
            )),
        ))

    d.create_standard_dialog_node(
        new_not_partnered_node_uuid,
        bg3.SPEAKER_HALSIN,
        [existing_answer_node_uuid],
        None,
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_State_PartneredWithShadowheart, False, slot_idx_tav),
            )),
        ))


    d.delete_child_dialog_node(existing_making_my_own_node_uuid, existing_answer_node_uuid)
    d.add_child_dialog_node(existing_making_my_own_node_uuid, new_selune_path_node_uuid)
    d.add_child_dialog_node(existing_making_my_own_node_uuid, new_shar_path_node_uuid)
    d.add_child_dialog_node(existing_making_my_own_node_uuid, new_not_partnered_node_uuid)


def patch_creepy_banter() -> None:
    ##################################################################
    # Banter: PB_Halsin_Shadowheart_ROM_Act3_Selune.lsf
    ##################################################################

    ##################################################################
    # Shadowheart & Halsin act 3 banter, Shadowheart's new response
    ##################################################################
    # d = bg3.dialog_object(files.get_file('Gustav', 'Mods/GustavDev/Story/DialogsBinary/Companions/Party_Banter/PB_Halsin_Shadowheart_ROM_Act3_Selune.lsf'))

    ab = game_assets.get_modded_dialog_asset_bundle('PB_Halsin_Shadowheart_ROM_Act3_Selune')
    d = bg3.dialog_object(ab.dialog)

    speaker_idx_creep = d.get_speaker_slot_index(bg3.SPEAKER_HALSIN)

    # Maybe. If you keep a respectable distance.
    #d.set_tagged_text('c271277b-9408-4c66-bf2f-c5b76fac64f4', bg3.text_content("hbf7a4276g3c6bg49c0gab09g790c7dcb6428", 2))
    
    # If that was an attempt at flirting, I should let you know I prefer the strong, <i>silent </i>type.
    d.set_tagged_text('c271277b-9408-4c66-bf2f-c5b76fac64f4', bg3.text_content("h0edd75e3g6b84g4facg97f6g2bcfda138c6d", 1))

    # I'm not quite sure I like where this is going.
    #d.set_tagged_text('c271277b-9408-4c66-bf2f-c5b76fac64f4', bg3.text_content("hf0b44b12g4b49g4b1fgb8c6g1e8e9f2568da", 1))

    d.set_dialog_flags('c271277b-9408-4c66-bf2f-c5b76fac64f4', setflags = (
        bg3.flag_group('Object', (
            bg3.flag(Creep_Harassed_Shadowheart.uuid, True, speaker_idx_creep),
        )),
    ))


def create_post_creepy_banter_scene() -> None:
    # crd = bg3.dialog_object(files.get_file('Gustav', 'Mods/GustavDev/Story/DialogsBinary/Camp/Camp_Relationship_Dialogs/Camp_Act3_CRD_HalsinRomance.lsf'))

    ab = game_assets.get_modded_dialog_asset_bundle('Camp_Act3_CRD_HalsinRomance')
    crd = bg3.dialog_object(ab.dialog)

    speaker_idx_tav = crd.get_speaker_slot_index(bg3.SPEAKER_PLAYER)
    # I'm afraid I just don't see you that way.
    crd.add_dialog_flags('27e3fa90-a2ac-636f-aeca-24f5317e975a', setflags = (
        bg3.flag_group('Object', (
            bg3.flag(Halsin_Rejected.uuid, True, speaker_idx_tav),
        )),
    ))
    # If I wanted to rut with half a tonne of dumb muscle, I'd seduce a deep rothé.
    crd.add_dialog_flags('89c45b14-3b7f-fe7d-78f8-cc5f4ba2166d', setflags = (
        bg3.flag_group('Object', (
            bg3.flag(Halsin_Rejected.uuid, True, speaker_idx_tav),
        )),
    ))

    # d = bg3.dialog_object(files.get_file('Gustav', 'Mods/GustavDev/Story/DialogsBinary/Companions/Halsin_InParty.lsf'))
    # t = bg3.timeline_object(files.get_file('Gustav', 'Public/GustavDev/Timeline/Generated/Halsin_InParty.lsf'), d)

    ab = game_assets.get_modded_dialog_asset_bundle('Halsin_InParty')
    d = bg3.dialog_object(ab.dialog)
    t = bg3.timeline_object(ab.timeline, d)

    speaker_idx_tav = d.get_speaker_slot_index(bg3.SPEAKER_PLAYER)
    speaker_idx_creep = d.get_speaker_slot_index(bg3.SPEAKER_HALSIN)

    conversations_root_node_uuid = 'addef3bf-04a8-4df3-b1d9-a1a5b93c800a'

    i_overheard_you_asking_node_uuid = 'dc712669-a84a-4d9f-bb1e-3aa6817c566d'
    creep_line_1_node_uuid = '3a43e153-abd5-4451-bf10-58651f1c7edd'
    creep_line_2_node_uuid = '582e6de0-3737-4f96-8c20-f4723802ec45'
    creep_line_3_node_uuid = 'd48e0f5c-4609-46b6-9269-86fe86500e33'
    told_you_already_node_uuid = 'af10f7e1-08b4-494c-8169-9c38099c091b'
    dont_see_you_the_way_node_uuid = 'e25f2f0f-3e5a-4953-9ec8-e644cebd2d2f'
    half_a_tonne_of_dumb_node_uuid = 'fe316325-294b-43cc-9799-86a45657be61'
    let_him_finish_node_uuid = '517a81e2-21d4-4b83-b94f-3c1bf041ca39'
    creep_stays_node_uuid = 'a2106406-6761-4e08-b43f-a4983d9c202d'
    creep_simple_no_node_uuid = '0a467790-2bd6-41d1-b5b5-2a1d845112cd'
    creep_i_understand_node_uuid = '7a40e852-3512-485d-bfed-efca9669bcaf'
    creep_have_tried_and_failed_node_uuid = 'bdd5f294-e888-475b-a36d-3d79c6e79176'
    narrator_rage_node_uuid = 'cc7a21f1-e692-475e-9e51-a03bf3438b7f'
    wis_roll_node_uuid = 'bc4ad101-259c-4231-b4a5-5b9727e64119'
    int_roll_node_uuid = 'ee097e87-0ec5-4c35-8103-ed60e2262646'
    cha_roll_node_uuid = 'f624bbd3-393e-487c-afca-edbd47bde719'
    violent_resolution_node_uuid = 'a8d75d93-e71b-4cfe-84dc-b04e9f94d6ae'
    non_violent_resolution_node_uuid = '94c4622c-d218-4170-9a69-d03636650f74'
    get_yourself_together_node_uuid = '9739e46a-1af6-422d-a789-0f27f1489663'
    give_in_to_emotions_node_uuid = '09ed5946-d76c-44c7-a260-eaf50ffd8ab6'
    give_in_to_emotions_short_node_uuid = '5570cfde-f311-4ab9-a1fa-154cbe7d9067'
    give_in_to_emotions_female_node_uuid = '522c8c80-1f04-412f-9c77-c6a48e8a60aa'
    durge_rage_fork_node_uuid = '216c05e7-2dc6-4ae4-a575-6e8dd283f300'
    fighter_rage_fork_node_uuid = '4cf1f5fd-d674-493d-a7d0-ea8d9d5683c9'
    barbarian_rage_fork_node_uuid = '35e487f8-60a5-4b15-a081-5ae9d7798a72'
    warlock_rage_fork_node_uuid = '70250e48-e997-432b-83af-7ed6b5430c83'
    bard_rage_fork_node_uuid = '535c520e-28bb-4066-8ce2-d7a997528491'
    rogue_rage_fork_node_uuid = '73cf3a13-2968-4b22-ad57-40c1d20d950b'
    ranger_rage_fork_node_uuid = '605785ed-5339-411e-9fe4-ca0137e0265b'
    durge_violent_options_node_uuid = '8264f8b0-8a21-44c7-8159-302b29c5b20b'
    tav_violent_options_node_uuid = 'e45de312-6d06-4d4e-817f-db89bd64c952'
    narrator_calm_down_node_uuid = '00c89c3e-7684-4963-81ae-c5e331bcb39a'
    narrator_rage_continues_node_uuid = '7a61d772-21e6-4536-9f3d-c24f98bb2c61'
    reconsider_your_life_choices_node_uuid = '66f55805-db46-4044-9f8d-744a53a7eaab'
    habit_of_intruding_into_private_node_uuid = '24e14b9c-ced2-4352-ac80-0a4a6d92dee7'
    this_is_ours_leave_us_alone_node_uuid = '79ab9b47-cdab-4fc3-b960-712a9ca4212a'
    creep_must_say_farewell_node_uuid = '47b22ae2-3d02-4166-9121-bca502675447'
    creep_says_farewell_node_uuid = '7489e443-408d-4966-9bdf-4420acf967c2'
    kick_em_in_the_balls_node_uuid = 'e68d7b45-ea9e-4387-9269-2ac5dae08738'
    knock_em_out_node_uuid = '077d6113-32a8-492f-b42c-24b5cb35bdf1'
    apply_kocked_out_status_node_uuid = '617dc943-7c26-4b50-99cb-92891830c46c'
    fuck_right_off_node_uuid = '2429c940-cbc7-450b-ae40-968dd54cc15a'
    look_with_disdain_node_uuid = 'ddf9380b-2b8b-4db3-acf2-c95525c5064d'
    creep_runs_away_node_uuid = 'c2ea5812-c939-425f-b528-9ae24c8a7a0d'

    """
    8e0c85c8-0771-469e-bdf7-a7787a810515 Tav -> Tav
    f1729ce3-4ef3-4fc6-b8d3-ecc8b14305c8 Tav -> Tav
    f26f44f0-f224-445e-b753-9cad18c4970b Creep -> Tav
    d6fa1bdc-4438-43c8-9934-906090970e86 Creep -> Tav
    b1c01ea8-ffa9-45dc-b6f3-2a769cbfc493 Creep -> Tav
    e12c5268-d8db-4934-b492-e0a57333edc8 Creep -> Tav
    7fe134a6-58f5-4359-a95c-b2d9b307dd7b Creep -> Creep
    233735c2-c16c-40dd-a1b5-105bca4ca484 Creep -> Creep
    ff762d89-62c9-46cd-9d12-afd0c3bcedd1 Tav -> Creep
    c0021c6a-f0da-42fd-b4a4-a14105dedf33 Tav -> Creep
    381b21bc-e3f6-4268-991e-d7455b3e3e75 Tav -> Creep
    """

    d.add_child_dialog_node(conversations_root_node_uuid, i_overheard_you_asking_node_uuid, 0)

    # I overheard you asking Shadowheart about swimming. What did you have in mind?
    d.create_standard_dialog_node(
        i_overheard_you_asking_node_uuid,
        bg3.SPEAKER_PLAYER,
        [creep_line_1_node_uuid],
        bg3.text_content('h42d1b00bg51a3g4375gb34dge423a6fe72e8', 1),
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(Creep_Harassed_Shadowheart.uuid, True, speaker_idx_creep),
            )),
        ),
        constructor = bg3.dialog_object.QUESTION)

    # I have lived a very long time. I have taken many lovers. My heart does not stir lightly. But it does now.
    d.create_standard_dialog_node(
        creep_line_1_node_uuid,
        bg3.SPEAKER_HALSIN,
        [creep_line_2_node_uuid],
        bg3.text_content('h1bb64a91ge87dg45deg812bgdb4253c71a14', 2))
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_HALSIN,
        '12.17',
        creep_line_1_node_uuid,
        ((None, 'ff762d89-62c9-46cd-9d12-afd0c3bcedd1'),),
        phase_duration = '12.5',
        emotions = {
            bg3.SPEAKER_HALSIN: ((0.0, 64, 2), (3.43, 4, None), (6.46, 64, None)),
            bg3.SPEAKER_PLAYER: ((0.0, 1, None),),
        })

    # I think you feel the same way. The connection is... palpable.
    d.create_standard_dialog_node(
        creep_line_2_node_uuid,
        bg3.SPEAKER_HALSIN,
        [let_him_finish_node_uuid, dont_see_you_the_way_node_uuid, told_you_already_node_uuid, half_a_tonne_of_dumb_node_uuid],
        bg3.text_content('h207c7ccfg73dcg48abg8bd4gbb15ea2e50bb', 2))
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_HALSIN,
        '5.65',
        creep_line_2_node_uuid,
        ((None, '233735c2-c16c-40dd-a1b5-105bca4ca484'),),
        phase_duration = '6.0',
        emotions = {
            bg3.SPEAKER_HALSIN: ((3.21, 32, None), (4.51, 16, None),),
            bg3.SPEAKER_PLAYER: ((0.0, 1, None),),
        })

    dont_see_you_the_way_node_uuid = 'e25f2f0f-3e5a-4953-9ec8-e644cebd2d2f'
    half_a_tonne_of_dumb_node_uuid = 'fe316325-294b-43cc-9799-86a45657be61'
    let_him_finish_node_uuid = '517a81e2-21d4-4b83-b94f-3c1bf041ca39'

    shadowheart_approval_plus_5 = bg3.reaction_object.create_new(files, { bg3.SPEAKER_SHADOWHEART : 5 }, uuid = 'f07427a7-2287-4914-b5d6-a0cc0996b90b')
    shadowheart_approval_minus_1 = bg3.reaction_object.create_new(files, { bg3.SPEAKER_SHADOWHEART : -1 }, uuid = 'ea38d0fa-8499-4013-8f67-a08798d52ec4')

    # You see that Halsin has more to say. Keep silent and let him finish.
    d.create_standard_dialog_node(
        let_him_finish_node_uuid,
        bg3.SPEAKER_PLAYER,
        [creep_line_3_node_uuid],
        bg3.text_content('h77c85f76g5407g4987g96adg074ece30828f', 1),
        constructor = bg3.dialog_object.QUESTION)

    # Halsin, you're a good friend, but that's about it. I don't see you the way you think I do.
    d.create_standard_dialog_node(
        dont_see_you_the_way_node_uuid,
        bg3.SPEAKER_PLAYER,
        [creep_i_understand_node_uuid],
        bg3.text_content('hf932554dg421bg4db0gaab0g1b6dad0e484b', 1),
        approval_rating_uuid = shadowheart_approval_plus_5.uuid,
        constructor = bg3.dialog_object.QUESTION)

    # I told you already, didn't I? I am not interested. Stop that.
    d.create_standard_dialog_node(
        told_you_already_node_uuid,
        bg3.SPEAKER_PLAYER,
        [creep_simple_no_node_uuid],
        bg3.text_content('h33fbed16g06d2g47a3gaf9fg55c01a59603c', 1),
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(Halsin_Rejected.uuid, True, speaker_idx_tav),
            )),
        ),
        approval_rating_uuid = shadowheart_approval_plus_5.uuid,
        constructor = bg3.dialog_object.QUESTION)

    # If I wanted to rut with half a tonne of dumb muscle, I'd seduce a deep rothé.
    d.create_standard_dialog_node(
        half_a_tonne_of_dumb_node_uuid,
        bg3.SPEAKER_PLAYER,
        [creep_simple_no_node_uuid],
        bg3.text_content('hc612d4dfgad1fg4cfdga323g2c4d22b0c2fa', 2),
        approval_rating_uuid = shadowheart_approval_plus_5.uuid,
        constructor = bg3.dialog_object.QUESTION)

    # You have bonded with Shadowheart, body and soul. Her scent lingers on your skin. If there is to be anything between us, it must be with her consent, and ... her participation.
    d.create_standard_dialog_node(
        creep_line_3_node_uuid,
        bg3.SPEAKER_HALSIN,
        [
            durge_rage_fork_node_uuid,
            fighter_rage_fork_node_uuid,
            barbarian_rage_fork_node_uuid,
            warlock_rage_fork_node_uuid,
            bard_rage_fork_node_uuid,
            rogue_rage_fork_node_uuid,
            ranger_rage_fork_node_uuid,
            non_violent_resolution_node_uuid
        ],
        bg3.text_content('ha06ce793g2c90g4073gaa0dg676340b475ec', 1))
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_HALSIN,
        '14.0',
        creep_line_3_node_uuid,
        (
            ('11.3', '381b21bc-e3f6-4268-991e-d7455b3e3e75'),
            (None, 'e12c5268-d8db-4934-b492-e0a57333edc8'),
        ),
        emotions = {
            bg3.SPEAKER_HALSIN: ((0.0, 16, None), (7.05, 32, None), (12.47, 64, None),),
            bg3.SPEAKER_PLAYER: ((0.0, 8, None), (12.5, 8, 2)),
        },
        phase_duration = '16.0')

    # A simple 'no' would have sufficed. I will trouble you with the matter no more.
    d.create_standard_dialog_node(
        creep_simple_no_node_uuid,
        bg3.SPEAKER_HALSIN,
        [],
        bg3.text_content('h0dea29bcg18beg44f0gab9fg307666dfb31b', 1),
        end_node = True,
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(Creep_Harassed_Shadowheart.uuid, False, speaker_idx_creep),
            )),
        ))
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_HALSIN,
        '6.3',
        creep_simple_no_node_uuid,
        ((None, '233735c2-c16c-40dd-a1b5-105bca4ca484'),),
        phase_duration = '6.7',
        emotions = {
            bg3.SPEAKER_HALSIN: ((0.0, 2048, None), (4.12, 32, None)),
            bg3.SPEAKER_PLAYER: ((0.0, 1, None),),
        })

    # I understand, and I still cherish our relationship
    d.create_standard_dialog_node(
        creep_i_understand_node_uuid,
        bg3.SPEAKER_HALSIN,
        [creep_have_tried_and_failed_node_uuid],
        bg3.text_content('hcbf16cc6g7498g4634ga715g28176e903980', 3),
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(Creep_Harassed_Shadowheart.uuid, False, speaker_idx_creep),
            )),
        ))
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_HALSIN,
        '6.3',
        creep_i_understand_node_uuid,
        ((None, '7fe134a6-58f5-4359-a95c-b2d9b307dd7b'),),
        phase_duration = '6.7',
        emotions = {
            bg3.SPEAKER_HALSIN: ((0.2, 256, None), (1.5, 32, None), (3.62, 16, None)),
            bg3.SPEAKER_PLAYER: ((0.0, 1, None),),
        })

    # Still... I could not have forgiven myself had I not taken the plunge. Better to have tried and failed.
    d.create_standard_dialog_node(
        creep_have_tried_and_failed_node_uuid,
        bg3.SPEAKER_HALSIN,
        [],
        bg3.text_content('h72ae54e3gc3fag4c6dga34cgc5982c58f90c', 2),
        end_node = True)
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_HALSIN,
        '8.18',
        creep_have_tried_and_failed_node_uuid,
        ((None, '233735c2-c16c-40dd-a1b5-105bca4ca484'),),
        phase_duration = '8.4',
        emotions = {
            bg3.SPEAKER_HALSIN: ((0.0, 32, None), (1.27, 256, None), (2.25, 32, None), (6.06, 32, 2)),
            bg3.SPEAKER_PLAYER: ((0.0, 1, None),),
        })

    d.create_standard_dialog_node(
        durge_rage_fork_node_uuid,
        bg3.SPEAKER_PLAYER,
        [narrator_rage_node_uuid],
        None,
        checkflags = (
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_REALLY_DARK_URGE, True, speaker_idx_tav),
            )),
            bg3.flag_group('Object', (
                bg3.flag(Cheated_On_Shadowheart.uuid, False, speaker_idx_tav),
                bg3.flag(Shadowheart_Has_Doubts_About_Tav.uuid, False, speaker_idx_tav)
            ))
        ))
    d.create_standard_dialog_node(
        fighter_rage_fork_node_uuid,
        bg3.SPEAKER_PLAYER,
        [narrator_rage_node_uuid],
        None,
        checkflags = (
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_FIGHTER, True, speaker_idx_tav),
            )),
            bg3.flag_group('Object', (
                bg3.flag(Cheated_On_Shadowheart.uuid, False, speaker_idx_tav),
                bg3.flag(Shadowheart_Has_Doubts_About_Tav.uuid, False, speaker_idx_tav)
            ))
        ))
    d.create_standard_dialog_node(
        barbarian_rage_fork_node_uuid,
        bg3.SPEAKER_PLAYER,
        [narrator_rage_node_uuid],
        None,
        checkflags = (
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_BARBARIAN, True, speaker_idx_tav),
            )),
            bg3.flag_group('Object', (
                bg3.flag(Cheated_On_Shadowheart.uuid, False, speaker_idx_tav),
                bg3.flag(Shadowheart_Has_Doubts_About_Tav.uuid, False, speaker_idx_tav)
            ))
        ))
    d.create_standard_dialog_node(
        warlock_rage_fork_node_uuid,
        bg3.SPEAKER_PLAYER,
        [narrator_rage_node_uuid],
        None,
        checkflags = (
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_WARLOCK, True, speaker_idx_tav),
            )),
            bg3.flag_group('Object', (
                bg3.flag(Cheated_On_Shadowheart.uuid, False, speaker_idx_tav),
                bg3.flag(Shadowheart_Has_Doubts_About_Tav.uuid, False, speaker_idx_tav)
            ))
        ))
    d.create_standard_dialog_node(
        bard_rage_fork_node_uuid,
        bg3.SPEAKER_PLAYER,
        [narrator_rage_node_uuid],
        None,
        checkflags = (
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_BARD, True, speaker_idx_tav),
            )),
            bg3.flag_group('Object', (
                bg3.flag(Cheated_On_Shadowheart.uuid, False, speaker_idx_tav),
                bg3.flag(Shadowheart_Has_Doubts_About_Tav.uuid, False, speaker_idx_tav)
            ))
        ))
    d.create_standard_dialog_node(
        rogue_rage_fork_node_uuid,
        bg3.SPEAKER_PLAYER,
        [narrator_rage_node_uuid],
        None,
        checkflags = (
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_ROGUE, True, speaker_idx_tav),
            )),
            bg3.flag_group('Object', (
                bg3.flag(Cheated_On_Shadowheart.uuid, False, speaker_idx_tav),
                bg3.flag(Shadowheart_Has_Doubts_About_Tav.uuid, False, speaker_idx_tav)
            ))
        ))
    d.create_standard_dialog_node(
        ranger_rage_fork_node_uuid,
        bg3.SPEAKER_PLAYER,
        [narrator_rage_node_uuid],
        None,
        checkflags = (
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_RANGER, True, speaker_idx_tav),
            )),
            bg3.flag_group('Object', (
                bg3.flag(Cheated_On_Shadowheart.uuid, False, speaker_idx_tav),
                bg3.flag(Shadowheart_Has_Doubts_About_Tav.uuid, False, speaker_idx_tav)
            ))
        ))

    # *You feel a rush of outrage. Rage sparks to hatred.*
    d.create_standard_dialog_node(
        narrator_rage_node_uuid,
        bg3.SPEAKER_NARRATOR,
        [durge_violent_options_node_uuid, tav_violent_options_node_uuid],
        bg3.text_content('h56f32cd2g389dg407cg98b4g002620edc107', 1))
    
    t.create_new_phase(narrator_rage_node_uuid, '6.4')
    t.create_tl_shot('e12c5268-d8db-4934-b492-e0a57333edc8', '0.0', '6.4', is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.EMOTION, bg3.SPEAKER_PLAYER, '0.0', '6.4', (
        t.create_emotion_key(0.0, 8),
        t.create_emotion_key(3.5, 128)
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.ATTITUDE, bg3.SPEAKER_PLAYER, '0.0', '6.4', (), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.ATTITUDE, bg3.SPEAKER_HALSIN, '0.0', '6.4', (), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.LOOK_AT, bg3.SPEAKER_PLAYER, '0.0', '6.4', (
        t.create_look_at_key(
            0.0,
            target = bg3.SPEAKER_HALSIN,
            bone = 'Head_M',
            turn_mode = 3,
            turn_speed_multiplier = 0.3,
            head_turn_speed_multiplier = 0.3,
            weight = 0.3,
            reset = True,
            is_eye_look_at_enabled = True,
            eye_look_at_target_id = bg3.SPEAKER_HALSIN,
            eye_look_at_bone = 'Head_M'
        ),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.LOOK_AT, bg3.SPEAKER_HALSIN, '0.0', '6.4', (
        t.create_look_at_key(
            0.0,
            target = bg3.SPEAKER_PLAYER,
            bone = 'Head_M',
            turn_mode = 3,
            turn_speed_multiplier = 0.3,
            head_turn_speed_multiplier = 0.3,
            weight = 0.3,
            reset = True,
            is_eye_look_at_enabled = True,
            eye_look_at_target_id = bg3.SPEAKER_HALSIN,
            eye_look_at_bone = 'Head_M'
        ),
    ), is_snapped_to_end = True)
    t.create_tl_voice(bg3.SPEAKER_NARRATOR, '0.0', '5.954', narrator_rage_node_uuid, is_snapped_to_end = True)

    d.create_standard_dialog_node(
        durge_violent_options_node_uuid,
        bg3.SPEAKER_PLAYER,
        [wis_roll_node_uuid, int_roll_node_uuid, cha_roll_node_uuid, give_in_to_emotions_node_uuid],
        None,
        checkflags = (
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_REALLY_DARK_URGE, True, speaker_idx_tav),
            )),
        ))

    d.create_standard_dialog_node(
        tav_violent_options_node_uuid,
        bg3.SPEAKER_PLAYER,
        [get_yourself_together_node_uuid, give_in_to_emotions_node_uuid],
        None)


    d.create_roll_dialog_node(
        wis_roll_node_uuid,
        bg3.SPEAKER_PLAYER,
        bg3.SPEAKER_PLAYER,
        bg3.dialog_object.ABILITY_WISDOM,
        bg3.dialog_object.SKILL_INSIGHT,
        bg3.DC_Act3_Easy,
        narrator_calm_down_node_uuid,
        narrator_rage_continues_node_uuid,
        bg3.text_content('hf55f117bgd9a9g45bbgb3abg70ba0ffed6ed', 1))

    d.create_roll_dialog_node(
        int_roll_node_uuid,
        bg3.SPEAKER_PLAYER,
        bg3.SPEAKER_PLAYER,
        bg3.dialog_object.ABILITY_INTELLIGENCE,
        bg3.dialog_object.SKILL_ARCANA,
        bg3.DC_Act3_Easy,
        narrator_calm_down_node_uuid,
        narrator_rage_continues_node_uuid,
        bg3.text_content('h56547ff0g9decg4039gb404g2dd49d28fe57', 1))

    d.create_roll_dialog_node(
        cha_roll_node_uuid,
        bg3.SPEAKER_PLAYER,
        bg3.SPEAKER_PLAYER,
        bg3.dialog_object.ABILITY_CHARISMA,
        bg3.dialog_object.SKILL_PERFORMANCE,
        bg3.DC_Act3_Easy,
        narrator_calm_down_node_uuid,
        narrator_rage_continues_node_uuid,
        bg3.text_content('h70cb2f3eg7015g4e6cgadd5gca8da9ec43df', 1))

    # Get yourself together and calm down.
    d.create_standard_dialog_node(
        get_yourself_together_node_uuid,
        bg3.SPEAKER_PLAYER,
        [narrator_calm_down_node_uuid],
        bg3.text_content('h5bed744cgf88fg416ega31dg27853909f664', 1),
        constructor = bg3.dialog_object.QUESTION)

    # Give in to emotions.
    d.create_standard_dialog_node(
        give_in_to_emotions_node_uuid,
        bg3.SPEAKER_PLAYER,
        [violent_resolution_node_uuid],
        bg3.text_content('h0d6265a0gfce2g48c8gb6f2g9905ba2d35ee', 1),
        constructor = bg3.dialog_object.QUESTION)

    # Kick his balls or punch his face.
    d.create_standard_dialog_node(
        violent_resolution_node_uuid,
        bg3.SPEAKER_PLAYER,
        [give_in_to_emotions_short_node_uuid, give_in_to_emotions_female_node_uuid, knock_em_out_node_uuid],
        None,
        approval_rating_uuid = shadowheart_approval_minus_1.uuid,
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(Halsins_Ass_Kicked.uuid, True, speaker_idx_tav),
                bg3.flag(Halsins_Leaves_Party.uuid, True, speaker_idx_tav)
            )),
        ))

    # Do not kick his balls of punch his face.
    d.create_standard_dialog_node(
        non_violent_resolution_node_uuid,
        bg3.SPEAKER_PLAYER,
        [reconsider_your_life_choices_node_uuid, habit_of_intruding_into_private_node_uuid, this_is_ours_leave_us_alone_node_uuid],
        None,
        approval_rating_uuid = shadowheart_approval_plus_5.uuid)

    # *A sense of calm settles in your heart.*
    d.create_standard_dialog_node(
        narrator_calm_down_node_uuid,
        bg3.SPEAKER_NARRATOR,
        [non_violent_resolution_node_uuid],
        bg3.text_content('ha249048dg6626g4111gb9f5g65be1071395a', 1))

    phase_duration = '3.5'
    t.create_new_phase(narrator_calm_down_node_uuid, phase_duration)
    t.create_tl_shot('8e0c85c8-0771-469e-bdf7-a7787a810515', '0.0', phase_duration, is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.EMOTION, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        t.create_emotion_key(0.0, 1),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.ATTITUDE, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.ATTITUDE, bg3.SPEAKER_HALSIN, '0.0', phase_duration, (), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.LOOK_AT, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        t.create_look_at_key(
            0.0,
            target = bg3.SPEAKER_HALSIN,
            bone = 'Head_M',
            turn_mode = 3,
            turn_speed_multiplier = 0.3,
            head_turn_speed_multiplier = 0.3,
            weight = 0.3,
            reset = True,
            is_eye_look_at_enabled = True,
            eye_look_at_target_id = bg3.SPEAKER_HALSIN,
            eye_look_at_bone = 'Head_M'
        ),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.LOOK_AT, bg3.SPEAKER_HALSIN, '0.0', phase_duration, (
        t.create_look_at_key(
            0.0,
            target = bg3.SPEAKER_PLAYER,
            bone = 'Head_M',
            turn_mode = 3,
            turn_speed_multiplier = 0.3,
            head_turn_speed_multiplier = 0.3,
            weight = 0.3,
            reset = True,
            is_eye_look_at_enabled = True,
            eye_look_at_target_id = bg3.SPEAKER_HALSIN,
            eye_look_at_bone = 'Head_M'
        ),
    ), is_snapped_to_end = True)
    t.create_tl_voice(bg3.SPEAKER_NARRATOR, '0.0', '3.07', narrator_calm_down_node_uuid, is_snapped_to_end = True)

    # *Your efforts have no effect.*
    d.create_standard_dialog_node(
        narrator_rage_continues_node_uuid,
        bg3.SPEAKER_NARRATOR,
        [violent_resolution_node_uuid],
        bg3.text_content('hadbb156ag8ecag45d6g93b0gdc9e2a5e124c', 1))

    phase_duration = '2.3'
    t.create_new_phase(narrator_rage_continues_node_uuid, phase_duration)
    t.create_tl_shot('8e0c85c8-0771-469e-bdf7-a7787a810515', '0.0', phase_duration, is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.EMOTION, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        t.create_emotion_key(0.0, 1),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.ATTITUDE, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.ATTITUDE, bg3.SPEAKER_HALSIN, '0.0', phase_duration, (), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.LOOK_AT, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        t.create_look_at_key(
            0.0,
            target = bg3.SPEAKER_HALSIN,
            bone = 'Head_M',
            turn_mode = 3,
            turn_speed_multiplier = 0.3,
            head_turn_speed_multiplier = 0.3,
            weight = 0.3,
            reset = True,
            is_eye_look_at_enabled = True,
            eye_look_at_target_id = bg3.SPEAKER_HALSIN,
            eye_look_at_bone = 'Head_M'
        ),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.LOOK_AT, bg3.SPEAKER_HALSIN, '0.0', phase_duration, (
        t.create_look_at_key(
            0.0,
            target = bg3.SPEAKER_PLAYER,
            bone = 'Head_M',
            turn_mode = 3,
            turn_speed_multiplier = 0.3,
            head_turn_speed_multiplier = 0.3,
            weight = 0.3,
            reset = True,
            is_eye_look_at_enabled = True,
            eye_look_at_target_id = bg3.SPEAKER_HALSIN,
            eye_look_at_bone = 'Head_M'
        ),
    ), is_snapped_to_end = True)
    t.create_tl_voice(bg3.SPEAKER_NARRATOR, '0.0', '1.71', narrator_rage_continues_node_uuid, is_snapped_to_end = True)

    # If the only reason why you're here is to hit on me or Shadowheart, you have to reconsider your life choices. Leave us alone.
    d.create_standard_dialog_node(
        reconsider_your_life_choices_node_uuid,
        bg3.SPEAKER_PLAYER,
        [creep_stays_node_uuid, creep_must_say_farewell_node_uuid],
        bg3.text_content('hd61ea635g70b7g4dbega2cbg8579d2119875', 1),
        constructor = bg3.dialog_object.QUESTION)

    # You have a habit of intruding into private matters of your companions. Either stop that, or leave.
    d.create_standard_dialog_node(
        habit_of_intruding_into_private_node_uuid,
        bg3.SPEAKER_PLAYER,
        [creep_stays_node_uuid, creep_must_say_farewell_node_uuid],
        bg3.text_content('hb039e2cdgda49g40bfg9419g2784b93a1f4c', 1),
        constructor = bg3.dialog_object.QUESTION)

    # What I and Shadowheart share, this is ours, and only ours. Please, leave us alone. Return to your own life.
    d.create_standard_dialog_node(
        this_is_ours_leave_us_alone_node_uuid,
        bg3.SPEAKER_PLAYER,
        [creep_stays_node_uuid, creep_must_say_farewell_node_uuid],
        bg3.text_content('h8d2960f1gbbd7g41e1g8972gfa991f70516f', 1),
        constructor = bg3.dialog_object.QUESTION)

    d.create_standard_dialog_node(
        creep_stays_node_uuid,
        bg3.SPEAKER_HALSIN,
        [creep_simple_no_node_uuid],
        None,
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_Approval_AtLeast_20_For_Sp2, True, speaker_idx_creep),
            )),
        ))

    """
    8e0c85c8-0771-469e-bdf7-a7787a810515 Tav -> Tav
    f1729ce3-4ef3-4fc6-b8d3-ecc8b14305c8 Tav -> Tav
    f26f44f0-f224-445e-b753-9cad18c4970b Creep -> Tav
    d6fa1bdc-4438-43c8-9934-906090970e86 Creep -> Tav
    b1c01ea8-ffa9-45dc-b6f3-2a769cbfc493 Creep -> Tav
    e12c5268-d8db-4934-b492-e0a57333edc8 Creep -> Tav
    7fe134a6-58f5-4359-a95c-b2d9b307dd7b Creep -> Creep
    233735c2-c16c-40dd-a1b5-105bca4ca484 Creep -> Creep
    ff762d89-62c9-46cd-9d12-afd0c3bcedd1 Tav -> Creep
    c0021c6a-f0da-42fd-b4a4-a14105dedf33 Tav -> Creep
    381b21bc-e3f6-4268-991e-d7455b3e3e75 Tav -> Creep
    """

    d.create_standard_dialog_node(
        give_in_to_emotions_short_node_uuid,
        bg3.SPEAKER_PLAYER,
        [kick_em_in_the_balls_node_uuid],
        None,
        checkflags = (
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_SHORT, True, speaker_idx_tav),
            )),
        ))
    d.create_standard_dialog_node(
        give_in_to_emotions_female_node_uuid,
        bg3.SPEAKER_PLAYER,
        [kick_em_in_the_balls_node_uuid],
        None,
        checkflags = (
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_FEMALE, True, speaker_idx_tav),
                bg3.flag(bg3.TAG_BODYTYPE_STRONG, False, speaker_idx_tav)
            )),
        ))

    # Cinematic node: knock'em out
    d.create_cinematic_dialog_node(
        knock_em_out_node_uuid,
        [apply_kocked_out_status_node_uuid])

    phase_duration = '7.0' #5.92
    t.create_new_phase(knock_em_out_node_uuid, phase_duration)
    t.create_tl_transform(bg3.SPEAKER_HALSIN, '0.0', phase_duration, (
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 0.0),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 0.0),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = -0.83),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = (0.0, 1.0, 0.0, 0.0)),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 1),
        ),
        (),
    ))
    t.create_tl_transform(bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 0.0),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 0.25),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 0.44),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = (0.0, 0.0, 0.0, 1.0)),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 1),
        ),
        (),
    ))
    t.create_tl_non_actor_node(bg3.timeline_object.SWITCH_STAGE, '0.0', phase_duration, (), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.LOOK_AT, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        t.create_look_at_key(
            0.0,
            target = bg3.SPEAKER_HALSIN,
            bone = 'Head_M',
            turn_mode = 3,
            turn_speed_multiplier = 0.3,
            head_turn_speed_multiplier = 0.3,
            weight = 0.3,
            reset = True,
            is_eye_look_at_enabled = True,
            eye_look_at_target_id = bg3.SPEAKER_HALSIN,
            eye_look_at_bone = 'Head_M'
        ),
    ))
    t.create_tl_actor_node(bg3.timeline_object.SOUND, bg3.SPEAKER_HALSIN, '0.0', phase_duration, (
        t.create_sound_event_key(1.16, sound_event_id = '49489c19-220f-cd9f-e2df-08d32db96c48', sound_object_index = 3),
        t.create_sound_event_key(1.82, sound_event_id = '309d9e8b-d4ad-68cd-7289-e363dcf30d3e', sound_object_index = 3),
    ))
    t.create_tl_actor_node(bg3.timeline_object.SOUND, bg3.SPEAKER_HALSIN, '0.0', phase_duration, (
        t.create_sound_event_key(1.91, sound_type = 5, vocal_type = 1),
    ))
    t.create_tl_actor_node(bg3.timeline_object.SOUND, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        t.create_sound_event_key(0.75, sound_event_id = 'f57e29cd-6157-4b25-bf06-02d96a3fbe66', sound_object_index = 1),
    ))
    t.create_tl_actor_node(bg3.timeline_object.SOUND, bg3.SPEAKER_HALSIN, '0.0', phase_duration, (
        t.create_sound_event_key(2.02, sound_type = 4, foley_intensity = 1),
    ))
    t.create_tl_actor_node(bg3.timeline_object.PHYSICS, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        t.create_value_key(time = 0.0, interpolation_type = 3, value_name = 'InverseKinematics', value = False),
    ), is_snapped_to_end = True)
    t.create_tl_camera_fov('c0021c6a-f0da-42fd-b4a4-a14105dedf33', '0.0', phase_duration, (
        t.create_value_key(time = 0.0, value_name = 'FoV', value = 35.0, interpolation_type = 2),
    ), is_snapped_to_end = True)
    t.create_tl_shot('c0021c6a-f0da-42fd-b4a4-a14105dedf33', '0.0', '1.85', is_snapped_to_end = True)
    t.create_tl_animation(
        bg3.SPEAKER_PLAYER, '0.0', phase_duration, #3.02,
        'dbf7c8a1-1ef3-4a19-9d60-cf714ed9b122',
        'f79d2f85-cd94-42b7-ba2b-fc2b6943aff7',
        animation_play_rate = 0.8,
        fade_in = 0.0,
        fade_out = 1.5,
        offset_type = 5,
        enable_root_motion = True)
    t.create_tl_animation(
        bg3.SPEAKER_HALSIN, '0.0', '1.85', #0.85, 1.69
        '2ce8d3d3-a079-449e-9d6d-6d4ea91e3e7f',
        'bdbcb0fb-31a4-496b-a8aa-8722edad0150',
        animation_play_rate = 0.8,
        animation_play_start_offset = 0.6, #0.3375, #1.4,#1.57,
        offset_type = 5,
        fade_in = 1.0,
        fade_out = 0.0,
        enable_root_motion = True,
        hold_animation = True)

    t.create_tl_transform('381b21bc-e3f6-4268-991e-d7455b3e3e75', '0.0', phase_duration, (
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = -0.5),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 1.9),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 0.5),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = bg3.euler_to_quaternion(-200.0, 50.0, 0.0, sequence = "yxz")),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 1),
        ),
        (),
    ))
    t.create_tl_camera_fov('381b21bc-e3f6-4268-991e-d7455b3e3e75', '0.0', phase_duration, (
        t.create_value_key(time = 0.0, value_name = 'FoV', value = 30.0, interpolation_type = 2),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.SHOW_VISUAL, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        t.create_value_key(time = 1.85, interpolation_type = 3, value_name = 'ShowVisual', value = False),
        t.create_value_key(time = 4.2, interpolation_type = 3),
    ))
    t.create_tl_shot('381b21bc-e3f6-4268-991e-d7455b3e3e75', '1.85', '4.2')
    t.create_tl_animation(
        bg3.SPEAKER_HALSIN, '1.85', '3.19',
        '7f390901-5eb0-165d-fda2-d0134d61504d',
        'bdbcb0fb-31a4-496b-a8aa-8722edad0150',
        animation_play_start_offset = 0.9,
        offset_type = 2,
        fade_in = 0.0,
        fade_out = 0.0,
        enable_root_motion = True,
        hold_animation = True)

    t.create_tl_shot('8e0c85c8-0771-469e-bdf7-a7787a810515', '4.2', phase_duration, is_snapped_to_end = True)


    #t.create_tl_shot('f1729ce3-4ef3-4fc6-b8d3-ecc8b14305c8', 3.19, phase_duration, is_snapped_to_end = True)


    # t.create_tl_camera_fov('ff762d89-62c9-46cd-9d12-afd0c3bcedd1', 3.19, phase_duration, (
    #     t.create_value_key(time = 3.19, value_name = 'FoV', value = 35.0, interpolation_type = 2),
    # ), is_snapped_to_end = True)
    # t.create_tl_shot('ff762d89-62c9-46cd-9d12-afd0c3bcedd1', 3.19, phase_duration, is_snapped_to_end = True)
    # t.create_tl_animation(
    #     bg3.SPEAKER_HALSIN, 1.69, 3.19,
    #     '7f390901-5eb0-165d-fda2-d0134d61504d',
    #     'bdbcb0fb-31a4-496b-a8aa-8722edad0150',
    #     animation_play_start_offset = 0.9,
    #     offset_type = 2,
    #     fade_in = 0.0,
    #     fade_out = 0.0,
    #     enable_root_motion = True,
    #     hold_animation = True)
    # t.create_tl_animation(
    #     bg3.SPEAKER_PLAYER, 3.02, 5.92,
    #     '06b2457d-fd6e-42c0-b8d9-527dfe61d005',
    #     'f79d2f85-cd94-42b7-ba2b-fc2b6943aff7',
    #     animation_play_rate = 0.13,
    #     fade_in = 0.0,
    #     fade_out = 2.0,
    #     enable_root_motion = True)

    d.create_standard_dialog_node(
        apply_kocked_out_status_node_uuid,
        bg3.SPEAKER_PLAYER,
        [],
        None,
        end_node = True,
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(Halsin_Knocked_Out.uuid, True, speaker_idx_tav),
            )),
        ))


    # Cinematic node: kick'em in balls
    d.create_standard_dialog_node(
        kick_em_in_the_balls_node_uuid,
        bg3.SPEAKER_HALSIN,
        [fuck_right_off_node_uuid, look_with_disdain_node_uuid],
        bg3.text_content('hb6f8b00fg8bd2g4a0dg973bg58b5fe96021a', 1))

    phase_duration = '11.85'
    t.create_new_phase(kick_em_in_the_balls_node_uuid, phase_duration)
    t.create_tl_non_actor_node(bg3.timeline_object.SWITCH_STAGE, '0.0', phase_duration, (), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.LOOK_AT, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        t.create_look_at_key(
            0.0,
            target = bg3.SPEAKER_HALSIN,
            bone = 'Head_M',
            turn_mode = 3,
            turn_speed_multiplier = 0.3,
            head_turn_speed_multiplier = 0.3,
            weight = 0.3,
            reset = True,
            is_eye_look_at_enabled = True,
            eye_look_at_target_id = bg3.SPEAKER_HALSIN,
            eye_look_at_bone = 'Head_M'
        ),
    ))
    # b1c01ea8-ffa9-45dc-b6f3-2a769cbfc493
    #camera1 = 'ff762d89-62c9-46cd-9d12-afd0c3bcedd1'
    camera1 = 'c0021c6a-f0da-42fd-b4a4-a14105dedf33'
    camera2 = '233735c2-c16c-40dd-a1b5-105bca4ca484'
    camera3 = '8e0c85c8-0771-469e-bdf7-a7787a810515'
    t.create_tl_actor_node(bg3.timeline_object.ATTITUDE, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        t.create_attitude_key(8.7, '8128cb03-b18f-46c9-aca9-1c93991cf4ef', bg3.ATTITUDE_DIAG_T_Pose),
    ))
    t.create_tl_actor_node(bg3.timeline_object.EMOTION, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        t.create_emotion_key(0.0, 8),
        t.create_emotion_key(9.5, 128, 1),
    ))
    t.create_tl_actor_node(bg3.timeline_object.EMOTION, bg3.SPEAKER_HALSIN, '0.0', phase_duration, (
        t.create_emotion_key(0.0, 4),
        t.create_emotion_key(1.5, 16, variation = 1),
        t.create_emotion_key(2.1, 2048, variation = 2),
        t.create_emotion_key(3.0, 2048, variation = 23),
        t.create_emotion_key(7.67, 2048, variation = 1),
        t.create_emotion_key(11.3, 8, variation = 2),
    ))
    t.create_tl_camera_fov(camera1, '0.0', phase_duration, (
        t.create_value_key(time = 0.0, value_name = 'FoV', value = 50.0, interpolation_type = 2),
    ), is_snapped_to_end = True)
    t.create_tl_camera_fov(camera3, '0.0', phase_duration, (
        t.create_value_key(time = 8.5, value_name = 'FoV', value = 45.0, interpolation_type = 2),
    ), is_snapped_to_end = True)
    t.create_tl_shot(camera1, '0.0', '3.5')
    t.create_tl_animation(
        bg3.SPEAKER_PLAYER, '0.0', '4.62',
        '9f24f4c1-1381-494c-ae2d-bc7cd85962a0',
        'ea59c5d3-b030-4a42-97df-0720ed3dc49c',
        fade_in = 0.0,
        fade_out = 1.0,
        offset_type = 5,
        enable_root_motion = True)
    t.create_tl_actor_node(bg3.timeline_object.SOUND, bg3.SPEAKER_PLAYER, '0.0', '4.62', (
        t.create_sound_event_key(0.87, sound_event_id = '544582c8-5564-4f86-a29d-2e39096f41b9'),
    ))
    t.create_tl_voice(
        bg3.SPEAKER_HALSIN, '1.0', '10.975',
        kick_em_in_the_balls_node_uuid)
    t.create_tl_shot(camera2, '3.5', '8.5')
    t.create_tl_shot(camera3, '8.5', phase_duration, is_snapped_to_end = True)

    d.create_standard_dialog_node(
        fuck_right_off_node_uuid,
        bg3.SPEAKER_PLAYER,
        [creep_runs_away_node_uuid],
        bg3.text_content('h63d7fa35g92c7g494cg9c10g6ad1182f85ec', 1),
        constructor = bg3.dialog_object.QUESTION)

    d.create_standard_dialog_node(
        look_with_disdain_node_uuid,
        bg3.SPEAKER_PLAYER,
        [creep_runs_away_node_uuid],
        bg3.text_content('h77628de1g5524g4f70g9fd4gff8298ee2ffe', 1),
        constructor = bg3.dialog_object.QUESTION)

    # Then I must say farewell.
    d.create_standard_dialog_node(
        creep_must_say_farewell_node_uuid,
        bg3.SPEAKER_HALSIN,
        [creep_says_farewell_node_uuid],
        bg3.text_content('h6ed7349dg97fbg4478g8232g573bfc8815d1', 2))
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_HALSIN,
        '3.88',
        creep_must_say_farewell_node_uuid,
        ((None, 'c0021c6a-f0da-42fd-b4a4-a14105dedf33'),),
        emotions = {
            bg3.SPEAKER_HALSIN: ((0.0, 1, None),),
        },
        phase_duration = '4.2')

    # May the Oak Father preserve you throughout the challenges that await. You shall be in my prayers, always.
    d.create_standard_dialog_node(
        creep_says_farewell_node_uuid,
        bg3.SPEAKER_HALSIN,
        [],
        bg3.text_content('he2d5483ag3ed8g4a4eg853bg34a563fa1f63', 2),
        end_node = True,
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(Companion_Permanently_Leaves_Party.uuid, True, speaker_idx_creep),
            )),
            bg3.flag_group('Object', (
                bg3.flag(Creep_Ran_Away.uuid, True, speaker_idx_tav),
            )),
        ))
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_HALSIN,
        '8.55',
        creep_says_farewell_node_uuid,
        ((None, '381b21bc-e3f6-4268-991e-d7455b3e3e75'),),
        emotions = {
            bg3.SPEAKER_HALSIN: ((0.0, 1, None),),
        },
        phase_duration = '9.0')


    # Farewell. May the Oak Father keep you - for I will not.
    d.create_standard_dialog_node(
        creep_runs_away_node_uuid,
        bg3.SPEAKER_HALSIN,
        [],
        bg3.text_content('h7d3baca3g988cg43bfg9d0ag3b0f38a96310', 1),
        end_node = True,
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(Companion_Permanently_Leaves_Party.uuid, True, speaker_idx_creep),
            )),
        ))

    phase_duration = '6.2'
    t.create_new_phase(creep_runs_away_node_uuid, phase_duration)
    t.create_tl_non_actor_node(bg3.timeline_object.SWITCH_STAGE, '0.0', phase_duration, (), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.LOOK_AT, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        t.create_look_at_key(
            0.0,
            target = bg3.SPEAKER_HALSIN,
            bone = 'Head_M',
            turn_mode = 3,
            turn_speed_multiplier = 0.3,
            head_turn_speed_multiplier = 0.3,
            weight = 0.3,
            reset = True,
            is_eye_look_at_enabled = True,
            eye_look_at_target_id = bg3.SPEAKER_HALSIN,
            eye_look_at_bone = 'Head_M'
        ),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.LOOK_AT, bg3.SPEAKER_HALSIN, '0.0', phase_duration, (), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.EMOTION, bg3.SPEAKER_HALSIN, '0.0', phase_duration, (
        t.create_emotion_key(0.0, 4),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.EMOTION, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        t.create_emotion_key(0.0, 4),
    ), is_snapped_to_end = True)
    t.create_tl_voice(bg3.SPEAKER_HALSIN, '0.0', phase_duration, creep_runs_away_node_uuid, is_snapped_to_end = True)
    t.create_tl_shot('381b21bc-e3f6-4268-991e-d7455b3e3e75', '0.0', phase_duration, is_snapped_to_end = True)


    #
    # Halsin leaves the party instead of a warning
    #

    # The first warning
    # d = bg3.dialog_object(files.get_file('Gustav', 'Mods/GustavDev/Story/DialogsBinary/Companions/Halsin_Warning1.lsf'))
    # t = bg3.timeline_object(files.get_file('Gustav', 'Public/GustavDev/Timeline/Generated/Halsin_Warning1.lsf'), d)

    ab = game_assets.get_modded_dialog_asset_bundle('Halsin_Warning1')
    d = bg3.dialog_object(ab.dialog)
    t = bg3.timeline_object(ab.timeline, d)

    speaker_idx_tav = d.get_speaker_slot_index(bg3.SPEAKER_PLAYER)
    speaker_idx_creep = d.get_speaker_slot_index(bg3.SPEAKER_HALSIN)

    halsin_fucks_off_entry_node_uuid = '78ad4c71-7a5c-4f28-82d7-50904e9098ac'
    halsin_fucks_off_voice_node_uuid = '1a4c5a42-3f18-44e1-8b74-15cbe24fad46'

    d.create_standard_dialog_node(
        halsin_fucks_off_entry_node_uuid,
        bg3.SPEAKER_HALSIN,
        [halsin_fucks_off_voice_node_uuid],
        None,
        constructor = bg3.dialog_object.GREETING,
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(Halsins_Leaves_Party.uuid, True, speaker_idx_tav),
            )),
        ),
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(Creep_Ran_Away.uuid, True, speaker_idx_tav),
                bg3.flag(Companion_Permanently_Leaves_Party.uuid, True, speaker_idx_creep),
            )),
        ))

    # This is where we must part ways. I hoped it wouldn't be necessary, but no... I cannot turn a blind eye to your actions any longer.
    d.create_standard_dialog_node(
        halsin_fucks_off_voice_node_uuid,
        bg3.SPEAKER_HALSIN,
        [],
        bg3.text_content('h4fa038f1g1c61g498dga282g32e1d2551fe0', 2),
        end_node = True)
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_HALSIN,
        '11.129',
        halsin_fucks_off_voice_node_uuid,
        ((None, '392a93df-077c-4fc1-a544-47453a460e99'),),
        phase_duration = '11.4',
        emotions = {
            bg3.SPEAKER_HALSIN: ((0.0, 16, None), (1.2, 32, None), (3.0, 16, None), (5.5, 2048, None)),
        })

    d.add_root_node(halsin_fucks_off_entry_node_uuid, index = 0)


    # The second warning
    # d = bg3.dialog_object(files.get_file('Gustav', 'Mods/GustavDev/Story/DialogsBinary/Companions/Halsin_Warning2.lsf'))
    # t = bg3.timeline_object(files.get_file('Gustav', 'Public/GustavDev/Timeline/Generated/Halsin_Warning2.lsf'), d)

    ab = game_assets.get_modded_dialog_asset_bundle('Halsin_Warning2')
    d = bg3.dialog_object(ab.dialog)
    t = bg3.timeline_object(ab.timeline, d)

    speaker_idx_tav = d.get_speaker_slot_index(bg3.SPEAKER_PLAYER)
    speaker_idx_creep = d.get_speaker_slot_index(bg3.SPEAKER_HALSIN)

    halsin_fucks_off_entry_node_uuid = '06fca0b0-5814-43ec-98f3-e67ba63234d8'
    halsin_fucks_off_voice_node_uuid = '4cf99107-29b6-478d-871a-a9f2402126ed'

    d.create_standard_dialog_node(
        halsin_fucks_off_entry_node_uuid,
        bg3.SPEAKER_HALSIN,
        [halsin_fucks_off_voice_node_uuid],
        None,
        constructor = bg3.dialog_object.GREETING,
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(Halsins_Leaves_Party.uuid, True, speaker_idx_tav),
            )),
        ),
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(Creep_Ran_Away.uuid, True, speaker_idx_tav),
                bg3.flag(Companion_Permanently_Leaves_Party.uuid, True, speaker_idx_creep),
            )),
        ))

    # This is where we must part ways. I hoped it wouldn't be necessary, but no... I cannot turn a blind eye to your actions any longer.
    d.create_standard_dialog_node(
        halsin_fucks_off_voice_node_uuid,
        bg3.SPEAKER_HALSIN,
        [],
        bg3.text_content('h4fa038f1g1c61g498dga282g32e1d2551fe0', 2),
        end_node = True)
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_HALSIN,
        '11.129',
        halsin_fucks_off_voice_node_uuid,
        ((None, '6c55974f-ea19-401b-a944-edc7a9e8d1a2'),),
        phase_duration = '11.4',
        emotions = {
            bg3.SPEAKER_HALSIN: ((0.0, 16, None), (1.2, 32, None), (3.0, 16, None), (5.5, 2048, None)),
        })

    d.add_root_node(halsin_fucks_off_entry_node_uuid, index = 0)

    # Halsin leaving
    # d = bg3.dialog_object(files.get_file('Gustav', 'Mods/GustavDev/Story/DialogsBinary/Companions/Halsin_Leaving.lsf'))

    ab = game_assets.get_modded_dialog_asset_bundle('Halsin_Leaving')
    d = bg3.dialog_object(ab.dialog)

    speaker_idx_tav = d.get_speaker_slot_index(bg3.SPEAKER_PLAYER)
    d.set_dialog_flags('8093029c-9481-4744-8b54-39809cd06581', setflags = (
        bg3.flag_group('Object', (
            bg3.flag(Creep_Ran_Away.uuid, True, speaker_idx_tav),
        )),
    ))


def patch_creepy_revenge() -> None:
    ab = game_assets.get_modded_dialog_asset_bundle('CAMP_HalsinsRevenge_CFM')
    d = bg3.dialog_object(ab.dialog)

    was_it_worth_it_node_uuid = '2cea9b40-888e-e78d-ed8f-ade944366bcf'

    attack_node_uuid = '3a1b711b-649f-48ac-87c4-6e31ace77f4d'

    d.create_standard_dialog_node(
        attack_node_uuid,
        bg3.SPEAKER_PLAYER,
        [],
        bg3.text_content('h5d10372dga198g4191g89bcg07c774e0528e', 1),
        constructor = bg3.dialog_object.QUESTION,
        end_node = True)

    d.add_child_dialog_node(was_it_worth_it_node_uuid, attack_node_uuid, 0)


bg3.add_build_procedure('patch_creepy_druid', patch_creepy_druid)
bg3.add_build_procedure('patch_creepy_banter', patch_creepy_banter)
bg3.add_build_procedure('create_post_creepy_banter_scene', create_post_creepy_banter_scene)
bg3.add_build_procedure('patch_creepy_revenge', patch_creepy_revenge)

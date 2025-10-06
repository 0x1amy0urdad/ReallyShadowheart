from __future__ import annotations

import bg3moddinglib as bg3

from .context import game_assets
from .flags import *

########################################################################################
# Cloister of Sombre Embrace
########################################################################################

def patch_cloister_events() -> None:

    ########################################################################################
    # ShadowHeart_InParty2.lsf
    ########################################################################################

    # This is no longer needed

    # d = bg3.dialog_object(files.get_file('Gustav', 'Mods/GustavDev/Story/DialogsBinary/Companions/ShadowHeart_InParty2.lsf'))

    # speaker_idx_tav = d.get_speaker_slot_index(bg3.SPEAKER_PLAYER)
    # speaker_idx_shadowheart = d.get_speaker_slot_index(bg3.SPEAKER_SHADOWHEART)

    # smells_of_the_city_node_uuid = 'a8bfd700-78db-04e4-8bcb-41b90f67aa44'
    # shadowheart_inparty_event_parentpointstart_flag = '56cbbbaa-b2fb-4e49-94a2-24601d19b446'
    # shadowheart_inparty_discussedcitymemories_dialog_flag = '446ce0c9-8bc2-4b87-b45f-504511836148'
    # d.set_dialog_flags(
    #     smells_of_the_city_node_uuid,
    #     setflags = (
    #         bg3.flag_group('Global', (
    #             bg3.flag(bg3.FLAG_ORI_Shadowheart_State_ParentPoints_HasEnoughPoints, True, None),
    #         )),
    #         bg3.flag_group('Dialog', (
    #             bg3.flag(shadowheart_inparty_discussedcitymemories_dialog_flag, True, speaker_idx_tav),
    #         )),
    #         bg3.flag_group('Object', (
    #             bg3.flag(shadowheart_inparty_event_parentpointstart_flag, True, speaker_idx_tav),
    #         ))
    #     ),
    #     checkflags = (
    #         bg3.flag_group('Dialog', (
    #             bg3.flag(shadowheart_inparty_discussedcitymemories_dialog_flag, False, speaker_idx_tav),
    #         )),
    #         bg3.flag_group('Object', (
    #             bg3.flag(Found_Memorable_Locations.uuid, True, speaker_idx_shadowheart),
    #             bg3.flag(bg3.FLAG_ORI_Shadowheart_State_HadParentsPoints, True, speaker_idx_shadowheart),
    #         )),
    #         bg3.flag_group('Global', (
    #             bg3.flag(bg3.FLAG_ORI_Shadowheart_State_RejectShar_KilledParents, False, None),
    #             bg3.flag(bg3.FLAG_ORI_Shadowheart_State_RejectShar_SavedParents, False, None),
    #             bg3.flag(bg3.FLAG_ORI_Shadowheart_State_Shar_SavedParents, False, None),
    #             bg3.flag(bg3.FLAG_ORI_Shadowheart_State_Shar_KilledParents, False, None),
    #         )),
    #     ))

    ########################################################################################
    # LOW_SharGrotto_ViconiaDefeated_OM_Shadowheart_COM.lsf
    ########################################################################################

    # d = bg3.dialog_object(files.get_file('Gustav', 'Mods/GustavDev/Story/DialogsBinary/Companions/Origin_Moments/LOW_SharGrotto_ViconiaDefeated_OM_Shadowheart_COM.lsf'))

    ab = game_assets.get_modded_dialog_asset_bundle('LOW_SharGrotto_ViconiaDefeated_OM_Shadowheart_COM')
    d = bg3.dialog_object(ab.dialog)

    slot_idx_tav = d.get_speaker_slot_index(bg3.SPEAKER_PLAYER)
    slot_idx_shadowheart = d.get_speaker_slot_index(bg3.SPEAKER_SHADOWHEART)

    # flags
    loot_viconias_stuff_true = bg3.flag_group('Object', (bg3.flag(Loot_Viconias_Stuff.uuid, True, slot_idx_tav),))
    loot_viconias_stuff_false = bg3.flag_group('Object', (bg3.flag(Loot_Viconias_Stuff.uuid, False, slot_idx_tav),))

    # dialog nodes
    viconia_node_uuid = '075925ee-5b83-f8ea-d00d-720c57ca6844'
    tav_decision_node_uuid = '2db696a0-5f5a-480a-b968-99c8f066ba64'
    shadowheart_decision_node_uuid = '135d73e9-bb85-5b14-cb28-41c8773237d3'
    kill_her_node_uuid = '300a5cf6-4f96-a4e7-5a1e-58f7b87a5a8f'
    kill_viconia_roll_node_uuid = 'cab06c2b-c320-4d0c-ab66-5e57cd6dc5ba'
    loot_viconias_stuff_node_uuid = '43e67fa4-d42a-412b-a550-924c98829384'
    shadowheart_kills_viconia_node_uuid = 'fbc03324-7fa3-b039-6392-d4ac255c1253'
    shadowheart_spares_viconia_node_uuid = 'ae0948ab-4134-9f9b-b93d-9147090354d3'

    # This dialog node adds an option to loot Viconia's stuff without killing her; it works for both Selune and Shar paths
    d.create_standard_dialog_node(
        loot_viconias_stuff_node_uuid,
        bg3.SPEAKER_PLAYER,
        [],
        bg3.text_content('ha0b56eb6gbc0bg4535g97efga2b7c2671c58', 1),
        constructor=bg3.dialog_object.QUESTION,
        checkflags=(loot_viconias_stuff_false,),
        setflags=(loot_viconias_stuff_true,))

    d.add_child_dialog_node(viconia_node_uuid, loot_viconias_stuff_node_uuid, 0)
    d.add_child_dialog_node(tav_decision_node_uuid, loot_viconias_stuff_node_uuid, 0)
    d.add_child_dialog_node(shadowheart_decision_node_uuid, loot_viconias_stuff_node_uuid, 0)

    # When on Selune path, Shadowheart doesn't want to follow what Viconia taught her;
    # it will require a skill check to make her kill Viconia.
    d.create_roll_dialog_node(
        kill_viconia_roll_node_uuid,
        bg3.SPEAKER_PLAYER,
        bg3.SPEAKER_SHADOWHEART,
        bg3.dialog_object.ABILITY_WISDOM,
        bg3.dialog_object.SKILL_RELIGION,
        bg3.DC_Act3_Hard,
        shadowheart_kills_viconia_node_uuid,
        shadowheart_spares_viconia_node_uuid,
        bg3.text_content("h78558948gae13g4d46g936dgf47d53d9fbaf", 2))

    d.delete_child_dialog_node(shadowheart_decision_node_uuid, kill_her_node_uuid)
    d.add_child_dialog_node(shadowheart_decision_node_uuid, kill_viconia_roll_node_uuid)

    ########################################################################################
    # Selunite Shadowheart saves parents
    ########################################################################################

    ########################################################################################
    # LOW_SharGrotto_ParentsFate_OM_Shadowheart_COM.lsf
    ########################################################################################

    # d = bg3.dialog_object(files.get_file('Gustav', 'Mods/GustavDev/Story/DialogsBinary/Companions/Origin_Moments/LOW_SharGrotto_ParentsFate_OM_Shadowheart_COM.lsf'))

    ab = game_assets.get_modded_dialog_asset_bundle('LOW_SharGrotto_ParentsFate_OM_Shadowheart_COM')
    d = bg3.dialog_object(ab.dialog)

    slot_idx_tav = d.get_speaker_slot_index(bg3.SPEAKER_PLAYER)
    slot_idx_shadowheart = d.get_speaker_slot_index(bg3.SPEAKER_SHADOWHEART)

    last_hurdle_node_uuid = '4aabcb2b-a3d6-2cb4-1cdf-0eb99e2463ca'
    but_the_curse_node_uuid = '5b7dc260-a93a-e231-efc9-a37f73c60089'
    you_have_great_faith_node_uuid = '34ae1c3e-8cdc-0eb0-00fa-773859e5645d'
    you_have_great_faith_adv_node_uuid = 'd61a9f9c-c241-4e6f-880a-077f01659262'
    you_can_endure_it_node_uuid = '1db6f59d-8002-109b-f915-d89a73c2de37'
    you_can_endure_it_adv_node_uuid = '90e91f1f-c526-40a1-baa8-536e48e20c2b'
    this_is_your_choice_node_uuid = '1f8d3b87-6a24-cc6c-11c3-684cf1bcdfef'
    remain_silent_node_uuid = 'c3a6e897-7565-25d4-ef70-24a968e9785b'
    is_this_truly_what_you_want_node_uuid = '13a9c749-b989-b71d-760c-c2a55796e202'
    you_should_end_their_suffering_node_uuid = '502739a5-ba58-d164-f793-d18c14dd8bf6'
    and_replace_it_with_another_node_uuid = '0001265e-7823-7e88-d1d3-bb16e735ac67'
    your_father_is_right_node_uuid = 'cba612bc-d577-8782-683e-d7797679320d'
    you_will_be_free_node_uuid = '6b7c30e5-d0c6-be55-c927-f1d62fc602be'
    dont_ask_me_to_kill_my_parents_node_uuid = '0686e3dc-23d6-4920-df64-2f3bbb9707fd'
    passive_check_bypass_node_uuid = 'af524645-8414-42a6-8276-79dc5fe59542'
    passive_check_node_uuid = '7b93af0a-5690-44d6-873d-c370ee4d544b'
    i_need_to_obey_my_parents_wishes = '4f4ac30c-45c4-283d-c696-b2bee39d1c2b'

    d.set_dialog_flags(last_hurdle_node_uuid, checkflags=(
        bg3.flag_group('Global', (
            bg3.flag(bg3.FLAG_ORI_Shadowheart_State_EnemyOfSharPath, True, None),
        )),
    ))

    #do_not_lose_your_parents_node_uuid = '6d67773e-2681-77f0-9dcd-0f206794e6ff'
    #d.delete_all_children_dialog_nodes(do_not_lose_your_parents_node_uuid)
    #d.add_child_dialog_node(do_not_lose_your_parents_node_uuid, last_hurdle_node_uuid)

    bg3.set_bg3_attribute(d.find_dialog_node(you_have_great_faith_node_uuid), 'DifficultyClassID', bg3.DC_Act3_Medium)
    bg3.set_bg3_attribute(d.find_dialog_node(you_can_endure_it_node_uuid), 'DifficultyClassID', bg3.DC_Act3_Medium)

    d.set_dialog_flags(you_have_great_faith_node_uuid, checkflags = (
        bg3.flag_group('Object', (
            bg3.flag(bg3.FLAG_ORI_State_PartneredWithShadowheart, False, slot_idx_tav),
        )),
    ))
    d.set_dialog_flags(you_can_endure_it_node_uuid, checkflags = (
        bg3.flag_group('Object', (
            bg3.flag(bg3.FLAG_ORI_State_PartneredWithShadowheart, False, slot_idx_tav),
        )),
    ))

    # You can endure it together, as a family. This is what you've been looking for - don't deny yourself.
    d.create_roll_dialog_node(
        you_can_endure_it_adv_node_uuid,
        bg3.SPEAKER_PLAYER,
        bg3.SPEAKER_SHADOWHEART,
        bg3.dialog_object.ABILITY_CHARISMA,
        bg3.dialog_object.SKILL_PERSUASION,
        bg3.DC_Act3_Medium,
        last_hurdle_node_uuid,
        i_need_to_obey_my_parents_wishes,
        bg3.text_content("h36917627gd2e7g45fdgab50g2271e3c33799", 2),
        advantage = 1,
        advantage_reason = ('he7d56031g63c2g4a69gacdcg1151b2bfc3b1', 1),
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_State_PartneredWithShadowheart, True, slot_idx_tav),
            )),
        ))

    # You have great faith and great resolve - all of you. Trust in that. You need not say goodbye here.
    d.create_roll_dialog_node(
        you_have_great_faith_adv_node_uuid,
        bg3.SPEAKER_PLAYER,
        bg3.SPEAKER_SHADOWHEART,
        bg3.dialog_object.ABILITY_WISDOM,
        bg3.dialog_object.SKILL_RELIGION,
        bg3.DC_Act3_Medium,
        last_hurdle_node_uuid,
        i_need_to_obey_my_parents_wishes,
        bg3.text_content("h37813951g6489g4e4fg90ecge3150692b4c3", 1),
        advantage = 1,
        advantage_reason = ('he7d56031g63c2g4a69gacdcg1151b2bfc3b1', 1),
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_State_PartneredWithShadowheart, True, slot_idx_tav),
            )),
        ))

    d.add_child_dialog_node(but_the_curse_node_uuid, you_have_great_faith_adv_node_uuid)
    d.add_child_dialog_node(but_the_curse_node_uuid, you_can_endure_it_adv_node_uuid)

    d.delete_all_children_dialog_nodes(this_is_your_choice_node_uuid)
    d.add_child_dialog_node(this_is_your_choice_node_uuid, passive_check_bypass_node_uuid)
    d.add_child_dialog_node(this_is_your_choice_node_uuid, passive_check_node_uuid)

    d.delete_all_children_dialog_nodes(remain_silent_node_uuid)
    d.add_child_dialog_node(remain_silent_node_uuid, passive_check_bypass_node_uuid)
    d.add_child_dialog_node(remain_silent_node_uuid, passive_check_node_uuid)

    # You should end their suffering, and yours.
    # DC 20 Charisma/Persuasion check to kill parents.
    d.delete_dialog_node(you_should_end_their_suffering_node_uuid)
    d.create_roll_dialog_node(
        you_should_end_their_suffering_node_uuid,
        bg3.SPEAKER_PLAYER,
        bg3.SPEAKER_SHADOWHEART,
        bg3.dialog_object.ABILITY_CHARISMA,
        bg3.dialog_object.SKILL_PERSUASION,
        bg3.DC_Act3_Hard,
        is_this_truly_what_you_want_node_uuid,
        last_hurdle_node_uuid,
        bg3.text_content("hf7ab97f1g9c21g467bg9feag961801ba37b9", 2))


    # Your father is right. This is the only way to free your family from Shar's curse and stop the pain.
    d.delete_dialog_node(your_father_is_right_node_uuid)
    d.create_standard_dialog_node(
        your_father_is_right_node_uuid,
        bg3.SPEAKER_PLAYER,
        [and_replace_it_with_another_node_uuid],
        bg3.text_content('hc0077229g09edg4ed4gb446g6e6f48cf2363', 1),
        constructor=bg3.dialog_object.QUESTION)

    d.delete_all_children_dialog_nodes(and_replace_it_with_another_node_uuid)
    d.add_child_dialog_node(and_replace_it_with_another_node_uuid, passive_check_bypass_node_uuid)
    d.add_child_dialog_node(and_replace_it_with_another_node_uuid, passive_check_node_uuid)

    # Let your parents die with honour. They will become Selûne's martyrs, and you will be free.
    d.delete_dialog_node(you_will_be_free_node_uuid)
    d.create_standard_dialog_node(
        you_will_be_free_node_uuid,
        bg3.SPEAKER_PLAYER,
        [dont_ask_me_to_kill_my_parents_node_uuid],
        bg3.text_content('h13ebab14g1a05g4971ga118g27bfe03dd22e', 1),
        constructor=bg3.dialog_object.QUESTION)

    d.delete_all_children_dialog_nodes(dont_ask_me_to_kill_my_parents_node_uuid)
    d.add_child_dialog_node(dont_ask_me_to_kill_my_parents_node_uuid, passive_check_bypass_node_uuid)
    d.add_child_dialog_node(dont_ask_me_to_kill_my_parents_node_uuid, passive_check_node_uuid)

    d.create_standard_dialog_node(
        passive_check_bypass_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [last_hurdle_node_uuid],
        None,
        checkflags = (
            bg3.flag_group('Global', (
                bg3.flag(bg3.FLAG_ORI_Shadowheart_State_ParentPoints_HasEnoughPoints, True, None),
            )),
        )
    )

    # DC 15 Wisdom/Religion passive check to save parents.
    d.create_roll_dialog_node(
        passive_check_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        bg3.SPEAKER_PLAYER,
        bg3.dialog_object.ABILITY_WISDOM,
        bg3.dialog_object.SKILL_RELIGION,
        bg3.DC_Act3_Medium,
        last_hurdle_node_uuid,
        is_this_truly_what_you_want_node_uuid,
        None,
        passive=True,
        transition_mode=True,
        advantage=0,
        exclude_companion_bonus=True,
        exclude_speaker_bonus=True)

    ########################################################################################
    # ShadowHeart_InParty2.lsf
    ########################################################################################

    # d = bg3.dialog_object(files.get_file('Gustav', 'Mods/GustavDev/Story/DialogsBinary/Companions/ShadowHeart_InParty2.lsf'))
    # t = bg3.timeline_object(files.get_file('Gustav', 'Public/GustavDev/Timeline/Generated/ShadowHeart_InParty2.lsf'), d)

    ab = game_assets.get_modded_dialog_asset_bundle('ShadowHeart_InParty')
    d = bg3.dialog_object(ab.dialog)
    t = bg3.timeline_object(ab.timeline, d)

    slot_idx_shadowheart = d.get_speaker_slot_index(bg3.SPEAKER_SHADOWHEART)
    slot_idx_tav = d.get_speaker_slot_index(bg3.SPEAKER_PLAYER)


    #######################################################################################
    # After the events in the Chamber of Loss, Shadowheart stays in camp until long rest
    #######################################################################################

    # Shadowheart will keep saying this until long rest

    # Give me a night, to try and get my head together.
    give_me_a_night_node_uuid = 'bcfdf718-6d56-45fa-ab0a-967b0f11abfa'
    d.create_standard_dialog_node(
        give_me_a_night_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [],
        bg3.text_content('h11c7cf31ga874g4f1bgb4e6gf6d126ea12da', 2),
        constructor = bg3.dialog_object.GREETING,
        root = True,
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(Shadowheart_After_Parents_Crisis.uuid, True, slot_idx_shadowheart),
                bg3.flag(Shadowheart_Cried_After_Parents.uuid, False, slot_idx_shadowheart),
            )),
        ),
        end_node = True)
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '3.47',
        give_me_a_night_node_uuid,
        ((None, '0e8837db-4344-48d0-9175-12262c73806b'),),
        emotions={
            bg3.SPEAKER_SHADOWHEART: ((0.0, 32, 1), (2.06, 2048, 1))
        })

    # This new node has the top priority.
    d.add_root_node(give_me_a_night_node_uuid, index=0)


    #######################################################################################
    # The following sets the flag for the line above to trigger
    #######################################################################################

    #######################################################################################
    # ShadowHeart_InParty2_Nested_CityChapter.lsf
    #######################################################################################

    # d = bg3.dialog_object(files.get_file('Gustav', 'Mods/GustavDev/Story/DialogsBinary/Companions/ShadowHeart_InParty2_Nested_CityChapter.lsf'))

    ab = game_assets.get_modded_dialog_asset_bundle('ShadowHeart_InParty2_Nested_CityChapter')
    d = bg3.dialog_object(ab.dialog)

    slot_idx_shadowheart = d.get_speaker_slot_index(bg3.SPEAKER_SHADOWHEART)
    slot_idx_tav = d.get_speaker_slot_index(bg3.SPEAKER_PLAYER)

    # Enemy of Shar path, killed parents
    d.set_dialog_flags(
        'daa105c0-10cc-4334-a550-9a0103674cc4',
        setflags=(
            bg3.flag_group('Object', (
                bg3.flag(Shadowheart_After_Parents_Crisis.uuid, True, slot_idx_shadowheart),
                bg3.flag(Shadowheart_Cried_After_Parents.uuid, False, slot_idx_shadowheart),
                bg3.flag(bg3.FLAG_OriginRemoveFromPartyAfterDialog, True, slot_idx_shadowheart),
                bg3.flag('d59fe46f-cce5-4a2c-ac44-65cfda9073f2', False, slot_idx_tav) # Shadowheart_InParty_Event_KilledParentsEnemyStart
            )),
        ))

    # Enemy of Shar path, saved parents
    d.set_dialog_flags(
        '48f77fda-8492-4b65-8a7f-a533388250f6',
        setflags=(
            bg3.flag_group('Object', (
                bg3.flag(Shadowheart_After_Parents_Crisis.uuid, True, slot_idx_shadowheart),
                bg3.flag(Shadowheart_Cried_After_Parents.uuid, False, slot_idx_shadowheart),
                bg3.flag(bg3.FLAG_OriginRemoveFromPartyAfterDialog, True, slot_idx_shadowheart),
                bg3.flag('e3c97bf9-c58c-4dfb-ba8e-27cba587d77d', False, slot_idx_tav) # Shadowheart_InParty_Event_SavedParentsEnemyStart
            )),
        ))

    # Shar path, saved parents
    d.set_dialog_flags(
        'a11549ed-8ffe-417d-a0f4-1ebbe313661d',
        setflags=(
            bg3.flag_group('Object', (
                bg3.flag(Shadowheart_After_Parents_Crisis.uuid, True, slot_idx_shadowheart),
                bg3.flag(Shadowheart_Cried_After_Parents.uuid, False, slot_idx_shadowheart),
                bg3.flag(bg3.FLAG_OriginRemoveFromPartyAfterDialog, True, slot_idx_shadowheart),
                bg3.flag('1e379d40-cd40-4b49-a45f-d9b28c2d0437', False, slot_idx_tav) # Shadowheart_InParty_Event_SavedParentsSharStart
            )),
        ))

    # fix for for Shadowheart's hideout dialog
    my_parents_stil_captive_node_uuid = '24048b6b-b998-42cd-8154-85f03c91d0fe'
    chamber_of_loss_beckons_node_uuid = '4c21f587-8bec-4518-9407-384dd3cdb571'
    hideout_conversation_node_uuid = 'ba4c1693-2117-42ae-85f8-6b34e7036610'
    d.remove_root_node(hideout_conversation_node_uuid)
    d.remove_root_node(chamber_of_loss_beckons_node_uuid)
    idx = d.get_root_node_index(my_parents_stil_captive_node_uuid)
    d.add_root_node(chamber_of_loss_beckons_node_uuid, idx)
    d.add_root_node(hideout_conversation_node_uuid, idx)


def patch_conversation_with_viconia() -> None:
    # d = bg3.dialog_object(files.get_file('Gustav', 'Mods/GustavDev/Story/DialogsBinary/Companions/Origin_Moments/LOW_SharGrotto_ConfrontViconia_OM_Shadowheart_COM.lsf'))

    ab = game_assets.get_modded_dialog_asset_bundle('LOW_SharGrotto_ConfrontViconia_OM_Shadowheart_COM')
    d = bg3.dialog_object(ab.dialog)

    speaker_idx_tav = d.get_speaker_slot_index(bg3.SPEAKER_PLAYER)

    nodes = (
        ('1aeb9de7-a524-ae50-e841-5b712d54963e', 'c874fb35-dec6-473f-a6ce-7bdfa3975628'),
        ('90a28f29-78e3-86a4-b6c8-f36e9854bd54', '9fc8660e-5c10-4724-9da2-a3b5d9606c9b'))
    # The following changes Tav's answers to Viconia when she demands they surrender Shadowheart to her
    for target_node_uuid, new_node_uuid in nodes:
        children = d.get_children_nodes_uuids(target_node_uuid)
        if len(children) == 2:
            d.delete_all_children_dialog_nodes(target_node_uuid)

            empty_tick_node_uuid = bg3.new_random_uuid()

            # YOU WILL CHOKE ON YOUR OWN BLOOD.
            d.create_standard_dialog_node(
                new_node_uuid,
                bg3.SPEAKER_PLAYER,
                d.get_children_nodes_uuids(children[1]),
                #[empty_tick_node_uuid],
                bg3.text_content('h73183838ga5b6g4c78gbc90g273486ca1dc2', 1),
                
                # TODO: remove these after test
                # setflags = (
                #     # bg3.flag_group('Object', (
                #     #     bg3.flag(Betrayer.uuid, True, speaker_idx_tav),
                #     # )),
                #     bg3.flag_group('Global', (
                #         bg3.flag(bg3.FLAG_LOW_SharGrotto_ConfrontViconia_SharranAlliance, True, None),
                #         bg3.flag(bg3.FLAG_LOW_SharGrotto_Event_SurrenderShadowheart, True, None),
                #     )),
                # ),

                constructor = bg3.dialog_object.QUESTION,
                checkflags = (
                    bg3.flag_group('Tag', (
                        bg3.flag(bg3.TAG_REALLY_DARK_URGE, True, speaker_idx_tav),
                    )),
                ))
            d.create_standard_dialog_node(
                empty_tick_node_uuid,
                bg3.SPEAKER_SHADOWHEART,
                [],
                None,
                end_node = True)
            d.add_child_dialog_node(target_node_uuid, new_node_uuid)
            d.add_child_dialog_node(target_node_uuid, children[1])
            d.add_child_dialog_node(target_node_uuid, children[0])
        else:
            raise RuntimeError("Viconia's dialog has changed")

    # shes_all_yours1_node_uuid = '52fcd5a0-32f4-459b-861e-87d2ba448ae6'
    # shes_all_yours2_node_uuid = 'c68050e1-2363-be20-8692-d34f563efc27'
    # d.set_dialog_flags(shes_all_yours1_node_uuid, setflags = (
    #     bg3.flag_group('Object', (
    #         bg3.flag(Betrayer.uuid, True, speaker_idx_tav),
    #     )),
    # ))
    # d.set_dialog_flags(shes_all_yours2_node_uuid, setflags = (
    #     bg3.flag_group('Object', (
    #         bg3.flag(Betrayer.uuid, True, speaker_idx_tav),
    #     )),
    # ))


def patch_conversation_with_mirie() -> None:
    ab = game_assets.get_modded_dialog_asset_bundle('LOW_HouseOfGrief_OM_Shadowheart_COM')
    d = bg3.dialog_object(ab.dialog)

    youd_try_to_flee_like_a_craven_node_uuid = 'a0e563b4-8cb6-2154-61c7-cfaf11abc7b5' # existing node
    spare_me_your_venom_node_uuid = '4b9a4599-e331-ac01-f278-b0b9c3f7bd3f' # existing node
    do_i_know_you_node_uuid = 'f42b88ff-f955-d428-eb58-f008587c2c15' # existing node
    all_in_due_time_node_uuid = 'b86c0789-7dce-501f-b7e1-d0486052e04a' # existing node

    continuation_node_uuid = d.get_children_nodes_uuids(all_in_due_time_node_uuid)[0]

    d.delete_all_children_dialog_nodes(youd_try_to_flee_like_a_craven_node_uuid)
    d.add_child_dialog_node(youd_try_to_flee_like_a_craven_node_uuid, do_i_know_you_node_uuid)

    d.delete_all_children_dialog_nodes(all_in_due_time_node_uuid)
    d.add_child_dialog_node(all_in_due_time_node_uuid, spare_me_your_venom_node_uuid)

    d.delete_all_children_dialog_nodes(spare_me_your_venom_node_uuid)
    d.add_child_dialog_node(spare_me_your_venom_node_uuid, continuation_node_uuid)


def make_late_redemption_easier() -> None:

    ########################################################################################
    # LOW_SharGrotto_ParentsFate_OM_Shadowheart_COM.lsf
    ########################################################################################

    ab = game_assets.get_modded_dialog_asset_bundle('LOW_SharGrotto_ParentsFate_OM_Shadowheart_COM')
    d = bg3.dialog_object(ab.dialog)

    speaker_idx_tav = d.get_speaker_slot_index(bg3.SPEAKER_PLAYER)
    speaker_idx_shadowheart = d.get_speaker_slot_index(bg3.SPEAKER_SHADOWHEART)

    i_have_to_do_it_node_uuid = 'fb1ea58d-ad1c-3b77-db3c-2ae5e5fd7f3f'
    durge_your_whole_life_node_uuid = 'f5f4b7b7-6d69-4efa-a04e-257e1338c946'
    the_unclaimed_node_uuid = 'aa77ee6d-8d69-45f2-ba29-b2e2c049212e'
    disadv_durge_your_whole_life_node_uuid = '86862b69-abcc-41f0-9d71-1e12ba7caf58'
    disadv_the_unclaimed_node_uuid = '080fa912-5b4d-44c5-aad7-15dfda943e6f'
    roll_success_node_uuid = 'd857e295-d97d-e8d4-561d-da88ed98855e' # existing node
    roll_failure_node_uuid = 'f655df64-3fb0-39b1-b64c-12d10abf7b45' # exsiting node

    #
    # New conditional DC skill checks
    #

    d.create_roll_dialog_node(
        durge_your_whole_life_node_uuid,
        bg3.SPEAKER_PLAYER,
        bg3.SPEAKER_SHADOWHEART,
        bg3.dialog_object.ABILITY_WISDOM,
        bg3.dialog_object.SKILL_PERSUASION,
        bg3.DC_Act3_Medium,
        roll_success_node_uuid,
        roll_failure_node_uuid,
        bg3.text_content('h2fecd538g3b31g4d43g9d68g2a532e8bf910', 1),
        advantage = 1,
        advantage_reason = 'h9c9dd9a6gcd6cg4adegbcddg4600f652dc0a',
        checkflags = (
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_REALLY_DARK_URGE, True, speaker_idx_tav),
            )),
            bg3.flag_group('Global', (
                bg3.flag(bg3.FLAG_ORI_DarkUrge_State_BhaalResisted, True, None),
            )),
            bg3.flag_group('Object', (
                bg3.flag(Shadowheart_Lost_Faith_In_Tav.uuid, False, speaker_idx_tav),
            ))
        ))

    d.create_roll_dialog_node(
        the_unclaimed_node_uuid,
        bg3.SPEAKER_PLAYER,
        bg3.SPEAKER_SHADOWHEART,
        bg3.dialog_object.ABILITY_INTELLIGENCE,
        bg3.dialog_object.SKILL_INSIGHT,
        bg3.DC_Act3_Challenging,
        roll_success_node_uuid,
        roll_failure_node_uuid,
        bg3.text_content('h32377027g4a56g47b0ga826gcd17c6ead8aa', 1),
        advantage = 1,
        advantage_reason = 'haf5835e2g1f36g41a2gbfb6ga4b5550676d8',
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(Tav_Gave_Unclaimed_Book_To_Shadowheart.uuid, True, speaker_idx_shadowheart),
            )),
            bg3.flag_group('Object', (
                bg3.flag(Shadowheart_Lost_Faith_In_Tav.uuid, False, speaker_idx_tav),
            ))
        ))

    d.create_roll_dialog_node(
        disadv_durge_your_whole_life_node_uuid,
        bg3.SPEAKER_PLAYER,
        bg3.SPEAKER_SHADOWHEART,
        bg3.dialog_object.ABILITY_WISDOM,
        bg3.dialog_object.SKILL_PERSUASION,
        bg3.DC_Act3_Medium,
        roll_success_node_uuid,
        roll_failure_node_uuid,
        bg3.text_content('h2fecd538g3b31g4d43g9d68g2a532e8bf910', 1),
        advantage = 2,
        advantage_reason = 'h7f65d54fg79d3g4abdgb0c9g2c09b329069a',
        checkflags = (
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_REALLY_DARK_URGE, True, speaker_idx_tav),
            )),
            bg3.flag_group('Global', (
                bg3.flag(bg3.FLAG_ORI_DarkUrge_State_BhaalResisted, True, None),
            )),
            bg3.flag_group('Object', (
                bg3.flag(Shadowheart_Lost_Faith_In_Tav.uuid, True, speaker_idx_tav),
            ))
        ))

    d.create_roll_dialog_node(
        disadv_the_unclaimed_node_uuid,
        bg3.SPEAKER_PLAYER,
        bg3.SPEAKER_SHADOWHEART,
        bg3.dialog_object.ABILITY_INTELLIGENCE,
        bg3.dialog_object.SKILL_INSIGHT,
        bg3.DC_Act3_Challenging,
        roll_success_node_uuid,
        roll_failure_node_uuid,
        bg3.text_content('h32377027g4a56g47b0ga826gcd17c6ead8aa', 1),
        advantage = 2,
        advantage_reason = 'h7f65d54fg79d3g4abdgb0c9g2c09b329069a',
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(Tav_Gave_Unclaimed_Book_To_Shadowheart.uuid, True, speaker_idx_shadowheart),
            )),
            bg3.flag_group('Object', (
                bg3.flag(Shadowheart_Lost_Faith_In_Tav.uuid, True, speaker_idx_tav),
            ))
        ))

    d.add_child_dialog_node(i_have_to_do_it_node_uuid, disadv_the_unclaimed_node_uuid, 0)
    d.add_child_dialog_node(i_have_to_do_it_node_uuid, disadv_durge_your_whole_life_node_uuid, 0)

    d.add_child_dialog_node(i_have_to_do_it_node_uuid, the_unclaimed_node_uuid, 0)
    d.add_child_dialog_node(i_have_to_do_it_node_uuid, durge_your_whole_life_node_uuid, 0)

    #
    # Existing DC skill checks
    #
    your_whole_lifes_been_a_lie_node_uuid = 'b82aaac7-5f4a-a026-0277-1b232fc81c34' # existing node
    its_not_worth_it_node_uuid = '3e9efd38-3e19-66a9-94e6-bb2ad03a0bde' # existing node
    theyre_your_parents_node_uuid = 'dcf68c1f-034c-d0db-3666-3fda730caec8' # existing node

    d.add_dialog_flags(your_whole_lifes_been_a_lie_node_uuid, checkflags = (
        bg3.flag_group('Object', (
            bg3.flag(Shadowheart_Lost_Faith_In_Tav.uuid, False, speaker_idx_tav),
        )),
    ))

    d.add_dialog_flags(its_not_worth_it_node_uuid, checkflags = (
        bg3.flag_group('Object', (
            bg3.flag(Shadowheart_Lost_Faith_In_Tav.uuid, False, speaker_idx_tav),
        )),
    ))

    d.add_dialog_flags(theyre_your_parents_node_uuid, checkflags = (
        bg3.flag_group('Object', (
            bg3.flag(Shadowheart_Lost_Faith_In_Tav.uuid, False, speaker_idx_tav),
        )),
    ))

    #
    # Versions of existing DC skill checks with disadvantage
    #
    disadv_your_whole_lifes_been_a_lie_node_uuid = '8f33d1b4-f3ab-4c46-8bc2-34c3fbf6c4f4'
    disadv_its_not_worth_it_node_uuid = '9e0154a4-8363-45f9-9919-25633f595670'
    disadv_theyre_your_parents_node_uuid = '158c4ed5-c691-4471-aaae-66559403280e'

    # Your whole life's been a lie. You don't have to do this.
    d.create_roll_dialog_node(
        disadv_your_whole_lifes_been_a_lie_node_uuid,
        bg3.SPEAKER_PLAYER,
        bg3.SPEAKER_SHADOWHEART,
        bg3.dialog_object.ABILITY_CHARISMA,
        bg3.dialog_object.SKILL_PERSUASION,
        bg3.DC_Act3_VeryHard,
        roll_success_node_uuid,
        roll_failure_node_uuid,
        bg3.text_content('hbfee06e0ged02g445dgaf1bg8600a8835ec5', 2),
        advantage = 2,
        advantage_reason = 'h7f65d54fg79d3g4abdgb0c9g2c09b329069a',
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(Shadowheart_Lost_Faith_In_Tav.uuid, True, speaker_idx_tav),
            )),
        ))

    d.create_roll_dialog_node(
        disadv_its_not_worth_it_node_uuid,
        bg3.SPEAKER_PLAYER,
        bg3.SPEAKER_SHADOWHEART,
        bg3.dialog_object.ABILITY_WISDOM,
        bg3.dialog_object.SKILL_INSIGHT,
        bg3.DC_Act3_VeryHard,
        roll_success_node_uuid,
        roll_failure_node_uuid,
        bg3.text_content('h44794308gebdbg41c5gb498g04b8cf5b95e9', 2),
        advantage = 2,
        advantage_reason = 'h7f65d54fg79d3g4abdgb0c9g2c09b329069a',
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(Shadowheart_Lost_Faith_In_Tav.uuid, True, speaker_idx_tav),
            )),
        ))

    # They're your parents. They'll forgive you.
    d.create_roll_dialog_node(
        disadv_theyre_your_parents_node_uuid,
        bg3.SPEAKER_PLAYER,
        bg3.SPEAKER_SHADOWHEART,
        bg3.dialog_object.ABILITY_CHARISMA,
        '',
        bg3.DC_Act3_VeryHard,
        roll_success_node_uuid,
        roll_failure_node_uuid,
        bg3.text_content('haaf3a8f7gb81bg469fga9ccgef55de8fe28a', 2),
        roll_type = bg3.dialog_object.ROLL_RAW_ABILITY,
        advantage = 2,
        advantage_reason = 'h7f65d54fg79d3g4abdgb0c9g2c09b329069a',
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(Shadowheart_Lost_Faith_In_Tav.uuid, True, speaker_idx_tav),
            )),
        ))

    d.add_child_dialog_node(i_have_to_do_it_node_uuid, disadv_your_whole_lifes_been_a_lie_node_uuid)
    d.add_child_dialog_node(i_have_to_do_it_node_uuid, disadv_its_not_worth_it_node_uuid)
    d.add_child_dialog_node(i_have_to_do_it_node_uuid, disadv_theyre_your_parents_node_uuid)


bg3.add_build_procedure('patch_cloister_events', patch_cloister_events)
bg3.add_build_procedure('patch_conversation_with_viconia', patch_conversation_with_viconia)
bg3.add_build_procedure('patch_conversation_with_mirie', patch_conversation_with_mirie)
bg3.add_build_procedure('make_late_redemption_easier', make_late_redemption_easier)

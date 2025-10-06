from __future__ import annotations

import bg3moddinglib as bg3

from .context import game_assets
from .flags import *

########################################################################################
# If Tav/Durge betrays Selune Shadowheart and surrenders her to Viconia,
# most companions leave the party, some will attack Tav/Durge.
# Only Minthara supports Tav/Durge.
########################################################################################

def create_betrayal_reactions() -> None:
    ########################################################################################
    # Astarion_InParty2_Nested_TopicalGreetings.lsf
    ########################################################################################

    # d = bg3.dialog_object(files.get_file('Gustav', 'Mods/GustavDev/Story/DialogsBinary/Companions/Astarion_InParty2_Nested_TopicalGreetings.lsf'))
    # t = bg3.timeline_object(files.get_file('Gustav', 'Public/GustavDev/Timeline/Generated/Astarion_InParty2_Nested_TopicalGreetings.lsf'), d)

    ab = game_assets.get_modded_dialog_asset_bundle('Astarion_InParty2_Nested_TopicalGreetings')
    d = bg3.dialog_object(ab.dialog)
    t = bg3.timeline_object(ab.timeline, d)

    d.remove_root_node('ad3ff2ae-3adc-4316-72d1-6cfc06a02ebe')
    d.add_root_node('ad3ff2ae-3adc-4316-72d1-6cfc06a02ebe', index = 0)

    slot_idx_tav = d.get_speaker_slot_index(bg3.SPEAKER_PLAYER)
    slot_idx_astarion = d.get_speaker_slot_index(bg3.SPEAKER_ASTARION)

    astarion_leaves_the_party_node1_uuid = '32f01af7-565f-42bf-8cea-ea06242a46e3'
    astarion_leaves_the_party_node2_uuid = '99f6f338-76c7-4bda-a85f-a37f3d04d3b8'

    d.delete_all_children_dialog_nodes('badf4e3f-f7ee-0d53-6151-572276c72015')
    d.add_child_dialog_node('badf4e3f-f7ee-0d53-6151-572276c72015', astarion_leaves_the_party_node1_uuid)

    # I may not have the moral high ground when it comes to betraying trust, but right now, I see everything I've been trying to escape in you.
    d.create_standard_dialog_node(
        astarion_leaves_the_party_node1_uuid,
        bg3.SPEAKER_ASTARION,
        [astarion_leaves_the_party_node2_uuid],
        bg3.text_content('h56773390g041cg48eag9b75g7f2ee54486be', 2))
    t.create_new_voice_phase_from_another(
        'badf4e3f-f7ee-0d53-6151-572276c72015',
        bg3.SPEAKER_ASTARION,
        '15.15',
        astarion_leaves_the_party_node1_uuid,
        skip_tl_nodes = ('TLShot',),
        emotions = {
            bg3.SPEAKER_ASTARION: ((0.0, 8, None), (4.02, 128, None), (8.17, 32, None), (11.03, 2048, None), (14.37, 8, 1)),
        })
    t.create_tl_shot('b96cdf16-020f-42cf-bfa5-f4f7771675bc', '0.0', '15.15')

    # I'll solve this damn thing myself. You can rot.
    d.create_standard_dialog_node(
        astarion_leaves_the_party_node2_uuid,
        bg3.SPEAKER_ASTARION,
        [],
        bg3.text_content('h574856degf40dg4309g9e78g91462c127473', 1),
        end_node=True,
        setflags=(
            bg3.flag_group('Object', (
                #bg3.flag(bg3.FLAG_Companion_Leaves_Party, True, slot_idx_astarion),
                bg3.flag(Companion_Permanently_Leaves_Party.uuid, True, slot_idx_astarion),
            )),
            bg3.flag_group('Quest', (
                bg3.flag('fefd0416-3508-4af6-9361-80f9048fa312', True, slot_idx_tav),
            )),
        ))
    t.create_new_voice_phase_from_another(
        'badf4e3f-f7ee-0d53-6151-572276c72015',
        bg3.SPEAKER_ASTARION,
        '4.875',
        astarion_leaves_the_party_node2_uuid,
        skip_tl_nodes = ('TLShot',),
        emotions = {
            bg3.SPEAKER_ASTARION: ((0.0, 8, 2),),
        })
    t.create_tl_shot('1cb62d92-33df-451a-b3bf-9eeb1964f6d6', '0.0', '4.875')


    ########################################################################################
    # Gale_InParty2_Nested_TopicalGreetings.lsf
    ########################################################################################

    # d = bg3.dialog_object(files.get_file('Gustav', 'Mods/GustavDev/Story/DialogsBinary/Companions/Gale_InParty2_Nested_TopicalGreetings.lsf'))
    # t = bg3.timeline_object(files.get_file('Gustav', 'Public/GustavDev/Timeline/Generated/Gale_InParty2_Nested_TopicalGreetings.lsf'), d)

    ab = game_assets.get_modded_dialog_asset_bundle('Gale_InParty2_Nested_TopicalGreetings')
    d = bg3.dialog_object(ab.dialog)
    t = bg3.timeline_object(ab.timeline, d)

    d.remove_root_node('dfefbc17-5eb7-bc85-cbaa-31b1b764650e')
    d.add_root_node('dfefbc17-5eb7-bc85-cbaa-31b1b764650e', index = 0)

    slot_idx_tav = d.get_speaker_slot_index(bg3.SPEAKER_PLAYER)
    slot_idx_gale = d.get_speaker_slot_index(bg3.SPEAKER_GALE)

    gale_leaves_the_party_node1_uuid = '2878d45e-d922-48c4-a5af-4ab1600b2d5d'
    gale_leaves_the_party_node2_uuid = '06242693-b363-431a-994a-ca2f70d14b75'
    gale_leaves_the_party_node3_uuid = '26896d4f-70c8-4c82-bfca-9393066c1ce8'

    d.delete_all_children_dialog_nodes('be456d41-4ad1-7e6b-360b-aacc272b2774')
    d.add_child_dialog_node('be456d41-4ad1-7e6b-360b-aacc272b2774', gale_leaves_the_party_node1_uuid)

    # I am a fool. A fool to have trusted you.
    d.create_standard_dialog_node(
        gale_leaves_the_party_node1_uuid,
        bg3.SPEAKER_GALE,
        [gale_leaves_the_party_node2_uuid],
        bg3.text_content('ha61ce3a6g66c5g4099ga29cg048b24c39f5f', 1))
    t.create_new_voice_phase_from_another(
        'be456d41-4ad1-7e6b-360b-aacc272b2774',
        bg3.SPEAKER_GALE,
        '4.5',
        gale_leaves_the_party_node1_uuid,
        skip_tl_nodes = ('TLShot',),
        emotions = {
            bg3.SPEAKER_GALE: ((0.0, 64, None),),
            bg3.SPEAKER_PLAYER: ((1.85, 8, None),),
        })
    t.create_tl_shot('dbc60980-2dde-47c7-8e51-cdb8e42c0e40', '0.0', '4.5')

    # I'd wish you a bright future, but since you cannot escape your own company, that would be a futile gesture.
    d.create_standard_dialog_node(
        gale_leaves_the_party_node2_uuid,
        bg3.SPEAKER_GALE,
        [gale_leaves_the_party_node3_uuid],
        bg3.text_content('hf3386cc0g8cbbg4454ga4d7gb3d832b60ffd', 1))
    t.create_new_voice_phase_from_another(
        'be456d41-4ad1-7e6b-360b-aacc272b2774',
        bg3.SPEAKER_GALE,
        '6.4',
        gale_leaves_the_party_node2_uuid,
        skip_tl_nodes = ('TLShot',),
        emotions = {
            bg3.SPEAKER_GALE: ((0.0, 8, 1),),
            bg3.SPEAKER_GALE: ((4.2, 8, 1),),
            bg3.SPEAKER_PLAYER: ((6.5, 8, 2),),
        })
    t.create_tl_shot('62717afe-b1b1-4a21-9d8c-c2eec556e44c', '0.0', '6.4')

    # So long. It hasn't been a pleasure.
    d.create_standard_dialog_node(
        gale_leaves_the_party_node3_uuid,
        bg3.SPEAKER_GALE,
        [],
        bg3.text_content('h17d0d051g766fg4755g832fg62d6a8cb762f', 1),
        end_node=True,
        setflags=(
            bg3.flag_group('Object', (
                #bg3.flag(bg3.FLAG_Companion_Leaves_Party, True, slot_idx_gale),
                bg3.flag(Companion_Permanently_Leaves_Party.uuid, True, slot_idx_gale),
            )),
            bg3.flag_group('Quest', (
                bg3.flag('b0ace4c1-2592-4e90-9306-de9f8e6cc1aa', True, slot_idx_tav),
            )),
        ))
    t.create_new_voice_phase_from_another(
        'be456d41-4ad1-7e6b-360b-aacc272b2774',
        bg3.SPEAKER_GALE,
        '3.94',
        gale_leaves_the_party_node3_uuid,
        skip_tl_nodes = ('TLShot',),
        emotions = {
            bg3.SPEAKER_GALE: ((0.0, 128, 1),),
        })
    t.create_tl_shot('dbc60980-2dde-47c7-8e51-cdb8e42c0e40', '0.0', '3.94')


    ########################################################################################
    # Karlach_InParty2_Nested_TopicalGreetings.lsf
    ########################################################################################

    # d = bg3.dialog_object(files.get_file('Gustav', 'Mods/GustavDev/Story/DialogsBinary/Companions/Karlach_InParty_Nested_TopicalGreetings.lsf'))
    # t = bg3.timeline_object(files.get_file('Gustav', 'Public/GustavDev/Timeline/Generated/Karlach_InParty_Nested_TopicalGreetings.lsf'), d)

    ab = game_assets.get_modded_dialog_asset_bundle('Karlach_InParty_Nested_TopicalGreetings')
    d = bg3.dialog_object(ab.dialog)
    t = bg3.timeline_object(ab.timeline, d)

    d.remove_root_node('d265f2a7-2f4d-b0ef-4351-5a10aa9ff300')
    d.add_root_node('d265f2a7-2f4d-b0ef-4351-5a10aa9ff300', index = 0)

    slot_idx_tav = d.get_speaker_slot_index(bg3.SPEAKER_PLAYER)
    slot_idx_karlach = d.get_speaker_slot_index(bg3.SPEAKER_KARLACH)

    karlach_leaves_the_party_node1_uuid = 'e408a5bb-3e15-43eb-9555-ce26b1e1da00'
    karlach_leaves_the_party_node2_uuid = 'a9f85537-9373-4050-84ee-84796900591a'
    karlach_leaves_the_party_node3_uuid = 'ba5784f3-207e-4fe4-8220-8948989356de'

    d.delete_all_children_dialog_nodes('e2d94b96-1ee4-2fb2-a166-c7ea6b5cde90')
    d.add_child_dialog_node('e2d94b96-1ee4-2fb2-a166-c7ea6b5cde90', karlach_leaves_the_party_node1_uuid)

    d.delete_all_children_dialog_nodes('f57edf1a-97cc-9707-c489-93db59c827fc')
    d.add_child_dialog_node('f57edf1a-97cc-9707-c489-93db59c827fc', karlach_leaves_the_party_node1_uuid)

    d.delete_all_children_dialog_nodes('e19b20b7-4c05-37ed-970b-ae3d349c1293')
    d.add_child_dialog_node('e19b20b7-4c05-37ed-970b-ae3d349c1293', karlach_leaves_the_party_node1_uuid)

    d.delete_all_children_dialog_nodes('ac29f78b-5ec6-061a-96bc-e28522897479')
    d.add_child_dialog_node('ac29f78b-5ec6-061a-96bc-e28522897479', karlach_leaves_the_party_node1_uuid)

    # Look, I think we should go our separate ways. I've spent long enough in the Hells to know a bad situation when I see one.
    d.create_standard_dialog_node(
        karlach_leaves_the_party_node1_uuid,
        bg3.SPEAKER_KARLACH,
        [karlach_leaves_the_party_node2_uuid, karlach_leaves_the_party_node3_uuid],
        bg3.text_content('hbd6440e1g5ba9g48eag854eg45cf84eb1697', 2),
        setflags=(
            bg3.flag_group('Object', (
                #bg3.flag(bg3.FLAG_Companion_Leaves_Party, True, slot_idx_karlach),
                bg3.flag(Companion_Permanently_Leaves_Party.uuid, True, slot_idx_karlach),
            )),
            bg3.flag_group('Quest', (
                bg3.flag('b89b7e8a-3def-4777-aa93-87f1af1b1453', True, slot_idx_tav),
            )),
        ))
    t.create_new_voice_phase_from_another(
        'ac29f78b-5ec6-061a-96bc-e28522897479',
        bg3.SPEAKER_KARLACH,
        '8.0',
        karlach_leaves_the_party_node1_uuid,
        skip_tl_nodes = ('TLShot',),
        emotions = {
            bg3.SPEAKER_KARLACH: ((0.0, 4, None), (1.2, 64, None), (2.06, 1, None), (3.45, 4, 1)),
        })
    t.create_tl_shot('94b10096-c9d4-4f64-a52f-41a416235e6f', '0.0', '8.0')

    # I was wrong to think there could've been something between us. We're just too different.
    d.create_standard_dialog_node(
        karlach_leaves_the_party_node2_uuid,
        bg3.SPEAKER_KARLACH,
        [],
        bg3.text_content('h9452b111ged7bg46a8g8893g08943e114e92', 1),
        end_node=True,
        checkflags=(
            bg3.flag_group('Object', (
                bg3.flag('f24c3f3e-7287-4908-84bf-ba314921f5ee', True, slot_idx_karlach),
            )),
        ))
    t.create_new_voice_phase_from_another(
        'ac29f78b-5ec6-061a-96bc-e28522897479',
        bg3.SPEAKER_KARLACH,
        '5.22',
        karlach_leaves_the_party_node2_uuid,
        skip_tl_nodes = ('TLShot',),
        emotions = {
            bg3.SPEAKER_KARLACH: ((0.0, 8, None), (1.62, 4, 1), (3.48, 1024, None),),
        })
    t.create_tl_shot('94b10096-c9d4-4f64-a52f-41a416235e6f', '0.0', '5.22')

    # I can't believe I thought you were the one. Maybe I'm still that naive kid after all - the one who'd trust anyone who showed her a bit of kindness.
    d.create_standard_dialog_node(
        karlach_leaves_the_party_node3_uuid,
        bg3.SPEAKER_KARLACH,
        [],
        bg3.text_content('hcac4ab0ag2a1fg4a7cga7d7gdadda38445de', 2),
        end_node=True)
    t.create_new_voice_phase_from_another(
        'ac29f78b-5ec6-061a-96bc-e28522897479',
        bg3.SPEAKER_KARLACH,
        '9.8',
        karlach_leaves_the_party_node3_uuid,
        skip_tl_nodes = ('TLShot',),
        emotions = {
            bg3.SPEAKER_KARLACH: ((0.0, 1024, 1), (1.19, 64, 2), (2.37, 1024, 1), (4.27, 4, 2), (6.3, 4, None), (8.34, 8, None)),
        })
    t.create_tl_shot('94b10096-c9d4-4f64-a52f-41a416235e6f', '0.0', '9.8')


    ########################################################################################
    # Laezel_InParty2_Nested_TopicalGreetings.lsf
    ########################################################################################

    # d = bg3.dialog_object(files.get_file('Gustav', 'Mods/GustavDev/Story/DialogsBinary/Companions/Laezel_InParty2_Nested_TopicalGreetings.lsf'))
    # t = bg3.timeline_object(files.get_file('Gustav', 'Public/GustavDev/Timeline/Generated/Laezel_InParty2_Nested_TopicalGreetings.lsf'), d)

    ab = game_assets.get_modded_dialog_asset_bundle('Laezel_InParty2_Nested_TopicalGreetings')
    d = bg3.dialog_object(ab.dialog)
    t = bg3.timeline_object(ab.timeline, d)

    d.remove_root_node('f97c9285-2bcd-72b2-88ea-30c8a06c24b2')
    d.add_root_node('f97c9285-2bcd-72b2-88ea-30c8a06c24b2', index = 0)

    slot_idx_tav = d.get_speaker_slot_index(bg3.SPEAKER_PLAYER)
    slot_idx_laezel = d.get_speaker_slot_index(bg3.SPEAKER_LAEZEL)

    laezel_leaves_the_party_node1_uuid = '31cedda0-d899-4ecb-955f-cd8fc25fd553'
    laezel_leaves_the_party_node2_uuid = 'b2485fdd-3ff5-442b-8b9b-7a7174ceb111'

    d.add_child_dialog_node('234ab3c5-9525-e2fa-06d0-309072dd1a01', laezel_leaves_the_party_node1_uuid)
    d.remove_dialog_attribute('234ab3c5-9525-e2fa-06d0-309072dd1a01', 'endnode')

    # To think I trusted <i>you. </i>At best you are a <i>ghaik</i> pawn. At worst, you are a coward.
    d.create_standard_dialog_node(
        laezel_leaves_the_party_node1_uuid,
        bg3.SPEAKER_LAEZEL,
        [laezel_leaves_the_party_node2_uuid],
        bg3.text_content('h02901d3cg9c31g4d09gb0d7g9c0a0afa2672', 3),
        setflags=(
            bg3.flag_group('Object', (
                #bg3.flag(bg3.FLAG_Companion_Leaves_Party, True, slot_idx_laezel),
                bg3.flag(Companion_Permanently_Leaves_Party.uuid, True, slot_idx_laezel),
            )),
            bg3.flag_group('Quest', (
                bg3.flag('c8ff2cac-0c3d-4eec-bc43-1696ea8ea591', True, slot_idx_tav),
            )),
        ))
    t.create_new_voice_phase_from_another(
        '234ab3c5-9525-e2fa-06d0-309072dd1a01',
        bg3.SPEAKER_LAEZEL,
        '8.65',
        laezel_leaves_the_party_node1_uuid,
        skip_tl_nodes = ('TLShot',),
        emotions = {
            bg3.SPEAKER_LAEZEL: ((1.0, 32, None), (2.71, 128, 1), (5.54, 8, 23), (7.95, 128, 23)),
        })
    t.create_tl_shot('ae73c534-ae3e-4546-b1a2-3d92197a448c', '0.0', '8.08')

    # No more. I can't bear it.
    d.create_standard_dialog_node(
        laezel_leaves_the_party_node2_uuid,
        bg3.SPEAKER_LAEZEL,
        [],
        bg3.text_content('h74f99beegfcc7g43dega1adgd6a6c8d7b850', 2),
        end_node=True)
    t.create_new_voice_phase_from_another(
        '234ab3c5-9525-e2fa-06d0-309072dd1a01',
        bg3.SPEAKER_LAEZEL,
        '3.8',
        laezel_leaves_the_party_node2_uuid,
        skip_tl_nodes = ('TLShot',),
        emotions = {
            bg3.SPEAKER_LAEZEL: ((0.0, 8, 1), (2.2, 8, 2)),
        })
    t.create_tl_shot('89b46dba-c7df-4fea-980f-07329fd871bb', '0.0', '3.8')


    # The following ends the dialog.
    # d = bg3.dialog_object(files.get_file('Gustav', 'Mods/GustavDev/Story/DialogsBinary/Companions/Laezel_InParty2.lsf'))

    ab = game_assets.get_modded_dialog_asset_bundle('Laezel_InParty2')
    d = bg3.dialog_object(ab.dialog)

    slot_idx_laezel = d.get_speaker_slot_index(bg3.SPEAKER_LAEZEL)

    d.create_standard_dialog_node(
        '9ffbc9a7-a26c-42d7-b434-4783c8359eb6',
        bg3.SPEAKER_LAEZEL,
        [],
        None,
        checkflags=(
            bg3.flag_group('Object', (
                #bg3.flag(bg3.FLAG_Companion_Leaves_Party, True, slot_idx_laezel),
                bg3.flag(Companion_Permanently_Leaves_Party.uuid, True, slot_idx_laezel),
            )),
        ),
        end_node=True)

    d.add_child_dialog_node('5ec1a9fd-6d4c-5903-75de-d88d42b23422', '9ffbc9a7-a26c-42d7-b434-4783c8359eb6', 0)

    ########################################################################################
    # Wyll_InParty2_Nested_TopicalGreetings.lsf
    ########################################################################################

    # d = bg3.dialog_object(files.get_file('Gustav', 'Mods/GustavDev/Story/DialogsBinary/Companions/Wyll_InParty2_Nested_TopicalGreetings.lsf'))
    # t = bg3.timeline_object(files.get_file('Gustav', 'Public/GustavDev/Timeline/Generated/Wyll_InParty2_Nested_TopicalGreetings.lsf'), d)

    ab = game_assets.get_modded_dialog_asset_bundle('Wyll_InParty2_Nested_TopicalGreetings')
    d = bg3.dialog_object(ab.dialog)
    t = bg3.timeline_object(ab.timeline, d)

    d.set_dialog_flags('6e96807a-99a7-b5bd-8090-f83bd8f7bc11', setflags = ())

    slot_idx_tav = d.get_speaker_slot_index(bg3.SPEAKER_PLAYER)
    slot_idx_wyll = d.get_speaker_slot_index(bg3.SPEAKER_WYLL)

    wyll_turns_hostile_node1_uuid = '7ab1e6b3-cd80-4afa-bf0d-57c4f54055b1'
    wyll_turns_hostile_node2_uuid = '1ddce457-0853-4da1-a970-59fcf2f3112f'
    wyll_turns_hostile_node3_uuid = '532eb756-abab-440f-9b05-e5abb3641f44'
    wyll_turns_hostile_node4_uuid = '9b8ed18e-b0d4-4a15-aa78-9873e88bedeb'

    # So you went through with it. You returned Shadowheart to Viconia.
    d.create_standard_dialog_node(
        wyll_turns_hostile_node1_uuid,
        bg3.SPEAKER_WYLL,
        [wyll_turns_hostile_node2_uuid],
        bg3.text_content('h0de77744g1415g431eg9674g19df53015d8e', 2),
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_Shadowheart_ShadowheartBetrayed, True, slot_idx_wyll),
            )),
        ),
        constructor = bg3.dialog_object.GREETING,
        root = True)
    t.create_new_voice_phase_from_another(
        '6e96807a-99a7-b5bd-8090-f83bd8f7bc11',
        bg3.SPEAKER_WYLL,
        '4.9',
        wyll_turns_hostile_node1_uuid,
        skip_tl_nodes = ('TLShot',),
        emotions = {
            bg3.SPEAKER_WYLL: ((0.0, 4, None), (2.08, 16, None)),
        })
    t.create_tl_shot('29b25589-d19a-4fdd-ab27-0d84fb565742', '0.0', '4.9')

    # Her mind will be wiped, and Viconia will remake her in whatever image she desires.
    d.create_standard_dialog_node(
        wyll_turns_hostile_node2_uuid,
        bg3.SPEAKER_WYLL,
        [wyll_turns_hostile_node3_uuid],
        bg3.text_content('he7c6545fg9a55g4eceg87c8g4ba09145c7c0', 1))
    t.create_new_voice_phase_from_another(
        '6e96807a-99a7-b5bd-8090-f83bd8f7bc11',
        bg3.SPEAKER_WYLL,
        '6.3',
        wyll_turns_hostile_node2_uuid,
        skip_tl_nodes = ('TLShot',),
        emotions = {
            bg3.SPEAKER_WYLL: ((0.0, 16, None), (1.2, 32, 2)),
        })
    t.create_tl_shot('e3f15f4a-7eb7-450e-b2b2-5eda7d5b98fa', '0.0', '6.3')

    # A cruel fate, and for what? An unreliable ally in Viconia? Or just for the sheer cruelty of it?
    d.create_standard_dialog_node(
        wyll_turns_hostile_node3_uuid,
        bg3.SPEAKER_WYLL,
        [wyll_turns_hostile_node4_uuid],
        bg3.text_content('hd19cb35ag369eg426bga41fg3c3a0e809259', 1))
    t.create_new_voice_phase_from_another(
        '6e96807a-99a7-b5bd-8090-f83bd8f7bc11',
        bg3.SPEAKER_WYLL,
        '7.4531',
        wyll_turns_hostile_node3_uuid,
        skip_tl_nodes = ('TLShot',),
        phase_duration = '8.0',
        emotions = {
            bg3.SPEAKER_WYLL: ((0.0, 16, None), (4.2, 8, 2)),
        })
    t.create_tl_shot('29b25589-d19a-4fdd-ab27-0d84fb565742', '0.0', '8.0')

    # Traitor. The Blade now comes for <i>you</i>.
    d.create_standard_dialog_node(
        wyll_turns_hostile_node4_uuid,
        bg3.SPEAKER_WYLL,
        [],
        bg3.text_content('h03dba394g1b9cg4fa6ga0a0g8147ccea08b3', 1),
        end_node = True,
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(Companion_Turns_Hostile.uuid, True, slot_idx_wyll),
            )),
        ))
    t.create_new_voice_phase_from_another(
        '6e96807a-99a7-b5bd-8090-f83bd8f7bc11',
        bg3.SPEAKER_WYLL,
        '4.5',
        wyll_turns_hostile_node4_uuid,
        skip_tl_nodes = ('TLShot',),
        emotions = {
            bg3.SPEAKER_WYLL: ((0.0, 8, 1), (1.2, 8, 2)),
        })
    t.create_tl_shot('e3f15f4a-7eb7-450e-b2b2-5eda7d5b98fa', '0.0', '4.5')


    d.remove_root_node('6e96807a-99a7-b5bd-8090-f83bd8f7bc11')
    d.delete_dialog_node('6e96807a-99a7-b5bd-8090-f83bd8f7bc11')
    d.add_root_node(wyll_turns_hostile_node1_uuid, index=0)

    ########################################################################################
    # Wyll_InParty2.lsf
    ########################################################################################

    # The following ends the dialog.
    # try:
    #     # Patch 7
    #     d = bg3.dialog_object(files.get_file('Patch7_Hotfix3', 'Mods/GustavDev/Story/DialogsBinary/Companions/Wyll_InParty2.lsf'))
    # except:
    #     # Patch 8
    #     d = bg3.dialog_object(files.get_file('Gustav', 'Mods/GustavDev/Story/DialogsBinary/Companions/Wyll_InParty2.lsf'))

    ab = game_assets.get_modded_dialog_asset_bundle('Wyll_InParty')
    d = bg3.dialog_object(ab.dialog)

    slot_idx_wyll = d.get_speaker_slot_index(bg3.SPEAKER_WYLL)

    d.create_standard_dialog_node(
        'e95a035a-e9e4-4684-a620-bf51e2a2e674',
        bg3.SPEAKER_WYLL,
        [],
        None,
        checkflags=(
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_Shadowheart_ShadowheartBetrayed, True, slot_idx_wyll),
            )),
        ),
        setflags=(
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_Shadowheart_ShadowheartBetrayed, False, slot_idx_wyll),
            )),
        ),
        end_node=True)

    d.add_child_dialog_node('69a6b97e-9272-ff99-4c8a-523a96bfd3bf', 'e95a035a-e9e4-4684-a620-bf51e2a2e674', 0)

    ########################################################################################
    # Minsc_InParty.lsf
    ########################################################################################

    # d = bg3.dialog_object(files.get_file('Gustav', 'Mods/GustavDev/Story/DialogsBinary/Companions/Minsc_InParty.lsf'))
    # t = bg3.timeline_object(files.get_file('Gustav', 'Public/GustavDev/Timeline/Generated/Minsc_InParty.lsf'), d)

    ab = game_assets.get_modded_dialog_asset_bundle('Minsc_InParty')
    d = bg3.dialog_object(ab.dialog)
    t = bg3.timeline_object(ab.timeline, d)

    slot_idx_tav = d.get_speaker_slot_index(bg3.SPEAKER_PLAYER)
    slot_idx_minsc = d.get_speaker_slot_index(bg3.SPEAKER_MINSC)

    minsc_node1_uuid = 'b3b771cd-e09a-461d-901f-fff0ac8535f1'
    minsc_node2_uuid = '7e4be8e4-288c-4cf5-8278-b6e3c28d9e69'
    minsc_node3_uuid = '538a2f5b-c3bd-4fe5-9229-1baa4f2f3dd3'
    minsc_node4_uuid = 'ff1a5606-0aae-49cb-9f72-05f9ec75d072'
    minsc_node5_uuid = '44cd6cce-eb7f-4739-b73d-3e397d037367'

    # Minsc has known Shadowheart for some time, and so feels permitted to say - getting to know her is a rocky road, but one well worth the walking.
    d.create_standard_dialog_node(
        minsc_node1_uuid,
        bg3.SPEAKER_MINSC,
        [minsc_node2_uuid],
        bg3.text_content('h99bd86e2g9edag4cfag960dgd4e50c6bcaa1', 3),
        constructor = bg3.dialog_object.GREETING,
        root = True,
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_Shadowheart_ShadowheartBetrayed, True, slot_idx_minsc),
            )),
        ),
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(Companion_Turns_Hostile.uuid, True, slot_idx_minsc),
            )),
        ))
    t.create_new_voice_phase_from_another(
        '6a0286b8-d9d9-6a01-06cd-6d15ea23055d',
        bg3.SPEAKER_MINSC,
        '11.5',
        minsc_node1_uuid,
        skip_tl_nodes = ('TLShot',),
        phase_duration = '12',
        emotions = {
            bg3.SPEAKER_MINSC: ((0.0, 16, None), (3.8, 32, None), (8.7, 16, None), (10.3, 64, None)),
        })
    t.create_tl_shot('3f0e9c96-3c94-4a4b-b884-9d15d0549820', '0.0', '12')

    # Jaheira hoped there was still some flimsy light of good within you, small as Boo but just as bright.
    d.create_standard_dialog_node(
        minsc_node2_uuid,
        bg3.SPEAKER_MINSC,
        [minsc_node3_uuid],
        bg3.text_content('hd4e507b0g952fg4ebagaaeagd0157c6dbab4', 3))
    t.create_new_voice_phase_from_another(
        '6a0286b8-d9d9-6a01-06cd-6d15ea23055d',
        bg3.SPEAKER_MINSC,
        '7.9',
        minsc_node2_uuid,
        skip_tl_nodes = ('TLShot',),
        phase_duration = '8.2',
        emotions = {
            bg3.SPEAKER_MINSC: ((0.0, 64, None), (5.2, 64, 1)),
        })
    t.create_tl_shot('60281a74-2ca2-40d7-bff9-6dc642ad6852', '0.0', '8.2')

    # Boo and I - we once hoped that that was true. But no longer.
    d.create_standard_dialog_node(
        minsc_node3_uuid,
        bg3.SPEAKER_MINSC,
        [minsc_node4_uuid],
        bg3.text_content('h0b1daa06g62afg4ce7g94b8g1a41ad583c00', 2))
    t.create_new_voice_phase_from_another(
        '6a0286b8-d9d9-6a01-06cd-6d15ea23055d',
        bg3.SPEAKER_MINSC,
        '7.5',
        minsc_node3_uuid,
        skip_tl_nodes = ('TLShot',),
        phase_duration = '8.0',
        emotions = {
            bg3.SPEAKER_MINSC: ((0.0, 64, 2), (5.2, 8, None)),
        })
    t.create_tl_shot('9ab4f6a3-c3ce-47da-9628-3d2a36ad4b5f', '0.0', '8.0')

    # And Minsc shall be your undoing!
    d.create_standard_dialog_node(
        minsc_node4_uuid,
        bg3.SPEAKER_MINSC,
        [minsc_node5_uuid],
        bg3.text_content('ha6a0226fg3dcdg4e93gb345g9a883ba8e363', 3))
    t.create_new_voice_phase_from_another(
        '6a0286b8-d9d9-6a01-06cd-6d15ea23055d',
        bg3.SPEAKER_MINSC,
        '3.85',
        minsc_node4_uuid,
        skip_tl_nodes = ('TLShot',),
        phase_duration = '4.2',
        emotions = {
            bg3.SPEAKER_MINSC: ((0.0, 8, 2),),
        })
    t.create_tl_shot('329e986a-a7f0-4786-a1ce-216270903aae', '0.0', '4.2')

    # AAAAAAAARRRRGGGGGH!
    d.create_standard_dialog_node(
        minsc_node5_uuid,
        bg3.SPEAKER_MINSC,
        [],
        bg3.text_content('h801c12b7gb1fag4e43ga3a0gc940f0e253f4', 1),
        end_node = True)
    t.create_new_voice_phase_from_another(
        '6a0286b8-d9d9-6a01-06cd-6d15ea23055d',
        bg3.SPEAKER_MINSC,
        '3.38',
        minsc_node5_uuid,
        skip_tl_nodes = ('TLShot',),
        phase_duration = '3.5',
        emotions = {
            bg3.SPEAKER_MINSC: ((0.0, 8, 2),),
        })
    t.create_tl_shot('846aa2bc-04a9-480e-9c22-d6657e902c07', '0.0', '3.5')


    d.add_root_node(minsc_node1_uuid, index = 0)

    ########################################################################################
    # Jaheira_InParty_Nested_TopicalGreetings.lsf
    ########################################################################################

    # d = bg3.dialog_object(files.get_file('Gustav', 'Mods/GustavDev/Story/DialogsBinary/Companions/Jaheira_InParty_Nested_TopicalGreetings.lsf'))
    # t = bg3.timeline_object(files.get_file('Gustav', 'Public/GustavDev/Timeline/Generated/Wyll_InParty2_Nested_TopicalGreetings.lsf'), d)

    ab = game_assets.get_modded_dialog_asset_bundle('Jaheira_InParty_Nested_TopicalGreetings')
    d = bg3.dialog_object(ab.dialog)

    d.set_dialog_flags('280da26d-a9e0-3adb-ec5a-22929797b955', setflags = ())

    ########################################################################################
    # Jaheira_InParty.lsf
    ########################################################################################

    # d = bg3.dialog_object(files.get_file('Gustav', 'Mods/GustavDev/Story/DialogsBinary/Companions/Jaheira_InParty.lsf'))
    # t = bg3.timeline_object(files.get_file('Gustav', 'Public/GustavDev/Timeline/Generated/Jaheira_InParty.lsf'), d)

    ab = game_assets.get_modded_dialog_asset_bundle('Jaheira_InParty')
    d = bg3.dialog_object(ab.dialog)
    t = bg3.timeline_object(ab.timeline, d)

    slot_idx_tav = d.get_speaker_slot_index(bg3.SPEAKER_PLAYER)
    slot_idx_jaheira = d.get_speaker_slot_index(bg3.SPEAKER_JAHEIRA)

    jaheira_node1_uuid = 'ad88f6f0-b07a-4e2b-b1e9-d6be817a1d28'
    jaheira_node2_uuid = 'cb223bff-37a7-471d-a126-f663e777632d'
    jaheira_node3_uuid = '7068d592-9002-4d9e-a4e4-846944da8b73'

    # I was ready to advise you to make common cause with Viconia, if it would have served the city.
    d.create_standard_dialog_node(
        jaheira_node1_uuid,
        bg3.SPEAKER_JAHEIRA,
        [jaheira_node2_uuid],
        bg3.text_content('h215f9658g3173g4df3gaa13g149bb1d4f4a8', 3),
        constructor = bg3.dialog_object.GREETING,
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_Shadowheart_ShadowheartBetrayed, True, slot_idx_jaheira),
            )),
        ),
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_Shadowheart_ShadowheartBetrayed, False, slot_idx_jaheira),
            )),
        ))
    t.create_new_voice_phase_from_another(
        'c8082352-1c09-2f41-8914-ba078cabae86',
        bg3.SPEAKER_JAHEIRA,
        '5.75',
        jaheira_node1_uuid,
        skip_tl_nodes = ('TLShot',),
        phase_duration = '6.0',
        emotions = {
            bg3.SPEAKER_JAHEIRA: ((0.0, 3, 4), (3.09, 3, 16), (4.64, 32, None)),
        })
    t.create_tl_shot('187a2767-1b01-43ae-a424-16795c142b6b', '0.0', '6.0')

    # But to trade an ally like chattel - you and the <i>Mother Superior</i> make fine bedfellows already.
    d.create_standard_dialog_node(
        jaheira_node2_uuid,
        bg3.SPEAKER_JAHEIRA,
        [jaheira_node3_uuid],
        bg3.text_content('hbcfa2ba3g5a44g4d74g8cceg0e0c6185abe0', 3))
    t.create_new_voice_phase_from_another(
        'c8082352-1c09-2f41-8914-ba078cabae86',
        bg3.SPEAKER_JAHEIRA,
        '7.72',
        jaheira_node2_uuid,
        skip_tl_nodes = ('TLShot',),
        phase_duration = '8.5',
        emotions = {
            bg3.SPEAKER_JAHEIRA: ((0.0, 128, 1), (1.46, 8, 1), (5.25, 128, 2)),
        })
    t.create_tl_shot('6a4e1e0d-8ea0-470d-bada-375174e071b4', '0.0', '8.5')

    # Bah! Vile things that befit a vile traitor.
    d.create_standard_dialog_node(
        jaheira_node3_uuid,
        bg3.SPEAKER_JAHEIRA,
        [],
        bg3.text_content('h7c220518ga13cg409egacf8g36d55e3996b8', 1),
        end_node = True,
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(Companion_Turns_Hostile.uuid, True, slot_idx_jaheira),
            )),
        ))
    t.create_new_voice_phase_from_another(
        'c8082352-1c09-2f41-8914-ba078cabae86',
        bg3.SPEAKER_JAHEIRA,
        '3.8',
        jaheira_node3_uuid,
        skip_tl_nodes = ('TLShot',),
        phase_duration = '4.2',
        emotions = {
            bg3.SPEAKER_JAHEIRA: ((0.0, 8, None), (1.8, 8, 1), (3.3, 8, 2)),
        })
    t.create_tl_shot('187a2767-1b01-43ae-a424-16795c142b6b', '0.0', '4.2')

    d.add_root_node(jaheira_node1_uuid, index = 0)


    ########################################################################################
    # Halsin_InParty.lsf
    ########################################################################################

    # d = bg3.dialog_object(files.get_file('Gustav', 'Mods/GustavDev/Story/DialogsBinary/Companions/Halsin_InParty.lsf'))
    # t = bg3.timeline_object(files.get_file('Gustav', 'Public/GustavDev/Timeline/Generated/Halsin_InParty.lsf'), d)

    ab = game_assets.get_modded_dialog_asset_bundle('Halsin_InParty')
    d = bg3.dialog_object(ab.dialog)
    t = bg3.timeline_object(ab.timeline, d)

    slot_idx_tav = d.get_speaker_slot_index(bg3.SPEAKER_PLAYER)
    slot_idx_halsin = d.get_speaker_slot_index(bg3.SPEAKER_HALSIN)

    halsin_node1_uuid = 'db804bde-96c3-405a-9835-3506a754a647'
    halsin_node2_uuid = '00398133-db13-4d24-9223-0fa4cb9f89b9'

    # A cruel parting of ways with Shadowheart. I can only hope the allies we have won will be worth our betrayal.
    d.create_standard_dialog_node(
        halsin_node1_uuid,
        bg3.SPEAKER_HALSIN,
        [halsin_node2_uuid],
        bg3.text_content('h413c5838g87f0g471fg9f42g73318f346691', 3),
        constructor = bg3.dialog_object.GREETING,
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_Shadowheart_ShadowheartBetrayed, True, slot_idx_halsin),
            )),
        ),
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_Shadowheart_ShadowheartBetrayed, False, slot_idx_halsin),
                bg3.flag(Companion_Permanently_Leaves_Party.uuid, True, slot_idx_halsin),
            )),
        ))
    t.create_new_voice_phase_from_another(
        'd1d77d4c-c2bf-49a1-875e-5f4e891641eb',
        bg3.SPEAKER_HALSIN,
        '7.64',
        halsin_node1_uuid,
        skip_tl_nodes = ('TLShot',),
        phase_duration = '8.0',
        emotions = {
            bg3.SPEAKER_HALSIN: ((0.0, 4, None), (0.8, 32, None), (2.4, 4, None), (3.17, 32, None), (4.1, 4, None),)
        })
    t.create_tl_shot('381b21bc-e3f6-4268-991e-d7455b3e3e75', '0.0', '8.0')

    # This is where we must part ways. I hoped it wouldn't be necessary, but no... I cannot turn a blind eye to your actions any longer.
    d.create_standard_dialog_node(
        halsin_node2_uuid,
        bg3.SPEAKER_HALSIN,
        [],
        bg3.text_content('h4fa038f1g1c61g498dga282g32e1d2551fe0', 2),
        end_node = True)
    t.create_new_voice_phase_from_another(
        'd1d77d4c-c2bf-49a1-875e-5f4e891641eb',
        bg3.SPEAKER_HALSIN,
        '11.15',
        halsin_node2_uuid,
        skip_tl_nodes = ('TLShot',),
        emotions = {
            bg3.SPEAKER_HALSIN: ((0.0, 16, None), (1.2, 32, None), (3.0, 16, None), (5.5, 2048, None)),
        })
    t.create_tl_shot('c0021c6a-f0da-42fd-b4a4-a14105dedf33', '0.0', '11.15')

    d.add_root_node(halsin_node1_uuid, index = 0)


    ########################################################################################
    # Minthara_InParty_Nested_TopicalGreetings.lsf
    ########################################################################################

    # d = bg3.dialog_object(files.get_file('Gustav', 'Mods/GustavDev/Story/DialogsBinary/Companions/Minthara_InParty_Nested_TopicalGreetings.lsf'))

    ab = game_assets.get_modded_dialog_asset_bundle('Minthara_InParty_Nested_TopicalGreetings')
    d = bg3.dialog_object(ab.dialog)

    d.remove_root_node('5e0b46c2-30f1-2d58-a6d4-7981af23478a')
    d.add_root_node('5e0b46c2-30f1-2d58-a6d4-7981af23478a', index = 0)


bg3.add_build_procedure('create_betrayal_reactions', create_betrayal_reactions)

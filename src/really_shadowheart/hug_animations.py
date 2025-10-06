from __future__ import annotations

import bg3moddinglib as bg3
import os
import os.path

from .context import (
    game_assets,
    root_path
)
from .flags import *

entry_point_node_uuid = '5df536d1-33bb-448c-a4a4-dea0329b4f6e'

hug_strong_node_uuid = '6b7703c0-ad03-4c5e-b607-15d18423f8b0'
hug_sad_strong_node_uuid = 'c9347a0e-4cb5-4642-8e4e-7d38e5472fc6'

hug_short_node_uuid = 'b5598fc0-0125-46a9-a1c4-4a8d66910b12'
hug_sad_short_node_uuid = '0143d539-ea95-4bc1-a5f2-3abcb5450298'

hug_dwarf_node_uuid = 'f9d5bd33-afe9-44ca-ba9c-5c66616a70cd'
hug_sad_dwarf_node_uuid = '9af047cd-7fcc-48e5-92c9-d204a9816c15'

hug_dragonborn_node_uuid = '451af6d4-b8c6-428f-8b86-a0c8815b844a'
hug_sad_dragonborn_node_uuid = '605a964e-690a-482f-99f5-c2bd60c8817b'

hug_normal_node_uuid = '93cded93-c188-4a05-925e-d2263c1ae858'
hug_sad_normal_node_uuid = '755a5814-0e6b-abbb-770e-1de32c6d0208'

sad_hug_end_node_uuid = '12e09065-ef6a-1194-227b-1177fbb21548'

hug_first_reaction_node_uuid = 'cff26d0c-4c6c-1960-afd6-ef648d0c027a'
hug_reaction_partnered_node_uuid = '4d5ca01d-0dd7-64c8-455a-70e3b7c2ffa4'
hug_reaction_dating_node_uuid = '788d6997-8ae8-8e1f-0664-f3131e8bf33a'
hug_reaction_node_uuid = '05ee0346-137b-d7b7-54b6-b14f0e8a5264'

###########################################################################
# Hugs
###########################################################################

def add_hugs_to_the_story() -> None:
    ###########################################################################
    # Dialog: ShadowHeart_InParty2_Nested_ShadowCurseChapter.lsf
    # Hug her after she spares Nightsong (at the Thorm mausoleum entrance)
    ###########################################################################

    # d = bg3.dialog_object(files.get_file('Gustav', 'Mods/GustavDev/Story/DialogsBinary/Companions/ShadowHeart_InParty2_Nested_ShadowCurseChapter.lsf'))
    ab = game_assets.get_modded_dialog_asset_bundle('ShadowHeart_InParty2_Nested_ShadowCurseChapter')
    d = bg3.dialog_object(ab.dialog)

    slot_idx_shadowheart = d.get_speaker_slot_index(bg3.SPEAKER_SHADOWHEART)
    slot_idx_tav = d.get_speaker_slot_index(bg3.SPEAKER_PLAYER)

    hug_her_node_uuid = 'a6e353d2-caa1-4cc0-cb7d-3a0abc6f2bd3'
    nested_dialog_node_uuid = '8c3cf523-3a13-d275-775c-db0b84d3f262'

    d.set_dialog_flags(hug_her_node_uuid, checkflags=(
        bg3.flag_group('Object', (
            bg3.flag(bg3.FLAG_Approval_AtLeast_40_For_Sp2, True, slot_idx_shadowheart),
        )),
    ))
    d.set_dialog_flags(nested_dialog_node_uuid, checkflags=())

    ###########################################################################
    # Hug her when talking after she spares Nightsong (companion dialog)
    # If Shadowheart was already hugged, this one won't appear in the dialog
    ###########################################################################

    hug_her_node_uuid = '77d47cd7-91e5-f569-f50e-1e3bf23e10fb'
    nested_dialog_node_uuid = 'd21d3171-1377-cd8e-288f-d2bd4a0db59c'

    d.set_dialog_flags(hug_her_node_uuid, checkflags=(
        bg3.flag_group('Object', (
            bg3.flag(bg3.FLAG_Approval_AtLeast_40_For_Sp2, True, slot_idx_shadowheart),
            bg3.flag(Shadowheart_State_Smiles_When_Hugged.uuid, False, slot_idx_shadowheart),
        )),
    ))
    d.set_dialog_flags(nested_dialog_node_uuid, checkflags=())
    d.delete_child_dialog_node('022fc6c6-7b3a-e80c-a2fa-81743e94f9a1', hug_her_node_uuid)
    d.add_child_dialog_node('022fc6c6-7b3a-e80c-a2fa-81743e94f9a1', hug_her_node_uuid, index=0)

    ###########################################################################
    # Dialog: CAMP_Shadowheart_DaughterTears_SD.lsf
    # if hugs weren't enabled in act 2, this enables them in act 3.
    # If parents saved, hugs are always enabled.
    # If parents moonmoted, Tav snould embrace her to enable hugs.
    ###########################################################################

    # This was moved to daughters_tears.py

    ###########################################################################
    # Dialog:   ShadowHeart_InParty2_Nested_ShadowheartHug.lsf
    # Timeline: ShadowHeart_InParty2_Nested_ShadowheartHug.lsf
    # Both files are copied from a local directory
    ###########################################################################

    #dialog_src_lsx = os.path.join(root_path, 'lsx', 'Dialog_ShadowHeart_InParty2_Nested_ShadowheartHug.lsf.lsx')
    #files.add_external_file(dialog_src_lsx, 'Mods/GustavDev/Story/DialogsBinary/Companions/ShadowHeart_InParty2_Nested_ShadowheartHug.lsf')

    #timeline_src_lsx = os.path.join(root_path, 'lsx', 'Timeline_ShadowHeart_InParty2_Nested_ShadowheartHug.lsf.lsx')
    #files.add_external_file(timeline_src_lsx, 'Public/GustavDev/Timeline/Generated/ShadowHeart_InParty2_Nested_ShadowheartHug.lsf')


    ###########################################################################
    # Dialog: ShadowHeart_InParty2.lsf
    # if hugs are enabled, there is a "Hug her" option in the dialog.
    ###########################################################################

    # d = bg3.dialog_object(files.get_file('Gustav', 'Mods/GustavDev/Story/DialogsBinary/Companions/ShadowHeart_InParty2.lsf'))
    ab = game_assets.get_modded_dialog_asset_bundle('ShadowHeart_InParty')
    d = bg3.dialog_object(ab.dialog)

    slot_idx_shadowheart = d.get_speaker_slot_index(bg3.SPEAKER_SHADOWHEART)
    slot_idx_tav = d.get_speaker_slot_index(bg3.SPEAKER_PLAYER)

    hug_her_node_uuid = 'f5a1f59f-7c05-55d4-3951-849dbdb62b2f'
    nested_dialog_node_uuid = '06d12f25-311e-be5b-3c1e-112918fa014d'

    d.set_dialog_flags(hug_her_node_uuid, checkflags=(
        bg3.flag_group('Object', (
            bg3.flag(bg3.FLAG_ORI_State_WasPartneredWithShadowheart, False, slot_idx_tav),
            bg3.flag(bg3.FLAG_Approval_AtLeast_60_For_Sp2, True, slot_idx_shadowheart),
            bg3.flag(Shadowheart_State_Hugs_Enabled.uuid, True, slot_idx_shadowheart),
        )),
    ))
    d.set_dialog_flags(nested_dialog_node_uuid, checkflags=())
    d.set_tagged_text(hug_her_node_uuid, bg3.text_content('h4e908b98g9055g4a21gb8b3g118fa3b5250c', 2, 'a2f9acbd-550c-476f-9632-66fe4e8ab150'))

    # Move 'Hug her' to the top
    d.delete_child_dialog_node(bg3.SHADOWHEART_QUESTION_BANK_ROOT_NODE_UUID, hug_her_node_uuid)
    d.add_child_dialog_node(bg3.SHADOWHEART_QUESTION_BANK_ROOT_NODE_UUID, hug_her_node_uuid, 0)


def create_hugs_dialogs() -> None:

    dialog_src_lsx = os.path.join(root_path, 'resources', 'main', 'templates', 'Dialog_ShadowHeart_InParty2_Nested_ShadowheartHug_Empty.lsf.lsx')
    dialog_file = bg3.game_file(game_assets.tool, "", source_file_path = dialog_src_lsx)
    ab = game_assets.get_modded_dialog_asset_bundle('ShadowHeart_InParty2_Nested_ShadowheartHug')
    dialog_node = dialog_file.xml.find('./region[@id="dialog"]/node[@id="dialog"]')
    # Set the correct timeline UUID
    if dialog_node:
        bg3.set_bg3_attribute(dialog_node, 'TimelineId', ab.modded_timeline_uuid)
    ab.dialog.replace_xml(dialog_file.xml)
    d = bg3.dialog_object(ab.dialog)

    # files.add_external_file(dialog_src_lsx, 'Mods/GustavDev/Story/DialogsBinary/Companions/ShadowHeart_InParty2_Nested_ShadowheartHug.lsf')
    # d = bg3.dialog_object(files.get_file(None, 'Mods/GustavDev/Story/DialogsBinary/Companions/ShadowHeart_InParty2_Nested_ShadowheartHug.lsf'))

    slot_idx_shadowheart = d.get_speaker_slot_index(bg3.SPEAKER_SHADOWHEART)
    slot_idx_tav = d.get_speaker_slot_index(bg3.SPEAKER_PLAYER)

    d.create_standard_dialog_node(
        entry_point_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [
            hug_dwarf_node_uuid,
            hug_sad_dwarf_node_uuid,
            hug_short_node_uuid,
            hug_sad_short_node_uuid,
            hug_dragonborn_node_uuid,
            hug_sad_dragonborn_node_uuid,
            hug_strong_node_uuid,
            hug_sad_strong_node_uuid,
            hug_normal_node_uuid,
            hug_sad_normal_node_uuid,
        ],
        None,
        constructor = bg3.dialog_object.GREETING,
        root = True
    )

    d.create_cinematic_dialog_node(
        hug_strong_node_uuid,
        [hug_first_reaction_node_uuid, hug_reaction_partnered_node_uuid, hug_reaction_dating_node_uuid, hug_reaction_node_uuid],
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(Shadowheart_State_Smiles_When_Hugged.uuid, True, slot_idx_shadowheart),
            )),
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_BODYTYPE_STRONG, True, slot_idx_tav),
            )),        
        )
    )
    d.create_cinematic_dialog_node(
        hug_sad_strong_node_uuid,
        [sad_hug_end_node_uuid],
        checkflags = (
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_BODYTYPE_STRONG, True, slot_idx_tav),
            )),        
        )
    )

    d.create_cinematic_dialog_node(
        hug_short_node_uuid,
        [hug_first_reaction_node_uuid, hug_reaction_partnered_node_uuid, hug_reaction_dating_node_uuid, hug_reaction_node_uuid],
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(Shadowheart_State_Smiles_When_Hugged.uuid, True, slot_idx_shadowheart),
            )),
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_SHORT, True, slot_idx_tav),
            )),        
        )
    )
    d.create_cinematic_dialog_node(
        hug_sad_short_node_uuid,
        [sad_hug_end_node_uuid],
        checkflags = (
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_SHORT, True, slot_idx_tav),
            )),        
        )
    )

    d.create_cinematic_dialog_node(
        hug_dwarf_node_uuid,
        [hug_first_reaction_node_uuid, hug_reaction_partnered_node_uuid, hug_reaction_dating_node_uuid, hug_reaction_node_uuid],
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(Shadowheart_State_Smiles_When_Hugged.uuid, True, slot_idx_shadowheart),
            )),
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_DWARF, True, slot_idx_tav),
            )),        
        )
    )
    d.create_cinematic_dialog_node(
        hug_sad_dwarf_node_uuid,
        [sad_hug_end_node_uuid],
        checkflags = (
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_DWARF, True, slot_idx_tav),
            )),        
        )
    )

    d.create_cinematic_dialog_node(
        hug_dragonborn_node_uuid,
        [hug_first_reaction_node_uuid, hug_reaction_partnered_node_uuid, hug_reaction_dating_node_uuid, hug_reaction_node_uuid],
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(Shadowheart_State_Smiles_When_Hugged.uuid, True, slot_idx_shadowheart),
            )),
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_DRAGONBORN, True, slot_idx_tav),
            )),        
        )
    )
    d.create_cinematic_dialog_node(
        hug_sad_dragonborn_node_uuid,
        [sad_hug_end_node_uuid],
        checkflags = (
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_DRAGONBORN, True, slot_idx_tav),
            )),        
        )
    )

    d.create_cinematic_dialog_node(
        hug_normal_node_uuid,
        [hug_first_reaction_node_uuid, hug_reaction_partnered_node_uuid, hug_reaction_dating_node_uuid, hug_reaction_node_uuid],
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(Shadowheart_State_Smiles_When_Hugged.uuid, True, slot_idx_shadowheart),
            )),
        )
    )
    d.create_cinematic_dialog_node(
        hug_sad_normal_node_uuid,
        [sad_hug_end_node_uuid]
    )

    d.create_standard_dialog_node(
        hug_first_reaction_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [],
        bg3.text_content('h7cc0a098g7cd0g419fga0e2g14719699b80e', 2),
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(Shadowheart_State_Hug_Reaction.uuid, False, slot_idx_shadowheart),
            )),
        ),
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(Shadowheart_State_Hug_Reaction.uuid, True, slot_idx_shadowheart),
            )),
        ),
        end_node = True
    )

    d.create_standard_dialog_node(
        hug_reaction_partnered_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [],
        [
            bg3.text_content('h2e10138dgea84g4551gafdeg5679d5136196', 2, '25463d4f-fa9a-48ac-ae6d-a2834b58f5a9'),
            bg3.text_content('h714be156g6df0g4027gae01g55e7dc00a214', 1, '80423156-a5bc-4c1c-ac14-87659cd4a850', custom_sequence_id = '80423156-a5bc-4c1c-ac14-87659cd4a850'),
            bg3.text_content('h13d42458g955dg46dag9acbg08d2f409091f', 1, 'b14431aa-303e-4b2e-837a-4c0f694db27d', custom_sequence_id = 'b14431aa-303e-4b2e-837a-4c0f694db27d'),
            bg3.text_content('ha028d13ag1b67g4d6agbb7fgd19a577ff478', 1, '001af130-b986-4de7-a067-de408a500f9c', custom_sequence_id = '001af130-b986-4de7-a067-de408a500f9c'),
        ],
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_State_PartneredWithShadowheart, True, slot_idx_tav),
            )),
        ),
        end_node = True
    )

    d.create_alias_dialog_node(
        hug_reaction_dating_node_uuid,
        hug_reaction_partnered_node_uuid,
        [],
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_State_DatingShadowheart, True, slot_idx_tav),
            )),
        ),
        end_node = True    
    )

    d.create_standard_dialog_node(
        hug_reaction_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [],
        [
            bg3.text_content('h5528f361g7d01g4b30gb478g8daa2d6a8d93', 2, '8acdaadb-f25a-4637-ad82-3f18c79ddf26'),
            bg3.text_content('h81ce5fcaga1d3g4c0eg931cg7fbdb7ebf9ce', 1, '5f9fcc12-d75e-4203-8700-ead81fad67b5', custom_sequence_id = '5f9fcc12-d75e-4203-8700-ead81fad67b5'),
            bg3.text_content('h7f15f36bgc0fbg4e63gaa4dgaea3e9d2104a', 1, '40e3cd39-3a77-496f-8b55-4fa9f12c7a5c', custom_sequence_id = '40e3cd39-3a77-496f-8b55-4fa9f12c7a5c'),
        ],
        end_node = True
    )

    d.create_standard_dialog_node(
        sad_hug_end_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [],
        None,
        transition_mode = True,
        end_node = True,
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(Shadowheart_State_Smiles_When_Hugged.uuid, True, slot_idx_shadowheart),
                bg3.flag(Shadowheart_State_Hugs_Enabled.uuid, True, slot_idx_shadowheart),
            )),
        )
    )

    d.add_root_node(entry_point_node_uuid)


def create_hugs_timeline() -> None:
    ###########################################################################
    # Timeline: ShadowHeart_InParty2_Nested_ShadowheartHug.lsf
    # This cell contains timelines for dialogs defined in the cell above 
    ###########################################################################

    # timeline_src_lsx = os.path.join(root_path, 'resources', 'templates', 'Timeline_ShadowHeart_InParty2_Nested_ShadowheartHug_Empty.lsf.lsx')
    # files.add_external_file(timeline_src_lsx, 'Public/GustavDev/Timeline/Generated/ShadowHeart_InParty2_Nested_ShadowheartHug.lsf')
    # d = bg3.dialog_object(files.get_file(None, 'Mods/GustavDev/Story/DialogsBinary/Companions/ShadowHeart_InParty2_Nested_ShadowheartHug.lsf'))
    # t = bg3.timeline_object(files.get_file(None, 'Public/GustavDev/Timeline/Generated/ShadowHeart_InParty2_Nested_ShadowheartHug.lsf'), d)

    timeline_src_lsx = os.path.join(root_path, 'resources', 'main', 'templates', 'Timeline_ShadowHeart_InParty2_Nested_ShadowheartHug_Empty.lsf.lsx')
    timeline_file = bg3.game_file(game_assets.tool, "", source_file_path = timeline_src_lsx)
    ab = game_assets.get_modded_dialog_asset_bundle('ShadowHeart_InParty2_Nested_ShadowheartHug')
    ab.timeline.replace_xml(timeline_file.xml)
    d = bg3.dialog_object(ab.dialog)
    t = bg3.timeline_object(ab.timeline, d)

    """
    Tav -> Shadowheart:
    18c5bd4f-c066-4c52-8cdb-d8bbe1d8034e
    89eeac49-0759-420d-8f99-3b76a8b2b7e8
    cc421647-a27f-4860-b524-9370db1b711d
    99480a46-e5ff-4101-ab73-d0ce43403c57

    Shadowheart -> Tav:
    befcdee8-6352-4be6-b2ea-23c2ac0dfe60
    fb91b3e2-b1b9-47d5-8478-659cececad9b
    450b4f98-d7bf-4d73-9844-6d2832d4a026
    a43f207a-ed78-4acf-9815-9103e41577d0

    Tav -> Tav
    cb95fcb5-efd7-48f4-9352-5eaeb3e44274
    64edf86f-1d72-47fd-b908-a444cadb2fc3
    """

    ###########################################################################
    # Normal body type
    ###########################################################################
    phase_duration = '24.55' # 20.67 + 3.88
    t.create_new_phase(hug_normal_node_uuid, phase_duration)

    t.create_tl_actor_node(bg3.timeline_object.ATTITUDE, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.ATTITUDE, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        t.create_attitude_key(0.0, bg3.ATTITUDE_DIAG_Pose_Stand_L_Forward_01, bg3.ATTITUDE_DIAG_T_Pose),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.ATTITUDE, bg3.PEANUT_SLOT_0, '0.0', phase_duration, (
        t.create_attitude_key(0.5, bg3.ATTITUDE_DIAG_Pose_Stand_L_Forward_01, bg3.ATTITUDE_DIAG_T_Pose),
    ), is_snapped_to_end = True, is_mimicry = True)
    t.create_tl_actor_node(bg3.timeline_object.ATTITUDE, bg3.PEANUT_SLOT_1, '0.0', phase_duration, (
        t.create_attitude_key(0.5, bg3.ATTITUDE_DIAG_Pose_Stand_L_Forward_01, bg3.ATTITUDE_DIAG_T_Pose),
    ), is_snapped_to_end = True, is_mimicry = True)
    t.create_tl_actor_node(bg3.timeline_object.ATTITUDE, bg3.PEANUT_SLOT_2, '0.0', phase_duration, (
        t.create_attitude_key(0.5, bg3.ATTITUDE_DIAG_Pose_Stand_L_Forward_01, bg3.ATTITUDE_DIAG_T_Pose),
    ), is_snapped_to_end = True, is_mimicry = True)


    t.create_tl_actor_node(bg3.timeline_object.EMOTION, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_emotion_key(0.0, 2),
        t.create_emotion_key(1.34 + 3.88, 2, variation = 2),
        t.create_emotion_key(15.79 + 3.88, 2, variation = 1),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.EMOTION, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        t.create_emotion_key(5.99 + 3.88, 2, variation = 1),
        t.create_emotion_key(8.83 + 3.88, 2, variation = 2),
        t.create_emotion_key(12.08 + 3.88, 2, variation = 1),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.EMOTION, bg3.PEANUT_SLOT_0, '0.0', phase_duration, (
        t.create_emotion_key(0.0, 2),
        t.create_emotion_key(1.34 + 3.88, 2, variation = 1),
        t.create_emotion_key(15.79 + 3.88, 2),
    ), is_snapped_to_end = True, is_mimicry = True)
    t.create_tl_actor_node(bg3.timeline_object.EMOTION, bg3.PEANUT_SLOT_1, '0.0', phase_duration, (
        t.create_emotion_key(0.0, 2),
        t.create_emotion_key(1.34 + 3.88, 2, variation = 1),
        t.create_emotion_key(15.79 + 3.88, 2),
    ), is_snapped_to_end = True, is_mimicry = True)
    t.create_tl_actor_node(bg3.timeline_object.EMOTION, bg3.PEANUT_SLOT_2, '0.0', phase_duration, (
        t.create_emotion_key(0.0, 2),
        t.create_emotion_key(1.34 + 3.88, 2, variation = 1),
        t.create_emotion_key(15.79 + 3.88, 2),
    ), is_snapped_to_end = True, is_mimicry = True)


    t.create_tl_actor_node(bg3.timeline_object.LOOK_AT, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_look_at_key(
            0.0,
            target = bg3.SPEAKER_PLAYER,
            bone = 'Head_M',
            turn_mode = 3,
            turn_speed_multiplier = 0.3,
            head_turn_speed_multiplier = 0.3,
            weight = 0,
            safe_zone_angle = 80,
            head_safe_zone_angle = 80,
            reset = True,
            look_at_mode = 1,
            eye_look_at_bone = 'Head_M'
        ),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.LOOK_AT, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        t.create_look_at_key(
            0.0,
            target = bg3.SPEAKER_SHADOWHEART,
            bone = 'Head_M',
            turn_mode = 3,
            turn_speed_multiplier = 0.3,
            head_turn_speed_multiplier = 0.3,
            weight = 0,
            safe_zone_angle = 80,
            head_safe_zone_angle = 80,
            reset = True,
            look_at_mode = 1,
            eye_look_at_bone = 'Head_M'
        ),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.LOOK_AT, bg3.PEANUT_SLOT_0, '0.0', phase_duration, (
        t.create_look_at_key(
            0.0,
            target = bg3.SPEAKER_SHADOWHEART,
            bone = 'Head_M',
            turn_mode = 3,
            turn_speed_multiplier = 0.3,
            head_turn_speed_multiplier = 0.3,
            weight = 0,
            safe_zone_angle = 80,
            head_safe_zone_angle = 80,
            reset = True,
            look_at_mode = 1,
            eye_look_at_bone = 'Head_M'
        ),
    ), is_snapped_to_end = True, is_mimicry = True)
    t.create_tl_actor_node(bg3.timeline_object.LOOK_AT, bg3.PEANUT_SLOT_1, '0.0', phase_duration, (
        t.create_look_at_key(
            0.0,
            target = bg3.SPEAKER_SHADOWHEART,
            bone = 'Head_M',
            turn_mode = 3,
            turn_speed_multiplier = 0.3,
            head_turn_speed_multiplier = 0.3,
            weight = 0,
            safe_zone_angle = 80,
            head_safe_zone_angle = 80,
            reset = True,
            look_at_mode = 1,
            eye_look_at_bone = 'Head_M'
        ),
    ), is_snapped_to_end = True, is_mimicry = True)
    t.create_tl_actor_node(bg3.timeline_object.LOOK_AT, bg3.PEANUT_SLOT_2, '0.0', phase_duration, (
        t.create_look_at_key(
            0.0,
            target = bg3.SPEAKER_SHADOWHEART,
            bone = 'Head_M',
            turn_mode = 3,
            turn_speed_multiplier = 0.3,
            head_turn_speed_multiplier = 0.3,
            weight = 0,
            safe_zone_angle = 80,
            head_safe_zone_angle = 80,
            reset = True,
            look_at_mode = 1,
            eye_look_at_bone = 'Head_M'
        ),
    ), is_snapped_to_end = True, is_mimicry = True)

    t.create_tl_non_actor_node(bg3.timeline_object.SWITCH_LOCATION, '0.0', phase_duration, (), is_snapped_to_end = True)

    # Place Shadowheart
    t.create_tl_transform(bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        (
            #t.create_value_key(time = 0.0, interpolation_type = 5, value = 0.10027611),
            t.create_value_key(time = 0.0, interpolation_type = 5, value = -0.282674465),
        ),
        (
            #t.create_value_key(time = 0.0, interpolation_type = 5, value = 2.3841858e-07),
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 0.0),
        ),
        (
            #t.create_value_key(time = 0.0, interpolation_type = 5, value = 9.4698734),
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 0.5080471000000006),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = (0.0, -0.24996054, 0.0, 0.96825606)),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 1.0),
        ),
        (),
    ), is_snapped_to_end = True)
    # Place Player
    t.create_tl_transform(bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        (
            #t.create_value_key(time = 0.0, interpolation_type = 5, value = 0.66562504),
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 0.282674465),
        ),
        (
            #t.create_value_key(time = 0.0, interpolation_type = 5, value = 3.5762787e-07),
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 0.0),
        ),
        (
            #t.create_value_key(time = 0.0, interpolation_type = 5, value = 8.4537792),
            t.create_value_key(time = 0.0, interpolation_type = 5, value = -0.5080471000000006),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = (0.0, 0.96666896, 0.0, 0.25602978)),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 1.0),
        ),
        (),
    ), is_snapped_to_end = True)

    t.create_tl_animation(
        bg3.SPEAKER_PLAYER,
        '0.0', '13.06',
        '882164de-1f6b-4d2a-b336-1f366cb36f14',
        'a2dae3f2-e3c9-4fc7-b8ac-82abf4a153b0',
        fade_in = 0.0,
        fade_out = 0.94)
    t.create_tl_animation(
        bg3.SPEAKER_SHADOWHEART,
        '0.0', '13.06',
        'a46f695f-051b-be6d-20cd-32f733524930',
        'c8dad77b-5b76-44fe-bfeb-61d676ede3f6',
        fade_in = 0.0,
        fade_out = 0.94)

    #t.create_tl_shot('befcdee8-6352-4be6-b2ea-23c2ac0dfe60', 0.0, 10.23)
    # looks at Tav
    t.create_tl_shot('fb91b3e2-b1b9-47d5-8478-659cececad9b', '0.0', '7.32')
    # looks at Tav
    t.create_tl_shot('befcdee8-6352-4be6-b2ea-23c2ac0dfe60', '7.32', '14.11')

    t.create_tl_animation(
        bg3.SPEAKER_PLAYER,
        '12.12', '21.67',
        '882164de-1f6b-4d2a-b336-1f366cb36f14',
        'a2dae3f2-e3c9-4fc7-b8ac-82abf4a153b0',
        fade_in = 0.0,
        fade_out = 0.0,
        animation_play_start_offset = 6.29)
    t.create_tl_animation(
        bg3.SPEAKER_SHADOWHEART,
        '12.12', '21.67',
        'a46f695f-051b-be6d-20cd-32f733524930',
        'c8dad77b-5b76-44fe-bfeb-61d676ede3f6',
        fade_in = 0.0,
        fade_out = 0.0,
        animation_play_start_offset = 6.29)

    #t.create_tl_shot('18c5bd4f-c066-4c52-8cdb-d8bbe1d8034e', 10.23, 20.67, is_snapped_to_end = True)
    # looks at Shadowheart
    t.create_tl_shot('18c5bd4f-c066-4c52-8cdb-d8bbe1d8034e', '14.11', '21.67')
    # looks at Tav
    t.create_tl_shot('cb95fcb5-efd7-48f4-9352-5eaeb3e44274', '21.67', phase_duration, is_snapped_to_end = True)

    t.create_tl_animation(
        bg3.SPEAKER_PLAYER,
        '21.67', phase_duration,
        '882164de-1f6b-4d2a-b336-1f366cb36f14',
        'a2dae3f2-e3c9-4fc7-b8ac-82abf4a153b0',
        fade_in = 0.0,
        fade_out = 2.0,
        animation_play_start_offset = 16.79,
        is_snapped_to_end = True)
    t.create_tl_animation(
        bg3.SPEAKER_SHADOWHEART,
        '21.67', phase_duration,
        'a46f695f-051b-be6d-20cd-32f733524930',
        'c8dad77b-5b76-44fe-bfeb-61d676ede3f6',
        fade_in = 0.0,
        fade_out = 1.44,
        animation_play_start_offset = 16.79,
        is_snapped_to_end = True)


    ###########################################################################
    # Normal body type, sad hug
    ###########################################################################
    t.create_new_phase(hug_sad_normal_node_uuid, phase_duration)

    t.create_tl_actor_node(bg3.timeline_object.ATTITUDE, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.ATTITUDE, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        t.create_attitude_key(0.0, bg3.ATTITUDE_DIAG_Pose_Stand_L_Forward_01, bg3.ATTITUDE_DIAG_T_Pose),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.ATTITUDE, bg3.PEANUT_SLOT_0, '0.0', phase_duration, (
        t.create_attitude_key(0.5, bg3.ATTITUDE_DIAG_Pose_Stand_L_Forward_01, bg3.ATTITUDE_DIAG_T_Pose),
    ), is_snapped_to_end = True, is_mimicry = True)
    t.create_tl_actor_node(bg3.timeline_object.ATTITUDE, bg3.PEANUT_SLOT_1, '0.0', phase_duration, (
        t.create_attitude_key(0.5, bg3.ATTITUDE_DIAG_Pose_Stand_L_Forward_01, bg3.ATTITUDE_DIAG_T_Pose),
    ), is_snapped_to_end = True, is_mimicry = True)
    t.create_tl_actor_node(bg3.timeline_object.ATTITUDE, bg3.PEANUT_SLOT_2, '0.0', phase_duration, (
        t.create_attitude_key(0.5, bg3.ATTITUDE_DIAG_Pose_Stand_L_Forward_01, bg3.ATTITUDE_DIAG_T_Pose),
    ), is_snapped_to_end = True, is_mimicry = True)

    t.create_tl_actor_node(bg3.timeline_object.EMOTION, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_emotion_key(0.0, 32, variation = 2),
        t.create_emotion_key(1.34 + 3.88, 32, variation = 24),
        t.create_emotion_key(15.79 + 3.88, 32, variation = 1),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.EMOTION, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        t.create_emotion_key(5.99 + 3.88, 32, variation = 1),
        t.create_emotion_key(8.83 + 3.88, 2048, variation = 2),
        t.create_emotion_key(12.08 + 3.88, 32, variation = 1),
        t.create_emotion_key('21.67', 2048, variation = 1),
    ))
    t.create_tl_actor_node(bg3.timeline_object.EMOTION, bg3.PEANUT_SLOT_0, '0.0', phase_duration, (
        t.create_emotion_key(0.0, 32),
        t.create_emotion_key(1.34 + 3.88, 32, variation = 1),
        t.create_emotion_key(15.79 + 3.88, 32),
    ), is_snapped_to_end = True, is_mimicry = True)
    t.create_tl_actor_node(bg3.timeline_object.EMOTION, bg3.PEANUT_SLOT_1, '0.0', phase_duration, (
        t.create_emotion_key(0.0, 32),
        t.create_emotion_key(1.34 + 3.88, 32, variation = 1),
        t.create_emotion_key(15.79 + 3.88, 32),
    ), is_snapped_to_end = True, is_mimicry = True)
    t.create_tl_actor_node(bg3.timeline_object.EMOTION, bg3.PEANUT_SLOT_2, '0.0', phase_duration, (
        t.create_emotion_key(0.0, 32),
        t.create_emotion_key(1.34 + 3.88, 32, variation = 1),
        t.create_emotion_key(15.79 + 3.88, 32),
    ), is_snapped_to_end = True, is_mimicry = True)

    t.create_tl_actor_node(bg3.timeline_object.LOOK_AT, bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        t.create_look_at_key(
            0.0,
            target = bg3.SPEAKER_PLAYER,
            bone = 'Head_M',
            turn_mode = 3,
            turn_speed_multiplier = 0.3,
            head_turn_speed_multiplier = 0.3,
            weight = 0,
            safe_zone_angle = 80,
            head_safe_zone_angle = 80,
            reset = True,
            look_at_mode = 1,
            eye_look_at_bone = 'Head_M'
        ),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.LOOK_AT, bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        t.create_look_at_key(
            0.0,
            target = bg3.SPEAKER_SHADOWHEART,
            bone = 'Head_M',
            turn_mode = 3,
            turn_speed_multiplier = 0.3,
            head_turn_speed_multiplier = 0.3,
            weight = 0,
            safe_zone_angle = 80,
            head_safe_zone_angle = 80,
            reset = True,
            look_at_mode = 1,
            eye_look_at_bone = 'Head_M'
        ),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.LOOK_AT, bg3.PEANUT_SLOT_0, '0.0', phase_duration, (
        t.create_look_at_key(
            0.0,
            target = bg3.SPEAKER_SHADOWHEART,
            bone = 'Head_M',
            turn_mode = 3,
            turn_speed_multiplier = 0.3,
            head_turn_speed_multiplier = 0.3,
            weight = 0,
            safe_zone_angle = 80,
            head_safe_zone_angle = 80,
            reset = True,
            look_at_mode = 1,
            eye_look_at_bone = 'Head_M'
        ),
    ), is_snapped_to_end = True, is_mimicry = True)
    t.create_tl_actor_node(bg3.timeline_object.LOOK_AT, bg3.PEANUT_SLOT_1, '0.0', phase_duration, (
        t.create_look_at_key(
            0.0,
            target = bg3.SPEAKER_SHADOWHEART,
            bone = 'Head_M',
            turn_mode = 3,
            turn_speed_multiplier = 0.3,
            head_turn_speed_multiplier = 0.3,
            weight = 0,
            safe_zone_angle = 80,
            head_safe_zone_angle = 80,
            reset = True,
            look_at_mode = 1,
            eye_look_at_bone = 'Head_M'
        ),
    ), is_snapped_to_end = True, is_mimicry = True)
    t.create_tl_actor_node(bg3.timeline_object.LOOK_AT, bg3.PEANUT_SLOT_2, '0.0', phase_duration, (
        t.create_look_at_key(
            0.0,
            target = bg3.SPEAKER_SHADOWHEART,
            bone = 'Head_M',
            turn_mode = 3,
            turn_speed_multiplier = 0.3,
            head_turn_speed_multiplier = 0.3,
            weight = 0,
            safe_zone_angle = 80,
            head_safe_zone_angle = 80,
            reset = True,
            look_at_mode = 1,
            eye_look_at_bone = 'Head_M'
        ),
    ), is_snapped_to_end = True, is_mimicry = True)

    t.create_tl_non_actor_node(bg3.timeline_object.SWITCH_LOCATION, '0.0', phase_duration, (), is_snapped_to_end = True)

    # Place Shadowheart
    t.create_tl_transform(bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        (
            #t.create_value_key(time = 0.0, interpolation_type = 5, value = 0.10027611),
            t.create_value_key(time = 0.0, interpolation_type = 5, value = -0.282674465),
        ),
        (
            #t.create_value_key(time = 0.0, interpolation_type = 5, value = 2.3841858e-07),
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 0.0),
        ),
        (
            #t.create_value_key(time = 0.0, interpolation_type = 5, value = 9.4698734),
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 0.5080471000000006),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = (0.0, -0.24996054, 0.0, 0.96825606)),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 1.0),
        ),
        (),
    ), is_snapped_to_end = True)
    # Place Player
    t.create_tl_transform(bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        (
            #t.create_value_key(time = 0.0, interpolation_type = 5, value = 0.66562504),
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 0.282674465),
        ),
        (
            #t.create_value_key(time = 0.0, interpolation_type = 5, value = 3.5762787e-07),
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 0.0),
        ),
        (
            #t.create_value_key(time = 0.0, interpolation_type = 5, value = 8.4537792),
            t.create_value_key(time = 0.0, interpolation_type = 5, value = -0.5080471000000006),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = (0.0, 0.96666896, 0.0, 0.25602978)),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 1.0),
        ),
        (),
    ), is_snapped_to_end = True)


    t.create_tl_animation(
        bg3.SPEAKER_PLAYER,
        '0.0', '13.06',
        '882164de-1f6b-4d2a-b336-1f366cb36f14',
        'a2dae3f2-e3c9-4fc7-b8ac-82abf4a153b0',
        fade_in = 0.0,
        fade_out = 0.94)
    t.create_tl_animation(
        bg3.SPEAKER_SHADOWHEART,
        '0.0', '13.06',
        'a46f695f-051b-be6d-20cd-32f733524930',
        'c8dad77b-5b76-44fe-bfeb-61d676ede3f6',
        fade_in = 0.0,
        fade_out = 0.94)

    t.create_tl_shot('fb91b3e2-b1b9-47d5-8478-659cececad9b', '0.0', '7.32')
    t.create_tl_shot('befcdee8-6352-4be6-b2ea-23c2ac0dfe60', '7.32', '14.11')

    t.create_tl_animation(
        bg3.SPEAKER_PLAYER,
        '12.12', '21.67',
        '882164de-1f6b-4d2a-b336-1f366cb36f14',
        'a2dae3f2-e3c9-4fc7-b8ac-82abf4a153b0',
        fade_in = 0.0,
        fade_out = 0.0,
        animation_play_start_offset = 6.29)
    t.create_tl_animation(
        bg3.SPEAKER_SHADOWHEART,
        '12.12', '21.67',
        'a46f695f-051b-be6d-20cd-32f733524930',
        'c8dad77b-5b76-44fe-bfeb-61d676ede3f6',
        fade_in = 0.0,
        fade_out = 0.0,
        animation_play_start_offset = 6.29)

    t.create_tl_shot('18c5bd4f-c066-4c52-8cdb-d8bbe1d8034e', '14.11', '21.67')
    t.create_tl_shot('cb95fcb5-efd7-48f4-9352-5eaeb3e44274', '21.67', phase_duration, is_snapped_to_end = True)

    t.create_tl_animation(
        bg3.SPEAKER_PLAYER,
        '21.67', phase_duration,
        '882164de-1f6b-4d2a-b336-1f366cb36f14',
        'a2dae3f2-e3c9-4fc7-b8ac-82abf4a153b0',
        fade_in = 0.0,
        fade_out = 2.0,
        animation_play_start_offset = 16.79,
        is_snapped_to_end = True)
    t.create_tl_animation(
        bg3.SPEAKER_SHADOWHEART,
        '21.67', phase_duration,
        'a46f695f-051b-be6d-20cd-32f733524930',
        'c8dad77b-5b76-44fe-bfeb-61d676ede3f6',
        fade_in = 0.0,
        fade_out = 1.44,
        animation_play_start_offset = 16.79,
        is_snapped_to_end = True)


    ###########################################################################
    # Strong body type
    ###########################################################################
    t.create_new_cinematic_phase_from_another(
        hug_normal_node_uuid,
        hug_strong_node_uuid,
        skip_tl_nodes = ('TLAnimation', 'TLShot')
    )

    t.create_tl_shot('fb91b3e2-b1b9-47d5-8478-659cececad9b', '0.0', '7.32')
    t.create_tl_shot('befcdee8-6352-4be6-b2ea-23c2ac0dfe60', '7.32', '21.67')

    t.create_tl_animation(
        bg3.SPEAKER_PLAYER,
        '0.0', '13.06',
        'fb8fbad0-57be-4c54-936b-a58c8fa46876',
        'a2dae3f2-e3c9-4fc7-b8ac-82abf4a153b0',
        fade_in = 0.0,
        fade_out = 0.94)
    t.create_tl_animation(
        bg3.SPEAKER_SHADOWHEART,
        '0.0', '13.06',
        'd8684f69-0a63-33dd-3304-87e0128c21ba',
        'c8dad77b-5b76-44fe-bfeb-61d676ede3f6',
        fade_in = 0.0,
        fade_out = 0.94)
    t.create_tl_animation(
        bg3.SPEAKER_PLAYER,
        '12.12', '21.67',
        'fb8fbad0-57be-4c54-936b-a58c8fa46876',
        'a2dae3f2-e3c9-4fc7-b8ac-82abf4a153b0',
        fade_in = 0.0,
        fade_out = 0.0,
        animation_play_start_offset = 6.29)
    t.create_tl_animation(
        bg3.SPEAKER_SHADOWHEART,
        '12.12', '21.67',
        'd8684f69-0a63-33dd-3304-87e0128c21ba',
        'c8dad77b-5b76-44fe-bfeb-61d676ede3f6',
        fade_in = 0.0,
        fade_out = 0.0,
        animation_play_start_offset = 6.29)

    t.create_tl_shot('cb95fcb5-efd7-48f4-9352-5eaeb3e44274', '21.67', phase_duration, is_snapped_to_end = True)

    t.create_tl_animation(
        bg3.SPEAKER_PLAYER,
        '21.67', phase_duration,
        'fb8fbad0-57be-4c54-936b-a58c8fa46876',
        'a2dae3f2-e3c9-4fc7-b8ac-82abf4a153b0',
        fade_in = 0.0,
        fade_out = 2.0,
        animation_play_start_offset = 16.79,
        is_snapped_to_end = True)
    t.create_tl_animation(
        bg3.SPEAKER_SHADOWHEART,
        '21.67', phase_duration,
        'd8684f69-0a63-33dd-3304-87e0128c21ba',
        'c8dad77b-5b76-44fe-bfeb-61d676ede3f6',
        fade_in = 0.0,
        fade_out = 1.44,
        animation_play_start_offset = 16.79,
        is_snapped_to_end = True)


    ###########################################################################
    # Strong body type, sad hug
    ###########################################################################
    t.create_new_cinematic_phase_from_another(
        hug_sad_normal_node_uuid,
        hug_sad_strong_node_uuid,
        skip_tl_nodes = ('TLAnimation', 'TLShot')
    )

    t.create_tl_shot('fb91b3e2-b1b9-47d5-8478-659cececad9b', '0.0', '7.32')
    t.create_tl_shot('befcdee8-6352-4be6-b2ea-23c2ac0dfe60', '7.32', '21.67')

    t.create_tl_animation(
        bg3.SPEAKER_PLAYER,
        '0.0', '13.06',
        'fb8fbad0-57be-4c54-936b-a58c8fa46876',
        'a2dae3f2-e3c9-4fc7-b8ac-82abf4a153b0',
        fade_in = 0.0,
        fade_out = 0.94)
    t.create_tl_animation(
        bg3.SPEAKER_SHADOWHEART,
        '0.0', '13.06',
        'd8684f69-0a63-33dd-3304-87e0128c21ba',
        'c8dad77b-5b76-44fe-bfeb-61d676ede3f6',
        fade_in = 0.0,
        fade_out = 0.94)
    t.create_tl_animation(
        bg3.SPEAKER_PLAYER,
        '12.12', '21.67',
        'fb8fbad0-57be-4c54-936b-a58c8fa46876',
        'a2dae3f2-e3c9-4fc7-b8ac-82abf4a153b0',
        fade_in = 0.0,
        fade_out = 0.0,
        animation_play_start_offset = 6.29)
    t.create_tl_animation(
        bg3.SPEAKER_SHADOWHEART,
        '12.12', '21.67',
        'd8684f69-0a63-33dd-3304-87e0128c21ba',
        'c8dad77b-5b76-44fe-bfeb-61d676ede3f6',
        fade_in = 0.0,
        fade_out = 0.0,
        animation_play_start_offset = 6.29)

    t.create_tl_shot('cb95fcb5-efd7-48f4-9352-5eaeb3e44274', '21.67', phase_duration, is_snapped_to_end = True)

    t.create_tl_animation(
        bg3.SPEAKER_PLAYER,
        '21.67', phase_duration,
        'fb8fbad0-57be-4c54-936b-a58c8fa46876',
        'a2dae3f2-e3c9-4fc7-b8ac-82abf4a153b0',
        fade_in = 0.0,
        fade_out = 2.0,
        animation_play_start_offset = 16.79,
        is_snapped_to_end = True)
    t.create_tl_animation(
        bg3.SPEAKER_SHADOWHEART,
        '21.67', phase_duration,
        'd8684f69-0a63-33dd-3304-87e0128c21ba',
        'c8dad77b-5b76-44fe-bfeb-61d676ede3f6',
        fade_in = 0.0,
        fade_out = 1.44,
        animation_play_start_offset = 16.79,
        is_snapped_to_end = True)


    ###########################################################################
    # Short body type
    ###########################################################################
    t.create_new_cinematic_phase_from_another(
        hug_normal_node_uuid,
        hug_short_node_uuid,
        skip_tl_nodes = ('TLAnimation', 'TLTransform', 'TLShot')
    )
    # Place Shadowheart
    t.create_tl_transform(bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        (
            #t.create_value_key(time = 0.0, interpolation_type = 5, value = 0.35311571),
            t.create_value_key(time = 0.0, interpolation_type = 5, value = -0.13836698),
        ),
        (
            #t.create_value_key(time = 0.0, interpolation_type = 5, value = 2.3841858e-07),
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 0.0),
        ),
        (
            #t.create_value_key(time = 0.0, interpolation_type = 5, value = 9.1730099),
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 0.36940669999999987),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = (0.0, -0.20995708, 0.0, 0.9777106)),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 1.0),
        ),
        (),
    ), is_snapped_to_end = True)
    # Place Player
    t.create_tl_transform(bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        (
            #t.create_value_key(time = 0.0, interpolation_type = 5, value = 0.62984967),
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 0.13836698),
        ),
        (
            #t.create_value_key(time = 0.0, interpolation_type = 5, value = 3.5762787e-07),
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 0.0),
        ),
        (
            #t.create_value_key(time = 0.0, interpolation_type = 5, value = 8.4341965),
            t.create_value_key(time = 0.0, interpolation_type = 5, value = -0.36940669999999987),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = (0.0, 0.98319805, 0.0, 0.18254192)),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 1.0),
        ),
        (),
    ), is_snapped_to_end = True)
    t.create_tl_animation(
        bg3.SPEAKER_PLAYER,
        '0.0', '13.65',
        '0a5b7810-3652-4465-876c-f6947aa618cf',
        'a2dae3f2-e3c9-4fc7-b8ac-82abf4a153b0',
        fade_in = 0.0,
        fade_out = 1.53)
    t.create_tl_animation(
        bg3.SPEAKER_SHADOWHEART,
        '0.0', '13.65',
        'd3cb3816-2562-6bbc-2e32-6e956c325718',
        'c8dad77b-5b76-44fe-bfeb-61d676ede3f6',
        fade_in = 0.0,
        fade_out = 1.53)

    t.create_tl_shot('befcdee8-6352-4be6-b2ea-23c2ac0dfe60', '0.0', '14.11')

    t.create_tl_animation(
        bg3.SPEAKER_PLAYER,
        '12.12', '21.67',
        '0a5b7810-3652-4465-876c-f6947aa618cf',
        'a2dae3f2-e3c9-4fc7-b8ac-82abf4a153b0',
        fade_in = 0.0,
        fade_out = 0.0,
        animation_play_start_offset = 8.0)
    t.create_tl_animation(
        bg3.SPEAKER_SHADOWHEART,
        '12.12', '21.67',
        'd3cb3816-2562-6bbc-2e32-6e956c325718',
        'c8dad77b-5b76-44fe-bfeb-61d676ede3f6',
        fade_in = 0.0,
        fade_out = 0.0,
        animation_play_start_offset = 8.0)

    #t.create_tl_shot('18c5bd4f-c066-4c52-8cdb-d8bbe1d8034e', '14.11', phase_duration, is_snapped_to_end = True)
    t.create_tl_camera_fov('18c5bd4f-c066-4c52-8cdb-d8bbe1d8034e', '14.11', '21.67', (
        t.create_value_key(time = 10.23 + 3.88, value = 30.0, value_name = 'FoV', interpolation_type = 3),
    ))
    t.create_tl_shot('18c5bd4f-c066-4c52-8cdb-d8bbe1d8034e', '14.11', '21.67')
    t.create_tl_shot('cb95fcb5-efd7-48f4-9352-5eaeb3e44274', '21.67', phase_duration, is_snapped_to_end = True)

    t.create_tl_animation(
        bg3.SPEAKER_PLAYER,
        '21.67', phase_duration,
        '0a5b7810-3652-4465-876c-f6947aa618cf',
        'a2dae3f2-e3c9-4fc7-b8ac-82abf4a153b0',
        fade_in = 0.0,
        fade_out = 2.5,
        animation_play_start_offset = 22.0,
        is_snapped_to_end = True)
    t.create_tl_animation(
        bg3.SPEAKER_SHADOWHEART,
        '21.67', phase_duration,
        'd3cb3816-2562-6bbc-2e32-6e956c325718',
        'c8dad77b-5b76-44fe-bfeb-61d676ede3f6',
        fade_in = 0.0,
        fade_out = 1.44,
        animation_play_start_offset = 22.0,
        is_snapped_to_end = True)


    ###########################################################################
    # Short body type, sad hug
    ###########################################################################
    t.create_new_cinematic_phase_from_another(
        hug_sad_normal_node_uuid,
        hug_sad_short_node_uuid,
        skip_tl_nodes = ('TLAnimation', 'TLTransform', 'TLShot')
    )
    # Place Shadowheart
    t.create_tl_transform(bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        (
            #t.create_value_key(time = 0.0, interpolation_type = 5, value = 0.35311571),
            t.create_value_key(time = 0.0, interpolation_type = 5, value = -0.13836698),
        ),
        (
            #t.create_value_key(time = 0.0, interpolation_type = 5, value = 2.3841858e-07),
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 0.0),
        ),
        (
            #t.create_value_key(time = 0.0, interpolation_type = 5, value = 9.1730099),
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 0.36940669999999987),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = (0.0, -0.20995708, 0.0, 0.9777106)),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 1.0),
        ),
        (),
    ), is_snapped_to_end = True)
    # Place Player
    t.create_tl_transform(bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        (
            #t.create_value_key(time = 0.0, interpolation_type = 5, value = 0.62984967),
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 0.13836698),
        ),
        (
            #t.create_value_key(time = 0.0, interpolation_type = 5, value = 3.5762787e-07),
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 0.0),
        ),
        (
            #t.create_value_key(time = 0.0, interpolation_type = 5, value = 8.4341965),
            t.create_value_key(time = 0.0, interpolation_type = 5, value = -0.36940669999999987),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = (0.0, 0.98319805, 0.0, 0.18254192)),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 1.0),
        ),
        (),
    ), is_snapped_to_end = True)
    t.create_tl_animation(
        bg3.SPEAKER_PLAYER,
        '0.0', '13.65',
        '0a5b7810-3652-4465-876c-f6947aa618cf',
        'a2dae3f2-e3c9-4fc7-b8ac-82abf4a153b0',
        fade_in = 0.0,
        fade_out = 1.53)
    t.create_tl_animation(
        bg3.SPEAKER_SHADOWHEART,
        '0.0', '13.65',
        'd3cb3816-2562-6bbc-2e32-6e956c325718',
        'c8dad77b-5b76-44fe-bfeb-61d676ede3f6',
        fade_in = 0.0,
        fade_out = 1.53)
    t.create_tl_shot('befcdee8-6352-4be6-b2ea-23c2ac0dfe60', '0.0', '14.11')
    t.create_tl_animation(
        bg3.SPEAKER_PLAYER,
        '12.12', '21.67',
        '0a5b7810-3652-4465-876c-f6947aa618cf',
        'a2dae3f2-e3c9-4fc7-b8ac-82abf4a153b0',
        fade_in = 0.0,
        fade_out = 0.0,
        animation_play_start_offset = 8.0)
    t.create_tl_animation(
        bg3.SPEAKER_SHADOWHEART,
        '12.12', '21.67',
        'd3cb3816-2562-6bbc-2e32-6e956c325718',
        'c8dad77b-5b76-44fe-bfeb-61d676ede3f6',
        fade_in = 0.0,
        fade_out = 0.0,
        animation_play_start_offset = 8.0)

    #t.create_tl_shot('18c5bd4f-c066-4c52-8cdb-d8bbe1d8034e', '14.11', phase_duration, is_snapped_to_end = True)
    t.create_tl_camera_fov('18c5bd4f-c066-4c52-8cdb-d8bbe1d8034e', '14.11', '21.67', (
        t.create_value_key(time = 10.23 + 3.88, value = 30.0, value_name = 'FoV', interpolation_type = 3),
    ))
    t.create_tl_shot('18c5bd4f-c066-4c52-8cdb-d8bbe1d8034e', '14.11', '21.67')
    t.create_tl_shot('cb95fcb5-efd7-48f4-9352-5eaeb3e44274', '21.67', phase_duration, is_snapped_to_end = True)

    t.create_tl_animation(
        bg3.SPEAKER_PLAYER,
        '21.67', phase_duration,
        '0a5b7810-3652-4465-876c-f6947aa618cf',
        'a2dae3f2-e3c9-4fc7-b8ac-82abf4a153b0',
        fade_in = 0.0,
        fade_out = 2.5,
        animation_play_start_offset = 22.0,
        is_snapped_to_end = True)
    t.create_tl_animation(
        bg3.SPEAKER_SHADOWHEART,
        '21.67', phase_duration,
        'd3cb3816-2562-6bbc-2e32-6e956c325718',
        'c8dad77b-5b76-44fe-bfeb-61d676ede3f6',
        fade_in = 0.0,
        fade_out = 1.44,
        animation_play_start_offset = 22.0,
        is_snapped_to_end = True)


    ###########################################################################
    # Dwarf body type
    ###########################################################################
    t.create_new_cinematic_phase_from_another(
        hug_normal_node_uuid,
        hug_dwarf_node_uuid,
        skip_tl_nodes = ('TLAnimation', 'TLTransform', 'TLShot')
    )
    # Place Shadowheart
    t.create_tl_transform(bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        (
            #t.create_value_key(time = 0.0, interpolation_type = 5, value = 0.35311571),
            t.create_value_key(time = 0.0, interpolation_type = 5, value = -0.13836698),
        ),
        (
            #t.create_value_key(time = 0.0, interpolation_type = 5, value = 2.3841858e-07),
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 0.0),
        ),
        (
            #t.create_value_key(time = 0.0, interpolation_type = 5, value = 9.1730099),
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 0.36940669999999987),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = (0.0, -0.20995708, 0.0, 0.9777106)),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 1.0),
        ),
        (),
    ), is_snapped_to_end = True)
    # Place Player
    t.create_tl_transform(bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        (
            #t.create_value_key(time = 0.0, interpolation_type = 5, value = 0.62984967),
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 0.13836698),
        ),
        (
            #t.create_value_key(time = 0.0, interpolation_type = 5, value = 3.5762787e-07),
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 0.0),
        ),
        (
            #t.create_value_key(time = 0.0, interpolation_type = 5, value = 8.4341965),
            t.create_value_key(time = 0.0, interpolation_type = 5, value = -0.36940669999999987),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = (0.0, 0.98319805, 0.0, 0.18254192)),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 1.0),
        ),
        (),
    ), is_snapped_to_end = True)


    t.create_tl_animation(
        bg3.SPEAKER_PLAYER,
        '0.0', '13.65',
        '54f674a3-2ae4-42c0-a0ae-b178239a79cd',
        'a2dae3f2-e3c9-4fc7-b8ac-82abf4a153b0',
        fade_in = 0.0,
        fade_out = 1.53)
    t.create_tl_animation(
        bg3.SPEAKER_SHADOWHEART,
        '0.0', '13.65',
        'e3194510-d4e1-18cc-c8c0-3174c912c168',
        'c8dad77b-5b76-44fe-bfeb-61d676ede3f6',
        fade_in = 0.0,
        fade_out = 1.53)

    t.create_tl_shot('befcdee8-6352-4be6-b2ea-23c2ac0dfe60', '0.0', '14.11')

    t.create_tl_animation(
        bg3.SPEAKER_PLAYER,
        '12.12', '21.67',
        '54f674a3-2ae4-42c0-a0ae-b178239a79cd',
        'a2dae3f2-e3c9-4fc7-b8ac-82abf4a153b0',
        fade_in = 0.0,
        fade_out = 0.0,
        animation_play_start_offset = 8.0)
    t.create_tl_animation(
        bg3.SPEAKER_SHADOWHEART,
        '12.12', '21.67',
        'e3194510-d4e1-18cc-c8c0-3174c912c168',
        'c8dad77b-5b76-44fe-bfeb-61d676ede3f6',
        fade_in = 0.0,
        fade_out = 0.0,
        animation_play_start_offset = 8.0)

    #t.create_tl_shot('18c5bd4f-c066-4c52-8cdb-d8bbe1d8034e', '14.11', phase_duration, is_snapped_to_end = True)
    t.create_tl_shot('18c5bd4f-c066-4c52-8cdb-d8bbe1d8034e', '14.11', '21.67')
    t.create_tl_camera_fov('18c5bd4f-c066-4c52-8cdb-d8bbe1d8034e', '14.11', '21.67', (
        t.create_value_key(time = 10.23 + 3.88, value = 30.0, value_name = 'FoV', interpolation_type = 3),
    ))
    t.create_tl_shot('cb95fcb5-efd7-48f4-9352-5eaeb3e44274', '21.67', phase_duration, is_snapped_to_end = True)

    t.create_tl_animation(
        bg3.SPEAKER_PLAYER,
        '21.67', phase_duration,
        '54f674a3-2ae4-42c0-a0ae-b178239a79cd',
        'a2dae3f2-e3c9-4fc7-b8ac-82abf4a153b0',
        fade_in = 0.0,
        fade_out = 2.5,
        animation_play_start_offset = 22.0,
        is_snapped_to_end = True)
    t.create_tl_animation(
        bg3.SPEAKER_SHADOWHEART,
        '21.67', phase_duration,
        'e3194510-d4e1-18cc-c8c0-3174c912c168',
        'c8dad77b-5b76-44fe-bfeb-61d676ede3f6',
        fade_in = 0.0,
        fade_out = 1.44,
        animation_play_start_offset = 22.0,
        is_snapped_to_end = True)


    ###########################################################################
    # Dwarf body type, sad hug
    ###########################################################################
    t.create_new_cinematic_phase_from_another(
        hug_sad_normal_node_uuid,
        hug_sad_dwarf_node_uuid,
        skip_tl_nodes = ('TLAnimation', 'TLTransform', 'TLShot')
    )
    # Place Shadowheart
    t.create_tl_transform(bg3.SPEAKER_SHADOWHEART, '0.0', phase_duration, (
        (
            #t.create_value_key(time = 0.0, interpolation_type = 5, value = 0.35311571),
            t.create_value_key(time = 0.0, interpolation_type = 5, value = -0.13836698),
        ),
        (
            #t.create_value_key(time = 0.0, interpolation_type = 5, value = 2.3841858e-07),
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 0.0),
        ),
        (
            #t.create_value_key(time = 0.0, interpolation_type = 5, value = 9.1730099),
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 0.36940669999999987),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = (0.0, -0.20995708, 0.0, 0.9777106)),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 1.0),
        ),
        (),
    ), is_snapped_to_end = True)
    # Place Player
    t.create_tl_transform(bg3.SPEAKER_PLAYER, '0.0', phase_duration, (
        (
            #t.create_value_key(time = 0.0, interpolation_type = 5, value = 0.62984967),
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 0.13836698),
        ),
        (
            #t.create_value_key(time = 0.0, interpolation_type = 5, value = 3.5762787e-07),
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 0.0),
        ),
        (
            #t.create_value_key(time = 0.0, interpolation_type = 5, value = 8.4341965),
            t.create_value_key(time = 0.0, interpolation_type = 5, value = -0.36940669999999987),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = (0.0, 0.98319805, 0.0, 0.18254192)),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 1.0),
        ),
        (),
    ), is_snapped_to_end = True)


    t.create_tl_animation(
        bg3.SPEAKER_PLAYER,
        '0.0', '13.65',
        '54f674a3-2ae4-42c0-a0ae-b178239a79cd',
        'a2dae3f2-e3c9-4fc7-b8ac-82abf4a153b0',
        fade_in = 0.0,
        fade_out = 1.53)
    t.create_tl_animation(
        bg3.SPEAKER_SHADOWHEART,
        '0.0', '13.65',
        'e3194510-d4e1-18cc-c8c0-3174c912c168',
        'c8dad77b-5b76-44fe-bfeb-61d676ede3f6',
        fade_in = 0.0,
        fade_out = 1.53)

    t.create_tl_shot('befcdee8-6352-4be6-b2ea-23c2ac0dfe60', '0.0', '14.11')

    t.create_tl_animation(
        bg3.SPEAKER_PLAYER,
        '12.12', '21.67',
        '54f674a3-2ae4-42c0-a0ae-b178239a79cd',
        'a2dae3f2-e3c9-4fc7-b8ac-82abf4a153b0',
        fade_in = 0.0,
        fade_out = 0.0,
        animation_play_start_offset = 8.0)
    t.create_tl_animation(
        bg3.SPEAKER_SHADOWHEART,
        '12.12', '21.67',
        'e3194510-d4e1-18cc-c8c0-3174c912c168',
        'c8dad77b-5b76-44fe-bfeb-61d676ede3f6',
        fade_in = 0.0,
        fade_out = 0.0,
        animation_play_start_offset = 8.0)

    #t.create_tl_shot('18c5bd4f-c066-4c52-8cdb-d8bbe1d8034e', '14.11', phase_duration, is_snapped_to_end = True)
    t.create_tl_camera_fov('18c5bd4f-c066-4c52-8cdb-d8bbe1d8034e', '14.11', '21.67', (
        t.create_value_key(time = 10.23 + 3.88, value = 30.0, value_name = 'FoV', interpolation_type = 3),
    ))
    t.create_tl_shot('18c5bd4f-c066-4c52-8cdb-d8bbe1d8034e', '14.11', '21.67')
    t.create_tl_shot('cb95fcb5-efd7-48f4-9352-5eaeb3e44274', '21.67', phase_duration, is_snapped_to_end = True)

    t.create_tl_animation(
        bg3.SPEAKER_PLAYER,
        '21.67', phase_duration,
        '54f674a3-2ae4-42c0-a0ae-b178239a79cd',
        'a2dae3f2-e3c9-4fc7-b8ac-82abf4a153b0',
        fade_in = 0.0,
        fade_out = 2.5,
        animation_play_start_offset = 22.0,
        is_snapped_to_end = True)
    t.create_tl_animation(
        bg3.SPEAKER_SHADOWHEART,
        '21.67', phase_duration,
        'e3194510-d4e1-18cc-c8c0-3174c912c168',
        'c8dad77b-5b76-44fe-bfeb-61d676ede3f6',
        fade_in = 0.0,
        fade_out = 1.44,
        animation_play_start_offset = 22.0,
        is_snapped_to_end = True)


    ###########################################################################
    # Dragonborn body type
    ###########################################################################
    t.create_new_cinematic_phase_from_another(
        hug_normal_node_uuid,
        hug_dragonborn_node_uuid,
        skip_tl_nodes = ('TLAnimation', 'TLShot')
    )

    t.create_tl_shot('befcdee8-6352-4be6-b2ea-23c2ac0dfe60', '0.0', '21.67')

    t.create_tl_animation(
        bg3.SPEAKER_PLAYER,
        '0.0', '13.06',
        '84117bdc-71dd-47a2-9cba-039df0b1890d',
        'a2dae3f2-e3c9-4fc7-b8ac-82abf4a153b0',
        fade_in = 0.0,
        fade_out = 0.94)
    t.create_tl_animation(
        bg3.SPEAKER_SHADOWHEART,
        '0.0', '13.06',
        '57523fff-f67e-c3d5-59a4-b45a84d3eaec',
        'c8dad77b-5b76-44fe-bfeb-61d676ede3f6',
        fade_in = 0.0,
        fade_out = 0.94)
    t.create_tl_animation(
        bg3.SPEAKER_PLAYER,
        '12.12', '21.67',
        '84117bdc-71dd-47a2-9cba-039df0b1890d',
        'a2dae3f2-e3c9-4fc7-b8ac-82abf4a153b0',
        fade_in = 0.0,
        fade_out = 0.0,
        animation_play_start_offset = 6.29)
    t.create_tl_animation(
        bg3.SPEAKER_SHADOWHEART,
        '12.12', '21.67',
        '57523fff-f67e-c3d5-59a4-b45a84d3eaec',
        'c8dad77b-5b76-44fe-bfeb-61d676ede3f6',
        fade_in = 0.0,
        fade_out = 0.0,
        animation_play_start_offset = 6.29)

    t.create_tl_shot('cb95fcb5-efd7-48f4-9352-5eaeb3e44274', '21.67', phase_duration, is_snapped_to_end = True)

    t.create_tl_animation(
        bg3.SPEAKER_PLAYER,
        '21.67', phase_duration,
        '84117bdc-71dd-47a2-9cba-039df0b1890d',
        'a2dae3f2-e3c9-4fc7-b8ac-82abf4a153b0',
        fade_in = 0.0,
        fade_out = 2.0,
        animation_play_start_offset = 16.79,
        is_snapped_to_end = True)
    t.create_tl_animation(
        bg3.SPEAKER_SHADOWHEART,
        '21.67', phase_duration,
        '57523fff-f67e-c3d5-59a4-b45a84d3eaec',
        'c8dad77b-5b76-44fe-bfeb-61d676ede3f6',
        fade_in = 0.0,
        fade_out = 1.44,
        animation_play_start_offset = 16.79,
        is_snapped_to_end = True)


    ###########################################################################
    # Dragonborn body type, sad hug
    ###########################################################################
    t.create_new_cinematic_phase_from_another(
        hug_sad_normal_node_uuid,
        hug_sad_dragonborn_node_uuid,
        skip_tl_nodes = ('TLAnimation', 'TLShot')
    )

    t.create_tl_shot('befcdee8-6352-4be6-b2ea-23c2ac0dfe60', '0.0', '21.67')

    t.create_tl_animation(
        bg3.SPEAKER_PLAYER,
        '0.0', '13.06',
        '84117bdc-71dd-47a2-9cba-039df0b1890d',
        'a2dae3f2-e3c9-4fc7-b8ac-82abf4a153b0',
        fade_in = 0.0,
        fade_out = 0.94)
    t.create_tl_animation(
        bg3.SPEAKER_SHADOWHEART,
        '0.0', '13.06',
        '57523fff-f67e-c3d5-59a4-b45a84d3eaec',
        'c8dad77b-5b76-44fe-bfeb-61d676ede3f6',
        fade_in = 0.0,
        fade_out = 0.94)
    t.create_tl_animation(
        bg3.SPEAKER_PLAYER,
        '12.12', '21.67',
        '84117bdc-71dd-47a2-9cba-039df0b1890d',
        'a2dae3f2-e3c9-4fc7-b8ac-82abf4a153b0',
        fade_in = 0.0,
        fade_out = 0.0,
        animation_play_start_offset = 6.29)
    t.create_tl_animation(
        bg3.SPEAKER_SHADOWHEART,
        '12.12', '21.67',
        '57523fff-f67e-c3d5-59a4-b45a84d3eaec',
        'c8dad77b-5b76-44fe-bfeb-61d676ede3f6',
        fade_in = 0.0,
        fade_out = 0.0,
        animation_play_start_offset = 6.29)

    t.create_tl_shot('cb95fcb5-efd7-48f4-9352-5eaeb3e44274', '21.67', phase_duration, is_snapped_to_end = True)

    t.create_tl_animation(
        bg3.SPEAKER_PLAYER,
        '21.67', phase_duration,
        '84117bdc-71dd-47a2-9cba-039df0b1890d',
        'a2dae3f2-e3c9-4fc7-b8ac-82abf4a153b0',
        fade_in = 0.0,
        fade_out = 2.0,
        animation_play_start_offset = 16.79,
        is_snapped_to_end = True)
    t.create_tl_animation(
        bg3.SPEAKER_SHADOWHEART,
        '21.67', phase_duration,
        '57523fff-f67e-c3d5-59a4-b45a84d3eaec',
        'c8dad77b-5b76-44fe-bfeb-61d676ede3f6',
        fade_in = 0.0,
        fade_out = 1.44,
        animation_play_start_offset = 16.79,
        is_snapped_to_end = True)


    ###########################################################################
    # Voice nodes
    ###########################################################################

    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '4.31',
        hug_first_reaction_node_uuid,
        ((None, '99480a46-e5ff-4101-ab73-d0ce43403c57'),),
        phase_duration = '4.5',
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0, 64, None), (1.36, 2, None)),
        }
    )

    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '2.13',
        hug_reaction_partnered_node_uuid,
        ((None, '99480a46-e5ff-4101-ab73-d0ce43403c57'),),
        phase_duration = '2.3',
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0, 2, None),),
        }
    )
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '3.3',
        hug_reaction_partnered_node_uuid,
        ((None, '99480a46-e5ff-4101-ab73-d0ce43403c57'),),
        line_index = 1,
        phase_duration = '3.4',
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0, 2, 2), (1.4, 2, None)),
        }
    )
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '4.28',
        hug_reaction_partnered_node_uuid,
        ((None, '99480a46-e5ff-4101-ab73-d0ce43403c57'),),
        line_index = 2,
        phase_duration = '4.4',
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0, 2, 1), (1.73, 2, None)),
        }
    )
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '3.12',
        hug_reaction_partnered_node_uuid,
        ((None, '99480a46-e5ff-4101-ab73-d0ce43403c57'),),
        line_index = 3,
        phase_duration = '3.3',
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0, 2, None), (0.93, 2, 2)),
        }
    )

    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '2.51',
        hug_reaction_node_uuid,
        ((None, '99480a46-e5ff-4101-ab73-d0ce43403c57'),),
        phase_duration = '2.6',
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0, 1, None), (1.03, 2, None)),
        }
    )
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '1.83',
        hug_reaction_node_uuid,
        ((None, '99480a46-e5ff-4101-ab73-d0ce43403c57'),),
        line_index = 1,
        phase_duration = '1.9',
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0, 2, None), (0.46, 2, 2)),
        }
    )
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '5.466',
        hug_reaction_node_uuid,
        ((None, '99480a46-e5ff-4101-ab73-d0ce43403c57'),),
        line_index = 2,
        phase_duration = '5.5',
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0, 1, None), (0.77, 1, 1), (1.36, 2, 2), (4.36, 2, None)),
        }
    )


bg3.add_build_procedure('add_hugs_to_the_story', add_hugs_to_the_story)
bg3.add_build_procedure('create_hugs_dialogs', create_hugs_dialogs)
bg3.add_build_procedure('create_hugs_timeline', create_hugs_timeline)

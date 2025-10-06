from __future__ import annotations

import bg3moddinglib as bg3

from .context import game_assets
from .flags import *

def patch_gale_recruitment() -> None:
    ab = game_assets.get_modded_dialog_asset_bundle('Gale_Recruitment2')
    d = bg3.dialog_object(ab.dialog)
    t = bg3.timeline_object(ab.timeline, d)

    speaker_idx_shadowheart = d.get_speaker_slot_index(bg3.SPEAKER_SHADOWHEART)

    gale_recruited_node_uuid = '38d40fe6-ed40-7b80-5ee4-b65c462cc27c' # existing node
    gale_recruited2_node_uuid = '8fcfb807-0286-ca58-c39a-06fa6724517f'

    you_keep_some_interesting_company_node_uuid = 'f0ac7b82-7119-4dec-9f4d-34db50874a33'
    woman_with_shadows_for_eyes_node_uuid = '50485d42-8d88-45d5-9efa-fcc95ec290cd'
    well_see_node_uuid = '7ce49244-3277-487d-8149-faa90d51e726'
    end_node_uuid = '8b51f075-b5b0-48c3-81a9-eececfae3e3c'

    d.remove_dialog_attribute(gale_recruited_node_uuid, 'endnode')
    d.add_child_dialog_node(gale_recruited_node_uuid, you_keep_some_interesting_company_node_uuid)
    d.add_child_dialog_node(gale_recruited_node_uuid, end_node_uuid)

    d.remove_dialog_attribute(gale_recruited2_node_uuid, 'endnode')
    d.add_child_dialog_node(gale_recruited2_node_uuid, you_keep_some_interesting_company_node_uuid)
    d.add_child_dialog_node(gale_recruited2_node_uuid, end_node_uuid)

    # 2df91020-9884-2eeb-b724-9fc343b58f8a -> Tav
    # 1cca824c-367d-f7a2-fce3-aadd0a561fe4 -> Gale
    # a2b32cfb-c457-9605-a9c5-e60a5475640b -> Shadowheart

    gale_camera1_uuid = '860d844d-908e-4613-8b6f-222d9cf415e6'
    gale_camera2_uuid = 'e89c083d-705d-407e-9ce4-838ad7abbc65'
    shadowheart_camera_uuid = 'a5b4d2f3-acfd-4f02-9f39-4375ee1502ad'

    # Besides, looks like you keep some interesting company.
    d.create_standard_dialog_node(
        you_keep_some_interesting_company_node_uuid,
        bg3.SPEAKER_GALE,
        [woman_with_shadows_for_eyes_node_uuid],
        bg3.text_content('h3d86f328g1291g4680ga4f7g06c919eb06c2', 1),
        checkflags = (
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_REALLY_SHADOWHEART, True, speaker_idx_shadowheart),
                bg3.flag(bg3.TAG_AVATAR, False, speaker_idx_shadowheart),
            )),
            bg3.flag_group('Global', (
                bg3.flag(ReallyShadowheart_Ext_V2_0_0_0.uuid, True, None),
            )),
        ))
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_GALE,
        '4.17',
        you_keep_some_interesting_company_node_uuid,
        ((None, gale_camera1_uuid),),
        phase_duration = '4.4',
        emotions = {
            bg3.SPEAKER_GALE: ((0.0, 4, None), (1.92, 2, 1),)
        })

    # A woman with shadows for eyes - deep as the Darklake. A pleasure, madam.
    d.create_standard_dialog_node(
        woman_with_shadows_for_eyes_node_uuid,
        bg3.SPEAKER_GALE,
        [well_see_node_uuid],
        bg3.text_content('hb40e2ddag4ab3g47c7g9861g22850b737c56', 1),
        setflags = (
            bg3.flag_group('Global', (
                bg3.flag(Gale_Gave_Compliment_Shadowheart.uuid, True, None),
            )),
        ))
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_GALE,
        '6.99',
        woman_with_shadows_for_eyes_node_uuid,
        ((None, gale_camera2_uuid),),
        phase_duration = '7.2',
        emotions = {
            bg3.SPEAKER_GALE: ((0.0, 4, None), (2.03, 4, 1), (5.04, 256, None), (6.4, 2, None))
        })

    # Is it indeed? We'll see.
    d.create_standard_dialog_node(
        well_see_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [],
        bg3.text_content('h5225b8bfgdda9g4140g8659g0857f29cf2ef', 1),
        end_node = True)
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        '2.41',
        well_see_node_uuid,
        (),
        phase_duration = '2.8',
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 8, None), (1.29, 16, None))
        },
        attitudes = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, bg3.ATTITUDE_DIAG_Pose_Crossed_01, bg3.ATTITUDE_DIAG_T_Pose, None),),
        })
    t.create_tl_shot(
        None,
        '0.0',
        '2.8',
        is_snapped_to_end = True,
        j_cut_length = 1.0,
        is_logic_enabled = True,
        companion_cameras = ('81b6ede6-3f4b-4caf-910b-3dd142f0b98b', '26949517-f0f4-4689-ae37-b94fe68dfee9', 'd3e056d9-f660-4ab7-b766-6aaff02b7c78')
    )

    d.create_standard_dialog_node(
        end_node_uuid,
        bg3.SPEAKER_GALE,
        [],
        None,
        end_node = True)


bg3.add_build_procedure('patch_gale_recruitment', patch_gale_recruitment)
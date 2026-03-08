from __future__ import annotations

import bg3moddinglib as bg3

from .context import get_context
from .dialog_overrides import add_dialog_dependency, get_dialog_uuid
from .flags import *


#tav_position = ('-2.0', '0', '0.38200456')
tav_position = ('-2.0', '0', '-3.12')

peanut_positions = (
    ('-1.0', '-0.2956394', '-1.0'),
    ('-2.0', '-0.2956394', '-1.0'),
    ('-3.0', '-0.2956394', '-1.0'),
)

peanut_rotations = (
    bg3.euler_to_quaternion(0, 0, 0, sequence='yxz'),
    bg3.euler_to_quaternion(0, 0, 0, sequence='yxz'),
    bg3.euler_to_quaternion(0, 0, 0, sequence='yxz'),
)

dx = bg3.decimal_from(0)
dy = bg3.decimal_from(0)
dz = bg3.decimal_from(0)

def patch_scene(ab: bg3.dialog_asset_bundle) -> None:
    global dx, dy, dz

    s = bg3.scene_object(ab.scene_lsf, ab.scene_lsx)

    # Inherited scene
    inherited_scenes = s.lsf_xml.findall('./region[@id="TLScene"]/node[@id="TLScene"]/children/node[@id="TLInheritedScenes"]/children/node[@id="TLScene"]')
    for inherited_scene in inherited_scenes:
        if bg3.get_bg3_attribute(inherited_scene, 'Object') == 'Public/Shared/Timeline/Scenes/Default/bnz_standing_Px1_EALaunch.lsx':
            bg3.set_bg3_attribute(inherited_scene, 'Object', 'Public/Shared/Timeline/Scenes/Default/bnz_standing_Px2_Shipping.lsx')

    if s.lsx_xml:
        inherited_scenes = s.lsx_xml.findall('./region[@id="TLScene"]/node[@id="root"]/children/node[@id="TLInheritedScenes"]/children/node[@id="TLScene"]')
        for inherited_scene in inherited_scenes:
            if bg3.get_bg3_attribute(inherited_scene, 'Object') == 'Public/Shared/Timeline/Scenes/Default/bnz_standing_Px1_EALaunch.lsx':
                bg3.set_bg3_attribute(inherited_scene, 'Object', 'Public/Shared/Timeline/Scenes/Default/bnz_standing_Px2_Shipping.lsx')

    # Update positions of actors
    x, y, z = s.get_actor_position(1)
    dx = bg3.decimal_from_str(tav_position[0]) - bg3.decimal_from_str(x)
    dy = bg3.decimal_from(0)
    dz = bg3.decimal_from_str(tav_position[2]) - bg3.decimal_from_str(z)

    n = 0
    for i in range(1, 6):
        # 4 is peanut
        if s.get_actor_type(i) == 4:
            s.set_actor_position(i, peanut_positions[n])
            s.set_actor_rotation(i, peanut_rotations[n])
            n += 1
        else:
            x, y, z = s.get_actor_position(i)
            x = bg3.decimal_to_str(bg3.decimal_from_str(x) + dx)
            y = bg3.decimal_to_str(bg3.decimal_from_str(y) + dy)
            z = bg3.decimal_to_str(bg3.decimal_from_str(z) + dz)
            s.set_actor_position(i, (x, y, z))

    # Update rotation of the 2nd peanut
    s.set_actor_rotation(3, bg3.euler_to_quaternion(-10, 0, 0, sequence='yxz'))

    # Update positions of cameras
    number_of_cameras = s.get_number_of_cameras()
    for i in range(0, number_of_cameras):
        if not s.is_attached_camera(i):
            x, y, Z = s.get_camera_position(i)
            x = bg3.decimal_to_str(bg3.decimal_from_str(x) + dx)
            y = bg3.decimal_to_str(bg3.decimal_from_str(y) + dy)
            z = bg3.decimal_to_str(bg3.decimal_from_str(z) + dz)
            s.set_camera_position(i, (x, y, z))

    # Fix lighting
    s.set_light_radius('d3ff4672-e030-463f-b021-3b33b2b046a8', 15.0)
    s.set_light_radius('da58d5f1-361b-44a3-aea8-01fb1555b773', 15.0)
    s.set_light_radius('3c3f7348-ed3d-4832-a648-72b566832495', 15.0)

    s.set_light_position('d3ff4672-e030-463f-b021-3b33b2b046a8', ('-3.0', '0.3', '-0.5'))
    s.set_light_position('da58d5f1-361b-44a3-aea8-01fb1555b773', ('-3.6', '0.8', '1.0'))
    s.set_light_position('3c3f7348-ed3d-4832-a648-72b566832495', ('-3.5', '-0.55', '-0.75'))


def patch_timeline(ab: bg3.dialog_asset_bundle) -> None:
    global dx, dy, dz

    d = bg3.dialog_object(ab.dialog)
    t = bg3.timeline_object(ab.timeline, d)

    # 9974e28d-4f08-42cc-af1b-a97cf237dc52 Shadowheart -> Shadowheart
    # 607c7d71-f1da-4780-a74b-d2564677b8d4 Shadowheart -> Shadowheart
    # 34b01a33-dc71-46a0-a581-6cea0c216755 Shadowheart -> Shadowheart
    # 70ebd7c1-ef6d-4578-942c-3fff7954128d Shadowheart -> Shadowheart
    # 7c2f7fc4-66d5-4690-8d6d-82427fe7cb6f Shadowheart -> Shadowheart

    # 123339bd-8058-4cce-8684-3f51ef48dd29 Shadowheart -> Tav

    # 0e92d3ba-ce39-4897-8a6b-ff5415201460 Tav         -> Shadowheart

    # 61331828-9730-4785-bf86-b52061dc3b96 Tav         -> Tav
    # 2d658af1-e616-4c2f-ad06-490016d022a2 Tav         -> Tav

    # e6a8d805-9f52-4be6-8456-ecbfb7547590 Laezel      -> Laezel
    # 1b0fd75e-95af-46bf-a836-598b752b1dc1 Laezel      -> Laezel
    # 4686528e-3383-463d-a87c-65d60e7b26cc Laezel      -> Laezel

    # 898d01a8-c33d-4de4-9800-ce97c68314f4 Gale        -> Gale
    # 92966b26-c467-4297-98f5-d3b743ec4e59 Gale        -> Gale

    # cb0e6f06-2367-4cc4-9b18-e52bf37fb62c Wyll        -> Wyll

    # f5a613dd-75c0-49de-ac1c-2163f30a23c2 Astarion    -> Astarion

    characters_and_cameras = frozenset(t.get_timeline_actors(('character', 'scenecam')).keys())
    for effect_comp in t.all_effect_components:
        if bg3.get_bg3_attribute(effect_comp, 'Type') == 'TLTransform':
            actor_uuid = t.get_tl_node_actor_uuid(effect_comp)
            if actor_uuid is not None and actor_uuid in characters_and_cameras:
                idx = 0
                while True:
                    n = 0
                    x = t.get_tl_transform_coordinate(effect_comp, 0, idx)
                    if x:
                        x = bg3.decimal_to_str(bg3.decimal_from_str(x) + dx)
                        t.set_tl_transform_coordinate(effect_comp, 0, x, idx)
                        n += 1
                    y = t.get_tl_transform_coordinate(effect_comp, 1, idx)
                    if y:
                        y = bg3.decimal_to_str(bg3.decimal_from_str(y) + dy)
                        t.set_tl_transform_coordinate(effect_comp, 1, y, idx)
                        n += 1
                    z = t.get_tl_transform_coordinate(effect_comp, 2, idx)
                    if z:
                        z = bg3.decimal_to_str(bg3.decimal_from_str(z) + dz)
                        t.set_tl_transform_coordinate(effect_comp, 2, z, idx)
                        n += 1
                    if n == 0:
                        break
                    idx += 1
        if bg3.get_bg3_attribute(effect_comp, 'Type') == 'TLAnimation':
            x, y, z = t.get_tl_animation_target_transform_position(effect_comp)
            if x != '' and y != '' and z != '':
                x = bg3.decimal_to_str(bg3.decimal_from_str(x) + dx)
                y = bg3.decimal_to_str(bg3.decimal_from_str(y) + dy)
                z = bg3.decimal_to_str(bg3.decimal_from_str(z) + dz)
                t.set_tl_animation_target_transform_position(effect_comp, (x, y, z))

    # Put the camera higher
    # Dialog node 6884141c-7fa5-e4be-c9b8-385add4d5320 phase 1
    # You're here. Just like it told me. And with a gith - I should have figured.
    t.set_tl_transform_coordinate('969808fa-332f-4a91-a3ae-4f54f71e70ea', 1, '1.1', 0)
    t.set_tl_transform_coordinate('969808fa-332f-4a91-a3ae-4f54f71e70ea', 1, '1.5', 1)

    t.set_tl_transform_coordinate('6e725468-c067-4cd6-80ad-e7fbf7384413', 1, '1.1', 0)
    t.set_tl_transform_coordinate('6e725468-c067-4cd6-80ad-e7fbf7384413', 1, '1.5', 1)

    t.set_tl_transform_coordinate('352413cb-2d0f-4afc-8283-fdd7581395f5', 1, '1.1', 0)
    t.set_tl_transform_coordinate('352413cb-2d0f-4afc-8283-fdd7581395f5', 1, '1.5', 1)

    t.set_tl_transform_coordinate('b6ef8c7c-3298-40c7-bf6e-711973442b1e', 1, '1.1', 0)
    t.set_tl_transform_coordinate('b6ef8c7c-3298-40c7-bf6e-711973442b1e', 1, '1.5', 1)

    tl_phase = t.use_existing_phase(1)
    t.edit_tl_transform('b74b1d5b-ccbf-4d28-b66a-12c6026e1d53', start = '7.0', end = tl_phase.duration, channels = (
        (
            t.create_value_key(time = '7.0', value = '-1.999997', value_type = 'float', interpolation_type = 0),
        ),
        (
            t.create_value_key(time = '7.0', value = '-0.2956394', value_type = 'float', interpolation_type = 0),
        ),
        (
            t.create_value_key(time = '7.0', value = '-3.1199996', value_type = 'float', interpolation_type = 0),
        ),
        (
            t.create_value_key(time = '7.0', value = (0.0, -0.12864251, 0, 0.99169105), value_type = 'fvec4', interpolation_type = 0),
        ),
        (
            t.create_value_key(time = '7.0', value = '1', value_type = 'float', interpolation_type = 3),
        ),
        (),
    ))

    # Fix the glitch in "You're here. Just like it told me. And with a gith - I should have figured."
    t.use_existing_phase(1)
    t.edit_tl_shot('8a76d5dc-44ce-41ab-876d-0b036de7f6da', end = '5.090001')
    t.create_tl_shot('0e92d3ba-ce39-4897-8a6b-ff5415201460', '5.090001', '7.0')

    # Fix the glitch in "It took me so long to find you."
    # Dialog node ec6dead7-24f4-b79e-4540-d079512238a7
    t.use_existing_phase(22)
    t.edit_tl_shot('7d7996a5-b4e0-4aa6-bf8f-c9429acaa1f0', end = '1.45')
    t.edit_tl_shot('772c7f46-a80a-49b3-827c-bc5b8f4ccfef', start = '1.45', camera_uuid = '61331828-9730-4785-bf86-b52061dc3b96')

    """
    unset ORI_ShadowHeart_HasMet_d06842a4-248e-7f83-da87-4eec7606178e
    Osi.PROC_GlobalClearFlagAndCache("d06842a4-248e-7f83-da87-4eec7606178e")

    unset ORI_Laezel_State_IsInParty_3ee6b1f2-24f4-4e85-b7dc-49060e6d2699
    Osi.PROC_GlobalClearFlagAndCache("3ee6b1f2-24f4-4e85-b7dc-49060e6d2699")

    Factions:
    Origin_ShadowHeart_901cd370-86ff-b538-e1e8-574c84135ca0
    Origin_ShadowHeart_Hostile_68d5b0df-a555-4486-9bf3-391e8f5227d0
    Neutral_NPC_cfb709b3-220f-9682-bcfb-6f0d8837462e

    Speaker 2: Lae'zel
    81b1889a-5263-6679-f6bf-b1ae03788965
    phases: 6 24
    1b0fd75e-95af-46bf-a836-598b752b1dc1 [81b6ede6-3f4b-4caf-910b-3dd142f0b98b]
    1b0fd75e-95af-46bf-a836-598b752b1dc1 [81b6ede6-3f4b-4caf-910b-3dd142f0b98b]

    Speaker 3: Wyll
    d2459f04-0433-9b92-f6f5-8f5990a796e1
    phases: 18 43
    cb0e6f06-2367-4cc4-9b18-e52bf37fb62c [d3e056d9-f660-4ab7-b766-6aaff02b7c78]
    cb0e6f06-2367-4cc4-9b18-e52bf37fb62c [d3e056d9-f660-4ab7-b766-6aaff02b7c78]

    Speaker 4: Astarion
    e2d0f8a7-1867-8421-3dd7-f0a2094563d0
    phases: 16 17
    cb0e6f06-2367-4cc4-9b18-e52bf37fb62c -> f5a613dd-75c0-49de-ac1c-2163f30a23c2 [6cba0c54-c48a-4796-b91e-f722c4f595c5]
    f5a613dd-75c0-49de-ac1c-2163f30a23c2 [6cba0c54-c48a-4796-b91e-f722c4f595c5]

    Speaker 5: Gale
    52211027-8502-5b6f-1dc1-995a3f51ba25
    phases: 34 12
    898d01a8-c33d-4de4-9800-ce97c68314f4 [d3e056d9-f660-4ab7-b766-6aaff02b7c78]
    92966b26-c467-4297-98f5-d3b743ec4e59 [d3e056d9-f660-4ab7-b766-6aaff02b7c78]

    
    S_GLO_Cazador_2f1880e6-1297-4ca3-a79c-9fabc7f179d3
    S_Dummy_Monitor_HumanForm_003_66e722c8-ecc5-40f3-b6a9-587b8f683451

    Osi.TeleportTo(Osi.GetHostCharacter(), "66e722c8-ecc5-40f3-b6a9-587b8f683451")
    """

    # 0e92d3ba-ce39-4897-8a6b-ff5415201460 Tav -> SH
    # 61331828-9730-4785-bf86-b52061dc3b96 Tav -> Tav
    # 2d658af1-e616-4c2f-ad06-490016d022a2 Tav -> Tav
    # 123339bd-8058-4cce-8684-3f51ef48dd29 SH  -> Tav
    # 34b01a33-dc71-46a0-a581-6cea0c216755 SH  -> SH
    # 70ebd7c1-ef6d-4578-942c-3fff7954128d SH  -> SH
    # 7c2f7fc4-66d5-4690-8d6d-82427fe7cb6f SH  -> SH
    # 607c7d71-f1da-4780-a74b-d2564677b8d4 SH  -> SH
    # 9974e28d-4f08-42cc-af1b-a97cf237dc52 SH  -> SH

    # Fix position of a knife
    t.set_tl_transform_coordinate('87a6965a-2006-4ef3-a068-50ba3d6a29f1', 2, '0.042')
    t.set_tl_transform_coordinate('b0b93176-b27d-44aa-93e9-3ad222d5952d', 2, '0.042')
    t.set_tl_transform_coordinate('b8961b30-e9d1-492e-8f72-9ac4c4b6e63d', 2, '0.042')
    t.set_tl_transform_coordinate('a42f7a99-26f6-4e71-bb89-2343db14fc2b', 2, '0.042')
    t.set_tl_transform_coordinate('77636aea-f1a4-4da8-b58d-165376c34f67', 2, '0.042')

    # Use full scale knife
    t.set_tl_transform_coordinate('91927b29-3d6e-4612-b673-6b607c757ed5', 4, '1.0')
    t.set_tl_transform_coordinate('8267d425-c4da-45fb-8887-41f08ebd37a8', 4, '1.0')
    t.set_tl_transform_coordinate('d1773a80-f76f-45a0-beba-9ad24975d27f', 4, '1.0')
    t.set_tl_transform_coordinate('bbf4b169-ddea-4fa1-a2cb-7ebea4aefdaf', 4, '1.0')
    t.set_tl_transform_coordinate('1743ce35-66db-48d6-96d9-320c8d7fdc74', 4, '1.0')

    t.set_tl_transform_coordinate('1743ce35-66db-48d6-96d9-320c8d7fdc74', 2, '0.2')

    # "I can't see anything else! I can't shake it."
    # Dialog node 978b13e5-750a-4437-d6b4-be0e78409176 phase 27
    t.edit_tl_shot('51238366-aa6c-4636-a9f2-64469e04dc7a', camera_uuid = '61331828-9730-4785-bf86-b52061dc3b96')
    t.remove_effect_component('1571eb18-9bad-4692-895a-1d9c411f6450') # TLTransform Tav
    t.remove_effect_component('45d82127-83a0-485e-8001-16710b6ed06d') # TLTransform Shadowheart
    t.remove_effect_component('1bbb3db7-22e3-40a7-8813-9497ded69f67') # TLTransform Tav

    #shadowheart_with_knife_pos = ('-2.157477', '-0.2562875', '-2.23896184')
    shadowheart_with_knife_pos = ('-2.157477', '-0.2562875', '-5.73896184')
    shadowheart_with_knife_rot = bg3.euler_to_quaternion(-130.0, 0.0, 0.0, sequence='yxz')

    # Enable narrator phrase: "*Your mind rushes into hers - a storm of desperation, confusion and a will other than her own.*"
    # Dialog node 40c0f227-8df9-aa3c-b50e-26bc45214bb4 phase 36
    d.set_dialog_flags('40c0f227-8df9-aa3c-b50e-26bc45214bb4', checkflags = ())
    t.use_existing_phase(36)

    t.remove_effect_component('b88c4685-aed3-4baa-8bc1-4969b84599d7') # old TLPlayEffectEvent
    t.remove_effect_component('a7258c6e-a76f-4bb9-807e-539dad5bc9aa') # old TLPlayEffectEvent

    # new effect nodes
    t.create_tl_actor_node(bg3.timeline_object.PLAY_EFFECT, '6db1b0fc-33e8-4c4c-9d0e-878c252d0152', '0.0', '10.0', (
        t.create_value_key(time = '0.0', interpolation_type = 3),
    ))
    t.create_tl_actor_node(bg3.timeline_object.PLAY_EFFECT_PHASE, '6db1b0fc-33e8-4c4c-9d0e-878c252d0152', '0.0', '10.0', (
        t.create_value_key(time = '0.0', interpolation_type = 3),
        t.create_value_key(time = '8.87', interpolation_type = 3, value_name = 'EffectPhase', value_type = 'int32', value = '2'),
    ))
    t.create_tl_actor_node(bg3.timeline_object.PLAY_EFFECT, '5185aa3e-26d3-458c-9b92-63591228c78f', '0.0', '10.0', (
        t.create_value_key(time = '0.0', interpolation_type = 3, value_name = 'PlayEffect', value_type = 'bool', value = 'False'),
        t.create_value_key(time = '2.66', interpolation_type = 3),
        t.create_value_key(time = '8.87', interpolation_type = 3, value_name = 'PlayEffect', value_type = 'bool', value = 'False'),
    ))
    t.create_tl_actor_node(bg3.timeline_object.PLAY_EFFECT_PHASE, '5185aa3e-26d3-458c-9b92-63591228c78f', '0.0', '10.0', (
        t.create_value_key(time = '2.66', interpolation_type = 3),
    ))
    # remove unnecessary animation (Shadowheart mindmeld)
    t.remove_effect_component('6a87b755-6a54-49b1-ba90-2c8d85009ebd')
    # remove attitude node
    t.remove_effect_component('133c8e18-c892-49b2-ae8d-6abc51b57931')
    t.create_tl_actor_node(bg3.timeline_object.ATTITUDE, bg3.SPEAKER_SHADOWHEART, '0.0', '10.0', (
        t.create_attitude_key('4.5', bg3.ATTITUDE_DIAG_Pose_Confused_L_01, bg3.ATTITUDE_DIAG_T_Pose),
        t.create_attitude_key('8.5', bg3.ATTITUDE_DIAG_Pose_Stand_L_Forward_01, bg3.ATTITUDE_DIAG_T_Pose),
    ))

    # "The whispering won't let me sleep. It keeps pushing me - to you."
    # Dialog node 7dcc819f-ebf3-7c4a-9369-759f35d2e477 phase 42
    t.use_existing_phase(42)
    t.edit_tl_node_set_keys(
        '60f29cbe-972c-4430-8b1e-c01c0c171c85',
        (
            t.create_attitude_key('0.0', bg3.ATTITUDE_DIAG_Pose_Confused_L_01, bg3.ATTITUDE_DIAG_T_Pose),
            t.create_attitude_key('5.7', bg3.ATTITUDE_DIAG_Pose_Hips_01, bg3.ATTITUDE_DIAG_T_Pose),
        ))
    t.create_tl_shot('123339bd-8058-4cce-8684-3f51ef48dd29', '0.0', '1.0')
    t.edit_tl_shot('802ac92b-318d-46da-95c2-806e9f5fe9d4', start = '1.0')

    # "The whispering's already quieter here. Once you're dead, it'll be gone entirely."
    # Dialog node d9402272-206a-276b-82b8-9cd976ea8286 phase 19
    t.edit_tl_shot('4536bdec-c52a-4a9c-90ad-8b337e72c928', camera_uuid = '9974e28d-4f08-42cc-af1b-a97cf237dc52')
    t.set_tl_animation_target_transform('ea86999e-e9a1-412d-8e6a-6a90e5b63abb', shadowheart_with_knife_pos, shadowheart_with_knife_rot, '1.0')

    # "No. Enough talk. Enough voices."
    # Dialog node 8b752880-555b-6025-8e0b-255156950127 phase 51
    t.edit_tl_shot('a34c3a6d-f1c1-44ff-9dd4-5a9574545fca', camera_uuid = '9974e28d-4f08-42cc-af1b-a97cf237dc52')
    t.set_tl_animation_target_transform('7e07c784-9144-49ce-ba67-b8bb30e4e00b', shadowheart_with_knife_pos, shadowheart_with_knife_rot, '1.0')
    #t.remove_effect_component('7e07c784-9144-49ce-ba67-b8bb30e4e00b')

    # "You can certainly try."
    # Dialog node c3355207-564d-8721-bd44-e60d43a9e178 phase 54
    t.edit_tl_shot('159871e8-a70b-468d-87cb-2f12beecbfab', camera_uuid = '607c7d71-f1da-4780-a74b-d2564677b8d4')
    t.set_tl_animation_target_transform('e47f1e91-6a5d-439c-92ec-a0d5495820ee', shadowheart_with_knife_pos, shadowheart_with_knife_rot, '1.0')
    #t.remove_effect_component('e47f1e91-6a5d-439c-92ec-a0d5495820ee')


    # Cinematic node, phase 5
    t.set_tl_animation_target_transform('9bf5548e-8835-4ff4-886f-27d8448133c8', shadowheart_with_knife_pos, shadowheart_with_knife_rot, '1.0')

    # "I'm tired of being pushed."
    # Dialog node a0616acb-c73c-c54f-b38b-22d08c647592 phase 9
    t.remove_effect_component('08139a04-98f4-4433-a2f7-91e449ab1727')
    t.remove_effect_component('46d9f859-d585-4ce8-8e74-cbe3737486aa')
    t.remove_effect_component('ab3c3880-a2d0-423b-84c9-9273765f7307')
    t.set_tl_animation_target_transform('17748f5a-5f1d-4df5-b84b-1d87965933f4', shadowheart_with_knife_pos, shadowheart_with_knife_rot, '1.0')
    #t.set_tl_animation_target_transform('ab3c3880-a2d0-423b-84c9-9273765f7307', shadowheart_with_knife_pos, shadowheart_with_knife_rot, '1.0')
    t.use_existing_phase(9)
    #t.edit_tl_node('17748f5a-5f1d-4df5-b84b-1d87965933f4', end = '12.98')
    t.edit_tl_shot('1ff25b8d-2881-4ca7-880a-9de6dc054d9f', end = '6.21001')
    t.create_tl_transform(bg3.SPEAKER_SHADOWHEART, '0.0', '2.27', (
        (
            t.create_value_key(time = '0.0', value = shadowheart_with_knife_pos[0], value_type = 'float'),
        ),
        (
            t.create_value_key(time = '0.0', value = shadowheart_with_knife_pos[1], value_type = 'float'),
        ),
        (
            t.create_value_key(time = '0.0', value = shadowheart_with_knife_pos[2], value_type = 'float'),
        ),
        (
            t.create_value_key(time = '0.0', value = bg3.euler_to_quaternion(-178.0, 0.0, 0.0, sequence='yxz')),
        ),
        (),
        (),
    ))
    t.create_tl_transform(bg3.SPEAKER_SHADOWHEART, '2.27', '12.98', (
        (
            t.create_value_key(time = '0.0', value = shadowheart_with_knife_pos[0], value_type = 'float'),
        ),
        (
            t.create_value_key(time = '0.0', value = shadowheart_with_knife_pos[1], value_type = 'float'),
        ),
        (
            t.create_value_key(time = '0.0', value = shadowheart_with_knife_pos[2], value_type = 'float'),
        ),
        (
            t.create_value_key(time = '0.0', value = shadowheart_with_knife_rot),
        ),
        (),
        (),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.LOOK_AT, bg3.SPEAKER_SHADOWHEART, '0.0', '12.98', (
        t.create_look_at_key(
            '0.0',
            target = bg3.SPEAKER_PLAYER,
            bone = 'Head_M',
            turn_mode = 3,
            weight = 0,
            safe_zone_angle = 80,
            head_safe_zone_angle = 80,
            look_at_mode = 1
        ),
    ), is_snapped_to_end = True)

    # "Don't look at me like that. I can't... no."
    # Dialog node 0193b5e2-dc64-c062-bd26-348cdd041c32 phase 4
    t.remove_effect_component('0ca20063-4ab4-470e-87ca-086971ff85f1') # Tav TLAnimation
    t.remove_effect_component('e3418375-d5d7-4fc8-9ad4-2aeaf900fc86') # Tav TLAttitudeEvent
    t.set_tl_animation_target_transform('0b72e80f-ba6b-4377-9582-f69784aa245d', shadowheart_with_knife_pos, shadowheart_with_knife_rot, '1.0')
    t.use_existing_phase(4)
    t.edit_tl_shot('1b6e2d18-a260-4044-adae-73efe6b35d7e', camera_uuid = '9974e28d-4f08-42cc-af1b-a97cf237dc52')
    t.create_tl_transform(bg3.SPEAKER_SHADOWHEART, '0.0', '7.95', (
        (
            t.create_value_key(time = '0.0', value = shadowheart_with_knife_pos[0], value_type = 'float'),
        ),
        (
            t.create_value_key(time = '0.0', value = shadowheart_with_knife_pos[1], value_type = 'float'),
        ),
        (
            t.create_value_key(time = '0.0', value = shadowheart_with_knife_pos[2], value_type = 'float'),
        ),
        (
            t.create_value_key(time = '0.0', value = shadowheart_with_knife_rot),
        ),
        (),
        (),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.ATTITUDE, bg3.SPEAKER_PLAYER, '0.0', '7.95', (
        t.create_attitude_key('0', bg3.ATTITUDE_DIAG_Pose_Crossed_01, bg3.ATTITUDE_DIAG_T_Pose),
    ))

    # Mindmeld success after perception check failure
    # "*A strange miasma clings to her thoughts. Not the tadpole, but your interruption fazes her.*"
    # Dialog node 1205165d-bddd-8ae6-6944-657acd7e2a30 phase 30
    t.use_existing_phase(30)
    t.create_tl_transform(bg3.SPEAKER_SHADOWHEART, '0.0', '8.28999', (
        (
            t.create_value_key(time = '0.0', value = shadowheart_with_knife_pos[0], value_type = 'float'),
        ),
        (
            t.create_value_key(time = '0.0', value = shadowheart_with_knife_pos[1], value_type = 'float'),
        ),
        (
            t.create_value_key(time = '0.0', value = shadowheart_with_knife_pos[2], value_type = 'float'),
        ),
        (
            t.create_value_key(time = '0.0', value = shadowheart_with_knife_rot),
        ),
        (),
        (),
    ), is_snapped_to_end = True)
    t.set_tl_animation_target_transform('ba477fd0-4ae8-45d8-ae11-441a2c957f9e', shadowheart_with_knife_pos, shadowheart_with_knife_rot, '1.0')


    # "Say what you have to say."
    # Dialog node 4358bfae-62df-b2c2-b18c-5deade473733 phase 39
    t.use_existing_phase(39)
    t.remove_effect_component('38894a77-6cc4-429e-8261-d9aff2ac0e9d')
    t.create_tl_transform(bg3.SPEAKER_SHADOWHEART, '0.0', '4.36998', (
        (
            t.create_value_key(time = '0.0', value = shadowheart_with_knife_pos[0], value_type = 'float'),
        ),
        (
            t.create_value_key(time = '0.0', value = shadowheart_with_knife_pos[1], value_type = 'float'),
        ),
        (
            t.create_value_key(time = '0.0', value = shadowheart_with_knife_pos[2], value_type = 'float'),
        ),
        (
            t.create_value_key(time = '0.0', value = bg3.euler_to_quaternion(-178.0, 0.0, 0.0, sequence = 'yxz')),
        ),
        (),
        (),
    ), is_snapped_to_end = True)
    t.edit_tl_node('cf7c0294-7094-4033-991e-96c2a913b65a', fade_in = '0.0')
    # Adjust the knife
    t.set_tl_transform_coordinate('08fbf92b-f705-492b-beba-94c39f9b8bf5', 2, '0.0')
    t.set_tl_transform_coordinate('08fbf92b-f705-492b-beba-94c39f9b8bf5', 4, '1.0')
    t.edit_tl_shot('c863ad49-4c29-4696-96eb-62e82f9cd420', end = '4.0')
    t.edit_tl_shot('9f0b1bd1-73d5-4f61-b1da-7839c25037b1', start = '4.0', camera_uuid = '61331828-9730-4785-bf86-b52061dc3b96')


    # "Maybe you're right. But the whispers won't stop."
    # Dialog node b31ba055-d1d6-74cb-202d-5e062fc44ea9 phase 14
    t.use_existing_phase(14)
    t.edit_tl_shot('9ecfbcd4-48d0-45ca-93c3-984d798b670d', start = '0.0', end = '3.690006', camera_uuid = '7c2f7fc4-66d5-4690-8d6d-82427fe7cb6f')


    # "No. I'm where I need to be."
    # Dialog node ddd10661-91e3-5461-3154-d696006cae35 phase 20
    t.remove_effect_component('ff85da23-644e-4090-a100-29a74b0aedbe')
    t.set_tl_animation_target_transform('43478099-4cd2-4b33-a135-b2c52fdfa3af', shadowheart_with_knife_pos, shadowheart_with_knife_rot, '1.0')

    # "I don't want explanations. I want sleep."
    # Dialog node e78a9946-10f1-8e44-890a-de2bfe1984fe phase 21
    t.set_tl_animation_target_transform('a982b03d-18af-43b5-9bce-39ed9dd69889', shadowheart_with_knife_pos, shadowheart_with_knife_rot, '1.0')

    # "What else do I do? My head is splitting open. I can't leave. I can't!"
    # Dialog node 9ac39ae6-dd63-7df1-2b70-8a974c4413a4 phase 25
    t.remove_effect_component('d5a1677e-a367-478c-b06e-39f82d3d1beb')

    # Cinematic node 26895b44-ba48-6aad-475b-3182604e1429 phase 32
    t.remove_effect_component('984d1354-9488-4ed3-a111-145924b295a8') # TLTransform
    t.remove_effect_component('d464c40f-fada-4ff3-b079-da3529e3d248') # TLAnimation
    t.use_existing_phase(32)
    shadowheart_rotation = bg3.euler_to_quaternion(-178.0, 0.0, 0.0, sequence = 'yxz')
    t.create_tl_transform(bg3.SPEAKER_SHADOWHEART, '0.0', '5.73', (
        (
            t.create_value_key(time = '0.0', value = shadowheart_with_knife_pos[0], value_type = 'float'),
        ),
        (
            t.create_value_key(time = '0.0', value = shadowheart_with_knife_pos[1], value_type = 'float'),
        ),
        (
            t.create_value_key(time = '0.0', value = shadowheart_with_knife_pos[2], value_type = 'float'),
        ),
        (
            t.create_value_key(time = '0.0', value = shadowheart_rotation),
        ),
        (),
        (),
    ), is_snapped_to_end = True)
    t.set_tl_animation_target_transform('d8c7a7f5-ca8b-4e20-b046-baea906e8b62', shadowheart_with_knife_pos, shadowheart_rotation, '1.0')
    t.edit_tl_node('d8c7a7f5-ca8b-4e20-b046-baea906e8b62', end = '5.73')
    t.edit_tl_shot('b7f1f30a-94f6-4a36-bd4c-f23fac65c984', camera_uuid = '2d658af1-e616-4c2f-ad06-490016d022a2')
    #t.set_tl_animation_target_transform('d464c40f-fada-4ff3-b079-da3529e3d248', shadowheart_with_knife_pos, shadowheart_rotation, '1.0')


    # Cinematic node 334aabce-3b4b-d528-3b41-4f5e1b7ef7d7 phase 47
    # Shadowheart falls asleep
    t.edit_tl_node('eadeac3d-8b4e-4add-a2a6-632d04168fb3', start = '3.0')
    t.edit_tl_node('d47caa08-aa56-4628-b795-a2251073d869', start = '0.0', end = '9.62', is_snapped_to_end = True)
    t.use_existing_phase(47)
    t.create_tl_shot('607c7d71-f1da-4780-a74b-d2564677b8d4', '0.0', '3.0')


    # Astarion's first line
    # "It sounds like death would be a mercy. Let's deliver it."
    # Dialog node c20c3eb7-63e9-655a-d1e4-2f4de70907a6 phase 16
    tl_phase = t.use_existing_phase(16)
    t.edit_tl_shot('78c25499-871c-41a1-8b84-ad029bf2bd15', camera_uuid = 'f5a613dd-75c0-49de-ac1c-2163f30a23c2')
    t.create_tl_camera_fov('f5a613dd-75c0-49de-ac1c-2163f30a23c2', '0.0', tl_phase.duration, (
        t.create_value_key(time = '0.0', value_name = 'FoV', value = '30.0', value_type = 'float', interpolation_type = 0)
    ), is_snapped_to_end = True)
    tl_phase = t.use_existing_phase(17)
    t.create_tl_camera_fov('f5a613dd-75c0-49de-ac1c-2163f30a23c2', '0.0', tl_phase.duration, (
        t.create_value_key(time = '0.0', value_name = 'FoV', value = '30.0', value_type = 'float', interpolation_type = 0)
    ), is_snapped_to_end = True)


    # "Get out of my head! <i>All of you!</i>"
    # Dialog node 98b3877d-7412-ec3b-96f2-8f283883462b phase 55
    # This hides the knife.
    tl_phase = t.use_existing_phase(55)
    t.remove_effect_component('cf8a563f-3b2f-42ee-9736-80a88d0f842d')
    t.create_tl_actor_node(bg3.timeline_object.SHOW_VISUAL, '39cc08bd-02ad-45d3-a7c3-c2a5eadcb2d5', '0.0', tl_phase.duration, (
        t.create_value_key(time = '0.0', value_name = 'ShowVisual', value_type = 'bool', value = 'False', interpolation_type = 3),
    ))

    # Perception check
    # "*There is a knife hidden in her belt. Her fingers twitch towards the hilt, ready to draw the blade.*"
    bg3.set_bg3_attribute(d.find_dialog_node('98002609-eab7-6ad7-29ab-5edcc98dea24'), 'DifficultyClassID', bg3.Act1_Medium)

    for node in t.find_effect_components('TLShowVisual', actor = bg3.SPEAKER_LAEZEL):
        t.remove_effect_component(node)
    for node in t.find_effect_components('TLShowVisual', actor = bg3.SPEAKER_WYLL):
        t.remove_effect_component(node)
    for node in t.find_effect_components('TLShowVisual', actor = bg3.SPEAKER_ASTARION):
        t.remove_effect_component(node)
    for node in t.find_effect_components('TLShowVisual', actor = bg3.SPEAKER_GALE):
        t.remove_effect_component(node)
    for node in t.find_effect_components('TLShowVisual', actor = bg3.SPEAKER_KARLACH):
        t.remove_effect_component(node)

    laezel_phases = { 6, 24 }
    wyll_phases = { 18, 43 }
    astarion_phases = { 16, 17 }
    gale_phases = { 12, 34 }

    for n in range(0, t.get_number_of_phases()):
        tl_phase = t.get_timeline_phase(n)
        t.use_existing_phase(n)
        if n == 1:
            t.create_tl_actor_node(bg3.timeline_object.SHOW_VISUAL, bg3.SPEAKER_LAEZEL, '0.0', '7.0', (
                t.create_value_key(time = '0.0', value_name = 'ShowVisual', value = False, value_type = 'bool', interpolation_type = 3),
            ))
            t.create_tl_actor_node(bg3.timeline_object.SHOW_VISUAL, bg3.SPEAKER_LAEZEL, '7.0', tl_phase.duration, (
                t.create_value_key(time = '0.0', value_name = 'ShowVisual', value = True, value_type = 'bool', interpolation_type = 3),
            ), is_snapped_to_end = True)
        else:
            t.create_tl_actor_node(bg3.timeline_object.SHOW_VISUAL, bg3.SPEAKER_LAEZEL, '0.0', tl_phase.duration, (
                t.create_value_key(time = '0.0', value_name = 'ShowVisual', value = n in laezel_phases, value_type = 'bool', interpolation_type = 3),
            ), is_snapped_to_end = True)
        t.create_tl_actor_node(bg3.timeline_object.SHOW_VISUAL, bg3.SPEAKER_WYLL, '0.0', tl_phase.duration, (
            t.create_value_key(time = '0.0', value_name = 'ShowVisual', value = n in wyll_phases, value_type = 'bool', interpolation_type = 3),
        ), is_snapped_to_end = True)
        t.create_tl_actor_node(bg3.timeline_object.SHOW_VISUAL, bg3.SPEAKER_ASTARION, '0.0', tl_phase.duration, (
            t.create_value_key(time = '0.0', value_name = 'ShowVisual', value = n in astarion_phases, value_type = 'bool', interpolation_type = 3),
        ), is_snapped_to_end = True)
        t.create_tl_actor_node(bg3.timeline_object.SHOW_VISUAL, bg3.SPEAKER_GALE, '0.0', tl_phase.duration, (
            t.create_value_key(time = '0.0', value_name = 'ShowVisual', value = n in gale_phases, value_type = 'bool', interpolation_type = 3),
        ), is_snapped_to_end = True)
        t.create_tl_actor_node(bg3.timeline_object.SHOW_VISUAL, bg3.SPEAKER_KARLACH, '0.0', tl_phase.duration, (
            t.create_value_key(time = '0.0', value_name = 'ShowVisual', value = False, value_type = 'bool', interpolation_type = 3),
        ), is_snapped_to_end = True)


def fix_speakers(ab: bg3.dialog_asset_bundle) -> None:
    d = bg3.dialog_object(ab.dialog)
    speakers = d.get_speakers()
    speaker_slots = list[tuple[str, str]]()
    for speaker_uuid in speakers:
        _, actor_uuid, _ = d.get_speaker_slot(speaker_uuid)
        speaker_slots.append((speaker_uuid, actor_uuid))

    timeline_speakers = ab.timeline.xml.findall('./region[@id="TimelineContent"]/node[@id="TimelineContent"]/children/node[@id="TimelineSpeakers"]/children/node[@id="Object"]')
    for timeline_speaker in timeline_speakers:
        index = int(bg3.get_required_bg3_attribute(timeline_speaker, 'MapKey'))
        if index < 7:
            bg3.set_bg3_attribute(timeline_speaker, 'MapValue', speaker_slots[index][1], attribute_type = 'guid')

    timeline_actor_data_objects = ab.timeline.xml.findall('./region[@id="TimelineContent"]/node[@id="TimelineContent"]/children/node[@id="TimelineActorData"]/children/node[@id="TimelineActorData"]/children/node[@id="Object"]')
    for timeline_actor_data_object in timeline_actor_data_objects:
        actor_uuid = bg3.get_bg3_attribute(timeline_actor_data_object, 'MapKey')
        val = timeline_actor_data_object.find('./children/node[@id="Value"]')
        if actor_uuid and val and bg3.get_bg3_attribute(val, 'ActorTypeId') == 'character':
            speaker_index = int(bg3.get_required_bg3_attribute(val, 'Speaker'))
            if actor_uuid != speaker_slots[speaker_index][1] and speaker_index < 7:
                bg3.set_bg3_attribute(timeline_actor_data_object, 'MapKey', speaker_slots[speaker_index][1], attribute_type = 'guid')


def fix_wyll_camera(ab: bg3.dialog_asset_bundle) -> None:
    timeline_root = ab.timeline.xml.getroot()
    timeline_actor_data_objects = timeline_root.findall('./region[@id="TimelineContent"]/node[@id="TimelineContent"]/children/node[@id="TimelineActorData"]/children/node[@id="TimelineActorData"]/children/node[@id="Object"]')
    for timeline_actor_data_object in timeline_actor_data_objects:
        if bg3.get_bg3_attribute(timeline_actor_data_object, 'MapKey') == 'cb0e6f06-2367-4cc4-9b18-e52bf37fb62c':
            val = timeline_actor_data_object.find('./children/node[@id="Value"]')
            if val:
                bg3.set_bg3_attribute(val, 'AttachTo', 'd2459f04-0433-9b92-f6f5-8f5990a796e1', attribute_type = 'guid')
                return


def restore_shadowheart_ultimatum() -> None:
    game_assets = get_context().assets

    ab = game_assets.get_modded_dialog_asset_bundle('CAMP_Shadowheart_CFM_Ultimatum')
    d = bg3.dialog_object(ab.dialog)

    patch_scene(ab)
    fix_speakers(ab)
    fix_wyll_camera(ab)
    patch_timeline(ab)

    speaker_idx_tav = d.get_speaker_slot_index(bg3.SPEAKER_PLAYER)
    speaker_idx_laezel = d.get_speaker_slot_index(bg3.SPEAKER_LAEZEL)

    random_inclusion_node_uuid = 'cead1afa-f8fd-8af5-f58d-34a9d1c1148f'
    jump_node_uuid = '1dfb6fcc-f4d8-4245-a6e3-e682f15463f5'
    karlach_inclusion_node = '5d249b24-8dd7-c728-7559-d848f0914c3f'
    d.delete_child_dialog_node(random_inclusion_node_uuid, karlach_inclusion_node)
    d.create_jump_dialog_node(jump_node_uuid, '94102576-4065-ab26-2f00-b0ef56b97692', 1)
    d.add_child_dialog_node(random_inclusion_node_uuid, jump_node_uuid)


    random_inclusion_node_uuid = 'f41518a1-1353-2b5b-0946-06e7fc5023d1'
    jump_node_uuid = '1c700e29-ab5f-4e9c-9315-63d7d039bf35'
    karlach_inclusion_node = '9c6ba38c-ab83-f009-08ac-0c47a185d15d'
    d.delete_child_dialog_node(random_inclusion_node_uuid, karlach_inclusion_node)
    d.create_jump_dialog_node(jump_node_uuid, '4118a0ac-0e7f-4635-5901-9429a19fdb2f', 1)
    d.add_child_dialog_node(random_inclusion_node_uuid, jump_node_uuid)

    # Check Lae'zel tag
    you_re_here_with_a_gith_node_uuid = '6884141c-7fa5-e4be-c9b8-385add4d5320'
    d.set_dialog_flags(you_re_here_with_a_gith_node_uuid, checkflags = (
        bg3.flag_group('Tag', (
            bg3.flag(bg3.TAG_REALLY_LAEZEL, True, speaker_idx_laezel),
            bg3.flag(bg3.TAG_AVATAR, True, speaker_idx_tav),
        )),
    ))

    # Add monk specific nodes
    maybe_youre_right_node_uuid = 'b31ba055-d1d6-74cb-202d-5e062fc44ea9' # existing node
    im_tired_of_being_pushed_node_uuid = 'a0616acb-c73c-c54f-b38b-22d08c647592' # existing node
    say_what_you_have_to_say_node_uuid = '4358bfae-62df-b2c2-b18c-5deade473733' # existing node
    there_is_a_knife_hidden_in_her_belt_node_uuid = '4d12a40c-5022-82a6-6690-357a8cc3d521' # existing node

    i_can_harm_you_or_help_you_node_uuid = '99800f33-884b-4426-aa88-b5401eafeaac'
    i_can_be_your_enemy_or_your_ally_node_uuid = '752f09f8-f634-4711-8ad6-989bf76e3754'
    first_you_need_to_calm_down_node_uuid = 'ec64cd42-50f0-4591-b2ce-507d2e7bf501'

    # I've spent years studying martial arts and even longer in meditation. I can harm you or help you. Your choice.
    d.create_standard_dialog_node(
        i_can_harm_you_or_help_you_node_uuid,
        bg3.SPEAKER_PLAYER,
        [maybe_youre_right_node_uuid],
        bg3.text_content('haf81aa5cg9a4cg4d59ga2dega391c7c6f212', 1),
        constructor = bg3.dialog_object.QUESTION,
        checkflags = (
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_MONK, True, speaker_idx_tav),
            )),
        ))

    # I've devoted years to martial arts and even more to meditation. I can be your enemy or your ally. You decide.
    d.create_standard_dialog_node(
        i_can_be_your_enemy_or_your_ally_node_uuid,
        bg3.SPEAKER_PLAYER,
        [say_what_you_have_to_say_node_uuid],
        bg3.text_content('hc0ac1647g6a79g4596gab70g55a73961e74b', 1),
        constructor = bg3.dialog_object.QUESTION,
        checkflags = (
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_MONK, True, speaker_idx_tav),
            )),
        ))

    # First, you need to calm down. That would be a great start.
    d.create_standard_dialog_node(
        first_you_need_to_calm_down_node_uuid,
        bg3.SPEAKER_PLAYER,
        [maybe_youre_right_node_uuid],
        bg3.text_content('h89819073g94d3g482ag9217g6a03d68c3d38', 1),
        constructor = bg3.dialog_object.QUESTION,
        checkflags = (
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_MONK, True, speaker_idx_tav),
            )),
        ))

    d.add_child_dialog_node(there_is_a_knife_hidden_in_her_belt_node_uuid, i_can_harm_you_or_help_you_node_uuid)
    d.add_child_dialog_node(im_tired_of_being_pushed_node_uuid, i_can_be_your_enemy_or_your_ally_node_uuid)
    d.add_child_dialog_node(say_what_you_have_to_say_node_uuid, first_you_need_to_calm_down_node_uuid, index = 0)


def patch_recruitment() -> None:
    game_assets = get_context().assets

    #
    # Shadowheart_Recruitment_Camp
    #
    ab = game_assets.get_modded_dialog_asset_bundle('Shadowheart_Recruitment_Camp')
    d = bg3.dialog_object(ab.dialog)

    speaker_idx_tav = d.get_speaker_slot_index(bg3.SPEAKER_PLAYER)
    speaker_idx_shadowheart = d.get_speaker_slot_index(bg3.SPEAKER_SHADOWHEART)

    # Remove 'Leave' from the 2nd conversation
    d.delete_child_dialog_node('d1f6ea32-4064-d59e-a120-4d1660c9239f', '347276b1-4ec4-a628-1b93-b2aa6fb1face')

    shadowheart_joins_the_party_node_uuid = 'ab9a613b-faa1-4adc-aa68-fc9cb1b006b5'
    shadowheart_joins_the_party_stays_in_camp_node_uuid = '9e8a5a67-36e0-40b1-859a-fd7b8f71e4f6'
    shadowheart_joins_the_party_active_companion_node_uuid = 'fb4ec776-de01-4f10-9953-5772ea85d827'

    d.create_standard_dialog_node(
        shadowheart_joins_the_party_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [shadowheart_joins_the_party_stays_in_camp_node_uuid, shadowheart_joins_the_party_active_companion_node_uuid],
        None,
        constructor = bg3.dialog_object.ANSWER)
    d.create_standard_dialog_node(
        shadowheart_joins_the_party_stays_in_camp_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [],
        None,
        constructor = bg3.dialog_object.ANSWER,
        end_node = True,
        checkflags = (
            bg3.flag_group('Global', (
                bg3.flag(bg3.FLAG_GEN_MaxPlayerCountReached, True, None),
            )),
        ),
        setflags = (
            bg3.flag_group('Global', (
                bg3.flag(bg3.FLAG_ORI_ShadowHeart_State_IsInParty, True, None),
            )),
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_GLO_ORI_Event_InvitedToCamp_Run, True, speaker_idx_shadowheart),
            )),
        ))
    d.create_standard_dialog_node(
        shadowheart_joins_the_party_active_companion_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [],
        None,
        constructor = bg3.dialog_object.ANSWER,
        end_node = True,
        setflags = (
            bg3.flag_group('Global', (
                bg3.flag(bg3.FLAG_ORI_ShadowHeart_State_IsInParty, True, None),
            )),
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_OriginAddToParty, True, speaker_idx_shadowheart),
            )),
        ))

    # Let's set off. Time is against us.
    d.remove_dialog_attribute('19ba0bfa-2649-db35-b10b-167bd988203d', 'endnode')
    d.set_dialog_flags('19ba0bfa-2649-db35-b10b-167bd988203d', checkflags = (), setflags = ())
    d.add_child_dialog_node('19ba0bfa-2649-db35-b10b-167bd988203d', shadowheart_joins_the_party_node_uuid)

    # I'm sure things will sort themselves out on the road.
    d.remove_dialog_attribute('3e77a20d-9419-1516-e415-71d35bd5e4b1', 'endnode')
    d.set_dialog_flags('3e77a20d-9419-1516-e415-71d35bd5e4b1', checkflags = (), setflags = ())
    d.add_child_dialog_node('3e77a20d-9419-1516-e415-71d35bd5e4b1', shadowheart_joins_the_party_node_uuid)

    # Yes. Let's get moving.
    d.remove_dialog_attribute('1fd3ca1f-1bfe-5f20-2bf3-47cdc387177a', 'endnode')
    d.set_dialog_flags('1fd3ca1f-1bfe-5f20-2bf3-47cdc387177a', checkflags = (), setflags = ())
    d.add_child_dialog_node('1fd3ca1f-1bfe-5f20-2bf3-47cdc387177a', shadowheart_joins_the_party_node_uuid)

    # You I don't mind, but your... kin is another story.
    d.set_dialog_flags('d44deba2-ccbb-94bf-0a41-f31f0a6f702b', checkflags = (
        bg3.flag_group('Global', (
            bg3.flag(bg3.FLAG_ORI_Laezel_State_IsInParty, True, None),
        )),
        bg3.flag_group('Tag', (
            bg3.flag(bg3.TAG_GITH, True, speaker_idx_tav),
        )),
    ))

    # And what does your gith companion have to say about that?
    d.set_dialog_flags('3d6118bf-88e6-ef1e-008c-b49e835d2e78', checkflags = (
        bg3.flag_group('Global', (
            bg3.flag(bg3.FLAG_ORI_Laezel_State_IsInParty, True, None),
        )),
    ))

    # Removes "I would, but you have a lot of hangers-on already. Thin your numbers, then we can talk." from the 1st convo
    d.delete_child_dialog_node('d58fe144-3b01-004a-903a-df8917901e35', 'ddd1b306-74c2-e92b-89be-7d170edf7be0')

    # Removes "I would, but you have a lot of hangers-on already. Thin your numbers, then we can talk." from the 2nd convo
    d.delete_child_dialog_node('ad996b77-f29e-af4e-ec56-3140fcd5867f', '35337e13-14c9-0d21-5b72-7f775a61469a')


    #
    # Shadowheart_Recruitment_Den
    #
    ab = game_assets.get_modded_dialog_asset_bundle('Shadowheart_Recruitment_Den')
    d = bg3.dialog_object(ab.dialog)

    speaker_idx_tav = d.get_speaker_slot_index(bg3.SPEAKER_PLAYER)

    # Remove "Wonderful. I was beginning to feel a little left out."
    node = d.find_dialog_node('b3d95318-7ac6-f6cf-0d6c-8f1eb9d528ee')
    tagged_texts_nodes = node.findall('./children/node[@id="TaggedTexts"]/children/node[@id="TaggedText"]/children/node[@id="TagTexts"]/children')
    for tagged_texts in tagged_texts_nodes:
        for tag_text in tagged_texts.findall('./node[@id="TagText"]'):
            handle = bg3.get_bg3_attribute(tag_text, 'TagText', value_name = 'handle')
            if handle == 'h620f0723g14dcg4858g80fdg063399ef8b9c':
                tagged_texts.remove(tag_text)
                break

    #
    # Shadowheart_Recruitment
    #
    ab = game_assets.get_modded_dialog_asset_bundle('Shadowheart_Recruitment')
    d = bg3.dialog_object(ab.dialog)

    # Remove "Wonderful. I was beginning to feel a little left out."
    node = d.find_dialog_node('09a5f386-3e49-9cc4-28f2-74a1702bad18')
    tagged_texts_nodes = node.findall('./children/node[@id="TaggedTexts"]/children/node[@id="TaggedText"]/children/node[@id="TagTexts"]/children')
    for tagged_texts in tagged_texts_nodes:
        for tag_text in tagged_texts.findall('./node[@id="TagText"]'):
            handle = bg3.get_bg3_attribute(tag_text, 'TagText', value_name = 'handle')
            if handle == 'h6cdc1333ga846g4a87g85dbg8df814df7a05':
                tagged_texts.remove(tag_text)
                break


def patch_campfire_trigger() -> None:
    files = get_context().files
    ultimatum_dialog_uuid = get_context().assets.get_modded_dialog_asset_bundle('CAMP_Shadowheart_CFM_Ultimatum').modded_dialog_uuid

    gf = files.get_file('Gustav', 'Mods/Gustav/Levels/LT_CMP_CentralCampfire_B/Triggers/_merged.lsf', mod_specific = True)
    triggers_parent = gf.xml.getroot().find('./region[@id="Templates"]/node[@id="Templates"]/children')
    if triggers_parent is None:
        raise RuntimeError('cannot patch S_CAMP_Shadowheart_CFM_Ultimatum_SceneTrigger')
    triggers = triggers_parent.findall('./node[@id="GameObjects"]')
    patched = False
    for trigger in triggers:
        if bg3.get_bg3_attribute(trigger, 'MapKey') == 'eea9d501-ef09-4929-89ac-a348849aeb50':
            timeline = trigger.find('./children/node[@id="Timelines"]/children/node[@id="Timeline"]')
            if timeline is None:
                raise RuntimeError('cannot patch S_CAMP_Shadowheart_CFM_Ultimatum_SceneTrigger')
            bg3.set_bg3_attribute(timeline, 'Object', ultimatum_dialog_uuid, attribute_type = 'guid')
            patched = True
        else:
            triggers_parent.remove(trigger)
    if not patched:
        raise RuntimeError('cannot patch S_CAMP_Shadowheart_CFM_Ultimatum_SceneTrigger')


bg3.add_build_procedure('restore_shadowheart_ultimatum', restore_shadowheart_ultimatum)
bg3.add_build_procedure('patch_campfire_trigger', patch_campfire_trigger)
bg3.add_build_procedure('patch_recruitment', patch_recruitment)


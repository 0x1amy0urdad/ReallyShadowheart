from __future__ import annotations

import bg3moddinglib as bg3

from .context import get_context
from .flags import *

#############################################################################################################
# Lae'zel/Wyll/Shadowheart banter bugfix: both Shar and Selune banters didn't have their respective flags.
# This causes both banters to play one after another, which is very odd.
#############################################################################################################


def fix_banters() -> None:
    files = get_context().files

    #############################################################################################################
    # Public/GustavDev/Gossips/Gossips.lsx
    #############################################################################################################
    gustav_gossips = bg3.gossips_object(files.get_file("Gustav", "Public/Gustav/Gossips/Gossips.lsx", exclude_from_build = True))
    gustavdev_gossips = bg3.gossips_object(files.get_file("Gustav", "Public/GustavDev/Gossips/Gossips.lsx", exclude_from_build = True))
    fixed_gossips = bg3.gossips_object.create_new(files)

    # PB_Shadowheart_Wyll_Legacy
    fixed_gossips.add_gossip_element(gustav_gossips.get_gossip_by_uuid('b3da8a37-3bc5-32a8-af43-6476d3d91a8d'))
    fixed_gossips.add_condition_flag('b3da8a37-3bc5-32a8-af43-6476d3d91a8d', 'Flag', bg3.FLAG_ORI_Wyll_State_IsDevil)


    # PB_Shadowheart_Laezel_ROM_Act1
    fixed_gossips.add_gossip_element(gustavdev_gossips.get_gossip_by_uuid('77803562-a190-fab7-cc8a-365c1612d14d'))
    fixed_gossips.add_condition_flag('77803562-a190-fab7-cc8a-365c1612d14d', 'Flag', bg3.FLAG_ORI_Laezel_State_Romance1HadSex)

    # PB_Astarion_Laezel_ROM_Act1
    fixed_gossips.add_gossip_element(gustavdev_gossips.get_gossip_by_uuid('616d7ea7-4b8f-f96e-6d96-e684a8568549'))
    fixed_gossips.add_condition_flag('616d7ea7-4b8f-f96e-6d96-e684a8568549', 'Flag', bg3.FLAG_ORI_Laezel_State_Romance1HadSex)

    # PB_Gale_Laezel_ROM_Act1
    fixed_gossips.add_gossip_element(gustavdev_gossips.get_gossip_by_uuid('1f8cb02b-a6da-17bd-4b8e-650f37637ef7'))
    fixed_gossips.add_condition_flag('1f8cb02b-a6da-17bd-4b8e-650f37637ef7', 'Flag', bg3.FLAG_ORI_Laezel_State_Romance1HadSex)

    # PB_Karlach_Laezel_ROM_Act1_001
    fixed_gossips.add_gossip_element(gustavdev_gossips.get_gossip_by_uuid('3527a53d-e38e-18d2-84cc-97609c8ae245'))
    fixed_gossips.add_condition_flag('3527a53d-e38e-18d2-84cc-97609c8ae245', 'Flag', bg3.FLAG_ORI_Laezel_State_Romance1HadSex)


    # PB_Laezel_Shadowheart_ROM_Act3_001
    fixed_gossips.add_gossip_element(gustavdev_gossips.get_gossip_by_uuid('864be4b4-5180-00c6-71eb-2154cd643362'))
    fixed_gossips.add_condition_flag('864be4b4-5180-00c6-71eb-2154cd643362', 'Flag', bg3.FLAG_NIGHT_Shadowheart_NightfallRitual)

    # PB_Laezel_Shadowheart_ROM_Act3_002
    fixed_gossips.add_gossip_element(gustavdev_gossips.get_gossip_by_uuid('145920b8-d582-5cd3-03c0-65557663fad9'))
    fixed_gossips.add_condition_flag('145920b8-d582-5cd3-03c0-65557663fad9', 'Flag', bg3.FLAG_NIGHT_Shadowheart_Skinnydipping)

    # PB_Wyll_Shadowheart_ROM_Act3_001
    fixed_gossips.add_gossip_element(gustavdev_gossips.get_gossip_by_uuid('78ee3f89-256f-0dba-f14c-4fcbb1a731a1'))
    fixed_gossips.add_condition_flag('78ee3f89-256f-0dba-f14c-4fcbb1a731a1', 'Flag', bg3.FLAG_ORI_Shadowheart_State_Shar_KilledParents)
    fixed_gossips.add_condition_flag('78ee3f89-256f-0dba-f14c-4fcbb1a731a1', 'Flag', bg3.FLAG_ORI_State_ShadowheartIsDating)

    # PB_Wyll_Shadowheart_ROM_Act3_002
    fixed_gossips.add_gossip_element(gustavdev_gossips.get_gossip_by_uuid('a5be03a8-7ecd-5d0e-b1d5-283f58806581'))
    fixed_gossips.add_condition_flag('a5be03a8-7ecd-5d0e-b1d5-283f58806581', 'Flag', Shadowheart_Turned_Away_From_Shar.uuid)
    fixed_gossips.add_condition_flag('a5be03a8-7ecd-5d0e-b1d5-283f58806581', 'Flag', bg3.FLAG_ORI_State_ShadowheartIsDating)


    # This removes duplicate banters that caused them repeat all the time
    # Patch 8 fixed this, 'if' clauses fix this for earlier patches
    # PB_Halsin_Shadowheart_ROM_Act3_Selune
    # if 'ba18fb11-3e5e-49a2-b18d-6ed0a7d4b73a' in g and '5ffe430e-2c29-4f17-afb5-85dbff17735c' in g:
    #     #g.remove_gossip('ba18fb11-3e5e-49a2-b18d-6ed0a7d4b73a')
    #     g.remove_gossip('5ffe430e-2c29-4f17-afb5-85dbff17735c')

    # # PB_Halsin_Shadowheart_ROM_Act3_Shar
    # if 'c3365dd5-83d6-4a53-9227-e2477e0a7fb5' in g and '431f4426-1a87-4f48-aca0-5f61ea236676' in g:
    #     #g.remove_gossip('c3365dd5-83d6-4a53-9227-e2477e0a7fb5')
    #     g.remove_gossip('431f4426-1a87-4f48-aca0-5f61ea236676')
    

bg3.add_build_procedure('fix_banters', fix_banters)

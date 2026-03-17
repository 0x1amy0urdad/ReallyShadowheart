from __future__ import annotations

import bg3moddinglib as bg3

from .context import get_context
from .flags import *
from .new_kisses_karlach import (
    create_karlach_kiss_A_timeline,
    create_karlach_kiss_B_timeline,
    create_karlach_kiss_C_timeline,
    create_karlach_kiss_D_timeline,
)
from .new_kisses_lword import (
    create_lword_kiss_bt1_timeline,
    create_lword_kiss_bt2_timeline,
    create_lword_kiss_bt34_timeline,
    create_lword_kiss_dragonborn_timeline,
    create_lword_kiss_short_timeline,
    create_lword_kiss_dwarf_timeline,
)
from .new_kisses_minthara import (
    create_minthara_kiss_A_timeline,
    create_minthara_kiss_B_timeline,
    create_minthara_kiss_C_timeline,
    create_minthara_kiss_D_timeline,
)

# existing exit node of the nested dialog ShadowHeart_InParty2_Nested_ShadowheartKiss
kiss_nested_dialog_exit_node_uuid = 'd67e9777-539d-f113-62e4-034dbe759c36'

# existing root node of the nested dialog ShadowHeart_InParty2_Nested_ShadowheartKiss
kiss_nested_dialog_root_node_uuid = '7145a7e3-d1b5-d29a-c685-3867b85b4021'

# New nested dialog UUID
new_kiss_nested_dialog_uuid = '25a2ef68-ec37-40f5-b0a3-f89abe22abff' # new nested dialog

###############################################################
# Enable all 6 kiss animations
###############################################################

def patch_kiss_animations() -> None:
    game_assets = get_context().assets

    ab = game_assets.get_modded_dialog_asset_bundle('ShadowHeart_InParty2_Nested_ShadowheartKiss')
    d = bg3.dialog_object(ab.dialog)
    t = bg3.timeline_object(ab.timeline, d)

    ###############################################################
    # Dialog: ShadowHeart_InParty2_Nested_ShadowheartKiss.lsf
    # Enable all 6 kiss animations
    ###############################################################

    slot_idx_shadowheart = d.get_speaker_slot_index(bg3.SPEAKER_SHADOWHEART)
    slot_idx_tav = d.get_speaker_slot_index(bg3.SPEAKER_PLAYER)

    # Reset kiss flags on nested dialog exit
    d.add_dialog_flags(
        kiss_nested_dialog_exit_node_uuid,
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(Shadowheart_Kiss_Event.uuid, True, slot_idx_shadowheart),
                bg3.flag(ORI_ShadowheartKiss_StartRandom.uuid, False, slot_idx_shadowheart),
                bg3.flag(ORI_ShadowheartKiss_VersionA.uuid, False, slot_idx_shadowheart),
                bg3.flag(ORI_ShadowheartKiss_VersionB.uuid, False, slot_idx_shadowheart),
                bg3.flag(ORI_ShadowheartKiss_VersionC.uuid, False, slot_idx_shadowheart),
                bg3.flag(ORI_ShadowheartKiss_VersionD.uuid, False, slot_idx_shadowheart),
                bg3.flag(ORI_ShadowheartKiss_VersionE.uuid, False, slot_idx_shadowheart),
                bg3.flag(ORI_ShadowheartKiss_VersionF.uuid, False, slot_idx_shadowheart),
                bg3.flag(ORI_ShadowheartKiss_LoveYou.uuid, False, slot_idx_shadowheart),
                bg3.flag(Karlach_Kiss_A.uuid, False, slot_idx_shadowheart),
                bg3.flag(Karlach_Kiss_B.uuid, False, slot_idx_shadowheart),
                bg3.flag(Karlach_Kiss_C.uuid, False, slot_idx_shadowheart),
                bg3.flag(Karlach_Kiss_D.uuid, False, slot_idx_shadowheart),
                bg3.flag(Minthara_Kiss_A.uuid, False, slot_idx_shadowheart),
                bg3.flag(Minthara_Kiss_B.uuid, False, slot_idx_shadowheart),
                bg3.flag(Minthara_Kiss_C.uuid, False, slot_idx_shadowheart),
                bg3.flag(Minthara_Kiss_D.uuid, False, slot_idx_shadowheart),
            )),
        ))

    #
    # Patch kiss nodes
    #

    # Short races
    d.set_dialog_flags('2ffffa29-fa83-40b1-aac9-a584cdb2f695', checkflags = (
        bg3.flag_group('Object', (
            bg3.flag(ORI_ShadowheartKiss_VersionA.uuid, True, slot_idx_shadowheart),
        )),
        bg3.flag_group('Tag', (
            bg3.flag(bg3.TAG_SHORT, True, slot_idx_tav),
        )),
    ))
    d.set_dialog_flags('cdc3977a-e50a-d981-8c31-c07504ea2a07', checkflags = (
        bg3.flag_group('Object', (
            bg3.flag(ORI_ShadowheartKiss_VersionB.uuid, True, slot_idx_shadowheart),
        )),
        bg3.flag_group('Tag', (
            bg3.flag(bg3.TAG_DWARF, True, slot_idx_tav),
            bg3.flag(bg3.TAG_SHORT, True, slot_idx_tav),
        )),
    ))
    d.set_dialog_flags('e7cc3a96-2a3a-7e24-ab65-82245a27b7b2', checkflags = (
        bg3.flag_group('Object', (
            bg3.flag(ORI_ShadowheartKiss_VersionB.uuid, True, slot_idx_shadowheart),
        )),
        bg3.flag_group('Tag', (
            bg3.flag(bg3.TAG_SHORT, True, slot_idx_tav),
        )),
    ))
    d.set_dialog_flags('23bffd00-5280-a6b6-3f21-54ad298cb67e', checkflags = (
        bg3.flag_group('Object', (
            bg3.flag(ORI_ShadowheartKiss_VersionC.uuid, True, slot_idx_shadowheart),
        )),
        bg3.flag_group('Tag', (
            bg3.flag(bg3.TAG_DWARF, True, slot_idx_tav),
            bg3.flag(bg3.TAG_SHORT, True, slot_idx_tav),
        )),
    ))
    d.set_dialog_flags('eb0d744a-a22f-326f-6194-88bff056f6bb', checkflags = (
        bg3.flag_group('Object', (
            bg3.flag(ORI_ShadowheartKiss_VersionC.uuid, True, slot_idx_shadowheart),
        )),
        bg3.flag_group('Tag', (
            bg3.flag(bg3.TAG_SHORT, True, slot_idx_tav),
        )),
    ))
    d.set_dialog_flags('4cf4c762-1738-2ebe-c65b-79f1300e97c7', checkflags = (
        bg3.flag_group('Object', (
            bg3.flag(ORI_ShadowheartKiss_VersionD.uuid, True, slot_idx_shadowheart),
        )),
        bg3.flag_group('Tag', (
            bg3.flag(bg3.TAG_DWARF, True, slot_idx_tav),
            bg3.flag(bg3.TAG_SHORT, True, slot_idx_tav),
        )),
    ))
    d.set_dialog_flags('bf5d6f26-ffa3-510e-be90-39f57002fbc9', checkflags = (
        bg3.flag_group('Object', (
            bg3.flag(ORI_ShadowheartKiss_VersionD.uuid, True, slot_idx_shadowheart),
        )),
        bg3.flag_group('Tag', (
            bg3.flag(bg3.TAG_SHORT, True, slot_idx_tav),
        )),
    ))
    d.set_dialog_flags('35bb16bc-27e0-febc-abf9-31b38a667199', checkflags = (
        bg3.flag_group('Object', (
            bg3.flag(ORI_ShadowheartKiss_VersionE.uuid, True, slot_idx_shadowheart),
        )),
        bg3.flag_group('Tag', (
            bg3.flag(bg3.TAG_DWARF, True, slot_idx_tav),
            bg3.flag(bg3.TAG_SHORT, True, slot_idx_tav),
        )),
    ))
    d.set_dialog_flags('d9f9b4c6-4929-f14a-85b0-cc48794abf43', checkflags = (
        bg3.flag_group('Object', (
            bg3.flag(ORI_ShadowheartKiss_VersionE.uuid, True, slot_idx_shadowheart),
        )),
        bg3.flag_group('Tag', (
            bg3.flag(bg3.TAG_SHORT, True, slot_idx_tav),
        )),
    ))
    d.set_dialog_flags('6dce7fcd-e8a4-e34a-1835-22628c420853', checkflags = (
        bg3.flag_group('Object', (
            bg3.flag(ORI_ShadowheartKiss_VersionF.uuid, True, slot_idx_shadowheart),
        )),
        bg3.flag_group('Tag', (
            bg3.flag(bg3.TAG_DWARF, True, slot_idx_tav),
            bg3.flag(bg3.TAG_SHORT, True, slot_idx_tav),
        )),
    ))
    d.set_dialog_flags('d0d19c73-576a-e417-e9ce-b0ff488c3ba4', checkflags = (
        bg3.flag_group('Object', (
            bg3.flag(ORI_ShadowheartKiss_VersionF.uuid, True, slot_idx_shadowheart),
        )),
        bg3.flag_group('Tag', (
            bg3.flag(bg3.TAG_SHORT, True, slot_idx_tav),
        )),
    ))

    # Dragonborn
    d.set_dialog_flags('b2ef3011-5998-205c-9ccc-a2d2b2c6f338', checkflags = (
        bg3.flag_group('Object', (
            bg3.flag(ORI_ShadowheartKiss_VersionA.uuid, True, slot_idx_shadowheart),
        )),
        bg3.flag_group('Tag', (
            bg3.flag(bg3.TAG_DRAGONBORN, True, slot_idx_tav),
        )),
    ))
    d.set_dialog_flags('82a9d305-ae45-d69c-d801-1c82cff326f1', checkflags = (
        bg3.flag_group('Object', (
            bg3.flag(ORI_ShadowheartKiss_VersionB.uuid, True, slot_idx_shadowheart),
        )),
        bg3.flag_group('Tag', (
            bg3.flag(bg3.TAG_DRAGONBORN, True, slot_idx_tav),
        )),
    ))
    d.set_dialog_flags('326bfde2-8fa5-5a6c-4375-5ad4be27a162', checkflags = (
        bg3.flag_group('Object', (
            bg3.flag(ORI_ShadowheartKiss_VersionC.uuid, True, slot_idx_shadowheart),
        )),
        bg3.flag_group('Tag', (
            bg3.flag(bg3.TAG_DRAGONBORN, True, slot_idx_tav),
        )),
    ))
    d.set_dialog_flags('b2d0a1d2-a0c1-8716-943b-45c873e58554', checkflags = (
        bg3.flag_group('Object', (
            bg3.flag(ORI_ShadowheartKiss_VersionD.uuid, True, slot_idx_shadowheart),
        )),
        bg3.flag_group('Tag', (
            bg3.flag(bg3.TAG_DRAGONBORN, True, slot_idx_tav),
        )),
    ))
    d.set_dialog_flags('8449fe59-b9ef-c695-1f8e-4af4d7b1adad', checkflags = (
        bg3.flag_group('Object', (
            bg3.flag(ORI_ShadowheartKiss_VersionE.uuid, True, slot_idx_shadowheart),
        )),
        bg3.flag_group('Tag', (
            bg3.flag(bg3.TAG_DRAGONBORN, True, slot_idx_tav),
        )),
    ))
    d.set_dialog_flags('f2a7d192-4dbb-4c6a-2cc5-3702a0917c2b', checkflags = (
        bg3.flag_group('Object', (
            bg3.flag(ORI_ShadowheartKiss_VersionF.uuid, True, slot_idx_shadowheart),
        )),
        bg3.flag_group('Tag', (
            bg3.flag(bg3.TAG_DRAGONBORN, True, slot_idx_tav),
        )),
    ))

    # Strong
    d.set_dialog_flags('27966d84-2797-3c76-a194-4ff46f1ceb51', checkflags = (
        bg3.flag_group('Object', (
            bg3.flag(ORI_ShadowheartKiss_VersionA.uuid, True, slot_idx_shadowheart),
        )),
        bg3.flag_group('Tag', (
            bg3.flag(bg3.TAG_BODYTYPE_STRONG, True, slot_idx_tav),
        )),
    ))
    d.set_dialog_flags('0866f9b0-0661-049a-68cf-3fee75dd975f', checkflags = (
        bg3.flag_group('Object', (
            bg3.flag(ORI_ShadowheartKiss_VersionB.uuid, True, slot_idx_shadowheart),
        )),
        bg3.flag_group('Tag', (
            bg3.flag(bg3.TAG_BODYTYPE_STRONG, True, slot_idx_tav),
        )),
    ))
    d.set_dialog_flags('1c8219d9-0968-f5ee-850b-718d7475c3e6', checkflags = (
        bg3.flag_group('Object', (
            bg3.flag(ORI_ShadowheartKiss_VersionC.uuid, True, slot_idx_shadowheart),
        )),
        bg3.flag_group('Tag', (
            bg3.flag(bg3.TAG_BODYTYPE_STRONG, True, slot_idx_tav),
        )),
    ))
    d.set_dialog_flags('6846f52c-f84c-1301-3c90-8e5af97cdfdc', checkflags = (
        bg3.flag_group('Object', (
            bg3.flag(ORI_ShadowheartKiss_VersionD.uuid, True, slot_idx_shadowheart),
        )),
        bg3.flag_group('Tag', (
            bg3.flag(bg3.TAG_BODYTYPE_STRONG, True, slot_idx_tav),
        )),
    ))
    d.set_dialog_flags('6df05a7c-ba69-56d4-d006-5bc5d749887f', checkflags = (
        bg3.flag_group('Object', (
            bg3.flag(ORI_ShadowheartKiss_VersionE.uuid, True, slot_idx_shadowheart),
        )),
        bg3.flag_group('Tag', (
            bg3.flag(bg3.TAG_BODYTYPE_STRONG, True, slot_idx_tav),
        )),
    ))
    d.set_dialog_flags('348eb539-29ef-d53f-2888-259886dd0215', checkflags = (
        bg3.flag_group('Object', (
            bg3.flag(ORI_ShadowheartKiss_VersionF.uuid, True, slot_idx_shadowheart),
        )),
        bg3.flag_group('Tag', (
            bg3.flag(bg3.TAG_BODYTYPE_STRONG, True, slot_idx_tav),
        )),
    ))

    # Female
    d.set_dialog_flags('2e786fd7-bbc4-df6b-0df2-e8413461e992', checkflags = (
        bg3.flag_group('Object', (
            bg3.flag(ORI_ShadowheartKiss_VersionA.uuid, True, slot_idx_shadowheart),
        )),
        bg3.flag_group('Tag', (
            bg3.flag(bg3.TAG_FEMALE, True, slot_idx_tav),
        )),
    ))
    d.set_dialog_flags('67685b15-4a85-9cc0-2bbd-830057576453', checkflags = (
        bg3.flag_group('Object', (
            bg3.flag(ORI_ShadowheartKiss_VersionB.uuid, True, slot_idx_shadowheart),
        )),
        bg3.flag_group('Tag', (
            bg3.flag(bg3.TAG_FEMALE, True, slot_idx_tav),
        )),
    ))
    d.set_dialog_flags('0f0cdfa6-9d87-0378-a11b-a150f263c20f', checkflags = (
        bg3.flag_group('Object', (
            bg3.flag(ORI_ShadowheartKiss_VersionC.uuid, True, slot_idx_shadowheart),
        )),
        bg3.flag_group('Tag', (
            bg3.flag(bg3.TAG_FEMALE, True, slot_idx_tav),
        )),
    ))
    d.set_dialog_flags('a075864d-1599-3e49-488c-9352becb96ad', checkflags = (
        bg3.flag_group('Object', (
            bg3.flag(ORI_ShadowheartKiss_VersionD.uuid, True, slot_idx_shadowheart),
        )),
        bg3.flag_group('Tag', (
            bg3.flag(bg3.TAG_FEMALE, True, slot_idx_tav),
        )),
    ))
    d.set_dialog_flags('d5a7a82e-5605-d625-1bde-1164a5e03315', checkflags = (
        bg3.flag_group('Object', (
            bg3.flag(ORI_ShadowheartKiss_VersionE.uuid, True, slot_idx_shadowheart),
        )),
        bg3.flag_group('Tag', (
            bg3.flag(bg3.TAG_FEMALE, True, slot_idx_tav),
        )),
    ))
    d.set_dialog_flags('801d3007-d326-ead4-716d-923a87c1e03e', checkflags = (
        bg3.flag_group('Object', (
            bg3.flag(ORI_ShadowheartKiss_VersionF.uuid, True, slot_idx_shadowheart),
        )),
        bg3.flag_group('Tag', (
            bg3.flag(bg3.TAG_FEMALE, True, slot_idx_tav),
        )),
    ))

    # Normal body type
    d.set_dialog_flags('5f5e750e-d2e2-4e2e-90fe-e6f7fc8eea71', checkflags = (
        bg3.flag_group('Object', (
            bg3.flag(ORI_ShadowheartKiss_VersionA.uuid, True, slot_idx_shadowheart),
        )),
    ))
    d.set_dialog_flags('835d0310-5eca-d609-2845-b6692e047f80', checkflags = (
        bg3.flag_group('Object', (
            bg3.flag(ORI_ShadowheartKiss_VersionB.uuid, True, slot_idx_shadowheart),
        )),    
    ))
    d.set_dialog_flags('bd660b28-e92c-2ea0-2303-dd1fb33a8cc8', checkflags = (
        bg3.flag_group('Object', (
            bg3.flag(ORI_ShadowheartKiss_VersionC.uuid, True, slot_idx_shadowheart),
        )),        
    ))
    d.set_dialog_flags('ccddbf44-b77d-ba97-54f4-a3332ca49b4b', checkflags = (
        bg3.flag_group('Object', (
            bg3.flag(ORI_ShadowheartKiss_VersionD.uuid, True, slot_idx_shadowheart),
        )),
    ))
    d.set_dialog_flags('0dffa14a-c979-c806-3edf-6313dab6e589', checkflags = (
        bg3.flag_group('Object', (
            bg3.flag(ORI_ShadowheartKiss_VersionE.uuid, True, slot_idx_shadowheart),
        )),
    ))
    d.set_dialog_flags('e78d9f78-9dee-6a1c-63c6-8b06ec82c2bc', checkflags = (    
        bg3.flag_group('Object', (
            bg3.flag(ORI_ShadowheartKiss_VersionF.uuid, True, slot_idx_shadowheart),
        )),
    ))

    #
    # Fallback nodes
    #

    # Short races
    d.create_alias_dialog_node(
        '802a2231-ebc4-43de-9f5d-c4f13d6bf73a',
        '2ffffa29-fa83-40b1-aac9-a584cdb2f695',
        [kiss_nested_dialog_exit_node_uuid],
        checkflags = (
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_SHORT, True, slot_idx_tav),
            )),
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_Kiss_VersionA, True, slot_idx_shadowheart),
            ))
        ),
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_Kiss_EndRandom, False, slot_idx_shadowheart),
            )),
        )
    )
    d.create_alias_dialog_node(
        '731508a7-53e7-41bd-be3c-73e518ffbbc5',
        'cdc3977a-e50a-d981-8c31-c07504ea2a07',
        [kiss_nested_dialog_exit_node_uuid],
        checkflags = (
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_DWARF, True, slot_idx_tav),
                bg3.flag(bg3.TAG_SHORT, True, slot_idx_tav),
            )),
            bg3.flag_group('Global', (
                bg3.flag(Shadowheart_Turned_Away_From_Shar.uuid, True, None),
            )),
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_Kiss_VersionB, True, slot_idx_shadowheart),
            ))
        ),
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_Kiss_EndRandom, False, slot_idx_shadowheart),
            )),
        )
    )
    d.create_alias_dialog_node(
        'a13efe06-8698-4934-b5a7-ce8e6aa38b80',
        'e7cc3a96-2a3a-7e24-ab65-82245a27b7b2',
        [kiss_nested_dialog_exit_node_uuid],
        checkflags = (
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_SHORT, True, slot_idx_tav),
            )),
            bg3.flag_group('Global', (
                bg3.flag(Shadowheart_Turned_Away_From_Shar.uuid, True, None),
            )),
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_Kiss_VersionB, True, slot_idx_shadowheart),
            ))
        ),
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_Kiss_EndRandom, False, slot_idx_shadowheart),
            )),
        )
    )
    d.create_alias_dialog_node(
        '024286cb-3b53-4f85-a22e-59be7f8838db',
        '23bffd00-5280-a6b6-3f21-54ad298cb67e',
        [kiss_nested_dialog_exit_node_uuid],
        checkflags = (
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_DWARF, True, slot_idx_tav),
                bg3.flag(bg3.TAG_SHORT, True, slot_idx_tav),
            )),
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_Kiss_VersionB, True, slot_idx_shadowheart),
            ))
        ),
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_Kiss_EndRandom, False, slot_idx_shadowheart),
            )),
        )
    )
    d.create_alias_dialog_node(
        'cd34fe3a-d6b2-4263-ad27-4d0422b9f29e',
        'eb0d744a-a22f-326f-6194-88bff056f6bb',
        [kiss_nested_dialog_exit_node_uuid],
        checkflags = (
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_SHORT, True, slot_idx_tav),
            )),
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_Kiss_VersionB, True, slot_idx_shadowheart),
            ))
        ),
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_Kiss_EndRandom, False, slot_idx_shadowheart),
            )),
        )
    )
    d.create_alias_dialog_node(
        '692f3647-0044-41a6-9bb4-fe2f4b9d8997',
        '4cf4c762-1738-2ebe-c65b-79f1300e97c7',
        [kiss_nested_dialog_exit_node_uuid],
        checkflags = (
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_DWARF, True, slot_idx_tav),
                bg3.flag(bg3.TAG_SHORT, True, slot_idx_tav),
            )),
            bg3.flag_group('Global', (
                bg3.flag(Shadowheart_Turned_Away_From_Shar.uuid, True, None),
            )),
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_Kiss_VersionC, True, slot_idx_shadowheart),
            ))
        ),
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_Kiss_EndRandom, False, slot_idx_shadowheart),
            )),
        )
    )
    d.create_alias_dialog_node(
        '33207314-881d-44f2-b63d-0d3b01296092',
        'bf5d6f26-ffa3-510e-be90-39f57002fbc9',
        [kiss_nested_dialog_exit_node_uuid],
        checkflags = (
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_SHORT, True, slot_idx_tav),
            )),
            bg3.flag_group('Global', (
                bg3.flag(Shadowheart_Turned_Away_From_Shar.uuid, True, None),
            )),
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_Kiss_VersionC, True, slot_idx_shadowheart),
            ))
        ),
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_Kiss_EndRandom, False, slot_idx_shadowheart),
            )),
        )
    )
    d.create_alias_dialog_node(
        '65954feb-ea67-4f27-b057-0f72abf162d1',
        '35bb16bc-27e0-febc-abf9-31b38a667199',
        [kiss_nested_dialog_exit_node_uuid],
        checkflags = (
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_DWARF, True, slot_idx_tav),
                bg3.flag(bg3.TAG_SHORT, True, slot_idx_tav),
            )),
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_Kiss_VersionC, True, slot_idx_shadowheart),
            ))
        ),
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_Kiss_EndRandom, False, slot_idx_shadowheart),
            )),
        )
    )
    d.create_alias_dialog_node(
        'f609373d-ca38-4461-9a9e-447c4f29c3bb',
        'd9f9b4c6-4929-f14a-85b0-cc48794abf43',
        [kiss_nested_dialog_exit_node_uuid],
        checkflags = (
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_SHORT, True, slot_idx_tav),
            )),
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_Kiss_VersionC, True, slot_idx_shadowheart),
            ))
        ),
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_Kiss_EndRandom, False, slot_idx_shadowheart),
            )),
        )
    )
    d.create_alias_dialog_node(
        'd7221ced-69d8-48fd-91a2-448ef0861819',
        '6dce7fcd-e8a4-e34a-1835-22628c420853',
        [kiss_nested_dialog_exit_node_uuid],
        checkflags = (
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_DWARF, True, slot_idx_tav),
                bg3.flag(bg3.TAG_SHORT, True, slot_idx_tav),
            )),
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_Kiss_VersionD, True, slot_idx_shadowheart),
            ))
        ),
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_Kiss_EndRandom, False, slot_idx_shadowheart),
            )),
        )
    )
    d.create_alias_dialog_node(
        '8eea9d48-a72a-4350-a1da-eb98503276aa',
        'd0d19c73-576a-e417-e9ce-b0ff488c3ba4',
        [kiss_nested_dialog_exit_node_uuid],
        checkflags = (
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_SHORT, True, slot_idx_tav),
            )),
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_Kiss_VersionD, True, slot_idx_shadowheart),
            ))
        ),
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_Kiss_EndRandom, False, slot_idx_shadowheart),
            )),
        )
    )

    d.add_child_dialog_node(kiss_nested_dialog_root_node_uuid, '802a2231-ebc4-43de-9f5d-c4f13d6bf73a')
    d.add_child_dialog_node(kiss_nested_dialog_root_node_uuid, '731508a7-53e7-41bd-be3c-73e518ffbbc5')
    d.add_child_dialog_node(kiss_nested_dialog_root_node_uuid, 'e7cc3a96-2a3a-7e24-ab65-82245a27b7b2')
    d.add_child_dialog_node(kiss_nested_dialog_root_node_uuid, '23bffd00-5280-a6b6-3f21-54ad298cb67e')
    d.add_child_dialog_node(kiss_nested_dialog_root_node_uuid, 'eb0d744a-a22f-326f-6194-88bff056f6bb')
    d.add_child_dialog_node(kiss_nested_dialog_root_node_uuid, '4cf4c762-1738-2ebe-c65b-79f1300e97c7')
    d.add_child_dialog_node(kiss_nested_dialog_root_node_uuid, 'bf5d6f26-ffa3-510e-be90-39f57002fbc9')
    d.add_child_dialog_node(kiss_nested_dialog_root_node_uuid, '35bb16bc-27e0-febc-abf9-31b38a667199')
    d.add_child_dialog_node(kiss_nested_dialog_root_node_uuid, 'd9f9b4c6-4929-f14a-85b0-cc48794abf43')
    d.add_child_dialog_node(kiss_nested_dialog_root_node_uuid, '6dce7fcd-e8a4-e34a-1835-22628c420853')
    d.add_child_dialog_node(kiss_nested_dialog_root_node_uuid, 'd0d19c73-576a-e417-e9ce-b0ff488c3ba4')

    # Dragonborn
    d.create_alias_dialog_node(
        '5f0cec3f-92b4-4f50-90cc-343977ef3992',
        'b2ef3011-5998-205c-9ccc-a2d2b2c6f338',
        [kiss_nested_dialog_exit_node_uuid],
        checkflags = (
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_DRAGONBORN, True, slot_idx_tav),
            )),
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_Kiss_VersionA, True, slot_idx_shadowheart),
            ))
        ),
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_Kiss_EndRandom, False, slot_idx_shadowheart),
            )),
        )
    )
    d.create_alias_dialog_node(
        'f2f0aaea-20ea-464c-9d46-58e9d238c54a',
        '82a9d305-ae45-d69c-d801-1c82cff326f1',
        [kiss_nested_dialog_exit_node_uuid],
        checkflags = (
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_DRAGONBORN, True, slot_idx_tav),
            )),
            bg3.flag_group('Global', (
                bg3.flag(Shadowheart_Turned_Away_From_Shar.uuid, True, None),
            )),
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_Kiss_VersionB, True, slot_idx_shadowheart),
            ))
        ),
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_Kiss_EndRandom, False, slot_idx_shadowheart),
            )),
        )
    )
    d.create_alias_dialog_node(
        'e59b0566-fc67-4130-9ce3-76c2182618c7',
        '326bfde2-8fa5-5a6c-4375-5ad4be27a162',
        [kiss_nested_dialog_exit_node_uuid],
        checkflags = (
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_DRAGONBORN, True, slot_idx_tav),
            )),
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_Kiss_VersionB, True, slot_idx_shadowheart),
            ))
        ),
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_Kiss_EndRandom, False, slot_idx_shadowheart),
            )),
        )
    )
    d.create_alias_dialog_node(
        '2ef6b1f4-9936-479f-af70-c6863e6e2725',
        'b2d0a1d2-a0c1-8716-943b-45c873e58554',
        [kiss_nested_dialog_exit_node_uuid],
        checkflags = (
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_DRAGONBORN, True, slot_idx_tav),
            )),
            bg3.flag_group('Global', (
                bg3.flag(Shadowheart_Turned_Away_From_Shar.uuid, True, None),
            )),
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_Kiss_VersionC, True, slot_idx_shadowheart),
            ))
        ),
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_Kiss_EndRandom, False, slot_idx_shadowheart),
            )),
        )
    )
    d.create_alias_dialog_node(
        'b4d1a14d-6f01-40cc-9eb2-8b6f99ad7ce6',
        '8449fe59-b9ef-c695-1f8e-4af4d7b1adad',
        [kiss_nested_dialog_exit_node_uuid],
        checkflags = (
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_DRAGONBORN, True, slot_idx_tav),
            )),
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_Kiss_VersionC, True, slot_idx_shadowheart),
            ))
        ),
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_Kiss_EndRandom, False, slot_idx_shadowheart),
            )),
        )
    )
    d.create_alias_dialog_node(
        '2173b8c0-2e20-4419-bc1a-734b351327c9',
        'f2a7d192-4dbb-4c6a-2cc5-3702a0917c2b',
        [kiss_nested_dialog_exit_node_uuid],
        checkflags = (
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_DRAGONBORN, True, slot_idx_tav),
            )),
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_Kiss_VersionD, True, slot_idx_shadowheart),
            ))
        ),
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_Kiss_EndRandom, False, slot_idx_shadowheart),
            )),
        )
    )
    d.add_child_dialog_node(kiss_nested_dialog_root_node_uuid, '5f0cec3f-92b4-4f50-90cc-343977ef3992')
    d.add_child_dialog_node(kiss_nested_dialog_root_node_uuid, 'f2f0aaea-20ea-464c-9d46-58e9d238c54a')
    d.add_child_dialog_node(kiss_nested_dialog_root_node_uuid, 'e59b0566-fc67-4130-9ce3-76c2182618c7')
    d.add_child_dialog_node(kiss_nested_dialog_root_node_uuid, '2ef6b1f4-9936-479f-af70-c6863e6e2725')
    d.add_child_dialog_node(kiss_nested_dialog_root_node_uuid, 'b4d1a14d-6f01-40cc-9eb2-8b6f99ad7ce6')
    d.add_child_dialog_node(kiss_nested_dialog_root_node_uuid, '2173b8c0-2e20-4419-bc1a-734b351327c9')

    # Strong body type
    d.create_alias_dialog_node(
        '989dd13e-7180-4b7f-88e0-73add63e37fd',
        '27966d84-2797-3c76-a194-4ff46f1ceb51',
        [kiss_nested_dialog_exit_node_uuid],
        checkflags = (
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_BODYTYPE_STRONG, True, slot_idx_tav),
            )),
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_Kiss_VersionA, True, slot_idx_shadowheart),
            ))
        ),
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_Kiss_EndRandom, False, slot_idx_shadowheart),
            )),
        )
    )
    d.create_alias_dialog_node(
        '6b28ea73-a974-4734-8767-d404507984ab',
        '0866f9b0-0661-049a-68cf-3fee75dd975f',
        [kiss_nested_dialog_exit_node_uuid],
        checkflags = (
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_BODYTYPE_STRONG, True, slot_idx_tav),
            )),
            bg3.flag_group('Global', (
                bg3.flag(Shadowheart_Turned_Away_From_Shar.uuid, True, None),
            )),
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_Kiss_VersionB, True, slot_idx_shadowheart),
            ))
        ),
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_Kiss_EndRandom, False, slot_idx_shadowheart),
            )),
        )
    )
    d.create_alias_dialog_node(
        '2a8e29eb-b517-4724-8a12-c97a6916fa41',
        '1c8219d9-0968-f5ee-850b-718d7475c3e6',
        [kiss_nested_dialog_exit_node_uuid],
        checkflags = (
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_BODYTYPE_STRONG, True, slot_idx_tav),
            )),
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_Kiss_VersionB, True, slot_idx_shadowheart),
            ))
        ),
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_Kiss_EndRandom, False, slot_idx_shadowheart),
            )),
        )
    )
    d.create_alias_dialog_node(
        'd20b131a-8092-4411-9f8a-83d8bf36d8fc',
        '6846f52c-f84c-1301-3c90-8e5af97cdfdc',
        [kiss_nested_dialog_exit_node_uuid],
        checkflags = (
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_BODYTYPE_STRONG, True, slot_idx_tav),
            )),
            bg3.flag_group('Global', (
                bg3.flag(Shadowheart_Turned_Away_From_Shar.uuid, True, None),
            )),
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_Kiss_VersionC, True, slot_idx_shadowheart),
            ))
        ),
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_Kiss_EndRandom, False, slot_idx_shadowheart),
            )),
        )
    )
    d.create_alias_dialog_node(
        '00693a73-00a8-4f05-8f62-8ac4180f7fea',
        '6df05a7c-ba69-56d4-d006-5bc5d749887f',
        [kiss_nested_dialog_exit_node_uuid],
        checkflags = (
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_BODYTYPE_STRONG, True, slot_idx_tav),
            )),
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_Kiss_VersionC, True, slot_idx_shadowheart),
            ))
        ),
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_Kiss_EndRandom, False, slot_idx_shadowheart),
            )),
        )
    )
    d.create_alias_dialog_node(
        '5957be7b-89da-4daa-8b0d-90921af9c810',
        '348eb539-29ef-d53f-2888-259886dd0215',
        [kiss_nested_dialog_exit_node_uuid],
        checkflags = (
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_BODYTYPE_STRONG, True, slot_idx_tav),
            )),
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_Kiss_VersionD, True, slot_idx_shadowheart),
            ))
        ),
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_Kiss_EndRandom, False, slot_idx_shadowheart),
            )),
        )
    )
    d.add_child_dialog_node(kiss_nested_dialog_root_node_uuid, '27966d84-2797-3c76-a194-4ff46f1ceb51')
    d.add_child_dialog_node(kiss_nested_dialog_root_node_uuid, '6b28ea73-a974-4734-8767-d404507984ab')
    d.add_child_dialog_node(kiss_nested_dialog_root_node_uuid, '2a8e29eb-b517-4724-8a12-c97a6916fa41')
    d.add_child_dialog_node(kiss_nested_dialog_root_node_uuid, 'd20b131a-8092-4411-9f8a-83d8bf36d8fc')
    d.add_child_dialog_node(kiss_nested_dialog_root_node_uuid, '00693a73-00a8-4f05-8f62-8ac4180f7fea')
    d.add_child_dialog_node(kiss_nested_dialog_root_node_uuid, '5957be7b-89da-4daa-8b0d-90921af9c810')

    # Female
    d.create_alias_dialog_node(
        'e125eaf8-dce2-43eb-9476-cd1d9b00ee6e',
        '2e786fd7-bbc4-df6b-0df2-e8413461e992',
        [kiss_nested_dialog_exit_node_uuid],
        checkflags = (
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_FEMALE, True, slot_idx_tav),
            )),
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_Kiss_VersionA, True, slot_idx_shadowheart),
            ))
        ),
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_Kiss_EndRandom, False, slot_idx_shadowheart),
            )),
        )
    )
    d.create_alias_dialog_node(
        'cbc1c0af-0ba1-4eee-8508-f5520d093df6',
        '67685b15-4a85-9cc0-2bbd-830057576453',
        [kiss_nested_dialog_exit_node_uuid],
        checkflags = (
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_FEMALE, True, slot_idx_tav),
            )),
            bg3.flag_group('Global', (
                bg3.flag(Shadowheart_Turned_Away_From_Shar.uuid, True, None),
            )),
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_Kiss_VersionB, True, slot_idx_shadowheart),
            ))
        ),
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_Kiss_EndRandom, False, slot_idx_shadowheart),
            )),
        )
    )
    d.create_alias_dialog_node(
        '17cd5eb2-cb01-4665-9e14-198292d54217',
        '0f0cdfa6-9d87-0378-a11b-a150f263c20f',
        [kiss_nested_dialog_exit_node_uuid],
        checkflags = (
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_FEMALE, True, slot_idx_tav),
            )),
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_Kiss_VersionB, True, slot_idx_shadowheart),
            ))
        ),
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_Kiss_EndRandom, False, slot_idx_shadowheart),
            )),
        )
    )
    d.create_alias_dialog_node(
        'fe0a0c90-43bb-4531-99dc-ebb7c5b21398',
        'a075864d-1599-3e49-488c-9352becb96ad',
        [kiss_nested_dialog_exit_node_uuid],
        checkflags = (
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_FEMALE, True, slot_idx_tav),
            )),
            bg3.flag_group('Global', (
                bg3.flag(Shadowheart_Turned_Away_From_Shar.uuid, True, None),
            )),
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_Kiss_VersionC, True, slot_idx_shadowheart),
            ))
        ),
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_Kiss_EndRandom, False, slot_idx_shadowheart),
            )),
        )
    )
    d.create_alias_dialog_node(
        '30f4c0a5-12a9-4d9a-84da-75eadef3227b',
        'd5a7a82e-5605-d625-1bde-1164a5e03315',
        [kiss_nested_dialog_exit_node_uuid],
        checkflags = (
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_FEMALE, True, slot_idx_tav),
            )),
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_Kiss_VersionC, True, slot_idx_shadowheart),
            ))
        ),
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_Kiss_EndRandom, False, slot_idx_shadowheart),
            )),
        )
    )
    d.create_alias_dialog_node(
        'd9d5e7a9-45b9-4e51-846e-8228138c6503',
        '801d3007-d326-ead4-716d-923a87c1e03e',
        [kiss_nested_dialog_exit_node_uuid],
        checkflags = (
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_FEMALE, True, slot_idx_tav),
            )),
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_Kiss_VersionA, True, slot_idx_shadowheart),
            ))
        ),
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_Kiss_EndRandom, False, slot_idx_shadowheart),
            )),
        )
    )
    d.add_child_dialog_node(kiss_nested_dialog_root_node_uuid, 'e125eaf8-dce2-43eb-9476-cd1d9b00ee6e')
    d.add_child_dialog_node(kiss_nested_dialog_root_node_uuid, 'cbc1c0af-0ba1-4eee-8508-f5520d093df6')
    d.add_child_dialog_node(kiss_nested_dialog_root_node_uuid, '17cd5eb2-cb01-4665-9e14-198292d54217')
    d.add_child_dialog_node(kiss_nested_dialog_root_node_uuid, 'fe0a0c90-43bb-4531-99dc-ebb7c5b21398')
    d.add_child_dialog_node(kiss_nested_dialog_root_node_uuid, '30f4c0a5-12a9-4d9a-84da-75eadef3227b')
    d.add_child_dialog_node(kiss_nested_dialog_root_node_uuid, 'd9d5e7a9-45b9-4e51-846e-8228138c6503')

    # Male
    d.create_alias_dialog_node(
        'c1139b8d-c791-4091-b69d-c3899702fae6',
        '5f5e750e-d2e2-4e2e-90fe-e6f7fc8eea71',
        [kiss_nested_dialog_exit_node_uuid],
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_Kiss_VersionA, True, slot_idx_shadowheart),
            )),
        ),
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_Kiss_EndRandom, False, slot_idx_shadowheart),
            )),
        )
    )
    d.create_alias_dialog_node(
        '81210836-ff01-40c4-aad2-9560fa9fe8bd',
        '835d0310-5eca-d609-2845-b6692e047f80',
        [kiss_nested_dialog_exit_node_uuid],
        checkflags = (
            bg3.flag_group('Global', (
                bg3.flag(Shadowheart_Turned_Away_From_Shar.uuid, True, None),
            )),
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_Kiss_VersionB, True, slot_idx_shadowheart),
            )),
        ),
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_Kiss_EndRandom, False, slot_idx_shadowheart),
            )),
        )
    )
    d.create_alias_dialog_node(
        'f341f0af-8dff-4b2f-8df2-b69ae5308f76',
        '0dffa14a-c979-c806-3edf-6313dab6e589',
        [kiss_nested_dialog_exit_node_uuid],
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_Kiss_VersionB, True, slot_idx_shadowheart),
            )),
        ),
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_Kiss_EndRandom, False, slot_idx_shadowheart),
            )),
        )
    )
    d.create_alias_dialog_node(
        '0174633d-ab54-4a44-912a-c8666d28ea1f',
        'bd660b28-e92c-2ea0-2303-dd1fb33a8cc8',
        [kiss_nested_dialog_exit_node_uuid],
        checkflags = (
            bg3.flag_group('Global', (
                bg3.flag(Shadowheart_Turned_Away_From_Shar.uuid, True, None),
            )),
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_Kiss_VersionC, True, slot_idx_shadowheart),
            ))
        ),
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_Kiss_EndRandom, False, slot_idx_shadowheart),
            )),
        )
    )
    d.create_alias_dialog_node(
        'b713ad19-66d2-4266-b318-e0970e5f2748',
        'e78d9f78-9dee-6a1c-63c6-8b06ec82c2bc',
        [kiss_nested_dialog_exit_node_uuid],
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_Kiss_VersionC, True, slot_idx_shadowheart),
            )),
        ),
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_Kiss_EndRandom, False, slot_idx_shadowheart),
            )),
        )
    )
    d.create_alias_dialog_node(
        '96a6f7d6-a5f2-489d-8576-4de27fcb152c',
        'ccddbf44-b77d-ba97-54f4-a3332ca49b4b',
        [kiss_nested_dialog_exit_node_uuid],
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_Kiss_VersionD, True, slot_idx_shadowheart),
            )),
        ),
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_Kiss_EndRandom, False, slot_idx_shadowheart),
            )),
        )
    )
    d.add_child_dialog_node(kiss_nested_dialog_root_node_uuid, 'c1139b8d-c791-4091-b69d-c3899702fae6')
    d.add_child_dialog_node(kiss_nested_dialog_root_node_uuid, '81210836-ff01-40c4-aad2-9560fa9fe8bd')
    d.add_child_dialog_node(kiss_nested_dialog_root_node_uuid, 'f341f0af-8dff-4b2f-8df2-b69ae5308f76')
    d.add_child_dialog_node(kiss_nested_dialog_root_node_uuid, '0174633d-ab54-4a44-912a-c8666d28ea1f')
    d.add_child_dialog_node(kiss_nested_dialog_root_node_uuid, 'b713ad19-66d2-4266-b318-e0970e5f2748')
    d.add_child_dialog_node(kiss_nested_dialog_root_node_uuid, '96a6f7d6-a5f2-489d-8576-4de27fcb152c')


    ###############################################################
    # Add more kisses
    ###############################################################

    lword_kiss_bt1_node_uuid = '0b6b7ad3-abeb-4f70-8d2e-97c830ab74bb'
    lword_kiss_bt2_node_uuid = '56e3dde5-4509-47f1-8861-09a2987c1a27'
    lword_kiss_bt34_node_uuid = 'e0f3af31-505a-410c-bfd8-3356cf731054'
    lword_kiss_dragonborn_node_uuid = '7442ec99-552b-40bf-a695-8c8e0a02677a'
    lword_kiss_short_node_uuid = '22c3b18f-fe5a-4c4f-927d-442b37d683f0'
    lword_kiss_dwarf_node_uuid = '6e216e67-9e5a-4cd5-8e3d-b7e925973877'

    d.create_standard_dialog_node(
        lword_kiss_bt1_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [kiss_nested_dialog_exit_node_uuid],
        bg3.text_content('h5cf45132g69fdg45ceg9483g7b67354eb3ec', 1),
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(ORI_ShadowheartKiss_LoveYou.uuid, True, slot_idx_shadowheart),
            )),
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_FEMALE, True, slot_idx_tav),
            )),
        ),
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(ORI_ShadowheartKiss_LoveYou.uuid, False, slot_idx_shadowheart),
            )),
        ))
    create_lword_kiss_bt1_timeline(d, t, lword_kiss_bt1_node_uuid)

    d.create_standard_dialog_node(
        lword_kiss_bt2_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [kiss_nested_dialog_exit_node_uuid],
        bg3.text_content('h5cf45132g69fdg45ceg9483g7b67354eb3ec', 1),
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(ORI_ShadowheartKiss_LoveYou.uuid, True, slot_idx_shadowheart),
            )),
        ),
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(ORI_ShadowheartKiss_LoveYou.uuid, False, slot_idx_shadowheart),
            )),
        ))
    create_lword_kiss_bt2_timeline(d, t, lword_kiss_bt2_node_uuid)

    d.create_standard_dialog_node(
        lword_kiss_bt34_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [kiss_nested_dialog_exit_node_uuid],
        bg3.text_content('h5cf45132g69fdg45ceg9483g7b67354eb3ec', 1),
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(ORI_ShadowheartKiss_LoveYou.uuid, True, slot_idx_shadowheart),
            )),
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_BODYTYPE_STRONG, True, slot_idx_tav),
            )),
        ),
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(ORI_ShadowheartKiss_LoveYou.uuid, False, slot_idx_shadowheart),
            )),
        ))
    create_lword_kiss_bt34_timeline(d, t, lword_kiss_bt34_node_uuid)

    d.create_standard_dialog_node(
        lword_kiss_dragonborn_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [kiss_nested_dialog_exit_node_uuid],
        bg3.text_content('h5cf45132g69fdg45ceg9483g7b67354eb3ec', 1),
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(ORI_ShadowheartKiss_LoveYou.uuid, True, slot_idx_shadowheart),
            )),
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_DRAGONBORN, True, slot_idx_tav),
            )),
        ),
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(ORI_ShadowheartKiss_LoveYou.uuid, False, slot_idx_shadowheart),
            )),
        ))
    create_lword_kiss_dragonborn_timeline(d, t, lword_kiss_dragonborn_node_uuid)

    d.create_standard_dialog_node(
        lword_kiss_short_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [kiss_nested_dialog_exit_node_uuid],
        bg3.text_content('h5cf45132g69fdg45ceg9483g7b67354eb3ec', 1),
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(ORI_ShadowheartKiss_LoveYou.uuid, True, slot_idx_shadowheart),
            )),
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_SHORT, True, slot_idx_tav),
            )),
        ),
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(ORI_ShadowheartKiss_LoveYou.uuid, False, slot_idx_shadowheart),
            )),
        ))
    create_lword_kiss_short_timeline(d, t, lword_kiss_short_node_uuid)

    d.create_standard_dialog_node(
        lword_kiss_dwarf_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [kiss_nested_dialog_exit_node_uuid],
        bg3.text_content('h5cf45132g69fdg45ceg9483g7b67354eb3ec', 1),
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(ORI_ShadowheartKiss_LoveYou.uuid, True, slot_idx_shadowheart),
            )),
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_DWARF, True, slot_idx_tav),
            )),
        ),
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(ORI_ShadowheartKiss_LoveYou.uuid, False, slot_idx_shadowheart),
            )),
        ))
    create_lword_kiss_dwarf_timeline(d, t, lword_kiss_dwarf_node_uuid)


    d.add_child_dialog_node(kiss_nested_dialog_root_node_uuid, lword_kiss_dwarf_node_uuid)
    d.add_child_dialog_node(kiss_nested_dialog_root_node_uuid, lword_kiss_short_node_uuid)
    d.add_child_dialog_node(kiss_nested_dialog_root_node_uuid, lword_kiss_dragonborn_node_uuid)
    d.add_child_dialog_node(kiss_nested_dialog_root_node_uuid, lword_kiss_bt34_node_uuid)
    d.add_child_dialog_node(kiss_nested_dialog_root_node_uuid, lword_kiss_bt1_node_uuid)
    d.add_child_dialog_node(kiss_nested_dialog_root_node_uuid, lword_kiss_bt2_node_uuid)

    ###############################################################
    # Timeline: ShadowHeart_InParty2_Nested_ShadowheartKiss.lsf
    # White hair fix for kisses
    # No longer needed since Hotfix 28
    ###############################################################

    # Removal of TLShowArmor nodes doesn't break cutscenes and prevents hair color change
    # t = bg3.timeline_object(files.get_file('Gustav', 'Public/GustavDev/Timeline/Generated/ShadowHeart_InParty2_Nested_ShadowheartKiss.lsf'), d)
    # show_armor_comps = []
    # for effect_component in t.all_effect_components:
    #    if bg3.get_required_bg3_attribute(effect_component, "Type") == "TLShowArmor":
    #        show_armor_comps.append(effect_component)
    # for effect_component in show_armor_comps:
    #    t.remove_effect_component(effect_component)

    # t.update_duration()

    ###############################################################
    # Dialog: ShadowHeart_InParty2_Nested_DefaultChapter.lsf
    # Use the new flag that enables all 6 kiss animations
    ###############################################################

    # d = bg3.dialog_object(files.get_file('Gustav', 'Mods/GustavDev/Story/DialogsBinary/Companions/ShadowHeart_InParty2_Nested_DefaultChapter.lsf'))

    ab = game_assets.get_modded_dialog_asset_bundle('ShadowHeart_InParty2_Nested_DefaultChapter')
    d = bg3.dialog_object(ab.dialog)

    slot_idx_shadowheart = d.get_speaker_slot_index(bg3.SPEAKER_SHADOWHEART)
    shadowheart_random_kiss_start_true = bg3.flag_group('Object', (bg3.flag(ORI_ShadowheartKiss_StartRandom.uuid, True, slot_idx_shadowheart),))

    # Reset the kiss flag, just in case
    greeting_node_uuid = '23749c85-4289-4965-a7db-1909f5cb63a2'
    d.set_dialog_flags(greeting_node_uuid, setflags = (
        bg3.flag_group('Object', (
            bg3.flag(ORI_ShadowheartKiss_StartRandom.uuid, False, slot_idx_shadowheart),
            bg3.flag('22c04792-d5fc-4285-b45d-95c7df986e47', False, slot_idx_shadowheart),
        )),
    ))

    may_i_have_a_kiss_node_uuid = '5752078a-349c-4ba7-b8de-3e9341cb0c9c'
    d.set_dialog_flags(may_i_have_a_kiss_node_uuid, setflags = (shadowheart_random_kiss_start_true,))

    ##############################################################
    # Dialog: ShadowHeart_InParty2_Nested_BackgroundChapter.lsf
    # Shar idol kiss fix
    # Use the new flag that enabled all 6 kiss animations
    ##############################################################

    # d = bg3.dialog_object(files.get_file('Gustav', 'Mods/GustavDev/Story/DialogsBinary/Companions/ShadowHeart_InParty2_Nested_BackgroundChapter.lsf'))

    ab = game_assets.get_modded_dialog_asset_bundle('ShadowHeart_InParty2_Nested_BackgroundChapter')
    d = bg3.dialog_object(ab.dialog)

    slot_idx_tav = d.get_speaker_slot_index(bg3.SPEAKER_PLAYER)
    slot_idx_shadowheart = d.get_speaker_slot_index(bg3.SPEAKER_SHADOWHEART)
    shadowheart_random_kiss_start_true = bg3.flag_group('Object', (bg3.flag(ORI_ShadowheartKiss_StartRandom.uuid, True, slot_idx_shadowheart),))


    #
    # Shar Idol kisses
    #
    kiss_me_like_you_hate_me_node_uuid = '8203a694-02be-4f2a-8059-e9b1cbc55b2f'
    d.set_dialog_flags(kiss_me_like_you_hate_me_node_uuid, setflags = (
        bg3.flag_group('Object', (
            bg3.flag(bg3.FLAG_ORI_Kiss_StartRandom, True, slot_idx_shadowheart),
        )),
    ))

    and_a_kiss_of_course_node_uuid = '24c10a92-b14e-4610-8786-b8756cfdecba'
    d.set_dialog_flags(and_a_kiss_of_course_node_uuid, setflags = (
        bg3.flag_group('Object', (
            bg3.flag(bg3.FLAG_ORI_Kiss_StartRandom, True, slot_idx_shadowheart),
        )),
    ))

    i_suppose_we_can_manage_that_node_uuid = '1f06b486-f426-44bc-8b1d-a049be8b5ad0'
    d.set_dialog_flags(i_suppose_we_can_manage_that_node_uuid, setflags = (
        bg3.flag_group('Object', (
            bg3.flag(bg3.FLAG_ORI_Kiss_StartRandom, True, slot_idx_shadowheart),
        )),
    ))

    #
    # Kiss when Tav/Durge are not Selunite, but dating her
    #
    ill_settle_for_a_kiss_node_uuid = '322da54c-e895-4ac6-9e38-24367d312fee'
    d.create_standard_dialog_node(
        ill_settle_for_a_kiss_node_uuid,
        bg3.SPEAKER_PLAYER,
        ['1f06b486-f426-44bc-8b1d-a049be8b5ad0'],
        bg3.text_content('hc9d545e9g2d2dg4e58g8ba5gf605bea98e1e', 1),
        constructor=bg3.dialog_object.QUESTION,
        setflags=(
            shadowheart_random_kiss_start_true,
        ),
        checkflags=(
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_State_DatingShadowheart, True, slot_idx_tav),
                bg3.flag(bg3.FLAG_ORI_State_PartneredWithShadowheart, False, slot_idx_tav),
            )),
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_SHADOWHEART, True, slot_idx_shadowheart),
            )),
        ))
    d.add_child_dialog_node('53a5af9f-2f3d-4698-b854-ec3265f910d2', ill_settle_for_a_kiss_node_uuid)


def create_new_kisses() -> None:
    game_assets = get_context().assets


    # #
    # # Shadowheart_InParty2_Nested_ShadowheartKiss
    # #

    # ab = game_assets.get_modded_dialog_asset_bundle('ShadowHeart_InParty2_Nested_ShadowheartKiss')
    # d = bg3.dialog_object(ab.dialog)
    # t = bg3.timeline_object(ab.timeline, d)

    # speaker_idx_shadowheart = d.get_speaker_slot_index(bg3.SPEAKER_SHADOWHEART)

    # karlach_kiss_a_node_uuid = 'd60052e9-e8a3-432c-ac80-6dddb75cc679'
    # karlach_kiss_b_node_uuid = 'bd03ca1c-3d74-4d0f-9ee2-b16e9ea38ebd'
    # karlach_kiss_c_node_uuid = '30dee453-ad5a-441f-ba42-51219d43de84'
    # karlach_kiss_d_node_uuid = '819f917c-457c-4a76-b90a-8245772ad96d'

    # minthara_kiss_a_node_uuid = '9fad7df8-9954-42dc-a697-7cee7b94b347'
    # minthara_kiss_b_node_uuid = 'a47887d4-6f84-4a44-b6b9-e7587ac2f541'
    # minthara_kiss_c_node_uuid = 'd3bd8b00-6343-46d4-ab3a-7820b3d227b9'
    # minthara_kiss_d_node_uuid = 'a73a8ac1-0607-4585-b4aa-15969b872817'

    # jump_to_new_kiss_dialog_node_uuid = '74b3bec7-1b30-4fa1-99bc-a6607d21d677'
    # new_kiss_nested_dialog_node_uuid = 'ca93806f-e08a-4493-9726-8f4e5fa5dfb9'

    # d.create_jump_dialog_node(jump_to_new_kiss_dialog_node_uuid, new_kiss_nested_dialog_node_uuid, 2)

    # d.create_nested_dialog_node(
    #     new_kiss_nested_dialog_node_uuid,
    #     new_kiss_nested_dialog_uuid,
    #     [kiss_nested_dialog_exit_node_uuid],
    #     speaker_count = 2)

    # d.create_standard_dialog_node(
    #     karlach_kiss_a_node_uuid,
    #     bg3.SPEAKER_PLAYER,
    #     [jump_to_new_kiss_dialog_node_uuid],
    #     None,
    #     checkflags = (
    #         bg3.flag_group('Object', (
    #             bg3.flag(Karlach_Kiss_A.uuid, True, speaker_idx_shadowheart),
    #         )),
    #     ))
    # d.create_standard_dialog_node(
    #     karlach_kiss_b_node_uuid,
    #     bg3.SPEAKER_PLAYER,
    #     [jump_to_new_kiss_dialog_node_uuid],
    #     None,
    #     checkflags = (
    #         bg3.flag_group('Object', (
    #             bg3.flag(Karlach_Kiss_B.uuid, True, speaker_idx_shadowheart),
    #         )),
    #     ))
    # d.create_standard_dialog_node(
    #     karlach_kiss_c_node_uuid,
    #     bg3.SPEAKER_PLAYER,
    #     [jump_to_new_kiss_dialog_node_uuid],
    #     None,
    #     checkflags = (
    #         bg3.flag_group('Object', (
    #             bg3.flag(Karlach_Kiss_C.uuid, True, speaker_idx_shadowheart),
    #         )),
    #     ))
    # d.create_standard_dialog_node(
    #     karlach_kiss_d_node_uuid,
    #     bg3.SPEAKER_PLAYER,
    #     [jump_to_new_kiss_dialog_node_uuid],
    #     None,
    #     checkflags = (
    #         bg3.flag_group('Object', (
    #             bg3.flag(Karlach_Kiss_D.uuid, True, speaker_idx_shadowheart),
    #         )),
    #     ))

    # d.create_standard_dialog_node(
    #     minthara_kiss_a_node_uuid,
    #     bg3.SPEAKER_PLAYER,
    #     [jump_to_new_kiss_dialog_node_uuid],
    #     None,
    #     checkflags = (
    #         bg3.flag_group('Object', (
    #             bg3.flag(Minthara_Kiss_A.uuid, True, speaker_idx_shadowheart),
    #         )),
    #     ))
    # d.create_standard_dialog_node(
    #     minthara_kiss_b_node_uuid,
    #     bg3.SPEAKER_PLAYER,
    #     [jump_to_new_kiss_dialog_node_uuid],
    #     None,
    #     checkflags = (
    #         bg3.flag_group('Object', (
    #             bg3.flag(Minthara_Kiss_B.uuid, True, speaker_idx_shadowheart),
    #         )),
    #     ))
    # d.create_standard_dialog_node(
    #     minthara_kiss_c_node_uuid,
    #     bg3.SPEAKER_PLAYER,
    #     [jump_to_new_kiss_dialog_node_uuid],
    #     None,
    #     checkflags = (
    #         bg3.flag_group('Object', (
    #             bg3.flag(Minthara_Kiss_C.uuid, True, speaker_idx_shadowheart),
    #         )),
    #     ))
    # d.create_standard_dialog_node(
    #     minthara_kiss_d_node_uuid,
    #     bg3.SPEAKER_PLAYER,
    #     [jump_to_new_kiss_dialog_node_uuid],
    #     None,
    #     checkflags = (
    #         bg3.flag_group('Object', (
    #             bg3.flag(Minthara_Kiss_D.uuid, True, speaker_idx_shadowheart),
    #         )),
    #     ))

    # d.add_child_dialog_node(kiss_nested_dialog_root_node_uuid, minthara_kiss_d_node_uuid, 0)
    # d.add_child_dialog_node(kiss_nested_dialog_root_node_uuid, minthara_kiss_c_node_uuid, 0)
    # d.add_child_dialog_node(kiss_nested_dialog_root_node_uuid, minthara_kiss_b_node_uuid, 0)
    # d.add_child_dialog_node(kiss_nested_dialog_root_node_uuid, minthara_kiss_a_node_uuid, 0)

    # d.add_child_dialog_node(kiss_nested_dialog_root_node_uuid, karlach_kiss_d_node_uuid, 0)
    # d.add_child_dialog_node(kiss_nested_dialog_root_node_uuid, karlach_kiss_c_node_uuid, 0)
    # d.add_child_dialog_node(kiss_nested_dialog_root_node_uuid, karlach_kiss_b_node_uuid, 0)
    # d.add_child_dialog_node(kiss_nested_dialog_root_node_uuid, karlach_kiss_a_node_uuid, 0)

    #
    # Shadowheart_InParty2_Nested_ShadowheartKissNew
    #

    nested_ab = game_assets.create_new_empty_dialog_from_another(
        'ShadowHeart_InParty2_Nested_ShadowheartKiss',
        'Shadowheart_InParty2_Nested_ShadowheartKissNew',
        new_kiss_nested_dialog_uuid,
        '6b38b5a7-b210-4cea-8e3e-1c9f59b9b48e',
        subfolder = 'ReallyShadowheart')
    parent_dialog_uuid = game_assets.get_modded_dialog_asset_bundle('ShadowHeart_InParty2_Nested_DefaultChapter').modded_dialog_uuid
    game_assets.append_dependency_to_dialog(parent_dialog_uuid, new_kiss_nested_dialog_uuid)
    d = bg3.dialog_object(nested_ab.dialog)
    t = bg3.timeline_object(nested_ab.timeline, d)
    kiss_root_node_uuid = '63ba27ca-7608-4e4a-92f1-bf9f1fc6446c'

    t.pad_timeline()

    d.create_standard_dialog_node(
        kiss_root_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [],
        None)
    d.add_root_node(kiss_root_node_uuid)

    minthara_bt1_kiss_A_node_uuid = '8a509fea-da01-4d78-946c-dedbfa12052c'
    minthara_bt1_kiss_B_node_uuid = '1554eec5-b7a2-41cf-995d-86be27692721'
    minthara_bt1_kiss_C_node_uuid = '1e4f3fdb-28d4-4cbb-a070-712db76f2179'
    minthara_bt1_kiss_D_node_uuid = 'e56dc596-f9a7-4b3e-b5ec-461a8da4a570'

    karlach_bt3_kiss_A_node_uuid = 'ba43f684-e26b-451e-8774-36e65ad137d7'
    karlach_bt3_kiss_B_node_uuid = '834eb846-70fe-4dac-805b-85898e112ef1'
    karlach_bt3_kiss_C_node_uuid = 'aeffb898-8ff7-4e2e-93d0-d2c8168989fe'
    karlach_bt3_kiss_D_node_uuid = 'f185976e-4db3-40db-901b-e5d0713560f2'

    karlach_bt2_kiss_A_node_uuid = '0c92978f-23d3-42a2-b351-a5b68b9f5e94'
    karlach_bt2_kiss_B_node_uuid = 'c442f602-8d0f-4611-ad42-b5ddccee57d4'
    karlach_bt2_kiss_C_node_uuid = '7909780c-255e-45bf-bef1-dc5acecf85b4'
    karlach_bt2_kiss_D_node_uuid = '03c7d41e-9e6c-4f5d-a4b1-93e565bbaf6c'

    karlach_bt2_gith_kiss_A_node_uuid = '2eef68b1-4f40-4e3b-a4a0-1c2ec2797648'
    karlach_bt2_gith_kiss_B_node_uuid = 'e58886a3-c732-409c-9d7d-66cae4d4b94b'
    karlach_bt2_gith_kiss_C_node_uuid = '59ea7fe1-5341-4d43-bf02-069a56ed08eb'
    karlach_bt2_gith_kiss_D_node_uuid = 'd7c9a05d-f1f5-442d-8f28-baa628d3f335'

    end_nested_kiss_node_uuid = '3ae1c83a-040a-4bfb-b411-51a3becca8ab'

    speaker_idx_shadowheart = d.get_speaker_slot_index(bg3.SPEAKER_SHADOWHEART)
    speaker_idx_tav = d.get_speaker_slot_index(bg3.SPEAKER_PLAYER)

    d.create_standard_dialog_node(
        end_nested_kiss_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [],
        None,
        end_node = True,
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(Karlach_Kiss_A.uuid, False, speaker_idx_shadowheart),
                bg3.flag(Karlach_Kiss_B.uuid, False, speaker_idx_shadowheart),
                bg3.flag(Karlach_Kiss_C.uuid, False, speaker_idx_shadowheart),
                bg3.flag(Karlach_Kiss_D.uuid, False, speaker_idx_shadowheart),
                bg3.flag(Minthara_Kiss_A.uuid, False, speaker_idx_shadowheart),
                bg3.flag(Minthara_Kiss_B.uuid, False, speaker_idx_shadowheart),
                bg3.flag(Minthara_Kiss_C.uuid, False, speaker_idx_shadowheart),
                bg3.flag(Minthara_Kiss_D.uuid, False, speaker_idx_shadowheart),
            )),
        ))

    #
    # Minthara kisses
    #

    # Kiss A
    d.create_cinematic_dialog_node(
        minthara_bt1_kiss_A_node_uuid,
        [end_nested_kiss_node_uuid],
        checkflags = (
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_FEMALE, True, speaker_idx_tav),
                bg3.flag(bg3.TAG_BODYTYPE_STRONG, False, speaker_idx_tav),
            )),
            bg3.flag_group('Object', (
                bg3.flag(Minthara_Kiss_A.uuid, True, speaker_idx_shadowheart),
            )),
        ))
    create_minthara_kiss_A_timeline(t, minthara_bt1_kiss_A_node_uuid)

    # Kiss B
    d.create_cinematic_dialog_node(
        minthara_bt1_kiss_B_node_uuid,
        [end_nested_kiss_node_uuid],
        checkflags = (
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_FEMALE, True, speaker_idx_tav),
                bg3.flag(bg3.TAG_BODYTYPE_STRONG, False, speaker_idx_tav),
            )),
            bg3.flag_group('Object', (
                bg3.flag(Minthara_Kiss_B.uuid, True, speaker_idx_shadowheart),
            )),
        ))
    create_minthara_kiss_B_timeline(t, minthara_bt1_kiss_B_node_uuid)

    # Kiss C
    d.create_cinematic_dialog_node(
        minthara_bt1_kiss_C_node_uuid,
        [end_nested_kiss_node_uuid],
        checkflags = (
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_FEMALE, True, speaker_idx_tav),
                bg3.flag(bg3.TAG_BODYTYPE_STRONG, False, speaker_idx_tav),
            )),
            bg3.flag_group('Object', (
                bg3.flag(Minthara_Kiss_C.uuid, True, speaker_idx_shadowheart),
            )),
        ))
    create_minthara_kiss_C_timeline(t, minthara_bt1_kiss_C_node_uuid)

    # Kiss D
    d.create_cinematic_dialog_node(
        minthara_bt1_kiss_D_node_uuid,
        [end_nested_kiss_node_uuid],
        checkflags = (
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_FEMALE, True, speaker_idx_tav),
                bg3.flag(bg3.TAG_BODYTYPE_STRONG, False, speaker_idx_tav),
            )),
            bg3.flag_group('Object', (
                bg3.flag(Minthara_Kiss_D.uuid, True, speaker_idx_shadowheart),
            )),
        ))
    create_minthara_kiss_D_timeline(t, minthara_bt1_kiss_D_node_uuid)


    #
    # Karlach kisses
    #

    # Kiss A
    d.create_cinematic_dialog_node(
        karlach_bt3_kiss_A_node_uuid,
        [end_nested_kiss_node_uuid],
        checkflags = (
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_FEMALE, True, speaker_idx_tav),
                bg3.flag(bg3.TAG_BODYTYPE_STRONG, True, speaker_idx_tav),
            )),
            bg3.flag_group('Object', (
                bg3.flag(Karlach_Kiss_A.uuid, True, speaker_idx_shadowheart),
            )),
        ))
    create_karlach_kiss_A_timeline(t, karlach_bt3_kiss_A_node_uuid, 'bt3')

    # Kiss B
    d.create_cinematic_dialog_node(
        karlach_bt3_kiss_B_node_uuid,
        [end_nested_kiss_node_uuid],
        checkflags = (
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_FEMALE, True, speaker_idx_tav),
                bg3.flag(bg3.TAG_BODYTYPE_STRONG, True, speaker_idx_tav),
            )),
            bg3.flag_group('Object', (
                bg3.flag(Karlach_Kiss_B.uuid, True, speaker_idx_shadowheart),
            )),
        ))
    create_karlach_kiss_B_timeline(t, karlach_bt3_kiss_B_node_uuid, 'bt3')

    # Kiss C
    d.create_cinematic_dialog_node(
        karlach_bt3_kiss_C_node_uuid,
        [end_nested_kiss_node_uuid],
        checkflags = (
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_FEMALE, True, speaker_idx_tav),
                bg3.flag(bg3.TAG_BODYTYPE_STRONG, True, speaker_idx_tav),
            )),
            bg3.flag_group('Object', (
                bg3.flag(Karlach_Kiss_C.uuid, True, speaker_idx_shadowheart),
            )),
        ))
    create_karlach_kiss_C_timeline(t, karlach_bt3_kiss_C_node_uuid, 'bt3')

    # Kiss D
    d.create_cinematic_dialog_node(
        karlach_bt3_kiss_D_node_uuid,
        [end_nested_kiss_node_uuid],
        checkflags = (
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_FEMALE, True, speaker_idx_tav),
                bg3.flag(bg3.TAG_BODYTYPE_STRONG, True, speaker_idx_tav),
            )),
            bg3.flag_group('Object', (
                bg3.flag(Karlach_Kiss_D.uuid, True, speaker_idx_shadowheart),
            )),
        ))
    create_karlach_kiss_D_timeline(t, karlach_bt3_kiss_D_node_uuid, 'bt3')


    # Kiss A
    d.create_cinematic_dialog_node(
        karlach_bt2_kiss_A_node_uuid,
        [end_nested_kiss_node_uuid],
        checkflags = (
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_FEMALE, False, speaker_idx_tav),
                bg3.flag(bg3.TAG_BODYTYPE_STRONG, False, speaker_idx_tav),
                bg3.flag(bg3.TAG_SHORT, False, speaker_idx_tav),
                bg3.flag(bg3.TAG_GITH, False, speaker_idx_tav),
            )),
            bg3.flag_group('Object', (
                bg3.flag(Karlach_Kiss_A.uuid, True, speaker_idx_shadowheart),
            )),
        ))
    create_karlach_kiss_A_timeline(t, karlach_bt2_kiss_A_node_uuid, 'bt2')

    # Kiss B
    d.create_cinematic_dialog_node(
        karlach_bt2_kiss_B_node_uuid,
        [end_nested_kiss_node_uuid],
        checkflags = (
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_FEMALE, False, speaker_idx_tav),
                bg3.flag(bg3.TAG_BODYTYPE_STRONG, False, speaker_idx_tav),
                bg3.flag(bg3.TAG_SHORT, False, speaker_idx_tav),
                bg3.flag(bg3.TAG_GITH, False, speaker_idx_tav),
            )),
            bg3.flag_group('Object', (
                bg3.flag(Karlach_Kiss_B.uuid, True, speaker_idx_shadowheart),
            )),
        ))
    create_karlach_kiss_B_timeline(t, karlach_bt2_kiss_B_node_uuid, 'bt2')

    # Kiss C
    d.create_cinematic_dialog_node(
        karlach_bt2_kiss_C_node_uuid,
        [end_nested_kiss_node_uuid],
        checkflags = (
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_FEMALE, False, speaker_idx_tav),
                bg3.flag(bg3.TAG_BODYTYPE_STRONG, False, speaker_idx_tav),
                bg3.flag(bg3.TAG_SHORT, False, speaker_idx_tav),
                bg3.flag(bg3.TAG_GITH, False, speaker_idx_tav),
            )),
            bg3.flag_group('Object', (
                bg3.flag(Karlach_Kiss_C.uuid, True, speaker_idx_shadowheart),
            )),
        ))
    create_karlach_kiss_C_timeline(t, karlach_bt2_kiss_C_node_uuid, 'bt2')

    # Kiss D
    d.create_cinematic_dialog_node(
        karlach_bt2_kiss_D_node_uuid,
        [end_nested_kiss_node_uuid],
        checkflags = (
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_FEMALE, False, speaker_idx_tav),
                bg3.flag(bg3.TAG_BODYTYPE_STRONG, False, speaker_idx_tav),
                bg3.flag(bg3.TAG_SHORT, False, speaker_idx_tav),
                bg3.flag(bg3.TAG_GITH, False, speaker_idx_tav),
            )),
            bg3.flag_group('Object', (
                bg3.flag(Karlach_Kiss_D.uuid, True, speaker_idx_shadowheart),
            )),
        ))
    create_karlach_kiss_D_timeline(t, karlach_bt2_kiss_D_node_uuid, 'bt2')


    # Kiss A
    d.create_cinematic_dialog_node(
        karlach_bt2_gith_kiss_A_node_uuid,
        [end_nested_kiss_node_uuid],
        checkflags = (
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_FEMALE, False, speaker_idx_tav),
                bg3.flag(bg3.TAG_BODYTYPE_STRONG, False, speaker_idx_tav),
                bg3.flag(bg3.TAG_SHORT, False, speaker_idx_tav),
                bg3.flag(bg3.TAG_GITH, True, speaker_idx_tav),
            )),
            bg3.flag_group('Object', (
                bg3.flag(Karlach_Kiss_A.uuid, True, speaker_idx_shadowheart),
            )),
        ))
    create_karlach_kiss_A_timeline(t, karlach_bt2_gith_kiss_A_node_uuid, 'bt2_gith')

    # Kiss B
    d.create_cinematic_dialog_node(
        karlach_bt2_gith_kiss_B_node_uuid,
        [end_nested_kiss_node_uuid],
        checkflags = (
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_FEMALE, False, speaker_idx_tav),
                bg3.flag(bg3.TAG_BODYTYPE_STRONG, False, speaker_idx_tav),
                bg3.flag(bg3.TAG_SHORT, False, speaker_idx_tav),
                bg3.flag(bg3.TAG_GITH, True, speaker_idx_tav),
            )),
            bg3.flag_group('Object', (
                bg3.flag(Karlach_Kiss_B.uuid, True, speaker_idx_shadowheart),
            )),
        ))
    create_karlach_kiss_B_timeline(t, karlach_bt2_gith_kiss_B_node_uuid, 'bt2_gith')

    # Kiss C
    d.create_cinematic_dialog_node(
        karlach_bt2_gith_kiss_C_node_uuid,
        [end_nested_kiss_node_uuid],
        checkflags = (
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_FEMALE, False, speaker_idx_tav),
                bg3.flag(bg3.TAG_BODYTYPE_STRONG, False, speaker_idx_tav),
                bg3.flag(bg3.TAG_SHORT, False, speaker_idx_tav),
                bg3.flag(bg3.TAG_GITH, True, speaker_idx_tav),
            )),
            bg3.flag_group('Object', (
                bg3.flag(Karlach_Kiss_C.uuid, True, speaker_idx_shadowheart),
            )),
        ))
    create_karlach_kiss_C_timeline(t, karlach_bt2_gith_kiss_C_node_uuid, 'bt2_gith')

    # Kiss D
    d.create_cinematic_dialog_node(
        karlach_bt2_gith_kiss_D_node_uuid,
        [end_nested_kiss_node_uuid],
        checkflags = (
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_FEMALE, False, speaker_idx_tav),
                bg3.flag(bg3.TAG_BODYTYPE_STRONG, False, speaker_idx_tav),
                bg3.flag(bg3.TAG_SHORT, False, speaker_idx_tav),
                bg3.flag(bg3.TAG_GITH, True, speaker_idx_tav),
            )),
            bg3.flag_group('Object', (
                bg3.flag(Karlach_Kiss_D.uuid, True, speaker_idx_shadowheart),
            )),
        ))
    create_karlach_kiss_D_timeline(t, karlach_bt2_gith_kiss_D_node_uuid, 'bt2_gith')


    d.add_child_dialog_node(kiss_root_node_uuid, karlach_bt2_gith_kiss_A_node_uuid, 0)
    d.add_child_dialog_node(kiss_root_node_uuid, karlach_bt2_gith_kiss_B_node_uuid, 0)
    d.add_child_dialog_node(kiss_root_node_uuid, karlach_bt2_gith_kiss_C_node_uuid, 0)
    d.add_child_dialog_node(kiss_root_node_uuid, karlach_bt2_gith_kiss_D_node_uuid, 0)

    d.add_child_dialog_node(kiss_root_node_uuid, karlach_bt2_kiss_A_node_uuid, 0)
    d.add_child_dialog_node(kiss_root_node_uuid, karlach_bt2_kiss_B_node_uuid, 0)
    d.add_child_dialog_node(kiss_root_node_uuid, karlach_bt2_kiss_C_node_uuid, 0)
    d.add_child_dialog_node(kiss_root_node_uuid, karlach_bt2_kiss_D_node_uuid, 0)

    d.add_child_dialog_node(kiss_root_node_uuid, karlach_bt3_kiss_A_node_uuid, 0)
    d.add_child_dialog_node(kiss_root_node_uuid, karlach_bt3_kiss_B_node_uuid, 0)
    d.add_child_dialog_node(kiss_root_node_uuid, karlach_bt3_kiss_C_node_uuid, 0)
    d.add_child_dialog_node(kiss_root_node_uuid, karlach_bt3_kiss_D_node_uuid, 0)

    d.add_child_dialog_node(kiss_root_node_uuid, minthara_bt1_kiss_A_node_uuid, 0)
    d.add_child_dialog_node(kiss_root_node_uuid, minthara_bt1_kiss_B_node_uuid, 0)
    d.add_child_dialog_node(kiss_root_node_uuid, minthara_bt1_kiss_C_node_uuid, 0)
    d.add_child_dialog_node(kiss_root_node_uuid, minthara_bt1_kiss_D_node_uuid, 0)


def add_new_kisses() -> None:
    game_assets = get_context().assets

    shadowheart_kiss_nested_dialog_uuid = game_assets.get_modded_dialog_asset_bundle('ShadowHeart_InParty2_Nested_ShadowheartKiss').modded_dialog_uuid

    ###############################################################
    # Dialog: ShadowHeart_InParty2_Nested_DefaultChapter.lsf
    ###############################################################
    ab = game_assets.get_modded_dialog_asset_bundle('ShadowHeart_InParty2_Nested_DefaultChapter')
    d = bg3.dialog_object(ab.dialog)

    speaker_idx_shadowheart = d.get_speaker_slot_index(bg3.SPEAKER_SHADOWHEART)

    # 5e26cf5f-ff2f-4ab8-8281-e8462d1c8655 -> 59d6dab0-dd97-7cac-8198-88d4e49b2394 # selunite
    # a109176e-8c92-471a-aeee-402b841b00cb -> 47eaa218-721a-446a-94fc-62895c1ce704 # DJ
    # 0efd0066-4d38-4797-b51c-4fad103cba3d -> ebae4805-558c-44ce-b24a-186b823f34a4 # love you kiss
    # 92f6ac2c-5e84-4ea8-8939-e65ff32ed9b5 -> 3192580f-34ca-4a9b-88b3-1e292b2f594e # confession kiss

    new_kiss_nested_dialog_node_uuid = 'ca93806f-e08a-4493-9726-8f4e5fa5dfb9'
    shadowheart_kiss_nested_dialog_node_uuid = '282f4e56-8de0-40ed-bbe2-5b3669f240b6'

    post_kiss_selunite_node_uuid = '8aba1af5-7d3c-4e35-8d1c-ea724c1b0cba'
    post_kiss_sharran_node_uuid = 'aec26f73-7502-45e9-b531-5caa29255587'

    jump_back_node_uuid = '56e10211-8a72-4ade-aa40-bc2514afcc02'
    end_dialog_node_uuid = '5bdd0e92-4691-4421-bcbe-8bc059d12808'

    karlach_kiss_a_node_uuid = 'd60052e9-e8a3-432c-ac80-6dddb75cc679'
    karlach_kiss_b_node_uuid = 'bd03ca1c-3d74-4d0f-9ee2-b16e9ea38ebd'
    karlach_kiss_c_node_uuid = '30dee453-ad5a-441f-ba42-51219d43de84'
    karlach_kiss_d_node_uuid = '819f917c-457c-4a76-b90a-8245772ad96d'

    minthara_kiss_a_node_uuid = '9fad7df8-9954-42dc-a697-7cee7b94b347'
    minthara_kiss_b_node_uuid = 'a47887d4-6f84-4a44-b6b9-e7587ac2f541'
    minthara_kiss_c_node_uuid = 'd3bd8b00-6343-46d4-ab3a-7820b3d227b9'
    minthara_kiss_d_node_uuid = 'a73a8ac1-0607-4585-b4aa-15969b872817'

    shadowheart_kiss_node_uuid = '8545cf98-a5eb-468f-a442-fab56d0a4343'

    d.create_jump_dialog_node(jump_back_node_uuid, '23749c85-4289-4965-a7db-1909f5cb63a2', 2)
    d.create_standard_dialog_node(
        end_dialog_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [],
        None,
        setflags = (
            bg3.flag_group('Global', (
                bg3.flag(bg3.FLAG_Shadowheart_InParty_State_EndDialog, True, speaker_idx_shadowheart),
            )),
        ),
        end_node = True
    )

    d.create_nested_dialog_node(
        new_kiss_nested_dialog_node_uuid,
        new_kiss_nested_dialog_uuid,
        [
            post_kiss_selunite_node_uuid,
            post_kiss_sharran_node_uuid,
        ],
        speaker_count = 2)
    d.create_nested_dialog_node(
        shadowheart_kiss_nested_dialog_node_uuid,
        shadowheart_kiss_nested_dialog_uuid,
        [
            post_kiss_selunite_node_uuid,
            post_kiss_sharran_node_uuid,
        ],
        speaker_count = 2)

    d.create_standard_dialog_node(
        post_kiss_selunite_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [jump_back_node_uuid],
        None,
        checkflags = (
            bg3.flag_group('Global', (
                bg3.flag(Shadowheart_Turned_Away_From_Shar.uuid, True, None),
            )),
        ))
    d.create_standard_dialog_node(
        post_kiss_sharran_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [end_dialog_node_uuid],
        None,
        checkflags = (
            bg3.flag_group('Global', (
                bg3.flag(Shadowheart_Turned_Away_From_Shar.uuid, False, None),
            )),
        ))

    d.create_standard_dialog_node(
        karlach_kiss_a_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [new_kiss_nested_dialog_node_uuid],
        None,
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(Karlach_Kiss_A.uuid, True, speaker_idx_shadowheart),
            )),
        ))
    d.create_standard_dialog_node(
        karlach_kiss_b_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [new_kiss_nested_dialog_node_uuid],
        None,
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(Karlach_Kiss_B.uuid, True, speaker_idx_shadowheart),
            )),
        ))
    d.create_standard_dialog_node(
        karlach_kiss_c_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [new_kiss_nested_dialog_node_uuid],
        None,
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(Karlach_Kiss_C.uuid, True, speaker_idx_shadowheart),
            )),
        ))
    d.create_standard_dialog_node(
        karlach_kiss_d_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [new_kiss_nested_dialog_node_uuid],
        None,
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(Karlach_Kiss_D.uuid, True, speaker_idx_shadowheart),
            )),
        ))
    d.create_standard_dialog_node(
        minthara_kiss_a_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [new_kiss_nested_dialog_node_uuid],
        None,
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(Minthara_Kiss_A.uuid, True, speaker_idx_shadowheart),
            )),
        ))
    d.create_standard_dialog_node(
        minthara_kiss_b_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [new_kiss_nested_dialog_node_uuid],
        None,
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(Minthara_Kiss_B.uuid, True, speaker_idx_shadowheart),
            )),
        ))
    d.create_standard_dialog_node(
        minthara_kiss_c_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [new_kiss_nested_dialog_node_uuid],
        None,
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(Minthara_Kiss_C.uuid, True, speaker_idx_shadowheart),
            )),
        ))
    d.create_standard_dialog_node(
        minthara_kiss_d_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [new_kiss_nested_dialog_node_uuid],
        None,
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(Minthara_Kiss_D.uuid, True, speaker_idx_shadowheart),
            )),
        ))

    d.create_standard_dialog_node(
        shadowheart_kiss_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [shadowheart_kiss_nested_dialog_node_uuid],
        None,
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(Karlach_Kiss_A.uuid, False, speaker_idx_shadowheart),
                bg3.flag(Karlach_Kiss_B.uuid, False, speaker_idx_shadowheart),
                bg3.flag(Karlach_Kiss_C.uuid, False, speaker_idx_shadowheart),
                bg3.flag(Karlach_Kiss_D.uuid, False, speaker_idx_shadowheart),
                bg3.flag(Minthara_Kiss_A.uuid, False, speaker_idx_shadowheart),
                bg3.flag(Minthara_Kiss_B.uuid, False, speaker_idx_shadowheart),
                bg3.flag(Minthara_Kiss_C.uuid, False, speaker_idx_shadowheart),
                bg3.flag(Minthara_Kiss_D.uuid, False, speaker_idx_shadowheart),
            )),
        ))

    d.create_standard_dialog_node(
        bg3.SHADOWHEART_KISS_FORK_NODE_UUID,
        bg3.SPEAKER_SHADOWHEART,
        [
            shadowheart_kiss_node_uuid,
            karlach_kiss_a_node_uuid,
            karlach_kiss_b_node_uuid,
            karlach_kiss_c_node_uuid,
            karlach_kiss_d_node_uuid,
            minthara_kiss_a_node_uuid,
            minthara_kiss_b_node_uuid,
            minthara_kiss_c_node_uuid,
            minthara_kiss_d_node_uuid,
        ],
        None)

    d.delete_child_dialog_node('5e26cf5f-ff2f-4ab8-8281-e8462d1c8655', '59d6dab0-dd97-7cac-8198-88d4e49b2394')
    d.add_child_dialog_node('5e26cf5f-ff2f-4ab8-8281-e8462d1c8655', bg3.SHADOWHEART_KISS_FORK_NODE_UUID)


bg3.add_build_procedure('patch_kiss_animations', patch_kiss_animations)
bg3.add_build_procedure('create_new_kisses', create_new_kisses)
bg3.add_build_procedure('add_new_kisses', add_new_kisses)

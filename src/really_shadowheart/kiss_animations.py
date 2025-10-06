from __future__ import annotations

import bg3moddinglib as bg3

from .context import game_assets
from .flags import *
from .more_kisses import (
    add_laezel_kiss_bt1_animation,
    add_laezel_kiss_bt2_animation,
    add_laezel_kiss_bt34_animation,
    add_laezel_kiss_dragonborn_animation,
    add_laezel_kiss_short_animation,
    add_laezel_kiss_dwarf_animation,
)

###############################################################
# Enable all 6 kiss animations
###############################################################

def patch_kiss_animations() -> None:

    # d = bg3.dialog_object(files.get_file('Gustav', 'Mods/GustavDev/Story/DialogsBinary/Companions/ShadowHeart_InParty2_Nested_ShadowheartKiss.lsf'))

    ab = game_assets.get_modded_dialog_asset_bundle('ShadowHeart_InParty2_Nested_ShadowheartKiss')
    d = bg3.dialog_object(ab.dialog)
    t = bg3.timeline_object(ab.timeline, d)

    ###############################################################
    # Dialog: ShadowHeart_InParty2_Nested_ShadowheartKiss.lsf
    # Enable all 6 kiss animations
    ###############################################################

    slot_idx_shadowheart = d.get_speaker_slot_index(bg3.SPEAKER_SHADOWHEART)
    slot_idx_tav = d.get_speaker_slot_index(bg3.SPEAKER_PLAYER)

    kiss_root_node_uuid = '7145a7e3-d1b5-d29a-c685-3867b85b4021'
    exit_node_uuid = 'd67e9777-539d-f113-62e4-034dbe759c36'

    # Reset kiss flags on nested dialog exit
    d.add_dialog_flags(
        exit_node_uuid,
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
        [exit_node_uuid],
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
        [exit_node_uuid],
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
        [exit_node_uuid],
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
        [exit_node_uuid],
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
        [exit_node_uuid],
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
        [exit_node_uuid],
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
        [exit_node_uuid],
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
        [exit_node_uuid],
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
        [exit_node_uuid],
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
        [exit_node_uuid],
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
        [exit_node_uuid],
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

    d.add_child_dialog_node(kiss_root_node_uuid, '802a2231-ebc4-43de-9f5d-c4f13d6bf73a')
    d.add_child_dialog_node(kiss_root_node_uuid, '731508a7-53e7-41bd-be3c-73e518ffbbc5')
    d.add_child_dialog_node(kiss_root_node_uuid, 'e7cc3a96-2a3a-7e24-ab65-82245a27b7b2')
    d.add_child_dialog_node(kiss_root_node_uuid, '23bffd00-5280-a6b6-3f21-54ad298cb67e')
    d.add_child_dialog_node(kiss_root_node_uuid, 'eb0d744a-a22f-326f-6194-88bff056f6bb')
    d.add_child_dialog_node(kiss_root_node_uuid, '4cf4c762-1738-2ebe-c65b-79f1300e97c7')
    d.add_child_dialog_node(kiss_root_node_uuid, 'bf5d6f26-ffa3-510e-be90-39f57002fbc9')
    d.add_child_dialog_node(kiss_root_node_uuid, '35bb16bc-27e0-febc-abf9-31b38a667199')
    d.add_child_dialog_node(kiss_root_node_uuid, 'd9f9b4c6-4929-f14a-85b0-cc48794abf43')
    d.add_child_dialog_node(kiss_root_node_uuid, '6dce7fcd-e8a4-e34a-1835-22628c420853')
    d.add_child_dialog_node(kiss_root_node_uuid, 'd0d19c73-576a-e417-e9ce-b0ff488c3ba4')

    # Dragonborn
    d.create_alias_dialog_node(
        '5f0cec3f-92b4-4f50-90cc-343977ef3992',
        'b2ef3011-5998-205c-9ccc-a2d2b2c6f338',
        [exit_node_uuid],
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
        [exit_node_uuid],
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
        [exit_node_uuid],
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
        [exit_node_uuid],
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
        [exit_node_uuid],
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
        [exit_node_uuid],
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
    d.add_child_dialog_node(kiss_root_node_uuid, '5f0cec3f-92b4-4f50-90cc-343977ef3992')
    d.add_child_dialog_node(kiss_root_node_uuid, 'f2f0aaea-20ea-464c-9d46-58e9d238c54a')
    d.add_child_dialog_node(kiss_root_node_uuid, 'e59b0566-fc67-4130-9ce3-76c2182618c7')
    d.add_child_dialog_node(kiss_root_node_uuid, '2ef6b1f4-9936-479f-af70-c6863e6e2725')
    d.add_child_dialog_node(kiss_root_node_uuid, 'b4d1a14d-6f01-40cc-9eb2-8b6f99ad7ce6')
    d.add_child_dialog_node(kiss_root_node_uuid, '2173b8c0-2e20-4419-bc1a-734b351327c9')

    # Strong body type
    d.create_alias_dialog_node(
        '989dd13e-7180-4b7f-88e0-73add63e37fd',
        '27966d84-2797-3c76-a194-4ff46f1ceb51',
        [exit_node_uuid],
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
        [exit_node_uuid],
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
        [exit_node_uuid],
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
        [exit_node_uuid],
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
        [exit_node_uuid],
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
        [exit_node_uuid],
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
    d.add_child_dialog_node(kiss_root_node_uuid, '27966d84-2797-3c76-a194-4ff46f1ceb51')
    d.add_child_dialog_node(kiss_root_node_uuid, '6b28ea73-a974-4734-8767-d404507984ab')
    d.add_child_dialog_node(kiss_root_node_uuid, '2a8e29eb-b517-4724-8a12-c97a6916fa41')
    d.add_child_dialog_node(kiss_root_node_uuid, 'd20b131a-8092-4411-9f8a-83d8bf36d8fc')
    d.add_child_dialog_node(kiss_root_node_uuid, '00693a73-00a8-4f05-8f62-8ac4180f7fea')
    d.add_child_dialog_node(kiss_root_node_uuid, '5957be7b-89da-4daa-8b0d-90921af9c810')

    # Female
    d.create_alias_dialog_node(
        'e125eaf8-dce2-43eb-9476-cd1d9b00ee6e',
        '2e786fd7-bbc4-df6b-0df2-e8413461e992',
        [exit_node_uuid],
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
        [exit_node_uuid],
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
        [exit_node_uuid],
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
        [exit_node_uuid],
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
        [exit_node_uuid],
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
        [exit_node_uuid],
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
    d.add_child_dialog_node(kiss_root_node_uuid, 'e125eaf8-dce2-43eb-9476-cd1d9b00ee6e')
    d.add_child_dialog_node(kiss_root_node_uuid, 'cbc1c0af-0ba1-4eee-8508-f5520d093df6')
    d.add_child_dialog_node(kiss_root_node_uuid, '17cd5eb2-cb01-4665-9e14-198292d54217')
    d.add_child_dialog_node(kiss_root_node_uuid, 'fe0a0c90-43bb-4531-99dc-ebb7c5b21398')
    d.add_child_dialog_node(kiss_root_node_uuid, '30f4c0a5-12a9-4d9a-84da-75eadef3227b')
    d.add_child_dialog_node(kiss_root_node_uuid, 'd9d5e7a9-45b9-4e51-846e-8228138c6503')

    # Male
    d.create_alias_dialog_node(
        'c1139b8d-c791-4091-b69d-c3899702fae6',
        '5f5e750e-d2e2-4e2e-90fe-e6f7fc8eea71',
        [exit_node_uuid],
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
        [exit_node_uuid],
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
        [exit_node_uuid],
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
        [exit_node_uuid],
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
        [exit_node_uuid],
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
        [exit_node_uuid],
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
    d.add_child_dialog_node(kiss_root_node_uuid, 'c1139b8d-c791-4091-b69d-c3899702fae6')
    d.add_child_dialog_node(kiss_root_node_uuid, '81210836-ff01-40c4-aad2-9560fa9fe8bd')
    d.add_child_dialog_node(kiss_root_node_uuid, 'f341f0af-8dff-4b2f-8df2-b69ae5308f76')
    d.add_child_dialog_node(kiss_root_node_uuid, '0174633d-ab54-4a44-912a-c8666d28ea1f')
    d.add_child_dialog_node(kiss_root_node_uuid, 'b713ad19-66d2-4266-b318-e0970e5f2748')
    d.add_child_dialog_node(kiss_root_node_uuid, '96a6f7d6-a5f2-489d-8576-4de27fcb152c')


    ###############################################################
    # Add more kisses
    ###############################################################

    forehead_kiss_bt1_node_uuid = '0b6b7ad3-abeb-4f70-8d2e-97c830ab74bb'
    forehead_kiss_bt2_node_uuid = '56e3dde5-4509-47f1-8861-09a2987c1a27'
    forehead_kiss_bt34_node_uuid = 'e0f3af31-505a-410c-bfd8-3356cf731054'
    forehead_kiss_dragonborn_node_uuid = '7442ec99-552b-40bf-a695-8c8e0a02677a'
    forehead_kiss_short_node_uuid = '22c3b18f-fe5a-4c4f-927d-442b37d683f0'
    forehead_kiss_dwarf_node_uuid = '6e216e67-9e5a-4cd5-8e3d-b7e925973877'

    d.create_standard_dialog_node(
        forehead_kiss_bt1_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [exit_node_uuid],
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
    add_laezel_kiss_bt1_animation(d, t, forehead_kiss_bt1_node_uuid)

    d.create_standard_dialog_node(
        forehead_kiss_bt2_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [exit_node_uuid],
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
    add_laezel_kiss_bt2_animation(d, t, forehead_kiss_bt2_node_uuid)

    d.create_standard_dialog_node(
        forehead_kiss_bt34_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [exit_node_uuid],
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
    add_laezel_kiss_bt34_animation(d, t, forehead_kiss_bt34_node_uuid)

    d.create_standard_dialog_node(
        forehead_kiss_dragonborn_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [exit_node_uuid],
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
    add_laezel_kiss_dragonborn_animation(d, t, forehead_kiss_dragonborn_node_uuid)

    d.create_standard_dialog_node(
        forehead_kiss_short_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [exit_node_uuid],
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
    add_laezel_kiss_short_animation(d, t, forehead_kiss_short_node_uuid)

    d.create_standard_dialog_node(
        forehead_kiss_dwarf_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [exit_node_uuid],
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
    add_laezel_kiss_dwarf_animation(d, t, forehead_kiss_dwarf_node_uuid)


    d.add_child_dialog_node(kiss_root_node_uuid, forehead_kiss_dwarf_node_uuid)
    d.add_child_dialog_node(kiss_root_node_uuid, forehead_kiss_short_node_uuid)
    d.add_child_dialog_node(kiss_root_node_uuid, forehead_kiss_dragonborn_node_uuid)
    d.add_child_dialog_node(kiss_root_node_uuid, forehead_kiss_bt34_node_uuid)
    d.add_child_dialog_node(kiss_root_node_uuid, forehead_kiss_bt1_node_uuid)
    d.add_child_dialog_node(kiss_root_node_uuid, forehead_kiss_bt2_node_uuid)

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
    # Use the new flag that enabled all 6 kiss animations
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
    # Selunite kiss
    #
    kiss_me_like_you_hate_me_node_uuid = '8203a694-02be-4f2a-8059-e9b1cbc55b2f'
    d.set_dialog_flags(kiss_me_like_you_hate_me_node_uuid, setflags = (shadowheart_random_kiss_start_true,))

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


bg3.add_build_procedure('patch_kiss_animations', patch_kiss_animations)

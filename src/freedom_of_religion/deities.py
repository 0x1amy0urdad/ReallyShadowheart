from __future__ import annotations

import bg3moddinglib as bg3

from .context import files

def enable_dieties_for_all_classes() -> None:
    gf = files.get_file('Shared', 'Public/Shared/ClassDescriptions/ClassDescriptions.lsx', mod_specific = True)
    root = gf.xml.getroot()
    if root is None:
        raise RuntimeError('Failed to enable dieties for all classes')
    class_names = frozenset((
        'Barbarian',
        'Bard',
        'Cleric',
        'Druid',
        'Fighter',
        'Monk',
        'Paladin',
        'Ranger',
        'Rogue',
        'Sorcerer',
        'Warlock',
        'Wizard'))
    class_descriptions = root.findall('./region[@id="ClassDescriptions"]/node[@id="root"]/children/node[@id="ClassDescription"]')
    for class_description in class_descriptions:
        class_name = bg3.get_bg3_attribute(class_description, 'Name')
        if class_names is not None and class_name in class_names:
            has_god = bg3.get_bg3_attribute(class_description, 'HasGod')
            if has_god == 'true':
                continue
            bg3.set_bg3_attribute(class_description, 'HasGod', 'true', attribute_type = 'bool')


def enable_dieties_for_all_races() -> None:
    gf1 = files.get_file('Shared', 'Public/Shared/Races/Races.lsx', mod_specific = True)
    gf2 = files.get_file('Shared', 'Public/SharedDev/Races/Races.lsx', exclude_from_build = True)

    gf1_races = gf1.xml.findall('./region[@id="Races"]/node[@id="root"]/children/node[@id="Race"]')    
    for race in gf1_races:
        children = race.find('children')
        if children is not None:
            excluded_gods = children.findall('node[@id="ExcludedGods"]')
            if excluded_gods:
                for excluded_god in excluded_gods:
                    children.remove(excluded_god)

    insert_here = gf1.xml.find('./region[@id="Races"]/node[@id="root"]/children')
    if insert_here is None:
        raise ValueError(f'corrupt game file {gf1.relative_file_path}')

    gf2_races = gf2.xml.findall('./region[@id="Races"]/node[@id="root"]/children/node[@id="Race"]')
    for race in gf2_races:
        children = race.find('children')
        if children is not None:
            excluded_gods = children.findall('node[@id="ExcludedGods"]')
            if excluded_gods:
                for excluded_god in excluded_gods:
                    children.remove(excluded_god)
                insert_here.append(race)

def add_god(
        parent_node: bg3.et.Element[str],
        description: str,
        display_name: str,
        name: str,
        god_uuid: str,
        tags: list[str],
        index: int | None = None
) -> None:
    lines = [
        '<node id="God">',
        f'<attribute id="Description" type="TranslatedString" handle="{description}" version="1"/>',
        f'<attribute id="DisplayName" type="TranslatedString" handle="{display_name}" version="1"/>',
        f'<attribute id="Name" type="FixedString" value="{name}"/>',
        f'<attribute id="UUID" type="guid" value="{god_uuid}"/>',
        '<children>']
    for tag in tags:
        lines.append(f'<node id="Tags"><attribute id="Object" type="guid" value="{tag}"/></node>')
    lines.append('</children></node>')
    if index is None:
        parent_node.append(bg3.et.fromstring(''.join(lines)))
    else:
        parent_node.insert(index, bg3.et.fromstring(''.join(lines)))


def add_more_gods() -> None:
    gf = files.add_new_file('Public/ModNameHere/Gods/Gods.lsx', is_mod_specific = True)
    xml = gf.root_node
    xml.append(bg3.et.fromstring('<version major="4" minor="0" revision="9" build="307"/>'))
    xml.append(bg3.et.fromstring('<region id="Gods"><node id="root"><children></children></node></region>'))
    gods = xml.find('./region[@id="Gods"]/node[@id="root"]/children')
    if gods is None:
        raise RuntimeError()
    add_god(
        gods,
        'h25ff1296g3e9cg4d44ga79egd2c29959b833',
        'h1b5f0ca9g5430g472dgb1e7g213bf0c9fefa',
        'Bhaal',
        '467e9e42-c7ac-45cd-aa4e-069d19b8332e',
        [bg3.GOD_BHAAL, bg3.ALIGN_EVIL])
    add_god(
        gods,
        'hd19f71a3gb275g4cb3gb988gde4730e91f16',
        'h0928d60cgb897g4ab2g830cgf0a762e87251',
        'Bane',
        '3ed46cdd-3309-486d-9258-2ab503042315',
        [bg3.GOD_BANE, bg3.ALIGN_EVIL])
    add_god(
        gods,
        'hef8ac47eg7b6bg4c5ega9e0ge8d4ced1c548',
        'h0a40a3eag306eg44b7gb7cdg68e81bfbe523',
        'Myrkul',
        '7f5583f7-b01d-4bcf-91e5-3bf7f693ce40',
        [bg3.GOD_MYRKUL, bg3.ALIGN_EVIL])
    add_god(
        gods,
        'h18852513gcd55g49d4ga4dag1ce62af70fa0',
        'h67ebb3abg6fbbg4b6dga735g3a49e88d0241',
        'Godless',
        'a43b1ff9-ef6e-485e-af73-9f490b87ba70',
        [bg3.GODLESS, bg3.ALIGN_NEUTRAL])


def modify_tags() -> None:
    # Selune
    bg3.tag_object.create_new(
        files,
        bg3.TAG_CLERIC_SELUNE,
        'WORSHIPPER_SELUNE',
        'Player or NPC is a worshipper of Selune.',
        ('h488ff590ge704g4980ga69eg5344e4a4f9fa', 1),
        ('hf4d779b8g29dbg41a2g9595g3b0c022a2642', 1),
        ('Dialog', 'Class', 'CharacterSheet'))
    bg3.tag_object.create_new(
        files,
        bg3.GOD_SELUNE,
        'SELUNE',
        '|Player or NPC chose Selune.|',
        ('', 0),
        ('hc7ab5da7gb105g495egbe63gddd2e114095f', 1),
        ('Dialog', 'Deity'))

    # Shar
    bg3.tag_object.create_new(
        files,
        bg3.TAG_CLERIC_SHAR,
        'WORSHIPPER_SHAR',
        'Player or NPC is a worshipper of Shar.',
        ('hfd8e101bg63a6g414agaff0g071e81a0aef2', 1),
        ('h095f2168gb8e9g4b7ega7a9g9c6633d2affb', 1),
        ('Dialog', 'Class', 'CharacterSheet'))
    bg3.tag_object.create_new(
        files,
        bg3.GOD_SHAR,
        'SHAR',
        '|Player or NPC chose Shar.|',
        ('', 0),
        ('hd1eda1a0ga3c7g4015g83d8gdee4e3a8ca7c', 1),
        ('Dialog', 'Deity'))

    # Tempus
    bg3.tag_object.create_new(
        files,
        bg3.TAG_CLERIC_TEMPUS,
        'WORSHIPPER_TEMPUS',
        'Player or NPC is a worshipper of Tempus.',
        ('h5bc0baa8g5a69g4ea5g895fg9e14f6223bc8', 1),
        ('hcb1bcd01g13e4g4de8gb750ge7829f4743f4', 1),
        ('Dialog', 'Class', 'CharacterSheet'))
    bg3.tag_object.create_new(
        files,
        bg3.GOD_TEMPUS,
        'TEMPUS',
        '|Player or NPC chose Tempus.|',
        ('', 0),
        ('h26cb3218g1f22g44f5gac07gabe57b40acae', 1),
        ('Dialog', 'Deity'))

    # Tyr
    bg3.tag_object.create_new(
        files,
        bg3.TAG_CLERIC_TYR,
        'WORSHIPPER_TYR',
        'Player or NPC is a worshipper of Tyr.',
        ('ha2c68ffdgfd2bg484egbd08gfb977bbca24a', 1),
        ('h06214de8gba90g4f4agb06cgc3f2727d32eb', 1),
        ('Dialog', 'Class', 'CharacterSheet'))
    bg3.tag_object.create_new(
        files,
        bg3.GOD_TYR,
        'TYR',
        '|Player or NPC chose Tyr.|',
        ('', 0),
        ('h05e7a55cg7006g47a9ga561g264561df715e', 1),
        ('Dialog', 'Deity'))

    # Helm
    bg3.tag_object.create_new(
        files,
        bg3.TAG_CLERIC_HELM,
        'WORSHIPPER_HELM',
        'Player or NPC is a worshipper of Helm.',
        ('h6444510fg314bg4178g82bagba386697db24', 1),
        ('hd6ab5b8egd435g4acegb707ga75c13ee8f67', 1),
        ('Dialog', 'Class', 'CharacterSheet'))
    bg3.tag_object.create_new(
        files,
        bg3.GOD_HELM,
        'HELM',
        '|Player or NPC chose Helm.|',
        ('', 0),
        ('ha44f365cg8c9eg4391g8e43ge59c430a17dd', 1),
        ('Dialog', 'Deity'))

    # Imater
    bg3.tag_object.create_new(
        files,
        bg3.TAG_CLERIC_ILMATER,
        'WORSHIPPER_ILMATER',
        'Player or NPC is a worshipper of Imater.',
        ('h0bc51315g360ag47e0gad6dg2e80ee2911cc', 1),
        ('hd4f99497g0451g463dg8812g2ffcdd3b245d', 1),
        ('Dialog', 'Class', 'CharacterSheet'))
    bg3.tag_object.create_new(
        files,
        bg3.GOD_ILMATER,
        'IMATER',
        '|Player or NPC chose Imater.|',
        ('', 0),
        ('h90ecda5bgeeffg4989g8ae1g9e43feaa5965', 1),
        ('Dialog', 'Deity'))

    # Mystra
    bg3.tag_object.create_new(
        files,
        bg3.TAG_CLERIC_MYSTRA,
        'WORSHIPPER_MYSTRA',
        'Player or NPC is a worshipper of Mystra.',
        ('hb978e16agf016g4043g8845g5aa89e36a944', 1),
        ('hca2d7becg6b25g4bb3gb0a8gaa917343179f', 1),
        ('Dialog', 'Class', 'CharacterSheet'))
    bg3.tag_object.create_new(
        files,
        bg3.GOD_MYSTRA,
        'MYSTRA',
        '|Player or NPC chose Mystra.|',
        ('', 0),
        ('h6f758b98g0cc8g482fg86b3g78cec64547e3', 1),
        ('Dialog', 'Deity'))

    # Oghma
    bg3.tag_object.create_new(
        files,
        bg3.TAG_CLERIC_OGHMA,
        'WORSHIPPER_OGHMA',
        'Player or NPC is a worshipper of Oghma.',
        ('h88eb0caeg3c8bg47d2g8329g9ebb386bf63d', 1),
        ('ha6a87807gcd22g4041gb565g17293fee4006', 1),
        ('Dialog', 'Class', 'CharacterSheet'))
    bg3.tag_object.create_new(
        files,
        bg3.GOD_OGHMA,
        'OGHMA',
        '|Player or NPC chose Oghma.|',
        ('', 0),
        ('h458d175cge82fg4aa8g9bdfg1fc366f9259f', 1),
        ('Dialog', 'Deity'))

    # Kelemvor
    bg3.tag_object.create_new(
        files,
        bg3.TAG_CLERIC_KELEMVOR,
        'WORSHIPPER_KELEMVOR',
        'Player or NPC is a worshipper of Kelemvor.',
        ('h5d8ed13dgde76g488fg9999g0e59f80a1393', 1),
        ('hc8f18c5fgc306g44bbgbb62g6bf89497932f', 1),
        ('Dialog', 'Class', 'CharacterSheet'))
    bg3.tag_object.create_new(
        files,
        bg3.GOD_KELEMVOR,
        'KELEMVOR',
        '|Player or NPC chose Kelemvor.|',
        ('', 0),
        ('h6b1a794cga8e3g42deg8adcg3c003a165d4b', 1),
        ('Dialog', 'Deity'))

    # Moradin
    bg3.tag_object.create_new(
        files,
        bg3.TAG_CLERIC_MORADIN,
        'WORSHIPPER_MORADIN',
        'Player or NPC is a worshipper of Moradin.',
        ('hca092851g82b6g45dbg9708ge81c3016de21', 1),
        ('h5f02bc1fga43ag4ceegab0fg10d5b25d981e', 1),
        ('Dialog', 'Class', 'CharacterSheet'))
    bg3.tag_object.create_new(
        files,
        bg3.GOD_MORADIN,
        'MORADIN',
        '|Player or NPC chose Moradin.|',
        ('', 0),
        ('hc5576c8ege333g4ab5g9d6egc8b540c17082', 1),
        ('Dialog', 'Deity'))

    # Corellon Larethian
    bg3.tag_object.create_new(
        files,
        bg3.TAG_CLERIC_CORELLON,
        'WORSHIPPER_CORELLON_LARETHIAN',
        'Player or NPC is a worshipper of Corellon Larethian.',
        ('h158ea31cg3eeag467bgac7ag02e5bee45d14', 1),
        ('h3cb70201gea36g4aeegb6aeg9eaabcb31ca4', 1),
        ('Dialog', 'Class', 'CharacterSheet'))
    bg3.tag_object.create_new(
        files,
        bg3.GOD_CORELLON_LARETHIAN,
        'CORELLON_LARETHIAN',
        '|Player or NPC chose Corellon Larethian.|',
        ('', 0),
        ('h06ab8f0egfe2bg48c6g97e1g0800412fc3da', 1),
        ('Dialog', 'Deity'))

    # Garl Glittergold
    bg3.tag_object.create_new(
        files,
        bg3.TAG_CLERIC_GARL,
        'WORSHIPPER_GARL_GLITTERGOLD',
        'Player or NPC is a worshipper of Garl Glittergold.',
        ('h0a18e2cdg3f0bg4b07g92ebg034e0f714f36', 1),
        ('hd8ed1642g4e46g4799gb47bgd524e0295fd8', 1),
        ('Dialog', 'Class', 'CharacterSheet'))
    bg3.tag_object.create_new(
        files,
        bg3.GOD_GARL_GLITTERGOLD,
        'GARL_GLITTERGOLD',
        '|Player or NPC chose Garl Glittergold.|',
        ('', 0),
        ('he964e18dg5c9fg4918gb36bg6e4efb91fa8c', 1),
        ('Dialog', 'Deity'))

    # Yondalla
    bg3.tag_object.create_new(
        files,
        bg3.TAG_CLERIC_YONDALLA,
        'WORSHIPPER_YONDALLA',
        'Player or NPC is a worshipper of Yondalla.',
        ('hc5c359fdg4a52g4579ga469gffc914b34d85', 1),
        ('hddb43827geb4bg4e3eg98f8g31493262fb45', 1),
        ('Dialog', 'Class', 'CharacterSheet'))
    bg3.tag_object.create_new(
        files,
        bg3.GOD_YONDALLA,
        'YONDALLA',
        '|Player or NPC chose Yondalla.|',
        ('', 0),
        ('hab7d9290g11e3g423agb540g0af2387467c8', 1),
        ('Dialog', 'Deity'))

    # Lolth
    bg3.tag_object.create_new(
        files,
        bg3.TAG_CLERIC_LOLTH,
        'WORSHIPPER_LOLTH',
        'Player or NPC is a worshipper of Lolth.',
        ('hc28d75f4gb863g4163g9982gb6fd8fde0b0d', 1),
        ('hccc3a727g6506g4791ga41bgf025735f77c2', 1),
        ('Dialog', 'Class', 'CharacterSheet'))
    bg3.tag_object.create_new(
        files,
        bg3.GOD_LOLTH,
        'LOLTH',
        '|Player or NPC chose Lolth.|',
        ('', 0),
        ('hea9b1f2dgc1f4g4ebagab4cgf8c642df5cd1', 1),
        ('Dialog', 'Deity'))

    # Laduguer
    bg3.tag_object.create_new(
        files,
        bg3.TAG_CLERIC_LADUGUER,
        'WORSHIPPER_LADUGUER',
        'Player or NPC is a worshipper of Laduguer.',
        ('h66abb157gf40bg4f96ga3c2g7750dd26939b', 1),
        ('h0e2ca933g5c22g4108gb252gbc2c643103c2', 1),
        ('Dialog', 'Class', 'CharacterSheet'))
    bg3.tag_object.create_new(
        files,
        bg3.GOD_LADUGUER,
        'LADUGUER',
        '|Player or NPC chose Laduguer.|',
        ('', 0),
        ('h5bf5e188g1933g4663ga851gd77764d7b3c2', 1),
        ('Dialog', 'Deity'))

    # Vlaakith
    bg3.tag_object.create_new(
        files,
        bg3.TAG_CLERIC_VLAAKITH,
        'WORSHIPPER_VLAAKITH',
        'Player or NPC is a worshipper of Vlaakith.',
        ('h61625eaeg2707g48efgb169g18ed5666b945', 1),
        ('hbb93e54eg560bg4c73g8597g9bcd1edc81a9', 1),
        ('Dialog', 'Class', 'CharacterSheet'))
    bg3.tag_object.create_new(
        files,
        bg3.GOD_VLAAKITH,
        'VLAAKITH',
        '|Player or NPC chose Vlaakith.|',
        ('', 0),
        ('h67a15686g1ba0g4fe5gaa57g269f611aa053', 1),
        ('Dialog', 'Deity'))

    # Eilistraee
    bg3.tag_object.create_new(
        files,
        bg3.TAG_CLERIC_EILISTRAEE,
        'WORSHIPPER_EILISTRAEE',
        'Player or NPC is a worshipper of Eilistraee.',
        ('h234084fdg683dg4751gaaf7g057c15a91c86', 1),
        ('hc315bf65g7bdfg4a01gb3e7g3df066084483', 1),
        ('Dialog', 'Class', 'CharacterSheet'))
    bg3.tag_object.create_new(
        files,
        bg3.GOD_EILISTRAEE,
        'EILISTRAEE',
        '|Player or NPC chose Eilistraee.|',
        ('', 0),
        ('hf3b0a4c9g2e3cg49edga83dgb2cfe56761aa', 1),
        ('Dialog', 'Deity'))

    # Lathander
    bg3.tag_object.create_new(
        files,
        bg3.TAG_CLERIC_LATHANDER,
        'WORSHIPPER_LATHANDER',
        'Player or NPC is a worshipper of Lathander.',
        ('h9ff87fbeg60feg4a1bg9b20gedb5fa871ef9', 1),
        ('h1d40b789g7862g4bdeg9ce7g899138a81173', 1),
        ('Dialog', 'Class', 'CharacterSheet'))
    bg3.tag_object.create_new(
        files,
        bg3.GOD_LATHANDER,
        'LATHANDER',
        '|Player or NPC chose Lathander.|',
        ('', 0),
        ('h8cfa5591g5edcg42d9gba5dg6bff4a5c5ed4', 1),
        ('Dialog', 'Deity'))

    # Talos
    bg3.tag_object.create_new(
        files,
        bg3.TAG_CLERIC_TALOS,
        'WORSHIPPER_TALOS',
        'Player or NPC is a worshipper of Talos.',
        ('hba372778g8fffg41e8gaf27g487e82c0932d', 1),
        ('h78615facg7d1dg48b3ga210g50004e763009', 1),
        ('Dialog', 'Class', 'CharacterSheet'))
    bg3.tag_object.create_new(
        files,
        bg3.GOD_TALOS,
        'TALOS',
        '|Player or NPC chose Talos.|',
        ('', 0),
        ('h05b65331gb9b1g4c22ga1b0g0b03ac951b56', 1),
        ('Dialog', 'Deity'))

    # Tymora
    bg3.tag_object.create_new(
        files,
        bg3.TAG_CLERIC_TYMORA,
        'WORSHIPPER_TYMORA',
        'Player or NPC is a worshipper of Tymora.',
        ('h324a3eb9g79ecg4de0g9f07g889a3d00085c', 1),
        ('hd0f95ee5gbe55g4374g8b9bg34e186b10673', 1),
        ('Dialog', 'Class', 'CharacterSheet'))
    bg3.tag_object.create_new(
        files,
        bg3.GOD_TYMORA,
        'TYMORA',
        '|Player or NPC chose Tymora.|',
        ('', 0),
        ('hc0e30445g72b6g4fb5g9801g5efe23bdc042', 1),
        ('Dialog', 'Deity'))

    # Mielikki
    bg3.tag_object.create_new(
        files,
        bg3.TAG_CLERIC_MIELIKKI,
        'WORSHIPPER_MIELIKKI',
        'Player or NPC is a worshipper of Mielikki.',
        ('h9ade59f9g6ad3g47beg9a22g9a3ff4b98a32', 1),
        ('h6725d7b0gc9b2g4d4fgb2cfg919c12e99e68', 1),
        ('Dialog', 'Class', 'CharacterSheet'))
    bg3.tag_object.create_new(
        files,
        bg3.GOD_MIELIKKI,
        'MIELIKKI',
        '|Player or NPC chose Mielikki.|',
        ('', 0),
        ('hfd7729b4g7af7g4bafgb1e0gf0538b5e89d3', 1),
        ('Dialog', 'Deity'))

    # Bahamut
    bg3.tag_object.create_new(
        files,
        bg3.TAG_CLERIC_BAHAMUT,
        'WORSHIPPER_BAHAMUT',
        'Player or NPC is a worshipper of Bahamut.',
        ('he3352264g3b0ag4606gaba2g22dc1420a856', 1),
        ('h767a26edg79ffg4143gbf67g754aa15055b4', 1),
        ('Dialog', 'Class', 'CharacterSheet'))
    bg3.tag_object.create_new(
        files,
        bg3.GOD_BAHAMUT,
        'BAHAMUT',
        '|Player or NPC chose Bahamut.|',
        ('', 0),
        ('hd33876a8gcd0ag45bfgbdb0gf51bf97640a2', 1),
        ('Dialog', 'Deity'))

    # Gruumsh
    bg3.tag_object.create_new(
        files,
        bg3.TAG_CLERIC_GRUUMSH,
        'WORSHIPPER_GRUUMSH',
        'Player or NPC is a worshipper of Gruumsh.',
        ('hf614144agcd50g4df7g9ef4gb4adfb19fe31', 1),
        ('hcfc688d4gbc08g43efgb409ge172a7e5deeb', 1),
        ('Dialog', 'Class', 'CharacterSheet'))
    bg3.tag_object.create_new(
        files,
        bg3.GOD_GRUUMSH,
        '_GRUUMSH',
        '|Player or NPC chose Gruumsh.|',
        ('', 0),
        ('h77d39903g8583g42cfg8484g5d900d26d78f', 1),
        ('Dialog', 'Deity'))

    # Tiamat
    bg3.tag_object.create_new(
        files,
        bg3.TAG_CLERIC_TIAMAT,
        'WORSHIPPER_TIAMAT',
        'Player or NPC is a worshipper of Tiamat.',
        ('h86fb9056g56f0g42d6ga96bgca11b8e255b3', 1),
        ('h53c5d270gf312g4e10gaa2fg312f92b1e48a', 1),
        ('Dialog', 'Class', 'CharacterSheet'))
    bg3.tag_object.create_new(
        files,
        bg3.GOD_TIAMAT,
        'TIAMAT',
        '|Player or NPC chose Tiamat.|',
        ('', 0),
        ('h637a45d8g8878g4774g8181gc1ca4ffb01fc', 1),
        ('Dialog', 'Deity'))

    # Bhaal
    bg3.tag_object.create_new(
        files,
        bg3.TAG_CLERIC_BHAAL,
        'WORSHIPPER_BHAAL',
        'Player or NPC is a worshipper of Bhaal.',
        ('h86fb9056g56f0g42d6ga96bgca11b8e255b3', 1),
        ('h53c5d270gf312g4e10gaa2fg312f92b1e48a', 1),
        ('Dialog', 'Class', 'CharacterSheet'))
    bg3.tag_object.create_new(
        files,
        bg3.GOD_BHAAL,
        'BHAAL',
        '|Player or NPC chose Bhaal.|',
        ('', 0),
        ('h1b5f0ca9g5430g472dgb1e7g213bf0c9fefa', 1),
        ('Dialog', 'Deity'))

    # Bane
    bg3.tag_object.create_new(
        files,
        bg3.TAG_CLERIC_BANE,
        'WORSHIPPER_BANE',
        'Player or NPC is a worshipper of Bane.',
        ('h938aa5b2g94cbg4ed1gb7c2gc2869a85226d', 1),
        ('hce83bf76gaa90g47ebga737g0bb10d2e5a07', 1),
        ('Dialog', 'Class', 'CharacterSheet'))
    bg3.tag_object.create_new(
        files,
        bg3.GOD_BANE,
        'BANE',
        '|Player or NPC chose Bane.|',
        ('', 0),
        ('h0928d60cgb897g4ab2g830cgf0a762e87251', 1),
        ('Dialog', 'Deity'))

    # Myrkul
    bg3.tag_object.create_new(
        files,
        bg3.TAG_CLERIC_MYRKUL,
        'WORSHIPPER_MYRKUL',
        'Player or NPC is a worshipper of Myrkul.',
        ('hfb2ee471g6de6g4660g8dabg6459caea65b4', 1),
        ('hc79ed229g43bag45cagbf9age4dd89d86dbf', 1),
        ('Dialog', 'Class', 'CharacterSheet'))
    bg3.tag_object.create_new(
        files,
        bg3.GOD_MYRKUL,
        'MYRKUL',
        '|Player or NPC chose Myrkul.|',
        ('', 0),
        ('h0a40a3eag306eg44b7gb7cdg68e81bfbe523', 1),
        ('Dialog', 'Deity'))

    # Worshipper of an evil god
    bg3.tag_object.create_new(
        files,
        bg3.TAG_CLERIC_EVIL,
        'WORSHIPPER_EVIL',
        'Player or NPC is a worshipper of an evil god.',
        ('h237ac7e6gba27g4263g8591gca942ea6dbe4', 1),
        ('ha4468f32g1088g4cfcgb3a2g5d86fd13f098', 1),
        ('Code', 'Dialog', 'Class', 'Class_Deity', 'CharacterSheet'))

    # Worshipper of a neutral god
    bg3.tag_object.create_new(
        files,
        bg3.TAG_CLERIC_NEUTRAL,
        'WORSHIPPER_NEUTRAL',
        'Player or NPC is a worshipper of a neutral god.',
        ('h9611d9e9g7b2fg4676gbdffgafc2780ce5b6', 1),
        ('h25c497f9g2925g4f08g87b2g40b8c459c7ab', 1),
        ('Code', 'Dialog', 'Class', 'Class_Deity', 'CharacterSheet'))

    # Worshipper of a good god
    bg3.tag_object.create_new(
        files,
        bg3.TAG_CLERIC_GOOD,
        'WORSHIPPER_GOOD',
        'Player or NPC is a worshipper of a good god.',
        ('h9964f550gb37ag4569gb377g1a5e8d51329f', 1),
        ('h1daaf2a1g6b1bg4b95g91d6ga32493e80f01', 1),
        ('Code', 'Dialog', 'Class', 'Class_Deity', 'CharacterSheet'))


bg3.add_build_procedure('modify_tags', modify_tags)
bg3.add_build_procedure('enable_dieties_for_all_classes', enable_dieties_for_all_classes)
bg3.add_build_procedure('enable_dieties_for_all_races', enable_dieties_for_all_races)
bg3.add_build_procedure('add_more_gods', add_more_gods)

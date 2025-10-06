from __future__ import annotations

import bg3moddinglib as bg3

from .context import files

########################################################
# Create custom strings, put them in english.loca.xml
########################################################

def create_text_content() -> None:
    content = {
        "h744690e1g4055g49b9gba6cgf175c791781f": (1, ""),

        # No god
        "h67ebb3abg6fbbg4b6dga735g3a49e88d0241": (1, "None"),
        "h18852513gcd55g49d4ga4dag1ce62af70fa0": (1, "Not all inhabitants of Faerun bow to a god. Free of any doctrine, they navigate their lives with their own moral compass, not bound by any dogma or tenets."),

        # Selune
        "hf4d779b8g29dbg41a2g9595g3b0c022a2642": (1, "Worshipper of Selûne"),
        "h488ff590ge704g4980ga69eg5344e4a4f9fa": (1, "Selûne is the goddess of the moon, navigation, and lycanthropes. Her worshippers honour Selûne's empathy and mystique, but are fearsome when facing Selûne's wicked sister, the goddess Shar."),
        "hc7ab5da7gb105g495egbe63gddd2e114095f": (1, "Selûne, Our Lady of Silver"),
        # Shar
        "h095f2168gb8e9g4b7ega7a9g9c6633d2affb": (1, "Worshipper of Shar"),
        "hfd8e101bg63a6g414agaff0g071e81a0aef2": (1, "Shar is the goddess of darkness, secrets, and loss. Forever in conflict with her twin sister Selûne, Shar's worshippers poison the world with fear and suffering while stealing forbidden knowledge in her name."),
        "hd1eda1a0ga3c7g4015g83d8gdee4e3a8ca7c": (1, "Shar, the Lady of Loss"),
        # Tempus
        "hcb1bcd01g13e4g4de8gb750ge7829f4743f4": (1, "Worshipper of Tempus"),
        "h5bc0baa8g5a69g4ea5g895fg9e14f6223bc8": (1, "Tempus is the god of war. His worshippers welcome conflict through force of arms, but only abide honourable combat and courageous action."),
        "h26cb3218g1f22g44f5gac07gabe57b40acae": (1, "Tempus, Lord of Battles"),
        # Tyr
        "h06214de8gba90g4f4agb06cgc3f2727d32eb": (1, "Worshipper of Tyr"),
        "ha2c68ffdgfd2bg484egbd08gfb977bbca24a": (1, "Tyr is the god of law and justice, and encourages his worshippers to uphold them no matter the sacrifices that must be made. He grants spells that enhance accuracy and martial prowess."),
        "h05e7a55cg7006g47a9ga561g264561df715e": (1, "Tyr, the Even-Handed"),
        # Helm
        "hd6ab5b8egd435g4acegb707ga75c13ee8f67": (1, "Worshipper of Helm"),
        "h6444510fg314bg4178g82bagba386697db24": (1, "Helm, the Vigilant One, is the god of those guard and defend others. His worshippers serve as implacable sentries, often wearing heavy plate armour to emulate their deity."),
        "ha44f365cg8c9eg4391g8e43ge59c430a17dd": (1, "Helm, the Vigilant One"),
        # Ilmater
        "hd4f99497g0451g463dg8812g2ffcdd3b245d": (1, "Worshipper of Ilmater"),
        "h0bc51315g360ag47e0gad6dg2e80ee2911cc": (1, "Ilmater is the god of suffering and endurance. His worshippers defend the oppressed and take on the burdens of others, leading to a reputation as martyrs among common folk."),
        "h90ecda5bgeeffg4989g8ae1g9e43feaa5965": (1, "Ilmater, the One Who Endures"),
        # Mystra
        "hca2d7becg6b25g4bb3gb0a8gaa917343179f": (1, "Worshipper of Mystra"),
        "hb978e16agf016g4043g8845g5aa89e36a944": (1, "Mystra is the goddess of all magic, guarding the Weave that allows mortal spellcasters to access its power. Her worshippers preserve ancient lore and protect bastions of magic."),
        "h6f758b98g0cc8g482fg86b3g78cec64547e3": (1, "Mystra, the Lady of Mysteries"),
        # Oghma
        "ha6a87807gcd22g4041gb565g17293fee4006": (1, "Worshipper of Oghma"),
        "h88eb0caeg3c8bg47d2g8329g9ebb386bf63d": (1, "Oghma is the Lord of Knowledge, overseeing inspiration and invention. His worshippers spread truth, encourage innovation, and stamp out falsehoods wherever they go."),
        "h458d175cge82fg4aa8g9bdfg1fc366f9259f": (1, "Oghma, the Binder"),
        # Kelemvor
        "hc8f18c5fgc306g44bbgbb62g6bf89497932f": (1, "Worshipper of Kelemvor"),
        "h5d8ed13dgde76g488fg9999g0e59f80a1393": (1, "Kelemvor is the fair-minded judge of the dead, shepherding lost souls to the afterlife. His worshippers perform burial rites and punish those who unnaturally extend their lifespans, such as liches and vampires."),
        "h6b1a794cga8e3g42deg8adcg3c003a165d4b": (1, "Kelemvor, Judge of the Damned"),
        # Moradin
        "h5f02bc1fga43ag4ceegab0fg10d5b25d981e": (1, "Worshipper of Moradin"),
        "hca092851g82b6g45dbg9708ge81c3016de21": (1, "Moradin, father of the dwarves, is the god of creation, smithing, stonework and protection. His worshippers are champions and guardians, leading the charge against age-old dwarven enemies."),
        "hc5576c8ege333g4ab5g9d6egc8b540c17082": (1, "Moradin, the Soul Forger"),
        # Corellon Larethian
        "h3cb70201gea36g4aeegb6aeg9eaabcb31ca4": (1, "Worshipper of Corellon Larethian"),
        "h158ea31cg3eeag467bgac7ag02e5bee45d14": (1, "Corellon Larethian, ever-changing creator of all elves. His worshippers are protectors of all things beautiful and champions in the never-ending fight against the enemies of the elves."),
        "h06ab8f0egfe2bg48c6g97e1g0800412fc3da": (1, "Corellon Larethian, the Protector"),
        # Garl Glittergold
        "hd8ed1642g4e46g4799gb47bgd524e0295fd8": (1, "Worshipper of Garl Glittergold"),
        "h0a18e2cdg3f0bg4b07g92ebg034e0f714f36": (1, "Garl Glittergold is the king of gnomish gods, a deity of humour, gem-cutting, protection, and trickery. His worshippers are often artisans or storytellers, relaying his tenets to the younger generations."),
        "he964e18dg5c9fg4918gb36bg6e4efb91fa8c": (1, "Garl Glittergold, the Joker"),
        # Yondalla
        "hddb43827geb4bg4e3eg98f8g31493262fb45": (1, "Worshipper of Yondalla"),
        "hc5c359fdg4a52g4579ga469gffc914b34d85": (1, "Yondalla is the mother-goddess of the halflings. Her worshippers view her as a strong and protective parent who bestows them with luck, and whose example should be followed."),
        "hab7d9290g11e3g423agb540g0af2387467c8": (1, "Yondalla, the Blessed One"),
        # Lolth
        "hccc3a727g6506g4791ga41bgf025735f77c2": (1, "Worshipper of Lolth"),
        "hc28d75f4gb863g4163g9982gb6fd8fde0b0d": (1, "Lolth is the evil drow goddess of deceit, shadows, and spiders. Her worshippers execute the will of the Spider Queen, weaving a complicated web of schemes and treachery."),
        "hea9b1f2dgc1f4g4ebagab4cgf8c642df5cd1": (1, "Lolth, the Spider Queen"),
        # Laduguer
        "h0e2ca933g5c22g4108gb252gbc2c643103c2": (1, "Worshipper of Laduguer"),
        "h66abb157gf40bg4f96ga3c2g7750dd26939b": (1, "Laduguer is the patron of the duergar and god of self-reliance, defence, and survival. His worshippers honour him by acquiring more power and wealth through any means possible."),
        "h5bf5e188g1933g4663ga851gd77764d7b3c2": (1, "Laduguer, the Exile"),
        # Vlaakith
        "hbb93e54eg560bg4c73g8597g9bcd1edc81a9": (1, "Worshipper of Vlaakith"),
        "h61625eaeg2707g48efgb169g18ed5666b945": (1, "Vlaakith is the dread lich queen of the githyanki. Anointed in a dark ritual, her worshippers are warriors who obey her every command."),
        "h67a15686g1ba0g4fe5gaa57g269f611aa053": (1, "Vlaakith, Lich Queen of Githyanki"),
        # Eilistraee
        "hc315bf65g7bdfg4a01gb3e7g3df066084483": (1, "Worshipper of Eilistraee"),
        "h234084fdg683dg4751gaaf7g057c15a91c86": (1, "Eilistraee is the goddess of good-aligned drow, beauty, song, and freedom. The Dark Maiden desires balance between all races, and struggles against her mother Lolth's corrupt aims."),
        "hf3b0a4c9g2e3cg49edga83dgb2cfe56761aa": (1, "Eilistraee, Lady of the Dance"),
        # Lathander
        "h1d40b789g7862g4bdeg9ce7g899138a81173": (1, "Worshipper of Lathander"),
        "h9ff87fbeg60feg4a1bg9b20gedb5fa871ef9": (1, "A servant of the god of morning dawn, whose deific name is Lathander."),
        "h8cfa5591g5edcg42d9gba5dg6bff4a5c5ed4": (1, "Lathander, the Morninglord"),
        # Talos
        "h78615facg7d1dg48b3ga210g50004e763009": (1, "Worshipper of Talos"),
        "hba372778g8fffg41e8gaf27g487e82c0932d": (1, "Talos represents the uncaring and destructive force of nature. His followers see life as a set of random effects in a sea of chaos, and take what they can - for who can say when Talos will strike next?"),
        "h05b65331gb9b1g4c22ga1b0g0b03ac951b56": (1, "Talos, the Storm Lord"),
        # Tymora
        "hd0f95ee5gbe55g4374g8b9bg34e186b10673": (1, "Worshipper of Tymora"),
        "h324a3eb9g79ecg4de0g9f07g889a3d00085c": (1, "Tymora is the bright-faced goddess of fortune, who favours those who gamble - and set out on adventure - with the utmost skill and daring."),
        "hc0e30445g72b6g4fb5g9801g5efe23bdc042": (1, "Tymora, Lady Luck"),
        # Mielikki
        "h6725d7b0gc9b2g4d4fgb2cfg919c12e99e68": (1, "Worshipper of Mielikki"),
        "h9ade59f9g6ad3g47beg9a22g9a3ff4b98a32": (1, "Mielikki is the goddess of forests and the creatures that live within them. She is a remote and spiritual deity, often spoken of in but the quietest of forests."),
        "hfd7729b4g7af7g4bafgb1e0gf0538b5e89d3": (1, "Mielikki, the Forest Queen"),
        # Bahamut
        "h767a26edg79ffg4143gbf67g754aa15055b4": (1, "Worshipper of Bahamut"),
        "he3352264g3b0ag4606gaba2g22dc1420a856": (1, "A servant of Bahamut, god of metallic dragons."),
        "hd33876a8gcd0ag45bfgbdb0gf51bf97640a2": (1, "Bahamut, the Justicemaker"),
        # Gruumsh
        "hcfc688d4gbc08g43efgb409ge172a7e5deeb": (1, "Worshipper of Gruumsh"),
        "hf614144agcd50g4df7g9ef4gb4adfb19fe31": (1, "A servant of Gruumsh, the one-eyed god of goblins."),
        "h77d39903g8583g42cfg8484g5d900d26d78f": (1, "Gruumsh, the One-Eye"),
        # Tiamat
        "h53c5d270gf312g4e10gaa2fg312f92b1e48a": (1, "Worshipper of Tiamat"),
        "h86fb9056g56f0g42d6ga96bgca11b8e255b3": (1, "A servant of the five-headed queen of dragons, Tiamat."),
        "h637a45d8g8878g4774g8181gc1ca4ffb01fc": (1, "Tiamat, the Many-Mawed"),
        # Bhaal
        "hc6ee7493gaf05g4cb6g97d8g6294ae8f9fbd": (1, "Worshipper of Bhaal"),
        "hea80b9bcg0582g4564g8c47gb5623831d694": (1, "Bhaal is the notorious god of murder. He once spread his heritage and sadistic impulses through all of Faerûn, then resurrected himself in a horrific ritual. His clerics are assassins, deliberately killing to honour their god."),
        "h1b5f0ca9g5430g472dgb1e7g213bf0c9fefa": (1, "Bhaal, Lord of Murder"),
        "h25ff1296g3e9cg4d44ga79egd2c29959b833": (1, "Bhaal is the implacable god of murder. His children, the Bhaalspawn, were responsible for a conflict that changed the face of Faerûn forever."),
        # Bane
        "hce83bf76gaa90g47ebga737g0bb10d2e5a07": (1, "Worshipper of Bane"),
        "h938aa5b2g94cbg4ed1gb7c2gc2869a85226d": (1, "Bane is the god of hatred, fear, and tyranny. His paladins are often remorseless commanders, leading armies dedicated to crushing the weak."),
        "h0928d60cgb897g4ab2g830cgf0a762e87251": (1, "Bane, The Black Hand"),
        "hd19f71a3gb275g4cb3gb988gde4730e91f16": (1, "Bane, the god of tyranny, believes himself to be the rightful ruler of every plane. His worshippers wield fear as a weapon, seeking to conquer all others in their path."),
        # Myrkul
        "hc79ed229g43bag45cagbf9age4dd89d86dbf": (1, "Worshipper of Myrkul"),
        "hfb2ee471g6de6g4660g8dabg6459caea65b4": (1, "Myrkul is the god of death and decay. He has few followers, but those who serve his faith inspire a fear of death in others, bringing doom wherever they tread."),
        "h0a40a3eag306eg44b7gb7cdg68e81bfbe523": (1, "Myrkul, Lord of Bones"),
        "hef8ac47eg7b6bg4c5ega9e0ge8d4ced1c548": (1, "Myrkul, also known as the Lord of Bones, is a god of death and necromancy. His wicked church seeks to put the fear of death - and thus, their lord - in any who pass their way."),
        # Worshipper of an evil god
        "h237ac7e6gba27g4263g8591gca942ea6dbe4": (1, "Followers of evil deities are driven to conquer and corrupt Faerûn in service to their gods. Shar, Bhaal, Bane, and Myrkul are common gods they worship."),
        "ha4468f32g1088g4cfcgb3a2g5d86fd13f098": (1, "Worshipper of an evil god"),
        # Worshipper of a neutral god
        "h9611d9e9g7b2fg4676gbdffgafc2780ce5b6": (1, "Followers of neutral deities uphold ideals of balance, fairness, and impartiality to further their faith. Helm, Kelemvor, Oghma, and Tempus are common gods they worship."),
        "h25c497f9g2925g4f08g87b2g40b8c459c7ab": (1, "Worshipper of a neutral god"),
        # Worshipper of a good god
        "h9964f550gb37ag4569gb377g1a5e8d51329f": (1, "Followers of good deities seek to better the world, empowered by their deities to heal others and destroy the undead. Selûne, Ilmater, Tyr, and Mystra are common gods they worship."),
        "h1daaf2a1g6b1bg4b95g91d6ga32493e80f01": (1, "Worshipper of a good god")
    }
    loca = bg3.loca_object(files.add_new_file(files.get_loca_relative_path()))
    loca.add_lines(content)

bg3.add_build_procedure('create_text_content', create_text_content)

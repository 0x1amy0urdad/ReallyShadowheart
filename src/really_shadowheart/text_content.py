from __future__ import annotations

import bg3moddinglib as bg3

from .context import files

########################################################
# Create custom strings, put them in english.loca.xml
########################################################

def create_text_content() -> None:
    content = {
        "h744690e1g4055g49b9gba6cgf175c791781f": (1, ""),
        "h8ce2f791g872eg4e96g9fc9g28bf3bf54a34": (1, "Rehearsal"),

        #
        # EA cut lines for reflection dialogues
        #

        # HAG_GurHunter_RD_ProtectedAstarion_Shadowheart
        "h8b4751f2g4391g412dg8f63gc05bf8c67056": (1, "What do you make of our encounter with the Gur monster hunter?"),
        "hfc1897b2g015ag4589gbe29gff4cf74aff01": (1, "He's one of us. I wasn't about to just betray him."),
        "hc1913f71g45e1g4388g9a08gbbef9784d018": (1, "He knows too much - safer to keep him with us than risk him exposing our condition."),
        "hbe191947g233fg4ef7gb172g415bdd40ba49": (1, "I just hope I don't come to regret standing by him."),

        # HAG_GurHunter_RD_BetrayedAstarion_Shadowheart
        "h4a382af4g128bg427dg8534g0d70b37f629b": (1, "It was the sensible choice. We've enough dangerous parasites in our midst already."),
        "h60393557ge940g4f75gae59g969fde0c36e7": (1, "What would you have done?"),
        "h99103040gfa01g4119g923egaf4365f8d6d6": (1, "I take it you don't approve?"),

        # DEN_CapturedGoblin_RD_Shadowheart
        "hfe0694dbg0061g4175gb808g7dd1e6216e92": (1, "Do you think helping that goblin was a good idea?"),
        "h8e40d0e4g5682g4becg9b95ga8ed381c9e67": (1, "This could very well end badly."),
        "hd5ab5d0ageff6g4d15g9fd1ge2b89983638b": (1, "Let's just hope Sazza remembers what we did for her."),

        # DEN_CapturedGoblin_RD_Shot_Shadowheart
        "hd128b7ffg3b6cg4d62ga6e5g3ce3e56b74d8": (1, "Tieflings are not above shooting caged prisoners. Good to know."),
        "h1f2acbeagf732g4949gb6edgfc1b26afa0a5": (1, "Good riddance."),
        "h5cf6685agca2bg46a7gb37cg20057becaebc": (1, "Letting her die like that didn't feel right."),

        # DEN_CapturedGoblin_RD_Healer_Shadowheart
        "hbf96955egebb7g46edgb7b2g5b84f10db31a": (1, "I can't believe we're going to seek help from a goblin healer."),
        "h03da7606g9062g4298ga35fgcbff2e1896f5": (1, "You're right. We have to investigate all leads, no matter how unsavoury."),
        "ha0d49ec1gbbaag4a7bga816gf133eaaae6b0": (1, "Venturing into a goblin camp? Sounds risky, to put it mildly."),

        # DEN_ShadowDruid_RD_KidDied_Shadowheart
        "hfbe84835g4054g4839g8131g7e08e7c89383": (1, "I didn't expect to find a viper's nest at the heart of the druid grove."),
        "h81035637g46d0g49ebgba34g354840f54aa8": (1, "I'm not dealing with child-killers, even if they do have a healer."),
        "h97820e55gb731g4d21ga969ge213b0d23b8c": (1, "I'm not dealing with child-killers. Doesn't matter if they can help us or not."),
        "h147c2a41g1b77g46a9gb35agdf188ca07c55": (1, "We could've stopped this but you held back. The child's death is on you as well."),
        "h681c54d6g5871g4a04g9744g891caf7f1ff2": (1, "I'm surprised you care. That little girl was nobody to you."),
        "hb12bfeaagab56g44fdga150g16a6349f918f": (1, "She tried to steal something precious to the druids - and paid the price."),
        "h5b7cadb0gf39dg4ceega647gcf122dea26d3": (1, "We should have done something. Maybe we could have saved her."),
        "h379b2d76gfb12g4851g845bgb2998b4a7581": (1, "I should have just attacked while I had the chance."),
        "h9c9ef589g432cg41b8g80a4g6ca8bcf03740": (1, "What will her parents say? We told them we'd help."),

        # DEN_Apprentice_RD_LockedUp_Shadowheart
        "hf3690a21g7aa9g4989g833eg7e134e2f536d": (1, "If I'm ever going to trust a druid again, please remind me of Nettie."),
        "h0ec85cefg0f8fg49c2g9716g1f566b7fdae7": (1, "Agreed. Telling the wrong person about our little problem could prove fatal."),
        "h7b65f7afgc1a1g4523ga3a3g56257996f45b": (1, "How do you expect to find help if we don't tell anyone what the problem is?"),

        # DEN_Apprentice_RD_Cyanide_Shadowheart
        "hd76b0332g14a4g40aag923ag09f88731c4ab": (1, "Well, at least this got us a free vial of poison."),
        "h4c03c093gef02g4258gbcf8g09ac9c185339": (1, "We went to the grove looking for a cure, but all we got is poison."),
        "h3d2fa92eg5accg4a1fgae8bgc7d33e163578": (1, "As a <i>very last</i> resort, yes. But not a pleasant notion all the same."),
        "h735fa879g5937g4f39ga162g0e4d6aca9f67": (1, "Sensible? Cowardly, more like. I haven't survived this long just to take my own life."),

        # FOR_PriestOfTheConqueringGod_Cultists
        "hf49b812fg1f2eg46c2gb455ge345905c1677": (1, "Another day, another tadpole... What do you think about it?"),
        "h856a7435gdde6g4c5ag8b26g95f10a46248a": (1, "These things live on even if we don't. All the more reason to find a cure."),
        "h9662455dg33f3g4b04gac47g9c9068cf8465": (1, "It was curious. Before he died, the host seemed oblivious to his tadpole."),
        "h5edf3529g1778g487egac48g4e93a5dabb7e": (1, "I'll be glad if I never have to see something like that again."),

        # FOR_BugbearLove_RD_AfterFight_Shadowheart
        "he87e92c1g8accg4a03g845fgdb5b0e8080aa": (1, "When I opened the barn door, I didn't expect to see &lt;i&gt;that&lt;/i&gt;."),
        "h4cb3264fg5f97g4c96g8552g9b5a2213d005": (1, "Things could have gone more smoothly, yes."),
        "h927af267gfab5g4691g9bbdg32d2b405bfb8": (1, "It would have been foolish to ignore a potential threat."),
        "hd3f708efg982bg4a07gbd98gd0fcf63c983d": (1, "We're lucky to have witnessed such a rare sight. A little curiosity is healthy."),

        # GOB_Checkpoint_RD_GoblinCampSneakIntro_Shadowheart
        "h3c811d37gd130g437cgb628g857e2fd18a2b": (1, "Judging by the stench, there are far more goblins than meets the eye."),
        "h8b4160c3ge0f9g458bg883cg74eede808efc": (1, "Indeed. Let's keep things discreet for now."),
        "h8d83d0aag5f12g4945g8c72ge7997846e38a": (1, "We could take them on. Numbers aren't everything."),
        "h1f259c06g38f0g44c9g81eeg2690864189ac": (1, "We only need to take out their leaders anyway. No point in making things harder on ourselves."),
        "hc5086a21gdd61g4fccg9ccag33d010647a2f": (1, "My blade thirsts for their blood."),
        "h74b9c7fbg9b00g4293g9f92gadeee6361b1f": (1, "I don't like this - walking through a camp of wicked creatures."),
        "hccb4dd99g8dc0g4e46gb56ag13184fc0c599": (1, "I'm not worried. I've outsmarted plenty of goblins before."),
        "h627b2b02g1572g4901gaab4g13e068fefa18": (1, "Being riled is the least that these creatures deserve."),

        # Gale_Recruitment
        "h3d86f328g1291g4680ga4f7g06c919eb06c2": (1, "Besides, looks like you keep some interesting company."),
        "hb40e2ddag4ab3g47c7g9861g22850b737c56": (1, "A woman with shadows for eyes - deep as the Darklake. A pleasure, madam."),

        "ha711ffbcg6a92g4bc7g92b8gfec9c20b4703": (1, "Last Light has been reduced to a pile of rubble..."),
        "hff4fc433ga337g4824g9fbagd9124e329177": (1, "A feast of death and pain... <i>glorious</i>."),
        "heefe6d89g2b87g4bccga3fcg4eaabf9319c0": (1, "&lt;i&gt;Tame yourself and change the subject.&lt;/i&gt;"),

        "h78686114g0677g4868g8905ge9213f98465a": (1, "So, the Gauntlet of Shar..."),

        "h17919bb2g242dg4852ga6degae6eaee08d11": (1, "It was wonderful. I really needed that..."),

        "h2fecd538g3b31g4d43g9d68g2a532e8bf910": (1, "Your whole life? It was taken from you. This is your last chance to take it all back. Like I did."),
        "h32377027g4a56g47b0ga826gcd17c6ead8aa": (1, "&lt;i&gt;Cite an excerpt from the book you both read a tenday ago, The Unclaimed.&lt;/i&gt;"),
        "h9c9dd9a6gcd6cg4adegbcddg4600f652dc0a": (1, "You turned away from Bhaal"),
        "haf5835e2g1f36g41a2gbfb6ga4b5550676d8": (1, "Viconia's fate is all too real"),
        "h7f65d54fg79d3g4abdgb0c9g2c09b329069a": (1, "Shadowheart lost faith in you"),

        "hca13afeag937fg43d6gbb06gff8f0a675b45": (1, "All that happened in the cloister, does it mean anything for what you and I share?"),
        "hfc1c1a85g0853g4dcbgb29bg0957807df0e1": (1, "I still can't believe you turned away from Shar. What comes next for us?"),
        "h2dc007d7ga4cdg4d87g9113g9940966c49d8": (1, "I just wanted to remind you, I'm here for you, if you need me."),
        "h620ae1d5g1041g4969gb2e0g56f9b5e9d1ae": (1, "Of course, it cannot be any other way."),
        "hbbfbc3ceg2938g41a2gaaf6gc5bb605da6f7": (1, "Yes, I do. I love you."),

        "ha711d2a9g2121g4a72g989agcd5c7cfa60a7": (1, "Shadowheart..."),
        "hd3542486g7197g41c1g840bgdebcac83aae9": (1, "Shadowheart?"),
        "h0c3be373g5b8dg474cg9d83gb5c0541854da": (1, "Sha... Jenevelle?"),
        "h295f5410g87edg4ae8gacd9g0435674745c5": (1, "Jenevelle?"),
        "h3a7c10c6g7b25g4695ga371g0a9504a60d9a": (1, "&lt;i&gt;Wait patiently.&lt;/i&gt;"),
        "h8d2f7d9ag2829g4d51gb7e1g026f4125b1d1": (1, "&lt;i&gt;Turn around and leave.&lt;/i&gt;"),

        #
        #
        #

        "h0007426egdc1ag4c38gb98cgf14f12078b3a": (1, "What?"),
        "h47e2da7eg3de5g4099gba00g4e24c73f6757": (1, "What's wrong with you? Can't you see that? For God's sake, talk to Shadowheart!"),

        "h4911fe70ge9e4g4a26g8245g2ac23f6ccbd6": (1, "I will commit an act of blasphemy against my goddess in exchange for a single kiss."),
        "h298e5b95g05c2g47e9ga0efg88498c299f74": (1, "Don't kiss me. Bite me. Make it hurt."),
        "h35785161gf2dag4d3cg8db5g2015f81e18ff": (1, "How much loss would warrant me another kiss? I am losing my mind because of you."),
        "h772fe651g90b6g4806g9c2dgca7e8b7128dd": (1, "I felt a divine touch the last time you kissed me. Kiss me again, let the darkness possess me."),
        "h95ce0b4bgf7dcg4218g9d40g1a7101bf3551": (1, "I &lt;b&gt;love&lt;/b&gt; you."),
        "h0d817f23g8ef3g4a75g8f69gdc6f6c6af9c4": (1, "&lt;i&gt;Sigh and say nothing.&lt;/i&gt;"),

        "hce7c0c72g0207g48d2g95eag63d16b3433c7": (1, "Halsin, tame yourself. Nobody's leaving. You know what's at stake, and you &lt;i&gt;will&lt;/i&gt; stop this quarrel."),
        "h46e2124fg95f5g4f56g810dg050666a9693c": (1, "Halsin, I read your diary in the grove. You redeemed yourself and lifted the curse. Stop the quarrel and help Minthara on her path to redemption."),
        "h2a032d7dg3c4eg42f1g91dfg7e1d157cbc7a": (1, "Halsin feels responsible for Isobel's death"),

        "h5d10372dga198g4191g89bcg07c774e0528e": (1, "To wipe out that deceptive smile from your smug face? Hell, yes.&lt;br&gt;You're as good as dead, Last Druid of the Former Grove."),
        "h68335c1dgfb26g4371ga60bg9f3a875df9d4": (1, "Stick to your Morals"),
        "hb5305b06g1ed5g4512gb17egcb10f5094603": (1, "Keep your dignity in an undignified place."),
        "he238353eg5b96g4969ga2cage6967553ee2f": (1, "When Less is More"),
        "h4f1100e2g4f18g41bagb467g64e8b4857895": (1, "Don't let your partner down."),
        "h93c12043g6cceg437cgb60eg8c0e6d55f466": (1, "Every day's an adventure when I'm at my love's side."),
        "h17d75cacg075bg4c4ag93eegb085da3f124e": (1, "Did you want something?"),
        "h2821bcd9g5940g4e36g908dgd97b9b1103cc": (1, "About those murals in the grove, you seemed to be intrigued... Why?"),
        "h8fd76834gff47g46a1ga97dgb43e95aa6962": (1, "Definitely, this isn't my cup of tea. You do you, and I go my way. Bye."),
        "h4b9a8445g655fg4fb0g9024g0a0ba786281a": (1, "A petty betrayer, you died by hands of your own companions. Well deserved and shameful death, you bastard!"),
        "h96c9a6d2gc5bfg4584g8badg883f003abf73": (1, "God's favourite princess."),
        "he9498ba4g20c8g491fgaa1eg91ef900f3da7": (1, "What do you feel?"),
        "h47ab25a9g984ag487fg87fcgf53f6f0939a3": (1, "You claimed back your stolen life. Everything will be fine."),
        "h7d99100fg9332g4ec3g8ff0gf438bba71a65": (1, "As a traitor to Lady Shar, you should feel shame - shame and dread."),
        "hf2a5e82ag0a76g41d3g8567g66b82c583fa9": (1, "May I hug you, Mom?"),
        "h33808f4bgb870g4fb2ga349g1e07c902ac97": (1, "I love you, Mom. We'll talk more later."),
        "h37557230gd8d3g4f9aga4c5gf62aa3431da5": (1, "I love you, Dad. Let's chat more later."),
        "hb1bbbc3fg1b4cg4e71g9adcg847742345a11": (1, "Dad, may I have a hug?"),
        "hd4092dd1g4eedg4d71g8f62gdd7bcbee39c5": (1, "Arnell, please take a look at spare clothes in the camp chest. Take anything you and your wife like."),
        "h2c5d201fgd8eag4bc1gb4a2gbf1158cce723": (1, "Emmeline, please take a look at spare clothes in the camp chest. Take anything you and your husband like."),
        "hef65e31dgcdc2g47b4g9622gd3f1b9c9377e": (1, "Dad, we have spare, clean clothes in the camp chest for you both."),
        "h7721fd74g9dc2g4582gb2dagf2d24e9c1d0d": (1, "Mom, we have spare, clean clothes in the camp chest for you both."),
        "haea72441gdfe6g41fcga75bg97af9661125e": (1, "I won't let you take my heart and my soul. I will only share my body with you."),
        "h58b582d2gb6ceg428dga83eg173f46859af9": (1, "I am sorry you had to watch what happened between me and Haarlep. Let's just forget we've ever been there, shall we?"),
        "hcd1956bag717cg4d73gbc9egfa85c62cf3b2": (1, "So, about that little incident with the incubus. We..."),
        "hf48e5c20g24d7g4ad8g8adag3c98a1515653": (1, "What is that look on your face? Is something wrong?"),
        "h4497715fg0105g43a9g8748g5f50dfa0cd30": (1, "&lt;i&gt;She has never truly understood me. I deserve so much more than just her.&lt;/i&gt;"),
        "hd8ceefa0g516eg4ad8gbbdeg509ecf2134f0": (1, "&lt;i&gt;She has nowhere else to go. She will cope, and she will stay with me.&lt;/i&gt;"),
        "hc36d812dgb030g48d9gb8ffg307186503100": (1, "&lt;i&gt;What am I doing? Have I lost my mind? I need to fight this ... thing.&lt;/i&gt;"),
        #"hd4281763g753cg4231g8db6g2281315827c4": (1, "Could you pretend to be an evil bhaalspawn for me?"),
        "hdf4bfc8eg13cdg433fgb980gf87262855ec4": (1, "Selûne teaches us to find our own paths through life. Perhaps, this is your path."),
        "h36708d75gaadbg4f8eg8965g538884c78db8": (1, "I've got a selunite prayer book. Perhaps, you might wanted to glance over it?"),
        "h0661e13bg0fa8g42cfgb4f9g1e03ce0351dd": (1, "I found a book. One of Ketheric's dark justiciars wrote it. You should see this."),
        "h1a6d0d4bga66bg4761gae2dg9eda3028262d": (1, "You might want to read this book, &lt;i&gt;The Unclaimed&lt;/i&gt;. Here, take it."),
        "h0e667597gc7c0g47ebg9e53g790f7da74b3f": (1, "I'm fine."),
        "hc587df2bg3b3cg44d9gbb8bg04b93d8bec79": (1, "Thank you, for being by my side through all of this. I'm glad we have each other."),
        "h4b4ff284g5083g5e63g9adfg8de423d3d883": (1, "A note from ReallyShadowheart mod author."),
        "h3f959d1cg8596g3b45g5b51gb0b61a33b9e1": (1, "Hello there&lt;br&gt;&lt;br&gt;If you read this, the mod was installed successfully and is working fine.&lt;br&gt;I hope you are enjoying your playthrough!&lt;br&gt;&lt;br&gt;--&lt;br&gt;Stan"),
        "h82afae29g158bg47c3g84d1g61088c55493a": (1, "Hi there&lt;br&gt;&lt;br&gt;If you read this, the mod was installed successfully and is working fine.&lt;br&gt;I hope you are enjoying your playthrough!&lt;br&gt;&lt;br&gt;--&lt;br&gt;Stan"),
        #"hefb469cbg616cg4481gbc6bgf799d5c6a704": (1, "My father had demanded you as a sacrifice to him once. I fear the worst."),
        #"hc211d57fg9125g4e24g8796g6d9a15c962e7": (1, "Now that you know my true nature, aren't you afraid of what lies ahead of us?"),
        #"hd892d8c5g541fg4565gbb4fg16cbfe9249f7": (1, "If I ever succumb into the madness again, kill me. For both of us."),
        "h714a3ffegcf05g4baagb188g29f1e509b3e6": (1, "This note is bound to your inventory. You cannot lose it."),
        "h73183838ga5b6g4c78gbc90g273486ca1dc2": (1, "YOU WILL CHOKE ON YOUR OWN BLOOD."),
        "hda03b2b0ga7d1g4114gad9cg678ae8cc2f03": (1, "I want to kiss you."),
        "h3a64ab5agbcb8g448fgaff6g28f09f3a3c98": (1, "I will help you to find and save your parents."),
        "h1240259dgc597g453cg8bacgb0fe544a5fdd": (1, "I felt the same. That little spark we shared, it is snuffed out now."),
        "hb6e5b7a3ged7dg44d3g9dcegfcc3ca6d0347": (1, "What are you talking about?"),
        "h1c32e152gd4adg4b31gac89gb05243bae1ff": (1, "What happened? What have I done to make you say that?"),
        "h875060d1g5ab3g49cag9993ge310a94ef55b": (1, "But why? I thought we're doing good together. Tell me what could I do for us..."),
        "h9be538c7g1ec6g43c7g89ebge43d29b981e3": (1, "I sacrificed my memories for Shar to preserve my mission. But one thing I do remember about myself is that I can't swim. I think it's time I remedied that. And washed off Shar's bile at the same time."),
        "h42d1b00bg51a3g4375gb34dge423a6fe72e8": (1, "I overheard you asking Shadowheart about swimming. What did you have in mind?"),
        "h33fbed16g06d2g47a3gaf9fg55c01a59603c": (1, "I told you already, didn't I? I am not interested. Stop that."),
        "hf932554dg421bg4db0gaab0g1b6dad0e484b": (1, "Halsin, you're a good friend, but that's about it. I don't see you the way you think I do."),
        "h77c85f76g5407g4987g96adg074ece30828f": (1, "&lt;i&gt;You noticed that Halsin has more to say. Keep silent and let him finish.&lt;/i&gt;"),
        "hb6f8b00fg8bd2g4a0dg973bg58b5fe96021a": (1, "&lt;i&gt;... muffled druidic noises ...&lt;/i&gt;"),
        "ha06ce793g2c90g4073gaa0dg676340b475ec": (1, "You have bonded with Shadowheart, body and soul. Her scent lingers on your skin. If there is to be anything between us, it must be with her consent, and ... her participation."),
        "h56f32cd2g389dg407cg98b4g002620edc107": (1, "*You feel a rush of outrage. Rage sparks to hatred.*"),
        "hf55f117bgd9a9g45bbgb3abg70ba0ffed6ed": (1, "&lt;i&gt;Breathe deeply but slowly, relax your clenched fists, and take emotions under control.&lt;/i&gt;"),
        "h56547ff0g9decg4039gb404g2dd49d28fe57": (1, "&lt;i&gt;Close your eyes and recall the World Tree cosmology of the Realmspace to calm yourself down.&lt;/i&gt;"),
        "h70cb2f3eg7015g4e6cgadd5gca8da9ec43df": (1, "&lt;i&gt;Repeat all sonnets of the Song of the North in reverse order and let the rage subside.&lt;/i&gt;"),
        "h5bed744cgf88fg416ega31dg27853909f664": (1, "&lt;i&gt;Get yourself together and calm down.&lt;/i&gt;"),
        "h0d6265a0gfce2g48c8gb6f2g9905ba2d35ee": (1, "&lt;i&gt;Give in to emotions.&lt;/i&gt;"),
        "hd61ea635g70b7g4dbega2cbg8579d2119875": (1, "If the only reason why you're here is to hit on me or Shadowheart, you have to reconsider your life choices. Leave us alone."),
        "hb039e2cdgda49g40bfg9419g2784b93a1f4c": (1, "You have a habit of intruding into private matters of your companions. Either stop that, or leave."),
        "h8d2960f1gbbd7g41e1g8972gfa991f70516f": (1, "What I and Shadowheart share, this is ours, and only ours. Please, leave us alone. Return to your own life."),
        "h63d7fa35g92c7g494cg9c10g6ad1182f85ec": (1, "My apologies, but you had it coming. Perhaps, it'd be better if you leave."),
        "h77628de1g5524g4f70g9fd4gff8298ee2ffe": (1, "&lt;i&gt;Look at him with disdain and say nothing.&lt;/i&gt;"),
        "h50379f60g5177g4986g89cage72e87dab0c9": (1, "Halsin's gone..."),
        "hdd530817g57ffg457fg853bg5665b8ba9d29": (1, "Hells, was that really necessary? Keep your hands to yourself."),
        "hc9d4a3begd325g43c3gbad9gba9afff1194e": (1, "&lt;i&gt;You're sure it was necessary, but you don't want to argue. Ignore her.&lt;/i&gt;"),
        "ha1b09cc8g23b1g4d8fg99fbg86cb2dfea5f2": (1, "Yes, that was necessary. He had it coming. How dared he speak to me like that? He's lucky to be alive."),
        "hbc4712f9g33ceg470fgaa3bg4d7e0cfa2828": (1, "I taught him a good lesson. Had he as much as touched you, he'd be lying dead now."),
        "h91f8224eg4917g4f31g91d5gc01933960797": (1, "I'm sorry, I really am. I lost my head the moment he said &lt;i&gt;that&lt;/i&gt;. He treated us like his toys, and our bond like a passing indulgence."),
        "h6d35fcc7g133cg47b9gad16g9dbdc0e3d5ce": (1, "What I did was uncalled for. It won't happen again."),
        "h72247b7dg8cadg42b2gba2bgc722a51e01be": (1, "I want you to know, you mean the world for me."),
        "h9dda2c14geaafg4a47gb232gb1dcd163d524": (1, "&lt;i&gt;You feel embarassed by your own actions. You can't find the right words to say, so you just hug her.&lt;/i&gt;"),
        "hc41af286gefabg4061gbe97g5786d98267ac": (1, "&lt;i&gt;Kiss her.&lt;/i&gt;"),
        "h1329b6fcg3af2g4116gb1f0g724131178f2e": (1, "&lt;i&gt;Play the strong, silent type.&lt;/i&gt;"),
        "h817752ecg4935g4a31g9ea7g35c3b014b249": (1, "Shadowheart is irresistable."),
        "he112f6b7gfd35g4cabg97dag817ab8be7767": (1, "*You succeeded... and you failed! Hmmm, at least you tried.*"),
        "h1d948c45g9286g4881ga6fegb4be459ce4b0": (1, "I suppose you're right. On both counts."),
        "h125217edg1082g4ad3g9b56g5b01a63b6b54": (1, "Arnell, I would like to ask for your blessing."),
        "h546e7566g6d98g4af1gb48fgeffb8d0a5de2": (1, "Emmeline, I would like to ask for your blessing."),
        "heab327e2gc976g4342ga0bfg894d952f25b5": (1, "I thought Lady Shar blessed you, yet the shadows hurt you. Do you want to talk about that?"),
        "h5e78e8b3ga141g4fdegaf94gb6848de17210": (1, "I'm not sure I'd agree, but ... very well."),
        "hc5db671eg0534g4598g948age7537f10f15d": (1, "I want to pray with you. Perhaps, the Nightsinger would be pleased and the shadows would spare you next time."),
        "h568ddb44g1bd5g4869g92aagf46a058edead": (1, "You said you're blessed and shadows can't hurt you. Did you anger your Lady Shar? Are you losing your blessing?"),
        "h8d40543bg23c0g45b7g924ag253d16e26545": (1, "Apparently, the Nightsinger only values you this much. It's good to know where the limit is, don't you agree?"),
        "h8d184815g3f6bg4475ga4e4g3677cafbd52b": (1, "&lt;i&gt;Carefully repeat every word.&lt;/i&gt;"),
        "h72bfa66dg9e41g4110ga2f3g8f7193f10092": (1, "See our actions, Lady Shar. Hear our words of faith."),
        "h662f6ae0g3786g473dgbfa8g3671968c6418": (1, "Ugh, this is embarrasing. I am not saying that. I don't serve Shar."),
        "he2c5ddc7gca8cg4416g80e2gd093b49f75ce": (1, "&lt;i&gt;Suppress your feelings and focus on repeating what she said.&lt;/i&gt;"),
        "hb4d4bfeag236eg4cd4g93dfgb2bfa840649b": (1, "Guide us to your perfect, eternal darkness."),
        "h0472ed53gbcf9g41e6g9d2agf231e8aca0e9": (1, "I don't see a thing in the darkness."),
        "hc39de06egc1a2g4e15gab05ga64464313bfa": (1, "&lt;i&gt;Snuff your inner protest and repeat after her.&lt;/i&gt;"),
        "ha33826a2g3260g412bga68fg161e7f5a694b": (1, "Empower us to slaughter the heretics."),
        "hd3ca3c69g6507g497cg9193g23ea94a8f784": (1, "Day-night cycles seem to be a better alternative to eternal darkness."),
        "hc2b9bd3cg7c82g4e90gb0e5g144b6c8a8d26": (1, "Her will could only be done over my dead body."),
        "h92e55267ga65ag4dfdgadcfgebb601a079ee": (1, "I want to pray with you to your goddess."),

        "h208de7e1g4c8bg4828ga771g0d5ae624e63d": (1, "Am I? I thought we were doing great together, but now I am not sure."),
        "hc70f7dfdg98e7g4e41g9ee4g88a6502124c8": (1, "Had I done something? Something that upset you? Tell me, I could do better next time."),
        "h2756a7e4g929eg4533g9b0cgf5232e323f14": (1, "Why, I didn't expect to hear you speaking like that."),
        "h132e0bdege62fg43d1ga95fg11c17111e614": (1, "But it's the opposite, isn't it? You were trying to get my attention lately."),

        "h6a2c1bbbg2dfcg4525g93eag287aaea2de8f": (1, "You don't sound like yourself since we arrived here. Should I be concerned?"),
        "h6d4158c7g11aag4eedg9d70g2811e83a7800": (1, "You hesitated to tell me something. What's bothering you?"),
        "hff321ee7g55dfg47a7g8ca3ga842eb015d0e": (1, "I can do better. I just need to know what I did wrong."),
        "hd5cd72bcg5c33g48adgbce9gec28e4c84b0f": (1, "Well, you can always find someone else who is not that different."),

        "h862a65d3g8f8fg46b7gb8afga7dc2ad11479": (1, "There's something I wanted to tell you. Something that was on my mind since I met you."),
        "h82e6c111g7e35g4b7fgba0egec25bbbe117a": (1, "Since the time I first saw you in that pod, I changed... no, you changed me. My life has a new meaning: you."),
        "h4d23cd12ga6fdg4485ga129g9ffda516643f": (1, "We are thrown together by dire circumstances, yet the brief time we shared was more precious than all my years."),
        "hd386265bgaf96g421bga57eg8d9ffdeeb899": (1, "I can't remember much of myself, and what I remember is a crimson mist... until you. You saved me. I am no Bhaal's Chosen. I am yours."),
        "h7ecf542bgf7c8g410dga109gb838c82a324e": (1, "I sneaked into the most protected vaults, stole countless treasures... only to find that my heart is stolen too. By you."),
        "h2058154fgca15g4c4dg81a9g331986e63a86": (1, "&lt;i&gt;Read a long, emotional, and sad love poem that you wrote for her.&lt;/i&gt;"),
        "h2c35be55g4742g47abgbdccg534dfa831e3e": (1, "Come here..."),
        "h5cf45132g69fdg45ceg9483g7b67354eb3ec": (1, "Love you."),
        "h8ba27ee6g443bg49cag82eagf508a23378d5": (1, "My love..."),
        "hbede93d1gcdd7g4c3cga77egca1774fbd7b8": (1, "My love... come here."),
        "hb23e9145g96dcg4946g85e2ga984fb7ac751": (1, "When I woke up this morning, I listened to your gentle snores for a while. I am the happiest man alive. I love you."),
        "h35801df6g8e05g4eefga058g983fa676324d": (1, "When I woke up this morning, I listened to your gentle snores for a while. I am the happiest woman alive. I love you."),
        "h10588bf1gd0c4g4b91g90cdg7442250d8d4a": (1, "I love you."),
        "h91c7ed29gaec4g4388g8655g77ae1647ebe7": (1, "Love you too."),
        "h2b8d754egf05bg4f89g8ae0gacf81a83ad38": (1, "&lt;i&gt;Say nothing.&lt;/i&gt;"),
        "h7df66cf3g43c8g4d4dg9581ga29d9779951b": (1, "Oopsie, my love, I accidentally clicked the wrong option in the dialog."),
        "hd6147aa7g76feg48a5g8c11g3f734c02a5a4": (1, "I realized we are too poor of a match. It'd be better to end this now."),
        "h1e8574a0gb5d2g48abg95a9gbe6264723760": (1, "I want to talk about us."),
        "hd896e304g5fc4g41e7g807cg524360fee6a9": (1, "I truly love you."),
        "hc8894122g2583g49fagb874gec6395df6db3": (1, "I don't feel it. It's over. My nightmare is gone."),
        "hf7fae672g1197g4ba1gbc2bg5c2362431368": (1, "I am here. I am with you. Come here."),
        "hbc1e6032gcbebg4226ga889gd7d1e7b7a121": (1, "&lt;i&gt;Words got stuck in your throat. Embrace her.&lt;/i&gt;"),
        "h35eecf11g59ceg496bg9d60g37fe40337891": (1, "You were looking at me like you wanted to say something. Don't be shy, tell me."),
        "h1717338fga82bg4f20ga158g6dbca07e41f3": (1, "We should've had wine more often. More warming than the fire."),
        "h0d248adbg6d7cg4e55gb525gd439c5d526d9": (1, "You don't need wine if you have me. I can keep you warm all night. There's room for you in my bedroll."),
        "h1cde79d9g165bg4f6fg9025g57881c3491f6": (1, "Did you manage to save one of those liberated vintages? I'd gladly kill a bottle or two."),
        "hc792b085g2c19g430fgb461g700fd3588775": (1, "There's more than one way to keep me warm."),
        "hc875bd6cgdffag4bc1gb668g133a1cf06ba5": (1, "There's room for you in my bedroll. And the bottle."),
        "h9a16a3c8g8292g4e7ag93f0g2b5e721d602e": (1, "I can't help but notice you seem happier of late. There's a spring in your step that wasn't there before."),
        "h9f205acbg8e31g462bgbfbbg956e9f1fb647": (1, "I'm not sure I want to know..."),
        "hd559506cg8e88g4afcg8035g762fee0051d7": (1, "What you said about our time together... What did you have in mind?"),
        "he3a0d778g05c4g4a26gaffcg576978f906a7": (1, "I want to ask you about something you mentioned earlier."),
        "h203c71e0g0992g46b8g939eg52adc1d0d7c7": (1, "Let's talk about something else."),
        "h198df115g788ag4de4g9ccfg5c8e82bc10f8": (1, "Let's keep that our special secret. Oh you know what I mean..."),
        "he7d56031g63c2g4a69gacdcg1151b2bfc3b1": (1, "Shadowheart is in love with you"),
        "hcce3a355g2e43g4231g94fdg0d16de9a5cb8": (1, "No... it can't be true..."),
        "h79ae6514g939dg49eega50eg86bbf7381a35": (1, "I... it's difficult for me to talk about..."),
        "hd0509e5dgee24g4e38g9e53gd72e5795cba6": (1, "Checking in on me? I'm right where I'm supposed to be - with the man I love."),
        "hfee6d489g9f92g4b08gad5egcde430d9f6e3": (1, "&lt;i&gt;Wipe a happy tear and kiss her.&lt;/i&gt;"),
        "heb4bc4d7g7624g48b7g8200g7c599b41938f": (1, "We should take your parents with us to the next party, if Withers calls us again."),
        "h6af6d9f8gede1g482fg8cc6g0cecb08e0cfa": (1, "Wait, are we... expecting? Do you really mean that?"),
        "haadd3e89g0eeeg4514g9cf2g3a73b36b9f98": (1, "Did you just say that we are expecting?!"),
        "h8e6de288g61c0g4ff3g8e6dga6505c33e960": (1, "Did you just say Selûne heard our prayers? Am I an expectant spouse now?"),
        "hab27fa75ge385g4d81g8b81gca48789e9a7b": (1, "I do hope your parents would step in and help us with our new trouble..."),
        "h460ba56dgd453g4e9cgbd11g1a7133b34cbe": (1, "Children are source of trouble, do you know that?"),
        "hcb948f33g2863g49d1g8074g267265978b66": (1, "&lt;i&gt;Pay no attention to that and move on to other matters.&lt;/i&gt;"),
        "hed5250f0g98dag42efga79ag3b0d5fb8f44c": (1, "I deserve to be hated for what I did. All I can say, don't leave me... although I cannot give you a reason not to."),
        "hbf3e9b58gce14g484bga545g9cfb5645c4cb": (1, "If we agree on that, we can turn the page now, shall we?"),
        "h757179ffg608bg47e6gaf76gb55db99ca2c8": (1, "Are you being sarcastic now?"),
        "h9188942ag8b41g4e68g894ag277ae309838f": (1, "We need allies for the fight to come. I tried to win Mizora's favor. I have no feelings for her."),
        "hfb28a99dg8cc8g4ad3g879bg6f843e2112d8": (1, "I do mean it. I regret every moment I spent in the Hells with Mizora."),
        "hfc18b96ege9ccg484ag946fg3aa2a789e477": (1, "You don't believe me, do you?"),
        "h52c04688gf4a9g4178ga99eg7f58bfe6fae5": (1, "I admit it, I was a fool and I regret what I've done. You must be hating me, and I absolutely deserve that."),
        "h1f7912b4g8b72g46ceg9e8bg8c9874f03472": (1, "Don't be foolish - you're far too handsome to hate. I'll still pet you as much as you like."),
        "hd9da4525g93d3g45e4g89b1g36bbc09cae31": (1, "Don't be foolish - you're far too pretty to hate. I'll still pet you as much as you like."),
        "h63ebfa3egc78eg487cga031g3cbc4b395e4a": (1, "You saw me with Mizora that evening, did you? Why didn't you talk me out of it?"),
        "hee80ea70g5160g490agac63g98f23b7d0501": (1, "Listen, Shadowheart. She's a half devil, she charmed, she tempted me. It meant nothing, I swear."),
        "hec9703c4g433cg4352gbfb1g5804f86ec900": (1, "This seems to be a perfect night to build a few sandcastles, don't you think?"),
        "h06a5cd66g501bg402bgb1e3g41bd32d9ca18": (1, "Others seem quite tired, they'll be asleep soon. Don't you think we could seize the opportunity?"),
        "h0a14be70g6828g4ed5g8202g288788d68b6e": (1, "What more could I need? If I had all that, and I had you... Yes. I want to share everything that lies ahead of me with you."),
        "h0d2027f1g386eg45bbg8a6ag7ab77f651a6c": (1, "A lot's changed since then. More than I ever thought was possible."),
        "h11a84dedgd2cbg46bfg8b92ga6c48d37a486": (1, "I really fell for you, you know. But then... You've changed, and not for the better. I can't be at such odds with you and be your lover. Not anymore."),
        "h2155d8e8g3584g48fbg95fdg5651ebed00ee": (1, "I want to spend my life with you. Would you marry me?"),
        "h40c1c09egd7bcg4575g8a9dgd8ee7a05e75d": (1, "Wait until the others are asleep, then come with me... Get some rest while you can."),
        "h4e692070gf12fg40e1g9b36ge64802670e20": (1, "Wait, I don't want to lose you... I want to be with you..."),
        "h5de64a8eg404fg4151ga564g5956eab0a0f4": (1, "Perhaps, you're right. It would be best for us if we end what we had."),
        "h5def25a4gf970g4dadgbb68gec13e203facc": (1, "I'm just trying to get you jealous, my love. Of course I wasn't going to do that."),
        "h694c1b90g4377g41b0gb07dg4a108f59fa65": (1, "I do not serve Shar anymore. Nor the Mother Superior."),
        "h6d9862b7g728fg4822ga5f3g658e9bfc16d3": (1, "What do you mean?"),
        "h78c89a38g324bg4a2cg9a76g58d634b668bf": (1, "Must I? Honestly, I'm still not used to being married - it's almost a surprise... But a very pleasant surprise."),
        "h7b905a4fgda7dg4417g9c24g768f4ef486e4": (1, "While it's a fascinating prospect, I'd like you all to myself..."),
        "h9635e41bge285g4f12gb61bg13692d55fba6": (1, "I didn't realize your feel this way. I want to be with you... Forget I ever said anything."),
        "h9a474f8dg36b3g4089gbf4aga01c55224234": (1, "Surely you wouldn't mind if I had a bit of fun? I am my own person, after all."),
        "h9b00b4fbgd0e0g4bbcgadc0gdbea99682ab5": (1, "It's difficult to put into words... I can't remember the last time I sought to confide in someone like this - maybe I never have, for all I know. But now it just feels... right."),
        "h9e23c5abg5a55g46c6g949fg4c089b18300f": (1, "You must be keen to get back to our cosy cottage, don't you?"),
        "ha0b56eb6gbc0bg4535g97efga2b7c2671c58": (1, "&lt;i&gt;Loot her belongings.&lt;/i&gt;"),
        "hc0077229g09edg4ed4gb446g6e6f48cf2363": (1, "Your father is right. This is the only way to free your family from Shar's curse and stop the pain."),
        "hd86ce9a8g7a59g49ddgad72g6f87d1c370dd": (1, "You're a bad liar... Don't treat me like an idiot, please!"),
        "hf070d2bag8b3cg4918ga17dg7f009caa75dc": (1, "I am free to do whatever I want. Leave, if you have a problem with that."),
        "hf278c5d2g81beg46abgaa45g649a20dfeb09": (1, "Our relationship was... fleeting. I want to move on."),
        "hbb1bd14dg56f9g40f3g8ee9gb7353e6d6d04": (1, "[This is an ancient notebook, whose ink is faded and pages are starting to crumble. It's not easy, but some words can still be made out.]&lt;br&gt;&lt;br&gt;&lt;br&gt;How do you describe events like these? An accident? A tragedy? The cruelty of fate?&lt;br&gt;It does not matter. Isobel is just as dead. &lt;br&gt;&lt;br&gt; I can't remember what happened with any clarity. We were negotiating. She with [...] I led the druids. [...] words grew heated [...] threw the first punch. It was mayhem. &lt;br&gt;[...] stared at me, my glaive's blade buried in her stomach and shock in her eyes. I can't believe she wanted to hurt me. It was pure instinct - the heat of combat. &lt;br&gt;&lt;br&gt;[...] washed the blood from my hands. My glaive was still there, coated in her blood, but something else felt different. There's a sickness in the blade. It seems cursed, but by whom? Selûne herself? &lt;br&gt;&lt;br&gt;It is locked away now. I do not trust its power in the wrong hands. And I never want to see it again."),
        "h2a7a961bg5a07g4adbgbab8g56db98e84814": (1, "I'd love to help you wash all that sand out of your hair."),
        "h93d2e7aeg716eg463fga1dag2f1110664d35": (1, "You don't waste time, do you?"),
        "h18ffbc26g6b50g4068g8b32g273ff82086a0": (1,  "Yes. I ... love you."),
        "h8aa24494g5c0dg400dg810bg94afbed5b8fd": (1, "Did the noblestalk help you recall anything from your past?"),
    }
    loca = bg3.loca_object(files.add_new_file(files.get_loca_relative_path()))
    loca.add_lines(content)

def create_string_keys() -> None:
    strings = bg3.string_keys.create_new(files, 'Misc')

    # The original druid diary from EA
    strings.add_string_key('hbb1bd14dg56f9g40f3g8ee9gb7353e6d6d04', 'DEN_DruidLair_CreepyDiary', text_version = 1)

    # The new game over reason for petty betrayers
    strings.add_string_key('h4b9a8445g655fg4fb0g9024g0a0ba786281a', 'GameOver_Betrayal')

    # For dummies who are about to miss the skinny dipping scene
    strings.add_string_key('h47e2da7eg3de5g4099gba00g4e24c73f6757', 'ReallyShadowheart_TalkToHer')



bg3.add_build_procedure('create_text_content', create_text_content)
bg3.add_build_procedure('create_string_keys', create_string_keys)

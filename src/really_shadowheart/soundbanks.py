from __future__ import annotations

import bg3moddinglib as bg3

from .context import files

#################################################################
# Soundbank: Shadowheart, 3ed74f063c6042dc83f6f034cb47c679.lsf
#################################################################

def create_shadowheart_voice_metadata() -> None:
    soundbank = bg3.soundbank_object.create_new(files, bg3.SPEAKER_SHADOWHEART)
    soundbank.add_voice_metadata('h7b905a4fgda7dg4417g9c24g768f4ef486e4', 04.801)
    soundbank.add_voice_metadata('h0d2027f1g386eg45bbg8a6ag7ab77f651a6c', 04.334)
    soundbank.add_voice_metadata('h9b00b4fbgd0e0g4bbcgadc0gdbea99682ab5', 14.938)
    soundbank.add_voice_metadata('h40c1c09egd7bcg4575g8a9dgd8ee7a05e75d', 06.506)
    soundbank.add_voice_metadata('h0a14be70g6828g4ed5g8202g288788d68b6e', 12.000)
    soundbank.add_voice_metadata('h78c89a38g324bg4a2cg9a76g58d634b668bf', 13.176)
    soundbank.add_voice_metadata('hd86ce9a8g7a59g49ddgad72g6f87d1c370dd', 05.338)
    soundbank.add_voice_metadata('h11a84dedgd2cbg46bfg8b92ga6c48d37a486', 05.338)
    soundbank.add_voice_metadata('h1f7912b4g8b72g46ceg9e8bg8c9874f03472', 08.684)
    soundbank.add_voice_metadata('hd9da4525g93d3g45e4g89b1g36bbc09cae31', 07.891)
    soundbank.add_voice_metadata('hcce3a355g2e43g4231g94fdg0d16de9a5cb8', 01.321)
    soundbank.add_voice_metadata('h744690e1g4055g49b9gba6cgf175c791781f', 00.250)
    soundbank.add_voice_metadata('h198df115g788ag4de4g9ccfg5c8e82bc10f8', 06.864)
    soundbank.add_voice_metadata('hd0509e5dgee24g4e38g9e53gd72e5795cba6', 05.696)
    soundbank.add_voice_metadata('h79ae6514g939dg49eega50eg86bbf7381a35', 05.251)
    soundbank.add_voice_metadata('h9a16a3c8g8292g4e7ag93f0g2b5e721d602e', 08.900)
    soundbank.add_voice_metadata('h9f205acbg8e31g462bgbfbbg956e9f1fb647', 05.477)
    soundbank.add_voice_metadata('h1717338fga82bg4f20ga158g6dbca07e41f3', 03.967)
    soundbank.add_voice_metadata('hc792b085g2c19g430fgb461g700fd3588775', 02.700)
    soundbank.add_voice_metadata('hd896e304g5fc4g41e7g807cg524360fee6a9', 01.873)
    soundbank.add_voice_metadata('h2c35be55g4742g47abgbdccg534dfa831e3e', 00.842)
    soundbank.add_voice_metadata('h5cf45132g69fdg45ceg9483g7b67354eb3ec', 00.760)
    soundbank.add_voice_metadata('h8ba27ee6g443bg49cag82eagf508a23378d5', 00.765)
    soundbank.add_voice_metadata('hbede93d1gcdd7g4c3cga77egca1774fbd7b8', 02.347)
    soundbank.add_voice_metadata('h25ae89f3g08c4g47fegb737gb796065444b0', 05.686)
    soundbank.add_voice_metadata('h5e78e8b3ga141g4fdegaf94gb6848de17210', 03.942)
    soundbank.add_voice_metadata('h50379f60g5177g4986g89cage72e87dab0c9', 05.638)
    soundbank.add_voice_metadata('hdd530817g57ffg457fg853bg5665b8ba9d29', 05.233)
    soundbank.add_voice_metadata('h1d948c45g9286g4881ga6fegb4be459ce4b0', 02.950)
    soundbank.add_voice_metadata('h9be538c7g1ec6g43c7g89ebge43d29b981e3', 17.206)
    soundbank.add_voice_metadata('hc587df2bg3b3cg44d9gbb8bg04b93d8bec79', 09.367)
    soundbank.add_voice_metadata('h0e667597gc7c0g47ebg9e53g790f7da74b3f', 09.367)
    soundbank.add_voice_metadata('h93c12043g6cceg437cgb60eg8c0e6d55f466', 03.216)
    soundbank.add_voice_metadata('h17d75cacg075bg4c4ag93eegb085da3f124e', 01.502)
    soundbank.add_voice_metadata('h0007426egdc1ag4c38gb98cgf14f12078b3a', 00.637)
    soundbank.add_voice_metadata('h93d2e7aeg716eg463fga1dag2f1110664d35', 01.710)

def create_creep_voice_metadata() -> None:
    soundbank = bg3.soundbank_object.create_new(files, bg3.SPEAKER_HALSIN)
    soundbank.add_voice_metadata('hb6f8b00fg8bd2g4a0dg973bg58b5fe96021a', 09.975)
    soundbank.add_voice_metadata('ha06ce793g2c90g4073gaa0dg676340b475ec', 14.000)

def create_narrator_voice_metadata() -> None:
    soundbank = bg3.soundbank_object.create_new(files, bg3.SPEAKER_NARRATOR)
    soundbank.add_voice_metadata('h56f32cd2g389dg407cg98b4g002620edc107', 05.954)
    soundbank.add_voice_metadata('he112f6b7gfd35g4cabg97dag817ab8be7767', 06.965)

def create_gale_voice_metadata() -> None:
    soundbank = bg3.soundbank_object.create_new(files, bg3.SPEAKER_GALE)
    soundbank.add_voice_metadata('h3d86f328g1291g4680ga4f7g06c919eb06c2', 04.166)
    soundbank.add_voice_metadata('hb40e2ddag4ab3g47c7g9861g22850b737c56', 06.982)



bg3.add_build_procedure('create_shadowheart_voice_metadata', create_shadowheart_voice_metadata)
bg3.add_build_procedure('create_gale_voice_metadata', create_gale_voice_metadata)
bg3.add_build_procedure('create_creep_voice_metadata', create_creep_voice_metadata)
bg3.add_build_procedure('create_narrator_voice_metadata', create_narrator_voice_metadata)

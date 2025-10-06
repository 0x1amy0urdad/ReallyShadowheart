from __future__ import annotations

import bg3moddinglib as bg3

from .context import game_assets

ASSETS : dict[str, dict[str, str]] = {
    # 'CAMP_FARM_SleepCutscene': {
    #     'dialog_uuid': '7bfa521a-93c7-4c5e-bab8-3f2fc3d2c3e0',
    #     'timeline_uuid': '8bed768f-0550-40c1-9a4b-afa5ec4eacab',
    # },
    # 'CAMP_SLUMS_SleepCutscene': {
    #     'dialog_uuid': '93b41f8a-8e8f-4b8f-bb1c-9d4ba6bf15c8',
    #     'timeline_uuid': 'ff0394f0-e392-4d2e-bfbe-36232aaaed5d',
    # },
    # 'CAMP_ELFSONG_SleepCutscene': {
    #     'dialog_uuid': '4d112f3a-dfa0-4299-96ac-144a6c8dae0d',
    #     'timeline_uuid': '9522481b-1e32-4d9e-972e-414d7bb4cc18',
    # },
    # 'Shadowheart_InParty': {
    #     'dialog_uuid': 'e7426efd-91c4-4800-ba21-dca78c316375',
    #     'timeline_uuid': '155e408a-bd27-42e3-88ba-1c00471f4875'
    # }



    # Shadowheart dialogs
    'Shadowheart_InParty': {},
    'ShadowHeart_InPartyEND': {},
    'ShadowHeart_InParty2_Nested_BackgroundChapter': {},
    'ShadowHeart_InParty2_Nested_CityChapter': {},
    'ShadowHeart_InParty2_Nested_DefaultChapter': {},
    'ShadowHeart_InParty2_Nested_OriginChapter': {},
    'ShadowHeart_InParty2_Nested_Romance': {},
    'ShadowHeart_InParty2_Nested_ShadowCurseChapter': {},
    'ShadowHeart_InParty2_Nested_ShadowheartHug': {},
    'ShadowHeart_InParty2_Nested_ShadowheartKiss': {},
    'ShadowHeart_InParty2_Nested_SharranChapter': {},
    'Shadowheart_InParty_Nested_TopicalGreetings': {},

    # Shadowheart romance cutscenes
    'CAMP_Shadowheart_Nightfall_SD_ROM': {},
    'CAMP_GoblinHuntCelebration_SD_ROM_NightWithShadowheart': {},
    'CAMP_Shadowheart_SkinnyDipping_SD_ROM': {},
    'END_GameFinale_RomanceFates_Shadowheart': {},

    # Shadowheart's CRDs, CFMs, and SDs
    'CAMP_Shadowheart_IVB_CFM_WildMagic': {},
    'CAMP_NightsongShadowheartVisit_CFM': {},
    'CAMP_Shadowheart_CRD_SkinnyDippingRomance': {},
    'CAMP_Shadowheart_DaughterTears_SD': {},
    'CAMP_MizoraMorningAfter_CFM_ROM': {},

    # Shadowheart's parents
    'CAMP_ShadowheartFather': {},
    'CAMP_ShadowheartMother': {},

    # Shadowheart's origin moments (AOMs, OOMs, COMs)
    'SHA_NightsongsFate_OM_Shadowheart_AOM_OOM_COM': {},
    'GOB_SeluneTemple_OM_ShadowHeart_COM': {},
    'FOR_Owlbear_OM_Shadowheart_COM': {},

    # Shadowheart recruitment
    'ShadowHeart_Recruitment_Beach': {},
    'ShadowHeart_Recruitment_Den': {},

    # Epilogue
    'EPI_Epilogue_Shadowheart': {},

    # Cloister
    'LOW_HouseOfGrief_OM_Shadowheart_COM': {},
    'LOW_SharGrotto_ConfrontViconia_OM_Shadowheart_COM': {},
    'LOW_SharGrotto_ViconiaDefeated_OM_Shadowheart_COM': {},
    'LOW_SharGrotto_ParentsFate_OM_Shadowheart_COM': {},

    # Tutorial
    'TUT_TransformChamber_PodLock': {},

    # Dark Urge
    'LOW_BhaalTemple_PostBattleDarkUrge_Resistance': {},

    # Night sleep cutscenes
    'CAMP_FARM_SleepCutscene': {},
    'CAMP_SLUMS_SleepCutscene': {},
    'CAMP_ELFSONG_SleepCutscene': {},

    # Camp
    'CAMP_Night1_CRD_Shadowheart': {},
    'CAMP_Night2_CRD_Shadowheart': {},
    'CAMP_Night3_CRD_Shadowheart': {},
    'CAMP_Shadowheart_IVB_CFM_LaezelFight': {},

    # Grove
    'DEN_Apprentice_Cyanide': {},
    'DEN_CapturedGoblin': {},
    'DEN_CapturedGoblin_GuardsAvenge': {},
    'DEN_General_Squirrel': {},
    'DEN_ShadowDruid_SnakesCourt': {},

    # World
    'LOW_HouseOfHope_ROM_Incubus': {},
    'WYR_DapperDrow_Intimacy': {},
    'WYR_DapperDrow_SiblingsThreeWay': {},
    'GOB_DrunkGoblin': {},

    # EA related stuff
    'HAG_GurHunter': {},
    'HAG_GurHunter_OM_Astarion_COM': {},

    # Astarion
    'Astarion_InParty2_Nested_TopicalGreetings': {},

    # Gale
    'Gale_InParty2_Nested_TopicalGreetings': {},
    'Gale_Recruitment2': {},

    # Karlach
    'Karlach_InParty_Nested_TopicalGreetings': {},

    # Lae'zel
    'Laezel_InParty2': {},
    'Laezel_InParty2_Nested_TopicalGreetings': {},

    # Wyll
    'Wyll_InParty': {},
    'Wyll_InParty2_Nested_TopicalGreetings': {},

    # Minsc
    'Minsc_InParty': {},
    'Minsc_InParty_Nested_PersonalQuestions': {},

    # Jaheira
    'Jaheira_InParty': {},
    'Jaheira_InParty_Nested_TopicalGreetings': {},

    # Minthara
    'Minthara_InParty': {},
    'Minthara_InParty_Nested_TopicalGreetings': {},
    'Minthara_InParty_Nested_PartyMemberThoughts': {},
    'CAMP_Halsin_Minthara_CFM_Confrontation': {},
 
    # End game
    'END_BrainBattle_CombatOver_Nested_StandardIntro': {},

    # Creepy stuff
    'CAMP_HalsinsRevenge_CFM': {},
    'Halsin_InParty': {},
    'Halsin_InParty_Nested_Polyamory': {},
    'Camp_Act3_CRD_HalsinRomance': {},
    'Halsin_Warning1': {},
    'Halsin_Warning2': {},
    'Halsin_Leaving': {},
    'PB_Halsin_Shadowheart_ROM_Act3_Selune': {},
}

ASSETS_OVERRIDES : dict[str, dict[str, str]] = {
    # Shadowheart dialogs
    # 95ca3833-09d0-5772-b16a-c7a5e9208fe5
    'Shadowheart_InParty': {
        'dialog_uuid': '7bfa521a-93c7-4c5e-bab8-3f2fc3d2c3e0',
        'timeline_uuid': '8bed768f-0550-40c1-9a4b-afa5ec4eacab',
    },
    # de869b93-4a43-1813-b166-b1c0aa52cd6e
    'ShadowHeart_InPartyEND': {},
    # 03bb2e38-1479-c894-127a-4ec6227ab443
    'ShadowHeart_InParty2_Nested_BackgroundChapter': {
        'dialog_uuid': 'e839a622-b2ed-4a07-8a05-2c5547fbe693',
        'timeline_uuid': '2b6325ff-59e5-4692-957c-c377b24fa9c7',
    },
    # 92a816b0-5eff-3751-d75e-3dc3deaebe40
    'ShadowHeart_InParty2_Nested_CityChapter': {
        'dialog_uuid': '64138e2e-39fb-4fc2-b450-c8498d70ce19',
        'timeline_uuid': 'fda24c48-e633-49e4-9f1c-9b63b99c8ce1',
    },
    # 8bd1efb6-27fb-a511-e459-dbad23302a3e
    'ShadowHeart_InParty2_Nested_DefaultChapter': {
        'dialog_uuid': '6f54cfda-98a8-4130-80ce-c9920d7f9487',
        'timeline_uuid': '9dfb9bb3-cbcd-444a-a570-f39fb81cc8d1',
    },
    # af5ad52d-8a38-7140-dfe2-f3c0e544741c
    'ShadowHeart_InParty2_Nested_OriginChapter': {
        'dialog_uuid': '8ca980b0-8ec5-4a77-a190-08d79a4cf290',
        'timeline_uuid': 'e4c83973-347a-46ea-ae81-21cfd4477137',
    },
    # 550b5241-3cc5-cc02-7fae-ff78f2990dfc
    'ShadowHeart_InParty2_Nested_Romance': {
        'dialog_uuid': '5d8383b9-c799-4bf6-a476-13c222711b23',
        'timeline_uuid': '80b1fb5c-80a5-449b-832e-7479749e0c8d',
    },
    # 058b61ef-8af6-3f48-08c3-46cbd4374446
    'ShadowHeart_InParty2_Nested_ShadowCurseChapter': {
        'dialog_uuid': 'f636b706-aa7b-43f6-9dee-09c5d236f8ba',
        'timeline_uuid': 'fab2e128-54ca-461d-b805-22781cf6d29c',
    },
    # 38e65f7e-1d89-9171-4e0a-743fb89dc55c
    'ShadowHeart_InParty2_Nested_ShadowheartHug': {
        'dialog_uuid': '3a871915-dabf-4524-a382-1359cdade422',
        'timeline_uuid': '7dc1e10e-c188-47b7-8235-f46ac81a0b12',
    },
    # 7d565080-9370-fe5b-9437-89d169096a04
    'ShadowHeart_InParty2_Nested_ShadowheartKiss': {
        'dialog_uuid': '405f359f-3f3d-4221-8c01-e4abd6f58a6f',
        'timeline_uuid': 'd697bf8f-5b1e-466b-af27-64d6865243db',
    },
    # d71b23ba-6d5a-b71b-a1f9-bca2944c6a62
    'ShadowHeart_InParty2_Nested_SharranChapter': {
        'dialog_uuid': '659bbed6-6e24-4046-9a58-fdbbdb5bddcd',
        'timeline_uuid': '1c965e59-b794-433d-b5d9-c4d563aece4d',
    },
    # d99444c9-199d-a423-bd39-3de47cbd843e
    'Shadowheart_InParty_Nested_TopicalGreetings': {
        'dialog_uuid': 'f510af74-63c9-4bee-ae3b-6ad424e9819f',
        'timeline_uuid': 'a3a91f40-95fd-48c6-9c25-ec64597b5602',
    },

    # Shadowheart romance cutscenes
    'CAMP_Shadowheart_Nightfall_SD_ROM': {
        'dialog_uuid': '6088ea97-8096-491c-99a4-a6655bc55f39',
        'timeline_uuid': '7c916b11-d211-4e61-a3ca-32006fbe67fc',
    },
    'CAMP_GoblinHuntCelebration_SD_ROM_NightWithShadowheart': {
        'dialog_uuid': 'befc9016-bce6-44d2-8d98-7fcd574d8052',
        'timeline_uuid': '99070203-9bf8-45e4-aebb-97371c8fb02e',
    },
    'CAMP_Shadowheart_SkinnyDipping_SD_ROM': {
        'dialog_uuid': '282d4a7a-344b-458e-81a2-4caa1261795b',
        'timeline_uuid': '97a06c9f-d915-4e8b-b185-1a35df708073',
    },
    'END_GameFinale_RomanceFates_Shadowheart': {
        'dialog_uuid': 'cc9cf429-3540-4d54-ad96-44b5ff1981b8',
        'timeline_uuid': 'd01ac781-8124-406f-b94a-c32607c5f3de',
    },

    # Shadowheart's CRDs, CFMs, and SDs
    'CAMP_Shadowheart_CRD_SkinnyDippingRomance': {
        'dialog_uuid': 'd52f1b7e-9f35-4a5e-8a4f-4663c79e52ff',
        'timeline_uuid': 'edbd47cd-8908-45be-89cc-1a12f41ad026',
    },
    'CAMP_Shadowheart_DaughterTears_SD': {
        'dialog_uuid': 'dcef3803-c878-4a88-a9fd-60136235c4d0',
        'timeline_uuid': '10b9f68b-1f53-4d72-afdc-68ebeef0385e',
    },
    'CAMP_Shadowheart_IVB_CFM_WildMagic': {},
    'CAMP_NightsongShadowheartVisit_CFM': {},
    'CAMP_MizoraMorningAfter_CFM_ROM': {},

    # Shadowheart's parents
    'CAMP_ShadowheartFather': {
        'dialog_uuid': '937b5cf1-fb1c-4095-98a3-0a8afc6f2481',
        'timeline_uuid': '4e24b77e-db78-48ee-8af1-458d5c2e1090',
    },
    'CAMP_ShadowheartMother': {
        'dialog_uuid': '323e51fb-a0b7-4841-973c-cfbb9d88cdda',
        'timeline_uuid': '29fbb296-62d9-4fe8-b924-9ae1ff3b5b83',
    },

    # Shadowheart's origin moments (AOMs, OOMs, COMs)
    'SHA_NightsongsFate_OM_Shadowheart_AOM_OOM_COM': {},
    'GOB_SeluneTemple_OM_ShadowHeart_COM': {},
    'FOR_Owlbear_OM_Shadowheart_COM': {},

    # Shadowheart recruitment
    'ShadowHeart_Recruitment_Beach': {
        'dialog_uuid': '81660980-17e0-4794-a427-5cbdae19ebd3',
        'timeline_uuid': '5cd8c213-ed9e-4f72-b9ba-6489ad411810',
    },
    'ShadowHeart_Recruitment_Den': {
        'dialog_uuid': '73d42ef7-783b-4935-b4ca-4aa6a7afb2a9',
        'timeline_uuid': '295da2c3-d174-46e6-902a-85a6556f56fe',
    },

    # Epilogue
    'EPI_Epilogue_Shadowheart': {
        'dialog_uuid': '965d20ef-aa30-48e2-9b01-c74a18fb93f2',
        'timeline_uuid': '5aa08127-fafe-4622-ba10-31fb125d878f',
    },

    # Cloister
    'LOW_HouseOfGrief_OM_Shadowheart_COM': {},
    'LOW_SharGrotto_ConfrontViconia_OM_Shadowheart_COM': {
        'dialog_uuid': '356a5943-0a7c-4204-8175-6f68e82bb964',
        'timeline_uuid': '65945121-3d46-4536-8ecd-ca4a00f2aa9d',
    },
    'LOW_SharGrotto_ViconiaDefeated_OM_Shadowheart_COM': {},
    'LOW_SharGrotto_ParentsFate_OM_Shadowheart_COM': {},

    # Tutorial
    'TUT_TransformChamber_PodLock': {
        'dialog_uuid': 'b3d6ff43-be8f-4bef-b8ca-638d9892863c',
        'timeline_uuid': '4a16b0f2-7b51-4485-b4db-b6f16b4d1409',
    },

    # Dark Urge
    'LOW_BhaalTemple_PostBattleDarkUrge_Resistance': {},

    # Night sleep cutscenes
    'CAMP_FARM_SleepCutscene': {
        'dialog_uuid': 'e7f82207-7a62-47e0-8785-3d1f5117ab20',
        'timeline_uuid': 'f898108f-7cf7-48da-be5d-5590a7ee32c3',
    },
    'CAMP_SLUMS_SleepCutscene': {
        'dialog_uuid': 'd8ec9ac9-2387-428b-a53b-6915eec8a64a',
        'timeline_uuid': '28b656e1-efbf-4982-b0d1-8e5a715a0e6c',
    },
    'CAMP_ELFSONG_SleepCutscene': {
        'dialog_uuid': 'c7dbf47b-c448-4d06-8118-ef9d3c8fc106',
        'timeline_uuid': 'acb110de-545d-4689-9b7e-feb1ac092719',
    },

    # Camp
    'CAMP_Night1_CRD_Shadowheart': {},
    'CAMP_Night2_CRD_Shadowheart': {},
    'CAMP_Night3_CRD_Shadowheart': {},
    'CAMP_Shadowheart_IVB_CFM_LaezelFight': {},

    # Grove
    'DEN_Apprentice_Cyanide': {},
    'DEN_CapturedGoblin': {},
    'DEN_CapturedGoblin_GuardsAvenge': {},
    'DEN_General_Squirrel': {},
    'DEN_ShadowDruid_SnakesCourt': {},

    # World
    'LOW_HouseOfHope_ROM_Incubus': {},
    'WYR_DapperDrow_Intimacy': {},
    'WYR_DapperDrow_SiblingsThreeWay': {},
    'GOB_DrunkGoblin': {},

    # EA related stuff
    'HAG_GurHunter': {},
    'HAG_GurHunter_OM_Astarion_COM': {},

    # Astarion
    'Astarion_InParty2_Nested_TopicalGreetings': {},

    # Gale
    'Gale_InParty2_Nested_TopicalGreetings': {},
    'Gale_Recruitment2': {},

    # Karlach
    'Karlach_InParty_Nested_TopicalGreetings': {},

    # Lae'zel
    'Laezel_InParty2': {},
    'Laezel_InParty2_Nested_TopicalGreetings': {},

    # Wyll
    'Wyll_InParty': {},
    'Wyll_InParty2_Nested_TopicalGreetings': {},

    # Minsc
    'Minsc_InParty': {},
    'Minsc_InParty_Nested_PersonalQuestions': {},

    # Jaheira
    'Jaheira_InParty': {},
    'Jaheira_InParty_Nested_TopicalGreetings': {},

    # Minthara
    'Minthara_InParty': {},
    'Minthara_InParty_Nested_TopicalGreetings': {},
    'Minthara_InParty_Nested_PartyMemberThoughts': {},
    'CAMP_Halsin_Minthara_CFM_Confrontation': {},
 
    # End game
    'END_BrainBattle_CombatOver_Nested_StandardIntro': {},

    # Creepy stuff
    'CAMP_HalsinsRevenge_CFM': {},
    'Halsin_InParty': {},
    'Halsin_InParty_Nested_Polyamory': {},
    'Camp_Act3_CRD_HalsinRomance': {},
    'Halsin_Warning1': {},
    'Halsin_Warning2': {},
    'Halsin_Leaving': {},
    'PB_Halsin_Shadowheart_ROM_Act3_Selune': {},
}

def prepare_assets() -> None:
    game_assets.prepare_assets(ASSETS, verbose = True)

def prepare_override_assets() -> None:
    game_assets.prepare_assets(ASSETS_OVERRIDES, verbose = True)

bg3.add_pre_build_procedure(0, 'prepare_assets', prepare_assets, 'override', False)
bg3.add_pre_build_procedure(0, 'prepare_override_assets', prepare_override_assets, 'override', True)

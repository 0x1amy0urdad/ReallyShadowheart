from __future__ import annotations

from ._speakers import *

# Use this actor to create fade to black transitions
FADE_TO_BLACK_SCENERY_ACTOR_UUID = '198c1799-42f2-4266-b09b-0323402abdd0'


# Dialog nodes

# "Something the matter?" in ShadowHeart_InParty2
SHADOWHEART_QUESTION_BANK_ROOT_NODE_UUID = '5f864b1a-65af-45de-ac29-d27242ab07b7'

# "We've been through quite a lot, with likely more to come. Care to narrow it down a little?" in ShadowHeart_InParty2_Nested_DefaultChapter
SHADOWHEART_THOUGHTS_QUESTION_BANK_NODE_UUID = '9f7d4510-e658-4b23-b066-4fe117fbba7b'

# Nested dialogs
SHADOWHEART_INPARTY2_NESTED_DEFAULTCHAPTER = '8bd1efb6-27fb-a511-e459-dbad23302a3e'

# Origins and Companions: UUIDs, these are used in reactions
ORIGIN_SHADOWHEART = '2bb39cf2-4649-4238-8d0c-44f62b5a3dfd'
ORIGIN_ASTARION    = '3780c689-d903-41c2-bf64-1e6ec6a8e1e5'
ORIGIN_LAEZEL      = 'fb3bc4c3-49eb-4944-b714-d0cb357bb635'
ORIGIN_GALE        = '35c3caad-5543-4593-be75-e7deba30f062'
ORIGIN_WYLL        = 'efc9d114-0296-4a30-b701-365fc07d44fb'
ORIGIN_DARK_URGE   = '5af0f42c-9b32-4c3c-b108-46c44196081b'
ORIGIN_JAHEIRA     = 'c1f137c7-a17c-47b0-826a-12e44a8ec45c'
ORIGIN_MINTHARA    = 'eae09670-869d-4b70-b605-33af4ee80b34'
ORIGIN_MINSC       = 'e1b629bc-7340-4fe6-81a4-834a838ff5c5'
ORIGIN_HALSIN      = 'a36281c5-adcd-4d6e-8e5a-b5650b8f17eb'
ORIGIN_ALFIRA      = '38357c93-b437-4f03-88d0-a67bd4c0e3e9'
ORIGIN_KARLACH     = 'b8b4a974-b045-45f6-9516-b457b8773abd'

SPEAKER_TO_ORIGIN_MAP = {
    SPEAKER_SHADOWHEART : ORIGIN_SHADOWHEART,
    SPEAKER_ASTARION    : ORIGIN_ASTARION,
    SPEAKER_LAEZEL      : ORIGIN_LAEZEL,
    SPEAKER_GALE        : ORIGIN_GALE,
    SPEAKER_WYLL        : ORIGIN_WYLL,
    SPEAKER_DURGE       : ORIGIN_DARK_URGE,
    SPEAKER_JAHEIRA     : ORIGIN_JAHEIRA,
    SPEAKER_MINTHARA    : ORIGIN_MINTHARA,
    SPEAKER_MINSC       : ORIGIN_MINSC,
    SPEAKER_MINSC       : ORIGIN_HALSIN,
    SPEAKER_KARLACH     : ORIGIN_KARLACH
}

# Peanuts
PEANUT_SLOT_0 = 'PEANUT_SLOT_0'
PEANUT_SLOT_1 = 'PEANUT_SLOT_1'
PEANUT_SLOT_2 = 'PEANUT_SLOT_2'
PEANUTS = frozenset((PEANUT_SLOT_0, PEANUT_SLOT_1, PEANUT_SLOT_2))


# Difficulty classes
Act1_Zero = '4dfcb0ff-e02a-4efd-b132-77dfd956055e'
Act1_Negligible = '2728289e-841d-4273-a29a-f24ae9f8c4fb'
Act1_VeryEasy = '8d398021-34e0-40b9-b7b2-0445f38a4c0b'
Act1_Easy = '31e92da6-bac9-46f7-af99-5f33d98fd4f0'
Act1_Medium = 'fa621d38-6f83-4e42-a55c-6aa651a75d46'
Act1_Challenging = '5e7ff0e9-6c80-459c-a636-3a3e8417a61a'
Act1_Hard = '831e1fbe-428d-4f4d-bd17-4206d6efea35'
Act1_VeryHard = '8986db4d-09af-46ee-9781-ac88ec10fa0e'
Act1_NearlyImpossible = 'ea049218-36a8-4440-a3fc-f3019a57c86b'
Act2_VeryEasy = '9d1f2171-fef1-4c03-9e83-523485174c46'
Act2_Easy = '0d9484eb-f680-4a33-853d-46fda64883f2'
Act2_Medium = '89f0acd4-346f-479d-8b7a-1a3eb5382f6d'
Act2_Challenging = 'c44bfd7d-84de-4568-9c57-a059b8df5435'
Act2_Hard = '91fb3598-dd68-4fa8-a306-2c7284709b08'
Act2_VeryHard = 'f3aa825b-785e-4f4a-90af-565c7e943609'
Act2_ExtraHard = '753ed8df-b5dc-4584-b9fa-de18c4c956b2'
Act2_NearlyImpossible = '52918812-bc1c-43b5-881a-58443902f5fa'
DC_Act3_VeryEasy = 'b9cea18d-f40a-444d-a692-76582a69130c'
DC_Act3_Easy = '5028066b-6ea0-4a6a-9e3e-53bee62559a7'
DC_Act3_Medium = '77cee1c4-384a-4217-b670-67db3c7add57'
DC_Act3_Challenging = '96bc76f2-0b2e-4a79-854f-e4971a772c36'
DC_Act3_Hard = '6298329e-255c-4826-9209-e911873b64e7'
DC_Act3_VeryHard = '60916b01-ba4c-418e-9f30-19a669704b4d'
DC_Act3_NearlyImpossible = '7bf230a0-b68a-4c79-a785-79b498d6c36b'
DC_Act3_Impossible = 'ef0d0c54-3500-466f-98db-5c0600158cb7'



FLAG_CURRENTREGION_SCL_Main_A = 'f76b85b5-b557-4409-98fd-cc7b22f8292b' # Global flag. Party is in SCL_Main_A
FLAG_CURRENTREGION_CTY_Main_A = 'd523976f-a39b-4d33-b6cb-f58b705a0396' # Global flag. Party is in CTY_Main_A
FLAG_CURRENTREGION_CRE_Main_A = 'bbc31a08-cfb0-4501-9401-4b12a78efa35' # Global flag. Party is in CRE Main
FLAG_CURRENTREGION_INT_Main_A = '7f78a1d7-3e5e-4cd2-8fcd-f751b01c0ee0' # Global flag. Party is in INT_Main_A
FLAG_CURRENTREGION_EPI_Main_A = '49a342c4-59f2-4861-9048-8fe63a7b7cde' # Global flag. Party is in EPI_Main_A
FLAG_CURRENTREGION_IRN_Main_A = '3b31600d-6416-4a37-962c-4c36c06fb41f' # Global flag. Party is in IRN_Main_A
FLAG_CURRENTREGION_BGO_Main_A = '11239767-48ad-4879-8312-b9164b6e4978' # Global flag. Party is in BGO Main
FLAG_CURRENTREGION_WLD_Main_A = '797d21c8-b2a9-4c86-a1e4-8ca3833a32ef' # Global flag. Party is in WLD_Main_A
FLAG_CURRENTREGION_END_Main = '140b4d3e-6cc7-48cb-b66f-dbc4eba710e1' # Global flag. Party is in END_Main

FLAG_VISITEDREGION_CRE_Main_A = 'c22062f9-2a42-4e19-8c72-34a2d9ff9c0a' # Global flag. Party visited CRE_Main_A

# Flags
FLAG_IMPOSSIBLE = '6e4b66e9-0f72-5171-04ba-441108b45b0e' # cut content
FLAG_ORI_Inclusion_Random = '5c169560-2732-c515-9e73-06ba1fd768f0' # Object flag. Set to true on Tav to pick a companion at random.
FLAG_ORI_Inclusion_PickedAtRandom = '46a601fb-8cb7-46ed-9856-3d4e38c53a02' # Object flag. Companion was picked at random after setting FLAG_ORI_Inclusion_Random.
FLAG_ORI_Inclusion_2Random = 'c30251ab-eab9-4ed8-bdf9-e1e816b7f12c' # Object flag. Set to true on Tav to pick 2 companions at random.
FLAG_ORI_Inclusion_PickedAtRandom2 = '32f45064-c5f2-465f-ac2d-5ad0c1ce9f59' # Object flag. 2 companions were picked at random after setting FLAG_ORI_Inclusion_2Random.
FLAG_ORI_Inclusion_End_Random = 'b5261e06-a89e-0ec8-bab9-2329ff72b6d1' # Object flag. Set to true on Tav to end random inclusion.

FLAG_AOM = '794d7d9a-4e15-849c-7c0d-6e6cdb67cdcb' # Avatar Origin Moment
FLAG_OOM = '018ab052-38df-6d2c-117f-8d7c1e56b061' # Non-Avatar (Origin) Origin Moment
FLAG_COM = '7075ec1a-70ad-bd25-3111-0a955cf07585' # Companion Origin Moment

FLAG_GEN_MaxPlayerCountReached = '823b5064-8aa4-c0b7-1b8c-657b46987ccd' # Global flag. Set if the party is already at the maximum size.
FLAG_GLO_ORI_Event_InvitedToCamp_Run = '07c4d37e-fc82-4055-b768-167650be9956' # Object flag. Set on a companion to make them join and go to camp.
FLAG_OriginAddToParty = '4870b2cd-210c-0fdc-9c58-4d0142bdae29' # Object flag. Add this origin to the party.

FLAG_SetOriginHostileAfterDialog = '91659c6d-ed58-4b95-894b-763b69df824d' # Object flag. Set on an origin to make them hostile.

TUT_TransformChamber_State_DisableWard = '5276092d-7b2b-49c8-b3fa-7220c801c1ce'
TUT_TransformChamber_State_EndPodDialogue = '46cfbaa6-ffae-4aec-afeb-78843d3f2d5d'

FLAG_GLO_InfernalBox_State_BoxBoundedTo = 'f4d2be66-0443-4069-8ca2-570143f17e27' # Object flag. Set on a character that has the artefact

FLAG_GLO_Camp_Event_SkipSleepCutscene = '1ee0a25e-4115-44ef-b87d-c2a5eee494b6' # Set this during a night dialogue to skip the succeeding sleepcutscene


FLAG_GLO_Pixie_State_ShieldActive = '1225b030-2183-4033-8bcd-819be1bb9e61' # The party is shielded from the shadow curse
FLAG_GLO_Pixie_Event_GivesImmunity = '4c29ab8b-9b56-49a8-838c-c83a257976e5' # Triggers the pixie blessing status

FLAG_Shadowheart_InParty_Event_UrgeHaven = '627d1ddc-cf6c-4f32-bb4a-e67475f1451d' # Durge brags about destruction of the Last Light Inn

FLAG_NIGHT_GoblinHunt_TieflingCelebration = '1ad8c357-2695-4d5c-b5f9-8b8c07803121' # Global flag. Goblin Hunt Celebration - Tieflings.
FLAG_NIGHT_GoblinHunt_RaiderCelebration = '86fee25f-1069-4f17-89fa-4c5b69f82e0b' # Global flag. Goblin Hunt Celebration - Raiders.

FLAG_ORI_State_Partnered = '6c1a31e8-1d3d-42a5-af4f-72ef7a798f74' # Avatar or Companion is in an exclusive relationship
FLAG_ORI_State_DoubleDating = '41320aeb-8e1a-433d-a82e-3d78aff578da' # Character is dating two Origins, blocking any additional dating
FLAG_ORI_State_Dating = 'a3346d5b-c54b-4c73-bf18-0a2bf90c35da' # Character is dating someone.

FLAG_ORI_InfernalBox_State_BoxBoundedTo = 'f4d2be66-0443-4069-8ca2-570143f17e27' # Character bounded to theinfernal box.
FLAG_ORI_Shadowheart_Event_LaezelFirst = 'd68af374-5808-5b37-210c-21f9e1c8c201' # Global flag. Laezel sneaks on Shadowheart and tries to kill her.

FLAG_OriginAddToParty = '4870b2cd-210c-0fdc-9c58-4d0142bdae29' # Set on origin to add them to party.

FLAG_Shadowheart_InParty2_Event_WYR_PartnerFlirtOpportunity = '7dc198dc-e80b-c699-2b73-28e419a157f3' # Set on Tav when they have an opportunity to flirt (I think I'd quite like to get lost with you, exploring the city)

# Shadowheart states
FLAG_ORI_State_DatingShadowheart = 'e87f1e21-a758-47ae-8c0e-9e715eb289b5' # This character has started on the path to a relationship with Shadowheart.
FLAG_ORI_State_PartneredWithShadowheart = '3808ae35-ad4e-465b-800b-63d32b77211e' # This character is in an exclusive relationship with Shadowheart
FLAG_ORI_State_WasPartneredWithShadowheart = '542e6cf4-bfd1-471d-b4b5-693d630376cb' # Player was in a relationship with Shadowheart.
FLAG_ORI_State_HandledBreakupWithShadowheart = 'd400a4f6-4a10-48a4-a425-73786e473815' # Shadowheart reacted to the player breaking up with her.
FLAG_ORI_State_ChosePartnerOverShadowheart = '3928d3fc-b2c8-44ac-850d-e269177f8c0a'

FLAG_TUT_TransformChamber_State_FreedShadowheart = 'c3980ab3-9370-4c2d-9c76-38aff5fe575a' # Set on player who frees Shadowheart
FLAG_ORI_ShadowheartRecruitment_State_ShadowheartKnockedOut = 'b526a042-1474-4570-9fba-b2d59776e53e'
FLAG_ORI_ShadowHeart_State_IsInParty = '9a029c5a-e3c3-45ef-9cd4-1cb45718deb1' # Global flag. Shadowheart joined the party
FLAG_ORI_Shadowheart_State_WolfDreamPoint_NautiloidSaved = '71127b5b-ad4c-46ff-b870-82e91fb3d067' # Global flag. Saved Shadowheart on the Nautiloid" />
FLAG_GLO_Shadowheart_State_RecruitedInTutorial = 'c7f8437b-6064-4a1d-9774-71da051887e5' # Global flag. Saved Shadowheart aboard the nautiloid.
FLAG_ORI_Shadowheart_State_IncurableWound_Unavailable ='cc2ed160-cc5e-4898-8cbc-06a410fbd632' # Global flag. Incurable wound should not appear.
FLAG_ORI_Shadowheart_State_SavedAnimal = '0fc7b106-64aa-4a75-9861-0cf132ed804a' # Shadowheart saved an animal.
FLAG_ORI_Shadowheart_State_BlockBackground = 'f3323dfc-c725-4627-a64f-fb8c6e8e4a74' # Global flag. Set when Shadowheart hit a particular milestone on revealing her background.
FLAG_ORI_Shadowheart_Knows_WolfFear = 'f5f935c3-7f73-4de4-9aee-553cb96fb6d1' # Global flag. Knows about Shadowheart's wolf fear
FLAG_ShadowHeart_InParty_Knows_SharWorshipper = '634f858d-9b54-0711-e31f-075d304422ab' # Global flag. Tav knows about Shar worship
FLAG_ORI_Shadowheart_Knows_JusticiarDream = 'f37f2c1d-89c9-4d09-baff-81046a625267' # Global flag.
FLAG_ORI_Shadowheart_Knows_JusticiarMurals = '87dea9e2-c18c-40a0-98cf-96cf2804cf4e' # Global flag.
FLAG_ORI_Shadowheart_Knows_IncurableWound = 'bf04e5f1-0add-4b21-a3ec-be25a73bfe92' # Global flag. Tav has seen Shadowheart's incurable wound
FLAG_ORI_Shadowheart_Knows_MotherSuperior = '2ccd399f-e743-45f6-9fea-12afaa4647f7' # Global flag
FLAG_ORI_Shadowheart_Knows_BecomeJusticiar = 'c29b8679-3e0b-43f9-8578-2a5d7659180e' # Global flag
FLAG_ORI_Shadowheart_Knows_HasSeenWolfDream = 'f7e48f6a-bc8b-4941-8016-6622956c84f9' # Global flag

FLAG_ORI_Shadowheart_State_NobleStalkMemory = 'd0d87954-6563-4e26-9f2c-4616e3cfeb0e' # Global flag
FLAG_UND_MushroomHunter_State_HasMushroom = '7b86b816-a97c-4500-9398-ef4c7f344e0b' # Object flag. Set on Tav when Tav has the shroom.
FLAG_LOW_SharGrotto_State_UnlockedFriendDialog = 'dd67ca1e-b36d-49d1-8822-6bb47ebfe2fe' # Global flag


FLAG_CAMP_Shadowheart_State_HadNightsongMeeting = '10b74e80-a963-420f-8c2a-d518b6aae143' # Global flag
FLAG_ORI_Shadowheart_Romance1_AfterCelebration_State_QueueInvitation = '2d7e1f5e-fee1-4732-a0a2-f1337cc5466c' # Global flag. Invitation to the waterfall romance cutscene
FLAG_CAMP_GoblinHuntCelebration_SD_ROM_NightWithShadowheart_State_Happened = '96508d74-26f3-c8a1-da78-b17c10a5ef11' # Global flag. Waterfall date has happened
FLAG_ORI_Shadowheart_State_NightsongPoint_GaveNightOrchid = 'cd01256d-93df-4d80-8d94-1233fe16ddf6' # Global flag
FLAG_ORI_Shadowheart_State_NightsongPoint_HasEnoughPoints = '82893505-534a-461a-8dd5-0f4677dad6ce' # Global flag
FLAG_ORI_Shadowheart_State_IrregularBehaviour = 'a1e4a324-4c58-48fb-b08e-d538fec45af8' # Global flag. Shadowheart is behaving oddly in camp.
FLAG_ORI_Shadowheart_State_EnemyOfSharPath = '055bbe0f-05f5-444b-a7e2-0f66edd2178c' # Global flag. Shadowheart rejected Shar
FLAG_ORI_Shadowheart_State_SharPath = 'bf9ae334-ff6a-458d-b898-3074bca0bdfb' # Global flag. Shadowheart remained loyal to Shar
FLAG_ORI_Shadowheart_State_StartedRomance = 'f725b333-9846-4e6c-8123-35330f3e7aa5' # Global flag. Tav started Shadowheart romance
FLAG_ORI_Shadowheart_State_HairChange = '2abcff91-1f1e-4853-98e2-ad7d2020158c' # Global flag. Change Shadowheart's hair to her new hairstyle.
FLAG_LOW_HouseOfGrief_Knows_IsSharCult = '6aa0816f-5827-4669-b3d3-b6dd71a6b95e' # Global flag. Knows House of Grief is a Shar Cult front
FLAG_ORI_Shadowheart_State_SparedViconia = 'cd5421b3-6051-4641-a56f-69588173c13c' # Global flag. Shadowheart let Vicona live.
FLAG_ORI_Shadowheart_State_KilledViconia = '472e18f2-15f9-4004-bdae-a9340fff7b15' # Global flag. Shadowheart killed Viconia.
FLAG_LOW_Grotto_State_ViconiaDefeated = '8e27eb4e-8d52-4966-8aa4-e658ff595097' # Global flag. Viconia was dealt with.
FLAG_ORI_Shadowheart_Knows_PersonalInfo = 'abbc836e-07f0-4951-bb7b-beac52d91b2a' # Global flag. Tav knows Shadowheart likes Night Orchids and cannot swim
FLAG_ORI_State_ShadowheartIsDating = '3b35c15c-465a-433b-876d-0717287629b3' # Global flag. Shadowheart is dating someone.
FLAG_ORI_Shadowheart_State_WasHugged = 'a9e3314f-8255-48dc-a764-37ea96d86924' # Global flag. Shadowheart was hugged by someone
FLAG_ORI_Shadowheart_State_IncurableWound_AskedHelp = '9ae22761-cb46-4d4d-9738-c134c39d150f' # Global flag. Players asked Shadowheart if they could help with her incurable wound
FLAG_ORI_Shadowheart_State_AbortedSkinnydipping = '26e83a93-8999-4488-83ee-a93d1ccd5cac' # Global flag. Aborted skinny dipping
FLAG_ORI_Shadowheart_State_ParentPoints_TeacherGrave = '600ca39c-5887-4657-bf4c-d417cc3d146b' # Global flag.
FLAG_ORI_Shadowheart_State_ParentPoints_Hideout = 'a1cf2f2f-8f3f-4ac7-a1f7-32e3bdb1bda4' # Global flag.
FLAG_ORI_Shadowheart_State_ParentPoints_Graffiti = '56084254-ec74-4c13-8eb2-6e8163f16b8f' # Global flag.
FLAG_ORI_Shadowheart_State_HadParentsPoints = 'c5c03e5f-44af-4347-a081-bbbd9d5fc632' # Object flag.
FLAG_ORI_Shadowheart_State_ParentPoints_HasEnoughPoints = '1bbdd0b8-c2de-4b2f-8ce8-6740812deb59' # Global flag.
FLAG_ORI_Shadowheart_State_Act3RomanceEnded = '4f67ad76-c654-490e-ab62-263ae8fa8d14' # Global flag.
FLAG_ORI_Shadowheart_State_RejectShar_KilledParents = 'e9060caf-66b0-4701-8dfd-5ae1125f5afd' # Global flag. Killed parents while on the reject shar path
FLAG_ORI_Shadowheart_State_RejectShar_SavedParents = '486d69d4-a7c2-4cb5-8fcb-8f2cb738ada9' # Global flag. Saved parents while on the reject shar path
FLAG_ORI_Shadowheart_State_Shar_SavedParents = '8a0fad17-1615-4a0d-a045-21661d9a2aa0' # Global flag. Saved parents while on shar path
FLAG_ORI_Shadowheart_State_Shar_KilledParents = '3a3b0ecf-a1ed-4733-8548-0348befc6bac' # Global flag. Killed parents while on Shar Path
FLAG_ORI_Shadowheart_State_RetiredToFarmWithAvatar = '25930d25-598a-8692-5a96-039c9b2c0512' # Tav and Shadowheart retired to live in a farmhouse

FLAG_Shadowheart_InParty_InterestInDarkJusticiars = '4d45b833-582d-c7a6-9936-0922e78e36d9' # Global flag. Shadowheart is interested in DJs mentioned by the creep.
FLAG_Shadowheart_InParty_FindDarkJusticiars = 'b8086f64-117b-3e7d-3277-ccb0f835ee90' # Global flag. Shadowheart discovered bodies of DJs.

FLAG_ORI_Shadowheart_State_WolfDreamPoint_WorshipGood = 'cd1832ce-2e41-4a82-a7bd-d9260f603757' # Offered a good reaction to her worship of Shar.

FLAG_Shadowheart_Inparty_State_DiscussedMurals = '77e50a1f-e5ca-483b-9132-81a3d9e29796' # Dialog flag. Discussed murals with Shadowheart

FLAG_LOW_SharGrotto_State_PromisedBringShadowheart = 'ba85fccc-c09b-41c3-82ec-69693db59204' # Global flag. Player promised to bring Shadowheart to Viconia.

# Shadowheart events
FLAG_ORI_Shadowheart_Event_IncurableWoundFlared = '9a1f4cad-75ec-48dd-a408-929af01136c9' # Shadowheart's incurable wound flares.
FLAG_Shadowheart_InParty_Event_WolfFearQuestionStart = '2a7514a0-e41e-49f6-a5c9-18cd3b4187b2' # Object flag. Set it on Tav to start wolf fear follow-up conversation.
FLAG_Shadowheart_InParty_Event_SeenMuralsStart = 'b868197d-c59e-41c1-b828-652f20dbd797' # Object flag. Shadowheart has seen murals in the grove.
FLAG_Shadowheart_InParty_Event_JusticiarInclusionStart = '01fbe8bc-74fc-4c92-8560-3382f3dfb14a' # Object flag. Shadowheart overheard about DJs.
FLAG_Shadowheart_InParty_Event_PartneredStart = '22c04792-d5fc-4285-b45d-95c7df986e47' # Object flag that triggers nested romantic conversation between partnered Tav and Shadowheart.
FLAG_Shadowheart_InParty_Event_MissedRomanceStart = '138c5749-0de1-44f6-b2bd-ae6588b1a1f5' # Object flag that triggers nested romantic conversation to start Shadowheart's romance path
FLAG_Shadowheart_InParty_Event_KissHappened = '0434578b-646b-e0a7-3124-bc3338144658' # Dialog flag. Tav kissed Shadowheart.
FLAG_Shadowheart_InParty_Event_NobleStalkStart = '2c8d80f8-c3c9-477c-9565-a012d08572cd' # Object flag. Set on Tav to start the noblestalk conversation.
FLAG_ORI_Shadowheart_Event_FailedNoblestalkEating = '11e69472-c6a1-7985-d106-f1b40334aa9f' # Object flag. Set on Tav when Shadowheart refused to eat the shroom

FLAG_GEN_SoloPlayer = '29e32f83-2001-0dbc-7df9-3ca2b3bc4349'

FLAG_HAV_TakingIsobel_Event_GiveOintment = 'efb6aed5-fd07-433b-b0c5-b980bf77bb2c' # Global flag. Isobel gives the Selune ointment to one of the players (the one currently talking to her in the dialog where this is set)

# Quest flags
FLAG_ORI_COM_Shadowheart_Travel_Memory_Suppressed = '0be0c177-16f7-4fe3-b878-ca87ca362657' # Quest flag: "Shadowheart told us that she had allowed her memory to be suppressed so she can serve Shar without compromising her."

# Laezel
FLAG_ORI_HadSexWithLaezel = '150c8ec7-fbd2-d040-9951-0c41c911c371' # Object flag. Slept with Laezel after the GoblinHunt celebrations in Act1
FLAG_ORI_Laezel_State_Romance1HadSex = 'ee418d4a-0bc3-4626-bfd0-eb14d6e537bc' # Global flag. Set when an avatar has sex with laezel in Act 1 Romance
FLAG_ORI_State_DatingLaezel = '86eaa84a-350b-401b-8b43-b53eeb534579'
FLAG_ORI_State_PartneredWithLaezel = 'd169a786-6e56-4f0d-a2eb-33c48d8d1160'
FLAG_ORI_State_WasPartneredWithLaezel = '6d402d9b-7af9-43ea-b0eb-98e9612dde27'
FLAG_ORI_State_HandledBreakupWithLaezel = '76f44c15-bcc3-4232-9dde-ae522a3db82d'
FLAG_ORI_State_ChosePartnerOverLaezel = '35c95a6d-4145-4903-ad73-a773df0e6892'

# Astarion states
FLAG_ORI_State_DatingAstarion = 'ba298c56-26b6-4918-9bd4-616668d369d8'
FLAG_ORI_State_PartneredWithAstarion = '30819c8d-b39d-42e7-acd1-2a8c2c309994'
FLAG_ORI_State_WasPartneredWithAstarion = '5a60943f-979b-4120-9b60-9e9b29529402'
FLAG_ORI_State_HandledBreakupWithAstarion = 'a8917c83-bcd4-4fb9-8459-649be92e2fbe'
FLAG_ORI_State_ChosePartnerOverAstarion = '529d4115-ef78-49aa-b1f2-24994e4e75e3'
FLAG_ORI_Astarion_State_StayedVampireSpawn = '2724b881-6be1-49a7-8375-a49e9acb4546' # Astarion chose to stay a Vampire Spawn
FLAG_ORI_Astarion_State_BecameVampireLord = 'c446ce94-efd8-45d5-b407-284177b6b57e' # Astarion became a Vampire Lord

# Gale states
FLAG_ORI_Gale_Event_BombDisarmed = '3d014e79-5595-9365-87bb-5cbb1f87fe5c' # Gale's bomb was disarmed.
FLAG_ORI_State_DatingGale = '75d0e041-c16c-d089-6d89-64354fa4c9d9'
FLAG_ORI_State_PartneredWithGale = 'e008e20d-d642-42ed-9008-297b6273aa21'
FLAG_ORI_State_WasPartneredWithGale = '60e14eb3-cce6-43c3-b893-b9b687e3d88f'
FLAG_ORI_State_HandledBreakupWithGale = 'dc42fe44-e320-4c96-85f0-66bb71403ee6'
FLAG_ORI_State_ChosePartnerOverGale = 'ff5cbe4e-d3a8-4cc6-86fa-f336f15e4304'

# Wyll states
FLAG_CAMP_MizorasPact_State_WyllReleasedFromPact = '79a90490-b009-507c-e0d3-f79b0bdd4cb6' # Wyll was released from his pact, Ravengard is doomed to the hells
FLAG_GLO_Wyll_State_GrandDuke = '0e223e4d-be63-89f4-380f-5cc755817abd' # Wyll chose to become Grand Duke before endgame
FLAG_CAMP_MizorasPact_State_WyllEternalPact = '8da8b1fb-5aa9-8cf5-8b45-6f8ca31a1227' # Wyll is eternally pacted to Mizora
FLAG_GLO_Wyll_State_BladeOfFrontiers = '8c46322f-7965-94c7-1318-62c391f1c8f1' # Wyll endgame state: he has chosen to remain the Blade of Frontiers
FLAG_GLO_Wyll_State_BladeOfAvernus = 'faeb73da-a609-dc56-7745-ac07f795c137' # Wyll's end game state: Blade of Avernus
FLAG_ORI_State_DatingWithWyll = 'f1520748-1d36-4500-9f8a-0da4207f8dd5'
FLAG_ORI_State_PartneredWithWyll = '5db4c1b6-3c42-43ae-aa85-1844acbf5a1d'
FLAG_ORI_State_WasPartneredWithWyll = '2652ff35-a62d-4947-b14b-11050ccfd329'
FLAG_ORI_State_HandledBreakupWithWyll = '3657b39e-6766-4395-bb97-d85aae0ca279'
FLAG_ORI_State_ChosePartnerOverWyll = 'f0b08362-76b7-4cf9-bd01-874fc1d8bf1c'

# Minthara states
FLAG_ORI_Minthara_State_AskedAboutAllCurrentTeamMembers = '6efc8f72-ace6-8414-bb77-862f9dd4d6a5' # Object flag. Asked Minthara about all current Team Members
FLAG_ORI_State_DatingMinthara = 'de1360cd-894b-40ea-95a7-1166d675d040'
FLAG_ORI_State_PartneredWithMinthara = '39ac48fa-b440-47e6-a436-6dc9b10058d8'
FLAG_ORI_State_WasPartneredWithMinthara = '8d0460d6-b00a-4947-bbd0-ad0c085a530f'
FLAG_ORI_State_HandledBreakupWithMinthara = '6a880802-bf76-4ece-816e-82cf90fa97be'
FLAG_ORI_State_ChosePartnerOverMinthara = '25202f13-55d3-4d13-b0c2-1245a90d99f2'

# Karlach states
FLAG_GLO_ForgingOfTheHeart_State_KarlachUpgraded = 'a818e2f5-9e0c-4ab3-8c1e-00765d3b892f'
FLAG_GLO_ForgingOfTheHeart_State_KarlachSecondUpgrade = 'f6dc0de4-1089-43c0-b392-306a9a44387c' # Dammon updates Karlach for the second time.
FLAG_ORI_State_DatingKarlach = 'f24c3f3e-7287-4908-84bf-ba314921f5ee'
FLAG_ORI_State_PartneredWithKarlach = 'd9ff60fa-0af9-45d7-99b4-bd7c3f80ed12'
FLAG_ORI_State_WasPartneredWithKarlach = '48f2a4d4-23f4-4514-b894-e225152d7a48'
FLAG_ORI_State_HandledBreakupWithKarlach = '005dbc62-472e-4268-b5e1-5d9c2c2c76a3'
FLAG_ORI_State_ChosePartnerOverKarlach = '8e5ba2d7-146c-4751-a62a-4bd98e8f279e'

# Durge states
FLAG_ORI_State_DarkUrge_KnowsBhaalspawn = 'd252e937-f659-7458-99d2-4aaf603185a7' # Global flag. The Dark Urge knows they are a Bhaalspawn
FLAG_ORI_DarkUrge_State_GivenSlayerForm = '14aec5bc-1013-4845-96ca-20722c5219e3' # Global flag. Flag used to identify that players have been given the slayer form, and therefore Orin does not have the form." />
FLAG_ORI_DarkUrge_State_BhaalResisted = '74944ac3-1ea0-4eae-9653-1f1319f8646b' # Global flag. Post-Orin fight, Dark Urge players rejected Bhaal's command to be his chosen.
FLAG_ORI_DarkUrge_State_BhaalAccepted = '904c45e0-bb06-40ed-b5d7-4f1c851b9d86' # Global flag. Post-Orin fight, Dark Urge players accepted Bhaal's command to be his chosen.
FLAG_ORI_DarkUrge_State_BhaalDisappointed = 'fb48dba0-24fd-e9ae-b6f9-4fadb9f8c4a0' # Global flag. DU failed through an edge case the Bhaal temple quest, without accepting or resisting Bhaal

# Scratch and Owlbear cub
FLAG_CAMP_OwlbearCubDog_State_NightActive = 'e092ebb1-f756-4644-b4dc-5bf0c0df3fd7' # Global flag. 
FLAG_CAMP_OwlbearCubDog_State_Friends = 'e1b55fd2-8172-4f1c-b5e6-12ba2646f355' # Global flag. Scratch and the cub are friends, this is used in dialogues.
FLAG_NIGHT_OwlbearCubDog = '902e10f8-e9d8-4eb6-ac0f-9ad8ba8787ed' # Global flag. The owlbear cub and the dog meet each other
FLAG_CAMP_Shadowheart_Event_PetArrived = '3fc1c969-f630-4d20-a61e-b1924873d8e2' # Global flag.
FLAG_CAMP_Shadowheart_Event_CallDog = 'a77ef785-def5-45cc-a5a1-e9e0cd08765b' # Global flag.
FLAG_CAMP_Shadowheart_Event_CallOwlbear = '6a1fe539-f2ea-47fa-ab19-916958b23eee' # Global flag.

FLAG_ORI_State_PartneredWithHalsin = '7b53fe60-bb16-48a9-ae5c-9bce1dfac1a9'
FLAG_ORI_State_WasPartneredWithHalsin = 'ee6b727d-243e-4189-b572-1d782ea78df8'
FLAG_ORI_State_HandledBreakupWithHalsin = '1268efe2-38d9-44e8-b83c-e78435344400'
FLAG_CAMP_Halsin_CRD_Romance_CheckWithExistingPartner = 'b523a2ba-8abf-4116-a5c1-636c77920ca3' # Object flag. Set on Tav when you need to ask your other partner about polyamory with Halsin
FLAG_ORI_State_PartneredWithHalsinSecondary = '6af0be74-d032-4a20-876a-11bab5f86db2' # Object flag. Set on Tav if they are in 3-way relationship including the druid.
CAMP_Halsin2_Event_RejectedHalsin = 'c1721e59-995d-40be-8f47-0916154b4408' # Dialog flag. Set when player rejects Halsin.

FLAG_GLO_LiftingTheCurse_State_BreathHasBeenRestored = '2113b54e-a140-4aa0-97ac-219fa7b7d038' # Global flag. Set when the shadow curse was lifted.
FLAG_GLO_LiftingTheCurse_State_HalsinRecruitable = '2c8b6be0-558d-485c-b4f2-93ec1926a2fa' # Global flag.

FLAG_OriginRemoveFromPartyAfterDialog = '7a429beb-fbfb-fa8a-3a33-0349323ad11d' # Set on a companion. They return to camp after the dialog.

FLAG_ORI_Shadowheart_State_ExistentialistCrisis = 'b441440e-832f-4ba2-a82c-a425ae11cf9b' # Global flag. Shadowheart defied Shar and haven't spoken to the Nightsong yet.
FLAG_ORI_Shadowheart_Event_PostNightfall_DiscussionAvailable = '1eefa664-d8c5-6f9e-e662-66625481a89b' # Global flag. Sets when the follow-up to SH nightfall SD ROM is available
FLAG_ORI_Shadowheart_State_PostSkinnyDipping_DiscussionAvailable = '741d48eb-112e-6419-3a67-7b8e5928d7e1' # Global flag. Sets when follow-up discussion to the skinnydipping SD ROM is available
FLAG_Shadowheart_InParty_Event_SkinnyDipStart = '0b659872-c728-4d0d-934d-34c3609cdeb7'
FLAG_ORI_State_PartneredCompanionIncluded = 'c401d64f-025e-433d-911d-1e32d0da37fa' # Player's partnered companion has been included to the current dialog (gets cleared when speaker leaves the dialog).
FLAG_CAMP_Halsin_CRD_Romance_PartnerAllowsHalsin = '2c588e1e-8acb-4c89-8c82-3db5979eb117' # Sets if your existing partner is ok with sharing you with Halsin
FLAG_CAMP_Halsin_CRD_Romance_PartnerDoesNotAllowHalsin = '3dba761a-28cc-4d6d-9af2-1e3835cf9321' # Sets when your existing partner is not ok with sharing you with Halsin
FLAG_GLO_Halsin_Knows_ShadowCurse = '4bfcb6bc-07e0-0cc5-637d-c59f137caa78' # Halsin told the party about the shadow curse
FLAG_Shadowheart_InParty_Event_HappenedThought = '8a9eecb6-3a5c-4292-b0d5-9a3b23d7c5e3' # Tav asked "What do you think of all that's happened to us so far?"
FLAG_LOW_SharGrotto_ConfrontViconia_SharranAlliance = 'ea829b7c-5f69-c4fc-6b4c-b8a190d31a86' # Global flag. Sets when the player is offered the support of the Shar Grotto
FLAG_LOW_SharGrotto_Event_SurrenderShadowheart = 'bfc7f3b7-4e58-44e1-bb58-131ee77fc0ad' # Global flag. Give Shadowheart to Viconia
FLAG_ORI_Shadowheart_ShadowheartBetrayed = 'f78e829a-55cb-4dbf-859e-2f125471fbdc' # Sold Shadowheart to Viconia
FLAG_ORI_State_Recruited = 'e78c0aab-fb48-98e9-3ed9-773a0c39988d' # Set on recruited companions
FLAG_GLO_Minthara_InParty_HasTopicalGreeting = '8069e1a8-51b5-afc0-de8c-f5af844f034d' # Object flag. Minthara has a topical greeting in place of normal greeting

FLAG_DEN_PartyProgress_EnteredGrove = '18cfaaeb-c0df-46ac-962d-0c300f816d73' # Global flag. At least one player entered the grove
FLAG_SHA_PartyProgress_EnteredSharTemple = 'd212e499-d006-4043-9dee-8aac504098e5' # Global flag. The party has entered the shar temple at least once
FLAG_COL_PartyProgress_EnteredColony = '666abe92-f197-4c38-85a8-d879a9e258b6' # Global flag. The party has entered the Colony
FLAG_VISITEDREGION_SCL_Main_A_ACT_2 = 'f6e72539-9bc6-42e1-a20f-390f3a17ad8d' # Global flag. Player visited shadow cursed lands.
FLAG_VISITEDREGION_INT_Main_A_ACT_3 = 'a2e1a618-d211-484e-9389-6b37308b8da1' # Global flag. The party had camped in a region between acts 2 and 3.
FLAG_VISITEDREGION_BGO_Main_A = '40f06537-814f-4796-b012-5ffaa648a8d9' # Global flag. Been in BGO_Main_A (Rivington)
FLAG_VISITEDREGION_CTY_Main_A = 'ce5346f4-c176-43ea-8da0-2067450e26ac' # Global flag. Been in CTY_Main_A (Lower city)

FLAG_LOW_BhaalTemple_State_KilledVictim = 'ba91f332-45d5-483c-b460-dfec2e6d87e9' # Global flag. Flag set in dialog when Orin stabs the victim.

FLAG_DEN_CapturedGoblin_State_PlayerWatchedGoblinExecution = 'cccd8084-dc8f-88c2-c145-482c34ab094f' # Global flag. Tav let Sazza die.
FLAG_DEN_CapturedGoblin_Knows_Priestess = '2ac20f1d-b8a0-4f06-a1e6-50e428a3b487' # Global flag. Sazza told about Gut
FLAG_DEN_Apprentice_Knows_HeardAboutNettie = '07818e31-1a13-0dd8-f02c-c27984614d17' # Global flag. Player knows about Nettie healer
FLAG_DEN_Apprentice_State_SeesExtraPlayers = '45011961-da83-7951-08e7-4a9864f12b4c' # Global flag. There are companions with Tav when they talk to Nettie.
FLAG_DEN_Apprentice_State_Cyanide_ShortPath = '9efd1083-8277-2b08-166d-b8ffaa086ee6' # Object flag. Set on Player when Nettie decided not to poison them.
FLAG_DEN_Apprentice_Event_GiveWyvenPoison = '23c131ba-6a0f-40bf-9bd6-f15a094d78fb' # Object flag. Set on Player who took the poison vial from Nettie.

FLAG_GLO_Absolute_Knows_Name = '1b7fa14e-1a35-342a-5aa9-6342116578b6'

GOB_State_LeadersAreDead = 'a1c5b01f-4b7f-47ab-82b0-d24d9c6d8bc6' # Global flag. Goblin leaders are dead
DEN_GoblinHunt_Event_LeaderMetPlayer = '097d69b7-7e59-49ba-830a-b2b7f950aec7' # Global flag. Flag set once the designated leader of the tieflings has met a player at the entrance of the Grove.
DEN_AttackOnDen_State_DenVictory = '71c7f23e-3ff1-c9b8-3ef5-d75fa1b42c8d' # Global flag. The tieflings won Attack on Den or Goblin Hunt was completed
DEN_AttackOnDen_State_RaiderVictory = 'abe1bce8-c234-4afe-a490-76210d98a078' # Global flag. Tieflings in the den were killed during Attack On Den
DEN_Lockdown_State_Active = '0b54c7d2-b7b1-4d0f-b8e4-0cf1ee32b1eb' # Global flag. The Druids' Grove is under lockdown.

FLAG_ORI_Shadowheart_SeenWithBox = '31d00a1b-9f7b-7385-4d94-e6f98883742c' # Global flag. Tav has seen Shadowheart with the artifact.
FLAG_GOB_Orpheus_State_HadVoiceOfAbsoluteEvent = '9546407d-19e3-4f26-88af-5970896997d7' # Global flag. The player took part in Voice of Absolute dialog and saw Orpheus box protecting from the Voice.
FLAG_Shadowheart_InParty_Event_LostBoxStart = '0f6714f5-b042-4432-9bbb-addbed1f1037' # Object flag. Set on player for a discission about artefact changing the owner
FLAG_ORI_Shadowheart_Event_OprheusProtectionFollowUpConcluded = 'c1be414f-6603-9385-8ce0-1f63cb2084ac' # Object flag. Set on player
FLAG_Act2_PointOfNoReturnReached = 'a3155f30-b8f3-4db5-ac21-d3036f4426e3' # Global flag. We entered the Shadowfell and the act 2 point of no return has been reached.

# Set to true when Tav reads Halsin's notebook describing his role in Isobel's death
DEN_DruidLair_Knows_SharDagger = '72d2bbf3-afab-0f8a-2654-73f04a213e2c'

FLAG_Companion_Leaves_Party = "363c71f4-8b46-c0c0-4bbb-0e5a85e4652d" # If set on a companion, they leave the party

# Dialog inclusion flags
FLAG_ORI_Inclusion_ShadowHeart = 'b7b419d9-2148-4acd-af40-85a1cae55204'
FLAG_ORI_Inclusion_End_ShadowHeart = 'cdc93794-08f8-4563-b721-c00872170dbf'
FLAG_ORI_Inclusion_Wyll = '31aca0be-c868-47bb-a1c2-601ff756b863'
FLAG_ORI_Inclusion_End_Wyll = '51c81a82-b1f7-4cb4-b6a9-abe16240bdd4'


# Global flags that indicate whether an origin character is an avatar (a human controlled player) or a companion
FLAG_GLO_Origin_Avatar_Shadowheart = '1a2858f5-f481-4af8-9440-1a2315df86b8' # Set when Shadowheart is part of the team and avatar, regardless of whether in camp or in party
FLAG_GLO_Origin_PartOfTheTeam_Shadowheart = '7f9ac9e8-1e8d-4bf8-8716-68215f0f066e' # Set when Shadowheart is part of the team, meaning recruited, regardless of whether in camp or in party
FLAG_GLO_Origin_Avatar_Laezel = 'ecbab7a6-0a96-4c30-81d1-f70cc960b749' # Set when Laezel is part of the team and avatar, regardless of whether in camp or in party
FLAG_GLO_Origin_PartOfTheTeam_Laezel = '57d93a1d-4400-4307-845f-25d9a250d332' # Set when Laezel is part of the team, meaning recruited, regardless of whether in camp or in party
FLAG_GLO_Origin_Avatar_Astarion = '5304da6f-4174-4253-b456-de4b0aadb33c' # Set when Astarion is part of the team and avatar, regardless of whether in camp or in party
FLAG_GLO_Origin_PartOfTheTeam_Astarion = '24ae9cee-0516-47c6-8291-cb143256264d' # Set when Astarion is part of the team, meaning recruited, regardless of whether in camp or in party
FLAG_GLO_Origin_Avatar_Gale = '7e4814d1-d7f5-4fbd-a101-8492eea43072' # Set when Gale is part of the team and avatar, regardless of whether in camp or in party
FLAG_GLO_Origin_PartOfTheTeam_Gale = '4f1acb3b-17e8-4036-a43c-fc6ee2828061' # Set when Gale is part of the team, meaning recruited, regardless of whether in camp or in party
FLAG_GLO_Origin_Avatar_Wyll = '4a2d36e6-e036-48dd-9c89-b99a19c053a0' # Set when Wyll is part of the team and avatar, regardless of whether in camp or in party
FLAG_GLO_Origin_PartOfTheTeam_Wyll = '24e24ca7-3446-440b-b645-19404845e108' # Set when Wyll is part of the team, meaning recruited, regardless of whether in camp or in party
FLAG_GLO_Origin_Avatar_Karlach = 'b5ad4b07-9522-47ec-98e6-85c28df64dc5' # Set when Karlach is part of the team and avatar, regardless of whether in camp or in party
FLAG_GLO_Origin_PartOfTheTeam_Karlach = 'b1e6f12a-600a-4e2e-9871-b08a9fe3a617' # Set when Karlach is part of the team, meaning recruited, regardless of whether in camp or in party
FLAG_GLO_Jaheira_State_PermaDefeated = '932fb5a1-00ba-4621-b7ae-877d40d7ddcd' # Jaheira is permanently defeated
FLAG_GLO_Origin_PartOfTheTeam_Jaheira = 'd7d29efe-70bb-47c2-9db3-bc8a10347bc6' # Set when Jaheira is part of the team, meaning recruited, regardless of whether in camp or in party
FLAG_GLO_Origin_PartOfTheTeam_Minsc = '3510cd49-7ff6-475c-829b-d4d68a07b085' # Set when Minsc is part of the team, meaning recruited, regardless of whether in camp or in party

GLO_Companion_LeaveBlocked = '4386e3a1-b16e-4331-92ec-29edbc359d51' # Companion is blocked from leaving the party - cannot be dismissed or leave through low approval" />

FLAG_LOW_CountingHouse_State_RobbersEscaped = '16197488-9cc2-48e2-94ae-36225025d4d8' # Global flag
FLAG_Jaheira_InParty_SpokeOfDoppelgangerJaheira = 'e8c6623a-32fc-4cfa-97e1-31803ab4158b' # Global flag
FLAG_ORI_Jaheira_Event_FoundLinkToSewers = 'f4e926b4-77c6-e1dd-9ce9-7467a15668bc' # Global flag

FLAG_Shadowheart_InParty_Event_AstralTadpoleStart = 'ef5c1269-1b52-445c-9f4a-c262d33e079e' # Object flag
FLAG_GLO_Tadpole_Event_BlockedTadpoleConvinceFailRepeatableApprovalDrain = '250e7baf-77e9-c42e-1981-05412a5f8457' # Object flag. Failed to convince the companion to remove their tadpole block: Repeatable Approval Drain" />
FLAG_Shadowheart_InParty_State_EndDialog = '83c61046-f6c7-4d0b-a012-37fdce36d957' # Set on Tav to end the dialog

# Flags (kisses)
FLAG_ORI_Kiss_StartRandom = '2a98bc41-f6b7-4277-a282-1a91c4ef8a9b' # Set on speaker to start a random kiss selection.
FLAG_ORI_Kiss_EndRandom = 'f13348d0-34bf-4328-80a5-29dd8a7b0aef' # Clears random kiss selection
FLAG_ORI_Kiss_VersionA = '6061dd44-55fe-41b0-a79c-fc696073de0a'
FLAG_ORI_Kiss_VersionB = '8da83898-1476-43e7-ab38-314c61b1ff74'
FLAG_ORI_Kiss_VersionC = '98e473ed-0144-482c-853a-e4fc739646f5'
FLAG_ORI_Kiss_VersionD = '0bdf3afd-1997-4c9e-82f3-b1365a47034c'

# Shadowheart's romance scene
FLAG_Shadowheart_InParty_Event_SkinnyDipQuestionStart = '14f885d5-b35c-4772-9f28-f042341a2f9f'
FLAG_Shadowheart_InParty_Event_NightfallQuestionStart = 'c8fd0751-450d-4fb2-b1c5-3622336fd8e1'

FLAG_ORI_Shadowheart_Event_SkinnyDippingRomanceScene = '3437a073-b92a-4999-b6b9-e7745865a0c2' # Starts the skinny dipping romance scene

FLAG_CAMP_Shadowheart_State_HadNightsongMeeting = '10b74e80-a963-420f-8c2a-d518b6aae143' # Global flag. Nightsong spoke to Shadowheart in camp (set immediately)
FLAG_NIGHT_NightsongShadowheartVisit = '5cf06d9e-44ce-4431-a1c6-839bfdad5f79' # Global flag. Nightsong spoke to Shadowheart in camp (night happened, set after LR).
FLAG_NIGHT_Shadowheart_DaughterTears = 'f9b1fa94-deef-4927-ad7d-3e1b0c393c13' # Global flag. Daughter's Tears scene has happened.

FLAG_NIGHT_Shadowheart_Skinnydipping = '9f583304-0a1a-498c-acf9-3c8dcc30ee3d' # Global flag. Skinny dipping has happened.
FLAG_ORI_Shadowheart_State_PostSkinnyDipping_DiscussionAvailable = '41d48eb-112e-6419-3a67-7b8e5928d7e1' # Global flag. Skinny dipping discussion is available.
FLAG_ORI_Shadowheart_State_PostSkinnydipping_Discussed = 'f0a86777-beff-43ed-92e4-ebc1568c51fc' # Global flag. Sets once the follow-up to the Skinny Dipping SD ROM has occurred.

FLAG_NIGHT_Shadowheart_NightfallRitual = '8f1697d4-2402-4283-802a-ef7e1ebd8aa1' # Global flag. Nightfall ritual has happened
FLAG_ORI_Shadowheart_Event_PostNightfall_DiscussionAvailable = '1eefa664-d8c5-6f9e-e662-66625481a89b' # Global flag. 
FLAG_ORI_Shadowheart_State_PostNightfall_Discussed = '9884856d-1885-b82c-638c-fa6c2788a677' # Global flag. Discussed the Nightfall ritual
FLAG_ORI_Shadowheart_State_AbortedNightfall = 'becb720c-0e30-448d-b1a5-42cddf36409f' # Global flag. Tav ran away from the Nightfall ritual
FLAG_Shadowheart_InParty_State_DiscussedAbortedNightfall = '2c40104c-8f1e-4601-91f6-62704c487b5c' # Global flag. Discussed the aborted Nightfall ritual

# Camp state flags
FLAG_GLO_CAMP_State_NightMode = 'fb53edc2-9a89-4ad2-af83-20b5fe425cdd'
FLAG_CAMP_GLO_State_InCamp = '161b7223-039d-4ebe-986f-1dcd9a66733f' # Set on a character when they are in camp
FLAG_GLO_Camp_Event_SkipSleepCutscene = '1ee0a25e-4115-44ef-b87d-c2a5eee494b6' # Global flag, set this during a night dialogue to skip the succeeding sleepcutscene

# Dapper drow related flags
FLAG_WYR_DapperDrow_Event_IntimacyDone = '10cfd95c-876e-cce9-9138-5593b5b5a33e' # Global flag. Intimate scene with Drow is complete.
FLAG_WYR_DapperDrow_State_HiredBrother = 'e0d6ad5e-c5d4-9d8c-8c6f-997694d6f7b8' # Set on a character. The player hired dapper drow brother.
FLAG_WYR_DapperDrow_State_HiredSister = '390a05d9-0313-095d-1356-1884bdf6273e'  # Set on a character. The player hired dapper drow sister.
FLAG_WYR_DapperDrow_State_HiredBoth = '4dc060ee-1076-ba53-8663-e436665b4800'    # The player hired both drows.

FLAG_GLO_Tadpoled_UsedToday1 = '36d218ea-3eab-481f-fdaa-4ee185e76c25' # This character used the tadpole once today
FLAG_GLO_TadpoledCount1 = 'ff1c4f21-91b7-9c21-0ed6-74ec9c1c5628' # This character used the tadpole for the first time today
FLAG_GLO_TadpoledCount2 = 'd35434a5-94f1-88b2-479d-674b9aee2a29' # This character used the tadpole for the second time today

FLAG_GLO_SafeRomance_Enabled = 'f46a2601-92d1-4b86-98b5-0dae4a290ff6' # Is the safe romance option enabled?

# End game companion random inclusion
END_RandomCompanion_Picked = 'd39d2a4e-2efb-c14c-ba23-f5c03fac5038' # Global flag. This companion was randomly picked in the end game dialogue.


# Global Flags: Allies
# Good allies
FLAG_ORI_Astarion_State_StayedVampireSpawn = '2724b881-6be1-49a7-8375-a49e9acb4546'
FLAG_GLO_Volo_State_AtCamp = 'de1cadca-2eca-4cee-a3dc-e262bbb92277'
FLAG_LOW_SorcerousSundries_State_ProdigyHasStayedAtRamazith = '524ab56a-8169-4926-9105-8bcaf8c87499'
FLAG_LOW_SorcerousSundries_State_PlayersSideWithNightsong = '992ec758-9536-40ce-9a45-72193c81ec1b'
FLAG_CAMP_OwlbearCub_State_Friend = '3b963a1c-ca06-db60-75c3-063592e84dc4'
FLAG_GLO_Origin_PartOfTheTeam_Jaheira = 'd7d29efe-70bb-47c2-9db3-bc8a10347bc6'
FLAG_COL_TadpolingCentre_Event_ReleasePods = '3e81dc65-eb2d-86aa-5163-28450894f868'
FLAG_GLO_LiftingTheCurse_State_BreathHasBeenRestored = '2113b54e-a140-4aa0-97ac-219fa7b7d038'
FLAG_LOW_MurderTribunal_Event_ValeriaLeavesTribunal = '57a75bf2-2648-c9f8-e75e-8366c582225e'
FLAG_LOW_SteelWatchFoundry_State_GainedGondianENDSupport = '1bb09a8b-001d-4b43-9f39-ba89eb3aece9'
FLAG_LOW_SteelWatchFoundry_BarcusIsLeader = '2feaf431-1f1d-d951-7b4f-daa744985a46'
FLAG_CAMP_ArabellaPowers_State_JergalToldToLeave = '3d22614e-8762-8aec-4537-9d50abb97b23'
FLAG_WYR_WyrmRockPrison_State_FlorrickEscaped = 'a84a5b16-ca29-43c3-91bf-17def670ba07'
FLAG_LOW_Guildhall_State_SidedWithNineFingers = '9a6c3448-67c8-e23a-ed28-7b3cfba65bf5'
FLAG_CAMP_Ravengard_State_RavengardInCamp = '37309008-04cf-493c-8ca6-43034d331a8a'
FLAG_LOW_Guildhall_State_MolHelpsPlayerInEND = '5c4d5b0f-a9bb-4fe0-8003-2af9213a64b0'

# Bad allies
FLAG_ORI_Astarion_State_BecameVampireLord = 'c446ce94-efd8-45d5-b407-284177b6b57e'
FLAG_END_GatherYourAllies_State_WulbrenGaveIronhandSupport = 'dd929cfa-685e-41d6-8e04-be2f1a14da98'
FLAG_LOW_Guildhall_State_PostCoup_ZhentControlled = 'bd914804-54c7-4de2-b51e-988919c2e644'
FLAG_LOW_SorcerousSundries_State_PlayersSideWithLorroakan = '24c45d86-9027-48cc-afdd-3e6bac7d5425'
FLAG_LOW_Orthon_State_PromisedENDSupport = 'b412f8bc-1cc6-2ac9-058e-8a5d06e77c5a'
FLAG_CAMP_MizorasPact_State_WyllEternalPact = '8da8b1fb-5aa9-8cf5-8b45-6f8ca31a1227'
FLAG_LOW_DevilishOx_State_HelpedPhasmToCity = 'd1498063-a466-4f43-8cb5-103baa46c753'
FLAG_LOW_BlushingMermaid_State_HagIsAllyInEND = '3bb65bd3-a72f-4a43-a497-10b1501cd6a5'


# Part of the team global flags
FLAG_GLO_Origin_PartOfTheTeam_Shadowheart = '7f9ac9e8-1e8d-4bf8-8716-68215f0f066e'
FLAG_GLO_Origin_PartOfTheTeam_Astarion = '24ae9cee-0516-47c6-8291-cb143256264d'
FLAG_GLO_Origin_PartOfTheTeam_Wyll = '24e24ca7-3446-440b-b645-19404845e108'
FLAG_GLO_Origin_PartOfTheTeam_Karlach = 'b1e6f12a-600a-4e2e-9871-b08a9fe3a617'
FLAG_GLO_Origin_PartOfTheTeam_Gale = '4f1acb3b-17e8-4036-a43c-fc6ee2828061'
FLAG_GLO_Origin_PartOfTheTeam_Halsin = '77382f4f-8302-4642-b6ba-6f0bc8acf5c3'
FLAG_GLO_Origin_PartOfTheTeam_Minthara = 'fa0e4e0b-08f9-4094-bfed-5205481c683c'
FLAG_GLO_Origin_PartOfTheTeam_Laezel = '57d93a1d-4400-4307-845f-25d9a250d332'

# IsInParty global flags, True if companion is in party
FLAG_ORI_ShadowHeart_State_IsInParty = '9a029c5a-e3c3-45ef-9cd4-1cb45718deb1'
FLAG_ORI_Astarion_State_IsInParty = 'ef789a01-f41e-4a7d-9097-fa9c4f1d0f16'
FLAG_ORI_Wyll_State_IsInParty = '3c0972ef-d7a4-46ac-abdd-0ce6aadd61b0'
FLAG_ORI_Karlach_State_IsInParty = 'eb7c4de0-36b7-4086-aa33-82c09596a395'
FLAG_ORI_Gale_State_IsInParty = '639d141f-6fa8-4d93-8eb7-41243e0fea32'
FLAG_ORI_Halsin_State_IsInParty = '9a3ea4cd-3a44-40f7-9d63-2b29bdb28725'
FLAG_ORI_Minthara_State_IsInParty = '766b8981-eb17-3ec5-5d30-2626509c550f'
FLAG_ORI_Laezel_State_IsInParty = '3ee6b1f2-24f4-4e85-b7dc-49060e6d2699'


# Tags: 'really' tags
TAG_REALLY_SHADOWHEART = '642d2aee-e3df-47e3-9f47-bbcd441bb9e0'
TAG_REALLY_DARK_URGE = 'cd611d7d-b67d-42b4-a75c-a0c6091ef8a2'
TAG_REALLY_ASTARION = 'ffd08582-7396-4cac-bcd4-8f9cd0fd8ef3'
TAG_REALLY_GALE = '9b0354c0-56d9-4723-8034-918ac9abab19'
TAG_REALLY_HALSIN = '9b8709f9-8d2a-4b4e-a465-8505c561d7f5'
TAG_REALLY_JAHEIRA = '8457eb5f-036c-4143-b6cf-447a9f555c7a'
TAG_REALLY_KARLACH = '1a2f70d6-8ead-4eb5-a824-79ee1971764a'
TAG_REALLY_LAEZEL = 'b5682d1d-c395-489c-9675-1f9b0c328ea5'
TAG_REALLY_MINSC = 'aeb694fc-83fb-452d-819a-b97ba442dc42'
TAG_REALLY_MINTHARA = '3e84e1cd-2193-4f9f-80b4-c2ededefaea6'
TAG_REALLY_WYLL = '5f40def5-d3ec-4698-a367-01a339888956'

REALLY_TAGS = {
    TAG_REALLY_SHADOWHEART,
    TAG_REALLY_DARK_URGE,
    TAG_REALLY_ASTARION,
    TAG_REALLY_GALE,
    TAG_REALLY_HALSIN,
    TAG_REALLY_JAHEIRA,
    TAG_REALLY_KARLACH,
    TAG_REALLY_LAEZEL,
    TAG_REALLY_MINSC,
    TAG_REALLY_MINTHARA,
    TAG_REALLY_WYLL,
}

# Tags: other
TAG_SHADOWHEART = '8b4cf0fa-f712-4839-9439-f86a519078fa'
TAG_SHADOWHEART_ENEMYOFSHARPATH = '8eca8027-996c-4c61-bec6-77f853de295b'
TAG_SHADOWHEART_SHARPATH = '9624a3fe-bb9e-47c5-b9ab-417e6da6f84b'
TAG_SHORT = '50e7beca-4e90-43cd-b7c5-c235e236077f'
TAG_DWARF = '486a2562-31ae-437b-bf63-30393e18cbdd'
TAG_DRAGONBORN = '02e5e9ed-b6b2-4524-99cd-cb2bc84c754a'
TAG_GITH = '677ffa76-2562-4217-873e-2253d4720ba4'
TAG_GOBLIN = '608597d9-bf00-4ede-aabe-767457280925'
TAG_BODYTYPE_STRONG = 'd3116e58-c55a-4853-a700-bee996207397'
TAG_MALE = '8f74d144-041e-4035-a9ac-72f41fc32de7'
TAG_FEMALE = '3806477c-65a7-4100-9f92-be4c12c4fa4f'
TAG_FULL_CEREMORPH = '3797bfc4-8004-4a19-9578-61ce0714cc0b' # Player has become a full Mind Flayer
TAG_HUMANOID_MONSTER = '7fbed0d4-cabc-4a9d-804e-12ca6088a0a8'
TAG_AVATAR = '306b9b05-1057-4770-aa17-01af21acd650'
TAG_HALFORC = '3311a9a9-cdbc-4b05-9bf6-e02ba1fc72a3'

# Classes
TAG_FIGHTER   = '1ae7017c-4884-4a43-bc4a-742fa0d201c0'
TAG_BARBARIAN = '02913f9a-f696-40cf-acdf-32032afab32c'
TAG_WARLOCK   = '5804f55a-93f7-4281-9512-8d548a9e2a22'
TAG_BARD      = 'd93434bd-6b71-4789-b128-ee24156057cc'
TAG_ROGUE     = 'f8a0608b-666c-4be6-a49c-03b369c10bd2'
TAG_RANGER    = '37a733c1-a862-4157-b92a-9cff46232c6a'
TAG_CLERIC    = '1671b4bf-4f47-4bb7-9cb9-80bb1f6009d5'
TAG_PALADIN   = '6d85ab2d-5c23-498c-a61e-98f05a00177a'
TAG_SORCERER  = '18266c0b-efbc-4c80-8784-ada4a37218d7'
TAG_WIZARD    = '6fe3ae27-dc6c-4fc9-9245-710c790c396c'
TAG_DRUID     = '44ac4317-4d38-4d28-80e2-94024c6e42f0'
TAG_MONK      = 'e1e460bb-d0ae-4452-8529-c9e176558731'

TAG_OATHBREAKER = 'c7bdcdf2-15e7-456e-adf1-21dda3172e18'


# Races
TAG_REALLY_GITHYANKI = 'e49c027c-6ec6-4158-9afb-8b59236d10fd'
TAG_REALLY_LOLTHDROW = 'c71eb8de-74e3-4d70-9826-22da7e2dc607'

# Religion related tags
TAG_CLERIC_SELUNE =     '10b2a53c-3eb0-451c-8057-0f1cc9e62a4d'
TAG_CLERIC_SHAR =       '0d1d64b8-70d6-4702-8643-be348b0f3fc6'
TAG_CLERIC_TEMPUS =     '31d96353-a4b8-4abf-9cce-f7a9174e65da'
TAG_CLERIC_TYR =        '16657b43-323e-4eee-8982-77338229444b'
TAG_CLERIC_HELM =       '6c28eba6-f46c-4755-9e4e-0223e64f7d72'
TAG_CLERIC_ILMATER =    '838e9a70-94fc-4bcf-850a-19be5247a43b'
TAG_CLERIC_MYSTRA =     '90de46bd-9f0c-4c2f-9505-56063b31b360'
TAG_CLERIC_OGHMA =      '9fbbedb6-c485-4c6b-94b7-c7d7592223b3'
TAG_CLERIC_KELEMVOR =   'a01efcc1-9e2f-4438-956b-b448cbf73bde'
TAG_CLERIC_MORADIN =    '3ce8734c-440c-43f8-b0f4-079d69e7eb33'
TAG_CLERIC_CORELLON =   'ca4e5850-139e-4b52-9d5e-553e33ff082a'
TAG_CLERIC_GARL =       '67bd28cc-9cf4-4c64-9213-8d26fbe27e1b'
TAG_CLERIC_YONDALLA =   '4335093d-2fa7-4775-a4cc-bc17b5d16e5a'
TAG_CLERIC_LOLTH =      '7aee9e55-ecb4-4cdc-804d-1ec20d07efc5'
TAG_CLERIC_LADUGUER =   '4276e5a0-f6b3-4f4e-8836-4cd8b0cade2f'
TAG_CLERIC_VLAAKITH =   '91b2d344-fce8-48b3-a83d-9688cbddb1b8'
TAG_CLERIC_EILISTRAEE = 'c4749983-8bb9-4aa5-bf18-afd9cb1ce915'
TAG_CLERIC_LATHANDER =  '6e31b516-92fc-4526-b1cd-92516e02cf86'
TAG_CLERIC_TALOS =      'da25a7cc-066d-43dc-8f1e-74c17cd0d589'
TAG_CLERIC_TYMORA =     'edc085f7-63f8-4bb0-b60c-b68c92b67708'
TAG_CLERIC_MIELIKKI =   '5ce73ec6-be80-4853-ad3c-12149d71e07e'
TAG_CLERIC_BAHAMUT =    '28ee4ac1-86a3-490e-ab02-7085bd7c56d6'
TAG_CLERIC_GRUUMSH =    'c3743bdd-3653-47fb-8a5c-d8489d7a1be0'
TAG_CLERIC_TIAMAT =     '4cd1c7f7-7a8c-421a-87dc-687c4eefd683'
TAG_CLERIC_BHAAL =      'b03d4a89-bba7-45a4-a89d-a132ddd75637'
TAG_CLERIC_BANE =       '178016d5-e3d3-44bd-8aa5-6ac3d1c61e6c'
TAG_CLERIC_MYRKUL =     '7ea36792-21e5-4ea9-9544-de276651c376'

TAG_CLERIC_GOOD =       '64dc9d31-db7a-418e-bbbe-6f5b4d32608f'
TAG_CLERIC_NEUTRAL =    '2947a463-3c45-4a70-959a-3e81a943ab92'
TAG_CLERIC_EVIL =       'aa9f126f-ac9a-48d9-a128-1394fae8f4e8'

TAG_DARK_JUSTICIAR =    '4e4e26e8-9bbf-4913-93c7-c55972a6d051'

# Tags used on God UUID objects to define their alignment. Don't change their names
ALIGN_GOOD =            '34064d50-38fe-44e4-aaed-129ac3b44933'
ALIGN_NEUTRAL =         'c1ff8a7f-c430-4671-bc4e-098f874ae302'
ALIGN_EVIL =            '6d08632e-0300-4587-80b9-8e411b0efb3b' 


# Gods
GODLESS =                'df89bab1-3d1e-43f2-b2ea-3721b44fffa5'
GOD_SELUNE =             '4533d292-5b1f-43c7-ad44-6bc7db1000ca'
GOD_SHAR =               '486e4a27-e6f9-40a5-9dd1-108a1d0f60eb'
GOD_TEMPUS =             'f6b88f18-328f-41c3-a579-e8a9b99c410b'
GOD_TYR =                'aa9a53ed-afad-4a6d-824c-ff0125986eb7'
GOD_HELM =               'c33d2cf7-1c8d-41ea-b4d9-4773778410f6'
GOD_ILMATER =            '75586076-1aaf-4e4a-a516-93f1e6cd3472'
GOD_MYSTRA =             'e79d9eca-e8ac-486a-bd21-cf42ef1133af'
GOD_OGHMA =              '7b019d89-9b7e-4c2a-a6b4-ffb64f25f734'
GOD_KELEMVOR =           '23541bea-8177-496d-b58b-c29c4f13c22c'
GOD_MORADIN =            'cfad7ead-098a-4944-84a6-d0570a98984d'
GOD_CORELLON_LARETHIAN = '575b3b3c-4a5b-44d5-868f-0c6875f95568'
GOD_GARL_GLITTERGOLD =   '4a4130a1-c96a-43e8-91cc-1e3959e50053'
GOD_YONDALLA =           'dc005135-7eee-4406-a46e-9535e7412422'
GOD_LOLTH =              '899a6ce7-731e-473b-b87b-5d0cf383abff'
GOD_LADUGUER =           '92919073-a23b-490a-a316-a083f179f083'
GOD_VLAAKITH =           'd84b4081-6800-45f9-b03f-16dba592c75d'
GOD_EILISTRAEE =         '7cef166f-7766-4332-b9aa-d0d06fbca61e'
GOD_LATHANDER =          '7cae2d74-89f3-4312-9816-6ae6827f318c'
GOD_TALOS =              'c8650f16-4610-4648-95d1-18a44a1188b7'
GOD_TYMORA =             'c0b03fe2-6495-4340-a0c8-ed6ccf206bcc'
GOD_MIELIKKI =           'f21f419c-bbf8-42df-ae89-f1de72e90cf5'
GOD_BAHAMUT =            'fdccfc34-47e9-45ff-8755-511f91cb0e97'
GOD_GRUUMSH =            '7ef33e10-bdb0-4268-833a-5da1e52aa26a'
GOD_TIAMAT =             '328683c2-8785-4b71-b128-7cec90df0abe'
GOD_BHAAL =              'f5e62c47-fb93-449f-9057-cb1a3c003aff'
GOD_BANE =               '494bddcf-9325-4883-a937-817fbdf11161'
GOD_MYRKUL =             'f1fc9c3f-0db9-4d19-adb4-18b1174a6b9d'


# Other tags
TAG_TADPOLED_ILLITHID = '1eec74e8-3673-4500-abec-57b7ed8469ed'


# Approval flags
FLAG_Approval_AtLeast_60_For_Sp1  = '4445984d-56f3-0e7c-25d5-cf5cca2a5642'
FLAG_Approval_AtLeast_80_For_Sp1  = 'c014f892-8450-7821-8936-f862cc67654e'

FLAG_Approval_AtLeast_N20_For_Sp2 = '4c39c64b-8373-6f5f-2dac-990196d3c6dc'
FLAG_Approval_AtLeast_0_For_Sp2   = 'c90a1ed4-c142-3300-65d0-0a0a4d6e08f7'
FLAG_Approval_AtLeast_5_For_Sp2   = '1966ea6c-0567-401b-96b6-28eb2b9116b8'
FLAG_Approval_AtLeast_10_For_Sp2  = 'fccac36f-92a5-ad84-9e45-fed71d386452'
FLAG_Approval_AtLeast_20_For_Sp2  = '91cfff92-fb1e-caf5-9d5c-9c5971b96d04'
FLAG_Approval_AtLeast_30_For_Sp2  = '98ca7185-0f2d-4420-be81-2b7c5e109e91'
FLAG_Approval_AtLeast_40_For_Sp2  = 'cb50595f-b514-26a8-0c90-fbb21185b22e'
FLAG_Approval_AtLeast_60_For_Sp2  = 'bf670cb3-8110-e901-ed45-bb0b0f15b761'
FLAG_Approval_AtLeast_80_For_Sp2  = '4975d4b7-031d-7a78-778a-86b46503a224'

FLAG_Approval_AtLeast_10_For_Sp3  = 'be8510e8-0339-3fee-f198-b1dbe1a0b010'
FLAG_Approval_AtLeast_20_For_Sp3  = '1e3e9473-4277-79b5-42a2-cfd066386593'
FLAG_Approval_AtLeast_30_For_Sp3  = '534d898c-b83a-2523-eff2-e44fec0c207e'
FLAG_Approval_AtLeast_40_For_Sp3  = 'f1ab5792-7ebe-3021-bb12-e8b749507477'
FLAG_Approval_AtLeast_50_For_Sp3  = '1ab5dca5-dc29-9dcc-2f8f-bcc15147a15c'
FLAG_Approval_AtLeast_60_For_Sp3  = '379b2a1e-207f-fca8-b2e7-372dc8751a5d'
FLAG_Approval_AtLeast_70_For_Sp3  = '207d5eaa-871d-a8ff-7ef4-a3778ef41660'
FLAG_Approval_AtLeast_80_For_Sp3  = '5d4a8ffd-8e6b-f5ad-22f4-c4c21fe9f3e0'
FLAG_Approval_AtLeast_90_For_Sp3  = '4caef451-20b0-49ff-c5ad-954fadd29d44'
FLAG_Approval_AtLeast_100_For_Sp3 = '4c9f41f5-b15c-7c2b-b62e-9c9b16ca46f5'

FLAG_Approval_AtLeast_10_For_Sp7  = 'ad3eebe2-0608-3b7d-940d-0a5f89817009'
FLAG_Approval_AtLeast_20_For_Sp7  = 'dfc5c129-03de-43ec-1355-b91dd281d1d3'
FLAG_Approval_AtLeast_30_For_Sp7  = 'da1fcdc2-de0d-7ff8-0487-9b970cdb6a01'
FLAG_Approval_AtLeast_40_For_Sp7  = 'e4647aa3-27b6-9141-1852-c3cb9ad387dc'
FLAG_Approval_AtLeast_50_For_Sp7  = '558ee7d5-41ec-430e-2f6e-b88d0164dbc8'
FLAG_Approval_AtLeast_60_For_Sp7  = 'f5e9b2a3-7008-f239-ed0d-c8c93468f4a3'
FLAG_Approval_AtLeast_70_For_Sp7  = '5b917a54-1f88-8d60-bee2-a0cac84fa475'
FLAG_Approval_AtLeast_80_For_Sp7  = 'b62c330f-45c1-31f8-259c-1612e5bde942'
FLAG_Approval_AtLeast_90_For_Sp7  = 'b0467b67-bbe5-5835-2788-3060dae6e779'
FLAG_Approval_AtLeast_100_For_Sp7 = 'ebeb67a2-c031-0b10-9205-041ece18f242'


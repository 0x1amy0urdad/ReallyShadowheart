from __future__ import annotations

import bg3moddinglib as bg3

from .context import files

###############################################################
# Custom flags
###############################################################

Really_Shadowheart_Softened_Version = bg3.flag_object(
    files, 'Really_Shadowheart_Softened_Version', bg3.GLOBAL_FLAG, flag_uuid='6435fd62-be1d-4bed-9f00-70c8468c02d4', description='Really Shadowheart softened version')

Shadowheart_Turned_Away_From_Shar = bg3.flag_object(
    files, 'Shadowheart_Turned_Away_From_Shar', bg3.GLOBAL_FLAG, flag_uuid='87c6c40a-87b5-4ffd-8d37-a5679258e7b0', description='Shadowheart turned away from Shar (either Selunite or late redemption)')

Shadowheart_After_Shadowfell = bg3.flag_object(
    files, 'Shadowheart_After_Shadowfell', bg3.GLOBAL_FLAG, flag_uuid='fb309297-8faf-4216-9425-f729c2c8dc7a', description='Shadowheart after Shadowfell')

# Emmeline_Blessed_Tav
Arnell_Blessed_Tav = bg3.flag_object(
    files, 'Arnell_Blessed_Tav', bg3.OBJECT_FLAG, flag_uuid='3e9033a6-8438-41f3-93fb-a376ae4d2c3f', description='Tav asked and received blessing from Arnell')

# Emmeline_Blessed_Tav
Emmeline_Blessed_Tav = bg3.flag_object(
    files, 'Emmeline_Blessed_Tav', bg3.OBJECT_FLAG, flag_uuid='6a9f9b77-5683-44c6-bac8-bc6a524696ca', description='Tav asked and received blessing from Emmeline')

# Kisses
ORI_ShadowheartKiss_StartRandom = bg3.flag_object(
    files, 'ORI_ShadowheartKiss_StartRandom', bg3.OBJECT_FLAG, flag_uuid='7495e78c-9e70-4ea9-95eb-17fde7f94b7c', description='Shadowheart random kiss start')
ORI_ShadowheartKiss_VersionA = bg3.flag_object(
    files, 'ORI_ShadowheartKiss_VersionA', bg3.OBJECT_FLAG, flag_uuid='f2781286-e51c-443f-b1a3-cea4ba95ccf9', description='Shadowheart kiss variant A')
ORI_ShadowheartKiss_VersionB = bg3.flag_object(
    files, 'ORI_ShadowheartKiss_VersionB', bg3.OBJECT_FLAG, flag_uuid='815a0406-7c85-4107-b704-439320fb7f0b', description='Shadowheart kiss variant B')
ORI_ShadowheartKiss_VersionC = bg3.flag_object(
    files, 'ORI_ShadowheartKiss_VersionC', bg3.OBJECT_FLAG, flag_uuid='c07bfea6-3d37-48f3-aefc-6eb1749b117f', description='Shadowheart kiss variant C')
ORI_ShadowheartKiss_VersionD = bg3.flag_object(
    files, 'ORI_ShadowheartKiss_VersionD', bg3.OBJECT_FLAG, flag_uuid='db362653-5649-4f1d-bc43-32b85fd42c0e', description='Shadowheart kiss variant D')
ORI_ShadowheartKiss_VersionE = bg3.flag_object(
    files, 'ORI_ShadowheartKiss_VersionE', bg3.OBJECT_FLAG, flag_uuid='ec79178f-2c18-4a71-b147-7b254439e5b2', description='Shadowheart kiss variant E')
ORI_ShadowheartKiss_VersionF = bg3.flag_object(
    files, 'ORI_ShadowheartKiss_VersionF', bg3.OBJECT_FLAG, flag_uuid='321d447c-5298-4a5c-82de-f884ba4757d4', description='Shadowheart kiss variant F')
ORI_ShadowheartKiss_LoveYou = bg3.flag_object(
    files, 'ORI_ShadowheartKiss_LoveYou', bg3.OBJECT_FLAG, flag_uuid='9e69e807-7153-45ab-8821-c5ece0716df7', description='Shadowheart kiss love you')

# Shadowheart_Kiss_Event
Shadowheart_Kiss_Event = bg3.flag_object(
    files, 'Shadowheart_Kiss_Event', bg3.OBJECT_FLAG, flag_uuid='c19efced-0896-451a-ab8c-671b4df21d30', description='Shadowheart kissed Tav event, set on Tav')

# Shadowheart kisses Tav (on her own, unsolicited)
# Shadowheart_Usolicited_Kiss_1
Shadowheart_Usolicited_Kiss_1 = bg3.flag_object(
    files, 'Shadowheart_Usolicited_Kiss_1', bg3.OBJECT_FLAG, flag_uuid='0f81b8e1-8553-45ba-95a6-d4c113798df8', description='Unsolicited kiss 1')

# Shadowheart_Usolicited_Kiss_2
Shadowheart_Usolicited_Kiss_2 = bg3.flag_object(
    files, 'Shadowheart_Usolicited_Kiss_2', bg3.OBJECT_FLAG, flag_uuid='bc7b6b94-f686-4f85-beb8-b248bc5b98f4', description='Unsolicited kiss 2')

# Shadowheart_Usolicited_Kiss_3
Shadowheart_Usolicited_Kiss_3 = bg3.flag_object(
    files, 'Shadowheart_Usolicited_Kiss_3', bg3.OBJECT_FLAG, flag_uuid='8c6a2843-23aa-4ec8-852a-849199f96bb1', description='Unsolicited kiss 3')

# Shadowheart_Daytime_Kiss_1
Shadowheart_Daytime_Kiss_1 = bg3.flag_object(
    files, 'Shadowheart_Daytime_Kiss_1', bg3.OBJECT_FLAG, flag_uuid='a8602f0b-a938-43da-84f5-57e31279d3a7', description='Shadowheart wants Tav to kiss her 1')

# Shadowheart_Daytime_Kiss_2
Shadowheart_Daytime_Kiss_2 = bg3.flag_object(
    files, 'Shadowheart_Daytime_Kiss_2', bg3.OBJECT_FLAG, flag_uuid='22724bd2-4601-41d7-8237-e0c309e36a72', description='Shadowheart wants Tav to kiss her 2')

# Shadowheart_Daytime_Kiss_3
Shadowheart_Daytime_Kiss_3 = bg3.flag_object(
    files, 'Shadowheart_Daytime_Kiss_3', bg3.OBJECT_FLAG, flag_uuid='9fc10afa-147c-4f8e-b5a4-f20bcbaa6360', description='Shadowheart wants Tav to kiss her 3')

# Shadowheart_Morning_Kiss
Shadowheart_Morning_Kiss = bg3.flag_object(
    files, 'Shadowheart_Morning_Kiss', bg3.OBJECT_FLAG, flag_uuid='634e69d9-7ae4-4b62-8f5b-fe3c5b6690e6', description='Shadowheart wants Tav to kiss her in the morning')

# Shadowheart_Kissed_Tav_Ever
Shadowheart_Kissed_Tav_Ever = bg3.flag_object(
    files, 'Shadowheart_Kissed_Tav_Ever', bg3.OBJECT_FLAG, flag_uuid='8ac70345-8c6e-4525-90ba-b143eeea39fb', description='Shadowheart kissed Tav, first ever flag')

# Shadowheart_Kissed_Tav_Once
Shadowheart_Kissed_Tav_Once = bg3.flag_object(
    files, 'Shadowheart_Kissed_Tav_Once', bg3.OBJECT_FLAG, flag_uuid='a77caba6-5a89-441e-bab5-2ac3aff2ac86', description='Shadowheart kissed Tav once')

# Shadowheart_Kissed_Tav_Twice
Shadowheart_Kissed_Tav_Twice = bg3.flag_object(
    files, 'Shadowheart_Kissed_Tav_Twice', bg3.OBJECT_FLAG, flag_uuid='fdd41a4f-b4d1-4ce7-a7ab-0a916dc88f4c', description='Shadowheart kissed Tav twice')

# Shadowheart_Kissed_Tav_Thrice
Shadowheart_Kissed_Tav_Thrice = bg3.flag_object(
    files, 'Shadowheart_Kissed_Tav_Thrice', bg3.OBJECT_FLAG, flag_uuid='a30feef0-52d1-46dc-82b7-c7760e61b2f5', description='Shadowheart kissed Tav thrice')

# Shadowheart_PDA_Trigger
Shadowheart_PDA_Trigger = bg3.flag_object(
    files, 'Shadowheart_PDA_Trigger', bg3.OBJECT_FLAG, flag_uuid='2f92ab41-97e7-4603-8982-880f1f457687', description='Shadowheart PDA trigger')

# Shadowheart_Morning_PDA_Trigger
Shadowheart_Morning_PDA_Trigger = bg3.flag_object(
    files, 'Shadowheart_Morning_PDA_Trigger', bg3.OBJECT_FLAG, flag_uuid='f980f170-f38d-4cbc-bf95-4794a5b7673f', description='Shadowheart morning PDA trigger')

Shadowheart_Stop_PDA_Trigger = bg3.flag_object(
    files, 'Shadowheart_Stop_PDA_Trigger', bg3.OBJECT_FLAG, flag_uuid='67edac2b-7bdf-4ace-a7fe-94854825e2df', description='Prevents further Shadowheart PDAs')

# DJ_Shadowheart_Kissed_Tav
DJ_Shadowheart_Kissed_Tav = bg3.flag_object(
    files, 'DJ_Shadowheart_Kissed_Tav', bg3.OBJECT_FLAG, flag_uuid='a7fe7750-7d7c-480f-b3c4-de0bd569e609', description='DJ Shadowheart kissed Tav')

# Under construction flag
Under_Construction = bg3.flag_object(
    files, 'Under_Construction', bg3.OBJECT_FLAG, flag_uuid='63ffe70f-4ad7-498c-966e-a47106e3b23d', description='Set to true to show unfinished content')

# Tav_Gave_A_Book_To_Shadowheart
#Tav_Gave_A_Book_To_Shadowheart = bg3.flag_object(
#    files, 'Tav_Gave_A_Book_To_Shadowheart', bg3.OBJECT_FLAG, flag_uuid='f1817473-a882-4a26-a46a-708e02203a45', description='Tav gave a book to Shadowheart')

# Tav_Has_Selune_Book_For_Shadowheart
Tav_Has_Selune_Book_For_Shadowheart = bg3.flag_object(
    files, 'Tav_Has_Selune_Book_For_Shadowheart', bg3.OBJECT_FLAG, flag_uuid='54d663c5-17a9-46df-b959-2818ae4208ca', description='Tav has the Selunite Prayer Book for Shadowheart')

# Tav_Gave_Selune_Book_To_Shadowheart
Tav_Gave_Selune_Book_To_Shadowheart = bg3.flag_object(
    files, 'Tav_Gave_Selune_Book_To_Shadowheart', bg3.OBJECT_FLAG, flag_uuid='0fafd10c-3b75-4c35-a01c-ced1f7f25a2f', description='Tav gave the Selunite Prayer Book to Shadowheart')

# Tav_Has_Unclaimed_Book_For_Shadowheart
Tav_Has_Unclaimed_Book_For_Shadowheart = bg3.flag_object(
    files, 'Tav_Has_Unclaimed_Book_For_Shadowheart', bg3.OBJECT_FLAG, flag_uuid='cd740fb0-f237-4d4f-be72-713446dce67d', description='Tav has The Unclaimed book for Shadowheart')

# Tav_Gave_Unclaimed_Book_To_Shadowheart
Tav_Gave_Unclaimed_Book_To_Shadowheart = bg3.flag_object(
    files, 'Tav_Gave_Unclaimed_Book_To_Shadowheart', bg3.OBJECT_FLAG, flag_uuid='f70686e7-31ba-4ba7-93d3-13053e3a7da8', description='Tav gave The Unclaimed book to Shadowheart')

# Tav_Has_DJ_Book_For_Shadowheart
Tav_Has_DJ_Book_For_Shadowheart = bg3.flag_object(
    files, 'Tav_Has_DJ_Book_For_Shadowheart', bg3.OBJECT_FLAG, flag_uuid='4e6c3976-e792-4805-9a20-750a50654734', description='Tav has the DJ Plea book for Shadowheart')

# Tav_Gave_DJ_Book_To_Shadowheart
Tav_Gave_DJ_Book_To_Shadowheart = bg3.flag_object(
    files, 'Tav_Gave_DJ_Book_To_Shadowheart', bg3.OBJECT_FLAG, flag_uuid='4399a01b-e876-4126-877c-429156b49338', description='Tav gave the DJ Plea book to Shadowheart')

# Shadowheart_Shadow_Cursed
Shadowheart_Shadow_Cursed = bg3.flag_object(
    files, 'Shadowheart_Shadow_Cursed', bg3.OBJECT_FLAG, flag_uuid='a2a44d74-eb8d-4d22-bc14-ddf9d482aed9', description='Shar didnt protect Shadowheart from the Shadow Curse')

# Shadowheart_Shadow_Cursed_Event
Shadowheart_Shadow_Cursed_Event = bg3.flag_object(
    files, 'Shadowheart_Shadow_Cursed_Event', bg3.OBJECT_FLAG, flag_uuid='e1f3e587-9872-4735-9169-c5df785a634d', description='Trigger flag for the new faith discussion')


# Shadowheart needs a night to get her thoughts together
Shadowheart_After_Parents_Crisis = bg3.flag_object(
    files, 'Shadowheart_After_Parents_Crisis', bg3.OBJECT_FLAG, flag_uuid='6f8e2b2b-5ffa-4e83-adf7-d80a8e36a8d8', description='Shadowheart needs a night to get her thoughts together')

# Shadowheart cried and got her thoughts together
Shadowheart_Cried_After_Parents = bg3.flag_object(
    files, 'Shadowheart_Cried_After_Parents', bg3.OBJECT_FLAG, flag_uuid='4777f4c8-d5ee-4d4e-83cc-243b3c837fa8', description='Shadowheart cried and got her thoughts together')

# Loot_Viconias_Stuff flag
Loot_Viconias_Stuff = bg3.flag_object(
    files, 'Loot_Viconias_Stuff', bg3.OBJECT_FLAG, flag_uuid='550ff254-7218-4e11-9699-17d837da43f8', description="Loot Viconia's stuff")

# Shadowheart_State_Smiles_When_Hugged
Shadowheart_State_Smiles_When_Hugged = bg3.flag_object(
    files, 'Shadowheart_State_Smiles_When_Hugged', bg3.OBJECT_FLAG, flag_uuid='3486a7e3-97c8-464b-9afa-665e8ec981ff', description='Shadowheart is hugged and she smiles')

# Shadowheart_State_Hugs_Enabled flag
Shadowheart_State_Hugs_Enabled = bg3.flag_object(
    files, 'Shadowheart_State_Hugs_Enabled', bg3.OBJECT_FLAG, flag_uuid='9402335a-e23e-464b-9c18-fb5fed9eff04', description='Shadowheart was hugged, she liked that and wants more hugs')

# Shadowheart_State_Hug_Reaction
Shadowheart_State_Hug_Reaction = bg3.flag_object(
    files, 'Shadowheart_State_Hug_Reaction', bg3.OBJECT_FLAG, flag_uuid='b55cf115-9659-4b46-9150-ae4a261ea0af', description='Shadowheart reacts to the first hug when she is not sad')

# Snuck_Away_To_Make_Sandcastles flag
Snuck_Away_To_Make_Sandcastles = bg3.flag_object(
    files, 'Snuck_Away_To_Make_Sandcastles', bg3.OBJECT_FLAG, flag_uuid='05c019dd-72c5-4ae0-85fa-71b79bf0bb4e', description='Tav said others will think they snuck away to make sandcastles')

# Shadowheart_More_Sandcastles flag
Shadowheart_More_Sandcastles = bg3.flag_object(
    files, 'Shadowheart_More_Sandcastles', bg3.OBJECT_FLAG, flag_uuid='2f2779cf-4a7b-44ef-8458-d29b48578740', description='Shadowheart hopes for more opportunities to slip away')

# Tav_Shadowheart_Made_Sandcastles_Two_Times flag
Tav_Shadowheart_Made_Sandcastles_Two_Times = bg3.flag_object(
    files, 'Tav_Shadowheart_Made_Sandcastles_Two_Times', bg3.OBJECT_FLAG, flag_uuid='6ca011be-afd0-4f09-b9c4-02bfd68b7b07', description='Tav and Shadowheart made sandcastles 2 or more times')

# Tav_Shadowheart_Made_Sandcastles_Three_Times flag
Tav_Shadowheart_Made_Sandcastles_Three_Times = bg3.flag_object(
    files, 'Tav_Shadowheart_Made_Sandcastles_Three_Times', bg3.OBJECT_FLAG, flag_uuid='bdd37b60-15a2-4d2d-90c7-a611028a0fac', description='Tav and Shadowheart made sandcastles 3 or more times')

# Tav_Shadowheart_Made_Sandcastles_Four_Times flag
Tav_Shadowheart_Made_Sandcastles_Four_Times = bg3.flag_object(
    files, 'Tav_Shadowheart_Made_Sandcastles_Four_Times', bg3.OBJECT_FLAG, flag_uuid='20aff345-750b-4516-a2d7-4013feb0ca35', description='Tav and Shadowheart made sandcastles 4 or more times')

# Shadowheart_LongRest_Before_More_Sandcastles flag
Shadowheart_LongRest_Before_More_Sandcastles = bg3.flag_object(
    files, 'Shadowheart_LongRest_Before_More_Sandcastles', bg3.OBJECT_FLAG, flag_uuid='fec1c849-c9b6-47ab-9dd4-84acff4cd01a', description='Wait 1 long rest before asking Shadowheart to slip away again')

# Shadowheart_More_Sandcastles_Replied flag
Shadowheart_More_Sandcastles_Replied = bg3.flag_object(
    files, 'Shadowheart_More_Sandcastles_Replied', bg3.OBJECT_FLAG, flag_uuid='8942cfa4-550f-482b-8b27-56625dee1c15', description='Shadowheart replied to a proposal of seizing an opportunity')

# Shadowheart_More_Sandcastles_Tonight flag
Shadowheart_More_Sandcastles_Tonight = bg3.flag_object(
    files, 'Shadowheart_More_Sandcastles_Tonight', bg3.OBJECT_FLAG, flag_uuid='46190b70-0be5-4f11-834c-59b278211de2', description='Triggers the skinny dipping cutscene one more time')

# Shadowheart_Tav_State_Married flag
Shadowheart_Tav_State_Married = bg3.flag_object(
    files, 'Shadowheart_Tav_State_Married', bg3.GLOBAL_FLAG, flag_uuid='9d34a5e6-8e66-42d6-affa-85ff0c2780b4', description='Tav and Shadowheart are married')

# Shadowheart_State_DontHireDapperDrowPromise flag
Shadowheart_State_DontHireDapperDrowPromise = bg3.flag_object(
    files, 'Shadowheart_State_DontHireDapperDrowPromise', bg3.OBJECT_FLAG, flag_uuid='6b71d4ba-373d-4332-bd8b-84faeee3d768', description='This character promised their romantic partner to not hire drow twins')

# Shadowheart_State_RejectedDapperDrow flag
Shadowheart_State_RejectedDapperDrow = bg3.flag_object(
    files, 'Shadowheart_State_RejectedDapperDrow', bg3.OBJECT_FLAG, flag_uuid='0ff9ee19-b9ca-40e1-b67f-f5f172fb83f9', description='This character made their mind to not hire drow twins')

# Shadowheart_State_RejectedDapperDrow3some flag
Shadowheart_State_RejectedDapperDrow3some = bg3.flag_object(
    files, 'Shadowheart_State_RejectedDapperDrow3some', bg3.OBJECT_FLAG, flag_uuid='e9d590df-3c6e-48c5-b19e-7ad3899b4eab', description='This character and their partner made their minds to not hire drow twins')

# Act3_Acolyte_StickToYourMorals inspiration point flag
Acolyte_StickToYourMorals = bg3.flag_object(
    files, 'Acolyte_StickToYourMorals', bg3.GLOBAL_FLAG, flag_uuid = 'f54ead6e-929c-4ad9-86a4-acf352c3eee8', description = 'Acolyte rejected prostitutes in Sharess Caress')

# Act3_Urchin_WhenLessIsMore inspiration point flag
Urchin_WhenLessIsMore = bg3.flag_object(
    files, 'Urchin_WhenLessIsMore', bg3.GLOBAL_FLAG, flag_uuid = 'ab9fa289-dae9-486c-8cd8-35953da26834', description = 'Urchin rejected Mizora and prostitutes in Sharess Caress')

# Shadowheart_Approval_Set_To_35 flag
Shadowheart_Approval_Set_To_35 = bg3.flag_object(
    files, 'Shadowheart_Approval_Set_To_35', bg3.OBJECT_FLAG, flag_uuid='a562c158-cb0c-40a9-9f34-44f76bfdfbf6', description="Reduce Shadowheart's approval of Tav to 35")

# Shadowheart_Approval_Set_To_Zero flag
Shadowheart_Approval_Set_To_Zero = bg3.flag_object(
    files, 'Shadowheart_Approval_Set_To_Zero', bg3.OBJECT_FLAG, flag_uuid='add81fd0-0641-45d3-8020-29098ccc22d7', description="Reduce Shadowheart's approval of Tav to naught")

# Shadowheart_Approval_Set_To_Neutral flag
Shadowheart_Approval_Set_To_Neutral = bg3.flag_object(
    files, 'Shadowheart_Approval_Set_To_Neutral', bg3.OBJECT_FLAG, flag_uuid='42a1da52-ccf5-46a0-954d-8f1c53dd20b6', description="Reduce Shadowheart's approval of Tav to the 'neutral' level")

# Shadowheart_Approval_Set_To_Low flag
Shadowheart_Approval_Set_To_Low = bg3.flag_object(
    files, 'Shadowheart_Approval_Set_To_Low', bg3.OBJECT_FLAG, flag_uuid='2701e07a-73a2-4b96-9951-9080555f3f8f', description="Reduce Shadowheart's approval of Tav to the 'low' level")

# Shadowheart_Approval_Set_To_VeryLow flag
Shadowheart_Approval_Set_To_VeryLow = bg3.flag_object(
    files, 'Shadowheart_Approval_Set_To_VeryLow', bg3.OBJECT_FLAG, flag_uuid='c80bad74-7669-4989-a912-106fd2ed4cd9', description="Reduce Shadowheart's approval of Tav to the 'very low' level")

# Shadowheart_BreakUp_Notification_Start flag
Shadowheart_BreakUp_Notification_Start = bg3.flag_object(
    files, 'Shadowheart_BreakUp_Notification_Start', bg3.OBJECT_FLAG, flag_uuid='d20cc281-6ed6-4e9b-bad5-28d403a2b0af', description='Tav did something stupid and Shadowheart broke up with them')

# Shadowheart_BreakUp_Notification_Finish flag
Shadowheart_BreakUp_Notification_Finish = bg3.flag_object(
    files, 'Shadowheart_BreakUp_Notification_Finish', bg3.OBJECT_FLAG, flag_uuid='80a1a14e-f831-4b3f-815a-684dc15f77e7', description='Shadowheart told Tav she has broken up with them')

# Tav_Regrets_Mizora_Romance flag
Tav_Regrets_Mizora_Romance = bg3.flag_object(
    files, 'Tav_Regrets_Mizora_Romance', bg3.OBJECT_FLAG, flag_uuid='54b85a7f-cc01-4391-8948-b637e9688aa5', description='Tav told Mizora they regret every moment they spent with her in the hells')

# Tav_Shadowheart_Marriage_Mentioned flag
Tav_Shadowheart_Marriage_Mentioned = bg3.flag_object(
    files, 'Tav_Shadowheart_Marriage_Mentioned', bg3.LOCAL_FLAG, flag_uuid='dfed76e7-7716-47c4-abc3-3217493fec66', description="Shadowheart told Tav she's still getting used to being married")

# Tav_Shadowheart_Marriage_Mentioned flag
Tav_Shadowheart_Grandchildren_Mentioned = bg3.flag_object(
    files, 'Tav_Shadowheart_Grandchildren_Mentioned', bg3.LOCAL_FLAG, flag_uuid='89a8ddee-6dce-46a0-9ca4-7a67feca6735', description="Shadowheart told Tav she's expecting")

# Tav_Shadowheart_Epilogue_Convesation_Happened flag
Tav_Shadowheart_Epilogue_Convesation_Happened = bg3.flag_object(
    files, 'Tav_Shadowheart_Epilogue_Convesation_Happened', bg3.LOCAL_FLAG, flag_uuid='4bb8d67c-e81c-47fa-b911-5ec8f191650e', description="Tav spoke to Shadowheart at the Epilogue party")

# Parents_Change_Clothes flag
Parents_Change_Clothes = bg3.flag_object(
    files, 'Parents_Change_Clothes', bg3.GLOBAL_FLAG, flag_uuid = '2ebf489a-9d98-49c8-9db1-c337ba853c90', description = 'Parents are going to change their clothes')

# Parents_New_Clothes flag
Parents_New_Clothes = bg3.flag_object(
    files, 'Parents_New_Clothes', bg3.GLOBAL_FLAG, flag_uuid = '27f1a908-8088-4b49-ad51-9178d3e88e33', description = 'Parents changed their clothes')

# Betrayed_Shadowheart flag
Betrayed_Shadowheart = bg3.flag_object(
    files, 'Betrayed_Shadowheart', bg3.OBJECT_FLAG, flag_uuid='414f6e7d-4a86-4cdf-b5aa-31d053ae76d9', description="Tav betrayed Shadowheart.")

# Companion_Permanently_Leaves_Party flag
Companion_Permanently_Leaves_Party = bg3.flag_object(
    files, 'Companion_Permanently_Leaves_Party', bg3.OBJECT_FLAG, flag_uuid='76339e33-bb45-4f1b-9d43-58773590175c', description="Companion permanently leaves the party.")

# Companion_Attacks_Player flag
Companion_Turns_Hostile = bg3.flag_object(
    files, 'Companion_Attacks_Player', bg3.OBJECT_FLAG, flag_uuid='b437177d-ac5d-4c44-a927-9a54b7f72bd2', description="Tav did something awful. Good-aligned companion attacks.")

# Post_Betrayal_InParty_Fight flag
Post_Betrayal_InParty_Fight = bg3.flag_object(
    files, 'Post_Betrayal_InParty_Fight', bg3.OBJECT_FLAG, flag_uuid='b482fd66-55ef-42e3-9922-347ed847c39d', description="A fight erupted in party because Shadowheart was betrayed.")

# Creep harassed Shadowheart
Creep_Harassed_Shadowheart = bg3.flag_object(
    files, 'Creep_Harassed_Shadowheart', bg3.OBJECT_FLAG, flag_uuid='76ff22b1-916b-42db-b73e-bb6a8c7b1893', description="The creep harassed Shadowheart and Tav with his kelpie nonsense.")

# Creep ran away
Creep_Ran_Away = bg3.flag_object(
    files, 'Creep_Ran_Away', bg3.OBJECT_FLAG, flag_uuid='0a3b99e8-d8a6-4a7f-a56c-7f9092f522b5', description="The creep ran away after Tav kicked him in the balls.")

# Shadowheart refused to take the astral touched tadpole
Shadowheart_Refused_Half_Illithid = bg3.flag_object(
    files, 'Shadowheart_Refused_Half_Illithid', bg3.OBJECT_FLAG, flag_uuid='ce729c43-09b1-4ff9-9bf2-05cf4930b03a', description="Shadowheart refused to take the astral touched tadpole.")

# Tav agreed to stop asking Shadowheart about the tadpole
Tav_Stopped_Asking_Half_Illithid = bg3.flag_object(
    files, 'Tav_Stopped_Asking_Half_Illithid', bg3.OBJECT_FLAG, flag_uuid='281caf27-9c84-409d-8615-6a830d0052db', description="Shadowheart refused to take the astral touched tadpole, and Tav won't ask again.")

# Tav_Played_With_Incubus
Tav_Played_With_Incubus = bg3.flag_object(
    files, 'Tav_Played_With_Incubus', bg3.OBJECT_FLAG, flag_uuid='d0fad05d-8fd2-4249-99c4-535f796788a6', description="Tav agreed and played with Haarlep.")

# Shadowheart_Saw_Tav_Played_With_Incubus
Shadowheart_Saw_Tav_Played_With_Incubus = bg3.flag_object(
    files, 'Shadowheart_Saw_Tav_Played_With_Incubus', bg3.OBJECT_FLAG, flag_uuid='bdbbf476-8d0a-4c50-b43c-23e20995a9fb', description="Shadowheart saw Tav had agreed and played with Haarlep.")

# Found_Memorable_Locations flag
#Found_Memorable_Locations = bg3.flag_object(
#    files, 'Found_Memorable_Locations', bg3.OBJECT_FLAG, flag_uuid='ac830dd2-bad2-44aa-9970-136c16477500', description="This character found 2 or more of Shadowheart's memorable locations in Baldur's Gate.")

# Tav_Mocked_Sharran_Prayer
Tav_Mocked_Sharran_Prayer = bg3.flag_object(
    files, 'Tav_Mocked_Sharran_Prayer', bg3.OBJECT_FLAG, flag_uuid='fa8d440f-1f40-4efe-b34c-a2a164e504de', description="Tav mocked her prayer. Bastard.")

# Tav_Prayed_With_Her
Tav_Prayed_With_Her = bg3.flag_object(
    files, 'Tav_Prayed_With_Her', bg3.OBJECT_FLAG, flag_uuid='e057c715-9a00-4bdd-b4dc-f60a20fa6d03', description="Tav prayed with Shadowheart to protect her from the shadows.")

# Tav_Already_Prayed_With_Her_Today
Tav_Already_Prayed_With_Her_Today = bg3.flag_object(
    files, 'Tav_Already_Prayed_With_Her_Today', bg3.OBJECT_FLAG, flag_uuid='a2a96abb-1b40-42fe-9f8b-6685eb173c63', description="This flag prevents too many prayers. Only one per long rest.")

# Tav_Prayer_Event
Tav_Prayer_Event = bg3.flag_object(
    files, 'Tav_Prayer_Event', bg3.OBJECT_FLAG, flag_uuid='5dd7a483-0578-40bc-b172-a7aaccf32f80', description="Event: Tav wants to pray with Shadowheart.")

# Halsin_Knocked_Out
Halsin_Knocked_Out = bg3.flag_object(
    files, 'Halsin_Knocked_Out', bg3.OBJECT_FLAG, flag_uuid='721f7a51-c724-4a5b-86db-58940d525601', description="Tav KOed the creep.")

# Halsins_Ass_Kicked
Halsins_Ass_Kicked = bg3.flag_object(
    files, 'Halsins_Ass_Kicked', bg3.OBJECT_FLAG, flag_uuid='c52fbf93-d839-4660-92f7-205c7d7004fa', description="Tav kicked druids ass.")

# Halsins_Leaves_Party
Halsins_Leaves_Party = bg3.flag_object(
    files, 'Halsins_Leaves_Party', bg3.OBJECT_FLAG, flag_uuid='9bd0296a-ae15-404e-913c-fc267455d3d9', description="Tav kicked druids ass and he leaves the party.")

# Halsin_Rejected
Halsin_Rejected = bg3.flag_object(
    files, 'Halsin_Rejected', bg3.OBJECT_FLAG, flag_uuid='e55da39e-ca64-465b-9d03-bc5fce366e6a', description="Set on Tav when they reject the creep.")

# Shadowheart_Has_Doubts_About_Tav flag
# d6fef6ce-129e-4edf-8f00-00e0ecb08052
# bff7d8ea-6bfd-4ce7-a2c3-5e775004938d
# 01944863-f589-41a5-9cd7-84d2bebc17ae
Shadowheart_Has_Doubts_About_Tav = bg3.flag_object(
    files, 'Shadowheart_Has_Doubts_About_Tav', bg3.OBJECT_FLAG, flag_uuid='2774e4ec-e92d-41c1-a4b0-c6ddc84417da', description="Tav did something that made Shadowheart question if they are a good match.")

# Shadowheart_Lost_Faith_In_Tav
Shadowheart_Lost_Faith_In_Tav = bg3.flag_object(
    files, 'Shadowheart_Lost_Faith_In_Tav', bg3.OBJECT_FLAG, flag_uuid='bff18cc2-e633-40c9-baa4-34868cb8b0f9', description="Shadowheart lost faith in Tav.")

# Shadowheart_Rejects_Proposal
Shadowheart_Rejects_Proposal = bg3.flag_object(
    files, 'Shadowheart_Rejects_Proposal', bg3.OBJECT_FLAG, flag_uuid='c8f7b189-ea19-4a74-b581-305abdc9eb19', description="Shadowheart will reject marriage proposal.")

# Cheated_On_Shadowheart flag
Cheated_On_Shadowheart = bg3.flag_object(
    files, 'Cheated_On_Shadowheart', bg3.OBJECT_FLAG, flag_uuid='94181834-3277-492b-b223-11309c7bd90c', description="Tav cheated on Shadowheart with dapper drows.")

# Shadowheart_Reacted_To_Cheating flag
Shadowheart_Reacted_To_Cheating = bg3.flag_object(
    files, 'Shadowheart_Reacted_To_Cheating', bg3.OBJECT_FLAG, flag_uuid='3b5b8a8a-3b0e-485c-970d-f0467de463c9', description="Shadowheart noticed that Tav's behavior changed.")

Nightfall_Cant_Happen_Again = bg3.flag_object(
    files, 'Nightfall_Cant_Happen_Again', bg3.OBJECT_FLAG, flag_uuid='d63d0f54-f257-4a81-a4ab-f7c04efb4f76', description="Set on Tav when they say NF cannot happen again.")

# Shadowheart_Hesitated_To_Ask
Shadowheart_Hesitated_To_Ask = bg3.flag_object(
    files, 'Shadowheart_Hesitated_To_Ask', bg3.OBJECT_FLAG, flag_uuid='d8d602d9-d2ab-4a8e-8ffb-c465fd52ce18', description="Shadowheart hesitated to ask about sleeping in one bedroll with Tav")

# Tav_Noticed_Shadowheart_Hesitated_To_Ask
Tav_Noticed_Shadowheart_Hesitated_To_Ask = bg3.flag_object(
    files, 'Tav_Noticed_Shadowheart_Hesitated_To_Ask', bg3.OBJECT_FLAG, flag_uuid='7b7c0c83-d397-42c5-b0bd-847b1f28cce1', description="Tav noticed that something's bothering Shadowheart")

# Shadowheart_Tav_Sleep_Together
Shadowheart_Tav_Sleep_Together = bg3.flag_object(
    files, 'Shadowheart_Tav_Sleep_Together', bg3.OBJECT_FLAG, flag_uuid='0187f803-6b3c-4249-b5a8-0e968306978b', description="Shadowheart sleeps with Tav at night")

# Shadowheart_Tav_Slept_Together
Shadowheart_Tav_Slept_Together = bg3.flag_object(
    files, 'Shadowheart_Tav_Slept_Together', bg3.OBJECT_FLAG, flag_uuid='09caaa22-7045-4764-970b-f5f90fb32386', description="Shadowheart slept with Tav at night")

# Alternative_Night_Sleep_Scene
Alternative_Night_Sleep_Scene = bg3.flag_object(
    files, 'Alternative_Night_Sleep_Scene', bg3.OBJECT_FLAG, flag_uuid='e45c72b0-3f0a-45e0-adae-956b271eefd0', description="Alternative night sleep scene")

# Tav_Love_Confession
Tav_Love_Confession = bg3.flag_object(
    files, 'Tav_Love_Confession', bg3.GLOBAL_FLAG, flag_uuid='a2f0421c-74dd-4b91-ba6f-bc6c55629518', description="Tav made a love confession to Shadowheart")

# Cuddles_Love_You
Cuddles_Love_You = bg3.flag_object(
    files, 'Cuddles_Love_You', bg3.GLOBAL_FLAG, flag_uuid='89be9f46-7a1a-436b-9a79-9b00f347b545', description="Tav said I love you to Shadowheart after night time cuddles")

# Tav_Said_Love_You
Tav_Said_Love_You = bg3.flag_object(
    files, 'Tav_Said_Love_You', bg3.GLOBAL_FLAG, flag_uuid='ea47a913-77a8-4a7e-bdfb-a13880f25107', description="Tav said I love you to Shadowheart")

# Skinny_Dipping_Recurrent_Conversation
Skinny_Dipping_Recurrent_Conversation = bg3.flag_object(
    files, 'Skinny_Dipping_Recurrent_Conversation', bg3.GLOBAL_FLAG, flag_uuid='d5fed96f-42f1-4d0c-9fdb-e40a0db7b8ae', description="Trigger recurrent conversation about SD")

# Parents_Long_Rested
Parents_Long_Rested = bg3.flag_object(
    files, 'Parents_Long_Rested', bg3.GLOBAL_FLAG, flag_uuid='0960e0d7-c080-4c22-aa26-8bbe551a7044', description="Arnell and Emmeline Hallowleaf long rested after the Daughters Tears")

###############################################################
# EA cut content: reflections to world events
###############################################################

# Old flag, do not use it
ReallyShadowheart_Ext_GutHunter_V1 = bg3.flag_object(
    files, 'ReallyShadowheart_Ext_GutHunter_V1', bg3.GLOBAL_FLAG, flag_uuid='2319a650-7273-43a6-86a4-a4d9823f8cbd', description="Gur hunter V1 EA content is available")

# If this flag is set, extension is present
ReallyShadowheart_Ext_V2_0_0_0 = bg3.flag_object(
    files, 'ReallyShadowheart_Ext_V2_0_0_0', bg3.GLOBAL_FLAG, flag_uuid='d526de63-740b-4b22-a7a9-aea7dad2e6e5', description="EA content extension version 2.0.0.0 is available")

# Reflection_Event_Gur_Hunter flag
Reflection_Event_Gur_Hunter = bg3.flag_object(
    files, 'Reflection_Event_Gur_Hunter', bg3.OBJECT_FLAG, flag_uuid='45879bf0-a54b-420e-a18a-6c0547592bab', description='Triggers Shadowhearts reflection about encounter with Gandrel')

# Reflection_Available_Gur_Hunter flag
Reflection_Available_Gur_Hunter = bg3.flag_object(
    files, 'Reflection_Available_Gur_Hunter', bg3.OBJECT_FLAG, flag_uuid='498a65f0-c7b8-4a12-82c2-c73e5aac0685', description='Reflection about encounter with Gandrel is available')

# Tav_Protected_Astarion flag
Tav_Protected_Astarion = bg3.flag_object(
    files, 'Tav_Protected_Astarion', bg3.OBJECT_FLAG, flag_uuid='ea2d64c0-1043-487b-8656-4813b3c590df', description='Tav protected Astarion from Gandrel')

# Tav_Betrayed_Astarion flag
Tav_Betrayed_Astarion = bg3.flag_object(
    files, 'Tav_Betrayed_Astarion', bg3.OBJECT_FLAG, flag_uuid='e688d213-2d07-4f29-af3a-24ff4f2ae6fa', description='Tav betrayed Astarion and surrendered him to Gandrel')

# Reflection_Event_Sazza flag
Reflection_Event_Sazza = bg3.flag_object(
    files, 'Reflection_Event_Sazza', bg3.OBJECT_FLAG, flag_uuid='e9fa6284-c467-4c2b-aafc-2125137bde02', description='Triggers Shadowhearts reflection about Sazza')

# Reflection_Available_Sazza flag
Reflection_Available_Sazza = bg3.flag_object(
    files, 'Reflection_Available_Sazza', bg3.OBJECT_FLAG, flag_uuid='26bf52e9-5d36-4072-95ed-a81541fd610b', description='Reflection about Sazza is available')

# Tav_Promised_Help_Sazza flag
Tav_Promised_Help_Sazza = bg3.flag_object(
    files, 'Tav_Promised_Help_Sazza', bg3.OBJECT_FLAG, flag_uuid='77a94bab-1497-4ab2-aa00-d97cbbd21e37', description='Tav promised to help Sazza')

# Reflection_Event_Nettie flag
Reflection_Event_Nettie = bg3.flag_object(
    files, 'Reflection_Event_Nettie', bg3.OBJECT_FLAG, flag_uuid='620ada9c-6129-4db5-be05-6238b7395b0f', description='Triggers Shadowhearts reflection about Nettie')

# Reflection_Available_Nettie flag
Reflection_Available_Nettie = bg3.flag_object(
    files, 'Reflection_Available_Nettie', bg3.OBJECT_FLAG, flag_uuid='7d55e2df-5890-4797-ac53-1020ab4a8fd7', description='Reflection about Nettie is available')

# Reflection_Event_Arabella_Death flag
Reflection_Event_Arabella_Death = bg3.flag_object(
    files, 'Reflection_Event_Arabella_Death', bg3.OBJECT_FLAG, flag_uuid='8e722f82-33b0-4357-b5a4-5cbff2187cb4', description='Triggers Shadowhearts reflection about death of Arabella')

# Reflection_Available_Arabella_Death flag
Reflection_Available_Arabella_Death = bg3.flag_object(
    files, 'Reflection_Available_Arabella_Death', bg3.OBJECT_FLAG, flag_uuid='5b461379-afe7-440a-995a-69ad986cbf05', description='Triggers Shadowhearts reflection about death of Arabella')

# Reflection_Event_Tadpole flag
Reflection_Event_Tadpole = bg3.flag_object(
    files, 'Reflection_Event_Tadpole', bg3.OBJECT_FLAG, flag_uuid='ed67655f-a749-454a-a137-f8b17a55ac84', description='Triggers Shadowhearts reflection about Edowins tadpole')

# Reflection_Available_Tadpole flag
Reflection_Available_Tadpole = bg3.flag_object(
    files, 'Reflection_Available_Tadpole', bg3.OBJECT_FLAG, flag_uuid='ab420719-5f04-4f47-99b6-484726758c75', description='Reflection about Edowins tadpole is available')

# Reflection_Event_Bugbear_Love flag
Reflection_Event_Bugbear_Love = bg3.flag_object(
    files, 'Reflection_Event_Bugbear_Love', bg3.OBJECT_FLAG, flag_uuid='ef654fd3-2fc3-49d7-afe1-5051b1372861', description='Triggers Shadowhearts reflection about that couple in the barn')

# Reflection_Available_Bugbear_Love flag
Reflection_Available_Bugbear_Love = bg3.flag_object(
    files, 'Reflection_Available_Bugbear_Love', bg3.OBJECT_FLAG, flag_uuid='8508e380-ab05-4436-92ac-5d6ff5f04d06', description='Reflection about that couple in the barn is available')

# Reflection_Event_Goblin_Camp flag
Reflection_Event_Goblin_Camp = bg3.flag_object(
    files, 'Reflection_Event_Goblin_Camp', bg3.OBJECT_FLAG, flag_uuid='c3989eff-6fef-4973-8942-f106d49c83c2', description='Triggers Shadowhearts reflection about the goblin camp')

# Reflection_Available_Goblin_Camp flag
Reflection_Available_Goblin_Camp = bg3.flag_object(
    files, 'Reflection_Available_Goblin_Camp', bg3.OBJECT_FLAG, flag_uuid='8164a020-8caa-4a70-9150-f96dbf794098', description='Reflection about the goblin camp is available')


# These two flags use different mechanism to trigger the reflection
# Reflection_Available_Gauntlet enables the Tav's question that sets the event flag
Reflection_Event_Gauntlet = bg3.flag_object(
    files, 'Reflection_Event_Gauntlet', bg3.OBJECT_FLAG, flag_uuid='423f69d5-0214-4240-941c-067d2947ff75', description='Reflection about the Gauntlet of Shar is available')

Reflection_Available_Gauntlet = bg3.flag_object(
    files, 'Reflection_Available_Gauntlet', bg3.OBJECT_FLAG, flag_uuid='7302b548-ce01-4f43-9ba9-b0cacc618db3', description='Reflection about the Gauntlet of Shar is available')

# Nightfall romance flags
Nightfall_Points_Has_Enough = bg3.flag_object(
    files, 'Nightfall_Points_Has_Enough', bg3.GLOBAL_FLAG, flag_uuid='54109051-90a1-476a-853e-fb764f8cd28a', description='Tav has enough nightfall points')
Nightfall_Point_Shar_Romance = bg3.flag_object(
    files, 'Nightfall_Point_Shar_Romance', bg3.GLOBAL_FLAG, flag_uuid='ecc36b99-b93e-4c19-a2f7-f0013ae33bfe', description='Shadowheart explained the catch of their romance')
Nightfall_Point_First_Night = bg3.flag_object(
    files, 'Nightfall_Point_First_Night', bg3.GLOBAL_FLAG, flag_uuid='46c67ea8-36f3-4ee3-b7fc-050c0844994b', description='The first night in the city')
Nightfall_Point_Second_Night = bg3.flag_object(
    files, 'Nightfall_Point_Second_Night', bg3.GLOBAL_FLAG, flag_uuid='7cc8d131-3533-4179-a65f-09d92f9d9206', description='The second night in the city')
Nightfall_Point_Ability_Check_Kiss = bg3.flag_object(
    files, 'Nightfall_Point_Ability_Check_Kiss', bg3.GLOBAL_FLAG, flag_uuid='a3f5c13a-f27a-45d4-9bee-d1830927f29e', description='Tav succeeded an ability check to convince Shadowheart to kiss them')
Nightfall_Point_Selune_Blasphemy_Kiss = bg3.flag_object(
    files, 'Nightfall_Point_Selune_Blasphemy_Kiss', bg3.GLOBAL_FLAG, flag_uuid='87dea5a3-04b9-440f-924d-c7951757805b', description='Selunite Tav promised an act of blasphemy against Selune')
Nightfall_Point_Love_You = bg3.flag_object(
    files, 'Nightfall_Point_Love_You', bg3.GLOBAL_FLAG, flag_uuid='a3268966-ed0d-43ed-8243-82cf72cdf5ad', description='Tav told that they love her when they failed an ability check')

Nightfall_Selune_Desecrated = bg3.flag_object(
    files, 'Nightfall_Selune_Desecrated', bg3.GLOBAL_FLAG, flag_uuid='7c6fdb3f-d1c2-4e94-adf7-b70018fc5722', description='Tav and DJ Shadowheart desecrated statue of Selune')

Shadowheart_Post_DJ_Romance = bg3.flag_object(
    files, 'Shadowheart_Post_DJ_Romance', bg3.OBJECT_FLAG, flag_uuid='bda7f5e9-6ea6-49ba-848a-d2f6aebdeb3e', description='Set on Tav to trigger post DJ romance conversation')

Shadowheart_Post_DJ_Now_And_Always = bg3.flag_object(
    files, 'Shadowheart_Post_DJ_Now_And_Always', bg3.GLOBAL_FLAG, flag_uuid='fd46e89e-f296-48d5-8fff-cf083b25efd0', description='Ex-DJ Shadowheart and Tav spoke after saving her parents')

###############################################################
# Use this flag to trigger the "exploring the city" cutscene
###############################################################

Tav_Flirt_Exploring_City = bg3.flag_object(
    files, 'Tav_Flirt_Exploring_City', bg3.OBJECT_FLAG, flag_uuid = 'b6c10b4f-bec2-4a28-9f1f-4bcda1d4f413', description = 'Tav said they would quite like to get lost with her exploring the city')

###############################################################
# Flags that enable aliases to recurring topics
###############################################################

Enable_Recurring_Convos = bg3.flag_object(
    files, 'Enable_Recurring_Convos', bg3.OBJECT_FLAG, flag_uuid = '3527c09b-f87b-45b1-9409-b580200e3e43', description = 'Enables recurring conversation')
Alias_Tell_Me_About_Fear = bg3.flag_object(
    files, 'Alias_Tell_Me_About_Fear', bg3.OBJECT_FLAG, flag_uuid = 'a95d68ed-7dda-4f88-b87f-72ec392b1dd8', description = 'Enables recurring conversation')
Alias_Whats_The_Story_Odd_Artifact = bg3.flag_object(
    files, 'Alias_Whats_The_Story_Odd_Artifact', bg3.OBJECT_FLAG, flag_uuid = '101981a9-174c-45ae-9941-4b74357f17e1', description = 'Enables recurring conversation')
Alias_Know_Each_Other = bg3.flag_object(
    files, 'Alias_Know_Each_Other', bg3.OBJECT_FLAG, flag_uuid = '06ba6e44-0173-42a3-a95b-5fe5c0a268a3', description = 'Enables recurring conversation')
Alias_I_Want_To_Get_To_Know_You_More = bg3.flag_object(
    files, 'Alias_I_Want_To_Get_To_Know_You_More', bg3.OBJECT_FLAG, flag_uuid = 'a1aa7dfa-ef5d-4564-9998-b68ae2c6837c', description = 'Enables recurring conversation')
Alias_You_Worship_Shar_Selune = bg3.flag_object(
    files, 'Alias_You_Worship_Shar_Selune', bg3.OBJECT_FLAG, flag_uuid = '7b1213bb-e445-4400-b9f9-54fc2cfbd62a', description = 'Enables recurring conversation')
Alias_Why_Were_You_In_Pain = bg3.flag_object(
    files, 'Alias_Why_Were_You_In_Pain', bg3.OBJECT_FLAG, flag_uuid = '94292c24-e227-4fab-851e-a182cec60695', description = 'Enables recurring conversation')
Alias_Flareups_Iam_Concerned_Low_Trust = bg3.flag_object(
    files, 'Alias_Flareups_Iam_Concerned_Low_Trust', bg3.OBJECT_FLAG, flag_uuid = '2584896c-6fed-4e6e-848d-e0972c00b452', description = 'Enables recurring conversation')
Alias_Help_Me_Understand_Wound = bg3.flag_object(
    files, 'Help_Me_Understand_Wound', bg3.OBJECT_FLAG, flag_uuid = 'ce68aebc-b27c-4e61-ba5a-24a92fa2a726', description = 'Enables recurring conversation')
Alias_Must_Be_Way_To_Heal_It = bg3.flag_object(
    files, 'Must_Be_Way_To_Heal_It', bg3.OBJECT_FLAG, flag_uuid = '383c8876-40e1-43de-8f0d-8ec44a164264', description = 'Enables recurring conversation')
Alias_Artefact_Do_You_Still_Have_It = bg3.flag_object(
    files, 'Alias_Artefact_Do_You_Still_Have_It', bg3.OBJECT_FLAG, flag_uuid = '79928573-b398-4c2f-85b6-55e84daba34f', description = 'Enables recurring conversation')
Alias_Artefact_Just_Come_To_Me = bg3.flag_object(
    files, 'Alias_Artefact_Just_Come_To_Me', bg3.OBJECT_FLAG, flag_uuid = '59c13c16-f2cd-49db-bc7c-0507a906229a', description = 'Enables recurring conversation')
Alias_You_Seemed_Intrigued_DJs = bg3.flag_object(
    files, 'Alias_You_Seemed_Intrigued_DJs', bg3.OBJECT_FLAG, flag_uuid = '876e944d-496a-4d11-a43e-751dbdade26e', description = 'Enables recurring conversation')
Alias_The_Curse_Isnt_Affecting_You = bg3.flag_object(
    files, 'The_Curse_Isnt_Affecting_You', bg3.OBJECT_FLAG, flag_uuid = '3b815d3b-08b8-4c46-8d70-24421304a292', description = 'Enables recurring conversation')
Alias_Tell_Me_More_About_Mother_Superior = bg3.flag_object(
    files, 'Tell_Me_More_About_Mother_Superior', bg3.OBJECT_FLAG, flag_uuid = '862e6b7c-1a0d-43eb-b56f-b23db6995a5e', description = 'Enables recurring conversation')
Alias_Sharrans_Might_Be_Watching = bg3.flag_object(
    files, 'Alias_Sharrans_Might_Be_Watching', bg3.OBJECT_FLAG, flag_uuid = '39c3d6a1-1da1-44f2-97f9-65995635c99b', description = 'Enables recurring conversation')
Alias_Shar_Followers_Might_Be_Watching = bg3.flag_object(
    files, 'Alias_Shar_Followers_Might_Be_Watching', bg3.OBJECT_FLAG, flag_uuid = '5ab0b8c2-7884-4f6e-a264-45b3784c5687', description = 'Enables recurring conversation')
Alias_Fellow_Sharrans_At_House_Of_Grief = bg3.flag_object(
    files, 'Alias_Fellow_Sharrans_At_House_Of_Grief', bg3.OBJECT_FLAG, flag_uuid = '3e92def6-4e0d-48e9-b6e5-207615ba8334', description = 'Enables recurring conversation')
Alias_Sharrans_Cover_At_House_Of_Grief = bg3.flag_object(
    files, 'Alias_Sharrans_Cover_At_House_Of_Grief', bg3.OBJECT_FLAG, flag_uuid = 'c1c1448a-7026-4619-a74b-1f73ba5f6728', description = 'Enables recurring conversation')

Alias_That_Grave_Did_It_Mean_Something = bg3.flag_object(
    files, 'That_Grave_Did_It_Mean_Something', bg3.OBJECT_FLAG, flag_uuid = '4a84f553-7049-47fb-a5a9-d2b29e3ad464', description = 'Enables recurring conversation')
Alias_That_Graffiti_We_Saw = bg3.flag_object(
    files, 'That_Graffiti_We_Saw', bg3.OBJECT_FLAG, flag_uuid = '62428da4-ca1d-4554-86a0-e435422ae686', description = 'Enables recurring conversation')
Alias_So_You_Had_Hideout = bg3.flag_object(
    files, 'Alias_So_You_Had_Hideout', bg3.OBJECT_FLAG, flag_uuid = 'a1743ba8-e94f-49f5-b32c-1ebdf16495eb', description = 'Enables recurring conversation')

Alias_Memories_Discussion_Selune_Parents_Saved = bg3.flag_object(
    files, 'Alias_Memories_Discussion_Selune_Parents_Saved', bg3.OBJECT_FLAG, flag_uuid = '6f44b5c4-6c26-4b15-94cc-c5563b354408', description = 'Enables recurring conversation')
Alias_Memories_Discussion_Selune_Parents_Killed = bg3.flag_object(
    files, 'Alias_Memories_Discussion_Selune_Parents_Killed', bg3.OBJECT_FLAG, flag_uuid = '8129a3c6-ef60-49dd-b8a7-ea913787622a', description = 'Enables recurring conversation')
Alias_Memories_Discussion_Shar_Parents_Saved = bg3.flag_object(
    files, 'Alias_Memories_Discussion_Shar_Parents_Saved', bg3.OBJECT_FLAG, flag_uuid = 'eaeb70fe-f296-452a-bae9-4983611e4724', description = 'Enables recurring conversation')

Tav_Discussed_Artefact_Came_To_Them = bg3.flag_object(
    files, 'Tav_Discussed_Artefact_Came_To_Them', bg3.OBJECT_FLAG, flag_uuid = '627be4e3-315f-4a1b-b5f0-bf9ea302535d', description = 'Tav told Shadowheart that the artefact came to them')

Tav_Asked_About_Herself = bg3.flag_object(
    files, 'Tav_Asked_About_Herself', bg3.OBJECT_FLAG, flag_uuid='06d91e16-5de4-450e-9635-637751cd6b00', description="Tav asked Shadowheart about herself, not about Shar or tadpoles")

Tav_Promised_Help_Saving_Parents = bg3.flag_object(
    files, 'Tav_Promised_Help_Saving_Parents', bg3.OBJECT_FLAG, flag_uuid='56e64ebd-6311-44c3-a47a-0614ea7ddcb4', description="Tav promised to help Shadowheart saving her parents.")

Aylin_Told_Shadowheart_About_Parents = bg3.flag_object(
    files, 'Aylin_Told_Shadowheart_About_Parents', bg3.OBJECT_FLAG, flag_uuid='b9524ed2-d6f5-482f-a2fc-7e4a74b0d782', description="Dame Aylin told Shadowheart about her parents.")

Removed_Content = bg3.flag_object(
    files, 'Removed_Content', bg3.GLOBAL_FLAG, flag_uuid='388b5716-db31-47c6-95ca-69a9555717fd', description="This content is removed from the game")

Shadowheart_FemTav_Greeting1 = bg3.flag_object(
    files, 'Shadowheart_FemTav_Greeting1', bg3.GLOBAL_FLAG, flag_uuid='47eff024-f577-495a-a698-c9e13a7e228b', description="Shadowheart will greet a female Tav with a special greeting")

Shadowheart_Laezel_Fight_Start = bg3.flag_object(
    files, 'Shadowheart_Laezel_Fight_Start', bg3.OBJECT_FLAG, flag_uuid='be5caf88-b0d7-4b9b-9dd9-4aea45d2179f', description="Set on Tav when Shadowheart vs Laezel fight starts")

# Shadowheart did not thank Tav for freeing her aboard the nautiloid
Shadowheart_Did_Not_Thank_Tav_For_Freeing_Her = bg3.flag_object(
    files, 'Shadowheart_Did_Not_Thank_Tav_For_Freeing_Her', bg3.OBJECT_FLAG, flag_uuid='5864a0de-5cd2-4d34-8415-cd7e318c73c4', description='Shadowheart did not thank Tav for freeing her aboard the nautiloid')

Shadowheart_Thanked_For_Freeing_Her = bg3.flag_object(
    files, 'Shadowheart_Thanked_For_Freeing_Her', bg3.OBJECT_FLAG, flag_uuid='ba049ff8-b0f1-4411-90b9-21f1cc9572c6', description="Set on Shadowheart when she thanked Tav for freeing her")

Disable_Banters = bg3.flag_object(
    files, 'Disable_Banters', bg3.OBJECT_FLAG, flag_uuid='d04c7721-fa3a-4ec0-a047-f36e48ecb293', description='Disable all banters while this character is around')

Gale_Gave_Compliment_Shadowheart = bg3.flag_object(
    files, 'Gale_Gave_Compliment_Shadowheart', bg3.GLOBAL_FLAG, flag_uuid='9f525a8b-4d4d-47e7-aada-ba0f27b49055', description='Gale gave a compliment to Shadowheart when he joined the party')

Tav_Asked_How_Are_You = bg3.flag_object(
    files, 'Tav_Asked_How_Are_You', bg3.GLOBAL_FLAG, flag_uuid='6f7b54a6-1467-42f0-a73f-4bf04621f8a1', description='On late redemption arc, after the cloister, Tav asked her how is she')


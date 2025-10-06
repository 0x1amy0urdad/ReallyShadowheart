has_config = false
suppress_greeting = true
status, json = pcall(Ext.IO.LoadFile, "ReallyShadowheart.json")
config = nil
if status then
  Ext.Utils.Print("ReallyShadowheart: config found")
  status, config = pcall(Ext.Json.Parse, json)
  has_config = status
  if status then
    Ext.Utils.Print("ReallyShadowheart: config parsed")
  end
end

function IsEnabled(value)
  value = string.lower(value)
  return value == "yes" or value == "y" or value == "true" or value == "t" or value == "1"
end

if has_config then
  if config["suppress_greeting"] ~= nil then
    suppress_greeting = IsEnabled(config["suppress_greeting"])
  end
end

Ext.Osiris.RegisterListener("LevelLoaded", 1, "after", function(level)
  Ext.Utils.Print("ReallyShadowheart: LevelLoaded " .. level)
end)

Ext.Osiris.RegisterListener("PROC_StartDialog_PreDialogStarted", 9, "after", function(dialog, success, instanceID, speaker1, speaker2, speaker3, speaker4, speaker5, speaker6)
  Ext.Utils.Print("ReallyShadowheart: PROC_StartDialog_PreDialogStarted " .. dialog .. ", " .. success .. ", " .. instanceID)
end)

Ext.Osiris.RegisterListener("DialogStartRequested", 2, "after", function(target, player)
  Ext.Utils.Print("ReallyShadowheart: DialogStartRequested " .. target .. ", " .. player)
end)

Ext.Osiris.RegisterListener("DialogStarted", 2, "after", function(dialog, instanceID)
  Ext.Utils.Print("ReallyShadowheart: DialogStarted " .. dialog .. ", " .. instanceID)
end)

Ext.Osiris.RegisterListener("DialogEnded", 2, "after", function(dialog, instanceID)
  Ext.Utils.Print("ReallyShadowheart: DialogEnded " .. dialog .. ", " .. instanceID)
end)

Ext.Osiris.RegisterListener("NestedDialogPlayed", 2, "after", function(dialog, instanceID)
  Ext.Utils.Print("ReallyShadowheart: NestedDialogPlayed " .. dialog .. ", " .. instanceID)
end)

--Ext.Osiris.RegisterListener("TemplateAddedTo", 4, "after", function(objectTemplate, objectInstance, inventoryHolder, addType)
--  Ext.Utils.Print("ReallyShadowheart: TemplateAddedTo " .. objectTemplate .. ", " .. objectInstance .. ", " .. inventoryHolder)
--end)


Ext.Osiris.RegisterListener("EntityEvent", 2, "after", function(object, event)
  --local object_uuid = string.sub(myString, -36)
  --if object_uuid == "3ed74f06-3c60-42dc-83f6-f034cb47c679" then
  --  Ext.Utils.Print("ReallyShadowheart: EntityEvent " .. object .. ", " .. event)
  --end
end)

if not suppress_greeting then
  Ext.Utils.Print("")
  Ext.Utils.Print("  .--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--. ")
  Ext.Utils.Print(" / .. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\")
  Ext.Utils.Print(" \\ \\/\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ \\/ /")
  Ext.Utils.Print("  \\/ /`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'\\/ / ")
  Ext.Utils.Print("  / /\\                                                                                                    / /\\ ")
  Ext.Utils.Print(" / /\\ \\   ____            _ _         ____  _               _               _                     _      / /\\ \\")
  Ext.Utils.Print(" \\ \\/ /  |  _ \\ ___  __ _| | |_   _  / ___|| |__   __ _  __| | _____      _| |__   ___  __ _ _ __| |_    \\ \\/ /")
  Ext.Utils.Print("  \\/ /   | |_) / _ \\/ _` | | | | | | \\___ \\| '_ \\ / _` |/ _` |/ _ \\ \\ /\\ / / '_ \\ / _ \\/ _` | '__| __|    \\/ / ")
  Ext.Utils.Print("  / /\\   |  _ <  __/ (_| | | | |_| |  ___) | | | | (_| | (_| | (_) \\ V  V /| | | |  __/ (_| | |  | |_     / /\\ ")
  Ext.Utils.Print(" / /\\ \\  |_| \\_\\___|\\__,_|_|_|\\__, | |____/|_| |_|\\__,_|\\__,_|\\___/ \\_/\\_/ |_| |_|\\___|\\__,_|_|   \\__|   / /\\ \\")
  Ext.Utils.Print(" \\ \\/ /                       |___/                                                                      \\ \\/ /")
  Ext.Utils.Print("  \\/ /                                                                                                    \\/ / ")
  Ext.Utils.Print("  / /\\.--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--./ /\\ ")
  Ext.Utils.Print(" / /\\ \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\/\\ \\")
  Ext.Utils.Print(" \\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `' /")
  Ext.Utils.Print("  `--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--' ")
  Ext.Utils.Print("")
else
  Ext.Utils.Print("ReallyShadowheart: successfully initialized")
end
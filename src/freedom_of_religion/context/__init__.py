from bg3moddinglib import context

MOD_NAME = 'FreedomOfReligion'
MOD_UUID = '4d9fdd9d-ad7c-4bde-bd62-3eb5fa8b8227'
MOD_DISPLAY_NAME = 'Freedom of Religion'
AUTHOR = 'iamy0urdad'
MOD_DESCRIPTION = 'This mod enables all deities for all classes and races. This unlocks all cleric content for all classes. Ever wanted to play a Lolth-sworn halfling? Now you can!'

MOD_DIR = MOD_NAME + '_' + MOD_UUID
MOD_PUBLISH_HANDLE = 0

ctx = context(MOD_NAME, MOD_UUID, "env_for")
env = ctx.env
tool = ctx.tool
files = ctx.files
assets = ctx.assets
root_path = ctx.root_path

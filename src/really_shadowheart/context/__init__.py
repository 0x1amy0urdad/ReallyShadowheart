from bg3moddinglib import context

MOD_NAME = 'ReallyShadowheart'
MOD_UUID = 'e49a2415-9dda-48ad-84c9-0abd35686529'
MOD_DISPLAY_NAME = 'Really Shadowheart'
AUTHOR = 'iamy0urdad'
MOD_DESCRIPTION = "This mod expands Shadowheart's romance, allowing you to propose marriage at the game's finale. It adds new conversations and enhances several cutscenes. It also makes her more invested in an exclusive relationship after she turns from Shar."
MOD_DIR = MOD_NAME + '_' + MOD_UUID
MOD_PUBLISH_HANDLE = 4979078

ctx = context(MOD_NAME, MOD_UUID, "really_shadowheart")
env = ctx.env
tool = ctx.tool
files = ctx.files
game_assets = ctx.assets
root_path = ctx.root_path

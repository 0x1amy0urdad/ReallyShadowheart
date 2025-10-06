from bg3moddinglib import context

MOD_NAME = 'ReallyShadowheart'
MOD_UUID = 'e49a2415-9dda-48ad-84c9-0abd35686529'
MOD_DISPLAY_NAME = 'Really Shadowheart'
AUTHOR = 'iamy0urdad'
MOD_DESCRIPTION = "You can propose to her. It doesn't mean she always accepts, she can reject you. She won't cheer you up if she catches you cheating on her. Instead, she will throw your belongings into the campfire. Lots of fixes, EA content, cutscenes, and more."

MOD_DIR = MOD_NAME + '_' + MOD_UUID
MOD_PUBLISH_HANDLE = 4979078


ctx = context(MOD_NAME, MOD_UUID, "env")
env = ctx.env
tool = ctx.tool
files = ctx.files
game_assets = ctx.assets
root_path = ctx.root_path

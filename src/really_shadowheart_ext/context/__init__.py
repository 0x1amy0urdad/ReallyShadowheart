from bg3moddinglib import context

#MOD_NAME = 'ReallyShadowheartExtension'
#MOD_UUID = 'a7e4e79b-4e4a-497b-bcc1-d324794b141d'
#MOD_DISPLAY_NAME = 'Really Shadowheart Extension'
#MOD_PUBLISH_HANDLE = 1234567
MOD_NAME = 'ReallyShadowheartEAContent'
MOD_UUID = 'bca42409-927d-2a30-aec3-2d73762da363'
MOD_DISPLAY_NAME = 'ReallyShadowheart Early Access Content'
AUTHOR = 'Stan'
MOD_DESCRIPTION = "This is an extension to Really Shadowheart that contains Early Access voice lines and mocap resources."
MOD_DIR = MOD_NAME + '_' + MOD_UUID
MOD_PUBLISH_HANDLE = 5453101

ctx = context(MOD_NAME, MOD_UUID, "really_shadowheart_extension")
env = ctx.env
tool = ctx.tool
files = ctx.files
assets = ctx.assets
root_path = ctx.root_path

ea_ctx = context(MOD_NAME, MOD_UUID, "really_shadowheart_early_access")
ea_env = ea_ctx.env
ea_tool = ea_ctx.tool
ea_files = ea_ctx.files
ea_assets = ea_ctx.assets
ea_root_path = ea_ctx.root_path

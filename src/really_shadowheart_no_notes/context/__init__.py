from bg3moddinglib import context

MOD_NAME = 'ReallyShadowheartNoNotes'
MOD_UUID = '5d78fa50-ef0c-4f74-9a2a-c0498d4f3521'

ctx = context(MOD_NAME, MOD_UUID, "env_nn")
env = ctx.env
tool = ctx.tool
files = ctx.files
assets = ctx.assets
root_path = ctx.root_path
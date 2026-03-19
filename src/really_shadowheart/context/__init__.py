from bg3moddinglib import (
    bg3_assets,
    bg3_modding_env,
    bg3_modding_tool,
    context,
    game_files
)

MOD_VERSION = (2, 1, 0, 22)

MOD_NAME = 'ReallyShadowheart'
MOD_UUID = 'e49a2415-9dda-48ad-84c9-0abd35686529'
MOD_DISPLAY_NAME = 'Really Shadowheart'
MOD_AUTHOR = 'Stan'
MOD_DESCRIPTION = "This mod expands Shadowheart's romance, allowing you to propose marriage at the game's finale. It adds new conversations and enhances several cutscenes. It also makes her more invested in an exclusive relationship after she turns from Shar."
MOD_DIR = MOD_NAME + '_' + MOD_UUID
MOD_PUBLISH_HANDLE = 4979078

ctx: context | None = None

def get_context(bg3_data_path: str | None = None) -> context:
    global ctx
    if ctx is None:
        ctx = context(MOD_NAME, MOD_UUID, 'really_shadowheart', bg3_data_path = bg3_data_path)
    return ctx

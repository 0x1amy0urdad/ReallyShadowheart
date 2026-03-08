from __future__ import annotations

import os
import os.path
import sys

# This mod deepens immersion of Shadowheart's romance. The choice she makes in "you know where" will have a much greater impact on her relationship with Tav/Durge. Besides that, this mod resolves inconsistencies in her character arc.

from bg3moddinglib import (
    set_parameters,
    feature_enabled,
    run_build_procedures
)
from .context import (
    MOD_AUTHOR,
    MOD_DESCRIPTION,
    MOD_DISPLAY_NAME,
    MOD_NAME,
    MOD_PUBLISH_HANDLE,
    MOD_UUID,
    MOD_VERSION,
    get_context
)

DUMMY_SIZE = 64739418
DUMMY_HASH = '15f1afd547fbd0ac70a98c2432c10868'

def build_mod(params: dict[str, str] | None = None) -> str:
    ctx = get_context()
    game_assets = ctx.assets
    env = ctx.env
    files = ctx.files
    root_path = ctx.root_path

    if params:
        set_parameters(params)

    sys.stdout.write('Initialization: copying files')
    env.cleanup_output()
    files.create_meta_lsx(
        MOD_NAME,
        MOD_DISPLAY_NAME,
        MOD_DESCRIPTION,
        MOD_UUID,
        MOD_AUTHOR,
        MOD_PUBLISH_HANDLE,
        MOD_VERSION,
        DUMMY_SIZE,
        DUMMY_HASH)
    files.copy_mod_logo(os.path.join(root_path, 'resources', 'really_shadowheart'), 'really_shadowheart.png')
    files.copy_memento_file(os.path.join(root_path, 'resources', 'really_shadowheart'), 'In_Loving_Memory_of_Chips_11-08-2010_18-11-2025.png')
    if feature_enabled('bg3se'):
        files.copy_script_extender_lua_files(os.path.join(root_path, 'resources', 'really_shadowheart', 'scriptextender'))
        sys.stdout.write(', copied ScriptExtender files\n')
    else:
        sys.stdout.write(', skipped copying of ScriptExtender files\n')
    files.copy_osiris_goals(os.path.join(root_path, 'resources', 'really_shadowheart', 'osiris'))
    files.copy_external_files(os.path.join(root_path, 'resources', 'really_shadowheart', 'speech'), f'Mods/{files.mod_name_uuid}')
    files.copy_external_files(os.path.join(root_path, 'resources', 'really_shadowheart', 'stats'), f'Public/{files.mod_name_uuid}')

    sys.stdout.write(f'Running build for data path {files.tool.env.bg3_data_path}\n')
    run_build_procedures(game_assets)

    return files.build(verbose = True)


def repack_mod(mod_hash: str, pak_size: int, mod_version: tuple[int, int, int, int] | None = None) -> str:
    files = get_context().files
    if mod_version is None:
        mod_version = MOD_VERSION
    files.create_meta_lsx(
        MOD_NAME,
        MOD_DISPLAY_NAME,
        MOD_DESCRIPTION,
        MOD_UUID,
        MOD_AUTHOR,
        MOD_PUBLISH_HANDLE,
        mod_version,
        pak_size,
        mod_hash)
    result = files.repack_mod()
    sys.stdout.write(f'Repacked the mod to: {result}\n')
    return result

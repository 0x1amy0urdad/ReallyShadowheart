from __future__ import annotations

import os
import os.path
import sys

from . import context

from .context import (
    assets,
    env,
    files,
    root_path
)

from bg3moddinglib import (
    run_build_procedures,
    set_parameters,
)

MOD_NAME = 'Really Shadowheart Extension'
MOD_DESCRIPTION = "This is an optional extension for Really Shadowheart. It adds cut content from Early Access to the modern BG3 patches 7/8. Both this mod and Really Shadowheart should be installed to actually enable the cut content."

DUMMY_SIZE = 64739418
DUMMY_HASH = '15f1afd547fbd0ac70a98c2432c10868'


def build_mod(mod_version: tuple[int, int, int, int], params: dict[str, str] | None = None) -> None:
    mod_name = context.MOD_NAME
    mod_display_name = context.MOD_DISPLAY_NAME
    mod_description = context.MOD_DESCRIPTION
    mod_uuid = context.MOD_UUID
    mod_publish_handle = context.MOD_PUBLISH_HANDLE

    if params:
        set_parameters(params)

    env.cleanup_output()
    files.create_meta_lsx(
        mod_name,
        mod_display_name,
        mod_description,
        mod_uuid,
        context.AUTHOR,
        mod_publish_handle,
        mod_version,
        DUMMY_SIZE,
        DUMMY_HASH)

    files.copy_osiris_goals(os.path.join(root_path, 'resources', 'really_shadowheart_ext', 'osiris'))
    files.copy_mod_logo(os.path.join(root_path, 'resources', 'really_shadowheart_ext'), 'really_shadowheart_ext.png')

    sys.stdout.write(f'Running build for data path {files.tool.env.bg3_data_path}\n')
    run_build_procedures(assets)

    files.build(verbose = True)

def repack_mod(mod_version: tuple[int, int, int, int], mod_hash: str, pak_size: int) -> None:
    files.create_meta_lsx(
        context.MOD_NAME,
        context.MOD_DISPLAY_NAME,
        context.MOD_DESCRIPTION,
        context.MOD_UUID,
        context.AUTHOR,
        context.MOD_PUBLISH_HANDLE,
        mod_version,
        pak_size,
        mod_hash)
    sys.stdout.write(f'Repacked the mod to: {files.build_mod_io_pak()}\n')

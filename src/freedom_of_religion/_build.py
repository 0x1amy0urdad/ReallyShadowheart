from __future__ import annotations

from .context import (
    assets,
    env,
    files,
    root_path
)

from bg3moddinglib import run_build_procedures, set_parameters


import os
import os.path
import sys

from . import context

DUMMY_SIZE = 64739418
DUMMY_HASH = '15f1afd547fbd0ac70a98c2432c10868'

def build_mod(mod_version: tuple[int, int, int, int], params: dict[str, str] | None = None) -> None:
    if params:
        set_parameters(params)

    env.cleanup_output()
    files.create_meta_lsx(
        context.MOD_NAME,
        context.MOD_DISPLAY_NAME,
        context.MOD_DESCRIPTION,
        context.MOD_UUID,
        context.AUTHOR,
        context.MOD_PUBLISH_HANDLE,
        mod_version,
        DUMMY_SIZE,
        DUMMY_HASH)
    files.copy_mod_logo(root_path, 'freedom_of_religion.png')
    files.copy_osiris_goals(os.path.join(root_path, 'resources', 'f_o_r', 'osiris'))
    files.copy_external_files(os.path.join(root_path, 'resources', 'f_o_r', 'gui'), f'Public/{files.mod_name_uuid}')

    sys.stdout.write(f'Running build for data path {files.tool.env.bg3_data_path}\n')
    run_build_procedures(assets)

    files.build(verbose = True)

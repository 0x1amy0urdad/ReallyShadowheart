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


MOD_NAME = 'Really Shadowheart No Notes'
MOD_DESCRIPTION = "This is an optional extension for Really Shadowheart. It removes the author's note from the save game, thus preventing a crash when you uninstall Really Shadowheart (ugh, not sure why would you do that)."


def build_mod(mod_version: tuple[int, int, int, int], params: dict[str, str] | None = None) -> None:
    if params:
        set_parameters(params)

    env.cleanup_output()
    files.create_meta_lsx(mod_version, author = 'iamy0urdad', display_name = MOD_NAME, description = MOD_DESCRIPTION)
    files.copy_mod_logo(root_path, 'really_shadowheart.png')
    files.copy_osiris_goals(os.path.join(root_path, 'resources', 'no_notes', 'osiris'))

    sys.stdout.write(f'Running build for data path {files.tool.env.bg3_data_path}\n')
    run_build_procedures(assets)

    files.build(verbose = True)

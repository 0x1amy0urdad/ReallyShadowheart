from __future__ import annotations

import os
import os.path

from ._assets import bg3_assets
from ._env import bg3_modding_env
from ._tool import bg3_modding_tool
from ._files import game_files

class context:
    __root_path: str
    __env: bg3_modding_env
    __tool: bg3_modding_tool
    __files: game_files
    __assets: bg3_assets

    def __init__(
            self,
            mod_name : str,
            mod_uuid : str,
            release_env: str,
            /,
            bg3_data_path: str | None = None,
            skip_config: bool = False
    ) -> None:
        self.__root_path = os.getcwd()
        if not os.path.isfile(os.path.join(self.__root_path, '.mod.root')):
            raise RuntimeError(f"Wrong root_path: {self.__root_path}. Please update it such that it points to a directory containing this notebook.")

        self.__env = bg3_modding_env(os.path.join(self.__root_path, "env", release_env), bg3_data_path = bg3_data_path, skip_config = skip_config)
        self.__tool = bg3_modding_tool(self.__env)
        self.__files = game_files(self.__tool, mod_name, mod_uuid)
        self.__assets = bg3_assets(self.__files)

    @property
    def root_path(self) -> str:
        return self.__root_path

    @property
    def env(self) -> bg3_modding_env:
        return self.__env

    @property
    def tool(self) -> bg3_modding_tool:
        return self.__tool

    @property
    def assets(self) -> bg3_assets:
        return self.__assets

    @property
    def files(self) -> game_files:
        return self.__files
from __future__ import annotations

import json
import os
import requests
import shutil
import time
import zipfile

from ._common import translate_path


from typing import cast

NORBYTE_LSLIB_EXPORT_TOOL_URL = ('https://github.com/Norbyte/lslib/releases/download/v1.20.3/', 'ExportTool-v1.20.3.zip')

class bg3_modding_env:
    __env_root_path: str
    __lslib_path: str
    __divine_exe: str
    __bg3_data_path: str
    __bg3_data_path_default: str
    __output_path: str
    __output_path_default: str
    __index_path: str
    __index_path_default: str
    __bg3_data_paths: dict[str, str]
    __output_paths: dict[str, str]
    __index_paths: dict[str, str]


    def __init__(
            self,
            env_root_path: str,
            /,
            bg3_data_path: str | None = None,
            output_path: str | None = None,
            index_path: str | None = None,
            skip_config: bool = False
    ) -> None:
        self.__env_root_path = env_root_path
        os.makedirs(env_root_path, exist_ok=True)
        self.__lslib_path = os.path.join(self.__env_root_path, "lslib")
        self.__divine_exe = os.path.join(self.__lslib_path, "Packed", "Tools", "divine.exe")
        self.__bg3_data_path = ""
        self.__output_path = os.path.join(self.__env_root_path, "out")
        self.__index_path = os.path.join(self.__env_root_path, "index")
        self.__get_lslib()
        if not skip_config:
            self.__read_config()
        if bg3_data_path is not None:
            self.__bg3_data_path = translate_path(bg3_data_path)
        if output_path is not None:
            self.__output_path = translate_path(output_path)
        if index_path is not None:
            self.__index_path = translate_path(index_path)
        self.__sanity_check()

    @property
    def env_root_path(self) -> str:
        return self.__env_root_path

    @property
    def lslib_path(self) -> str:
        return self.__lslib_path

    @property
    def divine_exe(self) -> str:
        return self.__divine_exe

    @property
    def bg3_data_path(self) -> str:
        return self.__bg3_data_path

    @property
    def output_path(self) -> str:
        return self.__output_path

    @property
    def index_path(self) -> str:
        return self.__index_path

    def use_config(self, name: str) -> None:
        if name == 'default':
            self.__bg3_data_path = self.__bg3_data_path_default
            self.__output_path = self.__output_path_default
            self.__index_path = self.__index_path_default
        elif name not in self.__bg3_data_paths or name not in self.__output_paths:
            raise KeyError(f"Configuration with name {name} doesn't exist")
        else:
            self.__bg3_data_path = self.__bg3_data_paths[name]
            self.__output_path = translate_path(os.path.join(self.__env_root_path, self.__output_paths[name]))
            self.__index_path = translate_path(os.path.join(self.__env_root_path, self.__index_paths[name]))

    def cleanup_output(self) -> None:
        if os.path.isdir(self.__output_path):
            shutil.rmtree(self.__output_path)
        os.makedirs(self.__output_path)

    def __lslib_exists(self) -> bool:
        return os.path.isdir(self.__lslib_path) and os.path.isfile(self.__divine_exe)

    def __get_lslib(self) -> None:
        try:
            if self.__lslib_exists():
                return
            temp_dir = os.getenv("TEMP")
            temp_path = os.path.join(temp_dir if temp_dir is not None else "./", "bg3modding" + str(time.time()))
            url = NORBYTE_LSLIB_EXPORT_TOOL_URL[0] + NORBYTE_LSLIB_EXPORT_TOOL_URL[1]
            dest_file_path = os.path.join(temp_path, NORBYTE_LSLIB_EXPORT_TOOL_URL[1])
            try:
                bg3_modding_env.download_file(url, dest_file_path)
                with zipfile.ZipFile(dest_file_path) as zip:
                    zip.extractall(path=self.__lslib_path)
            finally:
                shutil.rmtree(temp_path)
        except Exception as exc:
            raise RuntimeError(f"Failed to download and extract lslib") from exc

    def __read_config(self) -> None:
        config_file_path = os.path.join(self.__env_root_path, "config.json")
        if not os.path.isfile(config_file_path):
            return
        try:
            with open(config_file_path, "rt") as f:
                cfg = cast(dict[str, object], json.load(f))
            if 'bg3_data_paths' in cfg and isinstance(cfg['bg3_data_paths'], dict):
                bg3_data_paths = cast(dict[str, str], cfg['bg3_data_paths'])
                default_key = bg3_data_paths['default']
                self.__bg3_data_path = translate_path(bg3_data_paths[default_key])
                self.__bg3_data_path_default = self.__bg3_data_path
                self.__bg3_data_paths = bg3_data_paths
            if 'output_paths' in cfg and isinstance(cfg['output_paths'], dict):
                output_paths = cast(dict[str, str], cfg['output_paths'])
                default_key = output_paths['default']
                self.__output_path = translate_path(os.path.join(self.__env_root_path, output_paths[default_key]))
                self.__output_path_default = self.__output_path
                self.__output_paths = output_paths
            if 'index_paths' in cfg and isinstance(cfg['index_paths'], dict):
                index_paths = cast(dict[str, str], cfg['index_paths'])
                default_key = index_paths['default']
                self.__index_path = translate_path(os.path.join(self.__env_root_path, index_paths[default_key]))
                self.__index_path_default = self.__index_path
                self.__index_paths = index_paths
        except Exception as exc:
            raise RuntimeError(f"Failed to read configuration from {config_file_path}") from exc

    def __sanity_check(self) -> None:
        if not (os.path.isfile(os.path.join(self.__bg3_data_path, "Gustav.pak")) \
                and os.path.isfile(os.path.join(self.__bg3_data_path, "Shared.pak")) \
                and os.path.isfile(os.path.join(self.__bg3_data_path, "Engine.pak")) \
                and os.path.isdir(os.path.join(self.__bg3_data_path, "Localization"))):
            raise RuntimeError("BG3 data files aren't found at " + self.__bg3_data_path)
        if not os.path.isfile(self.__divine_exe):
            raise RuntimeError("Divine.exe, lslib and other tools are not found at " + self.__lslib_path)

    @staticmethod
    def download_file(url: str, dest_file_path: str) -> None:
        os.makedirs(os.path.dirname(dest_file_path))
        with open(dest_file_path, 'wb') as f:
            with requests.get(url, stream=True) as req:
                for part in req.iter_content(chunk_size=262144):
                    f.write(part)

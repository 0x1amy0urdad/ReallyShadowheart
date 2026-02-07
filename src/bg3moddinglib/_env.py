from __future__ import annotations

import json
import os
import requests
import shutil
import time
import traceback
import zipfile

from ._common import translate_path
from ._logger import get_logger


from typing import cast

NORBYTE_LSLIB_EXPORT_TOOL_URL = ('https://github.com/Norbyte/lslib/releases/download/v1.20.3/', 'ExportTool-v1.20.3.zip')

class bg3_modding_env:
    __env_root_path: str
    __lslib_path: str
    __divine_exe: str
    __bg3_data_path: str
    __bg3_data_path_default: str
    __bg3_toolkit_path: str
    __bg3_toolkit_path_default: str
    __modio_endpoint: str
    __modio_endpoint_default: str
    __modio_api_key: str
    __modio_api_key_default: str
    __modio_api_token: str
    __modio_api_token_default: str
    __output_path: str
    __output_path_default: str
    __index_path: str
    __index_path_default: str
    __bg3_data_paths: dict[str, str]
    __bg3_toolkit_paths: dict[str, str]
    __modio_endpoints: dict[str, str]
    __modio_api_keys: dict[str, str]
    __modio_api_tokens: dict[str, str]
    __output_paths: dict[str, str]
    __index_paths: dict[str, str]


    def __init__(
            self,
            env_root_path: str,
            /,
            bg3_data_path: str | None = None,
            bg3_toolkit_path: str | None = None,
            modio_endpoint: str | None = None,
            modio_api_key: str | None = None,
            modio_api_token: str | None = None,
            output_dir: str = "out",
            index_dir: str = "index",
            skip_config: bool = False
    ) -> None:
        self.__env_root_path = env_root_path
        os.makedirs(env_root_path, exist_ok=True)
        self.__lslib_path = os.path.join(self.__env_root_path, "lslib")
        self.__divine_exe = os.path.join(self.__lslib_path, "Packed", "Tools", "divine.exe")
        self.__bg3_data_path = ""
        self.__bg3_toolkit_path = ""
        self.__modio_endpoint = ""
        self.__modio_api_key = ""
        self.__modio_api_token = ""
        self.__output_path = ""
        self.__index_path = ""
        self.__get_lslib()
        if not skip_config:
            self.__read_config()
        if bg3_data_path is not None and not self.__bg3_data_path:
            self.__bg3_data_path = translate_path(bg3_data_path)
        if bg3_toolkit_path is not None and not self.__bg3_toolkit_path:
            self.__bg3_toolkit_path = translate_path(bg3_toolkit_path)
        if modio_endpoint is not None and not self.__modio_endpoint:
            self.__modio_endpoint = modio_endpoint
        if modio_api_key is not None and not self.__modio_api_key:
            self.__modio_api_key = modio_api_key
        if modio_api_token is not None and not self.__modio_api_token:
            self.__modio_api_token = modio_api_token
        if not self.__output_path:
            self.__output_path = translate_path(os.path.join(self.__env_root_path, output_dir))
        if not self.__index_path:
            self.__index_path = translate_path(os.path.join(self.__env_root_path, index_dir))
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
    def bg3_toolkit_path(self) -> str:
        return self.__bg3_toolkit_path

    @property
    def modio_endpoint(self) -> str:
        return self.__modio_endpoint

    @property
    def modio_api_key(self) -> str:
        return self.__modio_api_key

    @property
    def modio_api_token(self) -> str:
        return self.__modio_api_token

    @property
    def output_path(self) -> str:
        return self.__output_path

    @property
    def index_path(self) -> str:
        return self.__index_path

    def use_config(self, name: str) -> None:
        if name == 'default':
            self.__bg3_data_path = self.__bg3_data_path_default
            self.__bg3_toolkit_path = self.__bg3_toolkit_path_default
            self.__modio_endpoint = self.__modio_endpoint_default
            self.__modio_api_key = self.__modio_api_key_default
            self.__modio_api_token = self.__modio_api_token_default
            self.__output_path = self.__output_path_default
            self.__index_path = self.__index_path_default
        elif name not in self.__bg3_data_paths or name not in self.__output_paths:
            raise KeyError(f"Configuration with name {name} doesn't exist")
        else:
            self.__bg3_data_path = self.__bg3_data_paths[name]
            self.__bg3_toolkit_path = self.__bg3_toolkit_paths[name]
            self.__modio_endpoint = self.__modio_endpoints[name]
            self.__modio_api_key = self.__modio_api_keys[name]
            self.__modio_api_token = self.__modio_api_tokens[name]
            self.__output_path = translate_path(os.path.join(self.__env_root_path, self.__output_paths[name]))
            self.__index_path = translate_path(os.path.join(self.__env_root_path, self.__index_paths[name]))

    def cleanup_output(self) -> None:
        if os.path.isdir(self.__output_path):
            try:
                shutil.rmtree(self.__output_path)
            except:
                get_logger().error(f'bg3_modding_env.cleanup_output() failed due to exception: {traceback.format_exc()}')
        if os.path.isdir(self.__output_path):
            try:
                shutil.rmtree(self.__output_path, ignore_errors = True)
            except:
                get_logger().error(f'bg3_modding_env.cleanup_output() failed due to exception: {traceback.format_exc()}')
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
            if 'bg3_toolkit_paths' in cfg and isinstance(cfg['bg3_toolkit_paths'], dict):
                bg3_toolkit_paths = cast(dict[str, str], cfg['bg3_toolkit_paths'])
                default_key = bg3_toolkit_paths['default']
                self.__bg3_toolkit_path = translate_path(bg3_toolkit_paths[default_key])
                self.__bg3_toolkit_path_default = self.__bg3_toolkit_path
                self.__bg3_toolkit_paths = bg3_toolkit_paths
            if 'modio_endpoints' in cfg and isinstance(cfg['modio_endpoints'], dict):
                modio_endpoints = cast(dict[str, str], cfg['modio_endpoints'])
                default_key = modio_endpoints['default']
                self.__modio_endpoint = modio_endpoints[default_key]
                self.__modio_endpoint_default = self.__modio_endpoint
                self.__modio_endpoints = modio_endpoints
            if 'modio_api_keys' in cfg and isinstance(cfg['modio_api_keys'], dict):
                modio_api_keys = cast(dict[str, str], cfg['modio_api_keys'])
                default_key = modio_api_keys['default']
                self.__modio_api_key = modio_api_keys[default_key]
                self.__modio_api_key_default = self.__modio_api_key
                self.__modio_api_keys = modio_api_keys
            if 'modio_api_tokens' in cfg and isinstance(cfg['modio_api_tokens'], dict):
                modio_api_tokens = cast(dict[str, str], cfg['modio_api_tokens'])
                default_key = modio_api_tokens['default']
                self.__modio_api_token = modio_api_tokens[default_key]
                self.__modio_api_token_default = self.__modio_api_token
                self.__modio_api_tokens = modio_api_tokens
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
        if not os.path.isfile(self.__divine_exe) or not os.path.isdir(self.__lslib_path):
            raise RuntimeError("lslib and other tools are not found at " + self.__lslib_path)
        if not self.__index_path:
            raise RuntimeError("index path is not defined")

    @staticmethod
    def download_file(url: str, dest_file_path: str) -> None:
        os.makedirs(os.path.dirname(dest_file_path))
        with open(dest_file_path, 'wb') as f:
            with requests.get(url, stream=True) as req:
                for part in req.iter_content(chunk_size=262144):
                    f.write(part)

from __future__ import annotations

import json
import os

from typing import cast

from ._logger import get_logger, setup_logger

class config:
    __app_name: str = ""
    __env_root_path: str = ""
    __bg3_exe_path: str = ""
    __bg3_appdata_path: str = ""
    __bg3_toolkit_path: str = ""
    __window_width: int = 640
    __window_height: int = 768

    def __init__(self, app_name: str, use_local_appdata: bool = True) -> None:
        setup_logger(app_name)
        self.__app_name = app_name
        self.__bg3_exe_path = ""
        if use_local_appdata:
            local_appdata_path = os.getenv('LOCALAPPDATA')
            if local_appdata_path:
                self.__env_root_path = os.path.join(local_appdata_path, app_name)
            else:
                get_logger().warning(f'LOCALAPPDATA is not defined, will fall back to the current directory')
        if not self.__env_root_path:
            self.__env_root_path = os.path.abspath(os.curdir)
        get_logger().info(f'Config file path: {self.config_file_path}')
        if self.config_exists:
            self.load_config()

    @property
    def env_root_path(self) -> str:
        return self.__env_root_path

    @property
    def bg3_exe_path(self) -> str:
        return self.__bg3_exe_path

    @bg3_exe_path.setter
    def bg3_exe_path(self, val: str) -> None:
        self.__bg3_exe_path = val

    @property
    def bg3_appdata_path(self) -> str:
        return self.__bg3_appdata_path

    @bg3_appdata_path.setter
    def bg3_appdata_path(self, val: str) -> None:
        self.__bg3_appdata_path = val

    @property
    def window_width(self) -> int:
        return self.__window_width

    @window_width.setter
    def window_width(self, val: int) -> None:
        self.__window_width = val

    @property
    def window_height(self) -> int:
        return self.__window_height

    @window_height.setter
    def window_height(self, val: int) -> None:
        self.__window_height = val

    @property
    def config_file_path(self) -> str:
        return os.path.join(self.__env_root_path, self.__app_name + '.json')

    @property
    def config_exists(self) -> bool:
        return self.config_file_path != "" and os.path.isfile(self.config_file_path)

    def load_config(self) -> None:
        with open(self.config_file_path, 'rt') as f:
            get_logger().info(f'Loading configuration from {self.config_file_path}')
            cfg = cast(dict, json.load(f))
            if 'bg3_toolkit_path' in cfg:
                self.__bg3_toolkit_path = cast(str, cfg['bg3_toolkit_path'])
                get_logger().info(f'Configuration: bg3_toolkit_path = {self.__bg3_exe_path}')
            if 'bg3_exe_path' in cfg:
                self.__bg3_exe_path = cast(str, cfg['bg3_exe_path'])
                get_logger().info(f'Configuration: bg3_exe_path = {self.__bg3_exe_path}')
            if 'bg3_appdata_path' in cfg:
                self.__bg3_appdata_path = cast(str, cfg['bg3_appdata_path'])
                get_logger().info(f'Configuration: bg3_appdata_path = {self.__bg3_appdata_path}')
            if 'window_width' in cfg:
                self.__window_width = int(cfg['window_width'])
                get_logger().info(f'Configuration: window_width = {self.__window_width}')
            if 'window_height' in cfg:
                self.__window_height = int(cfg['window_height'])
                get_logger().info(f'Configuration: window_height = {self.__window_height}')

    def save_config(self) -> None:
        os.makedirs(os.path.dirname(self.config_file_path), exist_ok = True)
        with open(self.config_file_path, 'wt') as f:
            cfg = dict()
            if self.__bg3_exe_path:
                cfg['bg3_exe_path'] = self.__bg3_exe_path
            if self.__bg3_toolkit_path:
                cfg['bg3_toolkit_path'] = self.__bg3_toolkit_path
            if self.__bg3_appdata_path:
                cfg['bg3_appdata_path'] = self.__bg3_appdata_path
            cfg['window_width'] = self.__window_width
            cfg['window_height'] = self.__window_height
            f.write(json.dumps(cfg))
            get_logger().info(f'Saved configuration to {self.config_file_path}')

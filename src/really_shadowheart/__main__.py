from __future__ import annotations

import logging
import os
import sys
import traceback
import wx
import wx.lib.scrolledpanel as scrolled

from typing import cast

import bg3moddinglib as bg3

from common_ui import find_bg3_bin_path, open_bg3_exe

logger: logging.Logger

from really_shadowheart import build_mod

APP_NAME = 'Really Shadowheart Mod Generator'

class MainWindow(wx.Frame):
    __bg3_data_path: str
    __app: wx.App
    __config: bg3.config

    def __init__(self, cfg: bg3.config, app: wx.App, *args, **kwargs) -> None:
        super(MainWindow, self).__init__(None, *args, **kwargs)

        self.__bg3_data_path = os.path.join(os.path.dirname(os.path.dirname(cfg.bg3_exe_path)), 'Data')
        logger.info(f'self.__bg3_data_path = {self.__bg3_data_path}')

        self.SetMinSize(wx.Size(640, 480))
        self.SetSize(cfg.window_width, cfg.window_height)
    
        self.__app = app
        self.__config = cfg


def main() -> int:
    global logger
    app = wx.App()
    try:
        cfg = bg3.config(APP_NAME)
        logger = bg3.get_logger()
        os.makedirs(cfg.env_root_path, exist_ok = True)
        os.chdir(cfg.env_root_path)
        with open('.mod.root', 'w') as f:
            f.write('.mod.root')

        if not os.path.exists(cfg.bg3_exe_path):
            p = find_bg3_bin_path()
            if p is not None:
                cfg.bg3_exe_path = p

        w = MainWindow(cfg, app, title = APP_NAME)

        if not os.path.exists(cfg.bg3_exe_path):
            cfg.bg3_exe_path = open_bg3_exe(w)

        cfg.save_config()

        w.Show()
        app.MainLoop()
    except:
        exc_str = traceback.format_exc()
        sys.stderr.write(exc_str)
        if logger is not None:
            logger.fatal(exc_str)
            logger.info(f'{APP_NAME} has crashed')
        return 1
    return 0
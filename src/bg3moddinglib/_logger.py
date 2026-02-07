from __future__ import annotations

import logging
import os

from datetime import datetime


logger: logging.Logger | None = None

def setup_logger(app_name: str) -> None:
    global logger
    local_appdata_path = os.getenv('LOCALAPPDATA')
    if local_appdata_path:
        today = datetime.now()
        log_path = os.path.join(local_appdata_path, app_name, app_name + f'{today.year:04}{today.month:02}{today.day:02}.log')
        os.makedirs(os.path.dirname(log_path), exist_ok = True)
    else:
        log_path = app_name + '.log'

    if logger is None:
        logging.basicConfig(
            level = logging.INFO,
            format = '%(asctime)s [%(levelname)s] %(message)s',
            handlers = [
                logging.FileHandler(log_path),
                #logging.StreamHandler()
            ])
        logger = logging.getLogger(app_name)

def setup_console_logger() -> None:
    global logger
    if logger is None:
        logging.basicConfig(
            level = logging.INFO,
            format = '%(asctime)s [%(levelname)s] %(message)s',
            handlers = [
                logging.StreamHandler(),
            ])
        logger = logging.getLogger()

def get_logger() -> logging.Logger:
    global logger
    if logger is None:
        setup_logger('bg3moddinglib')
    return logger

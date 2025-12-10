from __future__ import annotations

import logging

logger: logging.Logger | None = None

def setup_logger(app_name: str) -> None:
    global logger
    logging.basicConfig(
        level = logging.INFO,
        format = '%(asctime)s [%(levelname)s] %(message)s',
        handlers = [
            logging.FileHandler(app_name + '.log'),
            logging.StreamHandler()
        ])
    logger = logging.getLogger(app_name)

def get_logger() -> logging.Logger:
    global logger
    if logger is None:
        raise RuntimeError('Logger is not initialized yet')
    return logger

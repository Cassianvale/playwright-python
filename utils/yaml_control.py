#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import yaml
from utils.log_control import INFO, ERROR
from common import ensure_path_sep


def get_yaml_data(filepath) -> dict:
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            _data = yaml.safe_load(f)  # yaml.load是不安全的
            INFO.logger.info(f"读取配置文件: {filepath}")
            return _data
    else:
        ERROR.logger.error(f"{filepath}文件路径不存在")
        raise FileNotFoundError(f"{filepath}文件路径不存在")


def read_config(key: str) -> str:
    try:
        config = ensure_path_sep('\\common\\config.yaml')
        data = get_yaml_data(config)
        return data[key]
    except KeyError:
        ERROR.logger.error(f"config不包含 {key} 键名")
        raise KeyError(f"config不包含 {key} 键名")



#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os
from typing import Text


def root_path():
    """ 获取根路径 """
    path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return path


def ensure_path_sep(path: Text) -> Text:
    """兼容 windows 和 linux 不同环境的操作系统路径 """
    if "/" in path:
        path = os.sep.join(path.split("/"))

    if "\\" in path:
        path = os.sep.join(path.split("\\"))

    return root_path() + path


def read_config(key: str) -> str:
    """ 读取config配置文件，下面是为了避免循环依赖 """
    from utils.yaml_control import GetYamlData
    config = GetYamlData(ensure_path_sep('\\common\\config.yaml')).get_yaml_data()
    return config[key]


if __name__ == '__main__':
    read_config('BASE_URL')

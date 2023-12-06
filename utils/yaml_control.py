#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import yaml

from utils.log_control import INFO


class GetYamlData:
    def __init__(self, filepath):
        self.filepath = str(filepath)

    def get_yaml_data(self) -> dict:
        if os.path.exists(self.filepath):
            with open(self.filepath, 'r', encoding='utf-8') as f:
                _data = yaml.safe_load(f)  # yaml.load是不安全的
                INFO.logger.info(f"读取配置文件: {self.filepath}")
                return _data
        else:
            raise FileNotFoundError("文件路径不存在")


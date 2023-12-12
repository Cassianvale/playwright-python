#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import os
import sys
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
    """ 读取config配置文件，下面是为了避免循环依赖 """
    try:
        config = ensure_path_sep('\\common\\config.yaml')
        data = get_yaml_data(config)
        return data[key]
    except KeyError:
        ERROR.logger.error(f"config不包含 {key} 键名")
        raise KeyError(f"config不包含 {key} 键名")


# 读取面具预设词
def mask_system():
    with open(ensure_path_sep('\\common\\mask_system.txt'), 'r', encoding='utf-8') as f:
        return f.read()

# 读取面具用户词(用于生成函数名,需要把feature内容遍历进去)
def mask_user():
    with open(ensure_path_sep('\\common\\mask_user.txt'), 'r', encoding='utf-8') as f:
        return f.read()

# 解析feature内容
def parse_feature_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        lines = content.splitlines()

    scenario_pattern = re.compile(r'^Scenario: (.*)$')
    given_pattern = re.compile(r'^Given: (.*)$')
    when_pattern = re.compile(r'^When: (.*)$')
    then_pattern = re.compile(r'^Then: (.*)$')
    and_pattern = re.compile(r'^And: (.*)$')


    scenarios = []
    scenario = []
    for line in lines:
        line = line.strip()
        if not line or line.startswith('#'):
            continue

        m = scenario_pattern.match(line)
        if m:
            scenario_text = m.group(1)
            scenario.append(scenario_text)
            scenarios.append(scenario)
            scenario = []
            continue

        m = given_pattern.match(line)
        if m:
            given_text = m.group(1)
            scenario.append(f"Given: {given_text}")
            continue

        m = when_pattern.match(line)
        if m:
            when_text = m.group(1)
            scenario.append(f"When: {when_text}")
            continue


        m = then_pattern.match(line)
        if m:
            then_text = m.group(1)
            scenario.append(f"Then: {then_text}")
            continue

        m = and_pattern.match(line)
        if m:
            and_text = m.group(1)
            # 如果当前场景不为空，并且不是Scenario:、Given:、When:或Then:的开始，添加到场景中
            if scenario and not line.startswith('And:'):
                scenario[-1] += ' ' + line
            continue

        # 如果当前不是Scenario:、Given:、When:或Then:的开始，添加到场景中
        if scenario:
            scenario[-1] += ' ' + line

    return scenarios



# 提取feature内容
def extract_feature_content(scenarios, output_file):
    with open(output_file, 'w', encoding='utf-8') as file:
        for scenario in scenarios:
            for line in scenario:
                file.write(f"{line}\n")




if __name__ == '__main__':
    # read_config('BASE_URL_A')
    # print(mask_system())

    feature_dir = ensure_path_sep('\\tests\\features')
    output_file = ensure_path_sep('\\common\\mask_user.txt')
    
    # 确保feature_dir目录存在
    if not os.path.isdir(feature_dir):
        sys.exit(f"特征文件目录'{feature_dir}'不存在")

    # 读取所有.feature文件
    feature_files = [os.path.join(feature_dir, f) for f in os.listdir(feature_dir) if f.endswith('.feature')]
    if not feature_files:
        sys.exit(f"特征文件目录'{feature_dir}'下没有找到.feature文件")

    # 遍历每个.feature文件并提取内容
    scenarios = []
    for feature_file in feature_files:
        print(f"处理文件: {feature_file}")
        scenarios += parse_feature_file(feature_file)

    # 将提取的内容写入到mask_user.txt文件中
    extract_feature_content(scenarios, output_file)
    print(f"提取的内容已写入到文件: {output_file}")

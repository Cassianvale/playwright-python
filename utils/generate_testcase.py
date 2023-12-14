# custom_generate_code.py
# -*- coding: utf-8 -*-

"""使用新模板生成测试用例"""

import os
import pytest
import argparse
import openai
from openai.error import OpenAIError
from pytest_bdd import generation
from pytest_bdd.generation import cast, make_python_name, make_python_docstring, make_string_literal, parse_feature_files
from pytest_bdd.parser import Feature, ScenarioTemplate, Step
from pytest_bdd.scripts import check_existense, migrate_tests
from mako.lookup import TemplateLookup
from typing import List
from utils.yaml_control import read_config, mask_system, mask_user
from utils.log_control import INFO, ERROR

new_template_lookup = TemplateLookup(directories=[os.path.join(os.path.dirname(__file__), "templates")])

openai.api_key = read_config("OPENAI_API_KEY")  # 获取config中配置的OPENAI_API_KEY
# openai.api_key = os.getenv("OPENAI_API_KEY")  # 获取你系统变量中配置的OPENAI_API_KEY
openai.api_base = "https://openai.wndbac.cn/v1" #在这里设置即可,需要特别注意这里的/v1是必须的，否则报错。前面的地址注意替换即可。
# openai.proxy = "https://api.nextweb.fun/openai"


def custom_generate_code(features: List[Feature], scenarios: List[ScenarioTemplate], steps: List[Step]) -> str:
    """Generate test code using a new template file."""
    grouped_steps = generation.group_steps(steps)

    template = new_template_lookup.get_template("new_test.py.mak")
    
    results = template.render(
        features=features,
        scenarios=scenarios,
        steps=grouped_steps,
        make_python_name=make_python_name,
        make_python_docstring=make_python_docstring,
        make_string_literal=make_string_literal,
        
    )

    # # 使用steps来生成函数名
    # function_names = []
    # try: 

    #     for step in steps:
    #         # 使用OpenAI生成函数名
    #         response = openai.ChatCompletion.create(
    #                 model="gpt-3.5-turbo-16k",  # 使用最新的模型
    #                 # 这里添加了messages参数，它是一个包含单个系统消息的列表
    #                 messages=[
    #                     {"role": "system", "content": f"Generate a function name for the step: {step.name}"}
    #                 ],
    #                 max_tokens=10000,
    #                 stop=["&nbsp;", "."],
    #             )
                
    #         # 处理生成的函数名
    #         for choice in response.choices:
    #             try:
    #                 function_name = choice.text.strip()
    #                 function_names.append(function_name)
    #             except AttributeError:
    #                 pass

    # except OpenAIError as e:
    #     ERROR.logger.error("OpenAI报错: %s", e)
    #     exit(1)

    return cast(str, results)

# 使用 monkeypatch 替换原库里的代码
@pytest.fixture
def patch_generate_code(monkeypatch):
    monkeypatch.setattr(generation, "generate_code", custom_generate_code)

def test_with_custom_generate_code(patch_generate_code):
    # 调用 generate_code 时将实际调用 custom_generate_code
    assert True


# generate cli命令
def print_generated_code(args: argparse.Namespace) -> None:
    """Print generated test code for the given filenames."""
    # 解析出还未放进模板的 features、scenarios、steps
    features, scenarios, steps = parse_feature_files(args.files)
    # 这里使用的是自定义 custom_generate_code 函数
    code = custom_generate_code(features, scenarios, steps)
    print(code)

def main() -> None:
    """Custom main entry point."""
    parser = argparse.ArgumentParser(prog="pytest-bdd")
    subparsers = parser.add_subparsers(help="sub-command help", dest="command")
    subparsers.required = True
    parser_generate = subparsers.add_parser("generate", help="generate help")
    parser_generate.add_argument(
        "files",
        metavar="FEATURE_FILE",
        type=check_existense,
        nargs="+",
        help="Feature files to generate test code with",
    )
    # 设置默认的函数为自定义的 print_generated_code 函数
    parser_generate.set_defaults(func=print_generated_code)

    parser_migrate = subparsers.add_parser("migrate", help="migrate help")
    parser_migrate.add_argument("path", metavar="PATH", help="Migrate outdated tests to the most recent form")
    parser_migrate.set_defaults(func=migrate_tests)

    args = parser.parse_args()
    if hasattr(args, "func"):
        args.func(args)


if __name__ == '__main__':
    main()

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

    return cast(str, results)

# 使用 monkeypatch 替换原库里的代码
@pytest.fixture
def patch_generate_code(monkeypatch):
    monkeypatch.setattr(generation, "generate_code", custom_generate_code)

# 这是一个使用了上面 fixture 的测试函数
def test_with_custom_generate_code(patch_generate_code):
    # 调用 generate_code 时将实际调用 custom_generate_code
    assert True


# generate cli命令
def print_generated_code(args: argparse.Namespace) -> None:
    """Print generated test code for the given filenames."""
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

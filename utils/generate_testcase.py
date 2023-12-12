# feature_to_testcase.py

import re
import os
from common import ensure_path_sep

def generate_test_cases(feature_file: str):
    """Generate pytest-bdd scenarios from feature text.

    Args:
        feature_file (str): Feature file path

    Returns:
        None
    """
    with open(feature_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    scenario = None
    steps = []
    for line in lines:
        line = line.strip()
        if line.startswith('Scenario:'):
            scenario = line.split('Scenario: ')[1].strip().replace(' ', '_').lower()
        elif line.startswith('Given') or line.startswith('When') or line.startswith('Then'):
            step = re.sub(r'(Given: |When: |Then: |And: )', '', line).strip().replace(' ', '_').lower()
            steps.append(step)



    # 获取文件名(不包含拓展名)
    filename = os.path.basename(feature_file)
    filename_parts = os.path.splitext(filename)[0]
    # 获取文件路径的前一部分，即上层目录并获取目录名称
    parent_dir_name = os.path.basename(os.path.dirname(feature_file))
    # 场景路径（文件名+上一级目录名称）
    scenario_path = parent_dir_name + '/' + filename


    with open(ensure_path_sep(f'\\tests\\step_defs\\test_{filename_parts}.py'), 'w', encoding='utf-8') as file:

        file.write('from pytest_bdd import scenario, given, when, then\n\n')
        file.write(f'@scenario(\'{scenario_path}\', \'{scenario.replace("_", " ").title()}\')\n')
        file.write(f'def test_{scenario}():\n')
        file.write('    pass\n\n')

        for step in steps:
            file.write(f'@given(\'{step.replace("_", " ").title()}\')\n')
            file.write(f'def given_{step}():\n')
            file.write('    pass\n\n')

        for step in steps:
            file.write(f'@when(\'{step.replace("_", " ").title()}\')\n')
            file.write(f'def {step}():\n')
            file.write('    pass\n\n')

        for step in steps:
            file.write(f'@then(\'{step.replace("_", " ").title()}\')\n')
            file.write(f'def {step}():\n')
            file.write('    pass\n\n')

if __name__ == '__main__':
    generate_test_cases(ensure_path_sep('\\tests\\features\\shop\\shop.feature'))
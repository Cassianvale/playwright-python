# feature_to_testcase.py

import os

from pytest_bdd import (
    scenario,
)


def generate_test_cases(feature_text):
    """Generate pytest-bdd scenarios from feature text.

    Args:
        feature_text (str): Gherkin 语法中的特征文本

    Returns:
        dict: 场景和步骤的字典
    """
    # Create a temporary file to store the feature text
    with open(os.path.join(os.path.dirname(__file__), 'feature.feature'), 'w') as f:
        f.write(feature_text)

    # Load the feature file into the pytest-bdd engine

    os.path.dirname(os.path.abspath(__file__))


factory = TempPathFactory(search_path=os.path.dirname(__file__))
pytest_bdd.pytest_plugins.register(factory.mktemp('').name)
pytest_bdd.setup_bdd(pytest.config, ['-s', '--debug'])

# Discover scenarios and steps
scenarios, steps = pytest_bdd.parse_scenarios('feature.feature')

# Convert the scenarios and steps into a dictionary
test_cases = {}
for scenario_name, scenario_steps in scenarios.items():
    test_case_name = f'test_{scenario_name.lower()}'
    test_cases[test_case_name] = scenario(scenario_name, target_fixture=test_case_name)
    for step_name, step_func in scenario_steps.items():
        test_cases[test_case_name].add_step(step_name, step_func)

return test_cases

# Example usage:
if __name__ == '__main__':
    feature_text = dedent("""\
      Feature: Login Feature
        Scenario: Successful Login
          Given I have opened the login page
          When I enter the correct username and password
          Then I should see the dashboard

        Scenario: Failed Login
          Given I have opened the login page
          When I enter the incorrect username and password
          Then I should see an error message
  """)

    test_cases = generate_test_cases(feature_text)
    print(test_cases)
    # Output should be a dictionary with two keys: 'test_successful_login' and 'test_failed_login'
    # Each key should point to a function representing a scenario.
    # The functions can be imported and used in a test suite.

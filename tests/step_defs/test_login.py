"""登录功能的测试 feature tests."""

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)


@scenario('features\test_login.feature', 'Failed Login')
def test_failed_login():
    """Failed Login."""


@scenario('features\test_login.feature', 'Successful Login')
def test_successful_login():
    """Successful Login."""


@given('我已经打开了登录页面')
def open_login_page():
    """Open Login Page."""

@when('我输入正确的用户名和密码')
def input_username_and_password():
    """Input username and password."""

@then('我应该看到仪表板')
def check_dashboard():
    """Check dashboard."""
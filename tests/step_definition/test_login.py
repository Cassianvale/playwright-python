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




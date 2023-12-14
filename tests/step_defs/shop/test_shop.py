"""As a new user, feature tests.
This is new template!
"""

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)


@scenario('shop\shop.feature', '我按照购物流程进行下单, 新用户注册等操作')
def test_我按照购物流程进行下单_新用户注册等操作():
    """我按照购物流程进行下单, 新用户注册等操作."""


@scenario('shop\shop.feature', '进入首页后, 查看附件数量')
def test_进入首页后_查看附件数量():
    """进入首页后, 查看附件数量."""


@given('Sean 作为新用户需要注册')
def _():
    """Sean 作为新用户需要注册."""
    raise NotImplementedError


@given('Sean 完成了下单')
def _():
    """Sean 完成了下单."""
    raise NotImplementedError


@given('Sean 打开了T-shirt 分类')
def _():
    """Sean 打开了T-shirt 分类."""
    raise NotImplementedError


@given('Sean 打开网站首页')
def _():
    """Sean 打开网站首页."""
    raise NotImplementedError


@given('Sean 选了一件T-shirt加入购物车并进行下一步')
def _():
    """Sean 选了一件T-shirt加入购物车并进行下一步."""
    raise NotImplementedError


@when('Sean 查看个人资料订单页面')
def _():
    """Sean 查看个人资料订单页面."""
    raise NotImplementedError


@then('Sean 发现订单显示丢失')
def _():
    """Sean 发现订单显示丢失."""
    raise NotImplementedError


@then('发现附件数量异常')
def _():
    """发现附件数量异常."""
    raise NotImplementedError


from utils.generate_testcase import generate_test_cases
from textwrap import dedent

data =dedent("""Feature: 登录功能的测试
    Description: 这是一个测试用户登录功能的特性

    Scenario: Successful Login
        Given: 我已经打开了登录页面
        When: 我输入正确的用户名和密码
        And: 我提交表单
        Then: 我应该看到仪表板

    Scenario: Failed Login
        Given: 我已经打开了登录页面
        When: 我输入错误的用户名和密码
        And: 我提交表单
        Then: 我应该看到错误消息""")
test_cases = generate_test_cases(data)
print(test_cases)
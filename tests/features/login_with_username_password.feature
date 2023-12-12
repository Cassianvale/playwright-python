@hotlink @login
  Feature: As a user,I want to login with username and password,In order to access the application.

    Background:
      Given Sean 打开url

    Scenario: Sean wants to login with username and password
      When Sean 输入用户名和密码登录
      Then Sean 应该看到登录页面


    Scenario: 我想打开登录页面，以便我可以登录我的帐户.
      Then 我可以在登录页面看到 Sean
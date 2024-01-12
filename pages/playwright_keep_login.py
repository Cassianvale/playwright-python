#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import pytest
from playwright.sync_api import Page, sync_playwright
from page_factory.button import Button
from page_factory.input import Input
from pages.playwright_home_page import PlaywrightHomePage
from utils.yaml_control import read_config


class PlaywrightKeepLogin(PlaywrightHomePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        # 定位登录框
        self.login_input_username = Input(
            page, locator="input[name='username']", name='UserName'
        )

        # 定位密码框
        self.login_input_password = Input(
            page, locator="input[name='password']", name='PassWord'
        )

        # 悬浮登录按钮
        self.login_button = Button(
            page, locator="button[type='submit']", name='Login'
        )

    def login(self, username: str, password: str):
        self.login_input_username.fill(username)
        self.login_input_password.fill(password)
        self.login_button.click()

    def wait_for_login(self):
        # 等待登录完成，这里可以添加更多特定的等待逻辑
        self.page.wait_for_selector(".login-success", state="visible")


@pytest.fixture(scope="session", autouse=True)
def keep_login() -> None:
    with sync_playwright() as playwright:
        chromium = playwright.chromium.launch(headless=False)
        page = chromium.new_page()
        # 假设PlaywrightKeepLogin类已经正确定义，并且page是您想要保持登录状态的页面实例
        keep_login = PlaywrightKeepLogin(page)
        keep_login.visit(read_config("BASE_URL_B"))
        keep_login.login("17551104890", "123456")
        keep_login.wait_for_login()


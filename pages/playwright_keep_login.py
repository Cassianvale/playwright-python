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
            page, locator="//span[text()='请输入用户名']", name='UserName'
        )

        # 定位密码框
        self.login_input_password = Input(
            page, locator="//input[@placeholder='请输入密码']", name='PassWord'
        )

        # 悬浮登录按钮
        self.login_button = Button(
            page, locator='//span[@class,"n-button__content"]', name='Login'
        )

    def login(self, username: str, password: str):
        self.login_input_username.fill(username)
        self.login_input_password.fill(password)
        self.login_button.click()

import allure
from playwright.sync_api import Page, Response
from typing import Union
from components.navigation.navbar import Navbar


class BasePage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.navbar = Navbar(page)

    '''用于打开一个新的页面，等待页面内容加载完成并且网络请求基本稳定后再进行后续操作'''
    def visit(self, url: str) -> Union[Response, None]:
        """
        wait_until:
            'domcontentloaded'：当页面的 HTML 文档被完全加载和解析后认为页面加载完成
            'load'：打开页面并等待直到 'load' 事件被触发
            'networkidle'：不建议使用，因为它会等待至少500毫秒内没有网络连接。文档中明确指出不要在测试中使用这个方法，而是依赖于网页断言来评估页面准备就绪的状态
            'commit'：当接收到网络响应并且文档开始加载时，认为操作已经完成
        """
        with allure.step(f'打开url "{url}"'):
            return self.page.goto(url, wait_until='networkidle')

    '''用于重新加载页面，等待页面的基本结构和内容就绪后再进行后续操作'''
    def reload(self) -> Union[Response, None]:
        with allure.step(f'使用 url 重新加载页面 "{self.page.url}"'):
            return self.page.reload(wait_until='domcontentloaded')

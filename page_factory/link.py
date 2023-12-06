import allure
from page_factory.component import BaseComponent
from playwright.sync_api import Locator, Page, expect


class Link(BaseComponent):
    @property
    def type_of(self) -> str:
        return 'link'

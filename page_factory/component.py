import allure
from abc import ABC, abstractmethod
from playwright.sync_api import Locator, Page, expect


class BaseComponent(ABC):
    def __init__(self, page: Page, locator: str, name: str) -> None:
        self.page = page
        self.name = name
        self.locator = locator

    @property
    @abstractmethod
    def type_of(self) -> str:
        return 'component'

    def get_locator(self, **kwargs) -> Locator:
        locator = self.locator.format(**kwargs)
        return self.page.locator(locator)

    def click(self, **kwargs) -> None:
        with allure.step(f'点击 {self.type_of} 名称为 "{self.name}"'):
            locator = self.get_locator(**kwargs)
            locator.click()

    def should_be_visible(self, **kwargs) -> None:
        with allure.step(f'检查 {self.type_of} "{self.name}" 是否可见'):
            locator = self.get_locator(**kwargs)
            expect(locator).to_be_visible()

    def should_have_text(self, text: str, **kwargs) -> None:
        with allure.step(f'检查 {self.type_of} "{self.name}" 是否包含文本 "{text}"'):
            locator = self.get_locator(**kwargs)
            expect(locator).to_have_text(text)

    # 验证跳转后的url
    def should_have_url(self, url: str, **kwargs) -> None:
        with allure.step(f'检查 {self.type_of} "{self.name}" 是否跳转到 "{url}"'):
            locator = self.get_locator(**kwargs)
            expect(locator).to_have_url(url)


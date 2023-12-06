import allure
from page_factory.component import BaseComponent


class Button(BaseComponent):
    @property
    def type_of(self) -> str:
        return 'button'

    def hover(self, **kwargs) -> None:
        with allure.step(f'悬停在 {self.type_of} 上，名称为 "{self.name}"'):
            locator = self.get_locator(**kwargs)
            locator.hover()

    def double_click(self, **kwargs):
        with allure.step(f'双击 {self.type_of}，名称为 "{self.name}"'):
            locator = self.get_locator(**kwargs)
            locator.dblclick()

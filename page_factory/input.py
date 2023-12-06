import allure
from playwright.sync_api import expect
from page_factory.component import BaseComponent


class Input(BaseComponent):
    @property
    def type_of(self) -> str:
        return 'input'

    #
    def fill(self, value: str, validate_value=False, **kwargs):
        with allure.step(f'将 {self.type_of} "{self.name}" 填写为值 "{value}"'):
            locator = self.get_locator(**kwargs)
            locator.fill(value)

            if validate_value:
                self.should_have_value(value, **kwargs)

    # 清空输入
    def clear(self, **kwargs):
        with allure.step(f'将 {self.type_of} "{self.name}" 清空'):
            locator = self.get_locator(**kwargs)
            locator.fill("")

    def should_have_value(self, value: str, **kwargs):
        with allure.step(f'检查 {self.type_of} "{self.name}" 是否具有值 "{value}"'):
            locator = self.get_locator(**kwargs)
            expect(locator).to_have_value(value)

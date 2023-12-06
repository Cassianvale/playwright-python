import allure
from page_factory.component import BaseComponent


class Title(BaseComponent):
    @property
    def type_of(self) -> str:
        return 'title'

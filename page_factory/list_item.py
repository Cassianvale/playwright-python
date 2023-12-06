import allure
from page_factory.component import BaseComponent


class ListItem(BaseComponent):
    @property
    def type_of(self) -> str:
        return 'list item'

import pytest

from pages.playwright_home_page import PlaywrightHomePage
from pages.playwright_languages_page import PlaywrightLanguagesPage
from common import read_config as rd


class TestSearch:
    @pytest.mark.parametrize('keyword', ['python'])
    def test_search(
        self,
        keyword: str,
        playwright_home_page: PlaywrightHomePage,
        playwright_languages_page: PlaywrightLanguagesPage
    ):
        playwright_home_page.visit(rd("BASE_URL"))
        playwright_home_page.navbar.open_search()
        playwright_home_page.navbar.search_modal.find_result(
            keyword, result_number=0
        )

        playwright_languages_page.language_present(language=keyword)

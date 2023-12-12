import pytest
import os
import codecs
import yaml
import jinja2
import pytest_bdd

from playwright.sync_api import Page, sync_playwright

from pages.playwright_home_page import PlaywrightHomePage
from pages.playwright_languages_page import PlaywrightLanguagesPage


@pytest.fixture(scope='function')
def chromium_page() -> Page:
    with sync_playwright() as playwright:
        chromium = playwright.chromium.launch(headless=False)
        yield chromium.new_page()


@pytest.fixture(scope='function')
def playwright_home_page(chromium_page: Page) -> PlaywrightHomePage:
    return PlaywrightHomePage(chromium_page)


@pytest.fixture(scope='function')
def playwright_languages_page(chromium_page: Page) -> PlaywrightLanguagesPage:
    return PlaywrightLanguagesPage(chromium_page)


@pytest.hookimpl(hookwrapper=True)
def pytest_generate_tests(metafunc):
    if 'fixturenames' in metafunc.fixtureinfo:
        fixturenames = metafunc.fixtureinfo['fixturenames']
        if fixturenames:
            # 获取当前测试模块的路径
            module_dir = os.path.dirname(metafunc.function.__code__.co_filename)
            # 打开模板文件
            with codecs.open(os.path.join(module_dir, 'template.py.j2'), 'r', 'utf-8') as f:
                template = jinja2.Template(f.read())
            # 读取Feature文件的内容
            feature_file_contents = []
            for f in metafunc.config.pluginmanager.getplugin('bdd')._feature_files:
                with codecs.open(f, 'r', 'utf-8') as fh:
                    feature_file_contents.append(fh.read())
            # 使用模板渲染
            tests = template.render(features=feature_file_contents)
            # 保存测试文件
            with codecs.open(os.path.join(module_dir, 'generated_{}.py'.format(metafunc.function.__name__)), 'w', 'utf-8') as outfile:
                outfile.write(tests)
            # 标记测试函数，以便pytest跳过它们
            metafunc.fixturenames = []
            metafunc.no_default_fixture = True
            metafunc._mark_test_as_skipped()



def pytest_addoption(parser):
    parser.addoption(
        '--include-generated-tests',
        action='store_true',
        default=False,
        help='Run tests generated from feature files.'
    )

def pytest_runtest_setup(item):
    if item.get_marker('skip_if_generated_tests_not_included'):
        if not item.config.getoption('--include-generated-tests'):
            pytest.skip('Skipping generated test. Use --include-generated-tests to run.')
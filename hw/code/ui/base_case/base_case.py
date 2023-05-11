import pytest
from _pytest.fixtures import FixtureRequest
from ui.pages.base_page import BasePage


class BaseCase:
    authorize = True
    EMAIL = 'basetest@example.com'
    PASSWORD = 'ka@ld34o(12Cafk'

    @pytest.fixture(scope="function", autouse=True)
    def set_page(self, driver, url_config):
        self.driver = driver
        self.page = BasePage(driver, url_config)

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, request: FixtureRequest):
        self.page.open()


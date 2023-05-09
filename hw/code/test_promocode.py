import pytest
from ui.pages.promocode_page import PromocodePage
from ui.base_case.base_case import BaseCase
from ui.paths import paths


class TestPromocode(BaseCase):
    @pytest.fixture(scope="function", autouse=True)
    def set_page(self, driver, url_config):
        self.driver = driver
        self.page = PromocodePage(driver, url_config)

    def test_empty_input(self):
        message = 'Введите промокод'
        self.page.authorize()
        self.page.add_product_after_login()
        self.page.click(self.page.locators.BUTTON_APPLY)
        assert self.page.find(self.page.locators.MESSAGE).text == message

    def test_error_symbols(self):
        message = 'Введены недопустимые символы'
        self.page.authorize()
        self.page.add_product_after_login()
        self.page.send_keys(self.page.locators.INPUT, '{1111]')
        self.page.click(self.page.locators.BUTTON_APPLY)
        assert self.page.find(self.page.locators.MESSAGE).text == message

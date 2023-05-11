import pytest
from ui.pages.address_popup_page import AddressPopupPage
from ui.base_case.base_case import BaseCase
from ui.paths import paths


class TestAddressPopup(BaseCase):
    @pytest.fixture(scope="function", autouse=True)
    def set_page(self, driver, url_config):
        self.driver = driver
        self.page = AddressPopupPage(driver, url_config)

    def test_open_address_popup(self):
        popup_header = 'Мои адреса'
        self.page.add_product()
        self.page.click(self.page.cart_locators.BUTTON_EDIT_ADDRESS)
        assert self.page.find(self.page.popup_locators.POPUP).is_displayed()
        assert self.page.find(self.page.popup_locators.POPUP_HEADER).text == popup_header

    def test_add_address_button(self):
        self.page.add_product()
        self.page.click(self.page.cart_locators.BUTTON_EDIT_ADDRESS)
        self.page.click(self.page.popup_locators.ADD_BUTTON_IN_POPUP)
        assert self.page.is_url(paths.PROFILE)

    def test_cancel_button(self):
        self.page.add_product()
        self.page.click(self.page.cart_locators.BUTTON_EDIT_ADDRESS)
        self.page.click(self.page.popup_locators.BUTTON_CANCEL)
        assert not self.page.find(self.page.popup_locators.POPUP).is_displayed()

    def test_apply_button(self):
        self.page.add_product()
        self.page.click(self.page.cart_locators.BUTTON_EDIT_ADDRESS)
        self.page.click(self.page.popup_locators.BUTTON_APPLY)
        assert not self.page.find(self.page.popup_locators.POPUP).is_displayed()

    def test_select_address(self):
        self.page.authorize()
        self.page.add_product_after_login()
        self.page.click(self.page.cart_locators.BUTTON_EDIT_ADDRESS)
        select_address = self.page.find(self.page.locators.ADDRESS).get_attribute('id')
        self.page.click(self.page.locators.ADDRESS)
        self.page.click(self.page.popup_locators.BUTTON_APPLY)
        assert self.page.find(
            self.page.cart_locators.SELECT_ADDRESS).get_attribute('id') == select_address

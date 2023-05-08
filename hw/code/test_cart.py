import pytest
from ui.pages.cart_page import CartPage
from ui.base_case.base_case import BaseCase
from ui.paths import paths


class TestCart(BaseCase):
    @pytest.fixture(scope="function", autouse=True)
    def set_page(self, driver, url_config):
        self.driver = driver
        self.page = CartPage(driver, url_config)

    # def test_title(self):
    #     title = 'Корзина - Reazon'
    #     assert self.driver.title == title

    # def test_empty_cart(self):
    #     empty_cart_message =  "Корзина пуста. Случайно не нужен \nтелефон\n?"
    #     assert self.page.find(self.page.locators.EMPTY_CART_MESSAGE).text == empty_cart_message
        
    #     self.page.click(self.page.locators.EMPTY_CART_MESSAGE_LINK)
    #     assert self.page.is_url(paths.CATEGORY_PHONES)
    
    # def test_button_clear_cart(self):
    #     empty_cart_message =  "Корзина пуста. Случайно не нужен \nтелефон\n?"
    #     self.page.add_product()
    #     self.page.click(self.page.locators.BUTTON_CLEAR_CART)
    #     assert self.page.find(self.page.locators.EMPTY_CART_MESSAGE).text == empty_cart_message

    # def test_all_checkbox_active(self):
    #     self.page.add_product()
    #     item_price, item_count = self.page.get_item_count_price()
    #     total_price = self.page.get_total_price()

    #     assert self.page.find(self.page.locators.CHECKBOX_SELECT_ALL).is_selected()
    #     assert self.page.find(self.page.locators.CHECKBOX_ITEM).is_selected()
    #     assert item_price * item_count == total_price
    
    # def test_checkbox_select_all_inactive(self):
    #     self.page.add_product()
    #     self.page.click(self.page.locators.CHECKBOX_SELECT_ALL)
    #     total_price = self.page.get_total_price()

    #     assert not self.page.find(self.page.locators.CHECKBOX_SELECT_ALL).is_selected()
    #     assert not self.page.find(self.page.locators.CHECKBOX_ITEM).is_selected()
    #     assert total_price == 0
    
    # def test_checkbox_select_all_active(self):
    #     self.page.add_product()
    #     self.page.click(self.page.locators.CHECKBOX_SELECT_ALL)
    #     self.page.click(self.page.locators.CHECKBOX_SELECT_ALL)
    #     total_price = self.page.get_total_price()
    #     item_price, item_count = self.page.get_item_count_price()

    #     assert self.page.find(self.page.locators.CHECKBOX_SELECT_ALL).is_selected()
    #     assert self.page.find(self.page.locators.CHECKBOX_ITEM).is_selected()
    #     assert total_price == item_price * item_count

    # def test_item_checkbox_inactive(self):
    #     self.page.add_product()
    #     total_price = self.page.get_total_price()
    #     self.page.click(self.page.locators.CHECKBOX_ITEM)
    #     new_total_price = self.page.get_total_price()
    #     item_price, item_count = self.page.get_item_count_price()

    #     assert new_total_price == total_price - item_count * item_price
    
    # def test_item_checkbox_active(self):
    #     self.page.add_product()
    #     self.page.click(self.page.locators.CHECKBOX_ITEM)
    #     total_price = self.page.get_total_price()
    #     self.page.click(self.page.locators.CHECKBOX_ITEM)
    #     new_total_price = self.page.get_total_price()
    #     item_price, item_count = self.page.get_item_count_price()

    #     assert new_total_price == total_price + item_price * item_count

    # def test_product_name_link(self):
    #     self.page.add_product()
    #     product_name_link_start = '/product/'
    #     product_name_link = self.page.find(self.page.locators.PRODUCT_NAME_LINK).get_attribute('href')

    #     assert product_name_link_start in product_name_link

    # def test_product_photo(self):
    #     self.page.add_product()
    #     product_name_link = self.page.find(self.page.locators.PRODUCT_NAME_LINK).get_attribute('href')
    #     product_photo_link = self.page.find(self.page.locators.PRODUCT_PHOTO_LINK).get_attribute('href')

    #     assert product_name_link == product_photo_link

    # def test_favorites_button(self):
    #     message_for_login = 'Войдите, чтобы добавить в избранное'
    #     self.page.add_product()
    #     self.page.click(self.page.locators.BUTTON_FAVOURITE)

    #     assert self.page.find(self.page.locators.POPUP_MESSAGE).is_displayed()
    #     assert self.page.find(self.page.locators.MESSAGE_FOR_LOGIN).text == message_for_login

    def test_delete_product_button(self):
        self.page.add_product()
        self.page.click(self.page.locators.BUTTON_DELETE_PRODUCT)
        total_price = self.page.get_total_price()
        assert total_price == 0

    def test_
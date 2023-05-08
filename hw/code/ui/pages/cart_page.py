from ui.locators import locators
from ui.pages.base_page import BasePage
from ui.base_case.base_case import BaseCase
from ui.paths import paths


class CartPage(BasePage):
    # auth_locators = locators.AuthorizeLocators
    header_locators = locators.HeaderLocators
    category_phones_locators = locators.CategoryPhonesLocators
    locators = locators.CartLocators
    PATH = paths.CART

    def add_product(self):
        self.click(self.locators.EMPTY_CART_MESSAGE_LINK)
        self.click(self.category_phones_locators.BUTTON_ADD_TO_CART)
        self.click(self.header_locators.BUTTON_CART)

    def get_item_count_price(self):
        item_price = int(self.find(self.locators.ITEM_PRICE).text.split(' ')[0])
        item_count = int(self.find(self.locators.ITEM_COUNT).text)
        return item_price, item_count

    def get_total_price(self):
        return int(self.find(self.locators.TOTAL_PRICE).text.split(' ')[0])    
    
    # def authorize(self):
    #     self.click(self.auth_locators.LOGIN_BUTTON)
    #     self.send_keys(self.auth_locators.INPUT_EMAIL, BaseCase.EMAIL)
    #     self.send_keys(self.auth_locators.INPUT_PASSWORD, BaseCase.PASSWORD)
    #     self.click(self.auth_locators.LOGIN_BUTTON_FORM)

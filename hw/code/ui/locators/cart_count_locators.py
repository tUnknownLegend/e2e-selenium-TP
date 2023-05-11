from selenium.webdriver.common.by import By
from ui.hrefs import Hrefs


class CartCountLocators():
    def __init__(self):
        self.hrefs = Hrefs()

    GET_COUNT_CONTAINER = (
        By.XPATH, '//div[@id="block-button-add-to-cart"]' + 
        '/div[contains(@id, "button-add-to-cart/")]'
    )

    GET_PLUS_BUTTON = (
        By.XPATH, '//button[contains(@id, "button-plus_cart/")]'
    )

    GET_MINUS_BUTTON = (
        By.XPATH, '//button[contains(@id, "button-minus_cart/")]'
    )

    GET_ITEM_COUNT_IN_CART = (
        By.XPATH, '//div[@class="add-to-cart-button_amount-selector__amount"]'
    )
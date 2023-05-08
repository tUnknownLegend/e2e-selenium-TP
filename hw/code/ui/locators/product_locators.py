from selenium.webdriver.common.by import By
from ui.locators.base_locators import BaseLocators


class ProductLocators(BaseLocators):
    def __init__(self):
        super(ProductLocators, self).__init__()

        self.GET_PRODUCT_TITLE = (
            By.CLASS_NAME,
            'text-normal-very-large link__no-color comment-page-header__title')
        self.GET_CATEGORY_BUTTON = (
            By.XPATH, '//div[@class="product-page-header product-page-color-jet-black"]' +
            '/div[@class="text-normal-default link__no-color"]'
        )

        self.GET_RATING_NUMBER = (
            By.XPATH, '//div[@class="product-page-header__rating link__no-color"]' +
            '/span[@class="text-normal-large-normal"]'
        )

        self.GET_FAVOURITES_LABEL = (
            By.XPATH, '//div[@class="product-page-header__selection"]'
        )

from selenium.webdriver.common.by import By
from ui.locators.base_locators import BaseLocators


class ProductTitleLocators(BaseLocators):
    def __init__(self):
        super(ProductTitleLocators, self).__init__()

        self.GET_PRODUCT_TITLE = (
            By.XPATH,
            '//a[@class="text-normal-very-large' +
            ' link__no-color comment-page-header__title"]')
        self.GET_CATEGORY_BUTTON = (
            By.XPATH, '//div[@class="product-page-header product-page-color-jet-black"]' +
            '/a[@class="text-normal-default link__no-color"]'
        )

        self.GET_RATING_NUMBER = (
            By.XPATH, '//a[@class="product-page-header__rating link__no-color"]' +
            '/span[@class="text-normal-large-normal"]'
        )

        self.GET_RATING_LINK = (
            By.XPATH, '//a[@class="product-page-header__rating link__no-color"]'
        )

        self.GET_FAVOURITES_LABEL = (
            By.XPATH, '//label[@class="product-page-header__selection"]'
        )

        self.GET_FAVOURITES_INPUT = (
            By.ID, 'favourite-opt_cart'
        )

        self.GET_PHOTO = (
            By.CLASS_NAME, 'product-page-main__photo'
        )

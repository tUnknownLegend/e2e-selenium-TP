import allure
import pytest

from ui.fixtures import get_driver
from ui.pages.product_page import ProductPage
from ui.locators.base_locators import BaseLocators


@pytest.mark.skip('skip')
class TestProduct():
    driver = get_driver(browser_name='chrome')
    product = ProductPage(driver)
    rating = ProductPage(driver, BaseLocators())

    def __init__(self, selectors):
        self.rating = ProductPage(self.driver, selectors())

    @allure.feature('Check photo')
    @allure.story('is photo broken')
    @product.render_decorator
    def test_is_photo_broken(self):
        self.productPage.checkItemPhoto()

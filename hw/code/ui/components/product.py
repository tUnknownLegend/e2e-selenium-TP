# import allure
# import pytest

# from ui.fixtures import get_driver
# from ui.pages.product_title import ProductTitle
# from ui.locators.base_locators import BaseLocators


# @pytest.mark.skip('skip')
# class TestProduct():
#     driver = get_driver(browser_name='chrome')
#     product = ProductTitle(driver)
#     rating = ProductTitle(driver, BaseLocators())

#     def __init__(self, selectors):
#         self.rating = ProductTitle(self.driver, selectors())

#     @allure.feature('Check photo')
#     @allure.story('is photo broken')
#     @product.render_decorator
#     def test_is_photo_broken(self):
#         self.productPage.checkItemPhoto()

import allure

from ui.fixtures import get_driver
from ui.pages.product_title import ProductTitle
from ui.pages.login_page import LoginPage
from ui.pages.header import Header

# import pytest

# @pytest.mark.skip('skip')


class TestProductTitle():
    driver = get_driver(browser_name='chrome')
    productPage = ProductTitle(driver)
    loginPage = LoginPage(driver)
    header = Header(driver)

    @allure.feature('Title')
    @allure.story('tab title, links, rating')
    @productPage.render_decorator
    def test_product_title(self):
        with allure.step('checkTabTitle'):
            self.productPage.checkTabTitle()

        with allure.step('checkLinkInTheTitles'):
            self.productPage.checkLinkInTheTitles()

        with allure.step('checkCategoryLink'):
            self.productPage.checkCategoryLink()

    @allure.feature('Favourites button')
    @allure.story('unauth check')
    @productPage.render_decorator
    def test_favorites_unauth(self):
        self.productPage.unauthFavourites()

    @allure.feature('Favourites button')
    @allure.story('auth check')
    @productPage.render_decorator
    def test_favorites_auth(self):
        with allure.step('login'):
            self.header.findLoginPageButton().click()
            self.loginPage.login()

        with allure.step('go back to product page'):
            self.productPage.render_page()

        with allure.step('authFavourites check and unchecked'):
            self.productPage.authFavourites()
            self.productPage.authFavourites()

        with allure.step('logout'):
            self.header.logout()

    @allure.feature('Check photo')
    @allure.story('is photo broken')
    @productPage.render_decorator
    def test_is_photo_broken(self):
        self.productPage.checkItemPhoto()

import allure
# import pytest


from ui.fixtures import get_driver
from ui.pages.login_page import LoginPage
from ui.pages.header import Header
from ui.pages.search_header import SearchHeader


class TestHeader():
    driver = get_driver(browser_name='chrome')
    login_page = LoginPage(driver)
    header = Header(driver)
    searchHeader = SearchHeader(driver)

    # @pytest.mark.skip('skip')
    @allure.feature('Tests login / profile button')
    @allure.story('Login and find profile button, then logout')
    @header.render_decorator
    def test_header_profile_button(self):
        allure.step('findLoginPageButton')
        self.header.findLoginPageButton().click()

        allure.step('login')
        self.login_page.login()

        allure.step('logout')
        self.header.logout()

    # @pytest.mark.skip('skip')
    @allure.feature('Header navigation buttons')
    @allure.story('Checks links in buttons on right side of the header')
    @header.render_decorator
    def test_rightHeaderButtons(self):
        allure.step('findOrdersPageButton')
        self.header.findOrdersPageButton()

        allure.step('findCartPageButton')
        self.header.findCartPageButton()

        allure.step('findFavouritesPageButton')
        self.header.findFavouritesPageButton()

    # @pytest.mark.skip('skip')
    @allure.feature('Tests search')
    @allure.story('different payloads for search and suggestions')
    @header.render_decorator
    def test_searchTest(self):
        allure.step('checkPhoneCategory')
        self.searchHeader.checkPhoneCategory()

        allure.step('checkProhibitedSymbolsSearch')
        self.searchHeader.checkProhibitedSymbolsSearch()

        allure.step('checkSearchSuggestions')
        self.searchHeader.checkSearchSuggestions()

        allure.step('sendNoResultsRequest')
        self.searchHeader.sendNoResultsRequest()

        allure.step('performTooShortSearchRequest')
        self.searchHeader.performTooShortSearchRequest()

    @allure.feature('Selects category')
    @allure.story('selects all categories from hamburger menu in header')
    @header.render_decorator
    def test_categorySelect(self):
        self.header.selectCategory()

    def checkLogo(self):
        self.header.find()

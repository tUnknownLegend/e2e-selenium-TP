from ui.pages.base_page import BasePage
from ui.locators.header_locators import HeaderLocators
from ui.locators.catalog_locators import CatalogLocators


class Header(BasePage):
    url = 'https://www.reazon.ru/'
    email = 'basetest@example.com'
    pwd = 'ka@ld34o(12Cafk'

    locators = HeaderLocators()
    categoryLocators = CatalogLocators()

    def emptyFunction():
        pass

    def findLoginPageButton(self):
        return self.find(self.locators.OPEN_LOGIN_PAGE_BUTTON)

    def findUserPageButton(self):
        return self.find(self.locators.OPEN_USER_PAGE_BUTTON)

    def findLogOutPopUp(self):
        return self.find(self.locators.SIGN_OUT_POP_UP)

    def hoverOverLogout(self):
        logOutPopUp = self.findLogOutPopUp()

        assert logOutPopUp.value_of_css_property(
            "display") == 'none'

        self.hover(self.findUserPageButton())

        assert logOutPopUp.value_of_css_property(
            "display") == 'block'

        return logOutPopUp

    def logout(self):
        self.hoverOverLogout().click()

    def findFavouritesPageButton(self):
        return self.find(self.locators.OPEN_FAVOURITES_PAGE_BUTTON)

    def findCartPageButton(self):
        return self.find(self.locators.OPEN_CART_PAGE_BUTTON)

    def findOrdersPageButton(self):
        return self.find(self.locators.OPEN_ORDERS_PAGE_BUTTON)

    def performSearch(self, searchValue, callback=emptyFunction):
        searchInput = self.find(self.locators.SEARCH_INPUT)
        searchInput.clear()
        searchInput.send_keys(searchValue)

        callback()

        self.find(self.locators.SEARCH_BUTTON).click()

    def checkErrorMessage(self, errorMessage):
        errorMessageElement = self.find(
            self.locators.HEADER_ERROR_MESSAGE)

        self.waitUntilVisible(self.locators.HEADER_ERROR_MESSAGE, 1)
        assert errorMessageElement.get_attribute('innerText') == errorMessage

        self.waitUntilInvisible(self.locators.HEADER_ERROR_MESSAGE, 6)

    def performTooShortSearchRequest(self):
        self.performSearch('df')

        self.checkErrorMessage('Введите не меньше 3 символов')

    def sendNoResultsRequest(self):
        self.performSearch(
            'aZАя!?()_./-',
            lambda: self.waitUntilInvisible(self.locators.GET_FIRST_SEARCH_SUGGESTION, 1))

        self.waitUntilVisible(self.locators.SEARCH_NO_RESULTS_MESSAGE, 3)

    def checkFirstSearchSuggestion(self):
        assert self.find(
            self.locators.GET_FIRST_SEARCH_SUGGESTION)

    def checkPhoneCategory(self):
        self.performSearch(
            'т', self.checkFirstSearchSuggestion)
        self.is_opened('https://www.reazon.ru/category/phones')

    def checkProhibitedSymbolsSearch(self):
        self.performSearch("<img src onerror=alert(1) />")

        self.checkErrorMessage('Введены недопустимые символы')

    def checkSearchSuggestions(self):
        searchInput = self.find(self.locators.SEARCH_INPUT)
        searchInput.clear()
        searchInput.send_keys('iph')

        thirdSearchSuggestion = self.find(
            self.locators.GET_THIRD_SEARCH_SUGGESTION)

        thirdSuggestionText = thirdSearchSuggestion.get_attribute('innerText')
        thirdSearchSuggestion.click()

        self.waitUntilVisible(self.locators.FIND_FIRST_SEARCH_RESULT_TITLE, 3)

        assert self.find(
            self.locators.FIND_FIRST_SEARCH_RESULT_TITLE
        ).get_attribute('innerText') == thirdSuggestionText

        self.waitUntilInvisible(self.locators.GET_THIRD_SEARCH_SUGGESTION, 1)

    def selectCategory(self):
        self.waitUntilInvisible(self.locators.GET_CATEGORIES_CONTAINER, 1)

        self.find(self.locators.OPEN_CATEGORY_SELECTOR_BUTTON).click()

        categories = self.find(self.locators.GET_CATEGORIES_CONTAINER)

        for index in range(int(categories.get_attribute('childElementCount'))):
            category = self.find(self.locators.CATEGORY_SELECTOR_MENU(index + 1))
            category.click()
            self.waitUntilInvisible(self.locators.GET_CATEGORIES_CONTAINER, 1)

            assert self.find(
                self.categoryLocators.GET_CATEGORY_NAME).get_attribute(
                'innerText') == category.get_attribute('innerText')

            self.find(self.locators.OPEN_CATEGORY_SELECTOR_BUTTON).click()

    def findLogo(self):
        assert self.find(self.locators.GET_LOGO).get_attribute('href') == '/'

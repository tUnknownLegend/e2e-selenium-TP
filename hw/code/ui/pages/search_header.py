from ui.pages.base_page import BasePage
from ui.locators.header_locators import HeaderLocators
from ui.locators.catalog_locators import CatalogLocators
from ui.locators.search_header_locators import SearchHeaderLocators


class SearchHeader(BasePage):
    url = 'https://www.reazon.ru/'

    headerLocators = HeaderLocators()
    categoryLocators = CatalogLocators()
    locators = SearchHeaderLocators()

    def _noop():
        pass

    def performSearch(self, searchValue, callback=_noop):
        searchInput = self.find(self.locators.SEARCH_INPUT)
        searchInput.clear()
        searchInput.send_keys(searchValue)

        callback()

        self.find(self.locators.SEARCH_BUTTON).click()

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

        self.waitUntilVisible(
            self.locators.GET_THIRD_SEARCH_SUGGESTION, 1)
        thirdSearchSuggestion = self.find(
            self.locators.GET_THIRD_SEARCH_SUGGESTION)

        thirdSuggestionText = thirdSearchSuggestion.get_attribute('innerText')
        thirdSearchSuggestion.click()

        self.waitUntilVisible(self.locators.FIND_FIRST_SEARCH_RESULT_TITLE, 1)

        assert self.find(
            self.locators.FIND_FIRST_SEARCH_RESULT_TITLE
        ).get_attribute('innerText') == thirdSuggestionText

        self.waitUntilInvisible(self.locators.GET_THIRD_SEARCH_SUGGESTION, 1)

from selenium.webdriver.common.by import By
from ui.locators.base_locators import BaseLocators


class SearchHeaderLocators(BaseLocators):
    def __init__(self):
        super(SearchHeaderLocators, self).__init__()

        self.SEARCH_INPUT = (By.NAME, 'search-line')

        self.SEARCH_BUTTON = (By.ID, 'search-button-submit')

        self.SEARCH_NO_RESULTS_MESSAGE = (By.ID, 'content-unAuth-page-redirect')

        self.FIND_FIRST_SEARCH_RESULT_TITLE = (
            By.XPATH, '//div[@id="items-block"]/div[@class="catalog-item-card"][1]' +
            '/div[@class="catalog-item-card__description-block"]' +
            '/div[@id="catalog_item-title-block"]')

        self.GET_THIRD_SEARCH_SUGGESTION = (By.ID, 'search-suggestion:2')

        self.GET_FIRST_SEARCH_SUGGESTION = (By.ID, 'search-suggestion:0')

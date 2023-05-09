from selenium.webdriver.common.by import By
from ui.locators.base_locators import BaseLocators


class CatalogLocators(BaseLocators):

    def __init__(self):
        super(CatalogLocators, self).__init__()

    GET_CATEGORY_NAME = (
        By.XPATH, '//div[@id="catalog_content"]' +
        '/div[@class="catalog__category-name text-normal-huge"]'
    )

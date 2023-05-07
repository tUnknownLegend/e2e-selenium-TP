from selenium.webdriver.common.by import By


class CatalogLocators():

    GET_CATEGORY_NAME = (
        By.XPATH, '//div[@id="catalog_content"]' +
        '/div[@class="catalog__category-name text-normal-huge"]')

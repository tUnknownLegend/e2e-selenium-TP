
from selenium.webdriver.common.by import By
from ui.hrefs import Hrefs


class HomeLocators():
    def __init__(self):
        self.hrefs = Hrefs()

        self.GET_CATEGORIES_CONTAINER = (By.ID, 'catalog')

    def CATEGORY_SELECTOR_MENU(self, index):
        return (By.XPATH, '//div[@id="catalog"]' +
                f'/a[@class="item-top-cards text-normal-default"][{index}]')

    def GET_CATEGORY_NAME(self, index):
        return (By.XPATH, '//div[@id="catalog"]' +
                f'/a[@class="item-top-cards text-normal-default"]{index}'
                '/div[@id="mainpage_top-category"]')

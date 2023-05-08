
from selenium.webdriver.common.by import By
from ui.hrefs import Hrefs


class HomeLocators():
    def __init__(self):
        self.hrefs = Hrefs()

        self.HOME_CATEGORIES = (By.ID, 'catalog')

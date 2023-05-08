from selenium.webdriver.common.by import By
from ui.locators.base_locators import BaseLocators


class FavouritesLocators(BaseLocators):
    def __init__(self):
        super(FavouritesLocators, self).__init__()

    def GET_FIRST_PRODUCT_BY_HREF(self, id): return (
        By.XPATH, f'//a[@href="{self.hrefs.product}/{id}"]')

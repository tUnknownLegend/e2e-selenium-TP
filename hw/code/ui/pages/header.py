from ui.pages.base_page import BasePage
from ui.locators.header_locators import HeaderLocators


class Header(BasePage):
    url = 'https://www.reazon.ru'
    email = 'basetest@example.com'
    pwd = 'ka@ld34o(12Cafk'

    locators = HeaderLocators()

    def findLoginPageButton(self):
        self.find(self.locators.OPEN_LOGIN_PAGE_BUTTON)

    def findUserPageButton(self):
        self.find(self.locators.OPEN_USER_PAGE_BUTTON)

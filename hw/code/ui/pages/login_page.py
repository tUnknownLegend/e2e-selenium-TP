from ui.pages.base_page import BasePage
from ui.locators.login_locators import LoginPageLocators
from ui.locators.home_locators import HomeLocators
import os


class LoginPage(BasePage):
    email = os.getenv('LOGIN_A')
    pwd = os.getenv('PWD_A')
    userName = 'Sheesh'

    homeLocators = HomeLocators()

    def __init__(self, driver):
        super(LoginPage, self).__init__(driver)
        self.locators = LoginPageLocators()
        self.url = self.locators.hrefs.domain + self.locators.hrefs.login

    def login(self):
        email_field = self.find(
            self.locators.EMAIL_INPUT_LOGIN_PAGE)

        email_field.clear()
        email_field.send_keys(self.email)

        pwd_field = self.find(
            self.locators.PASSWORD_INPUT_LOGIN_PAGE)
        pwd_field.clear()
        pwd_field.send_keys(self.pwd)

        self.find(self.locators.SIGN_IN_BUTTON_LOGIN_PAGE).click()

        self.waitUntilVisible(self.homeLocators.GET_CATEGORIES_CONTAINER)

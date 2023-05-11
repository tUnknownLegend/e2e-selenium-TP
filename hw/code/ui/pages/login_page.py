from ui.pages.base_page import BasePage
from ui.locators.locators import LoginLocators
from ui.locators.locators import BasePageLocators
from ui.base_case.base_case import BaseCase


class LoginPage(BasePage):
    locators = LoginLocators
    PATH = 'login'


    def login(self):
        self.click(LoginLocators.LOGIN_BUTTON)
        self.click(LoginLocators.EMAIL_INPUT_LOGIN_PAGE)
        self.send_keys(LoginLocators.EMAIL_INPUT_LOGIN_PAGE, BaseCase.EMAIL)
        self.send_keys(LoginLocators.PASSWORD_INPUT_LOGIN_PAGE, BaseCase.PASSWORD)
        self.click(LoginLocators.SIGN_IN_BUTTON_LOGIN_PAGE)

    def logout(self):
        self.click(BasePageLocators.USER_BUTTON)
        self.click(LoginLocators.LOGOUT_BUTTON)
        
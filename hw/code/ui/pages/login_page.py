from ui.pages.base_page import BasePage
from ui.locators.login_locators import LoginPageLocators


class LoginPage(BasePage):
    url = 'https://www.reazon.ru/login'
    email = 'basetest@example.com'
    pwd = 'ka@ld34o(12Cafk'

    locators = LoginPageLocators()

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

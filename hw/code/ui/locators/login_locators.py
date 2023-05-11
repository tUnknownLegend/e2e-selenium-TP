from selenium.webdriver.common.by import By
from ui.locators.base_locators import BaseLocators


class LoginPageLocators(BaseLocators):
    def __init__(self):
        super(LoginPageLocators, self).__init__()

        self.EMAIL_INPUT_LOGIN_PAGE = (By.NAME, 'email')

        self.PASSWORD_INPUT_LOGIN_PAGE = (By.NAME, 'password')

        self.SIGN_IN_BUTTON_LOGIN_PAGE = (By.ID, 'submit-result')

        self.ERROR = (By.ID, 'error-text')

        self.SIGNUP_LINK = (By.LINK_TEXT, 'Зарегистрироваться')
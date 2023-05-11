from selenium.webdriver.common.by import By
from ui.locators.base_locators import BaseLocators


class SignupPageLocators(BaseLocators):
    def __init__(self):
        super(SignupPageLocators, self).__init__()

        self.USERNAME_INPUT_SIGNUP_PAGE = (By.NAME, 'username')

        self.EMAIL_INPUT_SIGNUP_PAGE = (By.NAME, 'email')

        self.PASSWORD_INPUT_SIGNUP_PAGE = (By.NAME, 'password')

        self.REPEAT_PASSWORD_INPUT_SIGNUP_PAGE = (By.NAME, 'repeatPassword')


        self.SIGN_UP_BUTTON_SIGNUP_PAGE = (By.ID, 'submit-result')

        self.ERROR = (By.ID, 'error-text')

        self.SIGNIN_LINK = (By.LINK_TEXT, 'Войти')
        
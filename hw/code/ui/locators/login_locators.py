from selenium.webdriver.common.by import By


class LoginPageLocators():
    EMAIL_INPUT_LOGIN_PAGE = (By.NAME, 'email')

    PASSWORD_INPUT_LOGIN_PAGE = (By.NAME, 'password')

    SIGN_IN_BUTTON_LOGIN_PAGE = (By.ID, 'submit-result')

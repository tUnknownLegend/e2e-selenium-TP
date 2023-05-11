from selenium.webdriver.common.by import By


class BasePageLocators:
    USER_BUTTON = (By.XPATH, '//a[@href="/user"]')


class LoginLocators:
    EMAIL_INPUT_LOGIN_PAGE = (By.NAME, 'email')
    PASSWORD_INPUT_LOGIN_PAGE = (By.NAME, 'password')
    SIGN_IN_BUTTON_LOGIN_PAGE = (By.ID, 'submit-result')
    LOGIN_BUTTON = (By.XPATH, '//a[@href="/login"]')
    LOGOUT_BUTTON = (By.XPATH, '//a[@href="/logout"]')


class ProfileLocators:
    MUST_AUTH_MESSAGE = (By.XPATH, '//a[@href="/login" and @class="link"]')

    USER_AVATAR = (By.ID, 'user-photo_user-page')
    CHANGE_AVATAR_INPUT = (By.ID, 'changeUserPhoto__upload')
    DELETE_AVATAR_BUTTON = (By.ID, 'user-page__btn-delete-photo')

    CHANGE_NAME_BUTTON = (
        By.XPATH, '//img[contains(@alt, "edit name button")]')
    CHANGE_NAME_INPUT = (By.XPATH, '//input[contains(@id, "name__popUp")]')
    NAME_STRING = (By.ID, 'name-text')

    USER_INFO_POPUP_APPLY_BUTTON = (By.ID, 'popup-form_user-info__apply')
    USER_INFO_POPUP_CANCEL_BUTTON = (By.ID, 'popup-form_user-info__cancel')
    VALIDATION_RESULT_MSG = (By.ID, 'error-text')
    SERVER_ERROR_MSG = (By.ID, 'server-error__text_')

    CHANGE_EMAIL_BUTTON = (
        By.XPATH, '//img[contains(@alt, "edit email button")]')
    CHANGE_EMAIL_INPUT = (By.XPATH, '//input[contains(@id, "email__popUp")]')
    EMAIL_STRING = (By.ID, 'email-text')

    CHANGE_PHONE_BUTTON = (
        By.XPATH, '//img[contains(@alt, "edit phone button")]')
    CHANGE_PHONE_INPUT = (By.XPATH, '//input[contains(@id, "phone__popUp")]')
    PHONE_STRING = (By.ID, 'phone-text')

    CHANGE_PASSWORD_BUTTON = (By.XPATH, '//div[contains(@id, "password")]/a')
    # (By.ID, 'password')
    CURRENT_PASSWORD_INPUT = (By.ID, 'password__popUp')
    NEW_PASSWORD_INPUT = (By.ID, 'password__2__popUp')
    REPEAT_PASSWORD_INPUT = (By.ID, 'password__3__popUp')

    ADD_PAYMENT_CARD = (By.ID, 'add-payment-card')
    PAYMENT_CARD_NUMBER_INPUT = (By.ID, 'cardNumber')
    PAYMENT_CARD_MONTH_INPUT = (By.ID, 'month')
    PAYMENT_CARD_YEAR_INPUT = (By.ID, 'year')
    PAYMENT_CARD_CVC_INPUT = (By.ID, 'cvc')
    PAYMENT_CARD_APPLY_BUTTON = (By.ID, 'popup-form_add-card__apply')
    PAYMENT_CARD_CANCEL_BUTTON = (By.ID, 'popup-form_add-card__cancel')
    PAYMENT_CARD_NUMBER = (By.XPATH, '//div[contains(@class, "payment-card-number")]')


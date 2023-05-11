import pytest
from ui.pages.profile_page import ProfilePage
from ui.base_case.base_case import BaseCase
from ui.pages.login_page import LoginPage
from ui.locators.base_locators import BaseLocators
from ui.tabTitles import TabTitles
import os


class TestProfileWithoutAuth(BaseCase):
    PATH = 'user'

    @pytest.fixture(scope="function", autouse=True)
    def set_page(self, driver):
        self.driver = driver
        self.page = ProfilePage(driver, self.path.domain + self.path.user)
        self.loginPage = LoginPage(driver)

    def test_no_auth_message(self):
        assert str(self.page.get_attribute(
            self.page.locators.MUST_AUTH_MESSAGE, 'innerText')) == 'Войдите'


class TestProfile(BaseCase):
    PATH = 'user'
    baseLocators = BaseLocators()
    tabTitles = TabTitles()
    defaultAvatarPath = baseLocators.hrefs.domain + '/img/UserPhoto.webp'
    testAvatar = '/hw/code/ui/prikol.jpg'
    fieldCantBeEmptyMessage = 'Поле обязательно должно быть заполнено'
    wrongEmail = 'Неверный формат почты'
    phoneMustContain11DigitsMessage = 'Телефон должен содержать 11 цифр. Введено 4/11'
    oldPasswordIncorrectMessage = 'Старый пароль не верный'
    password = '123456'
    passwordMustContain6SymbolsMessage = 'Пароль должен содержать минимум 6 символов'
    passwordsUnmatch = 'Введенные пароли не совпадают'

    streetArbat = 'Arbat street'
    streetRedSquare = 'Red Square'
    houseNumber = '1'

    @pytest.fixture(scope="function", autouse=True)
    def set_page(self, driver):
        self.driver = driver
        self.page = ProfilePage(driver, self.path.domain + self.path.user)
        self.loginPage = LoginPage(driver)

    def test_title(self):
        self.loginPage.loginProfile()
        assert self.driver.title == self.tabTitles.profile

    def test_render_with_auth(self):
        self.loginPage.loginProfile()
        assert self.page.get_attribute(
            self.page.locators.CHANGE_PASSWORD_BUTTON, 'innerText') is not None

    def test_default_avatar(self):
        self.loginPage.loginProfile()

        assert self.page.get_attribute(
            self.page.locators.USER_AVATAR, 'src').strip() == (
            self.defaultAvatarPath)

    def test_change_avatar(self):
        self.loginPage.loginProfile()
        img_input = self.page.find(self.page.locators.CHANGE_AVATAR_INPUT)
        img_input.send_keys(os.getcwd() + self.testAvatar)

        assert self.page.get_attribute(
            self.page.locators.USER_AVATAR, 'src') != (
            self.defaultAvatarPath + '/')

        self.page.click(self.page.locators.USER_AVATAR)
        self.page.click(self.page.locators.DELETE_AVATAR_BUTTON)

    def test_change_avatar_with_refresh(self):
        self.loginPage.loginProfile()
        img_input = self.page.find(self.page.locators.CHANGE_AVATAR_INPUT)
        img_input.send_keys(os.getcwd() + '/hw/code/ui/prikol.jpg')

        self.page.refresh()

        assert self.page.get_attribute(
            self.page.locators.USER_AVATAR, 'src') != 'https://www.reazon.ru/img/UserPhoto.webp/'

        self.page.click(self.page.locators.USER_AVATAR)
        self.page.click(self.page.locators.DELETE_AVATAR_BUTTON)

    def test_change_name_not_empty_str(self):
        self.loginPage.loginProfile()

        self.page.click(self.page.locators.CHANGE_NAME_BUTTON)

        new_name = 'new name'

        input = self.page.find(self.page.locators.CHANGE_NAME_INPUT)
        input.send_keys(new_name)
        self.page.find(self.page.locators.USER_INFO_POPUP_APPLY_BUTTON).click()
        self.page.open()

        current_name = self.page.get_attribute(
            self.page.locators.NAME_STRING, 'innerText').strip()
        assert current_name == new_name

        self.page.click(self.page.locators.CHANGE_NAME_BUTTON)
        input = self.page.find(self.page.locators.CHANGE_NAME_INPUT)
        input.send_keys('default name')
        self.page.find(self.page.locators.USER_INFO_POPUP_APPLY_BUTTON).click()

    def test_change_name_empty_str(self):
        self.loginPage.loginProfile()

        self.page.click(self.page.locators.CHANGE_NAME_BUTTON)
        self.page.find(self.page.locators.USER_INFO_POPUP_APPLY_BUTTON).click()

        assert self.page.get_attribute(
            self.page.locators.VALIDATION_RESULT_MSG, 'innerText') == (
            self.fieldCantBeEmptyMessage
        )

    def test_change_email_empty_str(self):
        self.loginPage.loginProfile()

        self.page.click(self.page.locators.CHANGE_EMAIL_BUTTON)
        self.page.find(self.page.locators.USER_INFO_POPUP_APPLY_BUTTON).click()

        assert self.page.get_attribute(
            self.page.locators.VALIDATION_RESULT_MSG, 'innerText') == (
            self.fieldCantBeEmptyMessage
        )

    def test_change_email_incorrect_str(self):
        self.loginPage.loginProfile()

        self.page.click(self.page.locators.CHANGE_EMAIL_BUTTON)
        input = self.page.find(self.page.locators.CHANGE_EMAIL_INPUT)

        input.send_keys('test')
        self.page.find(self.page.locators.USER_INFO_POPUP_APPLY_BUTTON).click()

        assert self.page.get_attribute(
            self.page.locators.VALIDATION_RESULT_MSG, 'innerText') == (
            'Неверный формат почты')

    def test_change_email_correct_str(self):
        self.loginPage.loginProfile()

        self.page.click(self.page.locators.CHANGE_EMAIL_BUTTON)

        new_email = 'new@new'

        input = self.page.find(self.page.locators.CHANGE_EMAIL_INPUT)
        input.send_keys(new_email)
        self.page.click(self.page.locators.USER_INFO_POPUP_APPLY_BUTTON)

        self.page.refresh()
        current_email = self.page.get_attribute(
            self.page.locators.EMAIL_STRING, 'innerText').strip()
        self.page.refresh()

        self.page.click(self.page.locators.CHANGE_EMAIL_BUTTON)
        input = self.page.find(self.page.locators.CHANGE_EMAIL_INPUT)
        input.send_keys('basetest@example.com')
        self.page.click(self.page.locators.USER_INFO_POPUP_APPLY_BUTTON)

        assert current_email == new_email

    def test_change_phone_empty_str(self):
        self.loginPage.loginProfile()

        self.page.click(self.page.locators.CHANGE_PHONE_BUTTON)
        self.page.find(self.page.locators.CHANGE_PHONE_INPUT).clear()

        self.page.find(self.page.locators.USER_INFO_POPUP_APPLY_BUTTON).click()

        assert self.page.get_attribute(
            self.page.locators.VALIDATION_RESULT_MSG, 'innerText') == (
            self.fieldCantBeEmptyMessage
        )

    def test_change_phone_incorrect_str(self):
        self.loginPage.loginProfile()

        self.page.click(self.page.locators.CHANGE_PHONE_BUTTON)
        input = self.page.find(self.page.locators.CHANGE_PHONE_INPUT)

        input.send_keys('123')
        self.page.find(self.page.locators.USER_INFO_POPUP_APPLY_BUTTON).click()

        assert self.page.get_attribute(
            self.page.locators.VALIDATION_RESULT_MSG, 'innerText') == (
            self.phoneMustContain11DigitsMessage)

    def test_change_phone_correct_str(self):
        self.loginPage.loginProfile()

        self.page.click(self.page.locators.CHANGE_PHONE_BUTTON)
        self.page.find(self.page.locators.CHANGE_PHONE_INPUT).clear()

        new_phone = '+75544332211'

        input = self.page.find(self.page.locators.CHANGE_PHONE_INPUT)
        input.send_keys(new_phone)
        self.page.find(self.page.locators.USER_INFO_POPUP_APPLY_BUTTON).click()
        self.page.refresh()

        current_phone = self.page.get_attribute(
            self.page.locators.PHONE_STRING, 'innerText').strip()

        self.page.click(self.page.locators.CHANGE_PHONE_BUTTON)
        input = self.page.find(self.page.locators.CHANGE_PHONE_INPUT)
        input.send_keys('1122334455')
        self.page.find(self.page.locators.USER_INFO_POPUP_APPLY_BUTTON).click()

        assert current_phone == new_phone

    def test_change_password_incorrect_empty_str(self):
        self.loginPage.loginProfile()

        self.page.click(self.page.locators.CHANGE_PASSWORD_BUTTON)

        self.page.find(self.page.locators.USER_INFO_POPUP_APPLY_BUTTON).click()

        assert self.page.get_attribute(
            self.page.locators.VALIDATION_RESULT_MSG, 'innerText') == (
            'Поле обязательно должно быть заполнено')

    def test_change_password_incorrect_small_str(self):
        self.loginPage.loginProfile()

        self.page.click(self.page.locators.CHANGE_PASSWORD_BUTTON)
        input = self.page.find(self.page.locators.CURRENT_PASSWORD_INPUT)
        input.send_keys(BaseCase.PASSWORD)

        input = self.page.find(self.page.locators.NEW_PASSWORD_INPUT)
        input.send_keys('123')

        self.page.find(self.page.locators.USER_INFO_POPUP_APPLY_BUTTON).click()

        assert self.page.get_attribute(
            self.page.locators.VALIDATION_RESULT_MSG, 'innerText') == (
            'Пароль должен содержать минимум 6 символов')

    def test_change_password_incorrect_small_str_2(self):
        self.loginPage.loginProfile()

        self.page.click(self.page.locators.CHANGE_PASSWORD_BUTTON)
        input = self.page.find(self.page.locators.CURRENT_PASSWORD_INPUT)
        input.send_keys(self.password[:3])

        input = self.page.find(self.page.locators.NEW_PASSWORD_INPUT)
        input.send_keys(self.password)

        input = self.page.find(self.page.locators.REPEAT_PASSWORD_INPUT)
        input.send_keys(self.password)

        self.page.find(self.page.locators.USER_INFO_POPUP_APPLY_BUTTON).click()

        assert self.page.get_attribute(
            self.page.locators.VALIDATION_RESULT_MSG, 'innerText') == (
            self.passwordMustContain6SymbolsMessage
        )

    def test_change_password_incorrect_different_str(self):
        self.loginPage.loginProfile()

        self.page.click(self.page.locators.CHANGE_PASSWORD_BUTTON)
        input = self.page.find(self.page.locators.CURRENT_PASSWORD_INPUT)
        input.send_keys(BaseCase.PASSWORD)

        input = self.page.find(self.page.locators.NEW_PASSWORD_INPUT)
        input.send_keys(self.password)

        input = self.page.find(self.page.locators.REPEAT_PASSWORD_INPUT)
        input.send_keys(self.password[::-1])

        self.page.find(self.page.locators.USER_INFO_POPUP_APPLY_BUTTON).click()

        assert self.page.get_attribute(
            self.page.locators.VALIDATION_RESULT_MSG, 'innerText') == (
            self.passwordsUnmatch
        )

    def test_change_password_incorrect_wrong_password(self):
        self.loginPage.loginProfile()

        self.page.click(self.page.locators.CHANGE_PASSWORD_BUTTON)
        input = self.page.find(self.page.locators.CURRENT_PASSWORD_INPUT)
        input.send_keys(self.password)

        input = self.page.find(self.page.locators.NEW_PASSWORD_INPUT)
        input.send_keys(self.password)

        input = self.page.find(self.page.locators.REPEAT_PASSWORD_INPUT)
        input.send_keys(self.password)

        self.page.find(self.page.locators.USER_INFO_POPUP_APPLY_BUTTON).click()

        assert self.page.get_attribute(self.page.locators.SERVER_ERROR_MSG, 'innerText') == (
            self.oldPasswordIncorrectMessage
        )

    def test_change_password_correct_str(self):
        self.loginPage.loginProfile()
        self.page.change_password(BaseCase.PASSWORD_PROFILE, '123456')

        self.page.logout()
        self.loginPage.header.findLoginPageButton().click()
        self.loginPage.loginData(BaseCase.EMAIL_PROFILE, BaseCase.PASSWORD_PROFILE)

        errorMsg = self.page.get_attribute(
            self.page.locators.VALIDATION_RESULT_MSG, 'innerText')

        default_password = BaseCase.PASSWORD_PROFILE
        BaseCase.PASSWORD_PROFILE = '123456'

        self.loginPage.loginProfile()
        BaseCase.PASSWORD_PROFILE = default_password
        self.page.change_password('123456', BaseCase.PASSWORD_PROFILE)

        assert errorMsg == 'Неверная почта или пароль'

    def test_payment_card_correct_params(self):
        self.loginPage.loginProfile()

        self.page.click(self.page.locators.ADD_PAYMENT_CARD)
        self.page.send_keys(
            self.page.locators.PAYMENT_CARD_NUMBER_INPUT, '1111222233334444')
        self.page.send_keys(self.page.locators.PAYMENT_CARD_MONTH_INPUT, '02')
        self.page.send_keys(self.page.locators.PAYMENT_CARD_YEAR_INPUT, '30')
        self.page.send_keys(self.page.locators.PAYMENT_CARD_CVC_INPUT, '123')

        self.page.find(self.page.locators.PAYMENT_CARD_APPLY_BUTTON).click()

        assert self.page.get_attribute(
            self.page.locators.PAYMENT_CARD_NUMBER, 'innerText') == '1111222233334444'

        self.page.click(self.page.locators.PAYMENT_CARD_NUMBER)
        self.page.click(self.page.locators.DELETE_PAYMENT_CARD)

    def test_payment_card_incorrect_params_number(self):
        self.loginPage.loginProfile()

        self.page.click(self.page.locators.ADD_PAYMENT_CARD)
        self.page.send_keys(
            self.page.locators.PAYMENT_CARD_NUMBER_INPUT, self.houseNumber)

        self.page.find(self.page.locators.PAYMENT_CARD_APPLY_BUTTON).click()

        assert self.page.get_attribute(
            self.page.locators.SERVER_ERROR_MSG, 'innerText') == 'Номер карты состоит из 16 цифр. 1/16'

    def test_payment_card_incorrect_params_date(self):
        self.loginPage.loginProfile()

        self.page.click(self.page.locators.ADD_PAYMENT_CARD)
        self.page.send_keys(
            self.page.locators.PAYMENT_CARD_NUMBER_INPUT, '1111222233334444')
        self.page.send_keys(self.page.locators.PAYMENT_CARD_MONTH_INPUT, '02')
        self.page.send_keys(self.page.locators.PAYMENT_CARD_YEAR_INPUT, '2020')
        self.page.find(self.page.locators.PAYMENT_CARD_APPLY_BUTTON).click()

        assert self.page.get_attribute(
            self.page.locators.SERVER_ERROR_MSG, 'innerText').strip() == 'Срок действия карты истек'

    def test_payment_card_incorrect_params_date_expiration(self):
        self.loginPage.loginProfile()

        self.page.click(self.page.locators.ADD_PAYMENT_CARD)
        self.page.send_keys(
            self.page.locators.PAYMENT_CARD_NUMBER_INPUT, '1111222233334444')

        self.page.find(self.page.locators.PAYMENT_CARD_APPLY_BUTTON).click()

        assert self.page.get_attribute(
            self.page.locators.SERVER_ERROR_MSG, 'innerText').strip() == 'Срок действия карты формата 09/25'

    def test_payment_card_incorrect_params_date_wrong_month(self):
        self.loginPage.loginProfile()

        self.page.click(self.page.locators.ADD_PAYMENT_CARD)
        self.page.send_keys(
            self.page.locators.PAYMENT_CARD_NUMBER_INPUT, '1111222233334444')
        self.page.send_keys(self.page.locators.PAYMENT_CARD_MONTH_INPUT, '15')
        self.page.send_keys(self.page.locators.PAYMENT_CARD_YEAR_INPUT, '30')

        self.page.find(self.page.locators.PAYMENT_CARD_APPLY_BUTTON).click()

        assert self.page.get_attribute(
            self.page.locators.SERVER_ERROR_MSG, 'innerText').strip() == 'Месяц не может быть больше 12'

    def test_payment_card_incorrect_params_cvc(self):
        self.loginPage.loginProfile()

        self.page.click(self.page.locators.ADD_PAYMENT_CARD)
        self.page.send_keys(
            self.page.locators.PAYMENT_CARD_NUMBER_INPUT, '1111222233334444')
        self.page.send_keys(self.page.locators.PAYMENT_CARD_MONTH_INPUT, '10')
        self.page.send_keys(self.page.locators.PAYMENT_CARD_YEAR_INPUT, '30')
        self.page.send_keys(self.page.locators.PAYMENT_CARD_CVC_INPUT, '0')
        self.page.find(self.page.locators.PAYMENT_CARD_APPLY_BUTTON).click()

        assert self.page.get_attribute(
            self.page.locators.SERVER_ERROR_MSG, 'innerText').strip() == 'CVC код содержит 3 цифры'

    def test_address_card_correct_params_with_flat(self):
        self.loginPage.loginProfile()

        self.page.click(self.page.locators.ADD_ADDRESS_CARD)
        self.page.send_keys(self.page.locators.ADDRESS_CARD_CITY_INPUT, 'Moscow')
        self.page.send_keys(
            self.page.locators.ADDRESS_CARD_STREET_INPUT, self.streetRedSquare)
        self.page.send_keys(self.page.locators.ADDRESS_CARD_HOUSE_INPUT, self.houseNumber)
        self.page.click(self.page.locators.ADDRESS_CARD_APPLY_BUTTON)

        assert self.page.get_attribute(
            self.page.locators.ADDRESS_CARD_STREET_TEXT, 'innerText') == (
            self.streetRedSquare)

        self.page.click(self.page.locators.ADDRESS_CARD)
        self.page.click(self.page.locators.DELETE_ADDRESS_CARD)

    def test_address_card_correct_params_without_flat(self):
        self.loginPage.loginProfile()

        self.page.click(self.page.locators.ADD_ADDRESS_CARD)
        self.page.send_keys(self.page.locators.ADDRESS_CARD_CITY_INPUT, 'Moscow')
        self.page.send_keys(
            self.page.locators.ADDRESS_CARD_STREET_INPUT, self.streetRedSquare)
        self.page.send_keys(self.page.locators.ADDRESS_CARD_HOUSE_INPUT, self.houseNumber)
        self.page.send_keys(self.page.locators.ADDRESS_CARD_FLAT_INPUT, '15')
        self.page.click(self.page.locators.ADDRESS_CARD_APPLY_BUTTON)

        assert self.page.get_attribute(
            self.page.locators.ADDRESS_CARD_STREET_TEXT, 'innerText') == self.streetRedSquare

        self.page.click(self.page.locators.ADDRESS_CARD)
        self.page.click(self.page.locators.DELETE_ADDRESS_CARD)

    def test_address_card_incorrect_params_city(self):
        self.loginPage.loginProfile()

        self.page.click(self.page.locators.ADD_ADDRESS_CARD)
        self.page.click(self.page.locators.ADDRESS_CARD_APPLY_BUTTON)

        assert self.page.get_attribute(
            self.page.locators.SERVER_ERROR_MSG, 'innerText').strip() == 'Введите ваш город'

    def test_address_card_incorrect_params_street(self):
        self.loginPage.loginProfile()

        self.page.click(self.page.locators.ADD_ADDRESS_CARD)
        self.page.send_keys(self.page.locators.ADDRESS_CARD_CITY_INPUT, 'Moscow')
        self.page.click(self.page.locators.ADDRESS_CARD_APPLY_BUTTON)

        assert self.page.get_attribute(
            self.page.locators.SERVER_ERROR_MSG, 'innerText').strip() == 'Введите вашу улицу'

    def test_address_card_incorrect_params_house(self):
        self.loginPage.loginProfile()

        self.page.click(self.page.locators.ADD_ADDRESS_CARD)
        self.page.send_keys(self.page.locators.ADDRESS_CARD_CITY_INPUT, 'Moscow')
        self.page.send_keys(
            self.page.locators.ADDRESS_CARD_STREET_INPUT, self.streetRedSquare)
        self.page.click(self.page.locators.ADDRESS_CARD_APPLY_BUTTON)

        assert self.page.get_attribute(
            self.page.locators.SERVER_ERROR_MSG, 'innerText').strip() == 'Введите ваш дом'

    def test_address_card_edit_params(self):
        self.loginPage.loginProfile()

        self.page.click(self.page.locators.ADD_ADDRESS_CARD)
        self.page.send_keys(self.page.locators.ADDRESS_CARD_CITY_INPUT, 'Moscow')
        self.page.send_keys(
            self.page.locators.ADDRESS_CARD_STREET_INPUT, self.streetRedSquare)
        self.page.send_keys(self.page.locators.ADDRESS_CARD_HOUSE_INPUT, self.houseNumber)
        self.page.send_keys(self.page.locators.ADDRESS_CARD_FLAT_INPUT, '15')
        self.page.click(self.page.locators.ADDRESS_CARD_APPLY_BUTTON)

        self.page.click(self.page.locators.ADDRESS_CARD)
        self.page.click(self.page.locators.EDIT_ADDRESS_CARD)
        self.page.find(self.page.locators.ADDRESS_CARD_STREET_INPUT).clear()
        self.page.send_keys(
            self.page.locators.ADDRESS_CARD_STREET_INPUT, self.streetArbat)
        self.page.click(self.page.locators.ADDRESS_CARD_APPLY_BUTTON)

        assert self.page.get_attribute(
            self.page.locators.ADDRESS_CARD_STREET_TEXT, 'innerText') == self.streetArbat

        self.page.click(self.page.locators.ADDRESS_CARD)
        self.page.click(self.page.locators.DELETE_ADDRESS_CARD)

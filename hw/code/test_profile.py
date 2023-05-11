import pytest
from ui.pages.profile_page import ProfilePage
from ui.locators.locators import LoginLocators
from ui.base_case.base_case import BaseCase
import os
import time


class TestProfileWithoutAuth(BaseCase):
    PATH = 'user'

    @pytest.fixture(scope="function", autouse=True)
    def set_page(self, driver, url_config):
        self.driver = driver
        self.page = ProfilePage(driver, url_config)

    def test_no_auth_message(self):
        assert str(self.page.get_attribute(
            self.page.locators.MUST_AUTH_MESSAGE, 'innerText')) == 'Войдите'


class TestProfile(BaseCase):
    PATH = 'user'

    @pytest.fixture(scope="function", autouse=True)
    def set_page(self, driver, url_config):
        self.driver = driver
        self.page = ProfilePage(driver, url_config)

    def test_title(self):
        self.page.login()
        assert self.driver.title == 'Ваши данные - Reazon'

    def test_render_with_auth(self):
        self.page.login()
        assert self.page.get_attribute(
            self.page.locators.CHANGE_PASSWORD_BUTTON, 'innerText') != None

    def test_default_avatar(self):
        self.page.login()

        assert self.page.get_attribute(
            self.page.locators.USER_AVATAR, 'src').strip() == 'https://www.reazon.ru/img/UserPhoto.webp'

    def test_change_avatar(self):
        self.page.login()
        img_input = self.page.find(self.page.locators.CHANGE_AVATAR_INPUT)
        img_input.send_keys(os.getcwd() + '/hw/code/ui/prikol.jpg')

        assert self.page.get_attribute(
            self.page.locators.USER_AVATAR, 'src') != 'https://www.reazon.ru/img/UserPhoto.webp/'

        self.page.click(self.page.locators.USER_AVATAR)
        self.page.click(self.page.locators.DELETE_AVATAR_BUTTON)


    def test_change_name_not_empty_str(self):
        self.page.login()

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
        self.page.login()

        self.page.click(self.page.locators.CHANGE_NAME_BUTTON)
        self.page.find(self.page.locators.USER_INFO_POPUP_APPLY_BUTTON).click()

        assert self.page.get_attribute(
            self.page.locators.VALIDATION_RESULT_MSG, 'innerText') == 'Поле обязательно должно быть заполнено'

    def test_change_email_empty_str(self):
        self.page.login()

        self.page.click(self.page.locators.CHANGE_EMAIL_BUTTON)
        self.page.find(self.page.locators.USER_INFO_POPUP_APPLY_BUTTON).click()

        assert self.page.get_attribute(
            self.page.locators.VALIDATION_RESULT_MSG, 'innerText') == 'Поле обязательно должно быть заполнено'

    def test_change_email_incorrect_str(self):
        self.page.login()

        self.page.click(self.page.locators.CHANGE_EMAIL_BUTTON)
        input = self.page.find(self.page.locators.CHANGE_EMAIL_INPUT)

        input.send_keys('test')
        self.page.find(self.page.locators.USER_INFO_POPUP_APPLY_BUTTON).click()

        assert self.page.get_attribute(
            self.page.locators.VALIDATION_RESULT_MSG, 'innerText') == 'Неверный формат почты'

    def test_change_phone_empty_str(self):
        self.page.login()

        self.page.click(self.page.locators.CHANGE_PHONE_BUTTON)
        self.page.find(self.page.locators.CHANGE_PHONE_INPUT).clear()

        self.page.find(self.page.locators.USER_INFO_POPUP_APPLY_BUTTON).click()

        assert self.page.get_attribute(
            self.page.locators.VALIDATION_RESULT_MSG, 'innerText') == 'Поле обязательно должно быть заполнено'

    def test_change_phone_incorrect_str(self):
        self.page.login()

        self.page.click(self.page.locators.CHANGE_PHONE_BUTTON)
        input = self.page.find(self.page.locators.CHANGE_PHONE_INPUT)

        input.send_keys('123')
        self.page.find(self.page.locators.USER_INFO_POPUP_APPLY_BUTTON).click()

        assert self.page.get_attribute(
            self.page.locators.VALIDATION_RESULT_MSG, 'innerText') == 'Телефон должен содержать 11 цифр. Введено 4/11'

    def test_change_phone_correct_str(self):
        self.page.login()

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
        self.page.login()

        self.page.click(self.page.locators.CHANGE_PASSWORD_BUTTON)

        self.page.find(self.page.locators.USER_INFO_POPUP_APPLY_BUTTON).click()

        assert self.page.get_attribute(
            self.page.locators.VALIDATION_RESULT_MSG, 'innerText') == 'Поле обязательно должно быть заполнено'

    def test_change_password_incorrect_small_str(self):
        self.page.login()

        self.page.click(self.page.locators.CHANGE_PASSWORD_BUTTON)
        input = self.page.find(self.page.locators.CURRENT_PASSWORD_INPUT)
        input.send_keys(BaseCase.PASSWORD)

        input = self.page.find(self.page.locators.NEW_PASSWORD_INPUT)
        input.send_keys('123')

        self.page.find(self.page.locators.USER_INFO_POPUP_APPLY_BUTTON).click()

        assert self.page.get_attribute(
            self.page.locators.VALIDATION_RESULT_MSG, 'innerText') == 'Пароль должен содержать минимум 6 символов'

    def test_change_password_incorrect_small_str_2(self):
        self.page.login()

        self.page.click(self.page.locators.CHANGE_PASSWORD_BUTTON)
        input = self.page.find(self.page.locators.CURRENT_PASSWORD_INPUT)
        input.send_keys('123')

        input = self.page.find(self.page.locators.NEW_PASSWORD_INPUT)
        input.send_keys('123456')

        input = self.page.find(self.page.locators.REPEAT_PASSWORD_INPUT)
        input.send_keys('123456')

        self.page.find(self.page.locators.USER_INFO_POPUP_APPLY_BUTTON).click()

        assert self.page.get_attribute(
            self.page.locators.VALIDATION_RESULT_MSG, 'innerText') == 'Пароль должен содержать минимум 6 символов'

    def test_change_password_incorrect_different_str(self):
        self.page.login()

        self.page.click(self.page.locators.CHANGE_PASSWORD_BUTTON)
        input = self.page.find(self.page.locators.CURRENT_PASSWORD_INPUT)
        input.send_keys(BaseCase.PASSWORD)

        input = self.page.find(self.page.locators.NEW_PASSWORD_INPUT)
        input.send_keys('123456')

        input = self.page.find(self.page.locators.REPEAT_PASSWORD_INPUT)
        input.send_keys('654321')

        self.page.find(self.page.locators.USER_INFO_POPUP_APPLY_BUTTON).click()

        assert self.page.get_attribute(
            self.page.locators.VALIDATION_RESULT_MSG, 'innerText') == 'Введенные пароли не совпадают'

    def test_change_password_incorrect_wrong_password(self):
        self.page.login()

        self.page.click(self.page.locators.CHANGE_PASSWORD_BUTTON)
        input = self.page.find(self.page.locators.CURRENT_PASSWORD_INPUT)
        input.send_keys('123456')

        input = self.page.find(self.page.locators.NEW_PASSWORD_INPUT)
        input.send_keys('123456')

        input = self.page.find(self.page.locators.REPEAT_PASSWORD_INPUT)
        input.send_keys('123456')

        self.page.find(self.page.locators.USER_INFO_POPUP_APPLY_BUTTON).click()

        assert self.page.get_attribute(
            self.page.locators.SERVER_ERROR_MSG, 'innerText') == 'Старый пароль не верный'




    def test_payment_card_correct_params(self):
        self.page.login()

        self.page.click(self.page.locators.ADD_PAYMENT_CARD)
        self.page.send_keys(self.page.locators.PAYMENT_CARD_NUMBER_INPUT, '1111222233334444')
        self.page.send_keys(self.page.locators.PAYMENT_CARD_MONTH_INPUT, '02')
        self.page.send_keys(self.page.locators.PAYMENT_CARD_YEAR_INPUT, '2030')
        self.page.send_keys(self.page.locators.PAYMENT_CARD_CVC_INPUT, '123')

        self.page.find(self.page.locators.PAYMENT_CARD_APPLY_BUTTON).click()

        assert self.page.get_attribute(
            self.page.locators.PAYMENT_CARD_NUMBER, 'innerText') == '1111222233334444'
        
    def test_payment_card_correct_params(self):
        self.page.login()

        self.page.click(self.page.locators.ADD_PAYMENT_CARD)
        self.page.send_keys(self.page.locators.PAYMENT_CARD_NUMBER_INPUT, '1111222233334444')
        self.page.send_keys(self.page.locators.PAYMENT_CARD_MONTH_INPUT, '02')
        self.page.send_keys(self.page.locators.PAYMENT_CARD_YEAR_INPUT, '2030')
        self.page.send_keys(self.page.locators.PAYMENT_CARD_CVC_INPUT, '123')

        self.page.find(self.page.locators.PAYMENT_CARD_APPLY_BUTTON).click()

        assert self.page.get_attribute(
            self.page.locators.PAYMENT_CARD_NUMBER, 'innerText') == '1111222233334444'
        
        
    def test_payment_card_incorrect_params_number(self):
        self.page.login()

        self.page.click(self.page.locators.ADD_PAYMENT_CARD)
        self.page.send_keys(self.page.locators.PAYMENT_CARD_NUMBER_INPUT, '1')

        self.page.find(self.page.locators.PAYMENT_CARD_APPLY_BUTTON).click()

        assert self.page.get_attribute(
            self.page.locators.SERVER_ERROR_MSG, 'innerText') == 'Номер карты состоит из 16 цифр. 1/16'
        

    def test_payment_card_incorrect_params_date(self):
        self.page.login()

        self.page.click(self.page.locators.ADD_PAYMENT_CARD)
        self.page.send_keys(self.page.locators.PAYMENT_CARD_NUMBER_INPUT, '1111222233334444')
        self.page.send_keys(self.page.locators.PAYMENT_CARD_MONTH_INPUT, '02')
        self.page.send_keys(self.page.locators.PAYMENT_CARD_YEAR_INPUT, '2020')
        self.page.find(self.page.locators.PAYMENT_CARD_APPLY_BUTTON).click()

        assert self.page.get_attribute(
            self.page.locators.SERVER_ERROR_MSG, 'innerText') == 'Срок действия карты формата 09/25'
        
    def test_payment_card_incorrect_params_date(self):
        self.page.login()

        self.page.click(self.page.locators.ADD_PAYMENT_CARD)
        self.page.send_keys(self.page.locators.PAYMENT_CARD_NUMBER_INPUT, '1111222233334444')

        self.page.find(self.page.locators.PAYMENT_CARD_APPLY_BUTTON).click()

        assert self.page.get_attribute(
            self.page.locators.SERVER_ERROR_MSG, 'innerText') == 'Срок действия карты истек'


    def test_payment_card_incorrect_params_date(self):
        self.page.login()

        self.page.click(self.page.locators.ADD_PAYMENT_CARD)
        self.page.send_keys(self.page.locators.PAYMENT_CARD_NUMBER_INPUT, '1111222233334444')
        self.page.send_keys(self.page.locators.PAYMENT_CARD_MONTH_INPUT, '15')

        self.page.find(self.page.locators.PAYMENT_CARD_APPLY_BUTTON).click()

        assert self.page.get_attribute(
            self.page.locators.SERVER_ERROR_MSG, 'innerText') == 'Месяц не может быть больше 12'
        

    def test_payment_card_incorrect_params_date(self):
        self.page.login()

        self.page.click(self.page.locators.ADD_PAYMENT_CARD)
        self.page.send_keys(self.page.locators.PAYMENT_CARD_NUMBER_INPUT, '1111222233334444')
        self.page.send_keys(self.page.locators.PAYMENT_CARD_CVC_INPUT, '0')
        self.page.find(self.page.locators.PAYMENT_CARD_APPLY_BUTTON).click()

        assert self.page.get_attribute(
            self.page.locators.SERVER_ERROR_MSG, 'CVC код содержит 3 цифры')
    
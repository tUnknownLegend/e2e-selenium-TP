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

        assert self.page.get_attribute(
            self.page.locators.SERVER_ERROR_MSG, 'innerText') == (
            self.oldPasswordIncorrectMessage
        )

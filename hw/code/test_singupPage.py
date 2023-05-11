from ui.pages.signup_page import SignupPage
from ui.fixtures import get_driver
from ui.pages.header import Header
import uuid


class Case2:
    def __init__(self, usname, email, password, password2, message = ''):
        self.usname = usname
        self.email = email
        self.password = password
        self.password2 = password2
        self.message = message

class TestSignup():
    driver = get_driver(browser_name='chrome')
    signupPage = SignupPage(driver)
    header = Header(driver)

    failCases = [
        Case2("", "b", "c", "d", "Поле обязательно должно быть заполнено"),
        Case2("a", "", "c", "d", "Поле обязательно должно быть заполнено"),
        Case2("a", "b", "c", "d", "Неверный формат почты"),
        Case2("a", "b@test", "", "d", "Поле обязательно должно быть заполнено"),
        Case2("a", "b@test", "12", "d", "Пароль должен содержать минимум 6 символов"),
        Case2("a", "b@test", "123456", "", "Введенные пароли не совпадают"),
        Case2("a", "b@test", "123456", "123457", "Введенные пароли не совпадают"),
        Case2("a", "test@test", "123457", "123457", "Неверная почта или пароль"),
     ]
    
    @signupPage.render_decorator
    def test_redirect(self):
        self.signupPage.find(self.signupPage.locators.SIGNIN_LINK).click()
        assert self.driver.current_url == "https://www.reazon.ru/login"
        self.signupPage.render(self.signupPage.url)

    @signupPage.render_decorator
    def test_title(self):
        title = 'Регистрация - Reazon'
        assert self.driver.title == title

    @signupPage.render_decorator
    def test_fail(self):
        for case in self.failCases:
            self.signupPage.signup(case.usname, case.email, case.password, case.password2)
            assert self.signupPage.find(self.signupPage.locators.ERROR).text == case.message

    @signupPage.render_decorator
    def test_ok(self):
        uid = uuid.uuid4()
        test_email = "test@" + str(uid.int)
        self.signupPage.signup("a", test_email, "123456", "123456")
        self.signupPage.waitUntilVisible(self.signupPage.homeLocators.GET_CATEGORIES_CONTAINER)
        assert self.driver.current_url == "https://www.reazon.ru/"
        self.header.findUserPageButton()
        self.header.logout()

   


from ui.pages.login_page import LoginPage
from ui.fixtures import get_driver


class Case:
    def __init__(self, email, password, message = ''):
        self.email = email
        self.password = password
        self.message = message

class TestLogin():
    driver = get_driver(browser_name='chrome')
    loginPage = LoginPage(driver)

    failCases = [
         Case("a", "b", "Неверный формат почты"  )
     ]

    @loginPage.render_decorator
    def test_fail(self):
        for case in self.failCases:
            self.loginPage.login(case.email, case.password)
            assert self.loginPage.find(self.loginPage.locators.ERROR).text == case.message


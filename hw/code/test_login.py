from ui.fixtures import get_driver
from ui.pages.login_page import LoginPage
from ui.pages.header import Header


class TestLogin():
    driver = get_driver('chrome')

    def test_login(self):
        login_page = LoginPage(self.driver)

        login_page.render_page()

        header = Header(self.driver)
        header.findLoginPageButton()

        login_page.login()

        header.findUserPageButton()

import allure
# import pytest

from ui.fixtures import get_driver
from ui.pages.login_page import LoginPage
from ui.pages.header import Header


# @pytest.mark.skip('skip')
class TestLogin():
    driver = get_driver(browser_name='chrome')
    login_page = LoginPage(driver)

    @allure.feature('Test Login')
    @allure.story('Login')
    def test_login(self):
        self.login_page.render_page()

        header = Header(self.driver)
        header.findLoginPageButton()

        self.login_page.login()

        header.findUserPageButton()

import allure
import pytest

from ui.fixtures import get_driver
from ui.pages.view_comment import ViewComment
from ui.pages.login_page import LoginPage
from ui.pages.header import Header


@pytest.mark.skip('skip')
class TestViewComment():
    driver = get_driver(browser_name='chrome')
    viewComment = ViewComment(driver)
    loginPage = LoginPage(driver)
    header = Header(driver)

    @allure.feature('Auth add comment button')
    @allure.story('check error message')
    @viewComment.render_decorator
    def test_auth_add_comment_button(self):
        with allure.step('login'):
            self.loginPage.render_page()
            self.loginPage.login()

        with allure.step('checkErrorAddComment'):
            self.viewComment.render_page()
            self.viewComment.checkErrorAddComment()

        with allure.step('logout'):
            self.header.logout()

    @allure.feature('Unauth add comment button')
    @allure.story('check redirect')
    @viewComment.render_decorator
    def test_unauth_add_comment_button(self):
        self.viewComment.checkUnauthAddComment()

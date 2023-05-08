from ui.locators import locators
from ui.pages.base_page import BasePage
from ui.paths import paths


class AuthorizePage(BasePage):
    locators = locators.AuthorizeLocators
    PATH = paths.AUTHORIZE

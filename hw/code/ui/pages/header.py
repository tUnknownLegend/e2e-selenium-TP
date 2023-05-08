from ui.pages.base_page import BasePage
from ui.locators.header_locators import HeaderLocators
from ui.locators.catalog_locators import CatalogLocators


class Header(BasePage):

    def __init__(self, driver):
        super(Header, self).__init__(driver)
        self.locators = HeaderLocators()
        self.url = self.domain + self.locators.hrefs.home

    categoryLocators = CatalogLocators()

    def findLoginPageButton(self):
        return self.find(self.locators.OPEN_LOGIN_PAGE_BUTTON)

    def findUserPageButton(self):
        return self.find(self.locators.OPEN_USER_PAGE_BUTTON)

    def findLogOutPopUp(self):
        return self.find(self.locators.SIGN_OUT_POP_UP)

    def hoverOverLogout(self):
        logOutPopUp = self.findLogOutPopUp()

        assert logOutPopUp.value_of_css_property(
            "display") == 'none'

        self.hover(self.findUserPageButton())

        assert logOutPopUp.value_of_css_property(
            "display") == 'block'

        return logOutPopUp

    def logout(self):
        self.hoverOverLogout().click()

    def findFavouritesPageButton(self):
        return self.find(self.locators.OPEN_FAVOURITES_PAGE_BUTTON)

    def findCartPageButton(self):
        return self.find(self.locators.OPEN_CART_PAGE_BUTTON)

    def findOrdersPageButton(self):
        return self.find(self.locators.OPEN_ORDERS_PAGE_BUTTON)

    def selectCategory(self):
        self.waitUntilInvisible(self.locators.GET_CATEGORIES_CONTAINER, 1)

        self.find(self.locators.OPEN_CATEGORY_SELECTOR_BUTTON).click()

        categories = self.find(self.locators.GET_CATEGORIES_CONTAINER)

        for index in range(int(categories.get_attribute('childElementCount'))):
            category = self.find(self.locators.CATEGORY_SELECTOR_MENU(index + 1))
            category.click()
            self.waitUntilInvisible(self.locators.GET_CATEGORIES_CONTAINER, 1)

            assert self.getInnerText(
                self.categoryLocators.GET_CATEGORY_NAME
            ) == category.get_attribute('innerText')

            self.find(self.locators.OPEN_CATEGORY_SELECTOR_BUTTON).click()

    def findLogo(self):
        assert self.getHref(self.locators.GET_LOGO) == '/'

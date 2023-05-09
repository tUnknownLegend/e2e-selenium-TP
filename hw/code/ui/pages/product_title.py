from ui.pages.base_page import BasePage
from ui.locators.login_locators import LoginPageLocators
from ui.locators.product_title_locators import ProductTitleLocators
from ui.locators.header_locators import HeaderLocators
from ui.locators.favourites_locators import FavouritesLocators


class ProductTitle(BasePage):
    loginLocators = LoginPageLocators()
    headerLocators = HeaderLocators()
    favouriteLocators = FavouritesLocators()

    def __init__(self, driver):
        super(ProductTitle, self).__init__(driver)
        self.locators = ProductTitleLocators()
        self.url = self.locators.hrefs.domain + self.locators.hrefs.product + '/43'

    def checkTabTitle(self):
        self.getTabTitle() == self.getInnerText(
            self.locators.GET_PRODUCT_TITLE) + ' - Reazon'

    def checkLinkInTheTitles(self):
        self.is_opened(self.getHref(self.locators.GET_PRODUCT_TITLE))

    def checkCategoryLink(self):
        assert self.locators.hrefs.category in self.getHref(
            self.locators.GET_CATEGORY_BUTTON)

    def unauthFavourites(self):
        favouritesLabel = self.find(self.locators.GET_FAVOURITES_LABEL)

        assert not favouritesLabel.get_attribute('checked')

        favouritesLabel.click()

        assert not favouritesLabel.get_attribute('checked')

        self.checkErrorMessage('Войдите, чтобы добавить в избранное')

        assert not self.find(
            self.locators.GET_FAVOURITES_LABEL).get_attribute('checked')

    def authFavourites(self):
        favouritesInput = self.find(self.locators.GET_FAVOURITES_INPUT)

        if not favouritesInput.get_attribute('checked'):
            self.find(self.locators.GET_FAVOURITES_LABEL).click()
            assert favouritesInput.get_attribute('checked')

        else:
            self.find(self.locators.GET_FAVOURITES_LABEL).click()
            assert not favouritesInput.get_attribute('checked')

    def checkItemPhoto(self):
        self.checkPhoto(self.locators.GET_PHOTO)

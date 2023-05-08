import math

from ui.pages.base_page import BasePage
from ui.locators.login_locators import LoginPageLocators
from ui.locators.product_locators import ProductLocators


class ProductPage(BasePage):
    loginLocators = LoginPageLocators()
    locators = ProductLocators()

    def __init__(self, driver):
        super(ProductPage, self).__init__(driver)
        self.url = self.domain + self.locators.hrefs.product + '/43'

    def checkTabTitle(self):
        self.getTabTitle() == self.getInnerText(
            self.locators.GET_PRODUCT_TITLE) + ' - Reazon'

    def checkLinkInTheTitles(self):
        self.is_opened(self.domain +
                       self.getHref(self.locators.GET_PRODUCT_TITLE))

    def checkCategoryLink(self):
        assert 'category/' in self.find(self.locators.GET_CATEGORY_BUTTON)

    def checkRatingNumber(self):
        rating = float(self.getInnerText(self.locators.GET_RATING_NUMBER))

        assert math.ceil(rating / 10)
        assert int(rating * 10) % 1 == 0

    def checkLinkInRating(self):
        assert self.domain + \
            self.locators.hrefs.comment in self.getHref(self.locators.GET_RATING_LINK)

    def unauthFavourites(self):
        self.find(self.locators.GET_FAVOURITES_LABEL).click()

        self.checkErrorMessage('Войдите, чтобы добавить в избранное')

        assert not self.find(
            self.locators.GET_FAVOURITES_LABEL).get_attribute('checked')

    def authFavourites(self):
        favouritesLabel = self.find(self.locators.GET_FAVOURITES_LABEL)

        isChecked = self.find(
            self.locators.GET_FAVOURITES_LABEL).get_attribute('checked')

        favouritesLabel.click()

        assert isChecked or favouritesLabel.get_attribute('checked')

        self.checkErrorMessage('Войдите, чтобы добавить в избранное')

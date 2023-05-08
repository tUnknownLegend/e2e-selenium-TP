from ui.pages.base_page import BasePage


class CartCountChange(BasePage):

    def __init__(self, driver, selectors):
        super(CartCountChange, self).__init__(driver)
        self.locators = selectors
        self.url = self.domain + self.locators.hrefs.product + '/43'

    def checkButtonLabel(self):
        assert self.getInnerText(
            self.locators.GET_COUNT_CONTAINER) == 'В корзину'

    def getAddDefaultButton(self):
        return self.find(
            self.locators.GET_COUNT_CONTAINER)

    def getPlusButton(self):
        return self.find(self.locators.GET_PLUS_BUTTON)

    def getMinusButton(self):
        return self.find(self.locators.GET_MINUS_BUTTON)

    def getCountOfItemInCart(self):
        return self.getInnerText(
            self.locators.GET_ITEM_COUNT_IN_CART)

    def checkNumberOfItemsInCart(self, number):
        assert int(self.getCountOfItemInCart()) == number

from ui.pages.orders_page import OrdersPage
from ui.fixtures import get_driver
from ui.pages.header import Header


class TestOrders():
    driver = get_driver(browser_name='chrome')
    ordersPage = OrdersPage(driver)
    header = Header(driver)

    @ordersPage.render_decorator
    def test_title(self):
        title = 'Заказы - Reazon'
        assert self.driver.title == title

    @ordersPage.render_decorator
    def test_no_auth(self):
        self.ordersPage.render(self.ordersPage.url)
        assert self.ordersPage.find(self.ordersPage.locators.BUTTON_NO_AUTH_REDIRECT).is_displayed()

    @ordersPage.render_decorator
    def test_empty_orders(self):
        self.ordersPage.authorize("test2@test", "123456")
        self.ordersPage.render(self.ordersPage.url)
        assert self.ordersPage.find(self.ordersPage.locators.BUTTON_EMPTY_ORDERS_REDIRECT).is_displayed()
        self.header.findUserPageButton()
        self.header.logout()

    @ordersPage.render_decorator
    def test_button_deny_order(self):
        self.ordersPage.authorize("test@test", "123456")
        self.ordersPage.add_product_after_login()
        self.ordersPage.click(self.ordersPage.locators.BUTTON_MAKE_ORDER)
        self.ordersPage.click(self.ordersPage.locators.BUTTON_DENY_ORDER)
        self.ordersPage.waitUntilInvisible(self.ordersPage.locators.BUTTON_DENY_ORDER)
        #assert self.ordersPage.find(self.ordersPage.locators.ORDER_STATUS2).text() == "Отменен"
        #assert self.ordersPage.find(self.ordersPage.locators.MESSAGE).text == "Заказ успешно отменен"
        self.header.findUserPageButton()
        self.header.logout()

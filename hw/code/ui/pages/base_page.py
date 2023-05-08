import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from ui.locators.base_locators import BaseLocators


class PageNotOpenedExeption(Exception):
    pass


class BasePage(object):
    baseLocators = BaseLocators()

    def is_opened(self, url, timeout=15):
        started = time.time()
        while time.time() - started < timeout:
            if self.driver.current_url == url:
                return True

        raise PageNotOpenedExeption(
            f'{url} did not open in {timeout} sec,' +
            f'current url {self.driver.current_url}')

    def __init__(self, driver):
        self.driver = driver
        self.actions = ActionChains(driver)
        self.domain = 'https://www.reazon.ru'

    def render(self, url):
        self.driver.get(url)

    def render_page(self):
        self.render(self.url)
        self.is_opened(self.url)

    def render_decorator(self, func):
        def wrapper(newSelf):
            self.render_page()
            func(newSelf)
        return wrapper

    def wait(self, timeout=None):
        if timeout is None:
            timeout = 5
        return WebDriverWait(self.driver, timeout=timeout)

    def find(self, locator, timeout=10):
        return self.wait(timeout).until(
            EC.presence_of_element_located(locator))

    def hover(self, element):
        self.actions.move_to_element(element).perform()

    def waitUntilVisible(self, selector, timeout):
        self.wait(timeout).until(EC.presence_of_element_located(selector))

    def waitUntilInvisible(self, selector, timeout):
        self.wait(timeout).until(EC.invisibility_of_element_located(selector))

    def checkErrorMessage(self, errorMessage):
        errorMessageElement = self.find(
            self.baseLocators.HEADER_ERROR_MESSAGE)

        self.waitUntilVisible(self.baseLocators.HEADER_ERROR_MESSAGE, 1)
        assert errorMessageElement.get_attribute('innerText') == errorMessage

        self.waitUntilInvisible(self.baseLocators.HEADER_ERROR_MESSAGE, 6)

    def getTabTitle(self):
        return self.driver.getTitle()

    def getInnerText(self, selector):
        return self.find(selector).get_attribute('innerText')

    def getHref(self, selector):
        return self.find(selector).get_attribute('href')

import time
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import StaleElementReferenceException
import urllib.parse as urlparse
from ui.locators import locators


class PageNotOpenedExeption(Exception):
    pass


class StaleTimeoutExeption(Exception):
    pass


class BasePage(object):
    default_timeout = 20
    mini_timeout = 3
    locators = locators.BasePageLocators()
    PATH = ""

    def is_opened(self, url, timeout=default_timeout):
        started = time.time()
        while time.time() - started < timeout:
            if self.driver.current_url == url:
                return True

        raise PageNotOpenedExeption(f"{url} did not open in {timeout} sec, current url {self.driver.current_url}")

    def __init__(self, driver, url):
        self.driver = driver
        self.action = ActionChains(driver)
        self.BASE_URL = url

    def open(self, timeout=default_timeout):
        url = urlparse.urljoin(self.BASE_URL, self.PATH)
        self.driver.get(url)
        self.driver.maximize_window()
        self.is_opened(url, timeout)

    def wait(self, timeout=default_timeout):
        return WebDriverWait(self.driver, timeout=timeout)

    def wait_to_be_clickable(self, locator, timeout=default_timeout):
        return self.wait(timeout).until(EC.element_to_be_clickable(locator))

    def send_keys(self, locator, keys, timeout=default_timeout) -> WebElement:
        started = time.time()
        while time.time() - started < timeout:
            try:
                elem = self.wait_to_be_clickable(locator, timeout - (time.time() - started))
                elem.clear()
                elem.send_keys(keys)
                return elem
            except StaleElementReferenceException as Exception:
                pass
        raise StaleTimeoutExeption(
            f"{locator} did not clickable or have been throwing StaleElementReferenceExceptions in {timeout} sec, current url {self.driver.current_url}")

    def click(self, locator, timeout=default_timeout) -> WebElement:
        started = time.time()
        while time.time() - started < timeout:
            try:
                elem = self.wait_to_be_clickable(locator, timeout - (time.time() - started))
                elem.click()
                return elem
            except StaleElementReferenceException as Exception:
                pass
        raise StaleTimeoutExeption(
            f"{locator} did not clickable or have been throwing StaleElementReferenceExceptions in {timeout} sec, current url {self.driver.current_url}")

    def is_url(self, path):
        return EC.url_matches(urlparse.urljoin(self.BASE_URL, path))

    def find(self, locator, timeout=default_timeout):
            return self.wait(timeout).until(EC.presence_of_element_located(locator))
    
    def waitUntilVisible(self, selector, timeout=5):
        self.wait(timeout).until(EC.presence_of_element_located(selector))

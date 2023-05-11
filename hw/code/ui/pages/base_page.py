import time
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import StaleElementReferenceException
import urllib.parse as urlparse
from ui.locators import locators



class PageNotOpenedException(Exception):
    pass


class StaleTimeoutException(Exception):
    pass


class BasePage(object):
    default_timeout = 20
    locators = locators.BasePageLocators()
    PATH = ""

    def is_opened(self, url, timeout=default_timeout):
        started = time.time()
        while time.time() - started < timeout:
            if self.driver.current_url == url:
                return True

        raise PageNotOpenedException(
            f"{url} did not open in {timeout} sec, current url {self.driver.current_url}")

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
    
    def find(self, locator, timeout=default_timeout):
        return self.wait(timeout).until(EC.presence_of_element_located(locator))

    def send_keys(self, locator, keys, timeout=default_timeout) -> WebElement:
        started = time.time()
        while time.time() - started < timeout:
            try:
                elem = self.wait_to_be_clickable(
                    locator, timeout - (time.time() - started))
                elem.clear()
                elem.send_keys(keys)
                return elem
            except StaleElementReferenceException as Exception:
                pass
        raise StaleTimeoutException(
            f"{locator} did not clickable or have been throwing StaleElementReferenceExceptions in {timeout} sec, current url {self.driver.current_url}")

    def click(self, locator, timeout=default_timeout) -> WebElement:
        started = time.time()
        while time.time() - started < timeout:
            try:
                elem = self.wait_to_be_clickable(
                    locator, timeout - (time.time() - started))
                elem.click()
                return elem
            except StaleElementReferenceException as Exception:
                pass
        raise StaleTimeoutException(
            f"{locator} did not clickable or have been throwing StaleElementReferenceExceptions in {timeout} sec, current url {self.driver.current_url}")

    def get_attribute(self, locator, attribute, timeout=default_timeout) -> WebElement:
        started = time.time()
        while time.time() - started < timeout:
            try:
                content = self.find(locator).get_attribute(attribute)
                return content
            except StaleElementReferenceException as Exception:
                pass
        raise StaleTimeoutException(
            f"{locator} did not clickable or have been throwing StaleElementReferenceExceptions in {timeout} sec, current url {self.driver.current_url}")

    def get_text(self, locator, timeout=default_timeout) -> WebElement:
        started = time.time()
        while time.time() - started < timeout:
            try:
                content = self.find(locator).getText()
                return content
            except StaleElementReferenceException as Exception:
                pass
        raise StaleTimeoutException(
            f"{locator} did not clickable or have been throwing StaleElementReferenceExceptions in {timeout} sec, current url {self.driver.current_url}")

    def refresh(self, timeout=default_timeout):
        self.driver.refresh()


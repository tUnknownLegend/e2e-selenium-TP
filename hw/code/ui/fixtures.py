import pytest
import allure
import os

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from ui.pages.base_page import BasePage
from ui.pages.login_page import LoginPage
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService


def _options(headless=False):
    options = Options()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument("--incognito")
    options.add_argument("--disable-gpu")
    options.add_argument('--no-sandbox')
    options.add_argument("--disable-xss-auditor")
    options.add_argument("--disable-web-security")
    options.add_argument("--disable-setuid-sandbox")
    options.add_argument("--disable-webgl")
    options.add_argument("--disable-popup-blocking")
    options.page_load_strategy = 'normal'

    if headless:
        options.add_argument("--headless=new")
        options.add_argument("window-size=1920x1080")

    return options


def get_driver(browser_name):
    headless = True

    if browser_name == 'chrome':
        browser = webdriver.Chrome(
            service=ChromeService(
                executable_path=ChromeDriverManager().install()),
            options=_options(headless=headless))
    elif browser_name == 'firefox':
        browser = webdriver.Firefox(
            service=FirefoxService(
                executable_path=GeckoDriverManager().install()))
    else:
        raise RuntimeError(f'Unsupported browser: "{browser_name}"')

    if headless == True:
        browser.set_window_size(1920, 1080)
    else:
        browser.maximize_window()
    return browser


def ui_report(self, driver, request, temp_dir):
    failed_test_count = request.session.testsfailed
    yield
    if request.session.testsfailed > failed_test_count:
        browser_logs = os.path.join(temp_dir, 'browser.log')
        with open(browser_logs, 'w') as f:
            print(temp_dir)
            for i in driver.get_log('browser'):
                f.write(f"{i['level']} - {i['source']}\n{i['message']}\n")
        screenshot_path = os.path.join(temp_dir, 'failed.png')
        self.driver.save_screenshot(filename=screenshot_path)
        allure.attach.file(screenshot_path, 'failed.png',
                           allure.attachment_type.PNG)
        with open(browser_logs, 'r') as f:
            allure.attach(f.read(), 'test.log',
                          allure.attachment_type.TEXT)


@pytest.fixture(scope='session', params=['chrome', 'firefox'])
def all_drivers(config, request):
    url = config['url']
    browser = get_driver(request.param)
    browser.get(url)
    yield browser
    browser.quit()


@pytest.fixture
def base_page(driver):
    return BasePage(driver=driver)


@pytest.fixture
def main_page(driver):
    return LoginPage(driver=driver)

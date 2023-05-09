import pytest
import allure

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
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

    if headless is True:
        browser.set_window_size(1920, 1080)
    else:
        browser.maximize_window()
    return browser


@pytest.fixture(scope='session', params=['chrome', 'firefox'])
def all_drivers(config, request):
    url = config['url']
    browser = get_driver(request.param)
    browser.get(url)
    yield browser

    if request.node.rep_call.failed:
        browser.execute_script("document.body.bgColor = 'white';")

        allure.attach(browser.get_screenshot_as_png(),
                      name=request.function.__name__,
                      attachment_type=allure.attachment_type.PNG)

    browser.quit()
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from ui.pages.login_page import LoginPage


def get_driver(browser_name):
    if browser_name == "chrome":
        chrome_options = Options()
        chrome_options.add_argument('--no-proxy-server')
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument('--disable-gpu')
        chrome_options.set_capability(
                        "goog:loggingPrefs", {"performance": "ALL", "browser": "ALL"}
                    )
        driver = webdriver.Chrome(service=Service(executable_path=ChromeDriverManager().install()), options=chrome_options)
    elif browser_name == "firefox":
        driver = webdriver.Firefox(service=Service(executable_path=GeckoDriverManager().install()))
    else:
        raise RuntimeError(f'Unsupported browser: "{browser_name}"')

    driver.maximize_window()
    return driver


@pytest.fixture()
def driver(browser_config):
    driver = get_driver(browser_config)
    yield driver
    driver.quit()

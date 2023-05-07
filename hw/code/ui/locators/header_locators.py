from selenium.webdriver.common.by import By


class HeaderLocators():
    OPEN_LOGIN_PAGE_BUTTON = (
        By.XPATH, '//div[@class="header__profile"]/a[@href="/login"]')
    
    OPEN_USER_PAGE_BUTTON = (
        By.XPATH, '//div[@class="header__profile"]/a[@href="/user"]')

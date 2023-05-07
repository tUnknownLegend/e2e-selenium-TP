from selenium.webdriver.common.by import By


class HeaderLocators():
    OPEN_LOGIN_PAGE_BUTTON = (
        By.XPATH, '//div[@class="header__profile"]/a[@href="/login"]')

    OPEN_USER_PAGE_BUTTON = (
        By.XPATH, '//div[@class="header__profile"]/a[@href="/user"]')

    OPEN_CART_PAGE_BUTTON = (
        By.XPATH, '//div[@class="header__card"]/a[@href="/cart"]')

    OPEN_FAVOURITES_PAGE_BUTTON = (
        By.XPATH, '//div[@class="header__favourites"]/a[@href="/user/favorites"]')

    OPEN_ORDERS_PAGE_BUTTON = (
        By.XPATH, '//div[@class="header__order"]/a[@href="/orders"]')

    SIGN_OUT_POP_UP = (
        By.XPATH, '//div[@class="profile__pop-up"]'
    )

    SIGN_OUT_BUTTON_POP_UP = (
        By.XPATH, '//div[@class="profile__pop-up/a[@href="/logout"]"]'
    )

    OPEN_CATEGORY_SELECTOR_BUTTON = (By.ID, 'header__button-catalog')

    CATEGORY_SELECTOR_MENU = (By.ID, 'header__dropdown__content')

    def CATEGORY_SELECTOR_MENU(self, index): return (
        By.XPATH, f'//div[@id="header__dropdown__content"]/a[{index}]')

    GET_CATEGORIES_CONTAINER = (
        By.XPATH, '//div[@id="header__dropdown__content"]')

    GET_LOGO = (By.XPATH, '//div[@class="header__logotip"]/a')

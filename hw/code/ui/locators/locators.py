from selenium.webdriver.common.by import By


class BasePageLocators:
    base = ()

class CartLocators:
    TAB_NAME = (By.XPATH, '/html/head/title')
    EMPTY_CART_MESSAGE = (By.ID, 'content-unAuth-page-redirect')
    EMPTY_CART_MESSAGE_LINK = (By.XPATH, '//div[@id="content-unAuth-page-redirect"]/a')
    BUTTON_CLEAR_CART = (By.ID, 'button-default_cart__delete')
    CHECKBOX_SELECT_ALL = (By.ID, 'item_cart__select-all')
    CHECKBOX_ITEM = (By.XPATH, '//input[@name="itemCart"]')
    ITEM_PRICE = (By.XPATH, '//span[starts-with(@id, "price/")]')
    ITEM_COUNT = (By.XPATH, '//span[starts-with(@id, "count-product/")]')
    TOTAL_PRICE = (By.ID, 'total-price')
    PRODUCT_NAME_LINK = (By.CLASS_NAME, 'cart-item__cart__id')
    PRODUCT_PHOTO_LINK = (By.CLASS_NAME, 'cart-item__cart__img')
    BUTTON_FAVOURITE = (By.XPATH, '//input[starts-with(@id, "favourite-opt_cart/")]')
    POPUP_MESSAGE = (By.ID, 'header_error-message')
    MESSAGE_FOR_LOGIN = (By.XPATH, '//div[@id="header_error-message"]/span')
    BUTTON_DELETE_PRODUCT = (By.XPATH, '//span[starts-with(@id, "delete-cart-item/")]')
    
class CategoryPhonesLocators:
    BUTTON_ADD_TO_CART = (By.XPATH, '//div[@id="catalog_block-button-add-to-cart"][1]/div')
    
# class AuthorizeLocators:
#     LOGIN_BUTTON = (By.XPATH, '//div[starts-with(@class, "responseHead-module-button")]')
#     LOGIN_BUTTON_FORM = (By.XPATH, '//div[starts-with(@class,"authForm-module-button")]')
#     INPUT_EMAIL = (By.NAME, 'email')
#     INPUT_PASSWORD = (By.NAME, 'password')

class HeaderLocators:
    BUTTON_CART = (By.XPATH, '//div[@class="header__card"]/a')

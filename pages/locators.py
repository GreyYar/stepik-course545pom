from selenium.webdriver.common.by import By


class BasePageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    CART_LINK = (By.CSS_SELECTOR, ".basket-mini a.btn-default")


class LoginPageLocators(object):
    REGISTER_FORM = (By.ID, "register_form")
    LOGIN_FORM = (By.ID, "login_form")


class ProductPageLocators(object):
    ADD_TO_BASKET_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    ITEM_NAME = (By.CSS_SELECTOR, ".product_main h1")
    ITEM_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    ITEM_ADDED_TO_CART = (By.CSS_SELECTOR, ".alert-success strong")
    CART_TOTAL_PRICE = (By.CSS_SELECTOR, ".alert-info strong")


class CartPageLocators(object):
    BASKET_ITEM_LIST = (By.CLASS_NAME, "basket-items")
    EMPTY_BASKET_TEXT = (By.CSS_SELECTOR, "#content_inner > p")
    BASKET_TOTAL_PRICE_MESSAGE = (By.CSS_SELECTOR, "#messages .alert-info strong")

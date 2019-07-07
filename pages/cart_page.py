from .base_page import BasePage
from .locators import CartPageLocators


class CartPage(BasePage):
    def should_not_be_item_in_cart(self):
        assert self.is_not_element_present(*CartPageLocators.BASKET_ITEM_LIST), "Cart is not empty"

    def should_be_empty_cart_msg(self):
        assert self.is_element_present(*CartPageLocators.EMPTY_BASKET_TEXT), "Empty cart message is not appeared"

from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException
import math


class ProductPage(BasePage):
    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            print("Your code: {}".format(alert.text))
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def add_item_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        button.click()

    def should_be_item_added_to_card_msg(self):
        book_name = self.browser.find_element(*ProductPageLocators.ITEM_NAME).text
        added_book = self.browser.find_element(*ProductPageLocators.ITEM_ADDED_TO_CART).text
        assert added_book == book_name, "Book added to cart differs from current book name"

    def cart_price_msg_equals_item_price(self):
        item_price = self.browser.find_element(*ProductPageLocators.ITEM_PRICE).text
        cart_total = self.browser.find_element(*ProductPageLocators.CART_TOTAL_PRICE).text
        assert item_price == cart_total, "Cart total is differs from Item price"

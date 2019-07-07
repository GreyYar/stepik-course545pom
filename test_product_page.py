from pages.product_page import ProductPage
from pages.login_page import LoginPage
from pages.cart_page import CartPage
import pytest

link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"


@pytest.mark.long
@pytest.mark.parametrize('promo', ["?promo=newYear2019",
                                   "?promo=offer0",
                                   "?promo=offer1",
                                   "?promo=offer2",
                                   "?promo=offer3",
                                   "?promo=offer4",
                                   "?promo=offer5",
                                   "?promo=offer6",
                                   "?promo=offer7",
                                   "?promo=offer8",
                                   "?promo=offer9"])
def test_guest_can_add_promo_product_to_cart(browser, promo):
    new_link = link + promo
    page = ProductPage(browser, new_link)
    page.open()
    page.add_item_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_item_added_to_card_msg()
    page.cart_price_msg_equals_item_price()


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


def test_guest_should_see_login_link_on_product_page(browser):
    new_link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, new_link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


def test_guest_cant_see_product_in_cart_opened_from_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.go_to_cart_page()
    cart_page = CartPage(browser, browser.current_url)
    cart_page.should_not_be_item_in_cart()
    cart_page.should_be_empty_cart_msg()

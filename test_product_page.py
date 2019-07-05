from pages.product_page import ProductPage
import pytest

base_link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"


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
    link = base_link + promo
    page = ProductPage(browser, link)
    page.open()
    page.add_item_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_item_added_to_card_msg()
    page.cart_price_msg_equals_item_price()


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, base_link)
    page.open()
    page.should_not_be_success_message()

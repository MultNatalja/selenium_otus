from page_object.cart_page import CartPage
from page_object.main_page import MainPage
from page_object.shop_page import ShopPage


def test_add_items_to_cart(browser):
    add_items_to_cart = MainPage(browser)
    add_items_to_cart.check_main_page()
    add_items_to_cart.add_items_to_cart()
    alert_success = ShopPage(browser)
    alert_success.check_alert_success()
    alert_success.open_shopping_cart()
    check_items_on_cart = CartPage(browser)
    check_items_on_cart.check_items_in_cart()

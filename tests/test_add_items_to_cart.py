from page_object.cart_page import CartPage
from page_object.main_page import MainPage


def test_add_items_to_cart(browser):
    main_page = MainPage(browser)
    main_page.check_main_page()
    main_page.add_items_to_cart()
    main_page.check_alert_success()
    main_page.open_shopping_cart()
    cart_page = CartPage(browser)
    cart_page.check_items_in_cart()

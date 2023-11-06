from page_object.elements.main_locators import MainLocators
from page_object.shop_page import ShopPage


class MainPage(ShopPage):
    def __init__(self, browser):
        self.browser, self.url = browser
        self.browser.get(self.url)
        self.check_main_page()

    def check_main_page(self):
        self.find_element(MainLocators.TITLE_YOUR_STORE)

    def get_price(self):
        new_price_element = self._element(MainLocators.CURRENCY_VALUE, 2)
        return new_price_element.text

    def add_items_to_cart(self):
        self._element(MainLocators.CART_ADD_BUTTON, 5).click()

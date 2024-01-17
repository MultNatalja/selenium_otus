import allure

from page_object.elements.main_locators import MainLocators
from page_object.shop_page import ShopPage


class MainPage(ShopPage):
    def __init__(self, browser):
        self.browser, self.url = browser
        self.class_name = type(self).__name__
        self.logger = self.browser.logger
        self.logger.info("%s: Opening url: %s" % (self.class_name, browser))
        self.browser.get(self.url)
        self.check_main_page()

    def check_main_page(self):
        self._find_element(MainLocators.TITLE_YOUR_STORE)

    @allure.step("Get new price")
    def get_price(self):
        self.logger.debug(f"Get price {self.class_name}")
        new_price_element = self._element(MainLocators.CURRENCY_VALUE, 2)
        return new_price_element.text

    @allure.step("Add items to cart")
    def add_items_to_cart(self):
        self.logger.debug(f"Add items to cart {self.class_name}")
        self._element(MainLocators.CART_ADD_BUTTON, 5).click()

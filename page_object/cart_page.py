import allure

from page_object.base_page import BasePage
from page_object.elements.cart_locators import CartLocators


class CartPage(BasePage):
    @allure.step("Check items in carts")
    def check_items_in_cart(self):
        self.logger = self.browser.logger
        self.logger.info(f"Check items in cart {self.class_name}")
        self._find_element(CartLocators.TITLE_ELEMENT_CART)
        self._element(CartLocators.CHECK_ITEM_NAME)

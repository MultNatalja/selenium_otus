from page_object.base_page import BasePage
from page_object.elements.shop_locators import ShopLocators


class ShopPage(BasePage):
    def select_currency(self):
        self._element(ShopLocators.DROPDOWN_CURRENCY, 5).click()
        self._element(ShopLocators.SELECT_CURRENCY, 5).click()

    def check_alert_success(self):
        self._element(ShopLocators.ALERT_SUCCESS, 3)

    def open_shopping_cart(self):
        self._element(ShopLocators.OPEN_SHOPPING_CART).click()

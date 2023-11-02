from page_object.base_page import BasePage
from page_object.elements.shop_locators import ShopLocators


class ShopPage(BasePage):
    def select_currency(self):
        self._element(ShopLocators.DROPDOWN_CURRENCY, 5).click()
        self._element(ShopLocators.SELECT_CURRENCY, 5).click()

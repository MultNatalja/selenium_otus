import allure

from page_object.base_page import BasePage
from page_object.elements.shop_locators import ShopLocators


class ShopPage(BasePage):
    @allure.step("Select currency")
    def select_currency(self):
        self.logger = self.browser.logger
        self.logger.debug(f"Select currency {self.class_name}")
        self._element(ShopLocators.DROPDOWN_CURRENCY, 5).click()
        self._element(ShopLocators.SELECT_CURRENCY, 5).click()

    @allure.step("Check alert success")
    def check_alert_success(self):
        self.logger.debug(f"Check alert success {self.class_name}")
        self._element(ShopLocators.ALERT_SUCCESS, 3)

    @allure.step("Open shopping cart")
    def open_shopping_cart(self):
        self.logger.debug(f"Opening shopping cart {self.class_name}")
        self._element(ShopLocators.OPEN_SHOPPING_CART).click()

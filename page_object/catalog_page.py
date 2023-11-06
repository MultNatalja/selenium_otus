from page_object.shop_page import ShopPage
from page_object.elements.catalog_locators import CatalogLocators


class CatalogPage(ShopPage):
    def __init__(self, browser):
        self.browser, self.url = browser
        self.browser.get(self.url + '/desktops')
        self.check_catalog_page()

    def check_catalog_page(self):
        self.find_element(CatalogLocators.TITLE_DESKTOPS)

    def get_price(self):
        new_price_element = self._element(CatalogLocators.CURRENCY_VALUE, 2)
        return new_price_element.text

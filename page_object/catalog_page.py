from page_object.shop_page import ShopPage
from page_object.elements.catalog_locators import CatalogLocators


class CatalogPage(ShopPage):
    def __init__(self, browser, page_url):
        self.browser, self.url = browser
        self.browser.get(self.url + page_url)

    def check_catalog_page(self, title_locator):
        self._find_element(title_locator)

    def get_price(self):
        new_price_element = self._element(CatalogLocators.CURRENCY_VALUE, 2)
        return new_price_element.text

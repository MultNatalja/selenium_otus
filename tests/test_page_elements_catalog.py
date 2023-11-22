from page_object.catalog_page import CatalogPage
from page_object.elements.catalog_locators import CatalogLocators


def test_find_elements_catalog(browser):
    catalog_page = CatalogPage(browser, '/desktops')
    catalog_page.check_catalog_page(CatalogLocators.TITLE_DESKTOPS)
    catalog_page._element(CatalogLocators.PRODUCT_LAYOUT)
    catalog_page._element(CatalogLocators.INPUT_LIMIT)
    catalog_page._element(CatalogLocators.IMAGE_CATALOG)
    catalog_page._element(CatalogLocators.INPUT_SORT)
    catalog_page._element(CatalogLocators.CART_ADD_BUTTON)

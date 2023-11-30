import pytest
from page_object.catalog_page import CatalogPage
from page_object.elements.catalog_locators import CatalogLocators


@pytest.mark.parametrize("expected_currency", ["£"])
def test_change_currency_catalog(browser, expected_currency):
    catalog_page = CatalogPage(browser, '/desktops')
    catalog_page.check_catalog_page(CatalogLocators.TITLE_DESKTOPS)
    catalog_page.select_currency()
    new_price_text = catalog_page.get_price()
    assert expected_currency in new_price_text, f"Expected currency {expected_currency} not found in {new_price_text}"

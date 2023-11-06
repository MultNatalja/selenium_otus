import pytest
from page_object.catalog_page import CatalogPage


@pytest.mark.parametrize("expected_currency", ["£"])
def test_change_currency_catalog(browser, expected_currency):
    catalog_page = CatalogPage(browser)
    catalog_page.select_currency()
    new_price_text = catalog_page.get_price()
    assert expected_currency in new_price_text, f"Expected currency {expected_currency} not found in {new_price_text}"

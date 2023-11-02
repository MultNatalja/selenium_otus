import pytest
from page_object.main_page import MainPage


@pytest.mark.parametrize("expected_currency", ["£"])
def test_change_currency_main(browser, expected_currency):
    search_currency_main_page = MainPage(browser)
    search_currency_main_page.check_main_page()
    search_currency_main_page.select_currency()
    new_price_text = search_currency_main_page.check_price()
    assert expected_currency in new_price_text, f"Expected currency {expected_currency} not found in {new_price_text}"

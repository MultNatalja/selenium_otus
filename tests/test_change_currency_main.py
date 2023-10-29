import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_change_currency_main(browser, url):
    browser.get(url)
    WebDriverWait(browser, 5).until(EC.title_contains("Your Store"))
    currency_list = (browser.find_element(By.CSS_SELECTOR, "#form-currency div button"))
    currency_list.click()

    currency = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#form-currency div ul li:nth-child(2) button")))
    currency.click()

    new_price_element = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "#content > div.row > div:nth-child(1) > div > div.caption > p.price"))
    )
    new_price_text = new_price_element.text
    expected_currency = "£"

    assert expected_currency in new_price_text, f"Expected currency {expected_currency} not found in {new_price_text}"

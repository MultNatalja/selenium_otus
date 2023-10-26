import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_add_item_to_cart(browser, url):
    browser.get(url)
    WebDriverWait(browser, 5).until(EC.title_contains("Your Store"))
    WebDriverWait(browser, 1).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR,
                                          "#content div.row .product-layout .button-group button:nth-child(1)"))).click()
    WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#common-home div.alert.alert-success.alert-dismissible")))

    WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "ul li:nth-child(4) a"))).click()

    WebDriverWait(browser, 5).until(EC.title_contains("Shopping Cart"))
    WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#content form div table tbody tr td:nth-child(2)")))


if __name__ == '__main__':
    pytest.main()

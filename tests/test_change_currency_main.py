import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_change_currency_main(browser, url):
    browser.get(url)
    WebDriverWait(browser, 5).until(EC.title_contains("Your Store"))





if __name__ == '__main__':
    pytest.main()
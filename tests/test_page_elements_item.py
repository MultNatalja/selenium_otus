from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_find_elements_item(browser, url):
    browser.get(url + "/iphone")
    WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#input-quantity")))
    WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#button-cart")))
    WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#content h1")))
    WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#content img")))
    WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#content .image")))

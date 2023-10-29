from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_find_elements_catalog(browser, url):
    browser.get(url + "/desktops")
    WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".product-layout")))
    WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#input-limit")))
    WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".image")))
    WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#input-sort")))
    WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".button-group button")))

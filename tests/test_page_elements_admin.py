from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_find_elements_admin(browser, url):
    browser.get(url + "/admin")
    WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#input-username")))
    WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#input-password")))
    WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".btn-primary")))
    WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".help-block")))
    WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button[type='submit']")))

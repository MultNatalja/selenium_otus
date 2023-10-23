from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_find_elements_main_page(browser, url):
    browser.get(url)
    WebDriverWait(browser, 1).until(EC.title_is("Your Store"))
    WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name='search']")))
    WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#logo")))
    WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#cart button")))
    WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#cart button")))
    WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".swiper-container")))

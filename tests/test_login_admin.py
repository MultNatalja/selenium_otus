from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_login_admin(browser, url):
    login = "user"
    password = "bitnami"
    browser.get(url + "/admin")
    username_input = browser.find_element(By.ID, "input-username")
    password_input = browser.find_element(By.ID, "input-password")
    login_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")

    username_input.send_keys(login)
    password_input.send_keys(password)
    login_button.click()

    WebDriverWait(browser, 5).until(EC.title_contains("Dashboard"))

    logout_button = browser.find_element(By.CSS_SELECTOR, "ul.nav li:nth-child(2) a")
    logout_button.click()
    WebDriverWait(browser, 5).until(EC.title_contains("Administration"))

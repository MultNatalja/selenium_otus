from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By

from page_object.base_page import BasePage


class RegisterLocators(BasePage):
    INPUT_USERNAME = (By.ID, "input-username")
    PASSWORD_INPUT = (By.ID, "input-password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    LOGOUT_BUTTON = (By.CSS_SELECTOR, "ul.nav li:nth-child(2) a")
    TITLE_DASHBOARD = EC.title_contains("Dashboard")
    TITLE_ADMINISTRATION = EC.title_contains("Administration")
    ELEMENT_INPUT_USERNAME = EC.visibility_of_element_located((By.CSS_SELECTOR, "#input-username"))
    ELEMENT_INPUT_PASSWORD = EC.visibility_of_element_located((By.CSS_SELECTOR, "#input-password"))
    ELEMENT_BUTTON_LOGIN = EC.visibility_of_element_located((By.CSS_SELECTOR, ".btn-primary"))
    ELEMENT_HELP_BLOCK = EC.visibility_of_element_located((By.CSS_SELECTOR, ".help-block"))
    ELEMENT_BUTTON_SUBMIT = EC.visibility_of_element_located((By.CSS_SELECTOR, "button[type='submit']"))

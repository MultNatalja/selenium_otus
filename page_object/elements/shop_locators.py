from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class ShopLocators:
    DROPDOWN_CURRENCY = (By.CSS_SELECTOR, "#form-currency div button")
    SELECT_CURRENCY = (By.CSS_SELECTOR, "#form-currency div ul li:nth-child(2) button")
    ELEMENT_INPUT_SEARCH = EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name='search']"))
    ELEMENT_LOGO = EC.visibility_of_element_located((By.CSS_SELECTOR, "#logo"))
    ELEMENT_CART_BUTTON = EC.visibility_of_element_located((By.CSS_SELECTOR, "#cart button"))
    ALERT_SUCCESS = (By.CSS_SELECTOR, "#common-home div.alert.alert-success.alert-dismissible")
    OPEN_SHOPPING_CART = (By.CSS_SELECTOR, "ul li:nth-child(4) a")

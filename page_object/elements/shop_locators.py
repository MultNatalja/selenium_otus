from selenium.webdriver.common.by import By


class ShopLocators:
    DROPDOWN_CURRENCY = (By.CSS_SELECTOR, "#form-currency div button")
    SELECT_CURRENCY = (By.CSS_SELECTOR, "#form-currency div ul li:nth-child(2) button")

from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By


class MainLocators:
    TITLE_YOUR_STORE = EC.title_contains("Your Store")
    CURRENCY_VALUE = (By.CSS_SELECTOR, "#content > div.row > div:nth-child(1) > div > div.caption > p.price")

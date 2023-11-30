from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class CartLocators:
    TITLE_ELEMENT_CART = EC.title_contains("Shopping Cart")
    CHECK_ITEM_NAME = (By.CSS_SELECTOR, "#content form div table tbody tr td:nth-child(2)")

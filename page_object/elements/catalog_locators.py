from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class CatalogLocators:
    TITLE_DESKTOPS = EC.title_contains("Desktops")
    CURRENCY_VALUE = (
        By.CSS_SELECTOR,
        "#content div.caption p.price span.price-new"
    )
    PRODUCT_LAYOUT = (By.CSS_SELECTOR, ".product-layout")
    INPUT_LIMIT = (By.CSS_SELECTOR, "#input-limit")
    IMAGE_CATALOG = (By.CSS_SELECTOR, ".image")
    INPUT_SORT = (By.CSS_SELECTOR, "#input-sort")
    CART_ADD_BUTTON = (By.CSS_SELECTOR, ".button-group button")

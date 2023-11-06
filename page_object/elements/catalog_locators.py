from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class CatalogLocators:
    TITLE_DESKTOPS = EC.title_contains("Desktops")
    CURRENCY_VALUE = (
        By.CSS_SELECTOR,
        "#content div.caption p.price span.price-new"
    )

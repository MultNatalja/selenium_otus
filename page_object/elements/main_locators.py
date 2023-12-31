from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class MainLocators:
    TITLE_YOUR_STORE = EC.title_contains("Your Store")
    CURRENCY_VALUE = (By.CSS_SELECTOR, "#content > div.row > div:nth-child(1) > div > div.caption > p.price")
    ELEMENT_SWIPER_CONTAINER = EC.visibility_of_element_located((By.CSS_SELECTOR, ".swiper-container"))
    CART_ADD_BUTTON = (By.CSS_SELECTOR, "#content div.row .product-layout .button-group button:nth-child(1)")

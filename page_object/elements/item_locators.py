from selenium.webdriver.common.by import By


class ItemLocators:
    INPUT_QUANTITY = (By.CSS_SELECTOR, "#input-quantity")
    BUTTON_CART = (By.CSS_SELECTOR, "#button-cart")
    CONTENT_HEADER = (By.CSS_SELECTOR, "#content h1")
    CONTENT_IMAGE = (By.CSS_SELECTOR, "#content img")
    CONTENT_IMAGE_RELATED = (By.CSS_SELECTOR, "#content .image")

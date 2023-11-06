from selenium.webdriver.common.by import By


class RegistrationLocators:
    INPUT_FIRST_NAME = (By.CSS_SELECTOR, "#input-firstname")
    INPUT_CONFIRM = (By.CSS_SELECTOR, "#input-confirm")
    SUBSCRIBE_BUTTON_NO = (By.CSS_SELECTOR, "input[type='radio'][value='0']")
    PRIVACY_POLICY_CHECKBOX = (By.CSS_SELECTOR, "input[type='checkbox']")
    BUTTON_CONTINUE = (By.CSS_SELECTOR, ".btn-primary")

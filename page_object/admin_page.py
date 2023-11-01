from selenium.webdriver.support.ui import WebDriverWait

from page_object.base_page import BasePage
from page_object.elements.registration_locators import RegisterLocators


class AdminPage(BasePage):
    def __init__(self, browser):
        self.browser, self.url = browser
        self.browser.get(self.url + '/admin')
        self.check_admin_page()

    def check_admin_page(self):
        self._verify_element_presence(RegisterLocators.INPUT_USERNAME)

    def login(self, login, password):
        self._send_keys(RegisterLocators.INPUT_USERNAME, login)
        self._send_keys(RegisterLocators.PASSWORD_INPUT, password)
        self._element(RegisterLocators.LOGIN_BUTTON).click()
        WebDriverWait(self.browser, 5).until(RegisterLocators.TITLE_DASHBOARD)

    def logout(self):
        self._element(RegisterLocators.LOGOUT_BUTTON).click()
        WebDriverWait(self.browser, 5).until(RegisterLocators.TITLE_ADMINISTRATION)

    def find_element(self, locator):
        WebDriverWait(self.browser, 1).until(locator)

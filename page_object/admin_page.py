import allure

from page_object.base_page import BasePage
from page_object.elements.admin_login_locators import AdminLoginLocators


class AdminPage(BasePage):
    def __init__(self, browser, page_url):
        self.browser, self.url = browser
        self.class_name = type(self).__name__
        self.logger = self.browser.logger
        self.logger.info("%s: Opening url: %s" % (self.class_name, page_url))
        self.browser.get(self.url + page_url)
        self.check_admin_page()

    @allure.step("Check admin page")
    def check_admin_page(self):
        self._verify_element_presence(AdminLoginLocators.INPUT_USERNAME)

    @allure.step("Login by {login}")
    def login(self, login, password):
        self.logger.debug("%s: Login with: %s" % (self.class_name, login))
        self._send_keys(AdminLoginLocators.INPUT_USERNAME, login)
        self._send_keys(AdminLoginLocators.PASSWORD_INPUT, password)
        self._element(AdminLoginLocators.LOGIN_BUTTON).click()
        self._find_element(AdminLoginLocators.TITLE_DASHBOARD, 5)

    @allure.step("Logout from admin")
    def logout(self):
        self.logger.debug(f"Logout {self.class_name}")
        self._element(AdminLoginLocators.LOGOUT_BUTTON).click()
        self._find_element(AdminLoginLocators.TITLE_ADMINISTRATION, 5)

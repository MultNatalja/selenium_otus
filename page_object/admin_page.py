from page_object.base_page import BasePage
from page_object.elements.admin_login_locators import AdminLoginLocators


class AdminPage(BasePage):
    def __init__(self, browser):
        self.browser, self.url = browser
        self.browser.get(self.url + '/admin')
        self.check_admin_page()

    def check_admin_page(self):
        self._verify_element_presence(AdminLoginLocators.INPUT_USERNAME)

    def login(self, login, password):
        self._send_keys(AdminLoginLocators.INPUT_USERNAME, login)
        self._send_keys(AdminLoginLocators.PASSWORD_INPUT, password)
        self._element(AdminLoginLocators.LOGIN_BUTTON).click()
        self.find_element(AdminLoginLocators.TITLE_DASHBOARD, 5)

    def logout(self):
        self._element(AdminLoginLocators.LOGOUT_BUTTON).click()
        self.find_element(AdminLoginLocators.TITLE_ADMINISTRATION, 5)

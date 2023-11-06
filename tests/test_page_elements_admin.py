from page_object.admin_page import AdminPage
from page_object.elements.admin_login_locators import AdminLoginLocators


def test_find_elements_admin(browser):
    admin_login_page = AdminPage(browser)
    admin_login_page.find_element(AdminLoginLocators.ELEMENT_INPUT_USERNAME)
    admin_login_page.find_element(AdminLoginLocators.ELEMENT_INPUT_PASSWORD)
    admin_login_page.find_element(AdminLoginLocators.ELEMENT_BUTTON_LOGIN)
    admin_login_page.find_element(AdminLoginLocators.ELEMENT_HELP_BLOCK)
    admin_login_page.find_element(AdminLoginLocators.ELEMENT_BUTTON_SUBMIT)

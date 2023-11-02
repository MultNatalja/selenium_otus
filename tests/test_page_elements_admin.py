from page_object.admin_page import AdminPage
from page_object.elements.registration_locators import RegisterLocators


def test_find_elements_admin(browser):
    admin_login_page = AdminPage(browser)
    admin_login_page.find_element(RegisterLocators.ELEMENT_INPUT_USERNAME)
    admin_login_page.find_element(RegisterLocators.ELEMENT_INPUT_PASSWORD)
    admin_login_page.find_element(RegisterLocators.ELEMENT_BUTTON_LOGIN)
    admin_login_page.find_element(RegisterLocators.ELEMENT_HELP_BLOCK)
    admin_login_page.find_element(RegisterLocators.ELEMENT_BUTTON_SUBMIT)

from page_object.registration_page import RegistrationPage
from page_object.elements.registration_locators import RegistrationLocators


def test_find_elements_registration(browser):
    registration_page = RegistrationPage(browser, '/index.php?route=account/register')
    registration_page._element(RegistrationLocators.INPUT_FIRST_NAME)
    registration_page._element(RegistrationLocators.INPUT_CONFIRM)
    registration_page._element(RegistrationLocators.SUBSCRIBE_BUTTON_NO)
    registration_page._element(RegistrationLocators.PRIVACY_POLICY_CHECKBOX)
    registration_page._element(RegistrationLocators.BUTTON_CONTINUE)

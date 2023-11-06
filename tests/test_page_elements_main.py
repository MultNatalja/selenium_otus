from page_object.main_page import MainPage
from page_object.elements.main_locators import MainLocators
from page_object.elements.shop_locators import ShopLocators


def test_find_elements_main_page(browser):
    main_page = MainPage(browser)
    main_page._find_element(MainLocators.TITLE_YOUR_STORE)
    main_page._find_element(ShopLocators.ELEMENT_INPUT_SEARCH)
    main_page._find_element(ShopLocators.ELEMENT_CART_BUTTON)
    main_page._find_element(MainLocators.ELEMENT_SWIPER_CONTAINER)

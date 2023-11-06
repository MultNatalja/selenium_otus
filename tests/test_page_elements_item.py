from page_object.item_page import ItemPage
from page_object.elements.item_locators import ItemLocators


def test_find_elements_item(browser):
    item_page = ItemPage(browser)
    item_page._element(ItemLocators.INPUT_QUANTITY)
    item_page._element(ItemLocators.BUTTON_CART)
    item_page._element(ItemLocators.CONTENT_HEADER)
    item_page._element(ItemLocators.CONTENT_IMAGE)
    item_page._element(ItemLocators.CONTENT_IMAGE_RELATED)

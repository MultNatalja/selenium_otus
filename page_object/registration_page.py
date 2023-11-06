from page_object.shop_page import ShopPage


class RegistrationPage(ShopPage):
    def __init__(self, browser):
        self.browser, self.url = browser
        self.browser.get(self.url + '/index.php?route=account/register')

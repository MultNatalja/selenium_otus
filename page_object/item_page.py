from page_object.shop_page import ShopPage


class ItemPage(ShopPage):
    def __init__(self, browser, page_url):
        self.browser, self.url = browser
        self.browser.get(self.url + page_url)

from page_object.shop_page import ShopPage


class ItemPage(ShopPage):
    def __init__(self, browser, page_url):
        self.browser, self.url = browser
        self.class_name = type(self).__name__
        self.logger = self.browser.logger
        self.logger.info("%s: Opening url: %s" % (self.class_name, page_url))
        self.browser.get(self.url + page_url)

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, browser):
        self.browser, self.url = browser

    def _element(self, locator: tuple):
        return self._verify_element_presence(locator)

    def _verify_element_presence(self, locator: tuple):
        try:
            return WebDriverWait(self.browser, self.browser.t).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            raise AssertionError("Cant find elements by locator: {}".format(locator))

    def _send_keys(self, element, keys):
        element = self._element(element)
        element.send_keys(keys)

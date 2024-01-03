import allure
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, browser):
        self.browser, self.url = browser
        self.logger = self.browser.logger
        self.class_name = type(self).__name__

    def _element(self, locator: tuple, timeout=None):
        self.logger.info("%s: Verify element: %s" % (self.class_name, str(locator)))
        return self._verify_element_presence(locator, timeout)

    @allure.step
    def _verify_element_presence(self, locator: tuple, timeout=None):
        self.logger.info("%s: Verify element presence: %s" % (self.class_name, str(locator)))
        if timeout is None:
            timeout = self.browser.timeout
        try:
            return WebDriverWait(self.browser, timeout).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            raise AssertionError("Cant find elements by locator: {}".format(locator))

    @allure.step
    def _send_keys(self, element, keys):
        self.logger.info("%s: Send keys: %s" % (self.class_name, str(element)))
        element = self._element(element)
        element.send_keys(keys)

    @allure.step
    def _find_element(self, locator, timeout=None):
        self.logger.info("%s: Find element: %s" % (self.class_name, str(locator)))
        if timeout is None:
            timeout = self.browser.timeout
        try:
            return WebDriverWait(self.browser, timeout).until(locator)
        except TimeoutException:
            raise AssertionError("Cant find elements by locator: {}".format(locator))

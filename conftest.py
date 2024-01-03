import datetime
import json
import os

import allure
import pytest
import logging
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FFOptions
from selenium.webdriver.chrome.options import Options as ChromeOptions


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")
    parser.addoption("--max", action="store_true")
    parser.addoption("--url", help="base application url")
    parser.addoption("--headless", action="store_true")
    parser.addoption("--log_level", action="store", default="DEBUG")


@pytest.fixture(scope="session")
def url(request):
    return request.config.getoption("--url")


@pytest.fixture()
def browser(request):
    browser_name = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")
    url = request.config.getoption("--url")
    log_level = request.config.getoption("--log_level")

    logger = logging.getLogger(request.node.name)
    file_handler = logging.FileHandler(f"../logs/{request.node.name}.log")
    file_handler.setFormatter(logging.Formatter('%(levelname)s %(message)s'))
    logger.addHandler(file_handler)
    logger.setLevel(level=log_level)

    logger.info("Test %s started at %s" % (request.node.name, datetime.datetime.now()))

    if browser_name == "chrome":
        options = ChromeOptions()
        if headless:
            options.add_argument("--headless=new")
        driver = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        options = FFOptions()
        if headless:
            options.add_argument("--headless")
        driver = webdriver.Firefox(options=options)
    elif browser_name == "safari":
        driver = webdriver.Safari()
    elif browser_name == "edge":
        driver = webdriver.Edge()
    else:
        raise ValueError(f"Browser {browser_name} not supported")

    driver.log_level = log_level
    driver.logger = logger
    driver.test_name = request.node.name

    logger.info("Browser %s started" % browser)

    if request.config.getoption("--max"):
        driver.maximize_window()

    driver.timeout = 5

    allure.attach(
        name=driver.session_id,
        body=json.dumps(driver.capabilities),
        attachment_type=allure.attachment_type.JSON)

    yield driver, url

    driver.close()
    logger.info("Test %s finished at %s" % (request.node.name, datetime.datetime.now()))

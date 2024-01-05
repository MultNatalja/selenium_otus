import datetime
import json
import os

import allure
import pytest
import logging
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FFOptions
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.safari.options import Options as SafariOptions
from selenium.webdriver.edge.options import Options as EdgeOptions


def pytest_addoption(parser):
    parser.addoption("--browser", default="firefox")
    parser.addoption("--max", action="store_true")
    parser.addoption("--url", help="base application url")
    parser.addoption("--headless", action="store_true")
    parser.addoption("--log_level", action="store", default="DEBUG")
    parser.addoption("--executor", action="store", default="192.168.5.115")
    parser.addoption("--bv", default="120.0")
    parser.addoption("--video", action="store_true")
    parser.addoption("--vnc", action="store_true")
    parser.addoption("--start_type")


@pytest.fixture(scope="session")
def url(request):
    return request.config.getoption("--url")


@pytest.fixture()
def browser(request):
    browser_name = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")
    url = request.config.getoption("--url")
    log_level = request.config.getoption("--log_level")
    executor = request.config.getoption("--executor")
    bv = request.config.getoption("--bv")
    executor_url = f"http://{executor}:4444/wd/hub"
    video = request.config.getoption("--video")
    vnc = request.config.getoption("--vnc")
    start_type = request.config.getoption("--start_type")

    logger = logging.getLogger(request.node.name)
    file_handler = logging.FileHandler(f"../logs/{request.node.name}.log")
    file_handler.setFormatter(logging.Formatter('%(levelname)s %(message)s'))
    logger.addHandler(file_handler)
    logger.setLevel(level=log_level)

    logger.info("Test %s started at %s" % (request.node.name, datetime.datetime.now()))

    if start_type == "local":
        if browser_name == "chrome":
            options = ChromeOptions()
            if headless:
                options.add_argument("--headless")
            driver = webdriver.Chrome(options=options)
        elif browser_name == "firefox":
            options = FFOptions()
            if headless:
                options.add_argument("--headless")
            driver = webdriver.Firefox(options=options)
        elif browser_name == "safari":
            driver = webdriver.Safari()
        elif browser_name == "MicrosoftEdge":
            driver = webdriver.Edge()
        else:
            raise ValueError(f"Browser {browser_name} not supported")
    else:
        if browser_name == "chrome":
            options = ChromeOptions()
        elif browser_name == "firefox":
            options = FFOptions()
        elif browser_name == "safari":
            options = SafariOptions()
        elif browser_name == "MicrosoftEdge":
            options = EdgeOptions()
        else:
            raise ValueError(f"Browser {browser_name} not supported")

        if headless:
            options.add_argument("--headless")

        caps = {
            "browserName": browser_name,
            "browserVersion": bv,
            "selenoid:options": {
                "enableVideo": video,
                "enableVNC": vnc,
                "name": os.getenv("BUILD_NUMBER", f"{request.node.name}"),
            },
            "acceptInsecureCerts": True,
        }

        for k, v in caps.items():
            options.set_capability(k, v)

        driver = webdriver.Remote(
            command_executor=executor_url,
            options=options
        )

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

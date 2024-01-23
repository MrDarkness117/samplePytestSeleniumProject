import json
import logging
from pathlib import Path

import pytest
from paths import *
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService

driver_presets = {
    "Chrome": (webdriver.Chrome(service=ChromeService(ChromeDriverManager().install())), ChromeOptions(), DesiredCapabilities.CHROME),
    "Firefox": (webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install())), FirefoxOptions(), DesiredCapabilities.FIREFOX)
}


def pytest_configure(config):
    logging.basicConfig(
        level=logging.INFO,
        filename=pytest_logs,
        format="[%(levelname)s]: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",  # На случай если понадобится знать точное время
    )


@pytest.fixture(scope='session', params=driver_presets.keys())
def setup_login(request):
    logging.info(f"Beginning testing, browser {request.param}")
    if request.param == "Chrome":
        driver = driver_presets["Chrome"][0]
        driver_options = driver_presets["Chrome"][1]
        caps = driver_presets["Chrome"][2]
        prefs = json.load(open(selenium_prefs, "r", encoding="utf-8"))
        caps['goog:loggingPrefs'] = {'performance': 'ALL'}
        driver_options.add_experimental_option(name='prefs', value=prefs["Chrome"])
        driver_options.add_experimental_option(name='caps', value=caps)
    elif request.param == "Firefox":
        driver = driver_presets["Firefox"][0]
        options = driver_presets["Firefox"][1]
        caps = driver_presets["Firefox"][2]
    driver.maximize_window()

    yield driver

    driver.quit()
    logging.info("Finish testing.")

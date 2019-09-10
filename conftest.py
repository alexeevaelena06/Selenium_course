import os
import pytest
import threading
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from locators import admin_login
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


PROJECT_ROOT = os.path.dirname(__file__)
DOWNLOADS_DIR = os.path.join(PROJECT_ROOT, 'downloads')

local_data = threading.local()


def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="available: chrome, remote_chrome"
    )


@pytest.fixture
def fixture(request):
    local_data.browser = request.config.getoption('--browser')
    start_browser()
    request.addfinalizer(local_data.driver.quit)
    return local_data.driver


def start_browser():
    if local_data.browser == 'chrome':
        chrome_options = Options()
        chrome_options.add_experimental_option('prefs',
                                               {"download.default_directory": DOWNLOADS_DIR,
                                                "download.prompt_for_download": False,
                                                "download.directory_upgrade": True,
                                                "safebrowsing.enabled": True,
                                                "browser": "ALL"})
        driver = webdriver.Chrome(chrome_options=chrome_options)

    elif local_data.browser == 'IE':
        cap = DesiredCapabilities.INTERNETEXPLORER.copy()
        cap['IE_ENSURE_CLEAN_SESSION'] = True
        driver = webdriver.Ie(capabilities=cap)
    elif local_data.browser == 'firefox':
        firefox_capabilities = DesiredCapabilities.FIREFOX
        # firefox_capabilities['marionette'] = False
        # driver = webdriver.Firefox(capabilities=firefox_capabilities,
        #                            firefox_binary="C:\\Program Files\\Firefox Nightly\\firefox.exe")
        driver = webdriver.Firefox(capabilities=firefox_capabilities)
    elif local_data.browser == 'edge':
        edge_capabilities = DesiredCapabilities.EDGE
        driver = webdriver.Edge(capabilities=edge_capabilities)
    else:
        raise Exception(f'Browser "{local_data.browser}" is wrong!')
    driver.maximize_window()
    local_data.driver = driver
    return driver


def login_admin(driver):
    driver.get(admin_login[1])
    driver.implicitly_wait(60)
    find_and_fill_element(driver, element_name="username", value="admin")
    find_and_fill_element(driver, element_name="password", value="admin")
    driver.find_element_by_name("login").click()


def find_and_fill_element(driver, element_name, value):
    driver.find_element_by_name(element_name).click()
    driver.find_element_by_name(element_name).clear()
    driver.find_element_by_name(element_name).send_keys(value)

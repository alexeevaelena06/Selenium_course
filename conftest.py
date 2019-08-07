import os
import pytest
import threading
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


PROJECT_ROOT = os.path.dirname(__file__)
DRIVER_DIR = '{}\\chromedriver.exe'.format(str(os.getcwd()))
DOWNLOADS_DIR = os.path.join(PROJECT_ROOT, 'downloads')

local_data = threading.local()


def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="available: chrome, remote_chrome"
    )


@pytest.fixture
def fixture(request):
    start_browser()
    request.addfinalizer(local_data.driver.quit)
    return local_data.driver


def start_browser():
    chrome_options = Options()
    chrome_options.add_experimental_option('prefs',
                                           {"download.default_directory": DOWNLOADS_DIR,
                                            "download.prompt_for_download": False,
                                            "download.directory_upgrade": True,
                                            "safebrowsing.enabled": True})
    driver = webdriver.Chrome(executable_path=DRIVER_DIR, chrome_options=chrome_options)
    driver.maximize_window()
    local_data.driver = driver
    return driver

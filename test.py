import os
import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PROJECT_ROOT = os.path.dirname(__file__)
DRIVER_DIR = '{}\\chromedriver.exe'.format(str(os.getcwd()))


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome(executable_path=DRIVER_DIR)
    request.addfinalizer(wd.quit)
    return wd


def test_example(driver):
    driver.get("https://www.google.com/")
    driver.find_element_by_name("q").send_keys("webdriver")
    driver.find_element_by_name("q").send_keys(Keys.ENTER)
    WebDriverWait(driver, 10).until(EC.title_is("webdriver - Поиск в Google"))



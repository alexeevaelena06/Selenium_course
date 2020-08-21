from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Selenium_course.locators import admin_login, admin


def test_admin_login(fixture):
    driver = fixture
    driver.get(admin_login[0])
    driver.find_element_by_name("username").send_keys(admin['login_name'])
    driver.find_element_by_name("password").send_keys(admin['login_password'])
    driver.find_element_by_name("login").click()
    WebDriverWait(driver, 10).until(EC.title_is("My Store"))

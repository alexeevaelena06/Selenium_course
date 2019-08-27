# Задание 14. Проверьте, что ссылки открываются в новом окне
# Сделайте сценарий, который проверяет, что ссылки на странице редактирования страны открываются в новом окне.
#
# Сценарий должен состоять из следующих частей:
#
# 1) зайти в админку
# 2) открыть пункт меню Countries (или страницу http://localhost/litecart/admin/?app=countries&doc=countries)
# 3) открыть на редактирование какую-нибудь страну или начать создание новой
# 4) возле некоторых полей есть ссылки с иконкой в виде квадратика со стрелкой -- они ведут на внешние страницы и
# открываются в новом окне, именно это и нужно проверить.
from selenium.webdriver.support.wait import WebDriverWait
from contextlib import contextmanager
from helpers import login_admin
from locators import *


def test_check_countries_links(fixture):
    driver = fixture
    login_admin(driver=driver)
    driver.get(page_countries[0])
    driver.find_element_by_xpath(locator_add_new_country[0]).click()
    all_ex_link = driver.find_elements_by_xpath(locator_all_ex_links[0])
    print('Количество ссылок для открытия в новом окне: {}'.format(len(all_ex_link)))
    main_window = driver.current_window_handle
    old_windows = driver.window_handles
    for i in range(len(all_ex_link)):
        with wait_for_new_window(driver, 10):
            all_ex_link[i].click()
        new_windows = driver.window_handles
        new_window = list(set(new_windows).difference(old_windows))
        driver.switch_to.window(new_window[0])
        driver.close()
        driver.switch_to.window(main_window)


@contextmanager
def wait_for_new_window(driver, timeout=10):
    handles_before = driver.window_handles
    yield
    WebDriverWait(driver, timeout).until(
        lambda driver: len(handles_before) != len(driver.window_handles))

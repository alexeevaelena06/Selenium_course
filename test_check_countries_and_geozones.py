import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *


def test_check_countries_and_geozones(fixture):
    driver = fixture
    driver.get(admin_login[0])
    driver.find_element_by_name("username").send_keys(admin['login_name'])
    driver.find_element_by_name("password").send_keys(admin['login_password'])
    driver.find_element_by_name("login").click()
    WebDriverWait(driver, 5).until(EC.title_is("My Store"))
    driver.get(page_countries[0])
    time.sleep(1)
    displayed_countries = []
    displayed_countries_geozones = []
    countries_list = driver.find_elements_by_css_selector(locator_all_countries[0])
    for i in range(len(countries_list)):
        country = driver.find_elements_by_css_selector(locator_all_countries[0])
        country_name = country[i].text
        displayed_countries.append(country_name)
    sorted_country_list = sorted(displayed_countries)
    assert displayed_countries == sorted_country_list, 'Страны расположены не в алфавитном порядке'
    geo_zone_list = driver.find_elements_by_css_selector(locator_all_geozones[0])
    country_links = []
    for j in range(len(geo_zone_list)):
        geo_zone = driver.find_elements_by_css_selector(locator_all_geozones[0])
        if geo_zone[j].text != '0':
            country = driver.find_elements_by_css_selector(locator_all_countries[0])
            country_with_geozones = country[j].text
            displayed_countries_geozones.append(country_with_geozones)
            country_links.append(country[j])
    print('Countries with geozones: {}'.format(displayed_countries_geozones))
    country_list_text = []
    for country in country_links:
        print(country.get_attribute('href'))
        country_list_text.append(country.get_attribute('href'))
    for i in range(len(country_list_text)):
        geozones_list = []
        driver.get(country_list_text[i])
        geo_zones_in_selects = driver.find_elements_by_css_selector(locator_all_towns[0])
        for geozones in geo_zones_in_selects:
            geozones_list.append(geozones.text)
        geozones_list = geozones_list[:-1]
        sorted_geozones_list = sorted(geozones_list)
        print(geozones_list)
        assert geozones_list == sorted_geozones_list, 'Города расположены не в алфавитном порядке'


def test_geo_zones(fixture):
    driver = fixture
    driver.get(admin_login[0])
    driver.find_element_by_name("username").send_keys(admin['login_name'])
    driver.find_element_by_name("password").send_keys(admin['login_password'])
    driver.find_element_by_name("login").click()
    WebDriverWait(driver, 5).until(EC.title_is("My Store"))
    driver.get(page_geozones[0])
    geozones_list_text = []
    geo_links = driver.find_elements_by_xpath(locator_geozones[0])
    for link in geo_links:
        print(link.get_attribute('href'))
        geozones_list_text.append(link.get_attribute('href'))
    for i in range(len(geozones_list_text)):
        geozones_list = []
        driver.get(geozones_list_text[i])
        geo_zones_in_selects = driver.find_elements_by_xpath(locator_town_in_geozones[0])
        for geozones in geo_zones_in_selects:
            geozones_list.append(geozones.text)
        sorted_geozones_list = sorted(geozones_list)
        print(geozones_list)
        assert geozones_list == sorted_geozones_list, 'Города расположены не в алфавитном порядке'

from conftest import login_admin
from locators import page_catalogue, locator_rubber_ducks


def test_check_browser_log(fixture):
    driver = fixture
    login_admin(driver)
    driver.get(page_catalogue[0])
    links = driver.find_elements_by_xpath(locator_rubber_ducks)
    links_mass = []
    for link in links:
        links_mass.append(link.get_attribute('href'))
    links_count = len(links_mass)
    for i in range(links_count):
        links = driver.find_elements_by_xpath(locator_rubber_ducks)
        links[i].click()
        driver.find_element_by_name("cancel").click()

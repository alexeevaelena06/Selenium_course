import os
from helpers import *
from locators import *

PROJECT_ROOT = os.path.dirname(__file__)
PATH_TO_DUCK_IMG = os.path.join(PROJECT_ROOT, 'data\\duck_image.png')


def test_add_new_product(fixture):
        driver = fixture
        login_admin(driver=driver)
        name_of_new_prod = 'DUCK_' + get_random_name(letters, 10)
        driver.find_element_by_link_text("Catalog").click()
        driver.find_element_by_link_text("Add New Product").click()
        driver.find_element_by_css_selector("label").click()
        if not driver.find_element_by_name("status").is_selected():
            driver.find_element_by_name("status").click()
        find_and_fill_element(driver, element_name='name[en]', value=name_of_new_prod)
        find_and_fill_element(driver, element_name='code', value='6')
        find_and_fill_element(driver, element_name='quantity', value='10')
        find_and_fill_element(driver, element_name='new_images[]', value=PATH_TO_DUCK_IMG)
        driver.find_element_by_name('date_valid_from').click()
        driver.find_element_by_name('date_valid_from').send_keys('25.08.2019')
        driver.find_element_by_name('date_valid_to').click()
        driver.find_element_by_name('date_valid_to').send_keys('31.12.2019')
        driver.find_element_by_link_text("Information").click()
        if not driver.find_element_by_xpath(locator_information[0]).is_selected():
            driver.find_element_by_xpath(locator_information[0]).click()
        find_and_fill_element(driver, element_name='keywords', value='my_duck')
        find_and_fill_element(driver, element_name='short_description[en]', value='my_duck')
        driver.find_element_by_link_text("Prices").click()
        driver.find_element_by_name("purchase_price").send_keys("15")
        if not driver.find_element_by_xpath(locator_price[0]).is_selected():
            driver.find_element_by_xpath(locator_price[0]).click()
        find_and_fill_element(driver, element_name='prices[USD]', value='18')
        driver.find_element_by_name("save").click()
        driver.find_element_by_id("content").click()
        driver.find_element_by_link_text("Catalog").click()
        test = "//a[text()='"+str(name_of_new_prod)+"']"
        assert_element = driver.find_elements_by_xpath(test)
        assert len(assert_element) == 1, 'Товар {} не появился в каталоге'.format(name_of_new_prod)

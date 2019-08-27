import random
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from locators import *


def test_fill_and_empty_basket(fixture):
    driver = fixture
    driver.get(website_litecart[0])
    for i in range(1, 4):
        duck_goods = driver.find_elements_by_xpath(locator_duck_goods)
        random_index = random.randint(0, len(duck_goods) - 1)
        duck_goods[random_index].find_element_by_xpath("./a[@class='link']").click()
        driver.find_element_by_name(locator_add_product).click()
        WebDriverWait(driver, 20).until(EC.text_to_be_present_in_element((By.XPATH, locator_elem_in_basket), str(i)))
        driver.get(website_litecart[0])
    driver.get(checkout[0])
    time.sleep(10)
    order = driver.find_elements_by_xpath(locator_goods_cost)
    for i in range(len(order)):
        driver.find_element_by_name(locator_remove_button).click()
        time.sleep(1)
        WebDriverWait(driver, 10).until(EC.staleness_of(order[0]))

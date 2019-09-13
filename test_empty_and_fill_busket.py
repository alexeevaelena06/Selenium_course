import time
import random
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from locators import website_litecart, checkout, locator_duck_goods, locator_add_product, locator_elem_in_basket, \
  locator_goods_cost, locator_remove_button


class TestEmptyBusket():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_fill_empty_busket(self):
    self.go_to_website(website_litecart)
    self.choose_goods()
    self.go_to_website(checkout)
    self.remove_goods_from_cart()

  def remove_goods_from_cart(self):
    # remove goods from cart
    order = self.driver.find_elements_by_xpath(locator_goods_cost)
    for i in range(len(order)):
        self.driver.find_element_by_name(locator_remove_button).click()
        time.sleep(1)
        WebDriverWait(self.driver, 10).until(EC.staleness_of(order[0]))

  def choose_goods(self):
    # choose goods
    for i in range(1, 4):
        duck_goods = self.driver.find_elements_by_xpath(locator_duck_goods)
        random_index = random.randint(0, len(duck_goods) - 1)
        duck_goods[random_index].find_element_by_xpath("./a[@class='link']").click()
        self.driver.find_element_by_name(locator_add_product).click()
        WebDriverWait(self.driver, 20).until(EC.text_to_be_present_in_element((By.XPATH, locator_elem_in_basket), str(i)))

  def go_to_website(self, url):
    # go to website
    self.driver.get(url)

from helpers import *
from locators import *


def test_new_user_registration(fixture):
    driver = fixture
    mail = generate_mail()
    driver.get(website_litecart[0])
    driver.implicitly_wait(60)
    driver.find_element_by_link_text("New customers click here").click()
    find_and_fill_element(driver, 'tax_id', "12345")
    find_and_fill_element(driver, 'company', "MyCompany")
    find_and_fill_element(driver, 'firstname', "FirstName")
    find_and_fill_element(driver, 'lastname', "LastName")
    find_and_fill_element(driver, 'address1', "MyAddress1")
    find_and_fill_element(driver, 'address2', "MyAddress2")
    find_and_fill_element(driver, 'postcode', "123456")
    find_and_fill_element(driver, 'city', "City")
    find_and_fill_element(driver, 'email', mail[0])
    find_and_fill_element(driver, 'phone', "92112345678")
    find_and_fill_element(driver, 'password', "1111")
    find_and_fill_element(driver, 'confirmed_password', "1111")

    driver.find_element_by_name("create_account").click()
    driver.find_element_by_link_text("Logout").click()

    find_and_fill_element(driver, 'password', "1111")
    find_and_fill_element(driver, 'email', mail[0])
    driver.find_element_by_name("login").click()
    driver.find_element_by_link_text("Logout").click()

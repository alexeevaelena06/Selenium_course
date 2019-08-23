import string
import random
from locators import admin_login

"""HELPERS"""

letters = string.ascii_lowercase[:12]


def login_admin(driver):
    driver.get(admin_login[1])
    driver.implicitly_wait(60)
    find_and_fill_element(driver, element_name="username", value="admin")
    find_and_fill_element(driver, element_name="password", value="admin")
    driver.find_element_by_name("login").click()


def find_and_fill_element(driver, element_name, value):
    driver.find_element_by_name(element_name).click()
    driver.find_element_by_name(element_name).clear()
    driver.find_element_by_name(element_name).send_keys(value)


def get_random_domain(domains):
    return random.choice(domains)


def get_random_name(letters, length):
    return ''.join(random.choice(letters) for i in range(length))


def generate_new_email(nb, length):
    letters = string.ascii_lowercase[:12]
    domains = ["excelian.com", "gmail.com", "mail.com", "yahoo.com", "rambler.ru", "yandex.ru"]
    return [get_random_name(letters, length) + '@' + get_random_domain(domains) for i in range(nb)]


def generate_mail():
    return generate_new_email(1, 7)

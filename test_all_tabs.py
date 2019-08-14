import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *

# Test variables

EXPECTED_SUB_TAB = [
           'Template', 'Logotype', 'Catalog', 'Product Groups', 'Option Groups', 'Manufacturers', 'Suppliers',
           'Delivery Statuses', 'Sold Out Statuses', 'Quantity Units', 'CSV Import/Export', 'Countries',
           'Currencies', 'Customers', 'CSV Import/Export', 'Newsletter', 'Geo Zones', 'Languages',
           'Storage Encoding', 'Background Jobs', 'Customer', 'Shipping', 'Payment', 'Order Total', 'Order Success',
           'Order Action', 'Orders', 'Order Statuses', 'Pages', 'Monthly Sales', 'Most Sold Products',
           'Most Shopping Customers', 'Store Info', 'Defaults', 'General', 'Listings', 'Images', 'Checkout',
           'Advanced', 'Security', 'Slides', 'Tax Classes', 'Tax Rates', 'Search Translations', 'Scan Files',
           'CSV Import/Export', 'Users', 'vQmods']

EXPECTED_H1_LIST = [
           'Template', 'Logotype', 'Catalog', 'Product Groups', 'Option Groups', 'Manufacturers', 'Suppliers',
           'Delivery Statuses', 'Sold Out Statuses', 'Quantity Units', 'CSV Import/Export', 'Countries', 'Currencies',
           'Customers', 'CSV Import/Export', 'Newsletter', 'Geo Zones', 'Languages', 'Storage Encoding', 'Job Modules',
           'Customer Modules', 'Shipping Modules', 'Payment Modules', 'Order Total Modules', 'Order Success Modules',
           'Order Action Modules', 'Orders', 'Order Statuses', 'Pages', 'Monthly Sales', 'Most Sold Products',
           'Most Shopping Customers', 'Settings', 'Settings', 'Settings', 'Settings', 'Settings', 'Settings',
           'Settings', 'Settings', 'Slides', 'Tax Classes', 'Tax Rates', 'Search Translations',
           'Scan Files For Translations', 'CSV Import/Export', 'Users', 'vQmods']


def test_tab_appereance(fixture):
    driver = fixture
    driver.get(admin_login[0])
    driver.find_element_by_name("username").send_keys(admin['login_name'])
    driver.find_element_by_name("password").send_keys(admin['login_password'])
    driver.find_element_by_name("login").click()
    WebDriverWait(driver, 10).until(EC.title_is("My Store"))
    time.sleep(2)
    displayed_tabs = []
    displayed_titles = []
    tab_list = driver.find_elements_by_xpath(locator_all_tab[0])
    for i in range(len(tab_list)):
        tab = driver.find_elements_by_xpath(locator_all_tab[0])
        tab_name = tab[i].text
        tab[i].click()
        driver.implicitly_wait(1)
        sub_menu = driver.find_elements_by_xpath(locator_sub_tab[0])
        if len(sub_menu) < 1:
            head_title = driver.find_element_by_xpath(locator_title[0]).text
            displayed_tabs.append(tab_name)
            displayed_titles.append(head_title)
        for j in range(len(sub_menu)):
            sub_menu_el = driver.find_elements_by_xpath(locator_sub_tab[0])
            sub_menu_el[j].click()
            sub_menu_el = driver.find_elements_by_xpath(locator_sub_tab[0])
            sub_m_link_name = sub_menu_el[j].text
            head_title2 = driver.find_element_by_xpath(locator_title[0]).text
            displayed_tabs.append(sub_m_link_name)
            displayed_titles.append(head_title2)
    assert displayed_tabs == EXPECTED_SUB_TAB
    assert displayed_titles == EXPECTED_H1_LIST

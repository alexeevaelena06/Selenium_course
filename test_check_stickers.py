import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *


def test_check_stickers(fixture):
    driver = fixture
    driver.get(website_litecart[0])
    displayed_stickers = []
    stickers_list = driver.find_elements_by_css_selector(locator_all_goods[0])
    for i in range(len(stickers_list)):
        sticker = driver.find_elements_by_css_selector(locator_all_stickers[0])
        sticker_name = sticker[i].text
        assert sticker_name is not None, 'Sticker is absent of image'
        displayed_stickers.append(sticker_name)
    print(displayed_stickers)
    assert len(displayed_stickers) == len(stickers_list)




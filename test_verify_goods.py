import re
from locators import *


def test_verify_goods(fixture):
    driver = fixture
    driver.get(website_litecart[0])
    driver.implicitly_wait(30)
    check_duck_list = driver.find_elements_by_css_selector(locator_duck_campaigns[0])
    goods_num = []
    link_to_goods_page = []
    goods_description = []
    goods_price = []
    discount_goods_price = []
    goods_price_style_text_decoration = []
    discount_goods_price_color = []
    goods_price_style_font_size = []
    discount_goods_price_style_font_weight = []
    discount_goods_price_style_font_size = []

    i = 0
    for duck in check_duck_list:
        goods_num.append(i)
        link_to_goods_page.append(duck.find_element_by_xpath(".//a[@class='link']").get_attribute('href'))
        goods_description.append(duck.find_element_by_xpath(locator_goods_name_in_website[0]).text)
        goods_price.append(duck.find_element_by_xpath(locator_regular_price_in_website[0]).text)
        discount_goods_price.append(duck.find_element_by_xpath(locator_discount_price_in_website[0]).text)
        goods_price_style_text_decoration.append(
            duck.find_element_by_xpath(locator_goods_price_style_text_decoration[0]).value_of_css_property(
                'text-decoration'))
        results_1 = re.findall(r'\d{3}', goods_price_style_text_decoration[0])
        assert results_1[0] == results_1[1] == results_1[2], 'Цвет регулярной цены не серый'
        goods_price_style_font_size.append(
            duck.find_element_by_xpath(locator_goods_price_style_font_size[0]).value_of_css_property('font-size'))
        discount_goods_price_style_font_weight.append(
            duck.find_element_by_xpath(locator_discount_goods_price_style_font_weight[0]).value_of_css_property(
                'font-weight'))
        discount_goods_price_color.append(duck.find_element_by_xpath(locator_discount_goods_price_style_font_weight[0]).value_of_css_property(
                'text-decoration'))
        red_results = re.findall(r'\d', discount_goods_price_color[0])
        assert red_results[-2] == red_results[-1] == '0', 'Цвет цены со скидкой не красный'
        discount_goods_price_style_font_size.append(
            duck.find_element_by_xpath(locator_discount_goods_price_style_font_size[0]).value_of_css_property(
                'font-size'))

        i = i + 1

    for j in range(len(goods_num)):
        driver.get(link_to_goods_page[j])
        goods_name_in_page = driver.find_element_by_css_selector(locator_goods_name_on_page[0]).text
        goods_price_on_page = driver.find_element_by_css_selector(locator_regular_price_on_page[0]).text
        discount_goods_price_on_page = driver.find_element_by_css_selector(locator_discount_price_on_page[0]).text
        goods_price_style_text_decoration_on_page = driver.find_element_by_xpath(
            locator_goods_price_style_text_decoration_on_page[0]).value_of_css_property('text-decoration')
        results_2 = re.findall(r'\d{3}', goods_price_style_text_decoration_on_page)
        assert results_2[0] == results_2[1] == results_2[2], 'Цвет регулярной цены не серый'
        goods_price_style_fon_size_on_page = driver.find_element_by_xpath(
            locator_goods_price_style_fon_size_on_page[0]).value_of_css_property('font-size')
        discount_goods_price_style_font_weight_on_page = driver.find_element_by_xpath(
            locator_discount_goods_price_style_font_weight_on_page[0]).value_of_css_property('font-weight')
        discount_goods_price_color_on_page = driver.find_element_by_xpath(
            locator_discount_goods_price_style_font_weight_on_page[0]).value_of_css_property('text-decoration')
        red_results_2 = re.findall(r'\d', discount_goods_price_color_on_page)
        assert red_results_2[-2] == red_results_2[-1] == '0', 'Цвет цены со скидкой не красный'
        discount_goods_price_style_font_size_on_page = driver.find_element_by_xpath(
            locator_discount_goods_price_style_font_size_on_page[0]).value_of_css_property('font-size')

        assert goods_name_in_page == goods_description[j], \
            'Название товара на сайте {} и на странице {} не одинаковы'.format(goods_description[j],
                                                                               goods_name_in_page)
        assert goods_price_on_page == goods_price[j], \
            'Цена товара на сайте {} и на странице {} не одинаковы'.format(goods_price[j], goods_price_on_page)
        assert discount_goods_price_on_page == discount_goods_price[j], \
            'Цена товара со скидкой  на сайте {} и на странице {} не одинаковы'.format(discount_goods_price[j],
                                                                                       discount_goods_price_on_page)
        assert discount_goods_price_style_font_size[j] > goods_price_style_font_size[j], \
            'Размер цены со скидкой меньше размера регулярной цены'
        assert discount_goods_price_style_font_size_on_page > goods_price_style_fon_size_on_page, \
            'Размер цены со скидкой меньше размера регулярной цены'
        assert discount_goods_price_style_font_weight_on_page == discount_goods_price_style_font_weight[j]

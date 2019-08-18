"""""Path to website"""""

admin_login = ['http://localhost/litecart/admin/']

website_litecart = ['http://localhost/litecart/en/']

page_countries = ['http://localhost/litecart/admin/?app=countries&doc=countries']

page_geozones = ['http://localhost/litecart/admin/?app=geo_zones&doc=geo_zones']

admin = {'login_name': 'admin', 'login_password': 'admin'}

"""""Locators of elements"""""

locator_litecart = ['div a img[title="My Store"]']

locator_all_tab = ["//*[@id='app-']/a/span[2]"]

locator_sub_tab = ["//ul[@class='docs']//li//span"]

locator_title = [".//*[@id='content']/h1"]

locator_all_stickers = ["div.sticker"]

locator_all_goods = ["div img.image"]

locator_all_countries = ["tr.row td:nth-child(5) a"]

locator_all_geozones = ["tr.row td:nth-child(6)"]

locator_all_towns = ["table.dataTable tr td:nth-child(3)"]

locator_countries = ["div[id='box-apps-menu-wrapper'] li:nth-child(3)"]

locator_geozones = [".//*[@id='content']/form/table/tbody/tr[@class='row']/td [not(contains (@style,'text'))]/a"]

locator_town_in_geozones = [".//*[@id='table-zones']/tbody/tr/td/select[starts-with(@name,'zones[') and not(contains (@aria-hidden,'true'))]/option[@selected='selected']"]

locator_duck_campaigns = ["div[id='box-campaigns'] ul.listing-wrapper.products li"]

locator_goods_name_in_website = [".//div[@class='name']"]

locator_goods_name_on_page = ["h1.title"]

locator_regular_price_in_website = [".//div[@class='price-wrapper']/s"]

locator_discount_price_in_website = [".//strong[@class='campaign-price']"]

locator_regular_price_on_page = ["#box-product > div.content > div.information > div.price-wrapper > s"]

locator_discount_price_on_page = ["#box-product > div.content > div.information > div.price-wrapper > strong"]

locator_goods_price_style_font_size = ["//s[@class='regular-price']"]

locator_discount_goods_price_style_font_weight = ["//strong[@class='campaign-price']"]

locator_discount_goods_price_style_font_size = ["//strong[@class='campaign-price']"]

locator_goods_price_style_fon_size_on_page = [".//*[@id='box-product']//div[@class='information']//div[@class='price-wrapper']/s"]

locator_discount_goods_price_style_font_weight_on_page = [".//*[@id='box-product']//div[@class='information']//div[@class='price-wrapper']/strong"]

locator_discount_goods_price_style_font_size_on_page = [".//*[@id='box-product']//div[@class='information']//div[@class='price-wrapper']/strong[@class='campaign-price']"]

locator_goods_price_style_text_decoration = ["//s[@class='regular-price']"]

locator_goods_price_style_text_decoration_on_page = [".//*[@id='box-product']//div[@class='information']//div[@class='price-wrapper']/s"]

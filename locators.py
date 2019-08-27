"""""Path to website"""""

admin_login = ['http://localhost/litecart/admin/']

website_litecart = ['http://localhost/litecart/en/']

page_countries = ['http://localhost/litecart/admin/?app=countries&doc=countries']

page_geozones = ['http://localhost/litecart/admin/?app=geo_zones&doc=geo_zones']

admin = {'login_name': 'admin', 'login_password': 'admin'}

checkout = ["http://localhost/litecart/en/checkout"]

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

locator_add_product = "add_cart_product"

locator_duck_goods = ".//ul[@class='listing-wrapper products']//li"

locator_elem_in_basket = ".//*[ @ id = 'cart']//a//span[@class='quantity']"

locator_goods_cost = ".//*[@id='order_confirmation-wrapper']/table/tbody/tr/td[@class='unit-cost']"

locator_remove_button = "remove_cart_item"

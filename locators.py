"""""Path to website"""""

admin_login = ['http://localhost/litecart/admin/', 'http://localhost/litecart/admin/login.php']

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

locator_information = ["//div[@id='tab-information']//select[normalize-space(.)='-- Select -- ACME Corp.']//option[2]"]

locator_price = ["//div[@id='tab-prices']/table[1]/tbody/tr/td/select//option[2]"]

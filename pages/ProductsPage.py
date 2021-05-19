from driver_interactions.ElementsInteractions import ElementsInteractions
import utilities.Logger as Log
import time
import random

class ProductsPage(ElementsInteractions):

    log = Log.func_logger()

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    xpath_title_header = "//*[@id='header_container']/div[2]/span"
    id_menu_button = "react-burger-menu-btn"
    id_logout_menu_option = "logout_sidebar_link"
    class_sort_container = "product_sort_container"
    class_item_price_lbl = "inventory_item_price"
    class_add_to_cart_button = "btn_inventory"
    class_product_name_lbl = "inventory_item_name"
    class_shopping_cart_button = "shopping_cart_link"

    def validate_title_header(self):
        text = self.get_text(self.xpath_title_header, "xpath")
        self.log.info(text)
        if text != "PRODUCTS":
            assert False

    def click_menu_button(self):
        self.click_element(self.id_menu_button, "id")

    def click_logout_menu_option(self):
        time.sleep(1)
        self.click_element(self.id_logout_menu_option, "id")

    def sort_price_low_to_high(self):
        self.select_by_value(self.class_sort_container, "class", "lohi")

    def validate_price_order(self):
        elements = self.get_all_elements(self.class_item_price_lbl, "class")
        prices_list = []
        for element in elements:
            prices_list.append(float(element.text.replace("$", "")))
        if prices_list != sorted(prices_list):
            self.log.info("Products do not sorted")
            assert False

    def add_multiple_products(self):
        btn_add_to_cart = self.get_all_elements(self.class_add_to_cart_button, "class")
        number_product_one = random.randrange(len(btn_add_to_cart)-1)
        number_product_two = random.randrange(len(btn_add_to_cart)-1)
        btn_add_to_cart[number_product_one].click()
        btn_add_to_cart[number_product_two].click()
        product_names = self.get_all_elements(self.class_product_name_lbl, "class")
        return product_names[number_product_one].text, product_names[number_product_two].text

    def add_specific_product(self, specific_product_name):
        product_names = self.get_all_elements(self.class_product_name_lbl, "class")
        cont = 0
        for element in product_names:
            product_name = element.text
            if product_name == specific_product_name:
                break
            else:
                cont += 1
        products = self.get_all_elements(self.class_add_to_cart_button, "class")
        products[cont].click()

    def click_shopping_cart_button(self):
        self.click_element(self.class_shopping_cart_button, "class")

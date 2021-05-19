from driver_interactions.ElementsInteractions import ElementsInteractions
import utilities.Logger as Log

class ShoppingCartPage(ElementsInteractions):

    log = Log.func_logger()

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    xpath_title_header = "//*[@id='header_container']/div[2]/span"
    class_product_name_lbl = "inventory_item_name"
    id_checkout_button = "checkout"

    def validate_title_header(self):
        text = self.get_text(self.xpath_title_header, "xpath")
        self.log.info(text)
        if text != "YOUR CART":
            assert False

    def verify_added_products(self, products_names):
        elements = self.get_all_elements(self.class_product_name_lbl, "class")
        products_names_cart = []
        for element in elements:
            products_names_cart.append(element.text)
        for product_name in products_names:
            if product_name not in products_names:
                self.log.info("Product is not in cart")
                assert False

    def click_checkout_button(self):
        self.click_element(self.id_checkout_button, "id")

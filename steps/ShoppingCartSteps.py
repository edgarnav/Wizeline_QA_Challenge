from behave import given, when, then
from pages.LoginPage import LoginPage
from pages.ProductsPage import ProductsPage
from pages.ShoppingCartPage import ShoppingCartPage
import config_file.ConfigFile as Configs

class ShoppingCartSteps:

    product_names = []

    @given("Prepare classes shopping cart")
    def prepare_class(context):
        context.login = LoginPage(context.driver)
        context.products = ProductsPage(context.driver)
        context.shopping_cart = ShoppingCartPage(context.driver)

    @when("Click shopping cart button")
    def click_shopping_cart_button(context):
        context.products.click_shopping_cart_button()

    @then("Verify shopping cart page")
    def verify_shopping_cart_page(context):
        context.shopping_cart.validate_title_header()

    @when("Add multiple products")
    def add_multiple_products(context):
        context.product_names = []
        context.product_names = context.products.add_multiple_products()

    @then("Verify added products")
    def verify_added_products(context):
        context.shopping_cart.verify_added_products(context.product_names)

    @when("Add specific product to cart")
    def add_specific_product(context):
        context.products.add_specific_product(Configs.specific_product)
        context.product_names = []
        context.product_names.append(Configs.specific_product)

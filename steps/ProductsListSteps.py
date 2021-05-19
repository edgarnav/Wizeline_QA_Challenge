from behave import given, when, then
from pages.LoginPage import LoginPage
from pages.ProductsPage import ProductsPage

class ProductsListSteps:

    @given("Prepare classes products list")
    def prepare_class(context):
        context.login = LoginPage(context.driver)
        context.products = ProductsPage(context.driver)

    @when("Sort by price low to high")
    def sort_low_to_high(context):
        context.products.sort_price_low_to_high()

    @then("Validate price order")
    def validate_price_order(context):
        context.products.validate_price_order()

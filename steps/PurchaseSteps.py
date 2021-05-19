from behave import given, when, then
from pages.LoginPage import LoginPage
from pages.ProductsPage import ProductsPage
from pages.ShoppingCartPage import ShoppingCartPage
from pages.UserInformationPage import UserInformationPage
from pages.OverviewPage import OverviewPage
from pages.CompletePage import CompletePage
import config_file.ConfigFile as Configs

class PurchaseSteps:

    @given("Prepare classes purchase")
    def prepare_classes_purchase(context):
        context.login = LoginPage(context.driver)
        context.products = ProductsPage(context.driver)
        context.shopping_cart = ShoppingCartPage(context.driver)
        context.user_information = UserInformationPage(context.driver)
        context.overview = OverviewPage(context.driver)
        context.complete = CompletePage(context.driver)

    @when("Click checkout button")
    def click_checkout_button(context):
        context.shopping_cart.click_checkout_button()

    @then("Validate information page")
    def verify_information_page(context):
        context.user_information.validate_title_header()

    @when("Send personal information")
    def send_personal_information(context):
        context.user_information.send_personal_information(Configs.first_name, Configs.last_name, Configs.postal_code)

    @then("Click continue button")
    def click_continue_button(context):
        context.user_information.click_continue_button()

    @then("Validate overview page")
    def validate_overview_page(context):
        context.overview.validate_title_header()

    @when("Click finish button")
    def click_finish_button(context):
        context.overview.click_finish_button()

    @then("Verify complete page")
    def validate_complete_page(context):
        context.complete.validate_title_header()


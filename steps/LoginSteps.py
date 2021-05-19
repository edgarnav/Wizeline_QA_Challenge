from behave import given, when, then
from pages.LoginPage import LoginPage
from pages.ProductsPage import ProductsPage
import config_file.ConfigFile as Configs

class LoginSteps:

    @given("Prepare classes login")
    def prepare_class(context):
        context.login = LoginPage(context.driver)
        context.products = ProductsPage(context.driver)

    @then("Validate login page")
    def validate_login_page(context):
        context.login.validate_login_page()

    @when("Send user and password")
    def send_user_password(context):
        context.login.send_user_text(Configs.user)
        context.login.send_password_text(Configs.password)

    @then("Press login button")
    def press_login_button(context):
        context.login.click_login_btn()

    @then("Validate products page")
    def validate_products_page(context):
        context.products.validate_title_header()

    @when("Send invalid user and password")
    def send_user_password(context):
        context.login.send_user_text(Configs.invalid_user)
        context.login.send_password_text(Configs.password)

    @then("Validate error message")
    def validate_error_message(context):
        context.login.validate_error_message()

    @when("Click menu button")
    def click_menu_button(context):
        context.products.click_menu_button()

    @then("Click logout option")
    def click_logout_option(context):
        context.products.click_logout_menu_option()

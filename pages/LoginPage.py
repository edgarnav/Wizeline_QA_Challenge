from driver_interactions.ElementsInteractions import ElementsInteractions

class LoginPage(ElementsInteractions):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    class_login_logo = "login_logo"
    id_user_input = "user-name"
    id_password_input = "password"
    id_login_btn = "login-button"
    class_error_message = "error-message-container"

    def validate_login_page(self):
        self.is_element_displayed(self.class_login_logo, "class")

    def send_user_text(self, user):
        self.send_text(user, self.id_user_input, "id")

    def send_password_text(self, password):
        self.send_text(password, self.id_password_input, "id")

    def click_login_btn(self):
        self.click_element(self.id_login_btn, "id")

    def validate_error_message(self):
        self.is_element_displayed(self.class_error_message, "class")

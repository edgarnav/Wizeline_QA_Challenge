from driver_interactions.ElementsInteractions import ElementsInteractions
import utilities.Logger as Log

class UserInformationPage(ElementsInteractions):

    log = Log.func_logger()

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    xpath_title_header = "//*[@id='header_container']/div[2]/span"
    id_first_name_input = "first-name"
    id_last_name_input = "last-name"
    id_postal_code_input = "postal-code"
    id_continue_button = "continue"

    def validate_title_header(self):
        text = self.get_text(self.xpath_title_header, "xpath")
        self.log.info(text)
        if text != "CHECKOUT: YOUR INFORMATION":
            assert False

    def send_personal_information(self, first_name, last_name, postal_code):
        self.send_text(first_name, self.id_first_name_input, "id")
        self.send_text(last_name, self.id_last_name_input, "id")
        self.send_text(postal_code, self.id_postal_code_input, "id")

    def click_continue_button(self):
        self.click_element(self.id_continue_button, "id")

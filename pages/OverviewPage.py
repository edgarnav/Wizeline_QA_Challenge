from driver_interactions.ElementsInteractions import ElementsInteractions

class OverviewPage(ElementsInteractions):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    xpath_title_header = "//*[@id='header_container']/div[2]/span"
    id_finish_button = "finish"

    def validate_title_header(self):
        text = self.get_text(self.xpath_title_header, "xpath")
        self.log.info(text)
        if text != "CHECKOUT: OVERVIEW":
            assert False

    def click_finish_button(self):
        self.click_element(self.id_finish_button, "id")

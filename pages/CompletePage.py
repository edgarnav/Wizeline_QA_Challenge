from driver_interactions.ElementsInteractions import ElementsInteractions

class CompletePage(ElementsInteractions):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    xpath_title_header = "//*[@id='header_container']/div[2]/span"

    def validate_title_header(self):
        text = self.get_text(self.xpath_title_header, "xpath")
        self.log.info(text)
        if text != "CHECKOUT: COMPLETE!":
            assert False
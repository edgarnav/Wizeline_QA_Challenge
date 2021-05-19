from driver_interactions.WebDriver import WebDriver
from driver_interactions.ElementsInteractions import ElementsInteractions
import utilities.Logger as Log
import config_file.ConfigFile as Configs

log = Log.func_logger()

def before_all(context):
    log.info("Script started")

def after_all(context):
    log.info("Script ended")

def before_scenario(context, scenario):
    context.prepare_driver = WebDriver()
    context.driver = context.prepare_driver.init_web_driver()
    context.bp = ElementsInteractions(context.driver)
    context.bp.launch_web_page(Configs.url)

def after_scenario(context, scenario):
    context.driver.quit()

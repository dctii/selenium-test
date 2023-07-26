import allure

from src.allocator.driver import Driver
from src.config.base_config import url


def before_all(context):
    context.mode = context.config.userdata["mode"]
    context.env = (
        url["app_url"]
        if "None" in context.config.userdata["env"]
        else context.config.userdata["env"]
    )

    if context.config.userdata["browser"] in [
        "chrome",
        "firefox",
        "edge",
        "safari",
        "mobile",
    ]:
        context.browser = context.config.userdata["browser"]
    else:
        context.browser = "chrome"


def before_scenario(context, scenario):
    driver_instance = Driver(context)
    context.driver = driver_instance.get_driver()
    context.driver.delete_all_cookies()
    context.driver.refresh()


def after_step(context, step):
    if step.status == "failed":
        allure.attach(
            body=context.driver.get_screenshot_as_png(),
            name="Screenshot",
            attachment_type=allure.attachment_type.PNG,
        )
        allure.attach(
            body=context.driver.current_url,
            name="CurrentUrl",
            attachment_type=allure.attachment_type.URI_LIST,
        )
        log = context.driver.get_log("browser")
        log_result = "\n".join([i["message"] for i in log])
        allure.attach(
            body=log_result,
            name="ConsoleLog",
            attachment_type=allure.attachment_type.TEXT,
        )

    context.driver.quit()

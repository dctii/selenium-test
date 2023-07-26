import platform
import os
import shutil
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import datetime

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.options import Options as EdgeOptions

from utils.dirs import get_root_dir, get_curr_dir


class Driver(object):
    def __init__(self, context):
        self.driver = None
        self.browser = context.browser
        self.mode = context.mode

    def get_driver(self):
        web_driver = getattr(self, self.browser)
        return web_driver()

    def chrome(self):
        if platform.system() == 'Darwin' and platform.machine() == 'arm64':
            return self.chrome_mac_arm64()
        else:
            return self.chrome_default()

    def chrome_mac_arm64(self):
        desired_capabilities = DesiredCapabilities.CHROME
        options = self.set_chrome_browser_options_arguments(self)
        root_dir = get_root_dir(get_curr_dir(__file__))
        web_drivers_dir = f"{root_dir}/test/resources/browserdrivers"
        chrome_binary_path = f"{web_drivers_dir}/chromedriver_mac_arm64"
        chrome_app_path = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'

        if not os.path.exists(chrome_app_path):
            print("Google Chrome is not installed. Installing now...")
            os.system("brew install --cask google-chrome")
            print("Installation finished. If the script fails, please run it again.")

        options.binary_location = chrome_app_path
        return webdriver.Chrome(
            chrome_options=options,
            desired_capabilities=desired_capabilities,
            executable_path=chrome_binary_path
        )

    def chrome_default(self):
        desired_capabilities = DesiredCapabilities.CHROME
        options = self.set_chrome_browser_options_arguments(self)
        return webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()),
            chrome_options=options,
            desired_capabilities=desired_capabilities,
        )

    def firefox(self):
        profile = webdriver.FirefoxProfile()
        options = FirefoxOptions()
        if self.mode == "headless":
            options.headless = True
        browser = webdriver.Firefox(
            firefox_profile=profile,
            options=options,
            service=FirefoxService(GeckoDriverManager().install()),
        )
        browser.maximize_window()
        return browser

    def edge(self):
        options = EdgeOptions()
        options.add_argument("window-size=2000,2000")
        options.add_argument("user-agent=works0upkeep*couch.persuade-domicile")
        if self.mode == "headless":
            options.add_argument("--headless")
        browser = webdriver.Edge(
            options=options, service=EdgeService(EdgeChromiumDriverManager().install())
        )
        browser.maximize_window()
        return browser

    @staticmethod
    def safari():
        desired_capabilities = DesiredCapabilities.SAFARI
        browser = webdriver.Safari(desired_capabilities=desired_capabilities)
        browser.set_window_size(1400, 900)
        browser.maximize_window()
        return browser

    def mobile(self):
        print("Using Chrome with mobile Emulation")
        desired_capabilities = DesiredCapabilities.CHROME
        options = ChromeOptions()
        if self.mode == "headless":
            options.add_argument("--no-sandbox")
            options.add_argument("--headless")
        mobile_emulation = {"deviceName": "iPhone 12 Pro"}

        options.add_experimental_option("mobileEmulation", mobile_emulation)
        return webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()),
            chrome_options=options,
            desired_capabilities=desired_capabilities,
        )

    @staticmethod
    def set_chrome_browser_options_arguments(self):
        options = ChromeOptions()
        if self.mode == "headless":
            options.add_argument("--no-sandbox")
            options.add_argument("--headless")
        options.add_argument("--window-size=2000,2000")
        options.add_argument("--ignore-certificate-errors")
        options.add_argument("user-agent=works0upkeep*couch.persuade-domicile")
        options.add_argument("--disable-logging")
        return options

    def capture_screenshots_for_jira(self):
        path = os.getcwd() + "/temp"
        if os.path.exists(path):
            shutil.rmtree(path)
        os.mkdir(path)
        path_to_capture_screenshot = (
                path + "/" + str(datetime.datetime.now().timestamp()) + ".png"
        )
        self.driver.get_screenshot_as_file(
            path_to_capture_screenshot
        )  # need to refactor this line
        return path_to_capture_screenshot

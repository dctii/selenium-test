import os
import json


class Settings(object):

    def __init__(self):
        with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'test_settings.json')) as f:
            setting = json.load(f)
            self.url = setting['url']
            self.url_sandbox = setting['url_sandbox']
            self.browser = setting['browser']
            self.driver_timeout = int(setting['driver_timeout'])
            self.outlook_password = setting['outlook_password']
            self.wait_time = setting['wait_time']
            self.use_proxy = setting['use_proxy']
            self.proxy = setting['proxy']


settings = Settings()

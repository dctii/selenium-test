import src.config.base_config as config


class Reusable:
    def __init__(self, context):
        self.driver = context.driver
        self.timeout = config.default_wait

    def visit(self, url):
        self.driver.get(url)
        self.driver.refresh()
        print(f"Visiting url: {url}")
        return self

from src.allocator.reusables import Reusable


class UrlNavigationPage(Reusable):
    def __init__(self, context):
        Reusable.__init__(self, context)

    def visit_url(self, url):
        self.visit(url)

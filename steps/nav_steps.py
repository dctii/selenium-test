from behave import step

from src.pages.url_navigation_page import UrlNavigationPage


@step('I navigate to the home page')
def homepage_nav(context):
    UrlNavigationPage(context).visit_url(context.env)


@step('I navigate to the example dot com')
def homepage_nav(context):
    UrlNavigationPage(context).visit_url('https://www.example.com')
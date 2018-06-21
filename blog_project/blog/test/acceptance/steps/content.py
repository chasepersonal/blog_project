from behave import *

from blog_project.blog.test.acceptance.page_model.base_page import BasePage

use_step_matcher('re')

@then('there is a title shown on the page')
def step_impl(context):
    page = BasePage(context.browser)
    assert page.title.is_displayed()
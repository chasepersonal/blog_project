from behave import *
from selenium import webdriver

# Allows steps to receive arguments from the feature file
# Can use regular expression to extract variable elements

use_step_matcher('re')

@given('I am on the Welcome page')
# Implement step function
# Context allows
# Step functions can be the same as decorators are different
# Will differentiate with feature text
def step_impl(context):
    context.browser = webdriver.Chrome()
    context.browser.get('http://localhost:8000')

@given('I am on the blog page')
def step_impl(context):
    context.browser = webdriver.Chrome()
    context.browser.get('http://localhost:8000/post_list')

@then('I am on the blog page')
def step_impl(context):
    expected_url = 'http://localhost:8000/post_list/'
    assert context.browser.current_url == expected_url
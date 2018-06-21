from behave import *
from selenium import webdriver

# Allows steps to receive arguments from the feature file
use_step_matcher('re')

# All characters between the "()" will be imported as a variable
@when('I click on the "(.*)" link')
def step_impl(context, link_name):
    link = context.browser.find_element_by_link_text(link_name)
    link.click()
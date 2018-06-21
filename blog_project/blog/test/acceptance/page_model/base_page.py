from blog_project.blog.test.acceptance.locators.base_page import BasePageLocators


class BasePage:
    def __init__(self, browser):
        self.browser = browser

    @property
    def url(self):
        return 'http://localhost:8000'

    @property
    def title(self):
        return self.browser.find_element(*BasePageLocators.TITLE)

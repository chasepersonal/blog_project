from blog_project.blog.test.acceptance.locators.welcome_page import WelcomePageLocators
from blog_project.blog.test.acceptance.page_model.base_page import BasePage


class WelcomePage(BasePage):

    @property
    def url(self):
        return super(WelcomePage, self).url + '/'

    @property
    def blog_link(self):
        return self.browser.find_element(*WelcomePageLocators.NAVIGATION_LINK)
from django.test import TestCase, Client

class TestNavigation(TestCase):
    # Set up client object to retrieve url patters to test routing
    def setUp(self):
        self.client = Client()

    # Test that link to home page works
    def test_index_page(self):
        index_page = client.get('')
        self.assertTemplateUsed(index_page, 'index.html')

    # Test that link to about page works
    def test_about_page(self):
        about_page = client.get('about/')
        self.asserTemplateUsed(about_page, 'about.html')

    # Test that link to portfolio page works
    def test_portfolio_page(self):
        portfolio_page = client.get('portfolio/')
        self.assertTemplateUsed(portfolio_page, 'portfolio.html')

    # Test that link to looking for page works
    def test_looking_for_page(self):
        looking_for_page = client.get('looking_for/')
        self.assertTemplateUsed(looking_for_page, 'looking_for.html')

    # Test that link to resume page works
    def test_resume_page(self):
        resume_page = client.get('resume/')
        self.assertTemplateUsed(resume_page, 'resume.html')

    # Test that link to blog posts page works
    def test_post_list_page(self):
        post_list_page = client.get('post_list/')
        self.assertTemplateUsed(post_list_page, 'post_list.html')

    # Test that link to contact page works
    def test_contact_page(self):
        contact_page = client.get('contact/')
        self.assertTemplateUsed(contact_page, 'contact.html')

    # Test that link to success page works
    def test_success_page(self):
        success_page = client.get('success/')
        self.assertTemplateUsed(success_page, 'contact.html')
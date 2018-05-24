# import unicode, shortcuts, and models for rendering views

from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Post
from django.views.generic import TemplateView
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from .forms import ContactForm
from django.core.mail import get_connection, send_mail, EmailMessage, BadHeaderError
from django.template.loader import get_template
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings

# A list of posts will be displayed to the user

def post_list(request):
    posts_list = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')

    # Create variable for page list and set limit

    paginator = Paginator(posts_list, 4)

    # Get appropriate page number for post and set default to page 1

    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1

    # Get appropriate posts for page and check for invalid or empty pages

    try:
        posts = paginator.page(page)
    except(EmptyPage, InvalidPage):
        posts = paginator.page(paginator.num_pages)

    return render(request, 'blog/post_list.html', { 'posts' : posts })

# Contact form will display to the user

def contact(request):
    
    # Upon posting informaiton, gather the post data

    if request.method == 'POST':
        form = ContactForm(request.POST)
        
        # If there are no errors with the form, compile information and send e-mail
        
        if form.is_valid():
            contact_name = request.POST.get(
                'contact_name'
            , '')
            contact_email = request.POST.get(
                'contact_email'
            , '')
            message = request.POST.get('message', '')

            template = get_template('contact_template.txt')
            context = {
                'contact_name': contact_name,
                'contact_email': contact_email,
                'message': message,
            }
            content = template.render(context)

            email = EmailMessage(
                "New contact form submission: ",
                content,
                to=['chase.p.weyer@gmail.com'],
                headers = {'Reply-To': contact_email }
            )

            # Try to send e-mail unless there is a BadHeaderError

            try:
                email.send()
            except BadHeaderError:
                return HttpResponse('Invalid Header found.')
            else:
                return redirect('success')
        
    # If there are errors with the form, return to the form page

    else:
        form = ContactForm()

    return render(request, 'blog/contact.html', { 'form': form })

# Classes for static page views so they can import templates

class IndexPageView(TemplateView):
    template_name = "index.html"
    
class AboutPageView(TemplateView):
    template_name = "about.html"

class PortfolioPageView(TemplateView):
    template_name = "portfolio.html"

class LookingForPageView(TemplateView):
    template_name = "looking_for.html"

class ResumePageView(TemplateView):
    template_name = "resume.html"

class SuccessPageView(TemplateView):
    template_name = "success.html"


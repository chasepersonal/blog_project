# import unicode, shortcuts, and models for rendering views

from __future__ import unicode_literals

from django.shortcuts import render

from django.utils import timezone

from .models import Post

from django.views.generic import TemplateView

# A list of posts will be displayed to the user

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

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

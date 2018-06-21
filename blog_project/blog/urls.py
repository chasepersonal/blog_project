# import configuration for urls and view controls
from django.conf.urls import url
from . import views

# Establish url patterns for the blog app

urlpatterns = [
    url(r'^$', views.IndexPageView.as_view(), name='index'),
    url(r'^about/$', views.AboutPageView.as_view(), name='about'),
    url(r'^portfolio/$', views.PortfolioPageView.as_view(), name='portfolio'),
    url(r'^looking_for/$', views.LookingForPageView.as_view(), name='looking_for'),
    url(r'^resume/$', views.ResumePageView.as_view(), name='resume'),
    url(r'^post_list/$', views.post_list, name='post_list'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^success/$', views.SuccessPageView.as_view(), name='success'),
]

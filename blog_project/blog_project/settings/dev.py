# Django Development Settings

# Import necessary libraries

import os
from blog_project.settings.base import *

# Secret Key

SECRET_KEY = "yol#r_w_==rr%$!5%j0wqh)wcu^uvl-d9%(*&n+u*7c&0kfag0"

# Allowed Hosts for website

ALLOWED_HOSTS = ['127.0.0.1']

# Debug turned to true for development

DEBUG = True

# Database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'blog_project',
        'USER': 'admin_blog_project',
        'PASSWORD': 'IH@t3P30pl3!',
        'HOST': 'localhost',
        'PORT':'',
    }
 }


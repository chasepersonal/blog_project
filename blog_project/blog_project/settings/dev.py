# Django Development Settings

# Import necessary libraries

import os
from base.py import *

# Secret Key

SECRET_KEY = os.environ.get('SECRET_KEY', '')

# Allowed Hosts for website

ALLOWED_HOSTS = ['127.0.0.1']


# Database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'blog_project',
        'USER': 'admin_blog_project',
        'PASSWORD': os.environ.get('BLOG_PROJECT_DB_PASS', ''),
        'HOST': 'localhost',
        'PORT':'',
    }
}


# Django Production Settings

# Import necessary libraries

import os
from blog_project.settings.base import *

# Secret Key

SECRET_KEY = os.environ.get('SECRET_KEY')

# Allowed Hosts for website

ALLOWED_HOSTS = ['metalhero87.pythonanywhere.com']

# Debut turned off for production

DEBUG = False

# Database

DATABASES = { 
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get('DATABASE_NAME',''),
        'USER': os.environ.get('DATABASE_USER',''),
        'PASSWORD': os.environ.get('DATABASE_PASS', ''),
        'HOST': os.environ.get('DATABASE_HOST','')
        'PORT':'',
    }
}



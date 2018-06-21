#Django base settings

import os
import sys

# Build paths inside the project that will link from the base path

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ALLOWED_HOSTS = ['127.0.0.1']

# Secret Key
SECRET_KEY = 'yol#r_w_==rr%$!5%j0wqh)wcu^uvl-d9%(*&n+u*7c&0kfag0'

# Debug set to True for Development Purposes
DEBUG = True

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

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog',
    'widget_tweaks',
]

# Middleware

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

#Root URL

ROOT_URLCONF = 'blog_project.urls'

# Templates

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

#WSGI

WSGI_APPLICATION = 'blog_project.wsgi.application'



# Password validation


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Routing for fixtures

FIXTURE_DIRS = (
    '~/Documents/Django/Projects/blog_project/fixtures/',
)

# Internationalization

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)


STATIC_URL = '/static/'

# Look for static files not tied to an app

STATICFILES_DIR = (
    os.path.join(BASE_DIR, 'static'),
)

# Collect static files to be used in one place

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Settings to allow e-mail to send from app to a server

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'chase.p.weyer@gmail.com'
EMAIL_HOST_PASSWORD = '@n0th3r$3cur3P@$$wyrd'
EMAIL_PORT = 587

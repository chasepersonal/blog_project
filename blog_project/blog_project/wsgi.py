"""
WSGI config for blog_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# Environment Variables

os.environ["SECRET_KEY"] = "yol#r_w_==rr%$!5%j0wqh)wcu^uvl-d9%(*&n+u*7c&0kfag0"
os.environ["BLOG_PROJECT_DB_PASS"] = "IH@t3P30pl3!"

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "blog_project.settings")

application = get_wsgi_application()

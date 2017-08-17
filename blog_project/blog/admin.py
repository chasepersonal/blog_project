# Manage imports
from __future__ import unicode_literals

from django.contrib import admin

from .models import Post

# Home Page View

admin.site.register(Post)

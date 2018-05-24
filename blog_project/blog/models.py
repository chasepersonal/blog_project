# Import Utilities

from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django import forms


# Variable definitions for the Post class

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=255)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    # Publish each post with in the timezone of the user

    def publish(self):
        self.pubished_date=timezone.now()
        self.save()

    def __str__(self):
        return self.title

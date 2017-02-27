from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
    user_name = models.CharField(max_length=200)
    user_password = models.CharField(max_length=200)
    user_email = models.CharField(max_length=255)
    def __str__(self):
        return self.user_password
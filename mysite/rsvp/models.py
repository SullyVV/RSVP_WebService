from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Event(models.Model):
    created_by = models.ForeignKey('userAuth.User')
    title = models.CharField(max_length=50)
    descrption = models.CharField(max_length=200)
    date = models.DateField(auto_now_add=True)
    place = models.CharField(max_length=50)
    plusOne = models.BooleanField(default=False)
    def __str__(self):
        return self.title


class Guest(models.Model):
    event = models.ForeignKey('rsvp.Event')
    user = models.ForeignKey('userAuth.User')
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=200)
    comment = models.CharField(max_length=200)
    def __str__(self):
        return self.name

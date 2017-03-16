from django.db import models
from django.contrib.auth.models import User

'''
class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.EmailField()
    def __str__(self):
        return str(self.username)
'''


class Event(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    owner_name = models.CharField(max_length=50, default="admin")
    vender_name = models.CharField(max_length=50, default="admin")
    title = models.CharField(max_length=50)
    descrption = models.CharField(max_length=200)
    event_time = models.CharField(max_length=50,default="1/1/1970")
    place = models.CharField(max_length=50)
    plusOne = models.BooleanField(default=False)
    isFinal = models.BooleanField(default=False)
    venderPermitted = models.BooleanField(default=True)
    totalCounts = models.IntegerField(default=0)
    def __str__(self):
        return self.title + " -- " + str(self.id)

class Answer(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    event_title = models.CharField(max_length=50, default="none")
    answered_by = models.ForeignKey(User, on_delete=models.CASCADE)
    answer_name = models.CharField(max_length=50, default="admin")
    comment = models.CharField(max_length=200, default="none")
    plusOne = models.BooleanField(default=False)
    willCome = models.BooleanField(default=False)
    count = models.IntegerField(default=0)
    isEditable = models.BooleanField(default=True)
    def __str__(self):
        return str(self.event.title) + " -- " + str(self.answered_by)

class Relationship(models.Model):
    event_title = models.CharField(max_length=50)
    guest_name = models.CharField(max_length=50)
    isAnswered = models.BooleanField(default=False)
    isFinal = models.BooleanField(default=False)
    def __str__(self):
        return self.event_title + " -- " + self.guest_name

class Vender(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    event_title = models.CharField(max_length=50)
    vender = models.ForeignKey(User, on_delete=models.CASCADE)
    vender_name = models.CharField(max_length=50)
    def __str__(self):
        return self.event_title + " -- " + self.vender_name
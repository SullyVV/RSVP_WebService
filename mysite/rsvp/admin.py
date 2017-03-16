from django.contrib import admin
from django.contrib.auth.models import User
from .models import Event, Answer, Relationship, Vender

# Register your models here.
admin.site.unregister(User)
admin.site.register(User)
admin.site.register(Event)
admin.site.register(Answer)
admin.site.register(Relationship)
admin.site.register(Vender)
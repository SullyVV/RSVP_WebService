from django.contrib import admin
from .models import User, Event, Answer, Relationship, Vender

# Register your models here.
admin.site.register(User)
admin.site.register(Event)
admin.site.register(Answer)
admin.site.register(Relationship)
admin.site.register(Vender)
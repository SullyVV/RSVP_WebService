from django.contrib import admin
from .models import Question, User, Event, Answer, Relationship, Vender

# Register your models here.
admin.site.register(Question)
admin.site.register(User)
admin.site.register(Event)
admin.site.register(Answer)
admin.site.register(Relationship)
admin.site.register(Vender)
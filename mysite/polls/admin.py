from django.contrib import admin
from .models import Question, User, Event, Answer

# Register your models here.
admin.site.register(Question)
admin.site.register(User)
admin.site.register(Event)
admin.site.register(Answer)
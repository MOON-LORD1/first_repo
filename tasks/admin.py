from django.contrib import admin
from .models import Task, Answer, Profile

# Register your models here.
admin.site.register(Task)
admin.site.register(Answer)
admin.site.register(Profile)
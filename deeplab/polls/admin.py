from django.contrib import admin
from .models import Question

# Register your models here.

# give administrator access to questions
admin.site.register(Question)

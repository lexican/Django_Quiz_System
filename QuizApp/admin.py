from django.contrib import admin

# Register your models here.
from .models import Quiz, Scores
admin.site.register(Quiz)
admin.site.register(Scores)


from django.contrib import admin
from .models import TuitionPost

class TuitionModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'duration', 'class_of_student', 'days_per_week', 'required_qualification', 'description']

admin.site.register(TuitionPost, TuitionModelAdmin)

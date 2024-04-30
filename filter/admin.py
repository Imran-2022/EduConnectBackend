from django.contrib import admin
from .models import Filter

class FilterModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']  # Customize the fields displayed in the admin list view

admin.site.register(Filter, FilterModelAdmin)

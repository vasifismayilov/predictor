from django.contrib import admin
from .models import Login_user

# Register your models here.
# def deactivate(modeladmin, request, queryset):
#     queryset.update(show=False)
    
# @admin.action(description='Aktiv Et')
# def activate(modeladmin, request, queryset):
#     queryset.update(show=True)
admin.site.register(Login_user)

    # actions = (activate, deactivate)




from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin


class CustomUserAdmin(UserAdmin):
    list_display = ['username', 'first_name', 'group']


# Register your models here.
admin.site.register(User, CustomUserAdmin)
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account_api.models import User


class CustomUserAdmin(UserAdmin):
    list_display = ("username", "email", "is_superuser", "is_staff")


admin.site.register(User, CustomUserAdmin)
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'role', 'is_admin', 'is_teacher', 'is_student']
    fieldsets = UserAdmin.fieldsets + (
        ('Roles', {'fields': ('role', 'is_admin', 'is_teacher', 'is_student')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)

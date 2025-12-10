from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import User

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ("Extra", {"fields": ("is_student", "is_instructor", "student_id", "bio", "avatar")}),
    )

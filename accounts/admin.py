from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from  accounts.models import User

@admin.register(User)
class UserAdmin(UserAdmin):
    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'Extra Fields',
            {
                'fields': (
                    'role','gender',
                ),
            },
        ),
    )
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from  accounts.models import User



admin.site.site_header = "Welcome to AllkidsSevices"
admin.site.site_title = "welcome to AllkidsSevices' Dashboard"
admin.site.site_title = "Welcome to this portal"

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
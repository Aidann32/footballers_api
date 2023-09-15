from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User

UserAdmin.list_display += ('description',)

UserAdmin.fieldsets += (
    ('Description', {
        "fields": ('description',),
    }),
)


admin.site.register(User, UserAdmin)

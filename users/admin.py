from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin
from users.models import User, Relationship



admin.site.register(Relationship)

@admin.register(User)
class UserAdmin(AuthUserAdmin):
    add_fieldsets = (
        (None,{
            'classes':('wide',),
            'fields':('username', 'email', 'password', 'password2',),
        }),
    )

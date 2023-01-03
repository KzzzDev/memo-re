from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (_('一般'), {'fields': ('userid', 'password', 'username', 'email', 'icon', 'tag',)}),
        (_('日時'), {'fields': ('date_joined', 'last_login')}),
        (_('権限'), {'fields': (
            'is_superuser', 'is_staff', 'is_active', 'groups', 'user_permissions',), },),)
    add_fieldsets = ((None, {
        'classes': ('wide',),
        'fields': ('userid', 'password1', 'password2', 'username', 'email', 'icon', 'tag', 'is_superuser', 'is_staff',
                   'is_active'),
    },),)
    list_display = (
        'id', 'userid', 'username', 'email', 'icon', 'tag', 'date_joined', 'last_login',
        'is_superuser', 'is_staff', 'is_active'
    )
    list_display_links = ('id',)
    search_fields = (
        'userid', 'username', 'email', 'icon', 'tag', 'date_joined', 'last_login',
        'is_superuser', 'is_staff', 'is_active'
    )
    list_filter = (
        'userid', 'username', 'email', 'icon', 'tag', 'date_joined', 'last_login',
        'is_superuser', 'is_staff', 'is_active'
    )
    ordering = ("userid",)


admin.site.register(CustomUser, CustomUserAdmin)

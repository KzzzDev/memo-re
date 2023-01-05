from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (_('一般'), {'fields': ('password', 'username', 'email', 'icon', 'tag',)}),
        (_('日時'), {'fields': ('date_joined', 'last_login')}),
        (_('権限'), {'fields': (
            'is_superuser', 'is_staff', 'is_active', 'groups', 'user_permissions',), },),)
    add_fieldsets = ((None, {
        'classes': ('wide',),
        'fields': ('password1', 'password2', 'username', 'email', 'icon', 'tag', 'is_superuser', 'is_staff',
                   'is_active'),
    },),)
    list_display = (
        'id', 'username', 'email', 'icon', 'tag', 'date_joined', 'last_login',
        'is_superuser', 'is_staff', 'is_active'
    )
    list_display_links = ('id',)
    search_fields = (
        'username', 'email', 'icon', 'tag', 'date_joined', 'last_login',
        'is_superuser', 'is_staff', 'is_active'
    )
    list_filter = (
        'username', 'email', 'icon', 'tag', 'date_joined', 'last_login',
        'is_superuser', 'is_staff', 'is_active'
    )
    ordering = ("id",)


admin.site.register(CustomUser, CustomUserAdmin)

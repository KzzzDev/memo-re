from django.contrib import admin
from .models import CustomUser


class CustomerAdmin(admin.ModelAdmin):
    list_display = (
        'userid', 'username', 'email', 'icon', 'tag', 'date_joined', 'last_login',
        'is_superuser', 'is_staff', 'is_active')
    list_display_links = ('userid', 'username', 'email',)
    search_fields = (
        'userid', 'username', 'email', 'icon', 'tag', 'date_joined', 'last_login',
        'is_superuser', 'is_staff', 'is_active')
    list_filter = (
        'date_joined', 'last_login', 'is_superuser', 'is_staff', 'is_active')


admin.site.register(CustomUser, CustomerAdmin)

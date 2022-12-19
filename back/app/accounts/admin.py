from django.contrib import admin
from .models import CustomUser


class CustomerAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'email', 'username', 'date_joined', 'last_login',
        'is_superuser', 'is_staff', 'is_active')
    list_display_links = ('id', 'email')
    search_fields = (
        'id', 'email', 'username', 'date_joined', 'last_login',
        'is_superuser', 'is_staff', 'is_active')
    list_filter = (
        'date_joined', 'last_login', 'is_superuser', 'is_staff', 'is_active')


admin.site.register(CustomUser, CustomerAdmin)

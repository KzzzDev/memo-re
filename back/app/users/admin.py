from .models import CustomUser
from django.contrib import admin


class CustomerAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'username', 'email', 'icon', 'ranking', 'score', 'score_updated_at', 'date_joined', 'last_login',
        'last_name', 'first_name', 'is_superuser', 'is_staff', 'is_active')
    list_display_links = ('id', 'username')
    search_fields = (
        'id', 'username', 'email', 'icon', 'ranking', 'score', 'score_updated_at', 'date_joined', 'last_login',
        'last_name', 'first_name', 'is_superuser', 'is_staff', 'is_active')
    list_filter = (
        'score_updated_at', 'date_joined', 'last_login', 'is_superuser', 'is_staff', 'is_active')


admin.site.register(CustomUser, CustomerAdmin)

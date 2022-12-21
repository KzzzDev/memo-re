from django.contrib import admin
from .models import Friend


class FriendAdmin(admin.ModelAdmin):
    list_display = ('left', 'right', 'is_active')
    list_display_links = ('left', 'right',)
    search_fields = ('left__id', 'right__id', 'is_active')
    list_filter = ('left', 'right', 'is_active')


admin.site.register(Friend, FriendAdmin)

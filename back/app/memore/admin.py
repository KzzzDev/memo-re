from django.contrib import admin
from .models import Friend, Note, NoteShare


class FriendAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_from', 'user_to',
                    'apply', 'notified', 'register_at')
    list_display_links = ('id',)
    search_fields = ('user_from__id', 'user_to__id',
                     'apply', 'notified', 'register_at')
    list_filter = ('user_from', 'user_to', 'apply', 'notified', 'register_at')


class NoteAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'title', 'keyword', 'text_uri',
                    'image_uri', 'created_at', 'is_active', 'is_public')
    list_display_links = ('id',)
    search_fields = ('user__id', 'title', 'keyword', 'text_uri',
                     'image_uri', 'created_at', 'is_active', 'is_public')
    list_filter = ('user', 'title', 'keyword', 'text_uri',
                   'image_uri', 'created_at', 'is_active', 'is_public')


class NoteShareAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_from', 'user_to', 'note',
                    'notified', 'apply', 'register_at')
    list_display_links = ('id',)
    search_fields = ('user_from__id', 'user_to__id',
                     'note__id', 'notified', 'apply', 'register_at')
    list_filter = ('user_from', 'user_to', 'note',
                   'notified', 'apply', 'register_at')


admin.site.register(Friend, FriendAdmin)
admin.site.register(Note, NoteAdmin)
admin.site.register(NoteShare, NoteShareAdmin)

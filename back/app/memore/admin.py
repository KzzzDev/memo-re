from django.contrib import admin
from .models import Friend, Note, NoteShare


class FriendAdmin(admin.ModelAdmin):
    list_display = ('id', 'own_id', 'friend_id', 'approval', 'register_at')
    list_display_links = ('id',)
    search_fields = ('own_id__id', 'friend_id__id', 'approval', 'register_at')
    list_filter = ('own_id', 'friend_id', 'approval', 'register_at')


class NoteAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'title', 'keyword', 'text_uri', 'image_uri', 'created_at', 'is_active', 'is_public')
    list_display_links = ('id',)
    search_fields = ('user_id__id', 'title', 'keyword', 'text_uri', 'image_uri', 'created_at', 'is_active', 'is_public')
    list_filter = ('user_id', 'title', 'keyword', 'text_uri', 'image_uri', 'created_at', 'is_active', 'is_public')


class NoteShareAdmin(admin.ModelAdmin):
    list_display = ('id', 'own_id', 'friend_id', 'note_id', 'notified', 'apply')
    list_display_links = ('id',)
    search_fields = ('own_id__id', 'friend_id__id', 'note_id__id', 'notified', 'apply')
    list_filter = ('own_id', 'friend_id', 'note_id', 'notified', 'apply')


admin.site.register(Friend, FriendAdmin)
admin.site.register(Note, NoteAdmin)
admin.site.register(NoteShare, NoteShareAdmin)

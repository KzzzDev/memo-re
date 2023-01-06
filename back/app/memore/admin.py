from django.contrib import admin
from .models import Friend, Note, NoteShare


class FriendAdmin(admin.ModelAdmin):
    list_display = ('id', 'own', 'friend', 'approval', 'register_at')
    list_display_links = ('id',)
    search_fields = ('own__id', 'friend__id', 'approval', 'register_at')
    list_filter = ('own', 'friend', 'approval', 'register_at')


class NoteAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'title', 'keyword', 'text_uri',
                    'image_uri', 'created_at', 'is_active', 'is_public')
    list_display_links = ('id',)
    search_fields = ('user__id', 'title', 'keyword', 'text_uri',
                     'image_uri', 'created_at', 'is_active', 'is_public')
    list_filter = ('user', 'title', 'keyword', 'text_uri',
                   'image_uri', 'created_at', 'is_active', 'is_public')


class NoteShareAdmin(admin.ModelAdmin):
    list_display = ('id', 'own', 'friend', 'note', 'notified', 'apply')
    list_display_links = ('id',)
    search_fields = ('own__id', 'friend__id',
                     'note__id', 'notified', 'apply')
    list_filter = ('own', 'friend', 'note', 'notified', 'apply')


admin.site.register(Friend, FriendAdmin)
admin.site.register(Note, NoteAdmin)
admin.site.register(NoteShare, NoteShareAdmin)

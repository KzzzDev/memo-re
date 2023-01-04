from django.contrib import admin
from .models import Friend, Note, NoteShare


class FriendAdmin(admin.ModelAdmin):
    list_display = ('userid_id', 'friend', 'approval',
                    'register_at', 'is_deleted')
    list_display_links = ('userid_id', 'friend',)
    search_fields = ('userid_id__userid', 'friend__userid',
                     'approval', 'register_at', 'is_deleted')
    list_filter = ('userid_id', 'friend', 'approval',
                   'register_at', 'is_deleted')


class NoteAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'creator', 'keyword',
                    'text', 'image', 'category', 'is_active')
    list_display_links = ('id',)
    search_fields = ('title', 'creator__userid', 'keyword',
                     'text', 'image', 'category', 'is_active')
    list_filter = ('title', 'creator', 'keyword', 'text',
                   'image', 'category', 'is_active')


class NoteShareAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'note_id', 'is_active')
    list_display_links = ('user_id', 'note_id',)
    search_fields = ('user_id__userid', 'note_id__id', 'is_active')
    list_filter = ('user_id', 'note_id', 'is_active')


admin.site.register(Friend, FriendAdmin)
admin.site.register(Note, NoteAdmin)
admin.site.register(NoteShare, NoteShareAdmin)

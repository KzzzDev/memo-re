from django.contrib import admin
from .models import Friend, Note, NoteShare


class FriendAdmin(admin.ModelAdmin):
    list_display = ('left', 'right', 'is_active')
    list_display_links = ('left', 'right',)
    search_fields = ('left__userid', 'right__userid', 'is_active')
    list_filter = ('left', 'right', 'is_active')


class NoteAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'creator', 'keyword', 'text', 'image', 'category', 'is_active')
    list_display_links = 'id'
    search_fields = ('id', 'title', 'creator__userid', 'keyword', 'text', 'image', 'category', 'is_active')
    list_filter = ('id', 'title', 'creator', 'keyword', 'text', 'image', 'category', 'is_active')


class NoteShareAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'note_id', 'is_active')
    list_display_links = ('user_id', 'note_id',)
    search_fields = ('user_id__userid', 'note_id__id', 'is_active')
    list_filter = ('user_id', 'note_id', 'is_active')


admin.site.register(Friend, FriendAdmin)
admin.site.register(Note, NoteAdmin)
admin.site.register(NoteShare, NoteShareAdmin)

from rest_framework import viewsets
from rest_framework import generics
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from memore.models import Friend
from memore.models import Note
from .serializers import FriendSerializer
from .serializers import NoteSerializer


class MultipleFieldLookupMixin:
    """
    Apply this mixin to any view or viewset to get multiple field filtering
    based on a `lookup_fields` attribute, instead of the default single field filtering.
    """

    def get_object(self):
        queryset = self.get_queryset()             # Get the base queryset
        queryset = self.filter_queryset(queryset)  # Apply any filter backends
        filter = {}
        for field in self.lookup_fields:
            if self.kwargs.get(field):  # Ignore empty fields.
                filter[field] = self.kwargs[field]
        obj = get_object_or_404(queryset, **filter)  # Lookup the object
        self.check_object_permissions(self.request, obj)
        return obj


class FriendRetrieveAPIView(generics.RetrieveAPIView):
    """ユーザのフレンド取得（詳細）APIクラス"""

    queryset = Friend.objects.all()
    serializer_class = FriendSerializer


class FriendDestroyAPIView(generics.DestroyAPIView):
    """ユーザのフレンド削除APIクラス"""

    queryset = Friend.objects.all()
    serializer_class = FriendSerializer


class FriendCreateAPIView(generics.CreateAPIView):
    """ユーザのフレンド登録APIクラス"""

    queryset = Friend.objects.all()
    serializer_class = FriendSerializer


class FriendUpdateAPIView(generics.UpdateAPIView):
    """ユーザのフレンド申請承認APIクラス"""

    queryset = Friend.objects.all()
    serializer_class = FriendSerializer


class FriendRequestDestroyAPIView(generics.DestroyAPIView):
    """ユーザのフレンド申請承認APIクラス"""

    queryset = Friend.objects.all()
    serializer_class = FriendSerializer


class NoteListAPIView(generics.ListAPIView):
    """ブレイン取得APIクラス"""

    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    lookup_field = 'userid'


class NoteCreateAPIView(generics.CreateAPIView):
    """ノート作成APIクラス"""

    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    lookup_field = 'userid'


class NoteRetrieveAPIView(MultipleFieldLookupMixin, generics.RetrieveAPIView):
    """ノート取得APIクラス"""

    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    lookup_fields = ['userid', 'noteid']


class NoteUpdateAPIView(MultipleFieldLookupMixin, generics.UpdateAPIView):
    """ノート更新APIクラス"""

    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    lookup_fields = ['userid', 'noteid']


class NoteDestroyAPIView(MultipleFieldLookupMixin, generics.DestroyAPIView):
    """ノート削除APIクラス"""

    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    lookup_fields = ['userid', 'noteid']


class NoteShareCreateAPIView(MultipleFieldLookupMixin, generics.CreateAPIView):
    """ノート共有設定APIクラス"""

    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    lookup_fields = ['userid', 'noteid']


class NoteShareDestroyAPIView(MultipleFieldLookupMixin, generics.DestroyAPIView):
    """ノート共有削除APIクラス"""

    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    lookup_fields = ['userid', 'noteid']

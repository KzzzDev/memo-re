from rest_framework import generics
from rest_framework import mixins
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


class FriendRetrieveAPIView(generics.RetrieveDestroyAPIView):
    """ユーザのフレンドリスト取得・フレンド削除APIクラス"""

    queryset = Friend.objects.all()
    serializer_class = FriendSerializer


class FriendRequestAPIView(mixins.CreateModelMixin, mixins.UpdateModelMixin,  mixins.DestroyModelMixin, generics.GenericAPIView):
    """ユーザのフレンド申請・申請承認・申請取消APIクラス"""

    serializer_class = FriendSerializer
    queryset = Friend.objects.all()

    def post(self, request, *args, **kwargs):
        """フレンド申請"""
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        """フレンド申請承認"""
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        """フレンド申請取消"""
        return self.destroy(request, *args, **kwargs)


class NoteListCreateAPIView(generics.ListCreateAPIView):
    """ブレイン取得・ノート作成APIクラス"""

    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    lookup_field = 'userid'


class NoteRetrieveUpdateDestroyAPIView(MultipleFieldLookupMixin, generics.RetrieveUpdateDestroyAPIView):
    """ノート取得・更新・削除APIクラス"""

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


class NoteShareCreateDestroyAPIView(MultipleFieldLookupMixin, mixins.CreateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    """ノート共有設定・共有削除APIクラス"""

    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    lookup_fields = ['userid', 'noteid']

    def post(self, request, *args, **kwargs):
        """ノート共有設定"""
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        """ノート共有削除"""
        return self.destroy(request, *args, **kwargs)

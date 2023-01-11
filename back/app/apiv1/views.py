from rest_framework import generics
from rest_framework import mixins
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from memore.models import Friend
from memore.models import Note
from .serializers import FriendSerializer
from .serializers import NoteSerializer
from .serializers import NoteShareSerializer


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


class NoteListCreateAPIView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    """ブレイン取得・ノート作成APIクラス"""

    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    # serializer_class = NoteListCreateSerializer
    lookup_field = 'user'

    def get(self, request, *args, **kwargs):
        """ノート一覧を取得"""
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """ノート作成"""
        return self.create(request, *args, **kwargs)


class NoteRetrieveUpdateDestroyAPIView(MultipleFieldLookupMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    """ノート取得・更新・削除APIクラス"""

    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    lookup_fields = ['user', 'id']

    def get(self, request, *args, **kwargs):
        """ノートを取得"""
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        """ノートを更新"""
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        """ノートを削除"""
        return self.destroy(request, *args, **kwargs)


class NoteShareCreateDestroyAPIView(MultipleFieldLookupMixin, mixins.CreateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    """ノート共有設定・共有削除APIクラス"""

    queryset = Note.objects.all()
    serializer_class = NoteShareSerializer
    lookup_fields = ['user_from', 'note']

    def post(self, request, *args, **kwargs):
        """ノート共有設定"""
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        """ノート共有削除"""
        return self.destroy(request, *args, **kwargs)

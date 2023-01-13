from rest_framework import generics
from rest_framework import mixins
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from memore.models import Friend
from memore.models import Note
from memore.models import NoteShare
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


class FriendListRequestAPIView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    """ユーザのフレンドリスト取得・フレンド申請APIクラス"""

    queryset = Friend.objects.all()
    serializer_class = FriendSerializer

    def get_queryset(self):
        """
        ログインユーザのユーザIDでフィルタリング
        """
        auth_user_id = self.request.user.id
        return Friend.objects.filter(user_from=auth_user_id)

    def get(self, request, *args, **kwargs):
        """フレンドリストを取得"""
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """フレンド申請"""
        auth_user_id = self.request.user.id
        request.data['user_from'] = auth_user_id
        return self.create(request, *args, **kwargs)


class FriendDeleteAPIView(mixins.DestroyModelMixin, generics.GenericAPIView):
    """ユーザのフレンド削除APIクラス"""

    serializer_class = FriendSerializer
    lookup_field = 'user_to'
    queryset = Friend.objects.all()

    def get_queryset(self):
        """
        ログインユーザのユーザIDでフィルタリング
        """
        user = self.request.user.id
        delete_user_id = self.kwargs['user_to']

        return Friend.objects.filter(user_from=user, user_to=delete_user_id)

    def delete(self, request, *args, **kwargs):
        """フレンドを削除"""
        return self.destroy(request, *args, **kwargs)


class FriendRequestApplyAPIView(mixins.UpdateModelMixin, generics.GenericAPIView):
    """ユーザのフレンド申請承認APIクラス"""

    serializer_class = FriendSerializer
    queryset = Friend.objects.all()
    lookup_field = 'user_from'

    def get_queryset(self):
        """
        ログインユーザのユーザIDとURLパラメータのuser_formでフィルタリング
        """
        auth_user_id = self.request.user.id
        user_from_id = self.kwargs['user_from']
        return Friend.objects.filter(user_from=user_from_id, user_to=auth_user_id)

    def patch(self, request, *args, **kwargs):
        """フレンド申請承認"""
        return self.partial_update(request, *args, **kwargs)


class FriendRequestDeleteAPIView(mixins.CreateModelMixin, mixins.UpdateModelMixin,  mixins.DestroyModelMixin, generics.GenericAPIView):
    """ユーザのフレンド申請取消APIクラス"""

    serializer_class = FriendSerializer
    queryset = Friend.objects.all()
    lookup_field = 'user_to'

    def get_queryset(self):
        """
        ログインユーザのユーザIDとURLパラメータのuser_toでフィルタリング
        """
        auth_user_id = self.request.user.id
        user_to_id = self.kwargs['user_to']
        return Friend.objects.filter(user_from=auth_user_id, user_to=user_to_id)

    def delete(self, request, *args, **kwargs):
        """フレンド申請取消"""
        return self.destroy(request, *args, **kwargs)


class NoteListCreateAPIView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    """ノート一覧の取得・ノート作成APIクラス"""

    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    def get_queryset(self):
        """
        ログインユーザのユーザIDでフィルタリング
        """
        auth_user_id = self.request.user.id
        return Note.objects.filter(user=auth_user_id)

    def get(self, request, *args, **kwargs):
        """ノート一覧を取得"""
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """ノート作成"""
        auth_user_id = self.request.user.id
        request.data['user'] = auth_user_id
        return self.create(request, *args, **kwargs)


class NoteRetrieveUpdateDestroyAPIView(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    """ノート取得・更新・削除APIクラス"""

    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    lookup_field = 'id'

    def get_queryset(self):
        """
        ログインユーザのユーザIDでフィルタリング
        """
        auth_user_id = self.request.user.id
        note_id = self.kwargs['id']
        return Note.objects.filter(user=auth_user_id, id=note_id)

    def get(self, request, *args, **kwargs):
        """ノートを取得"""
        return self.retrieve(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        """ノートを更新"""
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        """ノートを削除"""
        return self.destroy(request, *args, **kwargs)


class NoteShareCreateDestroyAPIView(mixins.CreateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    """ノート共有設定・共有削除APIクラス"""

    queryset = Note.objects.all()
    serializer_class = NoteShareSerializer
    lookup_field = 'note'

    def get_queryset(self):
        """
        ログインユーザのユーザIDとURLパラメータのuser_formでフィルタリング
        """
        note_id = self.kwargs['note']
        auth_user_id = self.request.user.id
        return NoteShare.objects.filter(user_from=auth_user_id, note=note_id)

    def post(self, request, *args, **kwargs):
        """ノート共有設定"""
        note_id = self.kwargs['note']
        auth_user_id = self.request.user.id
        request.data['note'] = note_id
        request.data['user_from'] = auth_user_id
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        """ノート共有削除"""
        return self.destroy(request, *args, **kwargs)

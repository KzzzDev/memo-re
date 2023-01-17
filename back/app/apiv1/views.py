from rest_framework import generics
from rest_framework import mixins
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from memore.models import Friend
from memore.models import Note
from memore.models import NoteShare
from .serializers import FriendSerializer
from .serializers import FriendListSerializer
from .serializers import NoteSerializer
from .serializers import NoteEditSerializer
from .serializers import NoteShareSerializer
from accounts.serializers import CustomUserSerializer
from accounts.models import CustomUser
from django.db.models import Q
from rest_framework.response import Response
from rest_framework import status


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


class SearchUserAPIView(mixins.ListModelMixin, generics.GenericAPIView):
    """ユーザ検索用APIクラス"""

    serializer_class = CustomUserSerializer
    # queryset = CustomUser.objects.all()
    # filter_backends = [filters.DjangoFilterBackend]

    def get_queryset(self):
        """
        検索項目で渡されたクエリパラメータでフィルタリング
        """
        queryset = CustomUser.objects.all()
        get_query = self.request.query_params.getlist('get', None)
        if get_query is not None:
            queryset_result = CustomUser.objects.none()
            for n in get_query:
                if n:
                    queryset_result = queryset_result.union(queryset.filter(
                        Q(id__icontains=n) | Q(username__icontains=n) | Q(
                            tag__icontains=n)
                    ))
        return queryset_result

    def get(self, request, *args, **kwargs):
        """ユーザ検索の結果を取得"""
        return self.list(request, *args, **kwargs)


class FriendListAPIView(mixins.ListModelMixin, generics.GenericAPIView):
    """フレンドリスト取得APIクラス"""

    queryset = Friend.objects.all()
    serializer_class = FriendListSerializer

    def get(self, request, *args, **kwargs):
        """フレンドリスト（承認済み）を取得"""

        validate_json = []

        auth_user_id = self.request.user.id
        queryset = Friend.objects.filter(
            Q(user_from=auth_user_id) | Q(user_to=auth_user_id), apply=True)
        serializer = FriendListSerializer(queryset, context={"request":
                                                             request}, many=True)
        for i in range(len(serializer.data)):
            if auth_user_id != serializer.data[i]['user_from']['id']:
                validate_json.append(serializer.data[i]['user_from'])
            else:
                validate_json.append(serializer.data[i]['user_to'])
        return Response(validate_json, status.HTTP_200_OK)


class FriendRequestAPIView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    """フレンド申請APIクラス"""

    queryset = Friend.objects.all()
    serializer_class = FriendSerializer

    def get_queryset(self):
        """
        ログインユーザのユーザIDでフィルタリング
        """
        auth_user_id = self.request.user.id
        return Friend.objects.filter(Q(user_from=auth_user_id) | Q(user_to=auth_user_id), apply=True)

    def post(self, request, *args, **kwargs):
        """フレンド申請"""
        auth_user_id = self.request.user.id
        request.data['user_from'] = auth_user_id
        return self.create(request, *args, **kwargs)


class FriendRequestListAPIView(mixins.ListModelMixin, generics.GenericAPIView):
    """ログインユーザが申請中のユーザ一覧を取得するAPIクラス"""

    queryset = Friend.objects.all()
    serializer_class = FriendSerializer

    def get_queryset(self):
        """
        ログインユーザのユーザIDでフィルタリング
        """
        auth_user_id = self.request.user.id
        return Friend.objects.filter(user_from=auth_user_id, apply=False, rejection=False)

    def get(self, request, *args, **kwargs):
        """ログインユーザが申請中のユーザ一覧を取得"""
        return self.list(request, *args, **kwargs)


class FriendRequestApplyListAPIView(mixins.ListModelMixin, generics.GenericAPIView):
    """ログインユーザの承認待ちのユーザ一覧を取得APIクラス"""

    queryset = Friend.objects.all()
    serializer_class = FriendSerializer

    def get_queryset(self):
        """
        ログインユーザのユーザIDでフィルタリング
        """
        auth_user_id = self.request.user.id
        return Friend.objects.filter(user_to=auth_user_id, apply=False, rejection=False)

    def get(self, request, *args, **kwargs):
        """ログインユーザの承認待ちのユーザ一覧を取得"""
        return self.list(request, *args, **kwargs)


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


class FriendRequestAnswerAPIView(mixins.UpdateModelMixin, generics.GenericAPIView):
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


class NoteListFriendAPIView(mixins.ListModelMixin, generics.GenericAPIView):
    """他ユーザのノート一覧の取得APIクラス"""

    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    lookup_field = 'id'

    def get_queryset(self):
        """
        URLパラメータで渡されたユーザIDでフィルタリング
        """
        user_id = self.kwargs['id']
        queryset = Note.objects.filter(
            user=user_id, is_public=True)
        return queryset

    def get(self, request, *args, **kwargs):
        """他ユーザのノート一覧を取得"""
        return self.list(request, *args, **kwargs)


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
        if 'author' not in request.data:
            request.data['author'] = auth_user_id
        return self.create(request, *args, **kwargs)


class NoteRetrieveUpdateDestroyAPIView(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    """ノート取得・更新・削除APIクラス"""

    queryset = Note.objects.all()
    serializer_class = NoteEditSerializer
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


class NoteShareListCreateAPIView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    """承認済みのノート共有一覧取得・設定するAPIクラス"""

    queryset = NoteShare.objects.all()
    serializer_class = NoteShareSerializer

    def get_queryset(self):
        """
        ログインユーザのユーザIDでフィルタリング
        """
        auth_user_id = self.request.user.id
        return NoteShare.objects.filter(Q(user_from=auth_user_id) | Q(user_to=auth_user_id), apply=True, rejection=False)

    def get(self, request, *args, **kwargs):
        """承認済みのノート共有一覧を取得"""
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """ノート共有設定"""
        auth_user_id = self.request.user.id
        request.data['user_from'] = auth_user_id
        return self.create(request, *args, **kwargs)


class NoteShareRequestListAPIView(mixins.ListModelMixin, generics.GenericAPIView):
    """申請中のノート共有一覧を取得するAPIクラス"""

    queryset = NoteShare.objects.all()
    serializer_class = NoteShareSerializer

    def get_queryset(self):
        """
        ログインユーザのユーザIDでフィルタリング
        """
        auth_user_id = self.request.user.id
        return NoteShare.objects.filter(user_from=auth_user_id, apply=False, rejection=False)

    def get(self, request, *args, **kwargs):
        """申請中のノート共有一覧を取得"""
        return self.list(request, *args, **kwargs)


class NoteShareRequestAnswerListAPIView(mixins.ListModelMixin, generics.GenericAPIView):
    """フレンドからのノート共有申請の一覧を取得するAPIクラス"""

    queryset = NoteShare.objects.all()
    serializer_class = NoteShareSerializer

    def get_queryset(self):
        """
        ログインユーザのユーザIDでフィルタリング
        """
        auth_user_id = self.request.user.id
        return NoteShare.objects.filter(user_to=auth_user_id, apply=False, rejection=False)

    def get(self, request, *args, **kwargs):
        """フレンドからのノート共有申請の一覧を取得"""
        return self.list(request, *args, **kwargs)


class NoteShareUpdateDestroyAPIView(mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    """ノート共有削除APIクラス"""

    queryset = NoteShare.objects.all()
    serializer_class = NoteShareSerializer
    lookup_field = 'note'

    def get_queryset(self):
        """
        ログインユーザのユーザIDとURLパラメータのuser_formでフィルタリング
        """
        note_id = self.kwargs['note']
        user_to_id = self.kwargs['user_to']
        auth_user_id = self.request.user.id
        return NoteShare.objects.filter(user_from=auth_user_id, note=note_id, user_to=user_to_id)

    def patch(self, request, *args, **kwargs):
        """ノート共有の更新"""
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        """ノート共有削除"""
        return self.destroy(request, *args, **kwargs)

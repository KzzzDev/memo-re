from rest_framework import viewsets
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from memore.models import Friend
from .serializers import FriendSerializer


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

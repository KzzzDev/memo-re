from rest_framework import serializers
from memore.models import Friend
from memore.models import Note
from memore.models import NoteShare
from accounts.serializers import CustomUserSerializer
from drf_writable_nested import WritableNestedModelSerializer


class FriendListSerializer(WritableNestedModelSerializer):
    """フレンドリスト用のシリアライザ"""

    user_from = CustomUserSerializer(many=False, read_only=True)
    user_to = CustomUserSerializer(many=False, read_only=True)

    class Meta:
        model = Friend
        fields = ('user_from', 'user_to', 'apply')
        extra_kwargs = {
            'apply': {
                'write_only': True
            }, 'user_from': {
                'write_only': True
            }, 'user_to': {
                'write_only': True
            }
        }


class FriendSerializer(serializers.ModelSerializer):
    """フレンドモデル用のシリアライザ"""

    class Meta:
        model = Friend
        fields = '__all__'
        read_only_fields = ('register_at',)


class FriendRequestSerializer(serializers.ModelSerializer):
    """フレンド申請一覧用のシリアライザ"""

    user_from = CustomUserSerializer(many=False, read_only=True)
    user_to = CustomUserSerializer(many=False, read_only=True)

    class Meta:
        model = Friend
        fields = ('user_from', 'user_to', 'notified',
                  'apply', 'rejection', 'register_at',)
        read_only_fields = ('user_from', 'user_to', 'register_at',)


class NoteSerializer(serializers.ModelSerializer):
    """ノートモデル用のシリアライザ"""

    class Meta:
        model = Note
        fields = ('id', 'author', 'user', 'title', 'keyword', 'text_uri',
                  'image_uri', 'created_at', 'updated_at', 'is_public')
        read_only_fields = ('id', 'created_at', 'updated_at',)


class NoteAllListSerializer(serializers.ModelSerializer):
    """全てのユーザのノート一覧用のシリアライザ"""

    class Meta:
        model = Note
        fields = ('id', 'author', 'user', 'title', 'keyword', 'text_uri',
                  'image_uri', 'created_at', 'updated_at', 'is_public')
        read_only_fields = ('id', 'created_at', 'updated_at',)
        extra_kwargs = {
            'is_public': {
                'write_only': True
            }
        }


class NoteListSerializer(serializers.ModelSerializer):
    """ポップアップのノート情報取得用のシリアライザ"""

    class Meta:
        model = Note
        fields = ('id', 'user_id', 'image_uri',)
        read_only_fields = ('id', 'user_id', 'image_uri',)


class NoteEditSerializer(serializers.ModelSerializer):
    """ノート編集・削除用のシリアライザ"""

    class Meta:
        model = Note
        fields = ('id', 'author', 'user', 'title', 'keyword', 'text_uri',
                  'image_uri', 'created_at', 'updated_at', 'is_public')
        read_only_fields = ('id', 'author', 'user',
                            'created_at', 'updated_at',)


class NoteShareSerializer(serializers.ModelSerializer):
    """ノート共有モデル用のシリアライザ"""

    class Meta:
        model = NoteShare
        fields = '__all__'
        read_only_fields = ('id', 'register_at',)


class NoteShareListSerializer(serializers.ModelSerializer):
    """ノート共有申請一覧取得用のシリアライザ"""

    user_from = CustomUserSerializer(many=False, read_only=True)
    user_to = CustomUserSerializer(many=False, read_only=True)
    note = NoteListSerializer(many=False, read_only=True)

    class Meta:
        model = NoteShare
        fields = ('user_from', 'user_to', 'note', 'get', 'notified',
                  'apply', 'rejection', 'register_at',)
        read_only_fields = ('note', 'user_from', 'user_to', 'register_at',)

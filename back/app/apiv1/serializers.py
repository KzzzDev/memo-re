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


class NoteSerializer(serializers.ModelSerializer):
    """ノートモデル用のシリアライザ"""

    class Meta:
        model = Note
        fields = ('id', 'author', 'user', 'title', 'keyword', 'text_uri',
                  'image_uri', 'created_at', 'updated_at', 'is_public')
        read_only_fields = ('id', 'created_at', 'updated_at',)


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

from rest_framework import serializers
from memore.models import Friend
from memore.models import Note


class FriendSerializer(serializers.ModelSerializer):
    """フレンドモデル用のシリアライザ"""

    class Meta:
        model = Friend
        fields = ['left', 'right']


class NoteSerializer(serializers.ModelSerializer):
    """ノートモデル用のシリアライザ"""

    class Meta:
        model = Note
        fields = ['id', 'title', 'keyword', 'text',
                  'image', 'category', 'is_active', 'creator_id']

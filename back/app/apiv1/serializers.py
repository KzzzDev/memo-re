from rest_framework import serializers
from memore.models import Friend
from memore.models import Note


class FriendSerializer(serializers.ModelSerializer):
    """フレンドモデル用のシリアライザ"""

    class Meta:
        model = Friend
        fields = '__all__'


class NoteSerializer(serializers.ModelSerializer):
    """ノートモデル用のシリアライザ"""

    class Meta:
        model = Note
        fields = '__all__'

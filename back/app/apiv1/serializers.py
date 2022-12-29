from rest_framework import serializers
from memore.models import Friend


class FriendSerializer(serializers.ModelSerializer):
    """フレンドモデル用のシリアライザ"""

    class Meta:
        model = Friend
        fields = ['left', 'right']

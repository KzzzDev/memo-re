from djoser import serializers
from accounts.models import CustomUser


# djoserのシリアライザーを変更する場合
class CustomUserSerializer(serializers.UserSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'icon_uri', 'email', 'password', 'tag']
        read_only_fields = (id,)

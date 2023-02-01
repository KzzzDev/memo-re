from djoser import serializers
from accounts.models import CustomUser
from django.contrib.auth.hashers import make_password


# djoserのシリアライザーを変更する場合
class CustomUserSerializer(serializers.UserSerializer):

    def validate_password(self, value: str) -> str:
        return make_password(value)

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'icon_uri', 'email', 'password', 'tag']
        read_only_fields = ('id',)
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }

    def get_icon_uri(self, obj):
        request = self.context.get('request')
        photo_url = obj.fingerprint.url
        return request.build_absolute_uri(photo_url)


class CustomUserSearchSerializer(serializers.UserSerializer):

    def validate_password(self, value: str) -> str:
        return make_password(value)

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'icon_uri', 'tag']
        read_only_fields = ('id', 'username', 'icon_uri', 'tag')

    def get_icon_uri(self, obj):
        request = self.context.get('request')
        photo_url = obj.fingerprint.url
        return request.build_absolute_uri(photo_url)

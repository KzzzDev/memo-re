from rest_framework import serializers

from shop.models import Book


class UsersSerializer(serializers.ModelSerializer):
    """本モデル用のシリアライザ"""

    class Meta:
        model = Book
        fields = ['email', 'password']

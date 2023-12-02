from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from users_app.models import User, TelegramUser


class UserSerialzier(serializers.ModelSerializer):

    @staticmethod
    def validate_password(password: str) -> str:
        return make_password(password)

    class Meta:
        model = User
        fields = '__all__'




class UserDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        exclude = 'updated_at'



class TelegramUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = TelegramUser
        fields = '__all__'



class TelegramUserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = TelegramUser
        exclude = ['updated_at']
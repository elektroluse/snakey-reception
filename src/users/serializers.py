from rest_framework.serializers import ModelSerializer, Serializer
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from django.contrib.auth import authenticate
from .models import CustomUser
class CustomUserSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ("id","email","username","created_at")
        extra_kwargs = {
            "created_at":{"read_only": True}
        }
class RegisterUserSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["username","email", "password"]
        extra_kwargs = {
            "password":{"write_only": True}
        }
    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user

class LoginUserSerializer(Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise ValidationError("Invalid Login")


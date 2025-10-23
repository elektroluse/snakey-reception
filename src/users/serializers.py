from rest_framework.serializers import ModelSerializer
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
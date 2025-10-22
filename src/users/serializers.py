from rest_framework.serializers import ModelSerializer
from .models import CustomUser
class CustomUserSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ("id","email","username","created_at")
        extra_kwargs = {
            "created_at":{"read_only": True}
        }

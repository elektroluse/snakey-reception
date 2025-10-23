from django.db import transaction
from .serializers import RegisterUserSerializer
from rest_framework.exceptions import NotFound, ValidationError
class UserService:
    @staticmethod
    @transaction.atomic
    def create(user_data):
        serializer = RegisterUserSerializer(data = user_data)
        if serializer.is_valid(raise_exception = True):
            serializer.save()
            return serializer.data
        else :
            raise ValidationError("User data is not valid")
        """
            implement some event to send a registration confirmation
            to a future email service...
        """

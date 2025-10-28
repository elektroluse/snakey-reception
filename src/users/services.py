from django.db import transaction
from .serializers import RegisterUserSerializer, LoginUserSerializer, CustomUserSerializer
from rest_framework.exceptions import NotFound, ValidationError
from rest_framework_simplejwt.tokens import RefreshToken
from .dtos.login_dto import LoginServiceResponse
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

    @staticmethod
    def login(user_data):
        serializer = LoginUserSerializer(data = user_data)
        if serializer.is_valid():
            user = serializer.validated_data
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            return LoginServiceResponse(
                user = CustomUserSerializer(user).data,
                refresh = refresh,
                access_token = access_token,
                errors = ""
            )
        else :
            return LoginServiceResponse(
                user = None,
                refresh = None,
                access_token = None,
                errors = serializer.errors
            )
 
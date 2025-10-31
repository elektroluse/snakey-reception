from django.shortcuts import render
from rest_framework.generics import RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework_simplejwt.exceptions import InvalidToken
from .serializers import CustomUserSerializer, RegisterUserSerializer
from .services import UserService, RegistrationProducer
class UserInfoView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = CustomUserSerializer
    def get_object(self):
        return self.request.user

class UserRegistrationView(CreateAPIView):
    serializer_class = RegisterUserSerializer
    kafka_producer = RegistrationProducer()
    def post(self,request):
        response_data = UserService.create(request.data)
        self.kafka_producer.publish(response_data)
        return Response(
            response_data,
            status = status.HTTP_201_CREATED
        )

class LoginView(APIView):
    permission_classes = ()
    authentication_classes = ()
    def post(self, request):
        service_response = UserService.login(request.data)
        
        if not service_response.errors:
            response = Response(
                data = service_response.user,
                status = status.HTTP_200_OK
            )    
            response.set_cookie(
                key = "access_token",
                value = service_response.access_token,
                httponly = True,
                secure = True,
                samesite = "None"
            )
            response.set_cookie(
                key = "refresh",
                value = service_response.refresh,
                httponly = True,
                secure = True,
                samesite = "None"
            )
            return response
        return Response(
            service_response.errors,
            status = status.HTTP_400_BAD_REQUEST
        )

class LogoutView(APIView):

    def post(self, request):
        
        refresh_token = request.COOKIES.get("refresh")
        if refresh_token:
            try:
                refresh = RefreshToken(refresh_token)
                refresh.blacklist()
            except Exception as error:
                return Response(
                    {
                        "error": "Error invalidating tokens:" + str(error)},
                        status = status.HTTP_400_BAD_REQUEST
                        )
        response = Response({"message" : "Logout success"},
        status = status.HTTP_200_OK)
        response.delete_cookie(key = "access_token")
        response.delete_cookie(key = "refresh")
        return response

class CookieTokenRefreshView(TokenRefreshView):
    def post(self,request):
        refresh_token = request.COOKIES.get("refresh")
        if not refresh_token:
            return Response({"error":"no refresh token"},status=status.HTTP_401_UNAUTHORIZED)
        try:
            refresh = RefreshToken(refresh_token)
            access_token = str(refresh.access_token)
            response = Response(
                {"message": "Access token refreshed"},
                 status=status.HTTP_200_OK)
            response.set_cookie(
                key = "access_token",
                value = access_token,
                httponly = True,
                secure = True,
                samesite = "None"
            )
            response.set_cookie(
                key = "refresh",
                value = refresh,
                httponly = True,
                secure = True,
                samesite = "None"
            )
            return response
        except InvalidToken:
            return Response({"error":"Invalid token"},status = status.HTTP_401_UNAUTHORIZED)


from django.shortcuts import render
from rest_framework.generics import RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .serializers import CustomUserSerializer, RegisterUserSerializer
from .services import UserService
class UserInfoView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = CustomUserSerializer
    def get_object(self):
        return self.request.user

class UserRegistrationView(CreateAPIView):
    serializer_class = RegisterUserSerializer
    def post(self,request):
        response_data = UserService.create(request.data)
        return Response(
            response_data,
            status = status.HTTP_201_CREATED)

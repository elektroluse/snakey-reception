from django.shortcuts import render
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from .serializers import CustomUserSerializer
class UserInfoView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = CustomUserSerializer
    def get_object(self):
        return self.request.user

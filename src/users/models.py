from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .managers import CustomUserManager
class CustomUser(AbstractBaseUser):
    USERNAME_FIELD = 'username'
    username = models.CharField(unique=True, max_length=32)
    email = models.EmailField(unique=True)
    password = models.CharField(null=False)
    created_at = models.TimeField(auto_now_add=True)
    REQUIRED_FIELDS = ["email"]
    objects = CustomUserManager()

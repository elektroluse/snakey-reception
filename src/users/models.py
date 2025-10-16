from django.db import models
from django.contrib.auth.models import AbstractBaseUser

class CustomUser(AbstractBaseUser):
    USERNAME_FIELD = 'username'
    username = models.CharField(unique=True, max_length=32)
    email = models.EmailField(unique=True)
    password = models.CharField(null=False)
    REQUIRED_FIELDS = []

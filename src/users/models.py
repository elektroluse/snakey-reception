from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import CustomUserManager
class CustomUser(AbstractBaseUser, PermissionsMixin):
    USERNAME_FIELD = 'username'
    username = models.CharField(unique=True, max_length=32)
    email = models.EmailField(unique=True)
    password = models.CharField(null=False)
    created_at = models.TimeField(auto_now_add=True)
    is_staff = models.BooleanField(default = False)
    REQUIRED_FIELDS = ["email"]
    objects = CustomUserManager()
    
    class Meta:
        db_table = "user"
        verbose_name = "user"
        verbose_name_plural = "users"

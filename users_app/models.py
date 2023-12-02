from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models


class ROLE_CHOICE(models.TextChoices):
    ADMIN = ('ADMIN', )
    OPERATOR = ('OPERATOR', )
    DELIVER = ('DELIVER', )




class User(models.Model):

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    role = models.CharField(max_length=15, choices=ROLE_CHOICE.choices)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class TelegramUser(models.Model):
    chat_id = models.CharField(max_length=50)
    full_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    is_blocked = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name




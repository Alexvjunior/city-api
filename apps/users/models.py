from django.contrib.auth.models import AbstractUser
from django.db import models


class UserModel(AbstractUser):
    username = models.EmailField(unique=True)

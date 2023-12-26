from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=30, default='')
    last_name = models.CharField(max_length=30, default='')

    def __str__(self):
        return self.username

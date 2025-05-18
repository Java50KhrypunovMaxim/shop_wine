from django.contrib.auth.models import AbstractUser

from shop import models


class User(AbstractUser):
    address = models.CharField(max_length=255, null=True, blank=True)

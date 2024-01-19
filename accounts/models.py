from django.contrib.auth.models import AbstractUser
from django.db import models


class SiteUser(AbstractUser):
    email = models.EmailField(
        unique=True)

    USERNAME_FIELD = 'email'

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    is_driver = models.BooleanField(default=False)
    is_passenger = models.BooleanField(default=False)


class PassengerUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)


class DriverUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

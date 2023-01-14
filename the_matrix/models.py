from django.contrib.auth.models import AbstractUser, User
from django.db import models


# class User(AbstractUser):
#     is_passenger = models.BooleanField(default=False)
#     is_teacher = models.BooleanField(default=False)
#
#
# class Driver(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
#
#
# class Order(models.Model):
#     pass

class DriverUser(User):
    first_name = None
    last_name = None

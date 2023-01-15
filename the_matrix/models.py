from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    is_driver = models.BooleanField(default=False)
    is_passenger = models.BooleanField(default=False)


class PassengerUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    amount_of_money = models.FloatField(default=0)


class DriverUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    amount_of_money = models.FloatField(default=0)
    rating = models.FloatField(default=0)  # include this condition inside an if statement when calculating rating
    number_of_ratings = models.IntegerField(default=0)


# more information about potential values of "on_delete="
# https://stackoverflow.com/questions/38388423/what-does-on-delete-do-on-django-models


class Order(models.Model):
    id = models.IntegerField(primary_key=True)
    start_location = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)  # TODO: find ways to connect to Google API
    passenger = models.ForeignKey(PassengerUser, unique=True,  on_delete=models.SET_NULL)
    driver = models.ForeignKey(DriverUser, unique=True, on_delete=models.SET_NULL, blank=True, null=True)
    # or SET_DEFAULT (instead of SET_NULL), we will think about that
    price = models.FloatField(default=0)
    is_rated = models.BooleanField(default=False)

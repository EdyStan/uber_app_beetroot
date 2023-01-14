from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.db import transaction

from .models import User


class NewDriverForm(UserCreationForm):  # TODO: email field

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_driver = True
        user.save()
        return user


class NewPassengerForm(UserCreationForm):  # TODO: email field

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_driver = True
        user.save()
        return user

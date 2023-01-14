from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.db import transaction

from .models import User


class NewDriverForm(UserCreationForm):  # TODO: email field
    email = forms.EmailField(max_length=150)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        email = self.cleaned_data["email"]
        user = super().save(commit=False)
        user.email = email
        user.is_driver = True
        user.save()
        return user


class NewPassengerForm(UserCreationForm):  # TODO: email field
    email = forms.EmailField(max_length=150)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        email = self.cleaned_data["email"]
        user = super().save(commit=False)
        user.email = email
        user.is_passenger = True
        user.save()
        return user

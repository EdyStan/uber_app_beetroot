from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.db import transaction

from chat.models import Room
from .models import User


class NewDriverForm(UserCreationForm):
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
        Room.objects.create(name=f"Current Order", slug=f"{user.username}_chat_order", user1=None, user2=user)
        # when an order is created, user1 will be the passenger. I made rooms.html not show rooms with user1=None
        Room.objects.create(name=f"Driver {user.username} - Help Desk", slug=f"{user.username}-Help_Desk", user1=user, user2=None)
        return user


class NewPassengerForm(UserCreationForm):
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
        Room.objects.create(name=f"Passenger {user.username} - Help Desk", slug=f"{user.username}-Help_Desk", user1=user, user2=None)
        return user

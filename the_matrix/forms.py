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

class NewOrderForm(forms.Form):
    start_location = forms.CharField(label='Start Location', max_length=50, widget=forms.TextInput(attrs={'onfocus': 'select_pin(this)'}))
    end_location = forms.CharField(label='Destination', max_length=50, widget=forms.TextInput(attrs={'onfocus': 'select_pin(this)'}))
    price = forms.FloatField(label='Price', min_value=5, max_value=300, initial=5)

    def startCoordinates(self) -> list:
        coordinate_string = self.data['start_location']
        return [float(s) for s in coordinate_string.strip()[1:-1].split(", ")]

    def stopCoordinates(self) -> list:
        coordinate_string = self.data['end_location']
        return [float(s) for s in coordinate_string.strip()[1:-1].split(", ")]

    def price_value(self) -> float:
        return self.data['price']
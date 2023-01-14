from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import DriverUser
from django import forms


class NewDriverForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = DriverUser
        fields = ["username", "email", "password1", "password2"]

    def save(self, commit=True):
        user = super(NewDriverForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


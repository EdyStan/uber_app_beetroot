from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class CreateUserFormWithRole(forms.Form):
    username = forms.CharField(max_length=100)
    email = forms.EmailField()
    password1 = forms.CharField(max_length=100)
    password2 = forms.CharField(max_length=100)
    role = forms.CharField(max_length=20)

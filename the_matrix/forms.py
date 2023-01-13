from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import AppUser


class CreateUserForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class CreateUserFormWithRole(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    password1 = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = AppUser
        widgets = {
            'password': forms.PasswordInput(),
            'password1': forms.PasswordInput(),
        }
        fields = '__all__'

        def clean_password(self):
            password = self.cleaned_data.get('password')
            password1 = self.cleaned_data.get('password1')

            if not password1:
                raise forms.ValidationError("You have to verify your password")
            if password != password1:
                raise forms.ValidationError("Your passwords doesn't match")
            return password1

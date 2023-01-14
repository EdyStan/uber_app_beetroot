from django.shortcuts import render, redirect
from .forms import NewDriverForm
from django.contrib import messages
# from .models import DriverUser

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required


# @login_required(login_url='login')
def home_page(request):
    return render(request, 'main_app/main_page.html', {})


def register_driver(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = NewDriverForm(request.POST)
        if form.is_valid():
            user = form.save()
            user_name = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user_name)
            if user is not None:
                return redirect('login_driver')
    else:
        form = NewDriverForm()
        messages.error(request, 'Unsuccessful registration.')
    return render(request, 'main_app/register_driver.html', {'form': form})


def login_driver(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                # messages.info(request, f"You are now logged in as {username}.")
                return redirect("driver_page")
            else:
                messages.error(request, "Invalid username or password!")
        else:
            messages.error(request, "Invalid username or password!")
    form = AuthenticationForm()
    return render(request, 'main_app/login.html', {"login_form": form})


def logout_user(request):
    logout(request)
    return render(request, 'main_app/main_page.html', {})


def driver_page(request):
    return render(request, 'main_app/driver_page.html', {})

from django.shortcuts import render, redirect
from .forms import CreateUserForm
from django.contrib import messages

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# @login_required(login_url='login')
def home_page(request):
    return render(request, 'main_app/main_page.html', {})


def driver_page(request):
    return render(request, 'main_app/driver_page.html')


def passenger_page(request):
    return render(request, 'main_app/passenger_page.html')


def register_page(request):
    # if request.user.is_authenticated:
    #     return redirect('home')

    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)

            return redirect('login')
    return render(request, 'main_app/register.html', {'form': form})


def login_page(request):
    # if request.user.is_authenticated:
    #     return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username OR password is incorrect!')

    return render(request, 'main_app/login.html', {})


def logout_user(request):
    logout(request)
    return redirect('login')

from django.shortcuts import render, redirect
from .forms import CreateUserForm, CreateUserFormWithRole
from django.contrib import messages
from .models import UserType, AppUser

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# @login_required(login_url='login')
def home_page(request):
    return render(request, 'main_app/main_page.html', {})


def register_page(request):
    if request.user.is_authenticated:
        return redirect('home')

    form = CreateUserFormWithRole()

    if request.method == 'POST':
        form = CreateUserFormWithRole(request.POST)
        if form.is_valid():
            user_name = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user_name)

            return redirect('login')
    return render(request, 'main_app/register.html', {'form': form})


def login_page(request):
    if request.method == 'POST':
        email = request.POST.get('email')  # Get email value from form
        password = request.POST.get('password')  # Get password value from form
        role = request.POST.get('role')
        user = authenticate(request, email=email, role=role, password=password)

        if user is not None:
            login(request, user)
            type_obj = UserType.objects.get(user=user)
            if user.is_authenticated and type_obj.is_passenger:
                return redirect('passenger_menu')  # Go to student home
            elif user.is_authenticated and type_obj.is_driver:
                return redirect('driver_menu')  # Go to teacher home
        else:
            # Invalid email or password. Handle as you wish
            return redirect('home')

    return render(request, 'main_app/login.html', {})


def logout_user(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def passenger_page(request):
    if UserType.objects.get(user=request.user).is_passenger:
        return render(request, 'main_app/passenger_page.html')
    elif UserType.objects.get(user=request.user).is_driver:
        return redirect('driver_menu')
    else:
        return redirect('home')


@login_required(login_url='login')
def driver_page(request):
    if UserType.objects.get(user=request.user).is_driver:
        return render(request, 'main_app/driver_page.html')
    elif UserType.objects.get(user=request.user).is_passenger:
        return redirect('passenger_menu')
    else:
        return redirect('home')

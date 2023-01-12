from django.shortcuts import render, redirect
from .forms import CreateUserForm
from django.contrib import messages
from .models import user_type, AppUser

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# @login_required(login_url='login')
def home_page(request):
    return render(request, 'main_app/main_page.html', {})


# def register_page(request):
#     # if request.user.is_authenticated:
#     #     return redirect('home')
#
#     form = CreateUserForm()
#
#     if request.method == 'POST':
#         form = CreateUserForm(request.POST)
#         if form.is_valid():
#             form.save()
#             user = form.cleaned_data.get('username')
#             messages.success(request, 'Account was created for ' + user)
#
#             return redirect('login')
#     return render(request, 'main_app/register.html', {'form': form})

def register_page(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        ps = request.POST.get('passenger')
        dr = request.POST.get('driver')

        user = AppUser.objects.create_user(
            email=email,
        )
        user.set_password(password)
        user.save()

        usert = None
        if ps:
            usert = user_type(user=user, is_passenger=True)
        elif dr:
            usert = user_type(user=user, is_driver=True)

        usert.save()
        # Successfully registered. Redirect to homepage
        return redirect('login')
    return render(request, 'main_app/register.html')


def login_page(request):
    if request.method == 'POST':
        email = request.POST.get('email')  # Get email value from form
        password = request.POST.get('password')  # Get password value from form
        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            type_obj = user_type.objects.get(user=user)
            if user.is_authenticated and type_obj.is_passenger:
                return redirect('pmenu')  # Go to student home
            elif user.is_authenticated and type_obj.is_driver:
                return redirect('dmenu')  # Go to teacher home
        else:
            # Invalid email or password. Handle as you wish
            return redirect('home')

    return render(request, 'main_app/login.html', {})


def logout_user(request):
    logout(request)
    return redirect('login')


def pmenu(request):
    if request.user.is_authenticated and user_type.objects.get(user=request.user).is_passenger:
        return render(request, 'passenger_menu.html')
    elif request.user.is_authenticated and user_type.objects.get(user=request.user).is_driver:
        return redirect('dmenu')
    else:
        return redirect('home')


def dmenu(request):
    if request.user.is_authenticated and user_type.objects.get(user=request.user).is_driver:
        return render(request, 'driver_menu.html')
    elif request.user.is_authenticated and user_type.objects.get(user=request.user).is_student:
        return redirect('pmenu')
    else:
        return redirect('home')

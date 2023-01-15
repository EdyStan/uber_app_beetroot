from django.urls import path
from .views import passengers, drivers, common

urlpatterns = [
    path('', common.home_page, name='home'),
    path('register/', common.register_choices, name='register_choices'),  # register menu to choose if driver of passenger
    path('login/', common.login_user, name='login'),
    path('register/driver/', drivers.DriverSignUpView.as_view(), name='register_driver'),
    path('register/passenger/', passengers.PassengerSignUpView.as_view(), name='register_passenger'),
    path('logout/', common.logout_user, name='logout'),
    path('driver/', drivers.driver_page, name='driver_page'),
    path('passenger/', passengers.passenger_page, name='passenger_page'),
    path("password_change/", common.password_change, name="password_change"),
]

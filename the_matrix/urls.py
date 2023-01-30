from django.urls import path
from .views import passengers, drivers, common, order_details

urlpatterns = [
    path('', common.home_page, name='home'),
    path('register/', common.register_choices, name='register_choices'),  # register menu to choose if driver of passenger
    path('login/', common.login_user, name='login'),
    path('register/driver/', drivers.DriverSignUpView.as_view(), name='register_driver'),
    path('register/passenger/', passengers.PassengerSignUpView.as_view(), name='register_passenger'),
    path('logout/', common.logout_user, name='logout'),
    path('driver/', drivers.driver_page, name='driver_page'),
    path('driver_available_orders/', drivers.driver_available_orders, name='driver_available_orders'),
    path('driver_executed_orders/', drivers.driver_executed_orders, name='driver_executed_orders'),
    path('driver_income/', drivers.driver_income, name='driver_income'),
    path('driver_order/<int:order_id>/', drivers.driver_order, name='driver_order'),
    path('passenger/', passengers.passenger_page, name='passenger_page'),
    path('passenger_new_order/', passengers.passenger_new_order, name='passenger_new_order'),
    path('passenger_start_order/', passengers.passenger_start_order, name='passenger_start_order'),
    path("password_change/", common.password_change, name="password_change"),
    # google maps here
    path('geocode/', order_details.geocode, name="geocode"),
]

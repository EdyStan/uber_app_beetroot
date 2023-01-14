from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('register/', views.register_driver, name='register_driver'),
    path('login/', views.login_driver, name='login_driver'),
    path('logout/', views.logout_user, name='logout'),
    path('driver/', views.driver_page, name='driver_page'),
    # path('passenger/', views.passenger_page, name='passenger_menu'),
]

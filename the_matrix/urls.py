from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('register/', views.register_page, name='register'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('driver_menu/', views.dmenu, name='dmenu'),
    path('passenger_menu/', views.pmenu, name='pmenu'),
]

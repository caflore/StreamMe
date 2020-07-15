from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='app-home'),
    path('sign-up/', views.signup, name='app-signup'),
    path('login/', views.login, name='app-login'),
]
from django.contrib.auth import views as auth_views
from django.urls import path

from . import views
from .views import VodCreateView, VodDetailView, VodListView, StreamListView, StreamDetailView

urlpatterns = [
    path('', views.home, name='app-home'),
    path('sign-up/', views.signup, name='app-signup'),
    path('login/', auth_views.LoginView.as_view(template_name='app/login.html'), name='app-login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='app/logout.html'), name='app-logout'),
    path('accounts/profile/', views.profile, name='app-profile'),
    path('vods/', VodListView.as_view(), name='app-vods'),
    path('vods/<pk>/', VodDetailView.as_view(), name='app-vod-detail'),
    path('vod/new/', VodCreateView.as_view(), name='app-vod-create'),
    path('streams/', StreamListView.as_view(), name='app-streams'),
    path('streams/<pk>/', StreamDetailView.as_view(), name='app-stream-detail'),
]
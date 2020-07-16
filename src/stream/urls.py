from django.urls import path
from . import views

def fake_view(*args, **kwargs):
    raise Exception("This should never be called!")

urlpatterns = [
    path('start_stream', views.start_stream, name='start-stream'),
    path('stop_stream/', views.stop_stream, name='stop-login'),
    path('live/<username>/index.m3u8', fake_view, name="hls-url")
]
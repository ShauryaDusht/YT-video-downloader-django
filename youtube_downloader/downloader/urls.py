from django.urls import path
from .views import download_video, download_success

urlpatterns = [
    path('', download_video, name='download_video'),
    path('success/<str:title>/', download_success, name='download_success'),
]

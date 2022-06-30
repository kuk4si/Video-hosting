
from django.contrib import admin
from django.urls import path, include
from .views import MainPage, VideoView

urlpatterns = [
    path('', MainPage.as_view(), name='index'),
    path('watch/<int:pk>', VideoView.as_view(), name='watch'),
]

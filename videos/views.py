from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from .models import Video


class MainPage(ListView):
    model = Video
    template_name = 'videos/main.html'
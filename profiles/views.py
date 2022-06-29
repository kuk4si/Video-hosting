from django.shortcuts import render
from .models import Profile
# Create your views here.
from django.views.generic import DetailView


class ProfileDetail(DetailView):
    model = Profile
    template_name = 'profiles/detail.html'
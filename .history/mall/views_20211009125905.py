from django.shortcuts import render,
from . import templates.home

def home(request):
    return render(request, 'home.html')
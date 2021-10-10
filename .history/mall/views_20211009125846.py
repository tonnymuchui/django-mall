from django.shortcuts import render
from . import templates.h

def home(request):
    return render(request, 'home.html')
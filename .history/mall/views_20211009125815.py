from django.shortcuts import render
from .
def home(request):
    return render(request, 'home.html')
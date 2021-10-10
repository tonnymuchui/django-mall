from django.shortcuts import render
from .import t
def home(request):
    return render(request, 'home.html')
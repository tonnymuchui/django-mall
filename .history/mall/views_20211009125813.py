from django.shortcuts import render
from t
def home(request):
    return render(request, 'home.html')
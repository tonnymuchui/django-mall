from django.shortcuts import render
from .form import RegistrationForm

# Create your views here.
def register(register):
    
    return render('register.html')

def login(register):
    return render('sigin.html')

def logout(register):
    return render('sig.html')
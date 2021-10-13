from django.shortcuts import render

# Create your views here.
def register(register):
    from .forms import RegistrationForm
    return render('register.html')

def login(register):
    return render('register.html')

def logout(register):
    return render('register.html')
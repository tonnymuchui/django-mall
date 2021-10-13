from django.shortcuts import render
from .form import RegistrationForm

# Create your views here.
def register(re):
    context = {
        'form': RegistrationForm(),
    }
    return render(request, 'accounts/register.html', context)

def login(register):
    return render('sigin.html')

def logout(register):
    return render('signin.html')
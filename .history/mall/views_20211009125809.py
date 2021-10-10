from django.shortcuts import render
f
def home(request):
    return render(request, 'home.html')
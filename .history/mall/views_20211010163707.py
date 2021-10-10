from django.shortcuts import render

def home(request):
    products = Product.objects.
    return render(request, 'home.html')
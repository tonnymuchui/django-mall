from django.shortcuts import render

def home(request):
    products = Product.objects.all().fi
    return render(request, 'home.html')
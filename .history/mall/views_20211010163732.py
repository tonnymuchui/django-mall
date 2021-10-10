from django.shortcuts import render

def home(request):
    products = Product.objects.all().filter(is)
    return render(request, 'home.html')
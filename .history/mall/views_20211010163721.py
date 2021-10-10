from django.shortcuts import render

def home(request):
    products = Product.objects.all()
    return render(request, 'home.html')
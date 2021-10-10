from django.shortcuts import render

def home(request):
    products = Product.objects.all().filter(id=request.)
    return render(request, 'home.html')
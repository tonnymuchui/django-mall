from django.shortcuts import render

def home(request):
    products = Product.objects.all().filter(is_a)
    return render(request, 'home.html')
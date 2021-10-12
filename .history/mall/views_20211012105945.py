from django.shortcuts import render
from store.models import Product

def home(request):
    products = Product.objects.all().filter(is_available=True)

    content = {
        'products': products,
    }
    return render(request, '.html', content)
from django.shortcuts import render
from store.models import Product


# Create your views here.
def store(request):
    products = Product.objects.all().filter(is_available=True)

    content = {
        'products': products,
    }
    return render(request, 'store/store.html')
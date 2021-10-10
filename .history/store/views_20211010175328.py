from django.shortcuts import render
from store.models import Product


# Create your views here.
def store(request):
    products = Product.objects.all().filter(is_available=True)
    products_count = products.count()
    content = {
        'products': products,
        'products_count': products_count
    }
    return render(request, 'store/store.html', content)
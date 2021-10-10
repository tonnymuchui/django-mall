from django.shortcuts import get_object_or_404, render
from store.models import Product
from category.models import Category


# Create your views here.
def store(request, category_slug=None):
    categories = None
    products = None

    if category_slug is not None:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=categories, is_available=True)
    
    products = Product.objects.all().filter(is_available=True)
    products_count = products.count()
    content = {
        'products': products,
        'products_count': products_count,
    }
    return render(request, 'store/store.html', content)
from django.shortcuts import get_object_or_404, render
from store.models import Product


# Create your views here.
def store(request, category_slug=None):
    categories = get_object_or_404(Cate)
    products = Product.objects.all().filter(is_available=True)
    products_count = products.count()
    content = {
        'products': products,
        'products_count': products_count,
    }
    return render(request, 'store/store.html', content)
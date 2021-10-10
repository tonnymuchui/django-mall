from django.shortcuts import render

# Create your views here.
def store(request):
    products = Product.objects.all().filter(is_available=True)

    content = {
        'products': products,
    }
    return render(request, 'store/store.html')
from django.shortcuts import render

# Create your views here.
def add_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    try:
        


def cart(request):
    return render(request, 'store/cart.html')
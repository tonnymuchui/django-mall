from django.shortcuts import render

# Create your views here.
def _cart_id(request):
    cart = request.session.session.key
    if not cart:
        cart = request.session.create()

        return 
def add_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    try:
        cart = Cart.objects.get(icart_id=product.id)


def cart(request):
    return render(request, 'store/cart.html')
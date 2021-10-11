from django.urls import path
from .import views
urlpatterns = [
    path('/', views.cart, name='cart'),
    path('add_cart<slug:category_slug>/')
]

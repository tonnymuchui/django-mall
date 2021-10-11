from django.urls import path
from .import views
urlpatterns = [
    path('/', views.cart, name='cart'),
    path('add_cart<int:category_slug>/')
]

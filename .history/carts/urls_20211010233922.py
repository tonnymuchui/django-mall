from django.urls import path
from .import v
urlpatterns = [
    path('/', views.cart, name='cart'),
]

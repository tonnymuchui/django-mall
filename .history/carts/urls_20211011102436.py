from django.urls import path
from .import views
urlpatterns = [
    path('/', views.cart, name='cart'),
    path('<slug:category_slug>/')
]

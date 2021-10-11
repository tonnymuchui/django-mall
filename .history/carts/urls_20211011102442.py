from django.urls import path
from .import views
urlpatterns = [
    path('/', views.cart, name='cart'),
    path('add<slug:category_slug>/')
]

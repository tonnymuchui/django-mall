from django.urls import path
from .import views

urlpatterns = [
    path('', views.store, name='store'),
    path(<slug:category_>, views.store, name='store'),
]

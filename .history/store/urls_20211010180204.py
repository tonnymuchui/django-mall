from django.urls import path
from .import views

urlpatterns = [
    path('', views.store, name='store'),
    path(<slug:cate, views.store, name='store'),
]

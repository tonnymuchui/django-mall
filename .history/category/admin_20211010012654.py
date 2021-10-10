from django.contrib import admin
from .models  import Category

class Category(admin.Model):
admin.site.register(Category)
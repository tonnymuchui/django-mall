from django.contrib import admin
from .models  import Category

class CategoryAd(admin.Model):
admin.site.register(Category)
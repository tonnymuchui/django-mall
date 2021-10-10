from django.contrib import admin
from .models  import Category

class CategoryAdmin(admin.Model):
admin.site.register(Category)
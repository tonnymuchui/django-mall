from django.contrib import admin
from .models  import Category

class CategoryAdmin(admin.):
admin.site.register(Category)
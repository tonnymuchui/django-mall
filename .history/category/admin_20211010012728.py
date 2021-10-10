from django.contrib import admin
from .models  import Category

class CategoryAdmin(admin.Mo):
admin.site.register(Category)
from django.contrib import admin
from .models  import Category

class CategoryAdmin(adminModel):
admin.site.register(Category)
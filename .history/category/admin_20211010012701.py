from django.contrib import admin
from .models  import Category

class CategoryAdmin(admin.AdminModel):
admin.site.register(Category)
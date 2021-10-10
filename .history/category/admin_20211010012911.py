from django.contrib import admin
from .models  import Category

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = ('slug', 'category_name',)
    lis

admin.site.register(Category)
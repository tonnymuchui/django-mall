from django.contrib import admin
from .models  import Category

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = ('slug', 'category_name',)
    list_display = ()

admin.site.register(Category)
from django.contrib import admin
from .models  import Category

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = ('sl')

admin.site.register(Category)
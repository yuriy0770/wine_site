from django.contrib import admin

from main.models import Category, Product


@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    list_display = ['name', 'description']
    list_display_links = ['name', 'description']
    prepopulated_fields = {"slug": ('name',)}



@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'description']
    list_display_links = ['name', 'description']
    prepopulated_fields = {"slug": ('name',)}
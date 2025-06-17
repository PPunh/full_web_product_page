# coding=utf-8
from django.contrib import admin

from .models import *


@admin.register(ProductsModel)
class ProductsModelAdmin(admin.ModelAdmin):
    list_display = ['product_id', 'product_name', 'product_pricing', 'product_is_premium', 'product_created_at', 'product_updated_at', 'product_show_in_homepage']
    search_fields = ['product_name', 'product_description']
    list_filter = ['product_is_premium', 'product_created_at']
    ordering = ('product_id',)
    list_per_page = 20


@admin.register(ProductsCategory)
class ProductCategoryModelAdmin(admin.ModelAdmin):
    model = ProductsCategory
    list_display = ['category_name', 'category_descriptions']
    ordering = ('category_id',)

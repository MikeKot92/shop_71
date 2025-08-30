from .models import Product, ProductCategory
from django.contrib import admin
from django.db import models
from unfold.admin import ModelAdmin
from unfold.contrib.forms.widgets import WysiwygWidget

@admin.register(ProductCategory)
class ProductCategoryAdmin(ModelAdmin):
    list_display = ['name']


@admin.register(Product)
class ProductAdmin(ModelAdmin):
    list_display = ['name', 'price', 'quantity']
    search_fields = ['name']
    list_filter = ['category']

    formfield_overrides = {
        models.TextField: {
            "widget": WysiwygWidget,
        },
    }
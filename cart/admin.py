from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Cart


@admin.register(Cart)
class CartAdmin(ModelAdmin):
    list_display = ['product', 'quantity', 'created_timestamp']

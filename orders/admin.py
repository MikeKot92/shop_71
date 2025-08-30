from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Order


@admin.register(Order)
class OrderAdmin(ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'status', 'created']
    list_filter = ['status', 'created']

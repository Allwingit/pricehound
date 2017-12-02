# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Product_details
# Register your models here.
class ProductDetailsAdmin(admin.ModelAdmin):
    list_display = ('Brand', 'Product_name', 'Category','Store')

admin.site.register(Product_details,ProductDetailsAdmin)

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Product_details,Brand,Store,Category,Specification
# Register your models here.
class ProductDetailsAdmin(admin.ModelAdmin):
    list_display = ('Brand_name', 'Product_name', 'Product_Category','Product_Spec','Store_name')

admin.site.register(Product_details,ProductDetailsAdmin)

class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'domain','store_code')

admin.site.register(Store,StoreAdmin)

admin.site.register(Category)

class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'website')

admin.site.register(Brand,BrandAdmin)

class SpecificationAdmin(admin.ModelAdmin):
    list_display = ('color', 'Memory', 'RAM')

admin.site.register(Specification,SpecificationAdmin)

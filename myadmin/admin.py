from django.contrib import admin
from .models import Store, Category, Brand, ProductModel, ProductVariant, ProductListing


class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'domain','store_code')
admin.site.register(Store,StoreAdmin)

admin.site.register(Category)

class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'website')
admin.site.register(Brand,BrandAdmin)

class ProductModelAdmin(admin.ModelAdmin):
    list_display = ('brand', 'name','category','description','specifications')
admin.site.register(ProductModel,ProductModelAdmin)

class ProductVariantAdmin(admin.ModelAdmin):
    list_display = ('product_model', 'color','capacity','images','best_current_price')
admin.site.register(ProductVariant,ProductVariantAdmin)

class ProductListingAdmin(admin.ModelAdmin):
    list_display = ('product_variant', 'store','product_id','affiliate_url','current_price')
admin.site.register(ProductListing,ProductListingAdmin)

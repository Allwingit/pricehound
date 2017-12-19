from django.contrib import admin
from .models import Store, Category, Brand, ProductModel, ProductVariant, ProductListing


class StoreAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'domain','store_code')
admin.site.register(Store,StoreAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name')
admin.site.register(Category,CategoryAdmin)

class BrandAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'website')
admin.site.register(Brand,BrandAdmin)

class ProductModelAdmin(admin.ModelAdmin):
    list_display = ('id','brand', 'name','category','description','specifications')
admin.site.register(ProductModel,ProductModelAdmin)

class ProductVariantAdmin(admin.ModelAdmin):
    list_display = ('id','product_model', 'color','capacity','images','best_current_price')
admin.site.register(ProductVariant,ProductVariantAdmin)

class ProductListingAdmin(admin.ModelAdmin):
    list_display = ('id','product_variant', 'store','product_id','affiliate_url','current_price')
admin.site.register(ProductListing,ProductListingAdmin)

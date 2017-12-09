# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pricehound.settings')
from django.db import models
from django.utils import timezone

class Store(models.Model):

    name = models.CharField(max_length=200)
    domain = models.URLField()
    store_code = models.CharField(max_length=20)

    def add(self):
        self.added_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name

class Category(models.Model):

    name = models.CharField(max_length=200)

    def add(self):
        self.added_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name


class Brand(models.Model):

    name = models.CharField(max_length=200)
    website = models.URLField()

    def add(self):
        self.added_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name


class ProductModel(models.Model):

    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    name = models.CharField(max_length = 200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    specifications = models.TextField(blank=True)

    class Meta:
           unique_together =("brand", "name")

    def add(self):

        self.added_date = timezone.now()
        self.save()

    def __str__(self):
        return '%s %s' %(self.brand, self.name)


class ProductVariant(models.Model):

    # TODO: Add brand dropdown which will filter models by brand when adding variants


    product_model = models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    color = models.CharField(max_length = 50)
    capacity = models.CharField(max_length = 50, blank = True)
    images = models.TextField(blank=True) #change to image upload
    best_current_price = models.CharField(max_length=20, blank=True, editable = False)

    class Meta:
           unique_together =(("product_model", "color", "capacity"))


    def add(self):
        self.added_date = timezone.now()
        self.save()

    def __str__(self):
        return '%s - %s, %s' %(self.product_model, self.color, self.capacity)


class ProductListing(models.Model):

    # TODO: Add brand dropdown which will filter models by brand when selecting variants, for adding listing

    product_variant = models.ForeignKey(ProductVariant, on_delete=models.CASCADE)
    store = models.ForeignKey(Store, on_delete = models.CASCADE)
    product_id = models.CharField(max_length = 20, blank = True)
    listing_url = models.URLField(blank = True)
    affiliate_url = models.URLField(blank = True)
    current_price = models.CharField(max_length = 20, blank = True, editable = False)

    class Meta:
        unique_together =(("product_variant", "store",))


    def add(self):
        self.added_date = timezone.now()
        self.save()

    def __str__(self):
        return '%s > %s' %( self.product_variant, self.store)

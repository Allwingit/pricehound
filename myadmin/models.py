# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Store(models.Model):

    name = models.CharField(max_length=200)
    domain = models.URLField()
    store_code = models.CharField(max_length=20)

    def add(self):
        self.added_date = timezone.now()
        self.save()

    def __str__(self):
        return self.store_code

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

class Specification(models.Model):
    color = models.CharField(max_length=200)
    Memory = models.CharField(max_length=200)
    RAM = models.CharField(max_length=200)

    def add(self):
        self.added_date = timezone.now()
        self.save()

    def __str__(self):
        return '%s,%s,%s' %(self.color,self.Memory,self.RAM)


# Create your models here.
class Product_details(models.Model):
    Brand_name=models.ForeignKey(Brand, on_delete=models.CASCADE)
    Product_Category=models.ForeignKey(Category, on_delete=models.CASCADE)
    Product_name=models.CharField(max_length=100)
    Store_name=models.ForeignKey(Store, on_delete=models.CASCADE)
    Product_Spec= models.ForeignKey(Specification, on_delete=models.CASCADE)
    ProductID=models.CharField(max_length=100)

    def add(self):
        self.added_date = timezone.now()
        self.save()

    class Meta:
        """Table information."""
        verbose_name = ('Product Detail')
        verbose_name_plural = ('Product Details')

    def __str__(self):
        return '%s %s' %(self.Brand_name, self.Product_name)

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Product_details(models.Model):
    Brand=models.CharField(max_length=100)
    Category=models.CharField(max_length=100)
    Product_name=models.CharField(max_length=100)
    Store=models.CharField(max_length=100)
    ProductID=models.CharField(max_length=100)

    def add(self):
        self.added_date = timezone.now()
        self.save()

    class Meta:
        """Table information."""
        verbose_name = ('Product Detail')
        verbose_name_plural = ('Product Details')

    def __str__(self):
        return '%s %s' %(self.Brand, self.Product_name)

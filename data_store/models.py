# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from myadmin.models import Product_details

class PriceHistory(models.Model):
    listing = models.ForeignKey(Product_details, on_delete=models.CASCADE)
    price = models.CharField(max_length = 20)
    timestamp= models.DateTimeField(auto_now=True)

    class Meta:
        """Table information."""
        verbose_name = ('Price History')
        verbose_name_plural = ('Price History')

    def __str__(self):
        return '%s %s %s' %(self.listing.Brand_name, self.listing.Product_name,self.listing.Product_Spec)

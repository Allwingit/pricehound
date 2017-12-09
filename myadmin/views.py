# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import ProductModel

def update_price(request):
    products = ProductModel.objects.all()
    return render(request, 'pricehound_admin/product_list.html', {'products':products})

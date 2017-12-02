# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Product_details
# Create your views here.

def update_price(request):
    product_details=Product_details.objects.all()
    return render(request, 'pricehound_admin/product_list.html', {'products':product_details})

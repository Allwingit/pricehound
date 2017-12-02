# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.utils import timezone
from myadmin.models import Product_details
# Create your views here.
from data_store.tasks import fetch_from_fkin
from .models import PriceHistory
import requests
import json


def log_price_history(listing, price):

    price_history_entry = PriceHistory(listing = listing, price = price, timestamp = timezone.now())
    price_history_entry.save()


def update_price(request):

    product_models = Product_details.objects.all()

    for product_model in product_models:
        #print product_model
        if product_model.Store == "AM-IN":
            print "Amazon Listing"

        elif product_model.Store == "FK-IN":
            fetched_price = fetch_from_fkin.delay()
            #product_model.ProductID
            #fetch_from_fkin.delay(product_model.ProductID)
            price= fetched_price.get()
            #product_listing.current_price = price
            #product_listing.save(update_fields=['current_price'])
            #log_price_history(product_model, price)
    return render(request, 'pricechimp/crawl.html', {})

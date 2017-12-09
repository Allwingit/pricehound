# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.utils import timezone
from myadmin.models import ProductModel, ProductVariant, ProductListing, Store

from data_store.tasks import fetch_from_fkin
from .models import PriceHistory
import requests
import json


def log_price_history(listing, price):

   price_history_entry = PriceHistory(listing = listing, price = price, timestamp = timezone.now())
   price_history_entry.save()


def update_price(request):

    product_models = ProductModel.objects.all()

    for product_model in product_models:

        product_variants = ProductVariant.objects.filter(product_model = product_model) # filter attributes -> (pricehound_admin.models.ProductModel.product_model) = (product_model in loop)
        print product_model

        for product_variant in product_variants:

            print product_variant.color
            print product_variant.capacity
            product_listings = ProductListing.objects.filter(product_variant = product_variant) # same as above

            for product_listing in product_listings:

                listing_url = product_listing.listing_url
                store_code = product_listing.store.store_code

                if store_code == "AM-IN":

                    print "Amazon Listing"

                elif store_code == "FK-IN":

                    fetched_price = fetch_from_fkin.delay()

                    #product_listing.current_price = fetched_price
                    #product_listing.save(update_fields=['current_price'])

                    #log_price_history(product_listing, fetched_price)

    return render(request, 'pricechimp/crawl.html', {})

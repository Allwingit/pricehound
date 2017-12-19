from __future__ import absolute_import, unicode_literals
from celery import shared_task
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pricehound.settings')
import django
django.setup()

import requests
import json

from django.shortcuts import render
from django.utils import timezone
from django.contrib.auth import get_user_model

from myadmin.models import ProductModel,ProductVariant,ProductListing,Store
from .models import PriceHistory

@shared_task
def fetch_from_fkin():

        price_details = 0
        headers = {
            'Fk-Affiliate-Id': 'christoph31',
            'Fk-Affiliate-Token': 'e10dba90eca0457484328d9c51050512',
        }

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

                    params = (
                        ('id',product_listing.product_id),
                    )

                    if store_code == "AM-IN":
                        print "Amazon Listing"

                    elif store_code == "FK-IN":
                        response = requests.get('https://affiliate-api.flipkart.net/affiliate/1.0/product.json', headers=headers,params=params)
                        output = json.loads(response.text)
                        price  = output ['productBaseInfoV1']['flipkartSpecialPrice']['amount']

                        if price==0.0:
                            price  = output ['productBaseInfoV1']['flipkartSellingPrice']['amount']

                        #print price
                        product_listing.current_price = price
                        product_listing.save(update_fields=['current_price'])
                        price_details=price
                        price_history_entry = PriceHistory(listing = product_listing, price = price, timestamp = timezone.now())
                        price_history_entry.save()


        return price_details

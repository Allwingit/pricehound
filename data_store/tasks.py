from __future__ import absolute_import, unicode_literals
from celery import shared_task
import requests
import json
#from views import fetch_from_fkin,log_price_history
from django.shortcuts import render
from django.utils import timezone
from django.contrib.auth import get_user_model
#from .views import fetch_from_fkin
from myadmin.models import Product_details
from .models import PriceHistory


@shared_task
def fetch_from_fkin():

        product_models = Product_details.objects.all()

        headers = {
            'Fk-Affiliate-Id': 'christoph31',
            'Fk-Affiliate-Token': '3cbefcacc4584363a88b563a190b22ff',
        }

        for product_model in product_models:
                params = (
                    ('id',product_model.ProductID),
                )
                response = requests.get('https://affiliate-api.flipkart.net/affiliate/product/json', headers=headers, params=params)
                output = json.loads(response.text)
                price  = output ['productBaseInfo']['productAttributes']['sellingPrice']['amount']
                #print timezone.now()
                price_history_entry = PriceHistory(listing = product_model, price = price, timestamp = timezone.now())
                price_history_entry.save()
                #print output ['productBaseInfo']['productAttributes']['sellingPrice']['amount']

        return output ['productBaseInfo']['productAttributes']['sellingPrice']['amount']

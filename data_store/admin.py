# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import PriceHistory
# Register your models here.

class PriceHistoryAdmin(admin.ModelAdmin):
    list_display = ('listing', 'price', 'timestamp')
    readonly_fields = ('listing','timestamp','price')

admin.site.register(PriceHistory,PriceHistoryAdmin)

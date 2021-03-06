# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-17 17:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myadmin', '0002_auto_20171209_1918'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productlisting',
            name='affiliate_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='productlisting',
            name='current_price',
            field=models.CharField(blank=True, editable=False, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='productlisting',
            name='listing_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='productvariant',
            name='best_current_price',
            field=models.CharField(blank=True, editable=False, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='productvariant',
            name='images',
            field=models.TextField(blank=True, null=True),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-12-10 20:09
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0002_auto_20161209_2230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='Date',
            field=models.DateField(blank=True, default=datetime.datetime(2016, 12, 10, 20, 9, 20, 272291)),
        ),
        migrations.AlterField(
            model_name='news',
            name='Date',
            field=models.DateField(blank=True, default=datetime.datetime(2016, 12, 10, 20, 9, 20, 273937)),
        ),
        migrations.AlterField(
            model_name='product',
            name='Product_Image',
            field=models.ImageField(upload_to='mysite/static/images'),
        ),
        migrations.AlterField(
            model_name='research_timeline',
            name='Activity',
            field=models.TextField(blank=True, default=datetime.datetime(2016, 12, 10, 20, 9, 20, 273472)),
        ),
        migrations.AlterField(
            model_name='research_timeline',
            name='Date',
            field=models.DateField(blank=True, default=datetime.datetime(2016, 12, 10, 20, 9, 20, 273444)),
        ),
    ]
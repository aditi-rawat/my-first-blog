# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-03-23 09:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('popular', '0003_hotel_hotel1_annualreport_2011_hotel1_annualreport_2012_hotel1_annualreport_2013_hotel1_annualreport'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='status',
            field=models.CharField(default='Not-Approved', max_length=50),
        ),
    ]
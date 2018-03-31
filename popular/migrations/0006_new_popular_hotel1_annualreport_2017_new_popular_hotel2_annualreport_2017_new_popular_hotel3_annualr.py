# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-03-30 11:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('popular', '0005_auto_20180323_1026'),
    ]

    operations = [
        migrations.CreateModel(
            name='new_popular_hotel1_annualReport_2017',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('i', models.CharField(max_length=200)),
                ('month', models.CharField(max_length=10)),
                ('national_count', models.BigIntegerField()),
                ('international_count', models.BigIntegerField()),
                ('male_count', models.BigIntegerField()),
                ('female_count', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='new_popular_hotel2_annualReport_2017',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('i', models.CharField(max_length=200)),
                ('month', models.CharField(max_length=10)),
                ('national_count', models.BigIntegerField()),
                ('international_count', models.BigIntegerField()),
                ('male_count', models.BigIntegerField()),
                ('female_count', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='new_popular_hotel3_annualReport_2017',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('i', models.CharField(max_length=200)),
                ('month', models.CharField(max_length=10)),
                ('national_count', models.BigIntegerField()),
                ('international_count', models.BigIntegerField()),
                ('male_count', models.BigIntegerField()),
                ('female_count', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='new_popular_hotel4_annualReport_2017',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('i', models.CharField(max_length=200)),
                ('month', models.CharField(max_length=10)),
                ('national_count', models.BigIntegerField()),
                ('international_count', models.BigIntegerField()),
                ('male_count', models.BigIntegerField()),
                ('female_count', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='new_popular_hotel5_annualReport_2017',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('i', models.CharField(max_length=200)),
                ('month', models.CharField(max_length=10)),
                ('national_count', models.BigIntegerField()),
                ('international_count', models.BigIntegerField()),
                ('male_count', models.BigIntegerField()),
                ('female_count', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='new_popular_hotel_april_2017',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=200)),
                ('gender', models.CharField(max_length=200)),
                ('age', models.CharField(max_length=200)),
                ('nationality', models.CharField(max_length=200)),
                ('hometown', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='new_popular_hotel_august_2017',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=200)),
                ('gender', models.CharField(max_length=200)),
                ('age', models.CharField(max_length=200)),
                ('nationality', models.CharField(max_length=200)),
                ('hometown', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='new_popular_hotel_december_2017',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=200)),
                ('gender', models.CharField(max_length=200)),
                ('age', models.CharField(max_length=200)),
                ('nationality', models.CharField(max_length=200)),
                ('hometown', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='new_popular_hotel_february_2017',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=200)),
                ('gender', models.CharField(max_length=200)),
                ('age', models.CharField(max_length=200)),
                ('nationality', models.CharField(max_length=200)),
                ('hometown', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='new_popular_hotel_january_2017',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=200)),
                ('gender', models.CharField(max_length=200)),
                ('age', models.CharField(max_length=200)),
                ('nationality', models.CharField(max_length=200)),
                ('hometown', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='new_popular_hotel_july_2017',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=200)),
                ('gender', models.CharField(max_length=200)),
                ('age', models.CharField(max_length=200)),
                ('nationality', models.CharField(max_length=200)),
                ('hometown', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='new_popular_hotel_june_2017',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=200)),
                ('gender', models.CharField(max_length=200)),
                ('age', models.CharField(max_length=200)),
                ('nationality', models.CharField(max_length=200)),
                ('hometown', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='new_popular_hotel_march_2017',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=200)),
                ('gender', models.CharField(max_length=200)),
                ('age', models.CharField(max_length=200)),
                ('nationality', models.CharField(max_length=200)),
                ('hometown', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='new_popular_hotel_may_2017',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=200)),
                ('gender', models.CharField(max_length=200)),
                ('age', models.CharField(max_length=200)),
                ('nationality', models.CharField(max_length=200)),
                ('hometown', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='new_popular_hotel_november_2017',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=200)),
                ('gender', models.CharField(max_length=200)),
                ('age', models.CharField(max_length=200)),
                ('nationality', models.CharField(max_length=200)),
                ('hometown', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='new_popular_hotel_october_2017',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=200)),
                ('gender', models.CharField(max_length=200)),
                ('age', models.CharField(max_length=200)),
                ('nationality', models.CharField(max_length=200)),
                ('hometown', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='new_popular_hotel_september_2017',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=200)),
                ('gender', models.CharField(max_length=200)),
                ('age', models.CharField(max_length=200)),
                ('nationality', models.CharField(max_length=200)),
                ('hometown', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='new_popular_permit_office_annualReport_2017',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('i', models.CharField(max_length=200)),
                ('month', models.CharField(max_length=10)),
                ('national_count', models.BigIntegerField()),
                ('international_count', models.BigIntegerField()),
                ('male_count', models.BigIntegerField()),
                ('female_count', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='new_popular_permit_office_april_2017',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=200)),
                ('gender', models.CharField(max_length=200)),
                ('age', models.CharField(max_length=200)),
                ('nationality', models.CharField(max_length=200)),
                ('hometown', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='new_popular_permit_office_august_2017',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=200)),
                ('gender', models.CharField(max_length=200)),
                ('age', models.CharField(max_length=200)),
                ('nationality', models.CharField(max_length=200)),
                ('hometown', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='new_popular_permit_office_december_2017',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=200)),
                ('gender', models.CharField(max_length=200)),
                ('age', models.CharField(max_length=200)),
                ('nationality', models.CharField(max_length=200)),
                ('hometown', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='new_popular_permit_office_february_2017',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=200)),
                ('gender', models.CharField(max_length=200)),
                ('age', models.CharField(max_length=200)),
                ('nationality', models.CharField(max_length=200)),
                ('hometown', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='new_popular_permit_office_january_2017',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=200)),
                ('gender', models.CharField(max_length=200)),
                ('age', models.CharField(max_length=200)),
                ('nationality', models.CharField(max_length=200)),
                ('hometown', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='new_popular_permit_office_july_2017',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=200)),
                ('gender', models.CharField(max_length=200)),
                ('age', models.CharField(max_length=200)),
                ('nationality', models.CharField(max_length=200)),
                ('hometown', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='new_popular_permit_office_june_2017',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=200)),
                ('gender', models.CharField(max_length=200)),
                ('age', models.CharField(max_length=200)),
                ('nationality', models.CharField(max_length=200)),
                ('hometown', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='new_popular_permit_office_march_2017',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=200)),
                ('gender', models.CharField(max_length=200)),
                ('age', models.CharField(max_length=200)),
                ('nationality', models.CharField(max_length=200)),
                ('hometown', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='new_popular_permit_office_may_2017',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=200)),
                ('gender', models.CharField(max_length=200)),
                ('age', models.CharField(max_length=200)),
                ('nationality', models.CharField(max_length=200)),
                ('hometown', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='new_popular_permit_office_november_2017',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=200)),
                ('gender', models.CharField(max_length=200)),
                ('age', models.CharField(max_length=200)),
                ('nationality', models.CharField(max_length=200)),
                ('hometown', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='new_popular_permit_office_october_2017',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=200)),
                ('gender', models.CharField(max_length=200)),
                ('age', models.CharField(max_length=200)),
                ('nationality', models.CharField(max_length=200)),
                ('hometown', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='new_popular_permit_office_september_2017',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=200)),
                ('gender', models.CharField(max_length=200)),
                ('age', models.CharField(max_length=200)),
                ('nationality', models.CharField(max_length=200)),
                ('hometown', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='overall_sikkim_count',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('i', models.CharField(max_length=200)),
                ('year', models.CharField(max_length=10)),
                ('national_count', models.BigIntegerField()),
                ('international_count', models.BigIntegerField()),
                ('male_count', models.BigIntegerField()),
                ('female_count', models.BigIntegerField()),
            ],
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Click',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('idfa', models.CharField(max_length=200)),
                ('advertiser_id', models.CharField(max_length=200)),
                ('product_id', models.CharField(max_length=200)),
                ('campaign_id', models.CharField(max_length=200)),
                ('converted', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Element',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('element_id', models.CharField(max_length=200)),
                ('element_type', models.CharField(max_length=200)),
                ('product_id', models.CharField(max_length=200)),
                ('advertiser_id', models.CharField(max_length=200)),
                ('campaign_id', models.CharField(max_length=200)),
                ('impressions', models.IntegerField(default=0)),
                ('clicks', models.IntegerField(default=0)),
                ('conversions', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Intent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('idfa', models.CharField(max_length=200)),
                ('product_id', models.CharField(max_length=200)),
                ('advertiser_id', models.CharField(max_length=200)),
                ('converted', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]

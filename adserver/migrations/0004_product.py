# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adserver', '0003_element_product_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('product_id', models.CharField(max_length=200)),
                ('product_name', models.CharField(max_length=200)),
                ('product_price', models.DecimalField(max_digits=12, decimal_places=2)),
                ('advertiser_id', models.CharField(max_length=200)),
                ('product_image_url', models.CharField(max_length=2000)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]

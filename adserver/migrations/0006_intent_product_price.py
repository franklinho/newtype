# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adserver', '0005_auto_20150127_2216'),
    ]

    operations = [
        migrations.AddField(
            model_name='intent',
            name='product_price',
            field=models.DecimalField(default=0.0, max_digits=12, decimal_places=2),
            preserve_default=False,
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adserver', '0007_campaign'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_url',
            field=models.CharField(default='', max_length=2000),
            preserve_default=False,
        ),
    ]

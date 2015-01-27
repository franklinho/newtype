# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adserver', '0002_click_element_ids'),
    ]

    operations = [
        migrations.AddField(
            model_name='element',
            name='product_name',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adserver', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='click',
            name='element_ids',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]

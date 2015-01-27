# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adserver', '0004_product'),
    ]

    operations = [
        migrations.RenameField(
            model_name='element',
            old_name='product_name',
            new_name='text',
        ),
    ]

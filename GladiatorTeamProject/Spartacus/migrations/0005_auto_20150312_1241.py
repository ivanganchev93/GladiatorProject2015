# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Spartacus', '0004_auto_20150312_1231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='name',
            field=models.CharField(unique=True, max_length=128),
    #        preserve_default=True,
        ),
    ]

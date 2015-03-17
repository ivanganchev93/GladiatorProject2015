# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Spartacus', '0008_auto_20150313_1550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='itemType',
            field=models.CharField(default=b'sword', max_length=128, choices=[(b'sword', b'sword'), (b'shield', b'shield'), (b'armor', b'armor'), (b'helmet', b'helmet'), (b'boots', b'boots')]),
           # preserve_default=True,
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Spartacus', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='itemType',
            field=models.CharField(default=b'sword', max_length=128, choices=[(b'sword', b'sword'), (b'shield', b'shield'), (b'armor', b'armor')]),
            preserve_default=True,
        ),
    ]

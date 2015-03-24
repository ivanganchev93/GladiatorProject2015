# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Spartacus', '0011_auto_20150317_1856'),
    ]

    operations = [
        migrations.AddField(
            model_name='avatar',
            name='isFighting',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='avatar',
            name='cash',
            field=models.IntegerField(default=100),
            preserve_default=True,
        ),
    ]

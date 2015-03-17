# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('Spartacus', '0009_auto_20150316_2005'),
    ]

    operations = [
        migrations.AddField(
            model_name='avatar',
            name='fightStartedAt',
            field=models.DateField(default=datetime.datetime(2015, 3, 17, 18, 47, 53, 842000)),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='avatar',
            name='isFighting',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Spartacus', '0007_auto_20150312_1358'),
    ]

    operations = [
        migrations.AddField(
            model_name='avatar',
            name='cash',
            field=models.IntegerField(default=1000),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='avatar',
            name='intelligence',
            field=models.IntegerField(default=10),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='avatar',
            name='points',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='avatar',
            name='victories',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='item',
            name='price',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]

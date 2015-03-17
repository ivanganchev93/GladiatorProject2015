# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Spartacus', '0010_auto_20150317_1847'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='avatar',
            name='fightStartedAt',
        ),
        migrations.RemoveField(
            model_name='avatar',
            name='isFighting',
        ),
    ]

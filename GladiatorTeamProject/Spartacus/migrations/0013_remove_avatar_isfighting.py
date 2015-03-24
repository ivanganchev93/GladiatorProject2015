# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Spartacus', '0012_auto_20150324_1245'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='avatar',
            name='isFighting',
        ),
    ]

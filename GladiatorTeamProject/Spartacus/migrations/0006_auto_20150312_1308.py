# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Spartacus', '0005_auto_20150312_1241'),
    ]

    operations = [
        migrations.RenameField(
            model_name='avataritem',
            old_name='user',
            new_name='avatar',
        ),
    ]

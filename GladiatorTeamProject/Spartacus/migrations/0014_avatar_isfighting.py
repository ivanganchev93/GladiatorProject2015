# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Spartacus', '0013_remove_avatar_isfighting'),
    ]

    operations = [
        migrations.AddField(
            model_name='avatar',
            name='isFighting',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Spartacus', '0003_auto_20150312_1220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avataritem',
            name='item',
            field=models.ForeignKey(to='Spartacus.Item'),
          #  preserve_default=True,
        ),
    ]

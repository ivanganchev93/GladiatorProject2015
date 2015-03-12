# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Avatar',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('attack', models.IntegerField(default=10)),
                ('deffence', models.IntegerField(default=10)),
                ('strength', models.IntegerField(default=10)),
                ('agility', models.IntegerField(default=10)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AvatarItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('equiped', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('attack', models.IntegerField(default=10)),
                ('deffence', models.IntegerField(default=10)),
                ('strength', models.IntegerField(default=10)),
                ('agility', models.IntegerField(default=10)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='avataritem',
            name='item',
            field=models.OneToOneField(to='Spartacus.Item'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='avataritem',
            name='user',
            field=models.ForeignKey(to='Spartacus.Avatar'),
            preserve_default=True,
        ),
    ]

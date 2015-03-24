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
                ('picture', models.ImageField(upload_to=b'profile_images', blank=True)),
                ('cash', models.IntegerField(default=100)),
                ('attack', models.IntegerField(default=10)),
                ('deffence', models.IntegerField(default=10)),
                ('strength', models.IntegerField(default=10)),
                ('agility', models.IntegerField(default=10)),
                ('intelligence', models.IntegerField(default=10)),
                ('isFighting', models.BooleanField(default=False)),
                ('victories', models.IntegerField(default=0)),
                ('points', models.IntegerField(default=0)),
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
                ('avatar', models.ForeignKey(to='Spartacus.Avatar')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('price', models.IntegerField(default=0)),
                ('itemType', models.CharField(default=b'sword', max_length=128, choices=[(b'sword', b'sword'), (b'shield', b'shield'), (b'armor', b'armor'), (b'helmet', b'helmet'), (b'boots', b'boots')])),
                ('name', models.CharField(unique=True, max_length=128)),
                ('picture', models.ImageField(upload_to=b'item_images', blank=True)),
                ('attack', models.IntegerField(default=10)),
                ('deffence', models.IntegerField(default=10)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='avataritem',
            name='item',
            field=models.ForeignKey(to='Spartacus.Item'),
            preserve_default=True,
        ),
    ]

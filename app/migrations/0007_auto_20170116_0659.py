# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-16 06:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20170116_0429'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='is_spymaster',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='player',
            name='username',
            field=models.CharField(default=None, max_length=30),
        ),
    ]

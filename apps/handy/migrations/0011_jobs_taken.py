# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-10-13 01:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('handy', '0010_auto_20181013_0104'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobs',
            name='taken',
            field=models.BooleanField(default=False),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-10-13 00:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('handy', '0005_auto_20181013_0011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myjobs',
            name='title',
            field=models.CharField(max_length=255, null=True),
        ),
    ]

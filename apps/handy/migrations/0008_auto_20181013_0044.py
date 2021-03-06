# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-10-13 00:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('handy', '0007_auto_20181013_0042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myjobs',
            name='jobs',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='owned_job', to='handy.Jobs'),
        ),
        migrations.AlterField(
            model_name='myjobs',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_myjob', to='handy.User'),
        ),
    ]

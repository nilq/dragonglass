# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-12 08:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timesheet', '0004_auto_20160712_0800'),
    ]

    operations = [
        migrations.AlterField(
            model_name='time',
            name='stop_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]

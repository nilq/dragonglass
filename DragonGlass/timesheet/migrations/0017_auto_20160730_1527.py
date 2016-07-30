# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-30 13:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('timesheet', '0016_auto_20160730_1522'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='project',
        ),
        migrations.AddField(
            model_name='person',
            name='current_snippet',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='timesheet.Time'),
        ),
    ]

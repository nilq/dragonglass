# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-12 08:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('timesheet', '0003_auto_20160712_0735'),
    ]

    operations = [
        migrations.RenameField(
            model_name='time',
            old_name='person',
            new_name='person_safe',
        ),
        migrations.AddField(
            model_name='person',
            name='current_snippet',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='timesheet.Time'),
        ),
    ]

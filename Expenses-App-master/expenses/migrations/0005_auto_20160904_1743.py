# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-04 17:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0004_auto_20160904_1742'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='time',
            field=models.TimeField(default=django.utils.timezone.now),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-04-17 21:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cashier', '0007_auto_20170415_0050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='emergencyTlfNumber',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Emergency phone'),
        ),
    ]

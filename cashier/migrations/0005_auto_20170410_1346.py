# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-04-10 11:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cashier', '0004_auto_20170407_0224'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='accountNr',
            field=models.CharField(blank=True, max_length=20, verbose_name='Konto-nr'),
        ),
        migrations.AddField(
            model_name='room',
            name='hasMobilePay',
            field=models.BooleanField(default=False, verbose_name='MobilePay'),
        ),
    ]
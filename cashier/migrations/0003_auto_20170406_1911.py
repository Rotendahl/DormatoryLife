# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2017-04-06 17:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cashier', '0002_transaction_refunded'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='refunded',
            field=models.BooleanField(default=True, verbose_name='Refunded'),
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-11-08 13:26
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cashier', '0016_payment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='dateOfRefund',
            field=models.DateField(default=datetime.date(2017, 11, 8), verbose_name='Date of transfer'),
        ),
    ]
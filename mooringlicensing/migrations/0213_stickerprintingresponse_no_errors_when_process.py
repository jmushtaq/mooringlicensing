# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-08-17 06:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mooringlicensing', '0212_auto_20210817_1221'),
    ]

    operations = [
        migrations.AddField(
            model_name='stickerprintingresponse',
            name='no_errors_when_process',
            field=models.NullBooleanField(default=None),
        ),
    ]

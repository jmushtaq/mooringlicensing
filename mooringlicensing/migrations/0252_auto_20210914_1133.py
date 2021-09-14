# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-09-14 03:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mooringlicensing', '0251_merge_20210914_0613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='approval',
            name='lodgement_number',
            field=models.CharField(blank=True, max_length=9, unique=True),
        ),
        migrations.AlterField(
            model_name='dcvadmission',
            name='lodgement_number',
            field=models.CharField(blank=True, max_length=10, unique=True),
        ),
        migrations.AlterField(
            model_name='dcvpermit',
            name='lodgement_number',
            field=models.CharField(blank=True, max_length=10, unique=True),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-04-06 06:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mooringlicensing', '0044_mooringbay_mooring_bay_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mooringbay',
            old_name='mooring_bay_id',
            new_name='mooring_bookings_id',
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2022-03-15 08:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mooringlicensing', '0277_proposal_fee_season'),
    ]

    operations = [
        migrations.AddField(
            model_name='sticker',
            name='replaced_for_renewal',
            field=models.BooleanField(default=False),
        ),
    ]

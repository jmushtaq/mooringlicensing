# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-08-05 09:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mooringlicensing', '0205_stickerprintingresponse_processed'),
    ]

    operations = [
        migrations.AddField(
            model_name='stickerprintingresponse',
            name='email_message_id',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]

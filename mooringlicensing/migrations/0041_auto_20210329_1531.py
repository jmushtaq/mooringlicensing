# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-03-29 07:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mooringlicensing', '0040_proposal_proposal_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proposaltype',
            name='code',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]

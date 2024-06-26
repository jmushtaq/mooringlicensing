# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2022-03-29 08:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mooringlicensing', '0286_auto_20220328_1616'),
    ]

    operations = [
        migrations.CreateModel(
            name='StickerPrintedContact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('type', models.CharField(choices=[('to', 'To'), ('cc', 'Cc'), ('bcc', 'Bcc')], max_length=255)),
                ('enabled', models.BooleanField(default=True)),
            ],
        ),
    ]

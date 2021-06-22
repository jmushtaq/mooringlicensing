# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-06-22 08:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mooringlicensing', '0175_merge_20210622_1557'),
    ]

    operations = [
        migrations.RenameField(
            model_name='approvalhistory',
            old_name='sticker',
            new_name='stickers',
        ),
        migrations.AlterField(
            model_name='approvalhistory',
            name='proposal',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='approval_history_records', to='mooringlicensing.Proposal'),
            preserve_default=False,
        ),
    ]

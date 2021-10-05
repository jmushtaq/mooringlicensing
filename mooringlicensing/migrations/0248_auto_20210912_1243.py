# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-09-12 04:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mooringlicensing', '0247_proposal_keep_existing_mooring'),
    ]

    operations = [
        migrations.AddField(
            model_name='sticker',
            name='dcv_permit',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='stickers', to='mooringlicensing.DcvPermit'),
        ),
        migrations.AlterField(
            model_name='proposal',
            name='customer_status',
            field=models.CharField(choices=[('draft', 'Draft'), ('with_assessor', 'Under Review'), ('awaiting_endorsement', 'Awaiting Endorsement'), ('awaiting_documents', 'Awaiting Documents'), ('printing_sticker', 'Printing Sticker'), ('approved', 'Approved'), ('declined', 'Declined'), ('discarded', 'Discarded'), ('awaiting_payment', 'Awaiting Payment'), ('expired', 'Expired')], default='draft', max_length=40, verbose_name='Customer Status'),
        ),
        migrations.AlterField(
            model_name='proposal',
            name='processing_status',
            field=models.CharField(choices=[('draft', 'Draft'), ('with_assessor', 'With Assessor'), ('with_assessor_requirements', 'With Assessor (Requirements)'), ('with_approver', 'With Approver'), ('printing_sticker', 'Printing Sticker'), ('awaiting_endorsement', 'Awaiting Endorsement'), ('awaiting_documents', 'Awaiting Documents'), ('approved', 'Approved'), ('declined', 'Declined'), ('discarded', 'Discarded'), ('awaiting_payment', 'Awaiting Payment'), ('expired', 'Expired')], default='draft', max_length=40, verbose_name='Processing Status'),
        ),
    ]

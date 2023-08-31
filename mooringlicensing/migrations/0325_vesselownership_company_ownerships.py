# Generated by Django 3.2.20 on 2023-08-31 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mooringlicensing', '0324_alter_companyownership_end_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='vesselownership',
            name='company_ownerships',
            field=models.ManyToManyField(blank=True, null=True, related_name='vessel_ownerships', to='mooringlicensing.CompanyOwnership'),
        ),
    ]

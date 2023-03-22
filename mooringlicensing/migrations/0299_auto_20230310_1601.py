# Generated by Django 3.2.18 on 2023-03-10 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mooringlicensing', '0298_auto_20230310_1518'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proposal',
            name='vessel_beam',
            field=models.DecimalField(decimal_places=2, max_digits=8, null=True),
        ),
        migrations.AlterField(
            model_name='proposal',
            name='vessel_draft',
            field=models.DecimalField(decimal_places=2, max_digits=8, null=True),
        ),
        migrations.AlterField(
            model_name='proposal',
            name='vessel_length',
            field=models.DecimalField(decimal_places=2, max_digits=8, null=True),
        ),
        migrations.AlterField(
            model_name='proposal',
            name='vessel_weight',
            field=models.DecimalField(decimal_places=2, max_digits=8, null=True),
        ),
    ]

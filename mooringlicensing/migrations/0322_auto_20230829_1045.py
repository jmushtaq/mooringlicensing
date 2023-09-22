# Generated by Django 3.2.20 on 2023-08-29 02:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mooringlicensing', '0321_alter_dcvpermit_lodgement_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='proofofidentitydocument',
            name='proposal',
        ),
        migrations.CreateModel(
            name='ProposalProofOfIdentityDocument',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enabled', models.BooleanField(default=True)),
                ('proof_of_identity_document', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mooringlicensing.proofofidentitydocument')),
                ('proposal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mooringlicensing.proposal')),
            ],
        ),
        migrations.AddField(
            model_name='proposal',
            name='proof_of_identity_documents',
            field=models.ManyToManyField(through='mooringlicensing.ProposalProofOfIdentityDocument', to='mooringlicensing.ProofOfIdentityDocument'),
        ),
    ]
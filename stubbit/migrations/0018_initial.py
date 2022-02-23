# Generated by Django 4.0.2 on 2022-02-23 12:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('stubbit', '0017_remove_organization_licenseid_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='License',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('LicenseType', models.CharField(choices=[('Trial', 'Trial'), ('Tier 1', 'Tier 1'), ('Tier 2', 'Tier 2'), ('Tier 3', 'Tier 3'), ('Tier 4', 'Tier 4'), ('Tier 5', 'Tier 5')], default='Trial', max_length=15)),
                ('LicenseContent', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('OrganizationName', models.CharField(max_length=255)),
                ('StartDate', models.DateTimeField(auto_now_add=True)),
                ('AddressCountry', models.CharField(max_length=20)),
                ('AddressState', models.CharField(max_length=2)),
                ('AddressZip', models.IntegerField()),
                ('AddressCity', models.CharField(max_length=20)),
                ('AddressStreet', models.CharField(max_length=20)),
                ('AddressBuildingNumber', models.CharField(max_length=20, null=True)),
                ('PhoneNumber', models.CharField(max_length=12, null=True)),
                ('LicenseID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='stubbit.license')),
            ],
        ),
        migrations.CreateModel(
            name='Stub',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=255)),
                ('Overview', models.CharField(max_length=65535)),
                ('Category', models.CharField(choices=[('Request', 'Request'), ('Bug', 'Bug'), ('New Feature', 'New Feature'), ('Upgrade', 'Upgrade'), ('Improvement', 'Improvement'), ('Suggestion', 'Suggestion'), ('System Failure', 'System Failure')], max_length=14)),
                ('Urgency', models.CharField(choices=[('Immediate', 'Immediate'), ('Highly Important', 'Highly Important'), ('Important', 'Important'), ('Somewhat Important', 'Somewhat Important'), ('When You Have Time', 'When You Have Time')], max_length=18)),
                ('Domain', models.CharField(max_length=20)),
                ('StartDate', models.DateTimeField(null=True)),
                ('EstimatedCompletionTime', models.IntegerField(null=True)),
                ('EstimatedCompletionTimeUOM', models.CharField(max_length=1, null=True)),
                ('PriorityInQueue', models.FloatField(null=True)),
                ('InProcess', models.BooleanField()),
                ('Completed', models.BooleanField()),
                ('CreationDate', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(max_length=20, unique=True)),
                ('FirstName', models.CharField(max_length=255)),
                ('LastName', models.CharField(max_length=255)),
                ('Email', models.CharField(max_length=255)),
                ('Department', models.CharField(max_length=20)),
                ('Administrator', models.BooleanField()),
                ('OrganizationID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='stubbit.organization')),
            ],
        ),
        migrations.CreateModel(
            name='UserPass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('EncryptedPassword', models.CharField(max_length=60)),
                ('EncrpytionMethod', models.CharField(max_length=10)),
                ('EncryptionKey', models.CharField(max_length=255)),
                ('UserFileID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stubbit.userfile')),
            ],
        ),
        migrations.CreateModel(
            name='UserMeta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('AccountCreationDate', models.DateTimeField(auto_now_add=True)),
                ('LastLogInDate', models.DateTimeField()),
                ('UserFileID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stubbit.userfile')),
            ],
        ),
        migrations.CreateModel(
            name='StubAttachment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TotalSize', models.FloatField()),
                ('CompressedSize', models.FloatField()),
                ('FileServerPath', models.CharField(max_length=255)),
                ('StubID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stubbit.stub')),
            ],
        ),
        migrations.AddField(
            model_name='stub',
            name='DeveloperUserFileID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='DeveloperUserFileID', to='stubbit.userfile'),
        ),
        migrations.AddField(
            model_name='stub',
            name='IssuerUserFileID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='IssuerUserFileID', to='stubbit.userfile'),
        ),
    ]
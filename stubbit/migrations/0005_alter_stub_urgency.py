# Generated by Django 4.0.2 on 2022-02-17 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stubbit', '0004_stub_issuer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stub',
            name='Urgency',
            field=models.CharField(choices=[('High', 'High'), ('Medium', 'Medium'), ('Low', 'Low')], max_length=20, null=True),
        ),
    ]
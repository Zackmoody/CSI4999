# Generated by Django 4.0.2 on 2022-02-17 20:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stubbit', '0003_rename_users_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='stub',
            name='Issuer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='stubbit.profile'),
        ),
    ]
# Generated by Django 4.0.2 on 2022-03-07 20:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stubbit', '0006_usermeta_loggedin'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usermeta',
            name='LoggedIn',
        ),
    ]

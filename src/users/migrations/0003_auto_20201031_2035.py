# Generated by Django 3.1 on 2020-10-31 17:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20201031_1755'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='firstname',
            new_name='first_name',
        ),
    ]

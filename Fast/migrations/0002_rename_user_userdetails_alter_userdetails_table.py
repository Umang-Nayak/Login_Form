# Generated by Django 4.2.7 on 2023-11-07 10:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Fast', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='UserDetails',
        ),
        migrations.AlterModelTable(
            name='userdetails',
            table='UserDetails',
        ),
    ]

# Generated by Django 4.0.3 on 2022-08-18 01:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_rename_disk_using_gb_diskchanged_disk_using_gb_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='diskchanged',
            old_name='create_at',
            new_name='created_at',
        ),
    ]

# Generated by Django 4.2.4 on 2023-08-22 11:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_alter_complaint_status'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='request',
            new_name='waste_request',
        ),
    ]

# Generated by Django 4.1.2 on 2022-11-19 17:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0023_service'),
    ]

    operations = [
        migrations.RenameField(
            model_name='service',
            old_name='s_name',
            new_name='service_name',
        ),
    ]

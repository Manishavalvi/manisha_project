# Generated by Django 4.1.2 on 2022-11-20 16:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0024_rename_s_name_service_service_name'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Service',
        ),
    ]
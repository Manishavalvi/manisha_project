# Generated by Django 4.1.2 on 2022-11-15 12:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0019_service_alter_doctor_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='service',
            old_name='service_item',
            new_name='service_title',
        ),
        migrations.RemoveField(
            model_name='service',
            name='service_name',
        ),
    ]
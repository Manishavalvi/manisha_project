# Generated by Django 4.1.2 on 2022-11-08 07:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_alter_patient_p_city_alter_patient_p_state'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Patient',
        ),
    ]

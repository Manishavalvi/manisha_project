# Generated by Django 4.1.2 on 2022-11-12 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0013_alter_appouser_doctor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appouser',
            name='department',
        ),
        migrations.RemoveField(
            model_name='appouser',
            name='doctor',
        ),
        migrations.AddField(
            model_name='appouser',
            name='l_name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
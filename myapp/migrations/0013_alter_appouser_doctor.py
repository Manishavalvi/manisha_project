# Generated by Django 4.1.2 on 2022-11-11 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0012_alter_appouser_department_alter_appouser_doctor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appouser',
            name='doctor',
            field=models.CharField(choices=[('Dr.Harish Chauhan', 'DR.HARISH CHAUHAN'), ('Dr.Manish Malhotra', 'DR.MANISH MALHOTRA'), ('Dr.Helly Shah', 'DR.HELLY SHAH'), ('Dr.Bhavesh Patel', 'DR.BHAVESH PATEL'), ('Dr.Rahul Patel', 'DR.RAHUL PATEL'), ('Dr.Karan Patel', 'DR.KARAN PATEL')], default='Dr.Karan Patel', max_length=30),
        ),
    ]

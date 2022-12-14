# Generated by Django 4.1.2 on 2022-11-07 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(max_length=30)),
                ('l_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('designation', models.CharField(max_length=30)),
                ('education', models.CharField(max_length=30)),
                ('exp', models.CharField(max_length=30)),
            ],
        ),
    ]

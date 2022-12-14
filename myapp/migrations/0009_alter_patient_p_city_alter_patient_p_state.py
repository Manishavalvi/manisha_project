# Generated by Django 4.1.2 on 2022-11-08 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_patient'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='p_city',
            field=models.CharField(choices=[('Surat 1', 'SURAT 1'), ('Tirupur 2', 'TIRUPUR 2'), ('Pune 3', 'PUNE 3'), ('Jaipur 4', 'JAIPUR 4'), ('Bhopal 5', 'BHOPAL 5')], default='select', max_length=15),
        ),
        migrations.AlterField(
            model_name='patient',
            name='p_state',
            field=models.CharField(choices=[('Gujarat', 'GUJARAT'), ('Tamilnadu', 'TAMILNADU'), ('Maharashtra', 'MAHARASHTRA'), ('Rajasthan', 'RAJASTHAN'), ('Madhya Pradesh', 'MADHYA PRADESH')], default='select', max_length=15),
        ),
    ]

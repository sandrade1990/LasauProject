# Generated by Django 4.0.5 on 2022-10-13 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bibliotecaApp', '0002_rename_vehiculos_vehiculo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehiculo',
            name='created',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='updated',
            field=models.DateField(),
        ),
    ]

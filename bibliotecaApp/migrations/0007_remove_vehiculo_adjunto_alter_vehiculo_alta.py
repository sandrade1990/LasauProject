# Generated by Django 4.0.5 on 2022-10-14 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bibliotecaApp', '0006_rename_creación_vehiculo_alta_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vehiculo',
            name='Adjunto',
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='Alta',
            field=models.DateField(auto_now_add=True),
        ),
    ]

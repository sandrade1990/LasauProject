# Generated by Django 4.0.5 on 2022-10-26 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bibliotecaApp', '0008_vehiculo_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehiculo',
            name='Version',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]

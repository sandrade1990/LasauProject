# Generated by Django 4.0.5 on 2022-10-15 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bibliotecaApp', '0007_remove_vehiculo_adjunto_alter_vehiculo_alta'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehiculo',
            name='File',
            field=models.FileField(default=0, upload_to='vehiculos'),
            preserve_default=False,
        ),
    ]
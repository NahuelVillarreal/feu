# Generated by Django 4.0.4 on 2022-07-15 12:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('servicios', '0003_remove_servicios_dni_propietario_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='involucrados',
            old_name='tel_propietario',
            new_name='tel',
        ),
    ]
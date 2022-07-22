# Generated by Django 4.0.4 on 2022-07-22 03:32

import datetime
from django.db import migrations, models
import sistema.models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0003_unidades_activa'),
    ]

    operations = [
        migrations.CreateModel(
            name='Documentacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('fecha_publicacion', models.DateField(default=datetime.datetime(2022, 7, 22, 3, 32, 47, 520464), verbose_name='Fecha publicación')),
                ('tipo', models.CharField(choices=[('M', 'MODULOS'), ('C', 'CAPACITACIÓN'), ('O', 'ÓRDENES INTERNAS'), ('D', 'OTRO')], max_length=1)),
                ('archivo', models.FileField(upload_to=sistema.models.path_documentacion)),
            ],
            options={
                'verbose_name': 'Documentación',
                'verbose_name_plural': 'Documentación',
            },
        ),
    ]
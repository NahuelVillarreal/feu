# Generated by Django 4.0.4 on 2022-07-21 15:52

from django.db import migrations, models
import usuarios.models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0037_cursos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personal',
            name='foto_perfil',
            field=models.ImageField(blank=True, default='../media/fotos-perfil/firefighter.png', null=True, upload_to=usuarios.models.path_fotos),
        ),
    ]

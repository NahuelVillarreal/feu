# Generated by Django 4.0.4 on 2022-07-07 15:43

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0021_alter_puntajes_persona'),
    ]

    operations = [
        migrations.CreateModel(
            name='GruposGuardia',
            fields=[
                ('grupo', models.IntegerField(choices=[(1, 'GRUPO 1'), (2, 'GRUPO 2'), (3, 'GRUPO 4'), (4, 'GRUPO 4')], primary_key=True, serialize=False)),
                ('miembros', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Grupo',
                'verbose_name_plural': 'Grupos',
            },
        ),
    ]
# Generated by Django 4.0.4 on 2022-07-07 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0016_alter_puntajes_persona'),
    ]

    operations = [
        migrations.AlterField(
            model_name='puntajes',
            name='mes',
            field=models.IntegerField(choices=[(1, 'ENERO'), (2, 'FEBRERO'), (3, 'MARZO'), (4, 'ABRIL'), (5, 'MAYO'), (6, 'JUNIO'), (7, 'JULIO'), (8, 'AGOSTO'), (9, 'SEPTIEMBRE'), (10, 'OCTUBRE'), (11, 'NOVIEMBRE'), (12, 'DICIEMBRE')], default=7, unique=True),
        ),
    ]

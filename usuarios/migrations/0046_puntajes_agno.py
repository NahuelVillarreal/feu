# Generated by Django 4.0.4 on 2022-08-04 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0045_sanciones_fecha_alter_puntajes_mes'),
    ]

    operations = [
        migrations.AddField(
            model_name='puntajes',
            name='agno',
            field=models.IntegerField(default=2022),
        ),
    ]

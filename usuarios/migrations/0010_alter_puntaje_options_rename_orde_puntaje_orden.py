# Generated by Django 4.0.4 on 2022-07-07 01:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0009_puntaje'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='puntaje',
            options={'verbose_name': 'Puntaje', 'verbose_name_plural': 'Puntajes'},
        ),
        migrations.RenameField(
            model_name='puntaje',
            old_name='orde',
            new_name='orden',
        ),
    ]

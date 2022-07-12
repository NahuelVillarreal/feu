# Generated by Django 4.0.4 on 2022-07-12 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicios', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asistencias',
            name='motivo',
            field=models.CharField(blank=True, choices=[('A', 'ASISTENCIA'), ('C', 'CAPACITACIÓN'), ('D', 'CEREMONIAS'), ('O', 'OTROS')], max_length=1),
        ),
    ]
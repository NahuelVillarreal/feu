# Generated by Django 4.0.4 on 2022-07-08 22:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0024_remove_gruposguardia_miembros_gruposguardia_miembros'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='puntajes',
            name='persona',
        ),
        migrations.AddField(
            model_name='personal',
            name='puntajes',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='usuarios.puntajes'),
        ),
    ]
# Generated by Django 4.0.4 on 2022-07-03 01:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0004_remove_puntaje_persona_personal_puntaje_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personal',
            name='puntaje',
        ),
        migrations.AddField(
            model_name='puntaje',
            name='persona',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

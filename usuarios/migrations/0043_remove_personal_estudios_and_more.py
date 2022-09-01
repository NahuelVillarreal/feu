# Generated by Django 4.0.4 on 2022-07-27 11:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import usuarios.models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0042_alter_personal_estado_civil'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personal',
            name='estudios',
        ),
        migrations.AlterField(
            model_name='cursos',
            name='t_finalizacion_curso',
            field=models.DateTimeField(verbose_name='Finalización'),
        ),
        migrations.AlterField(
            model_name='cursos',
            name='t_inicio_curso',
            field=models.DateTimeField(verbose_name='Inicio'),
        ),
        migrations.CreateModel(
            name='Estudios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estudio', models.FileField(upload_to=usuarios.models.path_estudios)),
                ('fecha_subida', models.DateField()),
                ('persona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Estudio médico',
                'verbose_name_plural': 'Estudios médicos',
            },
        ),
    ]
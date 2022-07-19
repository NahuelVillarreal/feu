# Generated by Django 4.0.4 on 2022-07-19 14:06

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0036_alter_personal_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cursos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('t_inicio_curso', models.DateTimeField()),
                ('t_finalizacion_curso', models.DateTimeField()),
                ('metodologia', models.CharField(choices=[('P', 'PRESENCIAL'), ('V', 'VIRTUAL'), ('M', 'MIXTO')], max_length=1)),
                ('participantes', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Curso',
                'verbose_name_plural': 'Cursos',
            },
        ),
    ]

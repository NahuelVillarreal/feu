# Generated by Django 4.0.4 on 2022-06-30 15:15

from django.db import migrations, models
import usuarios.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Personal',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('correo', models.EmailField(blank=True, max_length=100, null=True, unique=True, verbose_name='correo electrónico')),
                ('documento', models.IntegerField(blank=True, null=True)),
                ('fecha_nacimiento', models.DateField(blank=True, null=True)),
                ('lugar_nacimiento', models.CharField(blank=True, max_length=50)),
                ('sexo', models.CharField(blank=True, choices=[('M', 'MASCULINO'), ('F', 'FEMENINO'), ('O', 'OTRO')], max_length=9)),
                ('grupo_sanguineo', models.CharField(blank=True, choices=[('O-', 'O NEGATIVO'), ('O+', 'O POSITIVO'), ('A-', 'A NEGATIVO'), ('A+', 'A POSITIVO'), ('B-', 'B NEGATIVO'), ('B+', 'B POSITIVO'), ('AB-', 'AB NEGATIVO'), ('AB+', 'AB POSITIVO')], max_length=20)),
                ('foto_perfil', models.ImageField(blank=True, null=True, upload_to=usuarios.models.path_fotos)),
                ('estudios', models.FileField(blank=True, null=True, upload_to=usuarios.models.path_estudios)),
                ('matricula', models.CharField(max_length=5, primary_key=True, serialize=False, unique=True)),
                ('cuerpo', models.CharField(blank=True, choices=[('A', 'ACTIVO'), ('R', 'RESERVA'), ('I', 'INACTIVO'), ('O', 'OTRO')], max_length=20)),
                ('jerarquia', models.CharField(blank=True, choices=[('AS', 'ASPIRANTE'), ('BO', 'BOMBERO'), ('SS', 'SUBOF. SUBAYUDANTE'), ('SA', 'SUBOF. AYUDANTE'), ('SA1', 'SUBOF. AYUDANTE DE 1RA'), ('SAP', 'SUBOF. AYUDANTE PRINCIPAL'), ('SAM', 'SUBOF. AYUDANTE MAYOR'), ('O3', 'OF. 3ERO'), ('O2', 'OF. 2DO'), ('O1', 'OF. 1ERO'), ('SC', 'SUBCOMANDANTE'), ('C', 'COMANDANTE'), ('CM', 'COMANDANTE MAYOR'), ('CG', 'COMANDANTE GENERAL')], max_length=20)),
                ('seccion', models.CharField(blank=True, choices=[('JE', 'JEFATURA'), ('EQ', 'EQUIPOS'), ('AU', 'AUTOMOTORES'), ('PE', 'PERSONAL'), ('OT', 'OTROS')], max_length=20)),
                ('fecha_alta', models.DateField(blank=True, null=True)),
                ('cantidad_toques', models.IntegerField(default=0, null=True)),
                ('active', models.BooleanField(default=True, verbose_name='Activo')),
                ('staff', models.BooleanField(default=False)),
                ('admin', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Miembro',
                'verbose_name_plural': 'Miembros',
            },
        ),
    ]

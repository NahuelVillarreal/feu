# Generated by Django 4.0.4 on 2022-07-15 23:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0032_alter_personal_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='gruposguardia',
            options={'ordering': ('miembros__jerarquia',), 'verbose_name': 'Grupo', 'verbose_name_plural': 'Grupos'},
        ),
        migrations.AlterModelOptions(
            name='personal',
            options={'verbose_name': 'Miembro', 'verbose_name_plural': 'Miembros'},
        ),
    ]

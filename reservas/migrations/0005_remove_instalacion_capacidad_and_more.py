# Generated by Django 4.1.5 on 2023-02-18 15:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservas', '0004_alter_reserva_productos'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='instalacion',
            name='capacidad',
        ),
        migrations.RemoveField(
            model_name='instalacion',
            name='equipo_incluido',
        ),
        migrations.RemoveField(
            model_name='instalacion',
            name='indumentaria',
        ),
        migrations.RemoveField(
            model_name='instalacion',
            name='recomendaciones',
        ),
    ]

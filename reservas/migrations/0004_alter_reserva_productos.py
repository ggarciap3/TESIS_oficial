# Generated by Django 4.1.5 on 2023-02-17 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservas', '0003_alter_reserva_presentaciones_alter_reserva_productos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='Productos',
            field=models.IntegerField(choices=[(0, '..........'), (1, 'Azucar Blanca'), (2, 'Azucar Morena'), (3, 'Azucar Ligero'), (4, 'Azucar Turbinado'), (5, 'Azucar Blanco Organico'), (6, 'Azucar De Coco Organico'), (7, 'Panela'), (8, 'Steviazucar Blanca'), (9, 'Steviazucar Morena'), (10, 'Stevia Panela')]),
        ),
    ]
# Generated by Django 4.1.5 on 2023-02-01 04:49

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Disiplina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=10, unique=True)),
                ('estado', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Instalacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30, unique=True)),
                ('descripcion', models.CharField(max_length=200)),
                ('restriciones', models.CharField(max_length=200)),
                #('precio', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                #('capacidad', models.CharField(max_length=10)),
                ('imagen', models.ImageField(upload_to='imagenes/instalaciones/%Y/%m/%d/')),
                #('indumentaria', models.CharField(max_length=200)),
                ('recomendaciones', models.CharField(max_length=200)),
                #('equipo_incluido', models.CharField(max_length=200)),
                ('estado', models.BooleanField(default=True)),
                ('id_diciplina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservas.disiplina')),
            ],
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=30)),
                ('apellidos', models.CharField(max_length=30)),
                ('cedula', models.CharField(max_length=10)),
                ('email', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=10)),
                ('fecha_creacion', models.DateField(default=datetime.datetime.now)),
                ('fecha_compra', models.DateField()),
                ('codigo_qr', models.CharField(max_length=255, unique=True)),
                ('cantidad', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('Presentaciones', models.IntegerField(choices=[ [0,'Stick Packs'],[1,'500g'],[2,'1kg'],[3,'2kg'],[4,'5kg'], [5,'10kg'], [6,'25kg'], [7,'50kg']])),
                ('Productos', models.IntegerField(choices=[[0,'Azucar Blanca'],[1,'Azucar Morena'],[2,'Azucar Ligero'],[3,'Azucar Turbinado'],[4,'Azucar Blanco Organico'],[5,'Azucar De Coco Organico'],[6,'Panela'],[7,'Steviazucar Blanca'],[8,'Steviazucar Morena'],[9,'Stevia Panela']])),
                ('estado', models.BooleanField(default=True)),
                ('id_instalacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservas.instalacion')),
            ],
        ),
    ]

# Generated by Django 4.2.5 on 2023-09-18 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoderYanaina', '0002_reserva_servicio_delete_cliente_reserva_servicio'),
    ]

    operations = [
        migrations.CreateModel(
            name='Perro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('raza', models.CharField(max_length=100)),
                ('edad', models.PositiveIntegerField()),
                ('dueño', models.CharField(max_length=100)),
                ('fecha_registro', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='reserva',
            name='apellido_cliente',
        ),
    ]

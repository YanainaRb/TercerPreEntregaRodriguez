from django.db import models

# Create your models here.

class Servicio(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=6, decimal_places=2)

class Reserva(models.Model):
    nombre_cliente = models.CharField(max_length=100)
    celular = models.CharField(max_length=15)
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    fecha_reserva = models.DateTimeField(auto_now_add=True)

class Perro(models.Model):
    nombre = models.CharField(max_length=100)
    raza = models.CharField(max_length=100)
    edad = models.PositiveIntegerField()
    dueño = models.CharField(max_length=100)
    fecha_registro = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nombre

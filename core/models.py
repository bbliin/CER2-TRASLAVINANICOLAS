from django.db import models
from datetime import date
from django.contrib.auth.models import User
class Solicitud(models.Model):
    estados=[
        ('P', 'Pendiente'),
        ('ER', 'En ruta'),
        ('C','Completada'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tipomat = models.CharField(max_length=100)
    cantidad = models.CharField(max_length=100)
    fecha = models.DateField(default="2025-01-01")
    estado = models.CharField(max_length=20, choices=estados, default='P')
    comentario = models.CharField(max_length=100, default="Sin comentario")

    operario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='asignadas')

    def __str__(self):
        return f"{self.user.username} - {self.tipomat} - {self.fecha}"

class TipoMaterial(models.Model):

    codigo = models.CharField(max_length=10, unique=True)
    tipomat = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=100, default="Sin descripcion")
    def __str__(self):
        return f"{self.codigo} - {self.tipomat}"

 
class puntitos(models.Model):
    nombre = models.CharField(max_length=100, default="Sin nombre")
    direccion = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)
    region = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre} - {self.ciudad}"

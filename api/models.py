from django.db import models
from django.contrib.auth.models import User

class Ubicacion(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=255)
    latitud = models.FloatField()
    longitud = models.FloatField()

    def __str__(self):
        return self.nombre

class Actividad(models.Model):
    TIPO_CHOICES = [
        ('aire_libre', 'Aire Libre'),
        ('interior', 'Interior'),
    ]
    
    ubicacion = models.ForeignKey(Ubicacion, on_delete=models.CASCADE, related_name='actividades')
    descripcion = models.TextField()
    fecha = models.DateField()
    horario = models.TimeField()
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    condiciones_clima_ideales = models.CharField(max_length=255) # Ej: "Despejado"
    completada = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.descripcion} en {self.ubicacion.nombre}"
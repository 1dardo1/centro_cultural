from django.db import models

class Monitor(models.Model):
    nombre = models.CharField(max_length=100)
    especializacion = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class UsuarioInscrito(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()
    email = models.EmailField()
    telefono = models.CharField(max_length=15)

    def __str__(self):
        return self.nombre

class ResponsableSala(models.Model):
    nombre = models.CharField(max_length=100)
    contacto = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Sala(models.Model):
    nombre = models.CharField(max_length=50)
    capacidad = models.IntegerField()
    ubicacion = models.CharField(max_length=100)
    responsable = models.OneToOneField(ResponsableSala, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Actividad(models.Model):
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50)
    horario = models.DateTimeField()
    descripcion = models.TextField()
    duracion = models.DurationField()
    plazas_disponibles = models.IntegerField()
    monitor = models.ForeignKey(Monitor, on_delete=models.CASCADE)
    usuarios = models.ManyToManyField(UsuarioInscrito, blank=True)
    sala_principal = models.ForeignKey(Sala, on_delete=models.CASCADE, related_name='actividades_principales')

    def __str__(self):
        return self.nombre

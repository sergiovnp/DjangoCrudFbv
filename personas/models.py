from django.db import models

# Create your models here.
class Persona(models.Model):
    nombre = models.CharField(max_length=30, verbose_name="Nombre")
    apellido = models.CharField(max_length=30, verbose_name="Apellido")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Creado")
    updated = models.DateTimeField(auto_now=True, verbose_name="Editado")

    class Meta:
        verbose_name = "Personas"
        verbose_name_plural = "Personas"

    def __str__(self):
        return self.nombre

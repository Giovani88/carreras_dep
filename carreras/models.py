from django.db import models

# Create your models here.
class Carreras(models.Model): # Se Crea en dep_alumnos la tabla para evitar la importacion circular
    
    nombre = models.CharField(max_length=100)
    clave = models.CharField(max_length=100)
    plan_estudios = models.CharField(max_length=100)
    is_active = models.BooleanField(blank=False)

    class Meta:
        db_table = 'carreras'
        verbose_name_plural = "Carreras"           

    def __str__(self):
        return f'{self.nombre}'
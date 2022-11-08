from tabnanny import verbose
from django.db import models

# Create your models here.

class Servicio(models.Model):
    titulo = models.CharField(max_length= 50)
    Contenido = models.CharField(max_length = 1000)
    imagen = models.ImageField(upload_to = 'servicios')
    created = models.DateField(auto_now_add = True)
    updated = models.DateField(auto_now_add = True)

    def __str__ (self):
        return str(self.imagen)

    class meta:
        verbose_name='servicio'
        verbose_name_plural = 'servicios'
    
    def __str__ (self):
        return self.titulo

   


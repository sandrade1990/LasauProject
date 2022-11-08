from msilib.schema import File
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class LasauPlanta(models.Model):

    Sector = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return (self.Sector)


class Vehiculo(models.Model):
    Nombre = models.CharField(max_length = 200, unique=True, error_messages={'Invalido': 'El registro ya existe!'})
    Sector = models.ForeignKey('LasauPlanta', null=True, blank=True, on_delete=models.CASCADE)
    Alta = models.DateField(auto_now_add = True)
    Revision = models.DateField()
    Version = models.IntegerField()
    Estado = models.CharField(max_length = 50)
    Codigo = models.CharField(max_length = 50)
    File = models.FileField(upload_to = 'vehiculos')

    def delete(self, *args, **kwargs): #Funcion para eliminar los archivos en la carpeta de almacenaje
        self.File.delete()
        super().delete(*args, **kwargs)
  
    def __str__ (self):
        return str(self.File)

    def save(self, *args, **kwargs): #Función para actualizar los archivos en la carpeta de almacenaje
        try:
            this = Vehiculo.objects.get(id = self.id)
            if this.File != self.File:
                this.File.delete(save=False)
        except:
            pass  # when new photo then we do nothing, normal case
        super().save(*args, **kwargs)

    class meta:
        verbose_name='vechiculo'
        verbose_name_plural = 'vechiculos'
    
    def __str__ (self):
        return self.Nombre


    
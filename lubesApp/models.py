from django.db import models

# Create your models here.
class Load(models.Model):
    
    name=models.CharField(max_length = 40)
    description = models.CharField(max_length =100)
    initdate = models.DateField()
    revisiondate = models.DateField()
    statusChoices = [
        ('ACT','Activo'),
        ('REV','Revisión'),
        ('OBS','Obsoleto'),
    ]
    status = models.CharField(max_length = 40, choices=statusChoices, default="ACT")
    file=models.FileField()


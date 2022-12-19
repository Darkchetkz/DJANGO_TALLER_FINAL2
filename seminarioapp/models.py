from django.db import models

# Create your models here.
est = [
    ('reserva','RESERVA'),
    ('completo','COMPLETo'),
    ('anuladar','ANULADAR'),
    ('no asisten','NO ASISTEN')
]

class Inscripciones(models.Model):
    Fec_inscripcion  = models.DateField()
    hora  = models.TimeField()
    Institucion  = models.CharField(max_length=30)
    rutP   = models.CharField(max_length=12)  
    nombrep  = models.CharField(max_length=30)
    Num_telefono  = models.IntegerField()
    Est_reserva = models.CharField(max_length = 30,choices = est)
    Observaciones = models.TextField(blank=True)

class Instituciones(models.Model):
    rutp  = models.CharField(max_length=30) 
    nombrep = models.CharField(max_length=30) 
from django.db import models

# Create your models here.

class Curso(models.Model):
    nombre=models.CharField(max_length=40)
    inicio=models.IntegerField()
    duracion=models.IntegerField()
    costo=models.IntegerField()
   

class Profesores(models.Model):
    nombre=models.CharField(max_length=40)
    asignatura=models.CharField(max_length=40)
    cargo=models.CharField(max_length=40)
    actividad=models.IntegerField()
    

class Egresados(models.Model):
    nombre=models.CharField(max_length=40)
    titulacion=models.CharField(max_length=40)
    graduacion=models.IntegerField()
    promedio=models.FloatField()
  


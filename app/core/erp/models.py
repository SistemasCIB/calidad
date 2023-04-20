
from django.db import models
from datetime import datetime

from django.forms import model_to_dict

from app.settings import MEDIA_URL, STATIC_URL

from core.models import BaseModel
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre', unique=True)
    desc = models.CharField(max_length=500, null=True, blank=True, verbose_name='Descripción')

    def __str__(self):
        return self.name

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['id']



class Plan(models.Model):
    
    dni = models.CharField(max_length=10, unique=True, verbose_name='Dni')
    cate = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=150, verbose_name='Nombre', unique=True)
    descripcionProblema = models.CharField(max_length=300, verbose_name=' Descripcion del Problema', unique=True)
   
    clasificacion = models.CharField(max_length=300, verbose_name='clasificacion', unique=True)
    normaIncumplida = models.CharField(max_length=300, verbose_name=' normaIncumplida', unique=True)
    tipoAccion = models.CharField(max_length=300, verbose_name='tipoAccion', unique=True)
    fuentePlan = models.CharField(max_length=300, verbose_name='fuentePlan', unique=True)
    entidad = models.CharField(max_length=300, verbose_name='entidad', unique=True)
    proceso = models.CharField(max_length=300, verbose_name='proceso', unique=True)
    tratamientoInmediato = models.CharField(max_length=300, verbose_name='tratamientoInmediato', unique=True)
    evidencia = models.CharField(max_length=300, verbose_name=' evidencia', unique=True)
    analisisCausa= models.CharField(max_length=300, verbose_name='  analisisCausa', unique=True)
    causaRaiz = models.CharField(max_length=300, verbose_name=' causaRaiz', unique=True)
    estado = models.CharField(max_length=300, verbose_name='estado', unique=True)
    image = models.ImageField(upload_to='imagen/%Y/%m/%d', null=True, blank=True)
    archivo = models.FileField(upload_to='imagen/%Y/%m/%d', null=True, blank=True)
    date_creation = models.DateTimeField(auto_now=True)
    date_update = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Plan'
        verbose_name_plural = 'Planes'
        ordering = ['id']


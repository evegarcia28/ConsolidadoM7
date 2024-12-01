import datetime
from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.
class Laboratorio(models.Model):
    nombre = models.CharField(max_length=200)
    ciudad =models.CharField(max_length=100, default='')
    pais = models.CharField(max_length=100, default='')
    
    def __str__(self):
        return self.nombre
    
class DirectorGeneral(models.Model):
    nombre = models.CharField(max_length=200)
    laboratorio=models.OneToOneField(Laboratorio, on_delete=models.CASCADE)
    especialidad = models.CharField(max_length=100, default='General')
    
    def __str__(self):
        return f' El {self.nombre} pertenece a: {self.laboratorio}'
    
class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    laboratorio=models.ForeignKey(Laboratorio, on_delete=models.CASCADE)
    f_fabricacion=models.DateField(validators=[MinValueValidator(datetime.date(2015,1,1))], verbose_name="F Fabricacion")
    p_costo=models.DecimalField(max_digits=10, decimal_places=2)
    p_venta=models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f' El {self.nombre} pertenece al {self.laboratorio} con fecha de fabricacion: {self.f_fabricacion}, con costo de:$ {self.p_costo} y precio de venta: $ {self.p_venta}'
    
    
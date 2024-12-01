from datetime import datetime
from django.contrib import admin
from .models import Laboratorio, DirectorGeneral, Producto
from django import forms


# Register your models here.
@admin.register(Laboratorio)
class LaboratorioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')
    
@admin.register(DirectorGeneral)
class DirectorGeneralAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'laboratorio')


class ProductoForm(forms.ModelForm):
    f_fabricacion = forms.DateField(
        widget=forms.SelectDateWidget(
            years=range(2015, datetime.now().year + 1)
        ),
        label="F Fabricacion"
    )

    class Meta:
        model = Producto
        fields = '__all__'
    
@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    form = ProductoForm
    list_display = ('id', 'nombre', 'laboratorio', 'get_f_fabricacion', 'p_costo', 'p_venta')
    
    def get_f_fabricacion(self, obj):
        return obj.f_fabricacion.year  # Mostrar solo el año en la lista
    get_f_fabricacion.short_description = 'F Fabricacion'  # Nombre de la columna en el admin

